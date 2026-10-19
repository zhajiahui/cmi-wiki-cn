---
title: Globalscore
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/globalscore
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Globalscore {#globalscore}

## 说明 {#description}

检查全局记分板值（与假玩家相关的值 **GLOBAL**）

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| objective | obj, o | 记分项。 |  |
| value | val, v | 要匹配的数值。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - globalscore{o=KillCount;value=5} true
```

## 别名 {#aliases}

- scoreglobal
