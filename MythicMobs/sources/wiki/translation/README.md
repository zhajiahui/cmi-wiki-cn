# MythicMobs Wiki 翻译记录

原文为本项目 `sources/wiki/original/` 中的官方快照。`canonical-pages.json` 固定实际页面与别名；`document-slots.json` 记录原文结构和代码，`translation-units.json` 记录可翻译正文，`reviewed/` 保存完整中文审译结果。

`page-titles.json` 根据官网页面标题维护中文标题，不把正文第一个小节当成页面名称。`literal-reviews/` 只补译原提取规则误判为技术标识的普通说明，按页面与片段索引精确定位。`token-review-exceptions.json` 记录普通英语判断词与程序字面量的具体区分及依据。

在工作区根目录运行 `python MythicMobs/scripts/render-wiki.py`，可从已归档原文结构和审译记录重建正文、导航及覆盖清单，不会联网或读取服务端文件。缺少任一必需翻译单元的页面会标为待译；全站验证会报告待译页。

渲染前检查链接占位标记、数字、代码和技术标识。构建和验证仍使用公共 `Site/` 工具。更新官方原文时需要重新审译变化内容，不应复用不匹配的旧片段记录。
