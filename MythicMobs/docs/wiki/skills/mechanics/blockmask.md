---
title: Block Mask
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/BlockMask
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Block Mask {#block-mask}

## 说明 {#description}

在指定目标周围创建方块遮罩。在指定的持续时间到期后，由此效果创建或更改的块将消失或重置为之前的状态。通过使用 blockunmask-effect 可以在较早的时间点重置块（请参见下面的示例）。

请注意，方块遮罩效果永远不会真正改变世界上的任何方块，因此永远不会以任何方式破坏环境。此效果所做的更改纯粹是装饰性的，没有更改实际的块，并且一切都会返回到其原始状态。

材质属性接受与其相关的 [Bukkit name](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html) 作为有效值。

Bukkit 材料/方块名称可以在游戏中获取。只需将要用于该效果的块握在手中，然后使用命令“/itemdb”即可。此命令将输出 bukkit-material 信息以及一些其他信息，包括块的数据值。此命令应该适用于任何 bukkit/spigot 服务器。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | mat, m, block, b | 方块伪装使用的[方块类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)。 | GRAVEL |
| radius | r | 方块伪装效果的半径。 | 0 |
| radiusy | ry | 半径的 y 分量。 | `radius` |
| noise | n | 定义效果的随机程度。 | 0 |
| duration | d | 效果的持续时间，单位为刻。 | 0 |
| shape | s | 效果的形状，`Sphere`/`Cube`。 | SPHERE |
| noair | na | 仅伪装非空气方块。 | true |
| onlyair | oa | 仅伪装空气方块。 | false |
| audience |  | 效果的[可见对象](../audience.md)。 | nearby |
| occ | o, oc | 使用 onlyair 时，也以透明方块为目标。 | true |

### Duration 属性 {#duration-attribute}

1 秒为 20 游戏刻。持续时间设为 0 时，效果无限持续。

### Shape 属性 {#shape-attribute}

`Sphere` 和 `Cube` 是唯一可用的形状。

## 示例 {#examples}

在施法生物周围创建一个下界岩环境。将持续时间保留在0游戏刻上将导致块保持新的假形式，直到提供手动块更新或玩家重新登录游戏。

```yaml
- effect:blockmask{m=netherrack;r=5} @self ~onTimer:1200
```

##  {#section}

在 50 方块半径内的所有玩家脚下形成一层冰，导致他们行走时不断打滑。

```yaml
- effect:blockmask{m=ice;r=2;d=20} @PIR{r=50} ~onTimer:5
```

##  {#section-2}

```yaml
- effect:blockmask{m=ice;r=2;d=20;onlyair=true} @origin ~onTimer:5 # this will replace air and transparent blocks (i.e. stairs, slabs and glass) with ice
- effect:blockmask{m=ice;r=2;d=20;onlyair=true;occ=false} @origin ~onTimer:5 # this will replace only air with ice
```

##  {#section-3}

将强制反转指定半径内由块遮罩效果创建的所有效果。 blockunmask 效果除了“radius”之外没有任何语法选项。

```yaml
- effect:blockunmask{r=30}
```

## 别名 {#aliases}

- effect:blockMask
- e:blockMask
