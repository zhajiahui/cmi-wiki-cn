---
title: Boss 血条
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/BossBar
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Boss 血条 {#boss-bar}

BossBar 功能可为自定义生物添加与末影龙、凋灵风格相同的生命条，同时提供更多自定义选项。

## 语法 {#syntax}

```yaml
internal_mobname:
  Type: <mobtype>
  BossBar:
    Enabled: [true/false]
    Title: '[name]'
    Range: [range]
    Color: [color]
    Style: [style]
    CreateFog: [true/false]
    DarkenSky: [true/false]
    PlayMusic: [true/false]
```

### Color {#color}

Color 的可用颜色（区分大小写）：PINK、BLUE、RED、GREEN、YELLOW、PURPLE、WHITE。

### Style {#style}

Style 的可用样式（区分大小写）：SOLID、SEGMENTED_6、SEGMENTED_10、SEGMENTED_12、SEGMENTED_20。

### Range {#range}

Range 表示 Boss 血条对生物周围玩家的显示距离。

### 额外选项 {#extra-options}

CreateFog 会在玩家处于 Boss 血条定义的半径内时，为其视野添加类似雾的效果。

DarkenSky 会在玩家处于 Boss 血条定义的半径内时，使天空变暗，类似凋灵生成时的效果。

## 示例 {#examples}

```yaml
SuperCreeper:
  Type: creeper
  Display: '&cTest'
  Health: 20
  BossBar:
    Enabled: true
    Title: 'Test'
    Range: 20
    Color: RED
    Style: SOLID
```
