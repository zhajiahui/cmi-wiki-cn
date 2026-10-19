---
title: Mythic 物品
source_url: https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/MythicItem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mythic 物品 {#mythic-item}

## 说明 {#description}

掉落一件 [Mythic 物品](../../items/items.md)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| level | lvl, l | 物品的等级 |  |
| lootsplosion | lootsplosionenabled, ls | 是否启用战利品喷发效果 |  |
| itemvfx | itemvfxenabled, iv | 是否启用物品视觉效果 |  |
| itemvfxmaterial | itemvfxmaterial, ivm | 物品视觉效果使用的材质 |  |
| vfxdata | vfxd | 物品视觉效果材质的自定义模型数据 |  |
| vfxcolor | vfxc, color | 物品视觉效果的颜色 |  |
| hologramname | hologramnameenabled, hn | 是否为掉落物启用全息图 |  |
| clientsidedrops | clientsidedropsenabled, csd | 是否启用客户端掉落物 |  |
| itemglowcolor | glowcolor, gc | 掉落物的发光颜色 |  |
| itembeamcolor | beamColor, bc | 掉落物的光束颜色 |  |
| billboarding | billboard, bill | 掉落物的面向模式（Billboarding） |  |
| brightness | bright, b | 掉落物的亮度 |  |

## 示例 {#examples}

```yaml
  Drops:
  - SuperCoolItem{lootsplosion=true} 2 0.5
```
