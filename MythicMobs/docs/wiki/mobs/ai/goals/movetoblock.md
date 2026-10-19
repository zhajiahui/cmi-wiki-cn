---
title: Movetoblock
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/movetoblock
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Movetoblock {#movetoblock}

## 说明 {#description}

让生物向指定类型的方块移动。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m, mat | 要作为目标的方块类型。 | IRON_ORE |
| radius | r, search, searchrange | 搜索方块的半径。 | 8 |
| radiusy | ry, verticalsearchrange, vsearch, yr, yradius | 搜索方块的 Y 轴半径。 | 2 |
| speed | s | 移动速度。 | 0.9 |

### 示例 {#examples}

```yaml
ExampleMob:
  Type: Pig
  AIGoalSelectors:
    - clear
    - moveToBlock{material=STONE;radius=8;radiusY=2;speed=0.9}
```

## 别名 {#aliases}

- gotoblock
