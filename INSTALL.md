# 安装说明

## MCP 地址

```text
https://leor.cn/agent-test/mcp
```

当前地址为公开测试入口。后续如 LEOR 切换正式 Agent 域名，请以 https://leor.cn/agent 公布的信息为准。

## 通用连接步骤

1. 打开你的 Agent 工具。
2. 找到 MCP、工具、插件、外部服务或自定义工具配置入口。
3. 新增一个 MCP 服务，名称建议填写：

```text
LEOR AI展台设计 Agent
```

4. MCP 地址填写：

```text
https://leor.cn/agent-test/mcp
```

5. 保存后，在 Agent 对话中输入：

```text
连接我的 LEOR 账号
```

6. 打开返回的 LEOR 授权链接，登录并确认授权。
7. 回到 Agent 对话继续使用。

## 支持工具

公开口径中已确认支持或计划适配的 Agent 工具包括：

- Codex
- Claude Code
- OpenClaw
- WorkBuddy
- QClaw

其他支持 MCP 或外部工具调用的 Agent 环境，也可以按通用连接步骤尝试接入。

## 常见问题

### 授权失败怎么办？

让 Agent 重新调用连接工具，或直接对 Agent 说：

```text
重新连接我的 LEOR 账号
```

不要让普通用户复制 token、查看 `.env`、检查本地源码或修改 MCP 服务代码。

### 图片一定要 URL 吗？

不一定。对于支持图片附件的 Agent，用户可以直接在对话中发送 JPG、PNG 或 WEBP 图片。Agent 应把图片作为当前任务输入交给 LEOR，不要要求普通用户自己找图床或转换 base64。

### 生成几张图？

LEOR Agent 默认每次只生成 1 张。若用户需要多张，应该一张一张生成，每次都让用户确认是否继续。
