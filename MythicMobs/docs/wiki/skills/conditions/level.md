---
title: Level
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/level
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Level {#level}

## 说明 {#description}

检查目标MythicMob的等级

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| level | l | 要匹配的等级范围。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - level{l=10} true
```

```yaml
  Conditions:
  - level{l=>10} true
```

```yaml
  Conditions:
  - level{l=1to10} true
```

```yaml
  Conditions:
  - level{l=<10} true
```
