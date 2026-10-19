---
title: Fill Chest
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/fillChest
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Fill Chest {#fill-chest}

## 说明 {#description}

用一系列物品或 [droptable](../../drops/droptables.md) 填充箱子

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| items | item, i | 用于填充箱子的物品，可以是逗号分隔的物品列表或 DropTable。 | NONE |
| shouldStack | stack | 是否在可能的情况下堆叠给定物品。true/false。 |  |
| shouldempty | empty | 添加物品前是否清空容器。true/false。 |  |

## 示例 {#examples}

用特定物品填充箱子的示例。

```yaml
  Skills:
  - fillchest{i=diamond_sword,diamond} @Location{x=#;y=#;z=#} ~onDeath
```

##  {#section}

用掉落物填充箱子的示例。

```yaml
  Skills:
  - fillchest{i=SkeletonKingDrops} @Location{x=#;y=#;z=#} ~onSpawn
```

## 别名 {#aliases}

- populateChest
- fillContainer
- populateContainer
