# Typewriter 中文文档

遵循工作区根目录 `../AGENTS.md`。

- 本项目翻译 https://docs.typewritermc.com/ 默认的 0.8.0 文档，包括使用文档、扩展条目和开发文档，共 316 页。历史版本链接保留原文入口，不纳入本版翻译。
- `sources/repository/` 为固定提交的官方原始资料，`sources/live/` 为对应网页归档；生成字段同时对照网页与组件源码。更新资料先保存到 `sources/incoming/`，核对后再更新基线。
- `docs/` 为独立 Wiki 正文和资源；公共站点只从这里复制。不要直接改写 `../Site/docs/typewriter/` 中的构建副本。
- 统一术语见 `terminology.tsv`、`notes/terminology.md`；英文条目名、字段名用于对照面板，命令、代码、配置键、权限与占位符保持原样。
- 译文修订保存在 `sources/review/`，`scripts/build-docs.py` 可重复生成。修改译稿后同步修订来源数据，避免下次生成覆盖修改。
- 原文疑点和交互组件的展示差异记在 `notes/source-issues.md`，不静默更改源示例。