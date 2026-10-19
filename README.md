# Minecraft 插件中文 Wiki

CMI、Residence、Typewriter 与 Phoenix 系列的中文文档，使用 MkDocs Material。站点顶部按项目分类；Phoenix 下按七个插件分别展开，新增“插件与配置”按插件查阅简介、前置关系、命令权限和中文配置。全文搜索可检索页面、命令、权限节点和配置键。

- 全站与 CMI：https://zhajiahui.github.io/cmi-wiki-cn/
- Residence：https://zhajiahui.github.io/cmi-wiki-cn/residence/
- Typewriter：https://zhajiahui.github.io/cmi-wiki-cn/typewriter/
- Phoenix：https://zhajiahui.github.io/cmi-wiki-cn/phoenix/
- 插件与配置：https://zhajiahui.github.io/cmi-wiki-cn/plugins/
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
| `Phoenix/` | Phoenix 首页、归档入口和共用翻译工具 |
| `MMOItems/`、`MMOCore/` | 各自的物品与 RPG 系统文档 |
| `MMOInventory/`、`MMOProfiles/` | 各自的自定义物品栏与多角色档案文档 |
| `MythicLib/`、`BountyHunters/`、`Contracts/` | 各自的开发库、悬赏和 Contracts 文档 |
| `Site/` | 公共主题、各分类的导航、搜索、构建和验证 |

`Plugins/` 保存公共插件索引；其余新增插件（如 `ItemsAdder/`、`WorldGuard/`、`LuckPerms/`）仍各用独立根目录。

每个项目分别维护 `docs/`、`sources/`、`notes/`。`Site/docs/` 中的项目页面在构建时生成，不在这里编辑译文。CMI 已发布页面继续使用原地址；Residence 的页面位于 `residence/` 下，Typewriter 的页面位于 `typewriter/` 下。

## 修改、构建与发布

CMI、Residence 的中文译稿位于各自的 `sources/reviewed/`，修改后运行对应的 `scripts/render-docs.py`。Typewriter 的修订位于 `sources/review/`，通过 `scripts/build-docs.py` 生成正文。Phoenix 系列修订保存在 `Phoenix/sources/review/`，通过 `Phoenix/scripts/build-docs.py` 生成。新增范围为官网 2026-10-19 的全部 243 页，包括归档与文档维护说明。随包配置的公开示例保存在各项目的 `sources/imported-configuration-examples.json`，通过 `Site/configuration.py` 重新生成页面；这些示例已脱敏。原 ZIP、实际配置、JAR、数据库和本地汉化覆盖包均不提交。新增插件简介的官方出处与原文摘录保存在各自的 `sources/overview-sources.md`。

随后从工作区根目录运行：

```powershell
.\.venv\Scripts\python.exe Site/verify.py
.\.venv\Scripts\python.exe -m mkdocs build --strict -f Site/mkdocs.yml
.\.venv\Scripts\python.exe Site/verify-site.py
```

静态文件输出到 `.cache/site/`。Windows 不区分 `Site` 和 `site`，请保留此输出目录设置。

双击根目录 **发布.bat**，会检查、构建并推送更改。主分支提交后，GitHub Actions 自动构建全部项目并部署到现有 GitHub Pages。首次提交前配置自己的 Git 提交姓名和邮箱，首次推送时按提示完成 GitHub 登录。仓库的 **Settings → Pages → Source** 保持 **GitHub Actions**。

## 翻译范围

仅依据各自官方文档翻译，保留命令、配置、条件、图片和示例，不将其他插件或其他版本的机制混入译文。各页附原文入口。原文中的疑点分别记录在项目的 `notes/source-issues.md`，未在 Minecraft 服务端运行验证示例。
