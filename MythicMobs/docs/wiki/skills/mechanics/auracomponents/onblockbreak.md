---
title: On Block Break
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/OnBlockBreak
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Block Break {#on-block-break}

## 说明 {#description}

将光环组件应用于目标，当目标打破方块时触发技能

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onBreakSkill | onBreak, oB | 目标破坏方块时执行的技能。 |  |
| cancelEvent | cancel, cE | 是否取消触发光环的事件。 | false |
| dropitem | drop, allowDrop | 破坏后是否掉落物品。 | true |
| blocktypes | bt, t, material, materials, m, blocks, block, b | 哪些方块会触发此光环。可在类型前添加 `*`，表示指定的是[方块标签](https://minecraft.wiki/w/Tag#Block_tags_2)而非方块类型，例如 `blocktype=*sculk_replaceable`。 |  |

## 示例 {#examples}

Simple:

对自己施加onBlockBreak光环，使粒子发生在破碎方块的位置

```yaml
ApplyAura:
  Skills:
  - aura{d=300;i=1;components=[
    - onBlockBreak{oB=FlameParticlesAtBlock;cE=false;auraname=Fire}
    ]} @self
FlameParticlesAtBlock:
  Skills:
  - particles{particle=flame;a=2;hs=0.25;vs=0.25;y=0.5;s=0.1125} @targetlocation
```

##  {#section}

```yaml
  Skills:
  - aura{d=99999;i=1;components=[
    - onBlockBreak{bt=#TORCH,#LIGHT;oB=[ addVar{var=caster.lightsBroken;a=1} ]}
    ]} @self
```

##  {#section-2}

进阶：（请先阅读说明，否则可能导致服务器崩溃或卡顿！）

为自身施加 onBlockBreak 光环。破坏方块时，会以该方块的 targetlocation 为中心，挖掘 5x5 区域（从中心方块向各方向延伸 3 格）。这里**必须**设置冷却，否则 breakblock 会无限重复触发 onblockbreak。冷却至少为 0.1 秒（2 游戏刻）。

这里需要 2 个元技能，让 blockinradius 以被破坏的方块为中心。若不用 2 个元技能，blocksInRadius 就会选择破坏方块的玩家周围，而非被破坏方块的位置。

```yaml
ApplyAura:
  Skills:
  - aura{d=300;i=1;components=[
    - onBlockBreak{oB=AreaMining1;cE=false;auraname=TotalDestruction;auraname=Fire}
    ]} @self
AreaMining1:
  Cooldown: 0.1
  Skills:
  - skill{s=AreaMining2} @targetLocation
AreaMining2:
  Skills:
  - breakblock{doDrops=true;doEffect=true;useTool=false;forcesync=true} @BlocksInRadius{r=3;ry=3}
```

## 别名 {#aliases}

- onbreakblock
