---
title: Target Predicted Location
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetPredictedLocation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Target Predicted Location {#target-predicted-location}

## 说明 {#description}

根据施法者首要[目标](target.md)当前的移动速度，预测该目标经过指定数量的游戏刻后所在的位置，并选中该位置。

代码通过从目标位置发出射线来实现预测，因此如果途中遇到方块，射线会提前停止，无法到达原本预计的终点

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| maxdistance | max, distance, d | 预测位置与目标当前位置之间的最大距离。如果预测位置本应更远，此目标选择器会改为选择较近的位置：从目标原位置沿其移动向量前进 `maxdistance` 格的位置。 | 64 |
| ticksPredicted | ticks, t | 此目标选择器向未来预测多远。 | 20 |
| ignoreTransparent | it | 用于预测的射线检测是否忽略透明方块。 | true |

## 示例 {#examples}

```yaml
  Skills:
  - skill{s=TheFloorIsLava} @targetPredictedLoc{ticks=15}
```

## 别名 {#aliases}

- targetPredictedLoc
- TPL
- PredictedTargetLocation
