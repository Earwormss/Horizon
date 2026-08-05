"""Built-in tools available to enrichment blocks."""

import asyncio
import json
import os
import subprocess
import sys
from dataclasses import dataclass
import logging
from typing import Any

logger = logging.getLogger(__name__)


_DDGS_SEARCH_SCRIPT = r"""
import json
import logging
import sys

logging.disable(logging.CRITICAL)
from ddgs import DDGS

results = DDGS().text(sys.argv[1], max_results=int(sys.argv[2]))
sys.stdout.buffer.write(
    json.dumps(results or [], ensure_ascii=False).encode("utf-8")
)
"""


@dataclass(frozen=True)
class ToolResult:
    request_id: str
    block_id: str
    tool: str
    results: list[dict[str, str]]


class WebSearchTool:
    name = "web_search"

    def __init__(self, timeout_sec: float = 15.0):
        self.timeout_sec = max(timeout_sec, 0.01)

    async def execute(self, arguments: dict[str, Any]) -> list[dict[str, str]]:
        query = arguments.get("query")
        if not isinstance(query, str) or not query.strip():
            raise ValueError("web_search requires a non-empty query")

        process = None
        try:
            child_env = os.environ.copy()
            child_env["PYTHONUTF8"] = "1"
            creationflags = (
                subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
            )
            process = await asyncio.create_subprocess_exec(
                sys.executable,
                "-c",
                _DDGS_SEARCH_SCRIPT,
                query.strip(),
                "3",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=child_env,
                creationflags=creationflags,
            )
            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=self.timeout_sec,
            )
            if process.returncode != 0:
                detail = stderr.decode("utf-8", errors="replace").strip()[:500]
                logger.warning("web_search failed for %r: %s", query, detail)
                return []
            raw = json.loads(stdout.decode("utf-8"))
        except asyncio.TimeoutError:
            if process and process.returncode is None:
                process.kill()
                await process.wait()
            logger.warning(
                "web_search timed out after %s seconds for %r",
                self.timeout_sec,
                query,
            )
            return []
        except Exception as exc:
            logger.warning("web_search failed for %r: %s", query, exc)
            return []
        return [
            {
                "title": str(result.get("title", "")),
                "url": str(result.get("href", "")),
                "text": str(result.get("body", "")),
            }
            for result in (raw or [])
            if isinstance(result, dict) and result.get("href")
        ]


class ToolRegistry:
    """Small allowlisted registry for executable profile tools."""

    def __init__(self):
        self._tools = {WebSearchTool.name: WebSearchTool()}

    @property
    def names(self) -> set[str]:
        return set(self._tools)

    async def execute(
        self,
        request_id: str,
        block_id: str,
        tool: str,
        arguments: dict[str, Any],
    ) -> ToolResult:
        try:
            implementation = self._tools[tool]
        except KeyError as exc:
            raise ValueError(f"Unknown enrichment tool: {tool}") from exc
        return ToolResult(
            request_id=request_id,
            block_id=block_id,
            tool=tool,
            results=await implementation.execute(arguments),
        )
