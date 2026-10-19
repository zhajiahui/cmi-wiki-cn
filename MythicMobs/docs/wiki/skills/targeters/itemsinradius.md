---
title: Items In Radius
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ItemsInRadius
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Items In Radius {#items-in-radius}

## 说明 {#description}

瞄准施法者周围半径内的所有物品

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - pickupitem @ItemsInRadius{r=10}
```

## 别名 {#aliases}

- IIR
