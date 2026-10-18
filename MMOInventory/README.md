# MMOInventory 中文文档

来源：[Phoenix 官方文档](https://docs.phoenixdevt.fr/)。本次以 **2026-10-19** 归档的官网页面为准，本项目共 **22 页**。页面中的插件版本、服务端要求、限制及弃用说明均按原文保留。

- `docs/`：中文正文及原始图片。
- `sources/live/`：对应官网网页的完整归档。
- `sources/en/`：包含原始代码、表格与章节锚点的英文正文。
- `sources/manifest.json`：页面与原文的对应关系及哈希。
- `sources/translations.json`：本项目使用的译文记录。
- `terminology.tsv`：术语；`notes/`：原文疑点及核对备注。

翻译和核对工具由 `../Phoenix/scripts/` 共用；各插件正文仍保存在自己的根目录。修订保存在 `Phoenix/sources/review/`，生成时不重新请求在线翻译。

在工作区根目录运行：

```powershell
CMI\.venv\Scripts\python.exe Phoenix/scripts/build-docs.py
CMI\.venv\Scripts\python.exe Phoenix/scripts/verify-docs.py
CMI\.venv\Scripts\python.exe -m mkdocs build --strict -f Site/mkdocs.yml
```

网站统一放在 Phoenix 分类下，保留各插件独立目录。完整站点可从根目录 `启动.bat` 预览。未进行 Minecraft 服务端运行验证。
