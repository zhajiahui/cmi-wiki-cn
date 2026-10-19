---
title: 占位符
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/Placeholders
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 占位符

这些是你可以在使用字符串的技能和机制中使用的所有占位符和特殊字符。底部有一些用法示例可以帮助你入门。

**注意：技能中的许多变量仅限 Premium 版本使用，MMOCore、特殊字符、颜色代码和 `setvariable` 除外**。

1. [特殊字符](placeholders.md#special-characters)
2. [颜色代码](placeholders.md#color-codes)
3. [其他占位符](placeholders.md#additional-placeholders)
4. [占位符](placeholders.md#placeholders)
   1. [作用域占位符](placeholders.md#scoped-placeholders)
   2. [其他占位符](placeholders.md#misc-placeholders)
   3. [物品占位符](placeholders.md#item-placeholders)
   4. [分数占位符](placeholders.md#score-placeholders)
   5. [文本占位符](placeholders.md#text-placeholders)
   6. [变量占位符](placeholders.md#variable-placeholders)
5. [元占位符](placeholders.md#meta-placeholders)
6. [占位符属性](placeholders.md#placeholder-attributes)
   1. [所有占位符](placeholders.md#all-placeholders)
   2. [双返回类型占位符](placeholders.md#double-return-type-placeholders)
7. [PlaceholderAPI 集成](placeholders.md#placeholderapi-integration)
   1. [PlaceholderAPI 解析](placeholders.md#placeholderapi-parsing)
8. [自定义占位符](placeholders.md#custom-placeholders)
9. [静态占位符](placeholders.md#static-placeholders)
   1. [加载时静态占位符解析](placeholders.md#load-time-static-placeholder-parsing)
10. [示例](placeholders.md#examples)

# 特殊字符 {#special-characters}

| **占位符** | **功能** | 符号 |
| --- | --- | --- |
| <&co> | 返回冒号 | `:` |
| <&sq> | 返回单引号 | `'` |
| <&da> | 返回短横线 | `-` |
| <&bs> | 返回反斜杠 | `\` | |
| <&fs> | 返回正斜杠 | `/` |
| <&sp> | 返回空格 |  |
| <&cm> | 返回逗号 | `,` |
| <&sc> | 返回分号 | `;` |
| <&eq> | 返回等号 | `=` |
| <&dq> | 返回双引号 | `"` |
| <&rb> | 返回右方括号 | `]` |
| <&lb> | 返回左方括号 | `[` |
| <&rc> | 返回右花括号 | `}` |
| <&lc> | 返回左花括号 | `{` |
| <&nm> | 返回井号 | `#` |
| <&nl> | 强制换行 |  |
| <&heart> | 返回爱心符号 | `❤` |
| <&skull> | 返回骷髅与交叉骨符号 | `☠` |
| <&lt> | 返回小于号 | `<` |
| <&gt> | 返回大于号 | `>` |
| <^dot> | 返回句点 | `.` |
| <^dot2> | 返回用于生成句点的占位符，适合需要谨慎处理占位符解析的情况 | `<^dot>` |

# 颜色代码 {#color-codes}

这些颜色代码可用于生物文件和技能文件中的任何位置，甚至也能正确设置命令技能中 tellraw 命令的文本格式！

旧版颜色代码：

| **代码** | **颜色** | **代码** | **颜色** |
| --- | --- | --- | --- |
| &0 | 黑色 | &B | 青色 |
| &1 | 深蓝色 | &C | 红色 |
| &2 | 深绿色 | &D | 浅紫色 |
| &3 | 深青色 | &E | 黄色 |
| &4 | 深红色 | &F | 白色 |
| &5 | 深紫色 | &K | 混淆 |
| &6 | 金色 | &L | 粗体 |
| &7 | 灰色 | &M | 删除线 |
| &8 | 深灰色 | &N | 下划线 |
| &9 | 蓝色 | &O | 斜体 |
| &A | 绿色 | &R | 重置 |

建议使用 [MiniMessage 标签](https://docs.adventure.kyori.net/minimessage/format.html#standard-tags)设置文本样式和装饰效果。以下是使用 MiniMessage 标签的示例：

```yml
MessageSkill:
  Skills:
    - message{m=<rainbow>This text is a rainbow</rainbow> but <red>this is red</red>!} @target
    - message{m=<#bae5f4>This is a cool color that I picked from</#bae5f4> <red><click:open_url:https://www.color-hex.com/color/bae5f4>color-hex site</click></red>} @target
```

MiniMessage 还有一个[网页预览器](https://webui.adventure.kyori.net/)，可以预览文本在游戏中的显示效果。

MiniMessage 标签内部的占位符也会被解析，例如 `<head:<target.name>>`。

# 额外占位符 {#additional-placeholders}

以下链接列出了扩展插件提供的占位符。只有安装对应插件后，这些占位符才能使用。

- [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Placeholders)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#placeholders)

# 占位符 {#placeholders}

## 带作用域的占位符 {#scoped-placeholders}

大多数从“环境中”获取数据的占位符都有一个 `scope` 前缀。作用域用于告诉占位符要从*哪个实体或位置*获取数据。

::include{file=/Skills/Placeholders/Scoped-Placeholder-Table.md}

例如，`<caster.name>` 返回该技能机制施法者的名称；`<target.name>` 同样返回名称，但返回的是该技能机制目标的名称

```yaml
  Skills:
  - message{m=Hello <target.name>, i am <caster.name>} @NearestPlayer
```

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v6"></path><path d="M12 17h.01"></path></svg>{scope}

在下面的列表中，占位符以 [{scope}](placeholders/scoped-placeholder-table.md) 开头，表示此处可使用上述*任意*作用域


<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 8h.01"></path></svg>Other words in `[]`

如果看到 `[]` 内写着其他内容（例如 `[auraname]`），使用占位符时就要在此处填入所需的信息。例如，`[auraname]` 应替换为要检查的光环名称：`<caster.aura.youraura.stacks>`。

| 占位符 | 功能 | 返回类型 |
| --- | --- | --- |
| <[{scope}](placeholders/scoped-placeholder-table.md).absorption> | 返回实体当前的伤害吸收生命值（金色生命值）；没有时返回 0。别名：`absorb` | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).armor> | 返回实体的护甲值 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).attack_cooldown> | 返回玩家装备物品的攻击冷却值，结果为 0（该物品的最大冷却时间）到 1（没有冷却）之间的双精度浮点数 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).aura.`{auraName}`.stacks> | 返回实体上指定光环的叠加层数 | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).block.data> | 返回该位置方块的数据 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).block.hardness> | 返回该位置方块的硬度 | Float |
| <[{scope}](placeholders/scoped-placeholder-table.md).block.type> | 返回该位置方块的类型 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).children> | 返回实体所有子实体的 UUID 列表 | List |
| <[{scope}](placeholders/scoped-placeholder-table.md).children.size> | 返回实体拥有的子实体数量 | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).cinematic.active> | 返回玩家是否正处于过场镜头中（`true`/`false`） | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).cinematic.frame> | 返回当前过场镜头开始后经过的刻数；没有正在播放的过场镜头时返回 `-1` | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).cinematic.progress> | 返回当前过场镜头的播放进度，范围为 `0.0` 到 `1.0`；没有正在播放的过场镜头时返回 `0.0` | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).damage> | 返回实体的 Attack_Damage 属性值 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).display> | 返回实体的显示名称 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).distance> | 返回实体与施法者之间的距离 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).distancesquared> | 返回实体与施法者之间距离的平方。实际使用中通常用不到此值。 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).enchantlevel.`{enchantname}`> | 返回实体身上指定附魔的总等级（将所有槽位上的等级相加） | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).item> | 对于掉落物实体，返回其物品 | Item |
| <[{scope}](placeholders/scoped-placeholder-table.md).item.amount> | 对于掉落物实体，返回物品数量；其他实体返回 0 | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).item.model> | 对于掉落物实体，返回物品的自定义模型数据；其他实体返回 0 | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).item.itemstack.`{slot}`> | 返回实体 `slot` 槽位中物品的物品堆叠 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).item.type> | 对于掉落物实体，返回物品类型；其他实体返回 AIR | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).itemcount.`{material/item}`> | 返回玩家背包中指定原版材质或 Mythic 物品 ID 的物品数量 | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).entity_type> | 返回实体类型 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).faction> | 返回实体的阵营 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).fovoffset{rotation=0;absolute=true}> | 返回施法者视线方向与施法者指向目标实体的方向之间的夹角，以度为单位。可用此偏角判断目标偏离施法者视野中心的程度 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).globalcooldown> | 返回实体的全局冷却 | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).hp> | 返回实体的生命值 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).php> | 返回实体的生命值百分比 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).mhp> | 返回实体的最大生命值 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).heldenchantlevel.`{enchantname}`> | 返回实体 HAND 槽位中指定附魔的等级 | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).held.item> | 返回实体手持的物品 | Item |
| <[{scope}](placeholders/scoped-placeholder-table.md).input.`{inputType key}`> | 返回玩家实体是否正在按下指定的 `{inputType key}`。可用按键为 `forward`、`backward`、`left`、`right`、`jump`、`sneak`、`sprint`。按下时返回 `1`，否则返回 `0` | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).lastsignal> | 返回实体最后收到的信号 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).level> | 返回实体的 Mythic 等级 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).l.pitch> | 返回该位置的 pitch（俯仰角） | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).l.yaw> | 返回该位置的 yaw（偏航角） | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).l.w> | 返回该位置所在的世界 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).l.x> | 返回该位置居中后的 x 坐标 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).l.x.double> | 返回该位置的精确 x 坐标 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).l.y> | 返回该位置居中后的 y 坐标 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).l.y.double> | 返回该位置的精确 y 坐标 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).l.z> | 返回该位置居中后的 z 坐标 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).l.z.double> | 返回该位置的精确 z 坐标 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).luck> | 返回实体的幸运值 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).mythic_type> | 返回实体的 Mythic 类型（Mythic 内部 ID） | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).name> | 返回实体名称 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).pity.`{category}`> | 返回实体在指定类别中的保底值 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).raytrace{maxdistance=4.5}> | 返回实体视线内、`maxdistance` 范围内的方块名称（默认范围为 `4.5`）。未找到方块时返回 `AIR`。 |  |
| <[{scope}](placeholders/scoped-placeholder-table.md).skill.`{Metaskill}`.cooldown> | 以浮点数返回实体指定技能的当前冷却值 | Float |
| <[{scope}](placeholders/scoped-placeholder-table.md).stance> | 返回实体当前的姿态 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).stat.[Stat]> | 返回实体上指定 {Stat} 的值 | Float |
| <[{scope}](placeholders/scoped-placeholder-table.md).threat> | 返回施法者对该实体的仇恨值 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).throwstrength.`{component}`> | 返回投掷上下文中的投掷力度。`{component}`：`horizontal`、`vertical` 或 `total`（默认） | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).tt.top> | 返回该实体仇恨值最高对象的名称 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).tt.size> | 返回该实体仇恨表中的实体数量 | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).type> | 若为 MythicMob，返回其内部 ID；否则返回实体名称 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).type.name> | 若为 MythicMob，返回其显示名称；否则返回实体名称 | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).uuid> | 返回实体的 UUID | String |
| <[{scope}](placeholders/scoped-placeholder-table.md).velocity> | 返回实体的速度 | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).velocity.global.`{component}`> | 返回实体在世界坐标系中的速度。`{component}`：`x`、`y`、`z` 或 `total`（默认） | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).velocity.relative.`{component}`> | 返回实体在自身局部坐标系中的速度。`{component}`：`x`、`y`、`z` 或 `total`（默认） | Double |
| <[{scope}](placeholders/scoped-placeholder-table.md).ydiff> | 返回施法者与该位置之间 y 坐标的差值 | Double |

