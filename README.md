# LEOR AI展台设计 Agent

LEOR AI展台设计 Agent 是 LEOR（leor.cn）提供的 AI 展台设计 Agent 连接入口。它支持 Codex、Claude Code、OpenClaw、WorkBuddy、QClaw 等 Agent 工具，让 AI 通过对话调用 LEOR 完成展台设计、生图、改图和项目资产保存。

其他支持 MCP 或外部工具调用的 Agent 环境，也可以按说明接入 LEOR。

## 官方入口

- 官网说明页：https://leor.cn/agent
- 当前公开测试 MCP 地址：https://leor.cn/agent-test/mcp
- LEOR 官网：https://leor.cn/

## 它能做什么

- 生成 AI 展台设计图和展示效果图。
- 使用 Logo、参考图、灵感广场案例辅助生成。
- 用动物、产品、颜色、材质、Logo 等图片做“万物成展”创意推导。
- 修改已有展台图片。
- 生成材质板、展位分镜、潮流海报、简约海报、玻璃质感海报。
- 对已有展台图做旋转视角。
- 查询 LEOR 账号积分和任务结果。
- 将结果保存到授权用户自己的 LEOR 项目资产中。

## 快速连接

1. 在 Codex、Claude Code、OpenClaw、WorkBuddy、QClaw 或其他支持 MCP 的 Agent 工具中添加 MCP 服务。
2. 填入 MCP 地址：

```text
https://leor.cn/agent-test/mcp
```

3. 对 Agent 说：

```text
连接我的 LEOR 账号
```

4. 打开 Agent 返回的 LEOR 授权链接，登录 LEOR 并确认授权。
5. 回到 Agent 对话，让它帮你收集展台设计资料并调用 LEOR。

普通用户不需要复制 token，不需要查看 `.env`，也不需要修改本地代码。

## 重要使用规则

- 做展台设计图前，Agent 应先收集完整展台资料。
- Logo 强烈建议上传，参考图建议上传。
- 扣积分前，Agent 应汇总需求并等待用户明确确认。
- 默认每次只生成 1 张图。
- 如果用户只是想找灵感、找参考图或看案例，Agent 不应该直接调用生图工具。
- 生成结果归属当前授权的 LEOR 账号。

## 公开安全承诺

- LEOR Agent 需要用户登录 LEOR 并确认授权。
- 扣积分功能消耗当前授权账号积分。
- 结果保存到当前授权账号的 LEOR 项目。
- LEOR 不会向 Agent 暴露核心提示词、模型密钥、内部路由、后台路径或提示词资产。

## 文档

- [安装说明](INSTALL.md)
- [示例提问](EXAMPLES.md)
- [版本记录](CHANGELOG.md)
- [安全说明](SECURITY.md)
- [目录提交资料](REGISTRY-SUBMISSION.md)
- [中文推广素材](CONTENT-KIT.md)
- [宣传素材交接说明](marketing/HANDOFF.md)
