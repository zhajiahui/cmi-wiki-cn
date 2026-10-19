---
title: Gotospawn
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/gotospawn
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Gotospawn {#gotospawn}

## 说明 {#description}

让生物返回最初的生成位置。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 移动速度修饰值。 | 1 |
| minRange | min, mr | 生物距出生位置多近时，视为已到达该位置。生物会向出生位置移动，直到距离缩短到此值。 | 2 |
| maxRange | max, r | 生物与出生位置之间允许的最大距离。超出此距离时，会激活该 AI 行为，向出生位置移动，直到进入最小距离范围。 | 16 |
| dropTarget | dt | 此 AI 行为激活时，生物是否放弃当前目标。 | true |

## 示例 {#examples}

这个僵尸会尝试近战攻击目标，直到它距离生成位置超过 20 格，然后转身走回生成处。

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - goToSpawn{speed=1;max=20;min=4}
    - meleeattack
```

## 别名 {#aliases}

- gotospawnlocation
