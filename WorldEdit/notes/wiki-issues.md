# WorldEdit Wiki 翻译备注

## 固定快照与范围

- 官方文档版本：7.4，来源 https://worldedit.enginehub.org/en/latest/。
- 快照时间：2026-10-19T15:14:26.436153+00:00。
- 快照标识：`b16b7f1e2fe96f05fcc2db1db1dff12ef0e4d6a5f948da2ad5587100a00dbde3`。
- 文档版本不等同于单个插件 JAR 的补丁版本；本次按已保存的官方文档快照完整翻译。
- 全部候选 44 页：已译 29 页，逐页排除 API 15 页，不可用 0 页。
- API 排除项的标题、URL、原文源码及具体理由均保留于覆盖清单；非 API 开发内容和进阶章节保留。

## 不可用页面

- 无。

## 原文中保留的差异

- 官方文档标为 7.4，权限页含 7.4.5 新增的 Fabric Permissions API v1 集成说明；本次没有将其当作随包 7.4.6 的独立版本说明。
- 选区页仍将区块高度写为 256；这是原文数值，并不等同于所有新版 Minecraft 世界的实际高度。
- 表达式函数表对 log10 同时写“base 10”和“base e”，两种表述互相矛盾；译文如实保留，未擅自改写。
- 放置位置切换在不同原文段落写为 //toggleplace、/toggleplace 或 /togglepos，各处命令均原样保留。
- 剪贴板蒙版段落的 //regen -c 后原文存在多余反引号，原文与译文均保留该字符。
- CraftScripts 原文安装路径写 config/WorldEdit，其他章节写 config/worldedit；译文保留原大小写。
- WorldEditDocs 仓库下载未成功；完整范围由官方已发布 Sphinx 的 toctree 与 _sources 原文递归确定，未编造 Git 提交号。

## 交付校验

- 英文 Markdown 原文按 UTF-8、LF 保存，并逐页记录 SHA-256。
- 译文完整保留代码块、inline code、命令权限占位符、表格行数、表格内段落和列表及显式标题锚点。
- 图片保存原始字节，来源、文件路径和 SHA-256 见 `sources/wiki/assets-manifest.json`。
- API 与站外链接保留官方地址，已有本地译文的链接改为相对路径。
- 未修改共享 Site、现有介绍页、configuration 或 mkdocs，未提交、未发布。
- 本次校验属于文档静态校验，没有进行 Minecraft 服务端运行验证。
