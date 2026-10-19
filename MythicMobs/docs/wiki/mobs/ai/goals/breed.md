---
title: Breed
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/breed
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Breed {#breed}

## 说明 {#description}

让生物可以与其他生物繁殖。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speedmodifier | speed,s | 向配偶移动的速度。 | 1 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: COW
  AIGoalSelectors:
    - clear
    - breed{s=2}
```
