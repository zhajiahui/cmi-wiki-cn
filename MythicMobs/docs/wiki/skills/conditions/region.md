---
title: Region
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/region
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Region {#region}

## 说明 {#description}

检查目标是否在给定的 WorldGuard 区域内。

> 通过 `/rg create` 命令创建区域时，无论你在命令中编写什么，名称将*始终*为小写。因此，当你需要通过此条件检查此类区域时，请记住也将其名称写为小写

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| region | r, name, n | 要检查的区域。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - region{r=someregion} true
```

## 别名 {#aliases}

- inregion
