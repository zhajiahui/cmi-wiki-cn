---
title: Teleportto
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/teleportto
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Teleportto {#teleportto}

## 说明 {#description}

将目标实体传送到指定位置。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| location | coordinates, loc, l, c, t, target, to | 传送目的地的坐标或目标选择器 |  |
| world | w | 目的地所在的世界。提供 "location" 时，此参数为可选项 |  |
| yaw | y | 受影响实体要采用的 yaw | 0 |
| pitch | p | 受影响实体要采用的 pitch | 0 |
| relative | r | 位置是相对位置（relative）还是方向位置（directional） | false |
| targetasorigin | tao | 使用目标的位置作为原点，而不是施法者的位置 | false |

## 示例 {#examples}

将施法生物周围 50 方块半径内的所有玩家传送到指定位置：

```yaml
  Skills:
  - teleportto{location=190,64,200;world=world_nether} @PIR{r=50}
```

##  {#section}

将 50 格半径内的所有玩家传送到技能机制施法者上方 10 格的位置

```yaml
  Skills:
  - teleportto{location=@selflocation{y=10}} @PIR{r=50}
```

## 别名 {#aliases}

- teleportlocation
- tpt
- tpl
