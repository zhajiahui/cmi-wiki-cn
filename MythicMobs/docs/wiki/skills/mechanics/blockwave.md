---
title: Block Wave
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/BlockWave
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Block Wave {#block-wave}

## 说明 {#description}

创建具有不同形状、速度和块的指定块的波浪。

请注意，方块波效应实际上永远不会改变世界上的任何方块，因此永远不会以任何方式破坏环境。此效果所做的更改纯粹是装饰性的，没有更改实际的块，并且一切都会返回到其原始状态。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m | 方块波浪使用的[材质](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)。 |  |
| radius | r | 方块波浪效果的半径。 | 2 |
| radiusy | ry | 方块波浪效果的 y 轴半径。 | `radius` |
| duration | d | 效果的持续时间，单位为刻。 | 15 |
| shape | s | 效果的形状（Sphere/Cube）。 | sphere |
| velocity | v | 效果的速度。 | 0.2 |
| horizontalvelocity | velocityh, vh | 效果在水平方向上的速度。 | 0 |
| specificvelocities | sv | 是否使用 `vx`、`vy` 和 `vz` 属性。 | false |
| velocityx | vx | 效果在 x 轴方向上的速度。 | 0 |
| velocityy | vy | 效果在 y 轴方向上的速度。 | 0 |
| velocityz | vz | 效果在 z 轴方向上的速度。 | 0 |
| noise | n | 效果的噪声。 | 0 |
| hidesourceblock | hidesource, hsb, hs | 是否隐藏源方块。 | true |
| ignoreair | ia | 是否忽略空气方块。 | true |

### Material 属性 {#material-attribute}

如果材质留空，它将使用它所使用的任何材质类型。示例：如果你将其留空并在村民建筑物上使用它，你将看到方块波中使用的建筑物的方块。

## 示例 {#examples}

```yaml
  Skills:
  - blockwave{duration=100;material=stone;radius=5;radiusY=5;velocity=10;shape=sphere} @selflocation
```

> 从你自己的位置开始创建球形的石块波

## 别名 {#aliases}

- effect:blockWave
- e:blockWave
