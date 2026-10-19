---
title: Region
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Region
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Region {#region}

## 说明 {#description}

用于选中区域的特殊目标选择器，仅支持特定技能机制

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| min |  | 第一个点的位置。 | 0,0,0 |
| max |  | 第二个点的位置。 | 0,0,0 |
| world |  | 区域所在的世界。 | `<caster.l.w>` |

### Min 和 Max 属性 {#min-and-max-attributes}

返回的区域将是这两点之间包含的区域

## 示例 {#examples}

```yaml
  Skills:
  - worldEditReplace{from=STONE;to=AIR} @Region{min=0,0,0;max=100,100,100;world=resources}
```
