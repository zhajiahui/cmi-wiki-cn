---
title: Moisturelevel
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/moisturelevel
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Moisturelevel {#moisturelevel}

## 说明 {#description}

检查目标耕地方块的湿润程度是否为指定值。

- `0` 表示干燥耕地。
- `1-6` 表示原本湿润的耕地在失去水源后逐渐变干。
- `7` 表示完全湿润的耕地。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| l | moistness, m | 要检查的湿润程度。 |  |

## 示例 {#examples}

```yml
  TargetConditions:
  - moisturelevel{l=3} true
```

```yml
  TargetConditions:
  - moistureness{l=1to6} true
```

## 别名 {#aliases}

- moistureness
- moistness
