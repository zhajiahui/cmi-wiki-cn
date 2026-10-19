---
title: Block Vein
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/BlockVein
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Block Vein {#block-vein}

## 说明 {#description}

从技能原点开始，选中所有相连且符合指定方块类型的方块

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| blocktypes | blocktype, bt, t, material, materials, mat, m, blocks, block, b | 要加入矿脉的方块，可以是列表。在类型前加 `*` 表示指定的是[方块标签](https://minecraft.wiki/w/Tag#Block_tags_2)，而不是方块类型，例如 `blocktype=*sculk_replaceable`。 | STONE |
| limit | max, l, m | 加入矿脉的方块数量上限。 | 10 |
| originMustMatch | match | 目标方块是否必须与元技能原点处的方块匹配。 | true |

## 示例 {#examples}

```yaml
# Vein mine whatever you mine (Crucible)
VeinMinerPickaxe:
  Id: NETHERITE_PICKAXE
  Skills:
  - breakblock{origin=@TargetBlock} @Vein{bt=<caster.raycast>} ~onBlockBreak

# Vein mine only certain ores (Crucible)
VeinMinerPickaxeOres:
  Id: DIAMOND_PICKAXE
  Skills:
  - breakblock{origin=@TargetBlock} @Vein{bt=REDSTONE_ORE, DEEPSLATE_REDSTONE_ORE} ~onBlockBreak

# Vein mine all ores (Crucible)
VeinMinerPickaxeOres_V2:
  Id: DIAMOND_PICKAXE
  Skills:
  - breakblock{origin=@TargetBlock} @Vein{bt=#_ORE} ~onBlockBreak
```

## 别名 {#aliases}

- vein
- bv
