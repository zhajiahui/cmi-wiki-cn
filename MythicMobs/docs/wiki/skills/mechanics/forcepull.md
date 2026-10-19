---
title: Forcepull
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/forcepull
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Forcepull {#forcepull}

## 说明 {#description}

将所有目标实体传送到施法生物周围 <spread> 格内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| spread | s | 玩家相对于施法生物的散布程度。 | 0 |
| vspread | spreadv, vs | 用于覆盖竖直散布值。 | spread |

## 示例 {#examples}

此示例会将 30 块内的所有实体传送到 Boss 的 5 块内的随机位置。

```yaml
ForceGrip:
  Skills:
  - forcepull{spread=5} @EntitiesInRadius{r=30}
```
