---
title: Meleeattack
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/meleeattack
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Meleeattack {#meleeattack}

## 说明 {#description}

让生物接近目标并进行近战攻击。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speedmodifier | speed, s | 执行此动作期间生物的速度修饰值。 | 1 |
| followUnseen | fu | 即使目标不在视野中，是否仍然跟随。 | false |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - meleeattack{s=1;fu=false}
```