## 杂项占位符 {#misc-placeholders}

| 占位符 | 功能 | 返回类型 |
| --- | --- | --- |
| <drop.amount> | 在特定掉落类型中使用时，返回掉落数量 |  |
| <drops.xp> | 返回特定掉落类型掉落的经验值 |  |
| <drops.money> | 返回通过 vault 插件掉落的金钱 |  |
| <echo.[text]> | 解析给定文本中的占位符后，返回该文本 | String |
| <random.#to#> | 返回指定范围内的随机整数 |  |
| <random.float.#to#> | 返回指定范围内的随机浮点数 |  |
| <random.float.rounded.#to#> | 返回指定范围内的随机浮点数，并四舍五入到 2 位小数 | String |
| <random.uuid> | 返回随机 UUID | String |
| <utils.epoch> | 返回当前的 Unix 时间戳 | Long |
| <utils.epoch.seconds> | 返回当前的 Unix 时间戳 | Long |
| <utils.epoch.timestamp> | 返回自 Unix 纪元起经过的毫秒数 | Long |
| <utils.epoch.millis> | 返回当前 Unix 时间戳的毫秒部分 | Long |
| <utils.epoch.ticks> | 将当前 Unix 时间戳换算为刻并返回，假定服务器始终保持每秒 20 刻，且计入毫秒部分。虽然这种用法不常见，但 Minecraft（以及 Mythic）以刻计时；当大量处理普通时间戳并换算为刻较为繁琐时，此值有助于简化流程 | Long |
| <skill.[skill].charges> | 返回施法者指定技能的可用充能次数 | Integer |
| <skill.[skill].maxcharges> | 返回指定技能配置的最大充能次数 | Integer |
| <skill.[skill].overflowcharges> | 返回施法者指定技能的溢出充能次数 | Integer |
| <skill.power> | 返回此占位符所在元技能的[强度](../mobs/power.md) | Float |
| <skill.targets> | 返回继承的目标数量 | Integer |
| <spawner.pir> | 返回刷怪点范围内的玩家数量 | Integer |
| <char.[code]> | 返回指定 Unicode 编码对应的字符（省略 `U+`）：`<char.007B>` 返回 `{`。也支持超过 FFFF 的编码，例如 `<char.1F600>`。编码可以以 `\u` 开头，但在 YAML 双引号内不可这样使用。`<&lc>` 等[特殊字符](placeholders.md#special-characters)会在其他所有占位符之前替换。若在另一个占位符内部使用，应改用 `<char>`，因为它会在稍后替换。对于 [MythicCrucible 字体图片](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/ResourcePack/ResourcePack-Generator#fonts)，应使用 `<fontimage.NAME>`，而不是其编码 | String |

## 物品占位符 {#item-placeholders}

| 占位符 | 功能 | 返回类型 |
| --- | --- | --- |
| <item.amount> | 返回触发技能的物品数量 | Integer |
| <item.droplevel> | 若为掉落物，返回物品的掉落等级；否则与 `<item.amount>` 的行为相同 | Integer |
| <[{scope}](placeholders/scoped-placeholder-table.md).slot.item.[slot]> | 将实体 `[slot]` 中的物品返回为支持逐层访问的物品值，可继续使用物品元数据关键字，例如 `<caster.slot.item.HAND.amount>`。`[slot]` 可为装备槽位名（`HAND`、`OFFHAND`、`HEAD`、`CHEST`、`LEGS`、`FEET`），玩家也可使用背包槽位编号。槽位为空时返回 AIR | Item |
| <mythicitem.[MythicItem].material> | 返回指定 Mythic 物品的材质 | String |
| <mythicitem.[MythicItem].model> | 返回指定 Mythic 物品的 custommodeldata | String |
| <mythicitem.[MythicItem].display> | 返回指定 Mythic 物品的显示名称 | String |
| <mythicitem.[MythicItem].lore> | 返回指定 Mythic 物品的描述，各行与物品描述逐行对应。描述中的占位符会被解析 | String |
| <mythicitem.[MythicItem].itemstack> | 返回指定 Mythic 物品的物品堆叠 | String |

## 计分板分数占位符 {#score-placeholders}

| 占位符 | 功能 | 返回类型 |
| --- | --- | --- |
| <[{scope}](placeholders/scoped-placeholder-table.md).score.[Objective]> | 返回当前作用域实体在 "{Objective}" 中的分数 | Integer |
| <global.score.[Objective]> | 返回虚拟玩家 __GLOBAL__ 在 "{Objective}" 中的分数 | Integer |
| <score.objective.player> | 返回指定玩家在 "objective" 中的分数 | Integer |
| <score.objective.dummyname> | 返回 "dummyname"（虚拟玩家）在 "objective" 中的分数 | Integer |

## 文本占位符 {#text-placeholders}

| 占位符 | 功能 | 返回类型 |
| --- | --- | --- |
| <bar{value=0;maxValue=100;length=100;remainingSymbol="#";progressSymbol="#";remainingPrefix=;progressPrefix=}> | 返回使用指定数值格式化后的进度条 | String |
| <centertext{value=The text to center;pixelwidth=100;singlepixelunicodes= , , , ;bold=false}> | 将指定文本居中。属性包括：`value/v/text/line`：要居中的文本；`pixelwidth/width/w/pw`：计算时使用的总像素宽度（整数，居中位置为宽度的一半）；`bold/b`：指定的文本是否加粗；`singlepixelunicodes/spus`：用于提高精度的 1-3 像素宽 Unicode 字符列表，默认为 `" , , , "` | String |

## 变量占位符 {#variable-placeholders}

这些占位符将返回已调用的任何变量。例如<caster.var.[name]>将返回施法者的[name]变量的值。

| 变量占位符 | 功能 | 返回类型 | 生成来源 |
| --- | --- | --- | --- |
| <dialog.[key]> | 返回技能变量 `dialog.[key]`：按输入项的 `Key` 取得输入值、取得[可点击文本](../dialogs.md#clickable-text)参数，或取得传入对话框的值。`<dialog.button>`：点击的按钮编号，从 0 开始；`ExitButton` 为 `-1`，可点击文本为 `-2`。`<dialog.page>`、`<dialog.pages>`：当前页码和总页数，仅用于带有 `PageSize` 的对话框 | String | [showDialog](mechanics/showdialog.md) 技能机制 |
| <caster.var.[VariableName]> | 返回技能机制施法者的变量注册表中 {VariableName} 变量的值 |  |  |
| <target.var.[VariableName]> | 返回技能机制目标的变量注册表中 {VariableName} 变量的值 |  |  |
| <world.var.[VariableName]> | 返回技能机制所在世界的变量注册表中 {VariableName} 变量的值 |  |  |
| <global.var.[VariableName]> | 返回整个服务器的变量注册表中 {VariableName} 变量的值 |  |  |
| <skill.var.[VariableName]> | 返回当前[技能树](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/SkillTrees)中 {VariableName} 变量的值 |  |  |
| <skill.var.damage-amount> | 返回受到或造成的伤害量 |  | [~onDamaged](triggers/ondamaged.md) 触发器；[~onAttack](triggers/onattack.md) 触发器；[~onBowHit](triggers/onbowhit.md) 触发器；[onDamaged](mechanics/ondamaged.md) 技能机制；[onAttack](mechanics/onattack.md) 技能机制 |
| <skill.var.damage-type> | 返回受到或造成的伤害类型（若有）。伤害没有元素类型时，改为返回以逗号分隔的伤害标签；若也没有标签，则返回 `SKILL`。在 onDamaged 执行路径中同样会填入此值 |  | [~onDamaged](triggers/ondamaged.md) 触发器；[~onAttack](triggers/onattack.md) 触发器；[~onBowHit](triggers/onbowhit.md) 触发器；[onDamaged](mechanics/ondamaged.md) 技能机制；[onAttack](mechanics/onattack.md) 技能机制 |
| <skill.var.damage-tags> | 返回以逗号分隔的伤害标签列表（若有） |  | [~onDamaged](triggers/ondamaged.md) 触发器；[~onAttack](triggers/onattack.md) 触发器；[~onBowHit](triggers/onbowhit.md) 触发器；[onDamaged](mechanics/ondamaged.md) 技能机制；[onAttack](mechanics/onattack.md) 技能机制 |
| <skill.var.damage-cause> | 返回受到或造成伤害的原因 |  | [~onDamaged](triggers/ondamaged.md) 触发器；[~onAttack](triggers/onattack.md) 触发器；[~onBowHit](triggers/onbowhit.md) 触发器；[onDamaged](mechanics/ondamaged.md) 技能机制；[onAttack](mechanics/onattack.md) 技能机制 |
| <skill.var.aura-name> | 返回光环名称 |  | 所有[光环](mechanics/aura.md)技能机制 |
| <skill.var.aura-type> | 返回光环类型 |  | 所有[光环](mechanics/aura.md)技能机制 |
| <skill.var.aura-charges> | 返回光环的剩余充能次数 |  | 所有[光环](mechanics/aura.md)技能机制 |
| <skill.var.aura-duration> | 返回光环的剩余持续时间 |  | 所有[光环](mechanics/aura.md)技能机制 |
| <skill.var.aura-duration-millis> | 返回光环的剩余持续时间，以毫秒为单位 |  | 所有[光环](mechanics/aura.md)技能机制 |
| <skill.var.aura-stacks> | 返回光环的剩余叠加层数 |  | 所有[光环](mechanics/aura.md)技能机制 |
| <skill.var.input> | 返回聊天输入内容 |  | [onChat](mechanics/onchat.md) 技能机制 |
| <skill.var.interval> | 返回当前迭代次数 |  | 使用 `repeat` 和 `repeatInterval` [通用属性](mechanics.md#universal-attributes) |
| <skill.var.itr> | 返回当前迭代次数 |  | 使用 `repeat` 和 `repeatInterval` [通用属性](mechanics.md#universal-attributes) |
| <skill.var.volume> | 返回 1 到 15 之间的浮点数，表示声音强度。此值与距离成正比（声源越远，该值越高） |  | [~onHear](triggers/onhear.md) 触发器 |
| <skill.var.sound-type> | 返回声音类型 |  | [~onHear](triggers/onhear.md) 触发器 |
| <skill.var.hit-block-type> | 返回命中的方块；未命中方块时返回 AIR |  | [raytrace](mechanics/raytrace.md) 技能机制 |
| <skill.var.bow-tension> | 返回投射物发射时的力度 |  | [~onShoot](triggers/onshoot.md) 触发器 |
| <skill.var.click-type> | 与[菜单按钮](../custom-menus.md#button-skills)交互时使用的点击类型。右键点击时返回 `1`，否则返回 `0` |  | [自定义菜单](../custom-menus.md#button-skills)交互 |

```yaml
  Skills:
  - setvariable{var=caster.test1;val=1} @self
  - setvariable{var=target.test2;val=2} @self
  - message{m=<caster.var.test1> <caster.var.test2> <target.var.test1> <target.var.test2>} @self
```

> 如果你自己执行这个元技能，就会收到内容为 `1 2 1 2` 的消息。因为每个技能机制的目标都是施法者，所以即使使用“target”作用域，访问的也始终是施法者的变量注册表

# 元占位符 {#meta-placeholders}

你可能会想：“占位符说明后面列出的 `Return Type` 是什么意思？”这个值决定了

- 占位符返回的数据类型，以及由此决定的
- **可以用哪些元占位符来修改它！**

例如，要将字符串转换为大写，可以使用

```yaml
<caster.name.uppercase>
```

要去掉字符串首尾可能存在的空白字符，还可以

```yaml
<caster.name.uppercase.trim>
```

[点击此处查看完整文档](placeholders/meta-placeholders.md)

# 占位符属性 {#placeholder-attributes}

一些占位符可以使用一组属性来进一步定义它们将给出的输出

## 全部占位符 {#all-placeholders}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| default | def, |  | 占位符无法取得预期值时返回的默认值 | UNDEFINED |

## 返回 Double 类型的占位符 {#double-return-type-placeholders}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| rounding | round, r | 返回的双精度浮点数的舍入方式 | 2 |

```yaml
  Skills:
  - message{m="<target.hp{round=2}>"} @self
```

# PlaceholderAPI 集成 {#placeholderapi-integration}

除了能够在支持占位符的任何地方使用 PlaceholderAPI 占位符之外，MythicMobs 还引入了一些新的 PAPI 占位符，第三方可以使用这些占位符来获取 MythicMobs 相关值。

| **PAPI 占位符** | **功能** |
| --- | --- |
| %mythic_var_someVar% | 返回玩家身上设置的 `someVar` 变量值 |
| %mythic_var_world_someVar% | 返回世界中设置的 `someVar` 变量值 |
| %mythic_var_global_someVar% | 返回服务器中设置的 `someVar` 变量值 |
| %mythic_var_<playerName>_someVar% | 按玩家名称返回指定玩家身上设置的 `someVar` 变量值 |
| %mythic_var_<UUID>_someVar% | 按实体 UUID 返回指定实体身上设置的 `someVar` 变量值 |
| %mythic_spawner_[name]_cooldown% | 返回名为 `name` 的刷怪点的冷却时间 |
| %mythic_spawner_[name]_cooldownleft% | 返回名为 `name` 的刷怪点的剩余冷却时间 |
| %mythic_spawner_[name]_warmup% | 返回名为 `name` 的刷怪点的预热时间 |
| %mythic_spawner_[name]_warmupleft% | 返回名为 `name` 的刷怪点的剩余预热时间 |
| %mythic_stat_[name]% | 返回被求值玩家的指定属性值 |

## PlaceholderAPI 解析 {#placeholderapi-parsing}

通过 PlaceholderAPI 使用占位符时，请记住其中一些占位符需要针对玩家解析。如果针对生物解析，可能会出现意外行为。

- 如果在机制内部使用，目标必须是玩家
- 如果在条件中使用，被检查的实体必须是玩家（conditions 检查施法者，targetconditions 检查继承的目标，triggerconditions 检查触发者）

...等等

# 自定义占位符 {#custom-placeholders}

在任意包的目录中创建 `placeholders.yml` 文件，即可定义自定义占位符。可以定义静态占位符，也可以定义按条件取值的占位符：选择第一个判断结果为   true   的项；如果所有项都为   false  ，则使用 `Default`。

自定义占位符可以通过 `<placeholder.[CustomPlaceholder]>` 使用，*[CustomPlaceholder]* 是自定义占位符的名称。

```yaml
TestPlaceholder: 'some value'

TestConditionalPlaceholder:
  Day:
    Conditions:
    - day
    Value: day
  Night:
    Conditions:
    - night
    Value: night
  Default: idk

TestRandomPlaceholder:
- red
- green
- blue
```

> 不接受“  null  ”值

# 静态占位符 {#static-placeholders}

当占位符的解析只能产生单个定义的输出时，占位符被视为“静态”。

截至目前，只有具有单个可能值的 [自定义占位符](placeholders.md#custom-placeholders) 属于这种情况

```yaml
TestPlaceholder: 'a single value'
AnotherTestPlaceholder: 'another single value'
```

## 加载时的静态占位符解析 {#load-time-static-placeholder-parsing}

静态占位符不会等到运行时执行配置行时才解析，而是在加载配置时就立即解析并替换。每次重载只解析一次，且早于其他所有解析步骤。

这有很多优点！

这里还有一种有趣的用法：由于静态占位符*先于其他所有内容*解析并替换，因此它们可以用于配置文件的*任何位置*，包括通常无法使用普通占位符的内部名称、技能机制名称等位置！

```yaml
# placeholders.yml
test: "message=1;"
debug: "#log"
```

```yaml
testPreparsedPlaceholders:
  Skills:
  - message{<placeholder.test>} @self
  - <placeholder.debug>{message="hello world"}
```

# 示例 {#examples}

**这会让生物向自身周围半径 20 格内的所有玩家发送青色消息，并在消息中以绿色显示杀死它的实体。**

```yaml
    Skills:
    - message{m="<&b><caster.name><&r> was slain by <&a><trigger.name><&r>."} @PIR{r=20} ~onDeath
```

**此技能会在生物生成时发布如下公告：**

![image](../assets/5436313bf1e788.png)

```yaml
  Skills:
  - Skill{s=SaveBossLocation} @self ~onSpawn
  - message{m="&eA &BGiant Zombie&e (Level &4<caster.level>&e) &ehas spawned at <caster.var.SpawnLoc>"} ~onSpawn @PlayersInWorld
  - message{m="&eThe &BGiant Zombie&e (Level &4<caster.level>&e) &espawned at <caster.var.SpawnLoc>&e has been slain."} ~onDeath @PlayersInWorld
```

请务必将此技能放置在技能文件中的某个位置

```yaml
SaveBossLocation:
  Skills:
  - setvariable{var=SpawnLoc;type=STRING;value="&b<caster.l.x>&e, &b<caster.l.y>&e, &b<caster.l.z>";scope=CASTER} @self
```

**还可以使用颜色标签和格式标签，为生物设置好看的名称：**

![image](../assets/547ab2bafa0183.png)

```yaml
ZOMBIE:
  Display: 'ZOMBIE &F- &A<caster.hp>/<caster.mhp>HP &F- &ELv.<caster.level>'
```
