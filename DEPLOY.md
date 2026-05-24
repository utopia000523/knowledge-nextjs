# 个人知识库 — 部署说明

## GitHub 仓库

https://github.com/utopia000523/knowledge-nextjs

## Vercel 部署步骤

1. 登录 https://vercel.com (推荐用 GitHub 账号登录)
2. 点击 **Add New → Project**
3. Import Git Repository → 选择 `utopia000523/knowledge-nextjs`
4. Framework Preset: 自动识别为 **Next.js**（无需修改）
5. Environment Variables: **无需配置**
6. 点击 **Deploy**

部署完成后会获得 `https://knowledge-nextjs.vercel.app` 的访问地址。

## 自动部署机制

每次知识库有更新时：
1. cron job（knowledge-auto-collect-and-expand）自动收录新书
2. 写入 `data/articles/` 并同步到 `public/data/`
3. 执行 `~/.hermes/scripts/git_push_knowledge.py`
   - `git add -A && git commit -m "auto: update @ 时间"`
   - `git push origin main`
4. Vercel 检测到 GitHub 推送 → 自动重新构建 → 部署新版本

每周一的索引自动更新（knowledge-index-weekly-update）同样会 commit + push。

## 本地开发

```bash
cd ~/.hermes/knowledge-nextjs
npm run dev
# 访问 http://localhost:3000
```
