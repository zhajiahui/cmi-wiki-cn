---
title: World Edit Replace
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/WorldEditReplace
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# World Edit Replace {#world-edit-replace}

## 说明 {#description}

使用WorldEdit替换区域中的块。需要 [@region](../targeters/region.md) 或类似的目标选择器

> **这是[仅限高级版](../../premium-features.md) 机制！**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| from | f | 要替换的材质 | AIR |
| to | t | 用于替换原材质的新材质 | AIR |

## 示例 {#examples}

```yaml
  Skills:
  - worldEditReplace{from=STONE;to=AIR} @Region{min=0,0,0;max=100,100,100;world=resources}
```

## 别名 {#aliases}

- weReplace
