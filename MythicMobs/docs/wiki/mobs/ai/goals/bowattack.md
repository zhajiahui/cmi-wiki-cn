---
title: Bowattack
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/bowattack
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Bowattack {#bowattack}

## 说明 {#description}

一种高级远程攻击，经常会让射手向后或顺时针侧移。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 移动速度修饰值。 | 1 |
| attackradius | radius,r | 攻击半径。 | 15 |
| attackspeedmax | smax | 最大攻击速度。 | 20 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: Skeleton
  AIGoalSelectors:
    - clear
    - bowattack{speed=1;radius=15}
```

## 别名 {#aliases}

- skeletonbowattack
- bowshoot
- bowmaster
