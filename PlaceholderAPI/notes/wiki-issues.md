# PlaceholderAPI Wiki 翻译核对记录

## 完成范围

- 固定当前官方站点快照：`official-site-2026-10-19-15adfb5d4a300156`。
- 官方 sitemap 共 18 页；完整翻译 15 页，排除 API 开发文档 3 页；正文来源不可用 0 页。
- 旧 GitHub Wiki 首页已公告迁移，当前站点作为正文范围。原始 HTML、提取的 Markdown 和其 SHA-256 同时保留。
- 原文全部表格、代码与原生图片保留；译文链接优先指向本地对应页面。API 排除页的入口继续指向官方来源。

## API 排除项

- [Hytale 配置 API](https://wiki.placeholderapi.com/developers/configuration-api-hytale/)：API 接口或占位符扩展实现编程文档。
- [创建占位符扩展](https://wiki.placeholderapi.com/developers/creating-a-placeholderexpansion/)：API 接口或占位符扩展实现编程文档。
- [通过 API 使用 PlaceholderAPI](https://wiki.placeholderapi.com/developers/using-placeholderapi/)：API 接口或占位符扩展实现编程文档。

## 原文疑点（保留原意与技术标记）

- [Minecraft 占位符列表](https://wiki.placeholderapi.com/users/placeholder-list/minecraft/)：ChangeOutput 的 `<match>` / `<matcher>`、Server 的 `<SimpleDateTime>` / `<SimpleDateFormat>` 写法不一致，均按出现位置保留。
- 同页 Prison 的 STATSRANKS 将 `<rankname>` 说明为矿区名称，另有部分别名重复；没有推定作者意图后重写。
- 同页 Multiverse-Core 的版本标签存在粘连；SkyWars 的两条链接使用 `hhttps://`；VKBackPack 标题有多余括号；NumberFormatter 部分示例符号格式可疑。未改动相关示例逻辑。
- [Expansion Cloud](https://wiki.placeholderapi.com/developers/expansion-cloud/)：域名说明存在新旧差异，并有未附解释的星号，按原文保留。
- [Hytale 占位符列表](https://wiki.placeholderapi.com/users/placeholder-list/hytale/)：个别占位符缺少结尾 `%`，Werchat 部分条目多出反引号，技术标记保持原样。
- [Minecraft 插件列表](https://wiki.placeholderapi.com/users/plugins-using-placeholderapi/minecraft/)：82 处 `[Link]` 没有提供链接地址，BetonQuest 条目也有原有标记异常；没有补造地址。

## 链接调整

- 原文 Hytale 占位符目录中的 `#Mod-placeholders` 大小写与实际标题 ID 不一致；译文改用 `#mod-placeholders`，对应同一原有标题。
- 其余中文标题使用官方页面原有 ID 保留英文锚点，站内链接映射到对应译文，未替换代码块或行内代码中的字符串。

## 核对方式

逐页对照全文并检查 UTF-8/LF 原文 hash、完整代码块、行内代码、表格行数、显式锚点、图片来源及未翻译正文。Hytale 插件列表保留 37 项，Minecraft 插件列表保留 339 项；Minecraft 占位符长页保留 332 个完整代码块。

核对针对文档与静态资料，没有在游戏服务器中验证命令或占位符行为。
