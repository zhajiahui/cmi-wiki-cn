---
title: Fleesun
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleesun
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Fleesun {#fleesun}

## 说明 {#description}

让生物避开阳光，躲入阴影处。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 向阴影处移动的速度。 | 1 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleesun{s=2}
```
