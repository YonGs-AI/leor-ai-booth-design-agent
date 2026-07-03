# GitHub 发布操作单

本仓库用于公开发布 LEOR AI展台设计 Agent 的文档和安装说明。它不是 LEOR 主站源码仓库，也不是 Agent Gateway 源码仓库。

## 发布前检查

在本目录执行：

```bash
git status --short
git log --oneline -3
```

预期结果：

- `git status --short` 没有未提交改动。
- 最新提交包含 `docs: prepare discovery channels for agent launch`。

## 创建 GitHub 仓库

仓库建议：

- Repository name: `leor-ai-booth-design-agent`
- Visibility: Public
- Description: `LEOR AI展台设计 Agent: MCP connector docs for AI booth design workflows.`
- Topics:
  - `mcp`
  - `ai-booth-design`
  - `ai展台设计`
  - `exhibition-design`
  - `leor`
  - `agent-tools`

创建仓库时不要勾选自动生成 README、LICENSE 或 `.gitignore`，避免和本地文件冲突。

## 推送命令

把 `<your-github-org-or-user>` 换成实际 GitHub 用户名或组织名：

```bash
git remote add origin https://github.com/<your-github-org-or-user>/leor-ai-booth-design-agent.git
git branch -M main
git push -u origin main
```

如果使用 SSH：

```bash
git remote add origin git@github.com:<your-github-org-or-user>/leor-ai-booth-design-agent.git
git branch -M main
git push -u origin main
```

## 发布后检查

打开 GitHub 仓库页面，检查：

- README 首屏能看到 `LEOR AI展台设计 Agent`。
- README 包含官网 `https://leor.cn/agent`。
- README 包含 MCP 地址 `https://mcp.leor.cn/mcp`。
- README 没有主站源码、网关源码、密钥、内部提示词、真实模型路由或后台路径。
- `DISCOVERY-CHANNELS.md`、`REGISTRY-SUBMISSION.md`、`SECURITY.md` 可正常打开。

## 下一步

GitHub 仓库公开后，再执行：

1. Official MCP Registry 提交。
2. Smithery 提交。
3. ModelScope MCP 广场提交。
4. 百度千帆 / 文心智能体接入材料准备。
5. 扣子 / Coze 接入材料准备。
6. MCP.so、MCP Hub 中国、Awesome MCP 中文列表补充提交。
