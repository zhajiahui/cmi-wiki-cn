---
title: Lookatplayers
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/lookatplayers
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Lookatplayers {#lookatplayers}

## 说明 {#description}

让生物看向附近的玩家。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| range | radius,r | 寻找玩家的范围。 | 5 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - lookatplayers{r=12}
```

## 别名 {#aliases}

- lookatplayer
