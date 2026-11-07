# 将本项目上传 GitHub：Windows / 浏览器方法

1. 先**解压**下载的 ZIP；不要只把 ZIP 文件传到 GitHub。
2. 登录 https://github.com ，点击右上角 `+` → `New repository`。
3. Repository name 建议 `kidney-transplant-waitlist-analysis`；选择 Private 或依学校要求选择 Public。**不要在 GitHub 页面预先创建 README**，因为本项目已有。
4. 创建后，在空仓库页面选择 `uploading an existing file`，或进入 `Add file` → `Upload files`。
5. 从 Windows 文件管理器打开已解压的项目目录，**将内部所有文件及子文件夹**拖到浏览器上传区（不要上传 ZIP 本身）。如网页未保留目录层级，建议改用下方 Git 命令。
6. 查看待提交文件清单，确认有 `README.md`、`kidney_wait/pipeline.py`、`sql/01_schema.sql`、`dashboard/app.py`、`tests/test_pipeline.py` 等层级。
7. 在 Commit message 写真实说明，如 `Add initial AI-assisted prototype with synthetic demo data`，点击 `Commit changes`。
8. 让另外两位同学访问仓库并在未来**真实地**完成各自任务；在 GitHub 中可通过 Settings → Collaborators 邀请（页面选项名称可能因 GitHub 更新不同）。

## 替代：使用 Git（更可靠地保留目录结构）

创建 GitHub 的**空仓库**，复制它的 HTTPS URL，在解压后文件夹打开 PowerShell：

```powershell
git init
git add .
git commit -m "Add initial AI-assisted prototype with synthetic demo data"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

将链接换成你刚创建的真实仓库链接。如果 Git 提示未配置用户，请先设置 `git config --global user.name` 和 `git config --global user.email` 为你的真实信息。授权登录按 GitHub 的页面操作。

## 提交课程作业时

GitHub 链接写在4页小组报告中；PDF 本身提交到 Brightspace 对应的 D.3.1 入口。只有 GitHub 文件而没有真实运行演示，不满足完整作业要求。
