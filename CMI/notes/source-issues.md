# 原文疑点与版本备注

这些记录用于维护翻译，不作为 Wiki 正文。译文按对应官方页面保留原意和技术标识；下列问题未据经验修补，也未在 Minecraft 服务端验证。

## 来源版本

- [首次运行](https://www.zrips.net/cmi/first-run/)称插件不依赖其他插件；[官网首页](https://www.zrips.net/cmi/)及[官方仓库 README](https://github.com/Zrips/CMI)说明需要 CMILib。两页译文分别保留原说法。
- [指令列表](https://www.zrips.net/cmi/commands/)标注对应 9.2.4.5；[查找](https://www.zrips.net/cmi/extra/search/)自 9.7.12.0 起适用，[扫描](https://www.zrips.net/cmi/extra/scan/)自 9.7.13.0 起适用。
- 指令页中的 `fixchunk`、`lfix`、`preview` 分别有旧 Minecraft 版本限制。译文保留这些限制。

## 命令与权限

- [权限页](https://www.zrips.net/cmi/permissions/)包含 `cmi.enchantments.`、`cmi.enchantments..$2`，疑似缺少占位符；另有 `/itemanem` 疑似拼写错误。
- `walkspeed`：英文指令与权限页写 0–10，官方中文语言文件写 0–5。以本次翻译的英文页面为准。
- 指令签名中的 `flightcharge`、`uncondense`、`exp`、`money` 有括号不配对问题，按原文保留。
- `command.alert.info.inform`、`bassbarcompass`、`largefirreball`、`jail_reasson`、`collumnName` 疑似命名或拼写问题，未替换。
- `setenchantworth` 说明出现 `scavenger`，指令表列出的是 `scavenge`。
- `cheque` 说明称右键支票会扣款；`nick` 的昵称修改说明存在矛盾。
- `repaircost` 英文写“设置”、中文语言文件写“查询”；`editwarnings` 英文写“编辑”、中文写“检查”。译文以英文页为准。

## 功能页

- [盔甲架编辑器](https://www.zrips.net/cmi/armor-stand-editor/)称有 17 种操作，但下方实际列出 18 个专项权限节点，译文保留数量说法和完整节点列表。
- [全息图](https://www.zrips.net/cmi/holograms/)使用 `click:shiftright!`，[特殊指令](https://www.zrips.net/cmi/commands/specialized/)使用 `rightshift`；未统一拼写。
- 全息图页使用“客户端 TPS”，且穿透显示与背板组合的说明有版本相关歧义。
- [特殊指令](https://www.zrips.net/cmi/commands/specialized/)的 `hasexactitem` 示例仍写作 `hasitem:coal;5`。
- [自定义别名](https://www.zrips.net/cmi/commands/custom-alias/)出现 `/cmi aliaseditot`；[指令预热](https://www.zrips.net/cmi/commands/warmups/)权限模板出现 `[comandName]`。
- [Boss 栏消息](https://www.zrips.net/cmi/commands/bossbarmsg-handling/)开头的消息文本和时长说明，与紧邻示例不一致。
- [对话框](https://www.zrips.net/cmi/commands/dialogs/)的 Boolean Value 说明称“单选项”，Slider 的 `[value]` 说明称“文本框中的值”。
- [传送点](https://www.zrips.net/cmi/commands/warps/)对设置传送点的权限，分别写 `cmi.command.setwarp` 和 `cmi.command.warp`。
- [随机传送](https://www.zrips.net/cmi/commands/rtp/)示例使用 `center:0,0`，语法列表使用 `center:[x]:[z]`；元数据限次方案保留原文待补充、待测试标记。
- [自动晋级](https://www.zrips.net/cmi/rankup-system/)的 `Branch2Rank1` 示例却广播晋升到 `Branch1Rank1`。
- [占位符](https://www.zrips.net/cmi/placeholders/)的两个名称含 `seconds` 的在线时长占位符，原文说明使用“分钟”。译文保留原单位。
- [自定义文本](https://www.zrips.net/cmi/custom-text/)示例含未闭合的 `<H>`，分页说明未显示具体标记；未自行补写。

## 归档与排版

- 官方层级中有 47 个页面记录；`extra` 分类入口和 `import-from-essentials` 子页正文为空。保留来源记录，不发布空白中文页；导入说明链接到有实际内容的“首次运行”。
- WordPress 部分代码块使用 HTML `<br>` 换行。归档转换和页面生成会恢复这些换行，保留其余代码字符。
- Nyan Cat 等示例包含不换行空格，按源文保留。

## 其他原文疑点

- 一行创建物品的刷怪笼命名说明，对名称设置顺序及转入物品描述的条件有歧义，按原文翻译。
- 生成生物页的 TNT 计时同时写了“整数”和“可以是小数”；`onfire`、`ohand` 段末有多余花括号；`saddle` 将羊驼列入可装备鞍的示例。均保留原文。
- Tab 动画示例部分列表符号使用 `–`，与 YAML 的 `-` 不同，未修改。
- 自定义头颅条件包含 `Pasive` 和重复 `Cyan`；描述格式与示例不一致，`CustomHeads.yml`／`customHeads.yml` 大小写存在差异。
- 聊天过滤示例中 `:DDD` 的字符数与大写比例注释不一致。
