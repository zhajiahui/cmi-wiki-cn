---
title: Lightlevel
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lightlevel
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Lightlevel {#lightlevel}

## 说明 {#description}

测试目标位置的光照水平

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| level | l | 要匹配的等级范围。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - lightlevel{l=10} true
```

```yaml
  Conditions:
  - lightlevel{l=>10} true
```

```yaml
  Conditions:
  - lightlevel{l=1to10} true
```
