"""Tests for enrichment tools and their process isolation."""

import asyncio
import json

from src.processing.tools import WebSearchTool


class FakeProcess:
    def __init__(self, *, stdout=b"[]", stderr=b"", returncode=0, delay=0):
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode
        self.delay = delay
        self.killed = False

    async def communicate(self):
        if self.delay:
            await asyncio.sleep(self.delay)
        return self.stdout, self.stderr

    def kill(self):
        self.killed = True
        self.returncode = -1

    async def wait(self):
        return self.returncode


def test_web_search_parses_isolated_subprocess_output(monkeypatch):
    payload = [
        {"title": "Result", "href": "https://example.com", "body": "Text"}
    ]
    process = FakeProcess(stdout=json.dumps(payload).encode("utf-8"))

    async def create_process(*args, **kwargs):
        return process

    monkeypatch.setattr(asyncio, "create_subprocess_exec", create_process)
    results = asyncio.run(WebSearchTool().execute({"query": "example"}))

    assert results == [
        {"title": "Result", "url": "https://example.com", "text": "Text"}
    ]


def test_web_search_kills_subprocess_on_timeout(monkeypatch):
    process = FakeProcess(delay=1, returncode=None)

    async def create_process(*args, **kwargs):
        return process

    monkeypatch.setattr(asyncio, "create_subprocess_exec", create_process)
    results = asyncio.run(
        WebSearchTool(timeout_sec=0.01).execute({"query": "stalled"})
    )

    assert results == []
    assert process.killed is True
