# Residence 中文 Wiki

本目录保存 [Residence 官方文档](https://www.zrips.net/residence/)的原文、中文译稿和图片，作为全站的 Residence 分类发布。

- 中文入口：https://zhajiahui.github.io/cmi-wiki-cn/residence/
- 10 个官方文档页面均有对应译文。
- 指令列表含 97 条命令，权限页含 59 个节点，标志页含 113 项，另有 25 个占位符。
- 9 张原文图片已本地保存；23 个代码块按原文保留。

## 文件

- `docs/`：网站页面和资源。
- `sources/html/`：官网正文 HTML。
- `sources/en/`：用于逐段核对的英文 Markdown。
- `sources/reviewed/`：中文译稿。
- `sources/pages.json`：官网页面清单及修改时间。
- `sources/manifest.json`：原文与译文对应关系及来源哈希。
- `sources/assets.json`：原图地址、本地路径及资源哈希。
- `notes/source-issues.md`：原文的版本差异、疑点及保留方式。
- `mkdocs.yml`：本项目的目录。

## 更新

在工作区根目录运行，先安装 `Site/requirements-tools.txt` 中的依赖：

```powershell
.\.venv\Scripts\python.exe Residence/scripts/fetch-sources.py
```

抓取结果写入 `sources/incoming/`，变化清单为 `refresh-report.json`，不覆盖现有原文和译文。确认变化后，更新归档与对应译稿，再运行：

```powershell
.\.venv\Scripts\python.exe Residence/scripts/render-docs.py
.\.venv\Scripts\python.exe Residence/scripts/verify-docs.py
```

预览和发布整个站点，使用工作区根目录的 `启动.bat`、`发布.bat`。本站按官方页面翻译，未在 Minecraft 服务端验证命令、配置或 API 示例。
