# MCP 目录提交资料

## 通用字段

### Name

LEOR AI展台设计 Agent

### Short Description

AI booth design agent connector for LEOR. It lets Codex, Claude Code, OpenClaw, WorkBuddy, QClaw, and other MCP-capable agents call LEOR to generate booth design images, edit booth images, create storyboards and material boards, and save results into the authorized LEOR account.

### 中文描述

LEOR AI展台设计 Agent 支持 Codex、Claude Code、OpenClaw、WorkBuddy、QClaw 等 Agent 工具，让 AI 通过对话调用 LEOR 完成展台设计、生图、改图和项目资产保存。

### Website

https://leor.cn/agent

### MCP Endpoint

https://mcp.leor.cn/mcp

### Transport

Streamable HTTP

### Authentication

OAuth-style LEOR account authorization. Users log in to LEOR and confirm authorization. Normal users do not copy tokens manually.

### Category

Design, Productivity, Image Generation, Exhibition Booth Design

### Keywords

AI展台设计, LEOR AI展台设计 Agent, MCP, 展台设计工具, AI booth design, booth rendering, exhibition design

## Official MCP Registry

已按 2026-07-03 官方文档核对：

- 官方 Registry 支持 `remotes` 类型的远程 MCP 服务。
- Streamable HTTP 是建议的远程传输方式。
- Registry 只保存元数据，不要求 LEOR 把私有网关源码放到 Registry。
- 远程地址必须能从公网访问。
- 正式发布需要使用 `mcp-publisher`，并证明命名空间所有权。

当前已发布条目：

```text
io.github.YonGs-AI/leor-ai-booth-design-agent
```

当前版本：

```text
0.2.1
```

Registry API 验证地址：

```text
https://registry.modelcontextprotocol.io/v0.1/servers/io.github.YonGs-AI%2Fleor-ai-booth-design-agent/versions
```

LEOR 长期建议用域名命名空间：

```text
cn.leor/ai-booth-design-agent
```

GitHub 登录当前可直接发布的命名空间是：

```text
io.github.YonGs-AI/leor-ai-booth-design-agent
```

首版先用 GitHub 命名空间发布，等后续完成 `leor.cn` 域名所有权验证后，再评估迁移或补充域名命名空间。对应的待提交文件见 [`registry/server.json`](registry/server.json)。切换到域名命名空间前需要完成以下两件事：

1. 新的官网 Agent 说明页已经上线。
2. 通过 DNS TXT 或 `/.well-known/mcp-registry-auth` 完成 `leor.cn` 域名所有权验证。

提交时按官方 Registry 当前文档执行域名所有权验证和发布流程。私钥、token 或一次性验证码不得写入 GitHub、文档、聊天或命令历史。

## Smithery

已按 2026-07-03 Smithery 官方文档核对：

- 可在 `https://smithery.ai/new` 直接提交已托管的公开 HTTPS MCP URL。
- 要求 Streamable HTTP；需要账号授权时，服务应提供 OAuth 授权。
- Smithery 会扫描工具元数据。需要授权的服务，提交过程中会要求登录。
- 未授权请求应返回 `401`，不是 `403`，否则扫描可能无法发现 OAuth。
- 如果自动扫描被限制，可在 `/.well-known/mcp/server-card.json` 提供手工元数据，但不应在该文件中泄露内部提示词或安全实现。

当前已发布：

```text
yongwah2026/leor-ai-booth-design-agent
```

页面：

```text
https://smithery.ai/servers/yongwah2026/leor-ai-booth-design-agent
```

Smithery 已扫描到 LEOR MCP server info 和 23 个 tools。resources/prompts 未公开属于预期行为，不作为失败项。

## 其他目录

- mcp.so 等第三方目录只作补充发现渠道。
- 提交字段继续使用本文档的通用字段。
- 如果平台要求公开私有网关源码、内部风控实现或密钥，停止提交。
- 国内可发现渠道优先看：
  - 魔搭 ModelScope MCP 广场。
  - 百度千帆 / 文心智能体 MCP 广场或外部 MCP 接入入口。
  - 扣子 / Coze 的 MCP 插件或自定义 MCP 入口。
  - MCP.so、MCP Hub 中国、Awesome MCP 中文列表等社区目录。
- 国内平台若不能直接提交公开 MCP 服务，先发布“连接教程 + MCP 地址 + 官网说明页”，让 Agent 和用户能按文档添加外部工具。

### MCP.so

- 状态：已提交，等待收录。
- 提交链接：https://github.com/chatmcp/mcpso/issues/2999

## 当前状态

- 提交字段：已准备。
- Official MCP Registry `server.json`：已发布，首版使用 GitHub 命名空间。
- 官网 Agent 说明页：已上线并通过静态抓取检查。
- 域名所有权验证：作为后续升级项，不阻塞 GitHub 命名空间首版发布。
- Smithery 正式发布：已完成。
