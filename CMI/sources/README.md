# 来源归档

正文来自 https://www.zrips.net/cmi/ 及其子页面，通过官网公开的 WordPress 页面接口获取；页面层级与正文内 CMI 链接已交叉检查。

- `pages.json`：47 条官网页面记录，包含 URL、页面 ID、标题和官网修改时间。
- `html/`：WordPress 正文原始 HTML，包含代码和页面资源引用。
- `en/`：供翻译对照的英文 Markdown。恢复了 HTML `<br>` 代码换行。
- `reviewed/`：45 页经原文核对的中文译稿。
- `manifest.json`：中文文件、来源和 HTML 在换行统一为 LF 后的 SHA-256 对应表。
- `assets.json`：162 个本地资源的来源、大小和 SHA-256。
- `command-translations.json`：从 Zrips/CMI 官方仓库的 `Translations/Locale_CN.yml` 提取的命令中文释义，仅用于术语参考；对应基线提交 `95cec1af672b051593117b11b26498ea57e251e1`。英文页面与语言文件不一致时，以该页原文为准并记入 notes。

`extra` 和 `import-from-essentials` 两个官网页面正文为空，因此不生成空白译文。

运行 `scripts/fetch-sources.py` 会把新资料写到 `sources/incoming/` 并生成差异报告，不覆盖本次归档或译稿。此次重新获取全部 47 页后，正文差异为 0。

原文及图片、动画归原作者所有。中文页面保留原文入口，外部视频使用源文链接。
