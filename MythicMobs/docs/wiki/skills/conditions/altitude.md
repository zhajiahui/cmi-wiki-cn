---
title: Altitude
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/altitude
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Altitude {#altitude}

## 说明 {#description}

此条件测试目标实体距地面有多远。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| height | altitude, a, h | 要检查的高度范围。 |  |
| maxHeight | mH | 限制此条件可检查的最大高度。 | 30 |

## 示例 {#examples}

```yaml
Conditions:
- altitude{h=3-5} true
```

## 别名 {#aliases}

- heightfromsurface
