---
title: elements.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: elements.yml
source_version: 1.7.1-SNAPSHOT
---

# elements.yml

文件：`elements.yml`。版本：`1.7.1-SNAPSHOT`。

随包配置。

## `FIRE` { #fire }

```yaml title="elements.yml · FIRE"
FIRE:

  # MMOCore 和 MMOItems 使用的公开译名
  name: "火"

  # 与该元素关联的物品，用于 MI 物品编辑器
  icon: BLAZE_POWDER

  # 用于伤害显示和 MI 物品描述的图标
  lore-icon: '🔥'

  # 与该元素关联的颜色，用于伤害显示和 MI 物品描述
  color: '&c'

  # 进行普通元素攻击时执行的内容
  regular-attack:
    mythiclib-skill-id: fire_elemental_attack

  # 进行元素暴击时执行的内容
  # 此项可选。未指定时不会发生暴击
  crit-strike:
    mythiclib-skill-id: fire_critical_strike
```

## `ICE` { #ice }

```yaml title="elements.yml · ICE"
ICE:
  name: "冰"
  icon: SNOWBALL
  lore-icon: '❄'
  color: '&b'
  regular-attack:
    mythiclib-skill-id: ice_elemental_attack
  crit-strike:
    mythiclib-skill-id: ice_critical_strike
```

## `EARTH` { #earth }

```yaml title="elements.yml · EARTH"
EARTH:
  name: "土"
  icon: OAK_SAPLING
  lore-icon: '₪'
  color: '&2'
  regular-attack:
    mythiclib-skill-id: earth_elemental_attack
  crit-strike:
    mythiclib-skill-id: earth_critical_strike
```

## `WIND` { #wind }

```yaml title="elements.yml · WIND"
WIND:
  name: "风"
  icon: FEATHER
  lore-icon: '🌊'
  color: '&7'
  regular-attack:
    mythiclib-skill-id: wind_elemental_attack
  crit-strike:
    mythiclib-skill-id: wind_critical_strike
```

## `THUNDER` { #thunder }

```yaml title="elements.yml · THUNDER"
THUNDER:
  name: "雷"
  icon: GUNPOWDER
  lore-icon: '★'
  color: '&e'
  regular-attack:
    mythiclib-skill-id: thunder_elemental_attack
  crit-strike:
    mythiclib-skill-id: thunder_critical_strike
```

## `WATER` { #water }

```yaml title="elements.yml · WATER"
WATER:
  name: "水"
  icon: LILY_PAD
  lore-icon: '🌊'
  color: '&3'
  regular-attack:
    mythiclib-skill-id: water_elemental_attack
  crit-strike:
    mythiclib-skill-id: water_critical_strike
```

## `DARKNESS` { #darkness }

```yaml title="elements.yml · DARKNESS"
DARKNESS:
  name: "黑暗"
  icon: COAL
  lore-icon: '☽'
  color: '&8'
  regular-attack:
    mythiclib-skill-id: none
```

## `LIGHTNESS` { #lightness }

```yaml title="elements.yml · LIGHTNESS"
  # 无法暴击

LIGHTNESS:
  name: "光明"
  icon: GLOWSTONE_DUST
  lore-icon: '☀'
  color: '&f'
  regular-attack:
    mythiclib-skill-id: none
  # 无法暴击
```
