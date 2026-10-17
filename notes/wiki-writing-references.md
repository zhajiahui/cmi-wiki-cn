# 中文插件 Wiki 写法参考

调研日期：2026-10-17。用途：为 CMI 忠实中文翻译选择自然、便于查阅的表达方式。
范围：只读其他插件的一手中文文档；未调研 CMI 功能，未建站，未验证游戏内行为。
方法：实际阅读下列 3 站的 6 个功能／指令页；入口页只用于核对维护来源和版本边界。正文均为自行归纳，不复制长段原文。

## 样本与实际阅读页

| 文档站 | 维护来源及版本边界 | 实际阅读页（均访问于 2026-10-17） |
| --- | --- | --- |
| TrMenu 官方中文教程 | [站内介绍](https://temp-17.gitbook.io/trmenu/chinese)自署“官方教程”，并写明教程完全基于 TrMenu v2.x 的旧版 Wiki；这里仅作为历史写法样本，不据此判断现版机制。来源访问：2026-10-17。 | [执行命令](https://temp-17.gitbook.io/trmenu/chinese/actions/actions/command)；[布局](https://temp-17.gitbook.io/trmenu/chinese/menu/structure/layout)。 |
| PlaceholderAPI 中文译文／Continue Project | [前言](https://continue-project.netlify.app/wiki/placeholderapi/)说明原译文曾托管在 MCBBS，当前维护者接手并重新汉化，页面列出贡献者 SnowCutieOwO。来源访问：2026-10-17。 | [命令](https://continue-project.netlify.app/wiki/placeholderapi/user-guides/commands)；[使用变量](https://continue-project.netlify.app/wiki/placeholderapi/user-guides/using-placeholders)。 |
| QuickShop-Hikari 官方中文文档 | [项目文档入口](https://quickshop-community.github.io/QuickShop-Hikari-Documents/zh-CN/docs/intro)说明文档仍在编辑，提供 Crowdin 翻译计划，并写明 QuickShop-Hikari 由 creatorfromhell 维护。来源访问：2026-10-17。 | [创建与购买](https://quickshop-community.github.io/QuickShop-Hikari-Documents/zh-CN/docs/modules/shops/shop-basic)；[商店权限独立控制](https://quickshop-community.github.io/QuickShop-Hikari-Documents/zh-CN/docs/modules/shops/per-shop-perms-management)。 |

选样说明：优先检查了 ItemsAdder 旧中文入口；访问 [https://itemsadder.devs.beer/chinese](https://itemsadder.devs.beer/chinese) 后跳转至 [https://wiki.itemsadder.com/chinese](https://wiki.itemsadder.com/chinese) 并返回 404，未取得可用的中文功能正文，因此改选 QuickShop-Hikari，ItemsAdder 不计入样本。访问日期：2026-10-17。

## 7 条可用于翻译的参考

下表的建议是样例写法偏好，不是强制页面模板；是否采用须服从 CMI 原文已有信息、顺序和层级。

| 方面 | 一手页面上的具体观察 | 可采用的表达／排版偏好 | 忠实翻译的边界 |
| --- | --- | --- | --- |
| 1. 开头 | TrMenu“执行命令”页直接以“以玩家身份执行命令”说明用途，随后给出节点和示例。来源：https://temp-17.gitbook.io/trmenu/chinese/actions/actions/command；访问：2026-10-17。 | 原文有用途句时，译成短而具体的开头，让读者先知道动作和对象；删掉空泛导语。 | 原文未写的用途、执行身份、适用对象均不补；也不能为了简短删掉条件。 |
| 2. 步骤 | QuickShop“创建与购买”页按“放置容器—左键点击—在聊天栏输入价格—创建商店”的顺序写操作，并在后续小节继续说明补货、切换模式、改价和删除。来源：https://quickshop-community.github.io/QuickShop-Hikari-Documents/zh-CN/docs/modules/shops/shop-basic；访问：2026-10-17。 | 用明确的动词和对象串起步骤；保留原文的小节边界，让点击对象、输入位置和结果容易定位。 | 保留原有顺序、按键、模式和结果；不补猜测的步骤，不把不同功能强行合并成统一流程。 |
| 3. 参数与列表 | PlaceholderAPI“命令”页先说明本页列出命令和功能描述，再按命令分组；每条命令通常依次给出描述、参数和示例。来源：https://continue-project.netlify.app/wiki/placeholderapi/user-guides/commands；访问：2026-10-17。 | 参数多时沿用原文的列表或表格，说明紧贴对应参数；不要为了统一外观把段落全部改成表格。 | 仅保留原文已有的必填、默认值、范围、权限和参数符号；不能根据其他插件的习惯新增列或改变括号含义。 |
| 4. 示例 | TrMenu“执行命令”页把 YAML 示例放在用途和节点之后，并在代码注释中解释用分号分隔多个命令；PlaceholderAPI 命令页把命令示例放在该命令的参数说明之后。来源：https://temp-17.gitbook.io/trmenu/chinese/actions/actions/command；https://continue-project.netlify.app/wiki/placeholderapi/user-guides/commands；访问：2026-10-17。 | 让原有示例和解释保持相邻，中文说明直接指向示例中的动作或参数。 | 不为凑出相同结构新增示例；命令、键、数值和可识别字符串照原文保留，注释只翻译明确可译的部分。 |
| 5. 前置条件与提示 | PlaceholderAPI“使用变量”页先分节说明插件支持情况、网络连接和变量拓展来源，并标注某项功能自 2.11.4 起加入；QuickShop 权限页在编辑组权限前用 caution 警告配置不当可能导致插件停止工作。来源：https://continue-project.netlify.app/wiki/placeholderapi/user-guides/using-placeholders；https://quickshop-community.github.io/QuickShop-Hikari-Documents/zh-CN/docs/modules/shops/per-shop-perms-management；访问：2026-10-17。 | 把前置条件放在相关操作之前；已有提示框就保留其位置和语气，明确触发条件、版本和后果。 | 提示只承载原文已有的限制和补充；不凭经验增加警告、升级风险或其他版本限制。 |
| 6. 术语与代码 | PlaceholderAPI“使用变量”页把变量、变量拓展、`/papi` 命令和环境变量分开说明；TrMenu“布局”页用中文解释 `Layout`、`PlayerInventory` 等配置项。来源：https://continue-project.netlify.app/wiki/placeholderapi/user-guides/using-placeholders；https://temp-17.gitbook.io/trmenu/chinese/menu/structure/layout；访问：2026-10-17。 | 普通叙述使用项目已经确认的中文称呼；配置键、命令、权限节点、变量和路径使用行内代码，方便对照。 | 不把其他站的译名直接定为 CMI 术语；未确认的专名先保留原名，不翻译程序识别字符串。 |
| 7. 章节收尾 | TrMenu“执行命令”页在示例后结束，“布局”页以布局限制和“标识图标的字符支持汉字”收尾，没有另加总结段。来源：https://temp-17.gitbook.io/trmenu/chinese/actions/actions/command；https://temp-17.gitbook.io/trmenu/chinese/menu/structure/layout；访问：2026-10-17。 | 原文讲完即可结束，让最后的示例、限制或注意事项承担收尾作用，避免机械重复。 | 不为了显得简洁删掉原文总结或链接；也不新增总结、推荐、FAQ、进阶用法或下一步。 |

## 使用时的取舍

- 编辑判断：自然感主要取自具体动词、清楚的指代和便于定位的说明；这是本记录的写法选择，不是对作者身份或读者效果的实证结论。
- 不整站照搬：QuickShop 权限页仍有英文残留、重复的“默认商店权限组”小节及命名不完全一致的权限项，适合作为局部结构参考。来源：https://quickshop-community.github.io/QuickShop-Hikari-Documents/zh-CN/docs/modules/shops/per-shop-perms-management；访问：2026-10-17。
- 原文缺少的信息继续留空；疑点和改写建议放进翻译备注，不混入正文。语言风格调整不得改变事实、示例逻辑、警告或版本范围。
- 本轮仅核对页面正文、维护来源与以上写法观察；未将这些插件的命令或机制作为 CMI 的资料依据。
