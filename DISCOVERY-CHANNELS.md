# 发现渠道发布清单

本文件用于规划 LEOR AI展台设计 Agent 在 GitHub、MCP 目录和国内 Agent 平台里的公开入口。公开内容只写产品能力、安装方式、授权方式和安全承诺，不写主站代码、网关实现、内部提示词、真实模型名、后台路径或风控细节。

## 1. 技术可信源

### GitHub

- 目标仓库名：`leor-ai-booth-design-agent`
- 仓库类型：公开仓库。
- 内容范围：文档、配置示例、目录提交资料、使用示例。
- 不包含：主站代码、Agent Gateway 源码、内部安全运行手册、密钥、真实模型路由、提示词库。
- 作用：让 Agent、开发者和第三方 MCP 目录有一个可引用的公开技术来源。

### Official MCP Registry

- 作用：官方 MCP 生态发现入口。
- 当前准备文件：`registry/server.json`。
- 当前状态：已发布 `io.github.YonGs-AI/leor-ai-booth-design-agent`，版本 `0.2.0`。
- 发布前置：
  - GitHub 公开仓库已可访问。
  - 官网说明页 `https://leor.cn/agent` 已可访问。
  - `https://leor.cn/agent-test/mcp` 公网可初始化。
- 后续升级项：完成 `leor.cn` 域名所有权验证后，评估切换或补充 `cn.leor/ai-booth-design-agent` 命名空间。

### Smithery

- 作用：MCP 服务发现、连接和分发入口。
- 提交方式：提交公开 HTTPS MCP URL。
- 当前状态：已发布 `yongwah2026/leor-ai-booth-design-agent`。
- 页面：https://smithery.ai/servers/yongwah2026/leor-ai-booth-design-agent
- 注意：如果平台要求公开私有源码或内部风控实现，停止提交。

### MCP.so

- 作用：第三方 MCP 目录，适合作为补充发现入口。
- 提交材料：使用 `REGISTRY-SUBMISSION.md` 的通用字段。
- 当前状态：已通过 GitHub issue 提交。
- 提交链接：https://github.com/chatmcp/mcpso/issues/2999

## 2. 国内优先渠道

### 魔搭 ModelScope MCP 广场

- 优先级：高。
- 原因：国内 MCP 广场和实验场用户更集中，适合让不翻墙的 Agent 用户发现。
- 发布策略：先提交公开服务或教程页；如果平台要求代码托管，优先使用文档型项目，不公开私有网关实现。
- 当前状态：提交资料已准备，见 `MODELSCOPE-SUBMISSION.md`。创建入口需要登录 ModelScope / 魔搭账号，当前未完成提交。

### 百度千帆 / 文心智能体

- 优先级：高。
- 原因：百度文档已出现 MCP 广场和外部 MCP 接入相关能力，适合国内智能体用户。
- 发布策略：准备“外部 MCP 服务接入教程”，重点说明 MCP 地址、账号授权和扣积分确认。
- 当前状态：待登录百度智能云/千帆平台确认是否支持公开 MCP 服务收录；先按外部 MCP 接入教程准备。

### 扣子 / Coze

- 优先级：高。
- 原因：扣子支持基于 MCP 服务创建插件或自定义工具，适合普通用户通过平台添加外部能力。
- 发布策略：准备扣子版安装教程，强调“先连接 LEOR 账号，再确认需求后生成”。
- 当前状态：待登录扣子平台确认是否支持公开发布；如只支持工作区内自定义 MCP，则先发布教程，不上传私有代码。

### 腾讯云开发者 MCP 广场 / CloudBase

- 优先级：中高。
- 原因：国内可见度高，腾讯云开发者 MCP 广场支持 Hosted / Local MCP 服务展示，CloudBase 也有 MCP Server 托管和收录说明。
- 发布策略：优先提交公网 Streamable HTTP 服务；如果要求使用腾讯云托管代码，则先不提交私有网关源码，只准备教程或申请收录。
- 当前状态：待登录腾讯云账号确认收录入口。

### MCP Hub 中国 / Awesome MCP 中文列表

- 优先级：中。
- 原因：社区目录更利于搜索和 Agent 抓取，但审核和稳定性不如官方或大平台。
- 发布策略：提交中文介绍、官网链接、GitHub 链接和 MCP 地址。

### 知乎 / 公众号 / 小红书 / 抖音

- 优先级：营销发现，不作为技术目录。
- 发布策略：
  - 知乎：解释“AI展台设计 Agent 是什么，怎么接 LEOR”。
  - 公众号：正式发布说明。
  - 小红书/抖音：面向普通用户的安装和使用演示。

## 3. 统一提交字段

- 名称：LEOR AI展台设计 Agent
- 一句话说明：LEOR AI展台设计 Agent 支持 Codex、Claude Code、OpenClaw、WorkBuddy、QClaw 等 Agent 工具，让 AI 通过对话调用 LEOR 完成展台设计、生图、改图和项目资产保存。
- 官网：https://leor.cn/agent
- MCP 地址：https://leor.cn/agent-test/mcp
- 传输方式：Streamable HTTP
- 授权方式：用户登录 LEOR 并确认授权。
- 分类：Design、Productivity、Image Generation、Exhibition Booth Design、AI展台设计。

## 4. 发布顺序

1. 发布 GitHub 公开仓库。已完成。
2. 提交 Official MCP Registry。已完成。
3. 提交 Smithery。已完成。
4. 提交 ModelScope MCP 广场。
5. 准备 ModelScope 魔搭提交。资料已完成，待登录平台提交。
6. 准备百度千帆 / 文心智能体接入教程或平台提交。
7. 准备扣子 / Coze 接入教程或插件提交。
8. 准备腾讯云 MCP 广场 / CloudBase 收录。
9. 补充提交 MCP.so、MCP Hub 中国、Awesome MCP 中文列表。MCP.so 已提交。
10. 发布中文内容平台教程。

## 5. 停止条件

遇到以下情况，不继续提交，先回到内部评估：

- 平台要求公开 LEOR 主站源码或 Agent Gateway 源码。
- 平台要求公开内部提示词、模型路由、密钥、后台路径或风控策略。
- 平台无法支持用户账号授权，可能导致所有调用混在一个公共账号里。
- 平台无法让用户明确确认扣积分操作。
- 平台会绕过 LEOR 的上传大小、格式、频率或积分限制。
