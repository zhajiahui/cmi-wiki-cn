---
title: Shootfireball
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shootfireball
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Shootfireball {#shootfireball}

## 说明 {#description}

从生物中向目标实体或位置发射火球。

> 注意！
> 这个火球的大版本可以破坏方块。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| yield | strength, y, s | 火球爆炸的威力 | 1 |
| velocity | v | 火球的速度 | 1 |
| fireTicks | ft | 火球留下的火焰持续时间，以刻为单位 | 0 |
| incendiary | i | （true/false）火球是否留下火焰 | false |
| charged | c | 火球是否处于充能状态 | false |
| fromorigin | fo | 是否从[原点](../targeters/origin.md)发射火球 | false |
| playsound | ps | 火球创建时是否播放发射音效 | false |
| smallfireball | small,sml | 是否使用较小的烈焰人火球，而不是恶魂火球 | false |
| type | t | 火球的类型 | SMALL |
| item | material | 使用 ITEM 类型时，火球的[材质](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html) | BLAZE_POWDER |

### Type 属性 {#type-attribute}

| 可用类型 |
| --- |
| NORMAL |
| SMALL |
| LARGE |
| WITHER |
| DRAGON |
| ITEM |

## 示例 {#examples}

此示例将向目标发射一连串 3 快速移动的火球。

```yaml
FireballBarrage:
  Skills:
  - shootfireball{y=1;v=4} @target
  - delay 10
  - shootfireball{y=1;v=4} @target
  - delay 10
  - shootfireball{y=1;v=4} @target
```

## 别名 {#aliases}

- fireball
