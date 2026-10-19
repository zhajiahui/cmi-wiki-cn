---
title: Dropitem
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/dropitem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Dropitem {#dropitem}

## 说明 {#description}

掉落一组物品或可选的 [DropTable](../../drops/droptables.md)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| items | item, i | 要掉落的物品，可以是逗号分隔的物品列表或 DropTable。可在物品名称后添加一个空格和数字来指定数量。 | NONE |
| naturally | natural, n | 物品是否自然掉落。 | true |
| onDropSkill | onDrop, then | 物品掉落时执行的[元技能](../metaskills.md)，会继承掉落物实体作为目标。 |  |
| dynamic | fd | 强制每次都将掉落物按动态物品解析。 | false |

## 示例 {#examples}

掉落指定物品的示例。

```yaml
  Skills:
  - dropitem{i=diamond_sword,diamond} @self ~onDeath
  - ...
```

以下示例将掉落钻石剑和5钻石

```yaml
  Skills:
  - dropitem{i=diamond_sword,diamond 5} @self ~onDeath
  - ...
```

##  {#section}

从 DropTable 掉落物品的示例。

```yaml
  Skills:
  - dropitem{i=SkeletonKingDrops} @self ~onSpawn
  - ...
```

## 别名 {#aliases}

- drop
- dropitems
- itemdrop
