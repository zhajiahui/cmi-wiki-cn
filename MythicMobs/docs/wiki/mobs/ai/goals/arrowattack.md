---
title: Arrowattack
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/arrowattack
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Arrowattack {#arrowattack}

## 说明 {#description}

远程实体可使用的基本远程攻击。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 移动速度修饰值。 | 1 |
| attackspeedmax | smax | 每次射击的最大间隔（单位为刻）。 | 60 |
| attackspeedmin | amin | 每次射击的最小间隔（单位为刻）。 | 20 |
| attackradius | radius, r | 此 AI 行为的攻击半径。 | 15 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: Skeleton
  AIGoalSelectors:
  - clear
  - rangedAttack{speed=1;smax=60;amin=20;radius=15}
```

## 别名 {#aliases}

- rangedAttack
