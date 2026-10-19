---
title: In Pin Region
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/InPinRegion
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# In Pin Region {#in-pin-region}

## 说明 {#description}

检查目标位置是否位于由两个 [pin](../../pins.md) 界定的区域内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| pin1 | p1 | 第一个[定位点](../../pins.md)。 |  |
| pin2 | p2 | 第二个[定位点](../../pins.md)。 |  |

## 示例 {#examples}

```yaml
  TargetConditions:
  - inpinregion{p1=mypin;p2=anotherpin}
```
