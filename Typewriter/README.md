# Typewriter 中文 Wiki

来源：[Typewriter 官方文档](https://docs.typewritermc.com/)。本版整理官网默认的 **0.8.0** 文档，共 **316 页**：43 页使用文档、245 页扩展文档和条目、28 页开发文档。

线上入口：https://zhajiahui.github.io/cmi-wiki-cn/typewriter/

## 目录

- `docs/`：中文正文与 108 个原始资源，包含 41 段视频。
- `sources/repository/`：官方仓库固定提交的原文、组件和资源。
- `sources/live/`：316 个对应网页的 HTML 归档，包含组件生成的字段说明。
- `sources/en/`：保留原始锚点和代码的英文正文。
- `sources/review/`：按翻译单元保存的中文修订。
- `titles.json`、`terminology.tsv`：页面译名和常用术语。
- `notes/`：术语说明、原文疑点和核对记录。

原始资料固定到官方仓库提交 `9b0a087150c594120d6b89b158f3402bb9d85142`。不包含独立 Beta 站点、旧版本站点、开发日志和隐私页面；当前文档中的 API 迁移记录、旧版链接和“待补充”提示仍按原文保留。

## 生成与核对

在工作区根目录运行：

```powershell
CMI\.venv\Scripts\python.exe Typewriter/scripts/build-docs.py
CMI\.venv\Scripts\python.exe Typewriter/scripts/verify-docs.py
CMI\.venv\Scripts\python.exe -m mkdocs build --strict -f Site/mkdocs.yml
CMI\.venv\Scripts\python.exe Site/verify-site.py
```

构建和校验使用已归档的译文与资源，不调用在线翻译服务。`draft-translations.py` 仅用于制作初稿，不应在发布时重新运行。修改译文请更新 `sources/review/` 对应记录，再生成正文。

可在根目录双击 `启动.bat` 预览三个插件分类，也可用本目录的 `mkdocs.yml` 单独构建。

## 展示方式

条目字段同时保留中文说明和英文名称，便于对照编辑面板。视频及 JSON 示例提供本地资源。任务流程图展开为包含全部状态转换的表格，任务状态示例保留中文交互；Rive 交互图保留原文入口和原始 `.riv` 文件。

原文的已知疑点见 `notes/source-issues.md`。以上是文档与网站核对，没有在 Minecraft 服务端运行插件或测试示例。