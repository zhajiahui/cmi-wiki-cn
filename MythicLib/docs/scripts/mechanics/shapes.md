---
title: 形状
source: https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/shapes
source_snapshot: '2026-10-19'
---

# 形状 {#📐-shapes}

> **警告**
>
> 建设中

要习惯这些可能非常复杂但配置起来非常有趣的机制，请使用简单的刻脚本来查看机制绘制的形状！

```yml
simple_tick:
  mechanics:
  - 'display_particle{particle=FLAME}'
```

## 螺旋 {#helix}

当螺旋线完全绘制时，将调用`end`配置选项指示的脚本。

```yml
example_mechanic:
    type: helix
    source: # Optional. Location targeter required
        type: source
    direction: # Optional. Location targeter required
        type: custom
        x: 1
        y: 0
        z: 0
    tick: simple_tick
    end: another_script

    # More options
    yaw: 360 # Amount of degrees 
    height: 3 # Height of helix
    radius: '2 + <caster.health> / 100'

    points: 40 # Amount of points displayed in one spiral
    time_interval: 1 # Interval of time (ticks) between two points
    points_per_tick: 1 # Amount of points displayed every interval
    helixes: 4 # Amount of spirals, 1 by default
```

## 抛物线 {#parabola}

两个位置之间显示的抛物线。你可以配置抛物线的高度及其显示速度。

```yml
example_mechanic:
    type: parabola
    source: # Location targeter required. Starting point of parabola
        type: caster
        position: BODY
    target: # Location targeter required. End point of parabola
        type: target
        position: BODY

    tick: simple_tick
    end: another_script # Called when reaching the end
    height: 10 # Height of parabola
    speed: 3 # Horizontal speed
```

## 投射物 {#projectile}

射弹停在第一个击中的方块/实体上。你必须指定你的射弹对应的交互类型（进攻性技能、支持技能等 - 了解更多信息 [此处](https://docs.phoenixdevt.fr/mythiclib/scripts/conditions/misc#if-script-caster-can-damagetarget-entity)）。

```yml
example_mechanic:
    type: projectile
    
    source: # Optional. Location targeter required
        type: caster
        position: EYES
    direction: # Optional. Location targeter required

    tick: simple_tick
    hit_entity: some_script # Called when hitting an entity
    hit_block: some_other_script # Called when hitting a block
    stop_on_block: true

    offense: true
    hits: 1 # Maximum amount of hit entities. Will disappear on last entity hit
    ignore_passable: false # It it should ignore passable blocks
    speed: 1 # 1 by default
    size: 0.2
    step: 0.2 # Distance between two calls of the tick script
    life_span: 60 # In ticks
```

## 光线投射 {#raycast}

光线投射是从玩家的眼睛位置发射的不可见光线。他们在第一个方块或实体命中时停止。

|参数|别名 |描述 |默认 |
| --- | --- | --- | --- |
| range | rng, length, len, distance, dist | 光线投射的长度 | 50 |
| size | width, wide | 光线投射的宽度 | 0.2 |
| step_size | step, st, ss | 两次调用刻脚本之间的距离 | 0.4 |
| ignore_passable | ip | 是否应忽略可通过的块 | false |
| neutral | - | 光线投射是否为中性（不检查友军火力） | false |
| offense | - | 光线投射是否具有攻击性（检查友军火力） | true |
| tick | - | 脚本调用光线投射的每一步 | none |
| hit_entity | - | 击中实体时调用的脚本 | none |
| hit_block | - | 击中方块时调用的脚本 | none |

```yml
example_script:
  mechanics:
  - 'raytrace{tick=simple_tick;hit_entity=some_other_script_name;range=50;size=0.2;step=0.4;ignore_passable=false}'
```

## 斜线 {#slash}

在脚本施法者面前执行类似武器的斜线操作

```yml
example_mechanic:
    type: slash

    tick: simple_tick
    end: some_other_script

    length: 4 # Slash length
    angle: -30 # Angle of the slash
    distance: 3 # Distance to the player

    # Same options as in the Helix mechanic
    points: 20
    time_interval: 1
    points_per_tick: 3
```

## 球体 {#sphere}

> **警告**
>
> 建设中

---

原文：[📐 Shapes](https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/shapes) · 原文归档：2026-10-19
