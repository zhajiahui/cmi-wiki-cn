---
title: Thunder Level
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ThunderLevel
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Thunder Level {#thunder-level}

## 说明 {#description}

对每个玩家造成风暴效果（不下雨）

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| level | lvl, l, type, t, environment, env, e | 效果类型，为 0 或 1 | 0 |

## 示例 {#example}

```yaml
Skills:
  - thunderlevel{l=1} @PIR{r=20} ~onSpawn
```

## 别名 {#aliases}

- effect:thunderlevel
- e:thunderlevel
