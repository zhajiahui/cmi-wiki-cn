---
title: 测试页面
source_url: https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Test-Page
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 测试页面

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v6"></path><path d="M12 17h.01"></path></svg>Important

这是你应该知道的重要事情。

以下是已实现粒子的列表，与其 DataType 组相关。根据它们所拥有的DataType，可以使用的属性也会相应变化。

**此列表的最新版本始终位于[此处](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html)的 spigot Javadoc 中**

- [DataTypes](test-page.md#datatypes)
  - [ItemStack](test-page.md#itemstack)
  - [BlockData](test-page.md#blockdata)
  - [MaterialData](test-page.md#materialdata)
  - [DustOptions](test-page.md#dustoptions)
  - [DustTransition](test-page.md#dusttransition)
- [Particles](test-page.md#particles)

# DataTypes {#datatypes}

## ItemStack {#itemstack}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m | 粒子所使用的材质。 | STONE |

## BlockData {#blockdata}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m | 粒子所使用的材质。 | STONE |

```yaml
  - effect:particles{particle=block_crack;material=COBBLESTONE}
```

## MaterialData {#materialdata}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m | 粒子所使用的材质。 | STONE |

## DustOptions {#dustoptions}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c | 粒子的颜色。 | #FF0000 |
| size |  | 粒子的大小。 | 1 |

## DustTransition {#dusttransition}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c, color1, c1, fromcolor, fc | 粒子的起始颜色。 | #FF0000 |
| color2 | c2, tocolor, tc | 粒子渐变到的颜色。 | #0000FF |
| size |  | 粒子的大小。 | 1 |

##  {#section}

# 粒子 {#particles}

| 灰烬（Ash） | 方块裂纹（Block Crack） |  |  |
| --- | --- | --- | --- |
|  |  |  |  |

### ash {#ash}

![ash](https://imgur.com/ggCYoIB.gif)

##  {#section-2}

### block_crack {#block-crack}

![block_crack](https://imgur.com/bHpnok7.gif)

### [BlockData](test-page.md#blockdata) {#blockdata-2}

### 别名 {#aliases}

- block
- blockcrack

##  {#section-3}

### block_dust {#block-dust}

![block_crack](https://imgur.com/oHIBddK.gif)

### [BlockData](test-page.md#blockdata) {#blockdata-3}

### 别名 {#aliases-2}

- dust
- blockdust

##  {#section-4}

### shriek {#shriek}

![image](https://imgur.com/eSmLMUL.gif)

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| rotation | rot, r | 粒子的旋转角度。 | 0 |

##  {#section-5}

### sculk_charge {#sculk-charge}

![image](https://example.org/)

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| rotation | rot, r | 粒子的旋转角度。 | 0 |

### 别名 {#aliases-3}

- sculkcharge
