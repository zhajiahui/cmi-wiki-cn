---
title: On Block Place
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/OnBlockPlace
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Block Place {#on-block-place}

## 说明 {#description}

将光环组件应用于目标，当目标放置方块时会触发技能

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onPlaceSkill | onplace, op | 目标放置方块时执行的技能。 |  |
| cancelEvent | cancel, cE | 是否取消触发光环的事件。 | false |

## 示例 {#examples}

Simple:

为自身施加 onBlockPlace 光环，每次放置方块时，将周围地形变成金块（点石成金）。这里使用 2 个元技能，让 @BlocksInRadius 以放置位置 @targetlocation 为中心；若不使用 2 个元技能，@BlocksInRadius 会以放置方块的玩家为中心。

```yaml
ApplyAura:
  Skills:
  - aura{d=300;i=1;components=[
    - onBlockPlace{op=MidasTouch1;auraname=Golden} @self
    ]} @self
MidasTouch1:
  Skills:
  - skill{s=MidasTouch2} @targetlocation
MidasTouch2:
  Skills:
  - setblock{m=GOLD_BLOCK} @BlocksInRadius{r=5;ry=1}
```

##  {#section}

Intermediate:

为自身施加 onBlockPlace 光环。放置方块时，将非贵重矿石的方块变成玻璃，实现类似透视的效果。这里仍使用 2 个元技能，但并非以放置位置为中心，而是通过第二个元技能避免将贵重矿石改成玻璃。若要同时以放置位置为中心，可结合上面的示例，使用 3 个元技能。

如果你不希望此 X 射线永久存在，你可以尝试使用材质设置为玻璃的块遮罩，而不是使用设置块机制。 Blockmask 使用数据包，因此可能会导致客户端延迟。玩玩它！这是最好的学习方式。

```yaml
ApplyAura:
  Skills:
  - aura{d=200;i=1;components=[
    - onBlockPlace{op=XRay;auraname=Cheater} @self
    ]} @self
XRay:
  Skills:
  - skill{s=XRay2} @BlocksInRadius{r=20;ry=20}
XRay2:
  TargetConditions:
  - blocktype{type=BEDROCK,END_PORTAL,END_PORTAL_FRAME,NETHER_PORTAL,CRAFTING_TABLE,SMITHING_TABLE,ENCHANTING_TABLE,COAL_ORE,DEEPSLATE_COAL_ORE,DIAMOND_ORE,DEEPSLATE_DIAMOND_ORE,EMERALD_ORE,DEEPSLATE_EMERALD_ORE,GOLD_ORE,NETHER_GOLD_ORE,DEEPSLATE_GOLD_ORE,NETHER_QUARTZ_ORE,IRON_ORE,DEEPSLATE_IRON_ORE,COPPER_ORE,DEEPSLATE_COPPER_ORE,LAPIS_ORE,DEEPSLATE_LAPIS_ORE,REDSTONE_ORE,DEEPSLATE_REDSTONE_ORE,ANCIENT_DEBRIS} false
  Skills:
  - setblock{m=GLASS}
```

## 别名 {#aliases}

- onplaceblock
