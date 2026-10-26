# LEOR AI展台设计 Agent

LEOR AI展台设计 Agent 是 LEOR（leor.cn）提供的 AI 展台设计 Agent 连接入口。它支持 Codex、Claude Code、OpenClaw、WorkBuddy、QClaw 等 Agent 工具，让 AI 通过对话调用 LEOR 完成展台设计、生图、改图和项目资产保存。

其他支持 MCP 或外部工具调用的 Agent 环境，也可以按说明接入 LEOR。

## 官方入口

- 官网说明页：https://leor.cn/agent
- 正式 MCP 地址：https://mcp.leor.cn/mcp
- GitHub 文档仓库：https://github.com/YonGs-AI/leor-ai-booth-design-agent
- Official MCP Registry 名称：`io.github.YonGs-AI/leor-ai-booth-design-agent`
- Smithery 页面：https://smithery.ai/servers/yongwah2026/leor-ai-booth-design-agent
- ModelScope 魔搭页面：https://modelscope.cn/mcp/servers/yongwah/leor-ai-booth-design-agent
- 扣子插件：`LEORAIAgent`（插件 ID：`7658391373665681442`，已发布）
- LEOR 官网：https://leor.cn/

## 它能做什么

- 生成 AI 展台设计图和展示效果图。
- 参考图可以是展位，也可以是建筑、展厅、店铺等空间图片。
- 使用完整展位参考图时，更准确地保留整体造型和设计风格；使用建筑等非展位参考图时，把有辨识度的空间造型语言转化为展位设计。
- 优化/改图支持一张目标图加最多三张参考图，可用于换 Logo、替换产品或柜体、借用局部造型、材质、布局和风格等组合任务。
- 用动物、产品、颜色、材质、Logo 等图片做“万物成展”创意推导。
- 修改已有展台图片。
- 把已有草图、CAD 截图或普通平面图重绘成三种专业提案平面图。
- 制作海报、PPT 页面、展板、封面、宣传页、信息图、导视等专业平面设计。
- 在不改展位结构和视角的前提下，把完整模型切换成六种渲染表现。
- 生成材质板、展位分镜、潮流海报、简约海报、玻璃质感海报。
- 对已有展台图做旋转视角。
- 查询 LEOR 账号积分和任务结果。
- 将结果保存到授权用户自己的 LEOR 项目资产中。

## 快速连接

1. 在 Codex、Claude Code、OpenClaw、WorkBuddy、QClaw 或其他支持 MCP 的 Agent 工具中添加 MCP 服务。
2. 填入 MCP 地址：

```text
https://mcp.leor.cn/mcp
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
- 多图改图时，要说明哪张是需要修改的目标图，以及每张参考图分别用在哪里、替换什么、哪些内容不要照搬。
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
- [专项能力使用说明](CAPABILITY-GUIDE.md)
- [示例提问](EXAMPLES.md)
- [版本记录](CHANGELOG.md)
- [安全说明](SECURITY.md)
