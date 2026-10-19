---
title: 烟花
source_url: https://wiki.mythiccraft.io/mythicmobs/Items/Firework
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 烟花

# Firework {#firework}

此属性用于修改 firework 或 firework_charge 物品的烟花效果。每个 firework 或 firework_charge 物品都必须具有此属性。

### 格式 {#format}

```yml
ItemName:
  Id: material
  Firework:
    Colors:
    FadeColors:
    Flicker:
    Trail:
```

## 烟花配置详解 {#breaking-down-the-firework-configuration}

### 颜色 {#colors}

要添加到烟花效果中的主颜色列表。颜色必须使用 RGB(red,green,blue) 格式。

```yml
# adds red(255,0,0), green(0,255,0), and blue(0,0,255) colors
# to the firework effect
example_item:
  Id: firework_charge
  Firework:
    Colors:
      - 255,0,0
      - 0,255,0
      - 0,0,255
```

### FadeColors {#fadecolors}

与 [colors](https://wiki.mythiccraft.io/mythicmobs/Items/Firework#Colors) 选项类似，但将颜色应用于渐变效果。

```yml
example_item:
  Id: firework_charge
  Firework:
    Colors:
      - 255,0,0
      - 0,255,0
      - 0,0,255
    FadeColors:
      - 255,0,255
      - 0,255,0
```

### 闪烁 {#flicker}

烟花效果是否闪烁。

```yml
example_item:
  Id: firework_charge
  Firework:
    Flicker: true
```

### Trail {#trail}

烟花效果是否带有拖尾。

```yml
example_item:
  Id: firework_charge
  Firework:
    Trail: true
```
