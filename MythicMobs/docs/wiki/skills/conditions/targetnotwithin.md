---
title: Targetnotwithin
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/targetnotwithin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Targetnotwithin {#targetnotwithin}

## 说明 {#description}

检查目标的 AI 攻击目标是否不在指定距离内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distance | d | 要检查的距离。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - targetnotwithin{d=10} true
```
