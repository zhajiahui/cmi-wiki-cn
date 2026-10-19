---
title: Pin
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Pin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Pin {#pin}

## 说明 {#description}

选中 [Pin](../../pins.md) 的位置。如果是通过 Pin Wand 制作的 Multi-Pin，则会选中其关联的所有位置。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| name | n, pin, p, key, k | 要选择为目标的[定位点](../../pins.md)名称。 |  |
| random | r | 指定定位点为多点定位标记时，是否仅随机选择一个位置。 | false |

## 示例 {#examples}

```yaml
  Skills:
  - teleport @Pin{p=mypin}
```
