---
title: Bossborder
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/bossborder
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Bossborder {#bossborder}

## 说明 {#description}

将目标玩家困在施法者周围的原版世界边界内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 边界半径。 | 32 |

## 示例 {#examples}

```yml
  Skills:
  - bossBorder{r=40} @NearestPlayer{r=30}
```

## 别名 {#aliases}

- effect:bossBorder
- e:bossBorder
