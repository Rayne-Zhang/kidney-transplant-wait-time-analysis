# 中文快速开始（请先读）

这是一份**新建立的项目原型**，按你们 Group 6 最终版提案搭建，适合上传 GitHub，后续让三位成员真正协作开发。里面的数字都是**虚构的演示数据**，不是加拿大肾移植真实调查数据。

## 运行与测试

1. 解压 ZIP，打开解压后的 `kidney-wait-dashboard-starter` 文件夹。
2. 安装 Python 3.10+，在此文件夹空白处点击右键打开 Windows 终端/PowerShell。
3. 输入 `py -m kidney_wait.pipeline`：会读取虚构演示数据，生成 `build/` 文件夹内的标准化 CSV 和质量报告。
4. 输入 `py -m unittest discover -s tests -v`：运行自动测试。
5. 如果想看可以交互操作的网页演示，再运行：

```powershell
py -m pip install -r requirements-dashboard.txt
py -m streamlit run dashboard/app.py
```

它会打开本地网页。这个网页是 **Streamlit 期中原型**，并不是最终提案所要求的 Power BI 文件；`powerbi/` 文件夹提供了下一步制作 Power BI 的说明。

## GitHub 上传

**GitHub 不会把你上传的 ZIP 自动展开成项目代码。必须先解压，再上传其中的文件夹和文件。** 完整步骤见 `docs/GITHUB_UPLOAD_GUIDE_ZH.md`。

## 和期中作业的关系

这些文件能帮助你开始真正开发和演示，但 GitHub 的30%并不是上传文件就可以获得：教授还要求真实 commit、不同成员的贡献。团队不能制造过去的提交历史，也不能把虚构数据写成实际研究结果。

建议：三位组员各自认领一个真实任务，review、修正与扩展原型，分别从自己的账户提交实际改动；这样才有真实的协作证据。
