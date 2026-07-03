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
- 当前状态：已发布 `io.github.YonGs-AI/leor-ai-booth-design-agent`，最新版本 `0.2.1`。
- 发布前置：
  - GitHub 公开仓库已可访问。
  - 官网说明页 `https://leor.cn/agent` 已可访问。
  - `https://mcp.leor.cn/mcp` 公网可初始化。
- 后续升级项：完成 `leor.cn` 域名所有权验证后，评估切换或补充 `cn.leor/ai-booth-design-agent` 命名空间。

### Smithery

- 作用：MCP 服务发现、连接和分发入口。
- 提交方式：提交公开 HTTPS MCP URL。
- 当前状态：已发布 `yongwah2026/leor-ai-booth-design-agent`；发布请求已被 Smithery 接受，页面已生成，搜索索引等待平台刷新。
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
- 当前状态：已发布。
- 页面：https://modelscope.cn/mcp/servers/yongwah/leor-ai-booth-design-agent
- 备注：已按 Streamable HTTP 配置，MCP 地址为 `https://mcp.leor.cn/mcp`，图标使用 LEOR 小 O 黑金图标。
- 待复查：ModelScope 页面服务介绍区可能缓存创建时的旧地址 `https://leor.cn/agent-test/mcp`。正式对外口径只使用 `https://mcp.leor.cn/mcp`，如平台缓存未自动刷新，需要进入编辑页修正或重新同步 GitHub 说明。

### 百度千帆 / 文心智能体

- 优先级：高。
- 原因：百度文档已出现 MCP 广场和外部 MCP 接入相关能力，适合国内智能体用户。
- 发布策略：准备“外部 MCP 服务接入教程”，重点说明 MCP 地址、账号授权和扣积分确认。
- 当前状态：已登录百度智能云/千帆核验，但未完成发布。
- 核验结论：
  - “上架工具”要求先有已发布工具，不能直接提交现有公网 MCP 地址。
  - “创建工具”提供低代码、云函数、基于 API 创建 MCP Server 三类入口。
  - 进入“基于 API 创建 MCP Server”后跳转到百度 AI 原生网关；页面提示当前账号未实名认证，无法开通。
  - 未点击“立即开通”，未接受服务开通，未上传 LEOR 私有代码。
- 后续动作：如果要继续百度渠道，先由账号主体完成百度智能云实名认证，再评估 AI 原生网关是否能安全代理公网 MCP；若要求上传网关源码或暴露内部接口，停止。

### 扣子 / Coze

- 优先级：高。
- 原因：扣子支持基于 MCP 服务创建插件或自定义工具，适合普通用户通过平台添加外部能力。
- 发布策略：准备扣子版安装教程，强调“先连接 LEOR 账号，再确认需求后生成”。
- 当前状态：已创建并发布扣子插件 `LEORAIAgent`，插件 ID：`7658391373665681442`。
- 核验结论：
  - 扣子编程资源库支持创建“插件”，类型可选 `MCP`。
  - 创建 MCP 插件时需要填写“插件 URL”，授权方式可选“不需要授权”。这里的“不需要授权”仅表示扣子访问 MCP 服务本身不需要平台级密钥；用户连接 LEOR 账号仍由 LEOR OAuth 授权工具完成。
  - 使用正式 MCP 地址 `https://mcp.leor.cn/mcp` 创建成功。
  - 工具列表已加载，至少 23 个工具可被扣子识别，调试状态显示通过。
  - 发布时按合规保守口径声明插件会收集/传输用户信息，并勾选“IP 地址”。未勾选银行卡、地址、生物识别等不相关类别。
  - 插件未上传 LEOR 私有代码，未公开 Agent Gateway 源码。
- 后续动作：复查扣子插件商店或工作区外部可见性；如果只能工作区内使用，则补充“扣子安装教程”，不把它当作完全公开目录。

### 腾讯云开发者 MCP 广场 / CloudBase

- 优先级：中高。
- 原因：国内可见度高，腾讯云开发者 MCP 广场支持 Hosted / Local MCP 服务展示，CloudBase 也有 MCP Server 托管和收录说明。
- 发布策略：优先提交公网 Streamable HTTP 服务，并申请腾讯云 MCP 广场收录，让 WorkBuddy / CodeBuddy 用户能在腾讯 MCP 资源入口发现 LEOR。如果要求使用腾讯云托管代码，则先不提交私有网关源码，只准备教程或申请收录。
- 当前状态：已找到腾讯云 MCP 广场入驻申请表，已准备申请材料。
- 入驻申请表：https://wj.qq.com/s2/23327353/7684/
- 申请材料：`TENCENT-MCP-SUBMISSION.md`

### MCP Hub 中国 / Awesome MCP 中文列表

- 优先级：中。
- 原因：社区目录更利于搜索和 Agent 抓取，但审核和稳定性不如官方或大平台。
- 发布策略：提交中文介绍、官网链接、GitHub 链接和 MCP 地址。
- 当前状态：已向 MCP Hub 中国提交推荐 issue，等待维护者审核。
- 提交链接：https://github.com/mengjian-github/mcp-cn/issues/20

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
- MCP 地址：https://mcp.leor.cn/mcp
- 传输方式：Streamable HTTP
- 授权方式：用户登录 LEOR 并确认授权。
- 分类：Design、Productivity、Image Generation、Exhibition Booth Design、AI展台设计。

## 4. 发布顺序

1. 发布 GitHub 公开仓库。已完成。
2. 提交 Official MCP Registry。已完成。
3. 提交 Smithery。已完成。
4. 提交 ModelScope MCP 广场。已完成。
5. 准备 ModelScope 魔搭提交。已完成。
6. 准备百度千帆 / 文心智能体接入教程或平台提交。已核验，受实名认证 / AI 原生网关开通限制，暂未完成。
7. 准备扣子 / Coze 接入教程或插件提交。已创建并发布扣子插件，仍需复查工作区外部可见性。
8. 准备腾讯云 MCP 广场 / CloudBase 收录。已准备腾讯云 MCP 广场入驻申请材料，待填写腾讯问卷。
9. 补充提交 MCP.so、MCP Hub 中国、Awesome MCP 中文列表。MCP.so 已提交，MCP Hub 中国已提交推荐 issue。
10. 发布中文内容平台教程。

## 5. 停止条件

遇到以下情况，不继续提交，先回到内部评估：

- 平台要求公开 LEOR 主站源码或 Agent Gateway 源码。
- 平台要求公开内部提示词、模型路由、密钥、后台路径或风控策略。
- 平台无法支持用户账号授权，可能导致所有调用混在一个公共账号里。
- 平台无法让用户明确确认扣积分操作。
- 平台会绕过 LEOR 的上传大小、格式、频率或积分限制。
