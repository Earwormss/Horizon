# 在其他 Windows 设备部署 Horizon

这个分支保存了 2026-08-05 的本地优化和安全配置模板，但不包含任何 API Key、`.env`、运行记录或已生成的日报。

## 一键部署

1. 安装 Git，然后打开命令提示符运行：

   ```bat
   git clone https://github.com/Earwormss/Horizon.git
   cd Horizon
   install-horizon.cmd
   ```

2. 安装结束后，打开项目根目录的 `.env`，填写：

   ```dotenv
   DEEPSEEK_API_KEY=你的密钥
   ```

3. 双击 `run-horizon.cmd`。日报保存在 `data\summaries`。

安装脚本会自动安装 `uv`、Python 3.12、项目依赖，并在首次安装时把 `data\config.local.example.json` 复制为本机的 `data\config.json`。已有的 `.env` 和 `data\config.json` 不会被覆盖。

## 已保存的主要设定

- DeepSeek `deepseek-chat`
- AI 请求超时 60 秒
- 单条背景富化超时 180 秒
- 背景富化并发数 2
- 中英双语 Markdown；每条英文后紧跟对应中文
- DDGS 搜索使用独立子进程和 15 秒硬超时，避免 Windows 控制台卡死
- AI 富化结果有 JSON 校验、重试和格式修复

## 更新代码

以后在项目目录运行：

```bat
git pull
```

代码更新不会上传或覆盖本机的 `.env`、`data\config.json` 和 `data\summaries`。
