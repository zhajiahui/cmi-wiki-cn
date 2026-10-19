---
title: Hascurrency
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hascurrency
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Hascurrency {#hascurrency}

## 说明 {#description}

检查目标是否拥有指定数量的 Vault 货币。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 货币数量。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - hascurrency{a=1000} true
```

## 别名 {#aliases}

- hasmoney
