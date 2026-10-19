---
title: Worldtime
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/worldtime
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Worldtime {#worldtime}

## 说明 {#description}

将范围与目标位置的世界时间进行匹配。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| time | t | 要检查的时间范围。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - worldtime{t=0to6000} true
```
