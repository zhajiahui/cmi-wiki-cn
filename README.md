# CMI 中文 Wiki

基于 CMI 官方文档整理的中文 Wiki，使用 MkDocs Material，提供折叠目录和中英文全文搜索。

- 站点地址：https://zhajiahui.github.io/cmi-wiki-cn/
- 官方文档：https://www.zrips.net/cmi/
- 仓库：https://github.com/zhajiahui/cmi-wiki-cn

## 本地预览

安装 Python 3.12 后，双击本目录的 **启动.bat**。首次运行会在项目内创建虚拟环境并安装依赖，之后打开 http://127.0.0.1:8000/cmi-wiki-cn/ 。关闭启动窗口即可停止预览。

手动操作（在本目录打开 PowerShell）：

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-tools.txt
.\.venv\Scripts\python.exe scripts/verify-docs.py
.\.venv\Scripts\python.exe -m mkdocs serve
```

构建静态网站：

```powershell
.\.venv\Scripts\python.exe -m mkdocs build --strict
```

生成结果位于 `site/`。静态文件需通过 HTTP 服务访问，全文搜索也在浏览器中运行。

## 修改文档

- `docs/`：网站使用的中文页面和本地图片。
- `sources/html/`、`sources/en/`：官网原始正文与便于对照的英文 Markdown。
- `sources/reviewed/`：校对后的译稿。更新译稿后，运行 `scripts/render-docs.py` 生成页面。
- `sources/manifest.json`：官网页面与中文页面的对应关系，以及来源哈希。
- `sources/assets.json`：图片、动画的原地址、本地文件及校验值。
- `notes/`：翻译风格、写法参考、原文疑点和验证记录，不发布到 Wiki 正文。
- `mkdocs.yml`：目录、主题和搜索配置。

翻译遵循上级工作区 `AGENTS.md` 的要求，项目内另附 `AGENTS.md` 供独立克隆时查阅。默认只翻译原文；语句可以润色，功能条件、技术标识和示例逻辑保持原意。

更新页面后执行：

```powershell
.\.venv\Scripts\python.exe scripts/render-docs.py
.\.venv\Scripts\python.exe scripts/verify-docs.py
.\.venv\Scripts\python.exe -m mkdocs build --strict
```

## 核对官网更新

```powershell
.\.venv\Scripts\python.exe scripts/fetch-sources.py
```

新抓取的资料保存在 `sources/incoming/`，变化清单为 `sources/incoming/refresh-report.json`。工具不覆盖已校对译文。核对差异并修改原文归档和译稿后，再生成网站。

## GitHub Pages

主分支提交会触发 `.github/workflows/pages.yml`：检查内容、严格构建、上传静态文件并部署到 GitHub Pages。仓库 **Settings → Pages → Source** 选择 **GitHub Actions**。

仓库已配置 GitHub Actions 部署。修改文档后，双击 **发布.bat** 检查、构建并推送更改；在仓库的 **Actions** 页面查看构建与部署结果。首次使用本机 Git 时需要完成 GitHub 登录。如需提交后续修改，请先在本仓库配置自己的 Git 提交姓名和邮箱。发布前先确认暂存范围内只有本项目资料。

## 来源与版本

官网不同页面对应的版本不完全一致。指令总表保留其标注的 9.2.4.5，部分功能页包含更新版本的说明。已发现的矛盾记录在 `notes/source-issues.md`，没有据此改写示例逻辑，也没有进行 Minecraft 服务端运行测试。

CMI 原文、截图和动画归各自原作者所有，页面附有原文入口。本站为非官方中文翻译，不提供插件本体下载。
