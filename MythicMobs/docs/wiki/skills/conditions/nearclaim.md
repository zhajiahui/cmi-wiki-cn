---
title: Nearclaim
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/nearclaim
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Nearclaim {#nearclaim}

## 说明 {#description}

检查目标位置是否靠近任意受支持领地插件的领地。

支持的插件：

- GriefPrevention
- Lands
- CrashClaim

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 要检查的给定范围。 | 16 |

## 示例 {#example}

```yaml
  Conditions:
  - nearclaim{r=20} false
```

## 别名 {#aliases}

- nearClaims
