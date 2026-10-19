# MythicMobs Wiki 问题记录

## table-cell 016：Potion 布尔说明中的 not 歧义（2026-10-20）

核对对象为官方 [Potion 机制页](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/potion) 的 Attributes 表，以及 [Shoot 机制页](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shoot) 的 Potion Type Attributes 表。两页均重新读取了实际正文；本地原文分别在 sources/wiki/original/skills/mechanics/potion.md 和 sources/wiki/original/skills/mechanics/shoot.md。

| 参数 / unit-id | Potion 原文 | 当前译文 | 官方页面中的别名与默认值 |
| --- | --- | --- | --- |
| force / ef1ad9669cb8a1fac97b | Whether not to override the current potion effect or not. | 是否覆盖当前的药水效果。 | overwrite, ow, override, or；false |
| hasParticles / 0310fd2ea8a4afb976d6 | Whether not to show the status effect particles. | 是否显示状态效果粒子。 | particles, p；true |
| hasIcon / 9e40a3ded03073379482 | Whether not to show the status effect icon. | 是否显示状态效果图标。 | icon, i；true |

原文问题：force 一句同时使用 “Whether not to … or not”，语法上的否定关系不明确；hasParticles 和 hasIcon 的 “Whether not to show …” 也可能被理解为“是否不显示”。此前将三项译为中性“是否……”但未同时记录此问题，现补充来源和判断依据，避免把它当作已确认的原文修正。

判断依据与边界：

- 官方 Shoot 页对 force 的对应说明为 “Whether to override the effect on the target if already applied”，同样列出 overwrite, ow, override, or，默认 false。这为“是否覆盖已有效果”的中性译法提供了对应机制页依据，并非只凭参数名推断。
- Shoot 页的 hasParticles 和 hasIcon 仍重复同样的 not 表述，无法独立消除 MythicMobs 文档自身的歧义。
- [Bukkit 官方 PotionEffect.hasParticles()](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffect.html#hasParticles()) 的返回说明为 “whether this effect has particles or not”；[PotionEffect.hasIcon()](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffect.html#hasIcon()) 为 “whether this effect has an icon or not”。官方构造器文档也分别将 particles 和 icon 指向这两个状态。这支持把表项写成“是否显示……”这一中性问句，但不构成 MythicMobs 配置值如何传入 Bukkit 的源码证据。
- 本次未取得并核实 MythicMobs 对这两个配置项的官方实现映射，也未进行游戏内验证，因此没有追加“true 一定显示／false 一定隐藏”等方向性结论，也没有擅自将原始归档中的 not 删除。016 的三条中性译文保持不变；开关方向的文档歧义仍应作为上游问题保留。

## table-cell 004：条件中的 true 字面量（2026-10-20）

以下四个 unit-id 的 true 表示条件求值结果，虽可译为“真”，为便于读者对照配置，已在 reviewed/table-cell/004.json 中保留为 true。unless 与 if 的条件方向保持原样。

- da6b46b1e23cf7f16732：The pack is skipped unless every listed condition is true
- c6a1f8692fcd7574da35：The pack is skipped if any listed condition is true
- cf514cfbfc692e5f05e3：`<glob> <condition>`: matching files are skipped unless the condition is true
- b424398d076d836ed551：`<glob> <condition>`: matching files are skipped if the condition is true

## table-cell 025：官方机制标签表中的截断句（2026-10-20）

下列单元的 source 已在句中结束，并与 sources/wiki/original/skills/tags/mechanic-tags.md 的实际表格核对。译文仅翻译原文已有内容；需要标明缺句时用省略号表示，未从其他机制页补写缺失对象、属性或数值。

| unit-id | 原文 |
| --- | --- |
| 40b4f527a87c76d5fd67 | Causes the mob to "mount" the specified targeter as though they were a |
| f9f3014c3959ccec6c38 | Pulls all targeted entities towards the caster with a base velocity, |
| 0f3283b75591dac0ebaf | Shoots a wither skull from the mob towards the target entity or |
| a9c14e213526910e92f2 | Adds an amount to a [variable](ZZURL000ZZ) on the specified |
| 9fc96ccf9ef59dcce01e | Sets a variable to the result of a math equation, where 'x' is the |
| 9c8ae9c0d354685d0d88 | Subtracts an amount to a [variable](ZZURL000ZZ) on the specified |
| 08688f6ef10c0402643d | Applies a potion effect to the target entity, which is usually |
| 985952cac7c8d20f5dd3 | Changes the target color, can only be applied to colorable mobs such as |
| de8786fb456e051df54a | Sets the "stance" attribute of the target Mythic Mob to the given |
| 8e8d9c8fb2fae6e718ae | Applies an absorb shield to the target entity for a percentage of their |

## table-cell 025–031：分批译文核对（2026-10-20）

025–030 各 120 条，031 为 21 条，共 741 条。各文件仅包含 unit-id 到完整中文译文的映射。核对 ID 覆盖、URL 占位符、反引号内容、尖括号变量、数字、颜色及目标选择器标识。原文 027 的固定 unit-id `750d9cc9c58cdedd2900` 中，“this is not true” 的 true 属于普通英语判断，不是配置值；正文自然译为“这一点并不成立”，不保留英文短语或译者说明。此单元由主线程设置显式语义校验例外；其余配置或条件说明中的 true/false 均保留。

## 官方目录与失效资源（2026-10-20）

本批按 2026-10-19 开始归档的官方在线 Wiki 整理。大小写及自动标题别名归并后有 969 个正文/目录页面；API 和 API-Information 接口子树排除。官方 Wiki 持续更新，不声明为随包 5.13.0-SNAPSHOT 的专用版本手册。

部分旧链接、占位图片与示例域名已经失效。实际结果逐项保存在 sources/wiki-coverage.json 和 sources/wiki/assets.json；保留其原地址，没有编造替代段落或图片。可取得的 PNG、GIF、SVG、WebP 等资源保存原始字节及 SHA-256。

官方机制标签索引中的部分句子已在句中截断。译文仅翻译现有文字，用省略号标明截断，不从对应机制页自行补写条件。完整机制页单独收录。

## 数学描述与保真范围

数学表格中 Multiplication、Division、Power、Remainder、Equals、cosine、secant、sine、tangent、minimum、maximum 为可读说明，已逐项翻译；运算符、公式、函数名称和示例保持原样。其他可读短说明通过 file/part_index 定位的人工审核记录补译，不对同名技术标识做全局替换。

英文原文的代码、标识、占位符、数字、颜色和布尔值在渲染前核对。HTML 参考链接按页面位置转换，代码中的地址保持原样。原站片段不匹配目标章节时保留官方地址，并记录在 sources/wiki/link-issues.json。

本批为文档翻译核对，未进行 Minecraft 服务端或客户端运行测试。

## Spawners 页的原始坏链接

官方正文中的 `[Commands](/commands and permissions)` 是含空格的根相对地址，未指向已确认的 MythicMobs 命令页。译文将其归于原官方站点并把空格编码为 `%20`，保留原路径，不将其误当成本中文站的根目录，也不猜测替换目标。该项同样列入 link-issues.json。
