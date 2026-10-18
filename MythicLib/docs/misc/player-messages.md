---
title: 玩家消息
source: https://docs.phoenixdevt.fr/mythiclib/misc/player-messages
source_snapshot: '2026-10-19'
---

# 玩家消息 {#💬-player-messages}

MythicLib为所有 MMO 插件发送到玩家的消息提供统一的语法。

大多数 MMO 插件都有一个`messages.yml`配置文件，你可以在其中编辑插件发送的消息。以下是`MMOCore/messages.yml`配置文件的一部分。

```yml
level-up:
  sound: ENTITY_PLAYER_LEVELUP,1,2
  # Runs a script on level up. This script is implemented
  # inside file MythicLib/scripts/mmocore_scripts.yml
  script: mmocore_level_up_effect
  message:
    - ''
    - '&eCongratulations, you reached level &6{level}&e!'
    - '&eUse &6/p &eto see your new statistics!'
    - ''
#......
exp-notification:
  message: '&f{profession} &e{progress} &e{ratio}%'
  action-bar: true
  #sound: ENTITY_EXPERIENCE_ORB_PICKUP # Not recommended, can be spammy
death-exp-loss:
  - ''
  - '&4You died and lost {loss} experience.'
  - ''
#......
already-on-class: '&cYou are already a {class}.'
```

在接下来的部分中，我们将以玩家等级上升到其主职业(`level-up`) 时发送的MMOCore消息为例，但这适用于来自任何 MMO 插件的任何消息。

## 基本语法 {#basic-syntax}

这将向玩家聊天发送一行文本。

```yml
level-up:
  format: '&eCongratulations, you reached level &6{level}&e!'
```

这会将多行文本发送到玩家聊天。如你所见，`format`可以是文本，也可以是文本列表。

```yml
level-up:
  format: 
    - '&eCongratulations, you reached level &6{level}&e!'
    - '&eUse &6/p &eto see your new statistics!'
```

## 禁用消息 {#disable-a-message}

如果要禁用消息（例如`level-up`），以便在升级时不会向玩家发送任何消息，请使用以下语法：

```yml
level-up: ''
#level-up: [] # This works too
#level-up: {} # This works too
```

## 发送到动作栏 {#send-to-action-bar}

如果你想将消息发送到玩家的动作栏，请将`action-bar`设置为`true`。

```yml
level-up:
  format:
    - '&eCongratulations, you reached level &6{level}&e!'
    - '&eUse &6/p &eto see your new statistics!'
  action-bar: true
```

### 额外选项 {#extra-options}

在MythicLib中，动作栏被所有 MMO 插件共享。为了避免动作栏消息相互冲突，我们实现了一个基本的*消息优先级和超时*系统。

每条消息都有一个优先级和持续时间，它们都是正整数。One-time消息（例如level-up或航点使用消息）通常具有高优先级，而被动消息（例如MMOCore玩家信息和动作栏）通常具有低优先级。

当多条消息同时发送到同一个玩家时，只有具有最高优先级的消息才会显示在玩家的动作栏上。high-priority消息将在设定的时间段（消息持续时间）内暂时“隐藏”低优先级的消息。

可以使用以下语法编辑消息优先级和持续时间

```yml
level-up:
  format: 'My message'
  action-bar: true # Has to be on
  priority: 30     # Message priority
  duration: 50     # In ticks, 2.5 seconds
```

MMOCore玩家信息动作栏在优先级`LOW`上运行，设置为`20`。MMOCore技能施放动作栏在设置为`30`的优先级`NORMAL`上运行。

## 播放声音 {#play-a-sound}

消息发送到玩家时可以播放声音。基本语法是`<sound_name>,<pitch>,<volume>`。声音名称可以是以下之一：

- [Bukkit声音](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Sound.html)，
- 资源包提供的自定义声音，例如`itemsadder:sound_id`，
- Minecraft[原版声音](https://minecraft.fandom.com/wiki/Sounds.json/Java_Edition_values)类似于`minecraft:entity.zombie.ambient`。

如果你想将音调和音量设置为1，则只需使用`<sound_name>`即可。音高范围从0.5（低音）到2（高音），默认为1。音量默认为1。

```yml
level-up:
  format: #......
  sound: 'ENTITY_PLAYER_LEVELUP,1,1' # Or simply 'ENTITY_PLAYER_LEVELUP'
```

如果你更喜欢 YML 语法而不是comma-separated值，你还可以使用以下语法：

```yml
level-up:
  format: #.....
  sound:
    sound: ENTITY_PLAYER_LEVELUP
    vol: 1
    pitch: 1
```

你甚至可以删除`format`字段，只向玩家发送声音，而不向玩家聊天或动作栏发送文本。

## 调用MythicLib脚本 {#call-a-mythiclib-script}

当消息发送到玩家时，你可以运行MythicLib脚本。例如，MythicLib附带一个名为`mmocore_level_up_effect`的脚本，该脚本在玩家周围显示小粒子效果。默认情况下，当玩家等级启动其主职业或副职业时，会调用它。

```yml
level-up:
  format: #......
  sound: #......
  script: 'mmocore_level_up_effect'
```

这是`mmocore_level_up_effect`脚本的代码，可以在`MythicLib/script/mmocore_scripts.yml`文件中找到。

```yml
# Script ran when leveling up
# Displays a helix of particles around the player
# This is configured in MMOCore/messages.yml > level-up.script
mmocore_level_up_effect:
  mechanics:
    - "helix{tick=mmocore_level_up_effect_tick;radius=1;height=2}"

mmocore_level_up_effect_tick:
  mechanics:
    - "spawn_particle{particle=TOTEM}"
```

---

原文：[💬 Player Messages](https://docs.phoenixdevt.fr/mythiclib/misc/player-messages) · 原文归档：2026-10-19
