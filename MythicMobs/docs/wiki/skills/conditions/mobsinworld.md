---
title: Mobsinworld
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mobsinworld
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mobsinworld {#mobsinworld}

## 说明 {#description}

将范围与目标世界中的生物数量相匹配

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要匹配的数值范围。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - mobsinworld{a=20to50} true
```

```yaml
  Conditions:
  - mobsinworld{a=<50} true
```
