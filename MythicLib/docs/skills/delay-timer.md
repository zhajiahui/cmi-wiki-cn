---
title: 延迟与计时器
source: https://docs.phoenixdevt.fr/mythiclib/skills/delay-timer
source_snapshot: '2026-10-19'
---

# 延迟与计时器 {#⌚-delays-and-timers}

## 技能每 X 个周期运行一次（计时器） {#skills-that-run-every-x-ticks-timers}

`TIMER`是一种特殊的触发器类型，每 X 个周期就会投射技能。要设置定时技能，只需使用`timer`技能修饰符定义计时器周期（以刻为单位）。这是 **ANY**技能的默认技能修饰符，就像`cooldown`或`mana`一样。如果技能触发器未设置为`TIMER`，则此技能修饰符将变为100%无用，你可以忽略它。

## 向技能添加延迟 {#adding-delays-to-skills}

自MythicLib1.5起，任何技能都可能有**投射延迟**。当施放此类技能时，玩家会暂时减慢，并且必须等待一小段时间才能实际施放技能。这为技能提供了出色的RPG功能，例如传送或其他超级强大的技能。

你可以在MythicLib配置文件中配置投射延迟的特定选项：

```yml
# What happens when the player is waiting for his skill to cast
# Does not apply if skill delay (it is a skill modifier) is set to 0
casting-delay:
  slowness: 50 # A % based speed reduction when casting
  cancel-on-move: false # If the casting should cancel if the player moves

  cast-script: # MythicLib script called when the countdown begins
    enabled: true
    script:
      mechanics:
        play_sound:
          type: sound
          sound: BLOCK_END_PORTAL_FRAME_FILL
          volume: 1
          pitch: 2

  cancel-script: # MythicLib script called if the countdown is cancelled
    enabled: true
    # Other format:
    # script: <public_script_name>
    script:
      mechanics:
        play_sound:
          type: sound
          sound: ENTITY_VILLAGER_NO
          volume: 1
          pitch: 2

  bossbar: # Displayed during casting delay
    enabled: true
    format: 'CASTING'
```

`slowness`选项指示玩家在技能延迟期间减慢的程度。当启用`cancel-on-move`时，如果玩家移动，技能将取消：在这种情况下，增加速度是毫无用处的。

`cast-script`是玩家进入投射延迟时运行的MythicLib脚本。默认情况下，它只是播放一点声音。`cancel-script`是当玩家在等待时取消技能时运行的脚本。因此，仅当`cancel-on-move`启用时才会触发。

你还可以选择启用或禁用自定义 bossbar，它将向用户显示`CASTING`。

---

原文：[⌚ Delays and Timers](https://docs.phoenixdevt.fr/mythiclib/skills/delay-timer) · 原文归档：2026-10-19
