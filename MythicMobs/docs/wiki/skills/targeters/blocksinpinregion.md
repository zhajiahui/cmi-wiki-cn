---
title: Blocks In Pin Region
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/BlocksInPinRegion
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Blocks In Pin Region {#blocks-in-pin-region}

## 说明 {#description}

选中由两个 Pin 界定的区域中的方块

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| pin1 | p1 | 第一个[定位点](../../pins.md)。 |  |
| pin2 | p2 | 第二个[定位点](../../pins.md)。 |  |

## 示例 {#examples}

```yaml
  - particle @BlocksInPinRegion{p1=mypin;p2=anotherpin}
```
