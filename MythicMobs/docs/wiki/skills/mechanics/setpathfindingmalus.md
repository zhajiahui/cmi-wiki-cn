---
title: Set Pathfinding Malus
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SetPathfindingMalus
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Set Pathfinding Malus {#set-pathfinding-malus}

## 说明 {#description}

设置生物的寻路代价，影响实体计算路径时对不同方块类型的评估。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| malus | type, malustype | 实体可能遇到的方块或地形类型 | OPEN |
| value | amount | 表示寻路对相应方块或地形的排斥程度的权重，可以为负数 | 0.0 |

### Malus 属性 {#malus-attribute}

有效的寻路代价类型：

|  |  |  |  |
| --- | --- | --- | --- |
| `BLOCKED` | `OPEN` | `WALKABLE` | `WALKABLE_DOOR` |
| `TRAPDOOR` | `POWDER_SNOW` | `DANGER_POWDER_SNOW` | `FENCE` |
| `LAVA` | `WATER` | `WATER_BORDER` | `RAIL` |
| `UNPASSABLE_RAIL` | `DANGER_FIRE` | `DAMAGE_FIRE` | `DANGER_OTHER` |
| `DAMAGE_OTHER` | `DOOR_OPEN` | `DOOR_WOOD_CLOSED` | `DOOR_IRON_CLOSED` |
| `BREACH` | `LEAVES` | `STICKY_HONEY` | `COCOA` |
| `DAMAGE_CAUTIOUS` |  |  |  |

### Value 属性 {#value-attribute}

实体 AI 计算路径时，会检查候选路径上的方块类型。修改寻路代价可以让实体更倾向于经过、绕行或避开某类方块。例如：

- 正值（例如，1.0）意味着实体将认为该块类型更难走过或不太有利，从而导致实体尝试避开它。
- 负值或零值（例如，-1.0或0.0）意味着该实体将认为该块类型是中性的或更容易走过，从而更有可能选择带有这些块的路径

## 示例 {#examples}

```yaml
  Skills:
  - setpathfindingmalus{malus=BLOCKED;value=2} @self
```

## 别名 {#aliases}

- setmalus
- malus
