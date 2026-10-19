# Citizens 官方 Wiki 翻译记录

## 范围与快照

- 插件基线：`2.0.43-SNAPSHOT (build 4210)`。
- 官方 Wiki 快照时间：`2026-10-19T15:08:41.713262+00:00`。
- 目录来源：https://wiki.citizensnpcs.co/api.php?action=query&list=allpages&aplimit=max&format=json。
- 通过 MediaWiki `allpages` 核验正文、项目、帮助和分类命名空间，共 191 个实际页面；每页保存固定修订号、修订时间、原始 wikitext、官方解析结果及统一 LF 的 Markdown 原文。正文链接另发现 55 个不存在的旧目标，均记录为 `unavailable`。
- 完成 179 页非 API 正文翻译，包含当前功能、1.x 历史文档、Denizen 和官方 Wiki 托管的附属插件用法，以及分类、帮助和版权页。历史页面中的版本和停用警告按原文保留。

## 排除的 API 页面

- [1.x/API](https://wiki.citizensnpcs.co/1.x/API)：API/SDK integration reference or Java trait example。
- [API](https://wiki.citizensnpcs.co/API)：API/SDK integration reference or Java trait example。
- [Denizen API](https://wiki.citizensnpcs.co/Denizen_API)：API/SDK integration reference or Java trait example。
- [Denizen API Command Template](https://wiki.citizensnpcs.co/Denizen_API_Command_Template)：API/SDK integration reference or Java trait example。
- [TestCharacterType](https://wiki.citizensnpcs.co/TestCharacterType)：API/SDK integration reference or Java trait example。

混合页面中少量 API 说明随整页保留，未因出现 API 字样而删除玩家或服主正文。

## 原站缺失与疑点

当前修订为空的 7 页：

- [Citizens Wiki/CitizensUI](https://wiki.citizensnpcs.co/Citizens_Wiki/CitizensUI)。
- [Custom Denizen Commands](https://wiki.citizensnpcs.co/Custom_Denizen_Commands)。
- [Denizen config.yml](https://wiki.citizensnpcs.co/Denizen_config.yml)。
- [Denizen temp](https://wiki.citizensnpcs.co/Denizen_temp)。
- [Denizen/0.7/Getting Started](https://wiki.citizensnpcs.co/Denizen/0.7/Getting_Started)。
- [Denizen/Quick Guide to Using Denizen](https://wiki.citizensnpcs.co/Denizen/Quick_Guide_to_Using_Denizen)。

其余 55 个不可用目标为官方正文中的红链；完整 URL、状态及原因见 `sources/wiki-coverage.json`。没有以简介、占位正文或其他页面的内容填补这些缺口。

- 1.x 页面中的“当前版本 2.0.2”、旧版 Bukkit、Denizen 0.6/0.7/0.8 等描述属于历史原文，不代表当前插件版本。
- Denizen 部分页面使用整段删除线包裹历史内容，且在 HTML 表格内嵌 YAML。保留相应结构和所有代码，不将示例折叠成概述。
- Builder 示例内还嵌有 Markdown 围栏，规范化时仅修复围栏的展示包裹，代码内容以官方 `<pre>` 原文为准。
- 部分页面存在未展开的 MediaWiki `#if` 模板文字，按官方可见内容保留；未猜测模板原意。

## 图片与链接

- 保存原始图片 37 个，未缩放或重绘。来源、使用页、文件大小及 SHA-256 见 `sources/wiki/assets-manifest.json`。
- 以下 4 个官方声明图片在 MediaWiki `imageinfo` 中无原始文件，保持官方引用并记录缺口：
  - https://wiki.citizensnpcs.co/File:CitizensUI.png。
  - https://wiki.citizensnpcs.co/File:Http://i.imgur.com/pahiSQf.png。
  - https://wiki.citizensnpcs.co/File:Http://i.imgur.com/w8o7v4u.png。
  - https://wiki.citizensnpcs.co/File:Mimic.png。
- 已存在译文的站内链接指向本地译文，API 和外站链接保留官方目标；原始来源链接与原文中的外部站点不做替换。
- 修复 1 个可确定对应关系的大小写、标点或旧名称锚点。
- 另有 22 个原文片段标识在冻结正文中没有目标，译文链接指向对应译文页本身；逐条原始片段与调整结果见 `sources/wiki/fragment-review.json`。未补造章节。

## 核对

- 每页 frontmatter 包含 `title`、`source_url`、`source_kind: official-wiki`、`translation_review: reviewed`、`source_version`。
- Manifest 是逐页对象列表；`source_sha256` 对统一 UTF-8/LF 原文计算。
- 179 页、414 个代码块、735 个行内代码标记、37 个图片文件已完成保真及本地链接检查，`verification.json` 的 `errors` 为 `[]`。
- 统一校对关键术语、开关方向、前置条件、数量、权限、命令示例和表格技术单元格；模板、商店、NPC 点击命令及基础安装/权限步骤另有人工审译覆盖。
- 此次检查覆盖原文对照及文件结构；未启动 Minecraft 服务器或客户端，未执行游戏内命令。
- 仅交付两个项目的 `docs/wiki`、`sources/wiki`、三个 Wiki 清单文件及本记录；未修改公共 Site、现有配置目录、项目主页或 mkdocs.yml，未提交或发布。

## 术语

Trait：特征；Behavior：行为；Waypoint：路径点；Template：模板；namespace：命名空间；NPC registry：NPC 注册表；bouncer：区域守卫；bodyguard：贴身护卫。插件名、事件名、脚本节点及配置键保留原名。
