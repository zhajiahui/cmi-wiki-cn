---
title: 区域旗标
source_url: https://worldguard.enginehub.org/en/latest/regions/flags/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 区域旗标 { #region-flags }

可以为区域设置旗标。例如：

- 用 `pvp` 旗标禁止玩家之间战斗

- 用 `entry` 旗标禁止进入区域

- 用 `snow-melt` 旗标禁止雪融化

- 用 `receive-chat` 旗标禁止区域内玩家接收聊天消息

- 用 `vine-growth` 旗标停止藤蔓生长

同一个区域可以同时设置多个不同旗标，但每个旗标同一时间只能有一个值。使用 `/region flag`，或其别名 `/rg flag` 设置旗标。以下以“spawn”和“hospital”区域为例：

```text
/region flag spawn pvp deny
/region flag spawn greeting Welcome to spawn!
/rg flag hospital heal-amount 2
/rg flag hospital heal-delay 1
```

不指定值即可移除旗标设置：

```text
/rg flag spawn pvp
```

使用“flags”命令列出旗标：

```text
/rg flags spawn
```

命令在游戏内的输出支持交互。点击旗标值可修改设置，点击底部箭头可以翻页。

<a id="contents"></a>

- [区域组](#region-groups)

- [旗标类型](#types-of-flags)

- [旗标冲突](#conflicting-flags)

- [旗标默认值](#default-values-of-flags)

- [旗标列表](#flag-listing)



  - [覆盖规则](#overrides)

  - [保护相关](#protection-related)

  - [生物、火焰与爆炸](#mobs-fire-and-explosions)

  - [自然事件](#natural-events)

  - [移动](#movement)

  - [地图制作](#map-making)

  - [其他](#miscellaneous)

<a id="id1"></a>

## 区域组 { #region-groups }

有时，希望旗标只影响特定一组玩家，而非所有进入区域的人。这可以通过设置旗标时额外指定“区域组”来实现。

区域组表示玩家是否属于某个区域。它们由 WorldGuard 在内部处理，与权限组完全无关。

可用的区域组如下：

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">区域组</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">all</td>
<td markdown="span">所有人</td>
</tr>
<tr>
<td markdown="span">members</td>
<td markdown="span">区域的成员和所有者</td>
</tr>
<tr>
<td markdown="span">owners</td>
<td markdown="span">区域的所有者</td>
</tr>
<tr>
<td markdown="span">nonmembers</td>
<td markdown="span">既不是区域所有者，也不是成员的所有人</td>
</tr>
<tr>
<td markdown="span">nonowners</td>
<td markdown="span">不是区域所有者的所有人</td>
</tr>
</tbody>
</table>

使用 `-g` 指定区域组，如下所示：

```text
/region flag spawn -g nonmembers pvp deny
```

在同一个区域中，**无法**为多个区域组分别给同一个旗标设置不同的值。如有这种需求，可考虑创建多个区域。

!!! note "注意"

    多个区域重叠时，玩家必须属于*设置该旗标的区域*，或在存在继承关系时属于*该区域的某个子区域*。详见[优先级与继承](priorities.md)。

!!! tip "提示"

    `entry` 和 `exit` 默认针对“non-member”，因此设为“deny”会禁止非成员进入或离开区域。位置旗标 `spawn` 默认针对“members”，即默认只有成员可以使用。`nonplayer-protection-domains` 不支持区域组。WorldGuard 提供的其他所有旗标默认针对“everyone”。

## 旗标类型 { #types-of-flags }

每个旗标都有特定类型，决定它接受什么值。例如，`heal-amount` 是整数旗标，因此只能设置整数。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">类型</th>
<th markdown="span">可用值</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">state</td>
<td markdown="span">‘allow’ 或 ‘deny’，后文会解释</td>
</tr>
<tr>
<td markdown="span">string</td>
<td markdown="span">任意文本</td>
</tr>
<tr>
<td markdown="span">integer</td>
<td markdown="span">不带小数的数字，例如 5，而不是 5.5</td>
</tr>
<tr>
<td markdown="span">double</td>
<td markdown="span">可以带小数的数字，例如 5、5.5、2.425</td>
</tr>
<tr>
<td markdown="span">location</td>
<td markdown="span">世界中的一个位置</td>
</tr>
<tr>
<td markdown="span">boolean</td>
<td markdown="span">True 或 false</td>
</tr>
<tr>
<td markdown="span">set</td>
<td markdown="span">由不重复条目组成的列表</td>
</tr>
</tbody>
</table>

内部还有更多类型，但一般无需关心。

!!! tip "提示"

    大多数字符串旗标接受 `\n` 作为换行符。例如，可通过 `greeting`/`farewell` 发送多行文本，或通过 `greeting-title` 和 `farewell-title` 发送标题与副标题。

    它们也可能接受颜色代码：旧式 `&[0-9a-f]`，或以 <code>&#96;[RrYyGgCcBbPp012w]</code> 表示深红、红、暗黄、黄等颜色；<code>[&amp;&#96;][klmnox]</code> 则用于随机字符、粗体、删除线、下划线和斜体。

    它们也可能接受替换变量，例如 `%name%` 为玩家名称、`%world%` 为世界名称、`%online%` 为玩家数量、`%id%` 为玩家 UUID、`%health%` 为玩家当前生命值。

示例：使用字符串格式选项

将 spawn 的 `greeting-title` 设为带有格式的欢迎消息：

```text
/rg flag spawn greeting-title `bWelcome to spawn!\n`YEnjoy your stay in `g`n%world%`x, `C%name%`Y!
```

## 旗标冲突 { #conflicting-flags }

同一位置可能有多个重叠区域，而且同一旗标的值不同。此时按以下规则决定使用哪个值：

- **如果**区域本身没有设置该旗标，就会从父区域继承。注意，`build` 会根据成员关系隐式设置。

- 高优先级区域覆盖低优先级区域。

- 全局区域与其他区域按同样方式处理，但优先级始终最低。

按上述规则处理后，旗标值仍可能冲突，例如两个重叠区域优先级相同。此时按旗标类型决定最终值：

- 对于状态旗标，只要存在 `deny`，结果就是 `deny`；否则，只要存在 `allow`，最终值就是 `allow`。

- 其他类型的旗标结果未定义。因此，不要在同一位置、相同优先级的区域中设置两条不同的欢迎消息等。

## 旗标默认值 { #default-values-of-flags }

旗标可以有默认值。当所有影响本次操作的区域中，都未针对操作主体所属的区域组设置该旗标时，就会使用默认值。默认行为会选择最合理的方式。例如，未定义 `item-pickup` 时，WorldGuard 默认允许拾取。可以用前文介绍的“flags”命令在游戏内查看默认值。状态旗标要么默认允许，要么没有默认值。通常，下方列出的保护相关旗标没有默认值，`build` 例外；其他状态旗标通常默认允许。`build` 很特殊：它的默认值取决于操作主体的区域成员关系。只要影响某项操作的最高优先级区域没有显式设置它，就会隐式设置。这就是默认允许成员和所有者建造、而不允许非成员建造的原因。其他保护相关旗标始终与 build 旗标共同检查，因此它们的默认行为取决于 build 的最终结果。

!!! tip "提示"

    大多数时候无需设置任何旗标。只有想改变默认行为，或覆盖其他区域已设置的旗标时，才应设置。尤其不要靠设置保护相关旗标来完整保护或取消保护某个区域，应改用成员关系或 `passthrough`。

## 旗标列表 { #flag-listing }

下方按类别列出旗标。

<a id="flag-overrides"></a>

### 覆盖规则 { #overrides }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">旗标</th>
<th markdown="span">类型</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">passthrough</td>
<td markdown="span">state</td>
<td markdown="block">

<p markdown="span">此旗标是“passthrough build”的缩写，与玩家移动无关。</p> <ul markdown="block"> <li markdown="span"><p markdown="span">未设置时**（默认）**，区域会保护其范围。</p> </li> <li markdown="span"><p markdown="span">设为 `deny` 时，区域会保护其范围。</p> </li> <li markdown="span"><p markdown="span">设为 `allow` 时，区域**不再**保护其范围。</p> </li> </ul> <p markdown="span">何时需要使用此旗标？</p> <ul markdown="block"> <li markdown="span"><p markdown="span">想使用 PvP、治疗等其他旗标，但不想禁止建造时。</p> </li> <li markdown="span"><p markdown="span">为什么不直接将 `build` 设为 `allow`（后文会解释）？因为那会覆盖其他区域，并让玩家可以建造！</p> </li> </ul>

</td>
</tr>
<tr>
<td markdown="span">nonplayer-protection-domains</td>
<td markdown="span">字符串集合</td>
<td markdown="block">

<p markdown="span">活塞等非玩家关联对象，通常被视为其所在的所有区域的成员，或仅被视为最高优先级区域的成员，具体取决于[配置](../config.md)中的 `use-max-priority-association`，以及是否为[全局区域](global-region.md)。因此，区域之间可能形成边界，使活塞无法将方块从一个区域推入另一个区域。</p> <p markdown="span">可以通过设置各区域的 `nonplayer-protection-domains`，为非玩家关联对象消除这种边界。此旗标是一组字符串，描述区域所属的保护域。如果一个非玩家关联对象是某个区域的成员，且该区域与另一个区域至少共有一个保护域，那么它也会视为另一个区域的成员。</p>

</td>
</tr>
</tbody>
</table>

### 保护相关 { #protection-related }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">旗标</th>
<th markdown="span">类型</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">build</td>
<td markdown="span">state</td>
<td markdown="block">

<p markdown="span">所有操作：</p> <ul markdown="block"> <li markdown="span"><p markdown="span">是否允许挖掘或放置方块</p> </li> <li markdown="span"><p markdown="span">是否允许使用门、拉杆等方块，不包括容器</p> </li> <li markdown="span"><p markdown="span">是否允许与实体和方块交互</p> </li> <li markdown="span"><p markdown="span">是否允许玩家之间战斗</p> </li> <li markdown="span"><p markdown="span">是否允许在床上睡觉</p> </li> <li markdown="span"><p markdown="span">是否允许打开容器</p> </li> <li markdown="span"><p markdown="span">是否允许放置船、矿车等载具</p> </li> <li markdown="span"><p markdown="span">等等。</p> </li> </ul>

</td>
</tr>
<tr>
<td markdown="span">interact</td>
<td markdown="span">state</td>
<td markdown="block">

<p markdown="span">所有涉及“使用”方块或实体的操作：</p> <ul markdown="block"> <li markdown="span"><p markdown="span">是否允许使用门、拉杆等方块，不包括容器</p> </li> <li markdown="span"><p markdown="span">是否允许骑乘载具，包括动物</p> </li> <li markdown="span"><p markdown="span">等等。</p> </li> </ul>

</td>
</tr>
<tr>
<td markdown="span">block-break</td>
<td markdown="span">state</td>
<td markdown="span">是否允许破坏方块</td>
</tr>
<tr>
<td markdown="span">block-place</td>
<td markdown="span">state</td>
<td markdown="span">是否允许放置方块</td>
</tr>
<tr>
<td markdown="span">use</td>
<td markdown="span">state</td>
<td markdown="span">是否允许使用门、拉杆等方块，不包括容器</td>
</tr>
<tr>
<td markdown="span">damage-animals</td>
<td markdown="span">state</td>
<td markdown="span">是否允许玩家伤害牛、羊等友好动物</td>
</tr>
<tr>
<td markdown="span">chest-access</td>
<td markdown="span">state</td>
<td markdown="span">是否允许打开容器</td>
</tr>
<tr>
<td markdown="span">ride</td>
<td markdown="span">state</td>
<td markdown="span">是否允许骑乘载具，包括动物</td>
</tr>
<tr>
<td markdown="span">pvp</td>
<td markdown="span">state</td>
<td markdown="span">是否允许玩家之间战斗</td>
</tr>
<tr>
<td markdown="span">sleep</td>
<td markdown="span">state</td>
<td markdown="span">是否允许在床上睡觉</td>
</tr>
<tr>
<td markdown="span">respawn-anchors</td>
<td markdown="span">state</td>
<td markdown="span">是否允许激活重生锚</td>
</tr>
<tr>
<td markdown="span">tnt</td>
<td markdown="span">state</td>
<td markdown="span">是否允许 TNT 引爆或破坏方块</td>
</tr>
<tr>
<td markdown="span">vehicle-place</td>
<td markdown="span">state</td>
<td markdown="span">是否允许放置船、矿车等载具</td>
</tr>
<tr>
<td markdown="span">vehicle-destroy</td>
<td markdown="span">state</td>
<td markdown="span">是否允许摧毁载具</td>
</tr>
<tr>
<td markdown="span">lighter</td>
<td markdown="span">state</td>
<td markdown="span">是否允许使用打火石或火焰弹</td>
</tr>
<tr>
<td markdown="span">block-trampling</td>
<td markdown="span">state</td>
<td markdown="span">是否允许踩坏耕地、海龟蛋或嗅探兽蛋</td>
</tr>
<tr>
<td markdown="span">frosted-ice-form</td>
<td markdown="span">state</td>
<td markdown="span">玩家穿着冰霜行者靴子时是否会形成冰</td>
</tr>
<tr>
<td markdown="span">item-frame-rotation</td>
<td markdown="span">state</td>
<td markdown="span">是否允许旋转物品展示框中的物品</td>
</tr>
<tr>
<td markdown="span">firework-damage</td>
<td markdown="span">state</td>
<td markdown="span">烟花是否能对实体造成伤害</td>
</tr>
<tr>
<td markdown="span">use-anvil</td>
<td markdown="span">state</td>
<td markdown="span">是否允许使用铁砧</td>
</tr>
<tr>
<td markdown="span">use-dripleaf</td>
<td markdown="span">state</td>
<td markdown="span">是否允许使用垂滴叶</td>
</tr>
</tbody>
</table>

!!! warning "警告"

    这些旗标都不是只针对玩家的。例如，将 `block-break` 设为 deny，**也会阻止活塞破坏方块**。

    理解这一点时，可以想想：玩家能从区域外向区域内发射 TNT，也能造一台像尺蠖一样向前移动、进入其他区域的活塞机器。虽然这些操作由玩家引起，但实际追查是谁建造或使用了 TNT 大炮要困难得多。即便如此，仍然需要防止有人用 TNT 大炮炸毁出生点。

    完全禁止 TNT 大炮或活塞并不是正确做法，因为它们应当在*某些*情况下获准使用。例如，区域内的 TNT 大炮或活塞应该能在*该区域内部*工作。

    首先记住，区域中能建造的**不是玩家这一类对象，而是成员**。看待活塞和 TNT 时也应如此。WorldGuard 如何判断活塞机器或 TNT 大炮是否属于区域成员？当然是看**它是否位于区域内部**！

    创建区域后，在设置任何旗标之前：

    - 成员可以建造

    - 非成员**不能**建造

    区域内的 TNT 大炮和活塞因为是“成员”而获准工作。假设玩家“Bobby”尚非成员，他就无法放置或破坏方块；把 Bobby 添加为区域成员后，他就可以建造。

    设置保护旗标会覆盖上述行为。如果将 `block-break` 设为 `deny`，就连成员也无法破坏方块：Bobby 不行，区域内的 TNT 大炮不行，区域内的活塞也不行。**于是活塞就无法正常工作了。**

    这会引出两个问题：

    - **如何禁止玩家放置或破坏方块？**什么也不用做，不要修改任何旗标！记住，默认只有成员能建造。

    - **如何让旗标只影响玩家？**你可能真正想问的是：如何只让旗标影响*非成员*？这很简单，使用[区域组](#region-groups)即可。

!!! tip "提示"

    注意：即使 `build` 设为 `allow` 或 `deny`，仍能被其他旗标（如 `block-break`、`interact` 等）覆盖。`build` 会根据成员关系隐式设置。

### 生物、火焰与爆炸 { #mobs-fire-and-explosions }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">旗标</th>
<th markdown="span">类型</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">creeper-explosion</td>
<td markdown="span">state</td>
<td markdown="span">苦力怕爆炸是否能造成伤害</td>
</tr>
<tr>
<td markdown="span">enderdragon-block-damage</td>
<td markdown="span">state</td>
<td markdown="span">末影龙是否能破坏方块</td>
</tr>
<tr>
<td markdown="span">ghast-fireball</td>
<td markdown="span">state</td>
<td markdown="span">恶魂火球和凋灵之首是否能造成伤害</td>
</tr>
<tr>
<td markdown="span">other-explosion</td>
<td markdown="span">state</td>
<td markdown="span">爆炸是否能造成伤害</td>
</tr>
<tr>
<td markdown="span">fire-spread</td>
<td markdown="span">state</td>
<td markdown="span">火焰是否能蔓延</td>
</tr>
<tr>
<td markdown="span">enderman-grief</td>
<td markdown="span">state</td>
<td markdown="span">末影人是否会破坏或放置方块</td>
</tr>
<tr>
<td markdown="span">snowman-trails</td>
<td markdown="span">state</td>
<td markdown="span">雪傀儡是否会在脚下生成雪</td>
</tr>
<tr>
<td markdown="span">ravager-grief</td>
<td markdown="span">state</td>
<td markdown="span">劫掠兽是否会破坏方块</td>
</tr>
<tr>
<td markdown="span">mob-damage</td>
<td markdown="span">state</td>
<td markdown="span">生物是否能伤害玩家</td>
</tr>
<tr>
<td markdown="span">mob-spawning</td>
<td markdown="span">state</td>
<td markdown="span">是否允许生物生成，包括通过命令、刷怪蛋等方式“手动”生成</td>
</tr>
<tr>
<td markdown="span">deny-spawn</td>
<td markdown="span">实体类型集合</td>
<td markdown="span">禁止生成的实体类型列表，包括通过命令、刷怪蛋等方式“手动”生成</td>
</tr>
<tr>
<td markdown="span">entity-painting-destroy</td>
<td markdown="span">state</td>
<td markdown="span">非玩家实体是否能破坏画</td>
</tr>
<tr>
<td markdown="span">entity-item-frame-destroy</td>
<td markdown="span">state</td>
<td markdown="span">非玩家实体是否能破坏物品展示框</td>
</tr>
<tr>
<td markdown="span">wither-damage</td>
<td markdown="span">state</td>
<td markdown="span">凋灵是否能造成伤害，指其自身的爆炸；凋灵之首投射物由前文的 ghast-fireball 处理</td>
</tr>
</tbody>
</table>

示例：禁止羊和牛在出生点生成

必须指定实体类型：

```text
/rg flag spawn deny-spawn cow,pig
```

### 自然事件 { #natural-events }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">旗标</th>
<th markdown="span">类型</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">lava-fire</td>
<td markdown="span">state</td>
<td markdown="span">岩浆是否能引发火灾</td>
</tr>
<tr>
<td markdown="span">lightning</td>
<td markdown="span">state</td>
<td markdown="span">闪电是否能劈落</td>
</tr>
<tr>
<td markdown="span">water-flow</td>
<td markdown="span">state</td>
<td markdown="span">水是否能流动</td>
</tr>
<tr>
<td markdown="span">lava-flow</td>
<td markdown="span">state</td>
<td markdown="span">岩浆是否能流动</td>
</tr>
<tr>
<td markdown="span">snow-fall</td>
<td markdown="span">state</td>
<td markdown="span">雪是否会在地面形成雪层</td>
</tr>
<tr>
<td markdown="span">snow-melt</td>
<td markdown="span">state</td>
<td markdown="span">雪是否会融化</td>
</tr>
<tr>
<td markdown="span">ice-form</td>
<td markdown="span">state</td>
<td markdown="span">冰是否会形成</td>
</tr>
<tr>
<td markdown="span">ice-melt</td>
<td markdown="span">state</td>
<td markdown="span">冰是否会融化</td>
</tr>
<tr>
<td markdown="span">frosted-ice-melt</td>
<td markdown="span">state</td>
<td markdown="span">霜冰是否会融化</td>
</tr>
<tr>
<td markdown="span">mushroom-growth</td>
<td markdown="span">state</td>
<td markdown="span">蘑菇是否会生长</td>
</tr>
<tr>
<td markdown="span">leaf-decay</td>
<td markdown="span">state</td>
<td markdown="span">树叶是否会腐烂</td>
</tr>
<tr>
<td markdown="span">grass-growth</td>
<td markdown="span">state</td>
<td markdown="span">草是否会生长</td>
</tr>
<tr>
<td markdown="span">mycelium-spread</td>
<td markdown="span">state</td>
<td markdown="span">菌丝体是否会扩散</td>
</tr>
<tr>
<td markdown="span">vine-growth</td>
<td markdown="span">state</td>
<td markdown="span">藤蔓和海带是否会生长</td>
</tr>
<tr>
<td markdown="span">rock-growth</td>
<td markdown="span">state</td>
<td markdown="span">滴水石等岩石是否会生长</td>
</tr>
<tr>
<td markdown="span">sculk-growth</td>
<td markdown="span">state</td>
<td markdown="span">幽匿及幽匿脉络是否会生长</td>
</tr>
<tr>
<td markdown="span">crop-growth</td>
<td markdown="span">state</td>
<td markdown="span">小麦、马铃薯、西瓜等作物是否会生长</td>
</tr>
<tr>
<td markdown="span">soil-dry</td>
<td markdown="span">state</td>
<td markdown="span">耕地是否会变干</td>
</tr>
<tr>
<td markdown="span">coral-fade</td>
<td markdown="span">state</td>
<td markdown="span">珊瑚离开水后是否会死亡</td>
</tr>
<tr>
<td markdown="span">copper-fade</td>
<td markdown="span">state</td>
<td markdown="span">铜是否会变色</td>
</tr>
</tbody>
</table>

!!! warning "警告"

    `fire-spread`、`water-flow`、`lava-flow` 和 `lava-fire` 需要在[配置](../config.md)中启用“高频旗标”选项。这些事件可能发生得非常频繁，需要更多区域查询，从而拖慢服务器，或至少让机房更热一些。

### 移动 { #movement }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">旗标</th>
<th markdown="span">类型</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">entry</td>
<td markdown="span">state</td>
<td markdown="span">玩家是否可以进入区域，默认针对非成员</td>
</tr>
<tr>
<td markdown="span">exit</td>
<td markdown="span">state</td>
<td markdown="span">玩家是否可以离开区域，默认针对非成员</td>
</tr>
<tr>
<td markdown="span">exit-via-teleport</td>
<td markdown="span">state</td>
<td markdown="block">

<p markdown="span">玩家是否可以通过传送离开区域。</p> <p markdown="span">只有玩家原本被禁止离开区域时，此项才会生效</p>

</td>
</tr>
<tr>
<td markdown="span">exit-override</td>
<td markdown="span">boolean</td>
<td markdown="span">是否始终允许玩家离开</td>
</tr>
<tr>
<td markdown="span">entry-deny-message</td>
<td markdown="span">string</td>
<td markdown="span">玩家被禁止进入时收到的消息</td>
</tr>
<tr>
<td markdown="span">exit-deny-message</td>
<td markdown="span">string</td>
<td markdown="span">玩家被禁止离开时收到的消息</td>
</tr>
<tr>
<td markdown="span">notify-enter</td>
<td markdown="span">boolean</td>
<td markdown="span">其他玩家进入区域时，是否通知拥有 `worldguard.notify` 权限的玩家</td>
</tr>
<tr>
<td markdown="span">notify-leave</td>
<td markdown="span">boolean</td>
<td markdown="span">其他玩家离开区域时，是否通知拥有 `worldguard.notify` 权限的玩家</td>
</tr>
<tr>
<td markdown="span">greeting</td>
<td markdown="span">string</td>
<td markdown="span">进入区域时在聊天中显示的消息</td>
</tr>
<tr>
<td markdown="span">greeting-title</td>
<td markdown="span">string</td>
<td markdown="span">进入区域时显示的标题。包含换行符（`\n`）时，会发送副标题。</td>
</tr>
<tr>
<td markdown="span">farewell</td>
<td markdown="span">string</td>
<td markdown="span">离开区域时在聊天中显示的消息</td>
</tr>
<tr>
<td markdown="span">farewell-title</td>
<td markdown="span">string</td>
<td markdown="span">离开区域时显示的标题。包含换行符（`\n`）时，会发送副标题。</td>
</tr>
<tr>
<td markdown="span">enderpearl</td>
<td markdown="span">state</td>
<td markdown="span">是否允许使用末影珍珠</td>
</tr>
<tr>
<td markdown="span">chorus-fruit-teleport</td>
<td markdown="span">state</td>
<td markdown="span">是否允许使用紫颂果传送</td>
</tr>
<tr>
<td markdown="span">teleport</td>
<td markdown="span">location</td>
<td markdown="span">使用 `/region teleport` 并指定该区域名称时的传送位置</td>
</tr>
<tr>
<td markdown="span">spawn</td>
<td markdown="span">location</td>
<td markdown="span">玩家在区域内死亡后的生成或传送位置，默认只针对成员</td>
</tr>
<tr>
<td markdown="span">teleport-message</td>
<td markdown="span">string</td>
<td markdown="span">通过 `/region teleport` 传送的玩家收到的消息</td>
</tr>
</tbody>
</table>

!!! tip "提示"

    如上文所述，位置旗标 `spawn` 默认针对“members”，即默认只有成员可以使用。可以修改该旗标的区域组来改变这一点。

!!! tip "提示"

    如果重叠区域设置了相同的 `greeting` 或 `farewell`，在这些区域间移动时不会发送消息，例如身处一个区域时又进入另一个区域。更一般地说，只要玩家移动*没有*导致起点和终点的旗标值改变，就不会发送消息。

!!! warning "警告"

    消息旗标 `greeting` 和 `farewell` 要求[配置](../config.md)中的“使用玩家移动事件”选项**保持启用**。

示例：禁止非成员进入“secret_club”区域

entry 默认针对“nonmembers”，因此无需在这里额外指定：

```text
/rg flag secret_club entry deny
```

### 地图制作 { #map-making }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">旗标</th>
<th markdown="span">类型</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">item-pickup</td>
<td markdown="span">state</td>
<td markdown="span">是否允许拾取物品</td>
</tr>
<tr>
<td markdown="span">item-drop</td>
<td markdown="span">state</td>
<td markdown="span">是否允许丢弃物品</td>
</tr>
<tr>
<td markdown="span">exp-drops</td>
<td markdown="span">state</td>
<td markdown="span">是否允许掉落经验</td>
</tr>
<tr>
<td markdown="span">deny-message</td>
<td markdown="span">string</td>
<td markdown="span">玩家的操作被拒绝时收到的消息</td>
</tr>
<tr>
<td markdown="span">invincible</td>
<td markdown="span">state</td>
<td markdown="span">玩家是否无敌</td>
</tr>
<tr>
<td markdown="span">fall-damage</td>
<td markdown="span">state</td>
<td markdown="span">实体是否受到摔落伤害</td>
</tr>
<tr>
<td markdown="span">game-mode</td>
<td markdown="span">gamemode</td>
<td markdown="span">玩家进入区域后应用的游戏模式，可为 survival、creative 或 adventure</td>
</tr>
<tr>
<td markdown="span">time-lock</td>
<td markdown="span">string</td>
<td markdown="span">玩家在区域内看到的日内时间，以 tick 为单位，范围为 0 到 24000。使用 + 或 - 可表示相对于世界时间的偏移。</td>
</tr>
<tr>
<td markdown="span">weather-lock</td>
<td markdown="span">weather</td>
<td markdown="span">玩家在区域内看到的天气，不影响世界机制。有效值为 `rain` 和 `clear`。</td>
</tr>
<tr>
<td markdown="span">natural-health-regen</td>
<td markdown="span">state</td>
<td markdown="span">玩家是否会因饱食或处于和平模式而自然恢复生命值。</td>
</tr>
<tr>
<td markdown="span">natural-hunger-drain</td>
<td markdown="span">state</td>
<td markdown="span">玩家是否会根据饱和度和消耗度自然消耗饥饿值。</td>
</tr>
<tr>
<td markdown="span">heal-delay</td>
<td markdown="span">integer</td>
<td markdown="span">每次治疗之间的秒数，仅在设置 `heal-amount` 时使用。设为 0 可禁用。</td>
</tr>
<tr>
<td markdown="span">heal-amount</td>
<td markdown="span">integer</td>
<td markdown="span">按 `heal-delay` 指定的频率治疗玩家的数量，以半颗心为单位；负值会造成伤害</td>
</tr>
<tr>
<td markdown="span">heal-min-health</td>
<td markdown="span">double</td>
<td markdown="span">通过 `heal-amount` 造成伤害时，生命值不会低于此下限，以半颗心为单位</td>
</tr>
<tr>
<td markdown="span">heal-max-health</td>
<td markdown="span">double</td>
<td markdown="span">通过 `heal-amount` 治疗时，生命值不会超过此上限，以半颗心为单位</td>
</tr>
<tr>
<td markdown="span">feed-delay</td>
<td markdown="span">integer</td>
<td markdown="span">参照对应的 heal 旗标，只不过此处针对食物</td>
</tr>
<tr>
<td markdown="span">feed-amount</td>
<td markdown="span">integer</td>
<td markdown="span">参照对应的 heal 旗标，只不过此处针对食物</td>
</tr>
<tr>
<td markdown="span">feed-min-hunger</td>
<td markdown="span">integer</td>
<td markdown="span">参照对应的 heal 旗标，只不过此处针对食物</td>
</tr>
<tr>
<td markdown="span">feed-max-hunger</td>
<td markdown="span">integer</td>
<td markdown="span">参照对应的 heal 旗标，只不过此处针对食物</td>
</tr>
<tr>
<td markdown="span">blocked-cmds</td>
<td markdown="span">字符串集合</td>
<td markdown="span">要禁止的命令列表</td>
</tr>
<tr>
<td markdown="span">allowed-cmds</td>
<td markdown="span">字符串集合</td>
<td markdown="span">命令白名单，所有未允许的命令都会被禁止</td>
</tr>
</tbody>
</table>

!!! warning "警告"

    治疗和饥饿值恢复旗标要求[配置](../config.md)中的“使用玩家移动事件”选项**保持启用**。

示例：修改玩家尝试执行的操作被阻止时收到的消息

设置 `deny-message` 旗标：

```text
/rg flag spawn deny-message Sorry! You are at spawn. If you want to find a place to call home, use the rail station to leave spawn.
```

示例：在出生点禁止“/tp”和“/teleport”命令

可用以下方式禁止相关命令：

```text
/rg flag spawn blocked-cmds /tp,/teleport
```

示例：在“hospital”区域中，每秒为玩家恢复一颗心，最多恢复到生命条的一半

没有增益效果时，玩家的最大生命值为 20，因此 10 就是一半：

```text
/rg flag hospital heal-delay 1
/rg flag hospital heal-amount 2
/rg flag hospital heal-max-health 10
```

### 其他 { #miscellaneous }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">旗标</th>
<th markdown="span">类型</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">pistons</td>
<td markdown="span">state</td>
<td markdown="span">是否允许使用活塞</td>
</tr>
<tr>
<td markdown="span">send-chat</td>
<td markdown="span">state</td>
<td markdown="span">玩家是否可以发送聊天消息</td>
</tr>
<tr>
<td markdown="span">receive-chat</td>
<td markdown="span">state</td>
<td markdown="span">玩家是否可以接收聊天消息</td>
</tr>
<tr>
<td markdown="span">potion-splash</td>
<td markdown="span">state</td>
<td markdown="span">药水是否可以产生喷溅效果</td>
</tr>
</tbody>
</table>

!!! note "注意"

    WorldGuard 只能限制其所在服务器上的聊天和命令。如果使用代理端处理聊天或命令，WorldGuard 无法影响代理端的处理。
