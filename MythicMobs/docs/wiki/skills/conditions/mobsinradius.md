---
title: Mobsinradius
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mobsinradius
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mobsinradius {#mobsinradius}

## 说明 {#description}

检查给定半径内有多少生物

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| types | type, t | 要检查的生物类型。 |  |
| amount | a | 要检查的生物数量范围，不计入施法者。 | 1 |
| radius | r | 要检查的半径。 | 5 |

## 示例 {#examples}

### 单个类型 {#single-type}

```yaml
  Conditions:
  - mobsInRadius{types=NewZombie;amount=5to10;radius=15}
```

### 多个类型 {#multiple-types}

```yaml
  Conditions:
  - mobsInRadius{types=NewZombie,NewSkeleton,NewSpider;amount=5to10;radius=15}
```
