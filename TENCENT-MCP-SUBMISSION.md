# 腾讯云 MCP 广场入驻申请材料

本文件用于提交腾讯云 MCP 广场 / WorkBuddy / CodeBuddy 生态收录申请。公开内容只写产品能力、连接方式、授权方式和安全承诺，不公开 LEOR 主站代码、Agent Gateway 源码、内部提示词、模型路由、密钥、后台路径或风控细节。

## 申请目标

让 WorkBuddy、CodeBuddy 以及腾讯云 MCP 广场用户可以在腾讯生态内发现并连接 `LEOR AI展台设计 Agent`，降低手动配置门槛。

## 官方依据

腾讯云 MCP 广场文档说明：

- WorkBuddy / CodeBuddy 可以从腾讯云 MCP 广场获取 MCP 服务。
- 自行开发的 MCP 申请上架 MCP 广场当前面向企业级 MCP 开发者开放。
- 企业级 MCP 开发者可通过腾讯云 MCP 广场入驻申请表提交上架需求。
- MCP 广场侧可能要求补充适用场景、适用人群、解决痛点、使用教程和应用案例。

入驻申请表：

```text
https://wj.qq.com/s2/23327353/7684/
```

## 基础信息

- MCP 名称：LEOR AI展台设计 Agent
- 公司名称：乐于尔（广州）网络科技有限公司
- 品牌名称：LEOR
- 官网：https://leor.cn/
- 官方说明页：https://leor.cn/agent
- MCP 地址：https://mcp.leor.cn/mcp
- 传输方式：Streamable HTTP
- GitHub 文档仓库：https://github.com/YonGs-AI/leor-ai-booth-design-agent
- Official MCP Registry：io.github.YonGs-AI/leor-ai-booth-design-agent
- Smithery：https://smithery.ai/servers/yongwah2026/leor-ai-booth-design-agent
- ModelScope：https://modelscope.cn/mcp/servers/yongwah/leor-ai-booth-design-agent

## 一句话介绍

LEOR AI展台设计 Agent 支持 Codex、Claude Code、OpenClaw、WorkBuddy、QClaw 等 Agent 工具，让 AI 通过对话调用 LEOR 完成展台设计、生图、改图和项目资产保存。

## 服务描述

LEOR AI展台设计 Agent 是 LEOR（leor.cn）提供的 AI 展台设计 MCP 服务。用户在 WorkBuddy、CodeBuddy 或其他支持 MCP / 外部工具调用的 Agent 环境中连接 LEOR 后，可以通过对话让 Agent 帮助整理展台设计需求、查询账号积分、调用 LEOR 生成展示效果图、修改已有展台图、生成材质板、展位分镜、海报和旋转视角，并把生成结果保存到当前授权用户自己的 LEOR 项目资产中。

LEOR 面向展台设计搭建公司、会展公司、设计主管、设计师、业务员、项目经理和大型会展团队，适合用于前期方案沟通、客户需求梳理、AI 展台设计图生成、方案对比、提案素材整理和项目资产沉淀。

## 适用人群

- 展台设计搭建公司
- 会展服务公司
- 展台设计师
- 设计主管
- 业务员
- 项目经理
- 客户跟单人员
- 大型会展项目团队

## 核心场景

- 客户需求梳理：让 Agent 先收集展台尺寸、行业、品牌、风格、颜色、造型、logo、参考图和补充说明。
- 展台设计图生成：资料齐全并经用户确认后，调用 LEOR 生成展示效果图。
- 参考图辅助生成：使用用户上传的 logo、产品图、参考图或灵感图辅助生成展台方案。
- 万物成展：把任意创意来源图片，如 logo、产品、颜色、动物、水果、纹理等，推导成展台创意方案。
- 展台图片修改：基于已有展台图继续调整风格、材质、颜色、结构或品牌信息。
- 提案素材生成：为展台方案生成材质板、展位分镜、海报和旋转视角。
- 项目资产保存：生成结果保存到当前授权用户自己的 LEOR 项目资产中，用户回到 LEOR 网站仍可继续查看和处理。

## 解决痛点

- 会展行业很多用户不会直接使用 AI 生图工具，Agent 可以通过对话帮助用户补齐需求。
- 展台设计前期沟通资料常常不完整，LEOR MCP 内置资料完整性检查，资料不足时不会直接扣积分生成。
- 传统前期方案沟通需要设计师反复出图，LEOR 可以先用 AI 生成展示效果图和提案素材，提高沟通效率。
- 用户在 Agent 里生成的图片不会散落在聊天记录里，结果会保存到 LEOR 项目资产中，方便后续继续设计和管理。

## 授权与扣费规则

- 使用前需要用户登录 LEOR 并确认授权。
- 普通用户不需要复制 token，不需要查看 `.env`，也不需要修改本地代码。
- 扣积分功能消耗当前授权账号积分。
- 默认每次只生成 1 张图。
- Agent 在调用会扣积分的生成或改图工具前，必须先向用户汇总需求并等待明确确认。
- 如果用户只是找灵感、看案例或搜索参考图，Agent 不应该直接调用扣积分生图工具。

## 安全承诺

- LEOR 不向 Agent 暴露核心提示词、模型密钥、内部路由、后台路径或后台数据。
- 公开 GitHub 仓库只包含文档、安装说明和配置示例，不包含 LEOR 主站代码或 Agent Gateway 源码。
- 用户授权、积分扣费、图片上传限制、项目资产归属和任务查询均由 LEOR 后端控制。
- LEOR MCP 不提供绕过积分、批量刷图、读取其他用户项目或导出内部提示词的能力。

## 腾讯生态适配说明

- LEOR MCP 使用公网 HTTPS 地址：`https://mcp.leor.cn/mcp`。
- 当前服务支持 Streamable HTTP。
- 服务已通过 MCP 初始化和工具列表查询验证，当前工具数约 23 个。
- 建议腾讯 MCP 广场优先以远程 / Hosted 方式收录，避免用户手动复制复杂配置。
- 如腾讯侧需要云托管，请先确认不会要求公开 LEOR Agent Gateway 源码、内部提示词、模型路由、密钥或后台路径。

## 可提交分类建议

- Design
- Productivity
- Image Generation
- AI展台设计
- 会展设计
- 展台设计工具
- Business / Marketing / Proposal

## 推荐搜索关键词

AI展台设计、展台设计、会展设计、展示效果图、展台生图、展会方案、展位设计、LEOR、MCP、WorkBuddy、CodeBuddy
