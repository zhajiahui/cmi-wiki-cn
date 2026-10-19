---
title: Crossbowattack
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/crossbowattack
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Crossbowattack {#crossbowattack}

## 说明 {#description}

使用弩攻击。只有猪灵和掠夺者可以使用 crossbowAttack 行为目标，而且必须手持弩。

### 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 移动速度修饰值。 | 1 |
| attackradius | radius, r | 生物开始射击的距离。 | 8 |

### 示例 {#examples}

```yaml
ExampleMob:
  Type: Piglins
  Equipment:
    - crossbow HAND
  AIGoalSelectors:
    - clear
    - crossbowAttack
```
