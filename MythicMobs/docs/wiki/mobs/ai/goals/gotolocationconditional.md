---
title: Go To Location Conditional
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/goToLocationConditional
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Go To Location Conditional

# 满足条件时前往指定位置 {#go-to-location-conditional}

## 说明 {#description}

让生物前往某个位置，但仅在该位置和生物满足给定条件时移动。位置可以使用占位符，例如位置变量；值发生变化时，生物会跟随新的位置。进入该位置的 `minrange` 范围、某项条件不再满足，或无法再读取位置时，生物就会停止。

写为 `x,y,z` 的位置属于生物当前所在的世界。写为 `world,x,y,z` 的位置只有在生物处于该世界时才生效；在其他任何世界中，生物都不会向它移动。如果无法读取直接写在配置中的位置，例如指定的世界不存在，控制台会显示警告。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| location | loc, l | 要前往的位置，格式为 `x,y,z` 或 `world,x,y,z`。支持占位符。 |  |
| speed | s | 速度修饰值。 | 1 |
| minrange | minr, mr | 生物进入距该位置此距离的范围内后，停止移动。 | 2 |
| cooldown | cd, interval, i | 生物移动时重新计算路径的间隔，单位为刻。 | 5 |
| locationconditions | locconditions, lconditions, lcond, lc | 位置必须满足的条件。 |  |
| mobconditions | mconditions, mcond, mc | 生物自身必须满足的条件。 |  |

## 示例 {#examples}

前往变量中保存的位置，但仅在生物的 `state` 变量为 `returning` 时移动：

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
  - 0 clear
  - 1 goToLocationConditional{location=<caster.var.home>;minrange=3;mobConditions=[ - variableEquals{var=caster.state;value=returning} ]}
  Skills:
  - setvariable{var=caster.home;type=LOCATION;value=world,100,64,100} @self ~onSpawn
```

仅在距离小于 30 格时，以 1.5 的速度前往固定位置：

```yaml
  AIGoalSelectors:
  - clear
  - gotoCond{location=100,64,100;speed=1.5;locationConditions=[ - distance{d=<30} ]}
```

也可以在行为目标名称后填写位置和速度：

```yaml
  AIGoalSelectors:
  - clear
  - gotoCond 100,64,100 1.5
```

## 别名 {#aliases}

- gotoConditional
- goToLocationCond
- gotoCond
