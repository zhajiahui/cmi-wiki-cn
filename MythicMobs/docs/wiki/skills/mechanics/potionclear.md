---
title: Potionclear
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/potionclear
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Potionclear {#potionclear}

## 说明 {#description}

清除目标实体的全部药水效果

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| types | type, t | 要清除的药水效果类型或类型列表。未提供类型时，会清除所有效果。 |  |

## 示例 {#examples}

```yaml
  Skills:
  - potionclear{type=FIRE_RESISTANCE} @target
  - potionclear{type=FIRE_RESISTANCE,SPEED} @self
  - potionclear @self
```

## 别名 {#aliases}

- clearpotion
- clearpotions
