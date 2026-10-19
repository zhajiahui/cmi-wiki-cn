---
title: Items Near Origin
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ItemsNearOrigin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Items Near Origin {#items-near-origin}

## 说明 {#description}

选中元技能原点周围指定半径内的所有物品

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |

## 示例 {#examples}

在此示例中，玩家发射的弹射物每次执行 onTick 元技能时，都会让施法者拾取弹射物周围半径 5 格内的所有物品

```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onTick=[
      - pickupitem @ItemsNearOrigin{r=5}
    ]}
```

## 别名 {#aliases}

- INO
