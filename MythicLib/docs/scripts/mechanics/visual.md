---
title: 视觉效果
source: https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/visual
source_snapshot: '2026-10-19'
---

# 视觉效果 {#🎨-visual}

> **警告**
>
> 建设中

## 向玩家发送消息 {#send-a-message-to-a-player}

这支持 PAPI占位符和颜色代码。

```yml
example_mechanic:
    type: tell
    format: 'Hello world!'
    target:
        type: caster
```

## 在目标位置播放声音 {#play-a-sound-at-target-location}

对于声音名称，你可以使用 [Bukkitjavadocs](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Sound.html)中的Bukkit/Paper声音名称，或使用Minecraft[原版声音名称](https://minecraft.wiki/w/Sounds.json/Java_Edition_values)。音高范围从0.5（低）到2（高）。

```yml
example_mechanic:
    type: sound
    sound: ENTITY_ENDER_DRAGON_FLAP
    pitch: 2
    volume: 1
    target:
        type: target_location
```

该机制还支持自定义声音。

```yml
#Custom Sound
example_mechanic:
    type: sound
    sound: minecraft:custom.effects.sound
    pitch: 2
    volume: 1
    target:
        type: target_location
```

## 产生一个粒子 {#spawn-a-particle}

粒子列表[此处为](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Particle.html)。

```yml
example_mechanic:
    type: particle
    target:
        type: circle
        radius: 3

    particle: FLAME
    amount: 30
    speed: 0.2
    x: 0
    y: 0
    z: 0
```

通过将 amount 设置为0，可以以初速度召唤粒子。你还可以使用它来召唤彩色粒子（特别是`REDSTONE`粒子）。`color`配置部分中提供的整数采用 RGB 格式，从0到255。

```yml
example_mechanic:
    type: particle
    target:
        type: circle
        radius: 3

    particle: REDSTONE
    amount: 1
    speed: 0
    x: 0
    y: 0
    z: 0
    color: # Color goes here.
        red: 255
        green: 220
        blue: 0
```

或者需要块数据的粒子（`BLOCK_CRACK`、`BLOCK_DUST`和`BLOCK_MARKER notably)`。你可以在`block`选项中找到可以使用的材质列表 [此处为](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)。

```yml
example_mechanic:
    type: particle
    target:
        type: circle
        radius: 3

    particle: BLOCK_CRACK
    amount: 1
    speed: 0
    x: 0
    y: 0
    z: 0
    block: PACKED_ICE
```

## 发送动作栏消息 {#send-an-action-bar-message}

这支持 PAPI占位符和颜色代码。有关消息优先级和持续时间，请参阅 [Messages](../../misc/player-messages.md#send-to-action-bar)wiki 页面。

```yml
example_script:
  mechanics:
    - 'action_bar{target=caster;format="&aYou have been hit for &c<damage> &adamage!";priority=30;duration=30}'
```

---

原文：[🎨 Visual](https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/visual) · 原文归档：2026-10-19
