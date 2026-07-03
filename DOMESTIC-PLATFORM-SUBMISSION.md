# 国内平台提交与接入资料

本文件用于百度千帆 / 文心智能体、扣子 / Coze、腾讯云开发者 MCP 广场 / CloudBase 等国内平台。若平台支持“外部 MCP / Streamable HTTP MCP”直接接入，优先使用 LEOR 公网 MCP 地址；若平台要求上传服务源码或托管私有网关，暂停提交。

## 通用服务信息

- 名称：LEOR AI展台设计 Agent
- 官网：https://leor.cn/agent
- MCP 地址：https://mcp.leor.cn/mcp
- 传输方式：Streamable HTTP
- GitHub：https://github.com/YonGs-AI/leor-ai-booth-design-agent
- Official MCP Registry：`io.github.YonGs-AI/leor-ai-booth-design-agent`
- Smithery：https://smithery.ai/servers/yongwah2026/leor-ai-booth-design-agent

## 一句话介绍

LEOR AI展台设计 Agent 支持 Codex、Claude Code、OpenClaw、WorkBuddy、QClaw 等 Agent 工具，让 AI 通过对话调用 LEOR 完成展台设计、生图、改图和项目资产保存。

## 适用场景

- 展台设计搭建团队前期方案沟通。
- 业务员 / 项目经理快速整理客户需求。
- 设计师生成 AI 展台设计图和展示效果图。
- 用 Logo、产品图、参考图辅助生成展台方案。
- 对已有展台图继续改图、生成材质板、展位分镜、海报和旋转视角。

## 平台接入说明

### 百度千帆 / 文心智能体

建议描述：

```text
在支持外部 MCP 工具的智能体环境中添加 LEOR MCP 地址：
https://mcp.leor.cn/mcp
用户通过 LEOR 授权页登录并确认授权。扣积分前，智能体必须汇总需求并等待用户确认。
```

待确认事项：

- 已确认“上架工具”不能直接提交公网 MCP 地址，需要先有平台内已发布工具。
- 已确认“基于 API 创建 MCP Server”入口会跳转到百度 AI 原生网关。
- 当前账号未完成百度智能云实名认证，AI 原生网关页面提示无法开通。
- 暂未确认是否允许外部 Streamable HTTP MCP URL。
- 暂未确认是否要求平台侧 OAuth 配置。
- 暂未确认是否会强制平台托管源码。

当前处理：

- 不开通 AI 原生网关。
- 不接受服务开通协议。
- 不上传 LEOR 私有代码。
- 等账号实名认证完成后，再核验是否可以仅代理公网 MCP 或提交文档型工具。

### 扣子 / Coze

当前状态：

- 已创建并发布扣子插件：`LEORAIAgent`
- 插件 ID：`7658391373665681442`
- MCP 地址：`https://mcp.leor.cn/mcp`
- 已确认工具列表能加载，调试状态显示通过。
- 发布时选择“插件会收集、传输用户的个人信息”，并勾选“IP 地址”作为平台要求的最小合规项。
- 未上传 LEOR 主站代码、Agent Gateway 源码、内部提示词、模型路由、密钥或后台路径。
- 待复查：插件是否已进入扣子公开插件商店，还是仅在当前工作区可用。

建议描述：

```text
创建 MCP 插件或外部工具时，使用 LEOR MCP 地址：
https://mcp.leor.cn/mcp
工具用途为 AI 展台设计、生图、改图和项目资产保存。普通用户不需要复制 token，通过 LEOR 授权页完成账号连接。
```

待确认事项：

- 已确认扣子编程资源库支持创建 MCP 类型插件。
- 已确认 MCP 插件可填写“插件 URL”和 Header。
- 已确认插件级授权方式可选“不需要授权”；LEOR 用户账号授权仍由 LEOR MCP 工具 `connect_leor_account` 发起。
- 已确认正式 MCP 地址 `https://mcp.leor.cn/mcp` 可以创建插件。
- 暂未确认是否可以被其他扣子用户从插件商店直接搜索安装。
- 暂未确认是否支持完整外部 OAuth 授权链路。
- 暂未确认是否只允许在当前工作区内自用。

后续处理：

- 复查扣子插件商店外部可见性。
- 如果只是工作区内插件，准备扣子安装教程和智能体创建教程。
- 如果可公开搜索，补充公开安装截图和搜索关键词。

### 腾讯云开发者 MCP 广场 / CloudBase

建议描述：

```text
LEOR AI展台设计 Agent 是公网可访问的 Streamable HTTP MCP 服务，适合作为 Hosted / Remote MCP 服务收录。MCP 地址：
https://mcp.leor.cn/mcp
```

待确认事项：

- 腾讯云开发者 MCP 广场是否支持第三方公网 MCP URL 自助提交。
- CloudBase Marketplace 是否必须使用腾讯云托管部署。
- 若要求源码托管，是否允许只提交文档型项目和远程 URL。

## 安全边界

对外只写：

- 需要 LEOR 账号授权。
- 扣积分功能消耗当前授权账号积分。
- 结果保存到当前授权账号项目。
- 默认每次只生成 1 张。
- 生成前需要确认需求。
- 不暴露核心提示词、模型密钥、内部路由、后台路径或提示词资产。

不要写：

- 主站源码。
- Agent Gateway 源码。
- 内部风控实现。
- 真实模型路由。
- 数据库结构。
- 私钥、token、环境变量。
