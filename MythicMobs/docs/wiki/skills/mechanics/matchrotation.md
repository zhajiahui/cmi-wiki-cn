---
title: Match Rotation
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/MatchRotation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Match Rotation {#match-rotation}

## 说明 {#description}

将目标的偏航和俯仰设置为与指定目标属性相同的值

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| target | to, t, location, loc, l, of | [目标选择器](../targeters.md) |  |

## 示例 {#examples}

```yaml
  Skills:
  - matchrotation{target=@Parent} @self
```

## 别名 {#aliases}

- matchrot
