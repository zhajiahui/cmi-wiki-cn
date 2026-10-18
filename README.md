# Minecraft 插件中文 Wiki

CMI、Residence 与 Typewriter 的中文文档，使用 MkDocs Material。站点顶部按插件分为三个分类，左侧展开各自目录，全文搜索可以检索三个项目的页面、命令和权限节点。

- 全站与 CMI：https://zhajiahui.github.io/cmi-wiki-cn/
- Residence：https://zhajiahui.github.io/cmi-wiki-cn/residence/
- Typewriter：https://zhajiahui.github.io/cmi-wiki-cn/typewriter/
- 仓库：https://github.com/zhajiahui/cmi-wiki-cn

## 本地预览

安装 Python 3.12 后，双击根目录的 **启动.bat**。首次运行会安装依赖，然后打开 http://127.0.0.1:8000/cmi-wiki-cn/ 。关闭启动窗口即可停止预览。

手动操作，在工作区根目录打开 PowerShell：

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r Site/requirements-tools.txt
.\.venv\Scripts\python.exe Site/serve.py
```

## 项目目录

| 目录 | 内容 |
| --- | --- |
| `CMI/` | CMI 的 45 页译文、官网归档、图片及核对备注 |
| `Residence/` | Residence 的 10 页译文、官网归档、图片及核对备注 |
| `Typewriter/` | Typewriter 0.8.0 的 316 页译文、官方原文、视频和 JSON 示例 |
| `Site/` | 公共主题、三个分类的导航、搜索、构建和验证 |

每个项目分别维护 `docs/`、`sources/`、`notes/`。`Site/docs/` 中的项目页面在构建时生成，不在这里编辑译文。CMI 已发布页面继续使用原地址；Residence 的页面位于 `residence/` 下，Typewriter 的页面位于 `typewriter/` 下。

## 修改、构建与发布

CMI、Residence 的中文译稿位于各自的 `sources/reviewed/`，修改后运行对应的 `scripts/render-docs.py`。Typewriter 的修订位于 `sources/review/`，通过 `scripts/build-docs.py` 生成正文。随后从工作区根目录运行：

```powershell
.\.venv\Scripts\python.exe Site/verify.py
.\.venv\Scripts\python.exe -m mkdocs build --strict -f Site/mkdocs.yml
.\.venv\Scripts\python.exe Site/verify-site.py
```

静态文件输出到 `.cache/site/`。Windows 不区分 `Site` 和 `site`，请保留此输出目录设置。

双击根目录 **发布.bat**，会检查、构建并推送更改。主分支提交后，GitHub Actions 自动构建三个项目并部署到现有 GitHub Pages。首次提交前配置自己的 Git 提交姓名和邮箱，首次推送时按提示完成 GitHub 登录。仓库的 **Settings → Pages → Source** 保持 **GitHub Actions**。

## 翻译范围

仅依据各自官方文档翻译，保留命令、配置、条件、图片和示例，不将其他插件或其他版本的机制混入译文。各页附原文入口。原文中的疑点分别记录在项目的 `notes/source-issues.md`，未在 Minecraft 服务端运行验证示例。
