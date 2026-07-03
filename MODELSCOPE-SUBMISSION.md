# ModelScope 魔搭 MCP 广场提交资料

## 当前状态

- 待提交。
- 需要登录 ModelScope / 魔搭账号。
- 官方文档入口：https://modelscope.cn/docs/mcp/create
- MCP 广场入口：https://www.modelscope.cn/mcp

## 基础信息

### 服务名称

LEOR AI展台设计 Agent

### 英文/Slug 建议

leor-ai-booth-design-agent

### 简短描述

LEOR AI展台设计 Agent 支持 Codex、Claude Code、OpenClaw、WorkBuddy、QClaw 等 Agent 工具，让 AI 通过对话调用 LEOR 完成展台设计、生图、改图和项目资产保存。

### 分类建议

- 设计工具
- 图像生成
- 生产力工具
- 展览展示 / 会展

### 标签建议

- AI展台设计
- 展台设计工具
- 展台效果图
- MCP
- Agent
- 图像生成
- 会展设计
- LEOR

## MCP 信息

### MCP Endpoint

```text
https://leor.cn/agent-test/mcp
```

### 传输方式

```text
Streamable HTTP
```

### 授权方式

用户通过 LEOR 授权页登录并确认授权。普通用户不需要复制 token，不需要配置 API key。

### 官网

```text
https://leor.cn/agent
```

### GitHub 文档仓库

```text
https://github.com/YonGs-AI/leor-ai-booth-design-agent
```

### Official MCP Registry

```text
io.github.YonGs-AI/leor-ai-booth-design-agent
```

### Smithery

```text
https://smithery.ai/servers/yongwah2026/leor-ai-booth-design-agent
```

## 详细介绍

LEOR AI展台设计 Agent 是 LEOR（leor.cn）提供的 AI 展台设计 MCP 服务。用户在支持 MCP 或外部工具调用的 Agent 工具中连接 LEOR 后，可以让 Agent 通过对话帮助整理展台设计需求、查询账号积分、调用 LEOR 生成展示效果图、修改已有展台图、生成材质板、展位分镜、海报和旋转视角，并把生成结果保存到当前授权用户自己的 LEOR 项目资产中。

适合展台设计搭建公司、会展公司、设计主管、设计师、业务员、项目经理和大型会展团队，用于前期方案沟通、客户需求梳理、AI 展台设计图生成、方案对比和提案素材整理。

## 安全说明

- 需要用户登录 LEOR 并确认授权。
- 扣积分功能消耗当前授权账号积分。
- 结果保存到当前授权账号的 LEOR 项目。
- 默认每次只生成 1 张图。
- 生成前要求 Agent 汇总需求并等待用户确认。
- LEOR 不向 Agent 暴露核心提示词、模型密钥、内部路由、后台路径或提示词资产。

## 使用示例

```text
连接我的 LEOR 账号。
```

```text
我要做一个 6x6 米食品展展位，品牌是 V8 食品。我会上传 Logo 和参考图，请先帮我整理需求，不要直接生图。
```

```text
用这张产品图做万物成展，推导一个食品展展位创意。
```

```text
查一下我 LEOR 账号还剩多少积分。
```

## 提交注意

如果 ModelScope 要求公开 LEOR 主站源码、Agent Gateway 源码、内部提示词、模型路由、密钥、后台路径或风控细节，停止提交。

如果平台只支持托管代码型 MCP，不支持外部 Streamable HTTP URL，先保留为待办，不上传私有网关源码。
