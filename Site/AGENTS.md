# 公共站点文件

遵循工作区根目录 `../AGENTS.md`。

本目录只维护公共导航、样式、搜索、构建与验证。项目事实、原文和译稿分别放在 `../CMI/`、`../Residence/`、`../Typewriter/` 及各 Phoenix 插件的独立根目录。Phoenix 系列在导航中合为一个分类。

`docs/` 中仅 `assets/wiki.css` 与 `assets/logo.svg` 是公共源文件；其余页面、图片由 `hooks.py` 在构建时复制，不直接编辑或提交。

输出目录固定为工作区 `.cache/site/`。Windows 不区分 `Site` 和 `site`，不得将输出设为工作区 `site/`。
