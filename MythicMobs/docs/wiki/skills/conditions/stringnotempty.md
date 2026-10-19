---
title: String Not Empty
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/StringNotEmpty
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# String Not Empty {#string-not-empty}

## 说明 {#description}

检查提供的字符串是否不为空

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| value | val, v, string, s | 要检查的字符串。 |  |

## 示例 {#example}

```yaml
  Conditions:
  - stringNotEmpty{value=<caster.var.examplevariable>}
```

> 检查 <caster.var.examplevariable> 占位符的值是否*不是*空字符串

## 别名 {#aliases}

- notEmpty
