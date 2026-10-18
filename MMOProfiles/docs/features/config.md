---
title: 配置选项
source: https://docs.phoenixdevt.fr/mmoprofiles/features/config
source_snapshot: '2026-10-19'
---

# 配置选项 {#⚙️-config-options}

## 不同的地图服务器 {#different-map-servers}

当多台服务器使用不同地图时，此选项很有用。例如，玩家退出一台服务器后进入另一台，是否还应传送到上次的位置？两台服务器的地图不同，坐标可能无法直接对应。

这主要是生存服务器的问题，因为大多数纯 RPG 群组服务器使用共享且不允许玩家破坏的地图。

受影响的是以下与位置有关的数据：

- 上次所在位置
- 床的重生点
- 指南针目标

为使用不同地图的服务器设置不同的服务器标识符，可以解决此问题。标识符相同的服务器会共享已保存的位置；标识符不同的服务器**不会**共享与位置有关的玩家数据。

```yml
server-identifier: 'default'
```

## 同步数据 {#synced-data}

这些字段用于分别开启或关闭原版数据的同步。某项设为 false 后，切换档案时就不会改变对应数据。

```yml
# Customization of the data that is synced or not between profiles.
synced-data:
  health: true
  health-scale: true
  food-level: true
  saturation: true
  walk-speed: true
  fly-speed: true
  allow-flight: true
  flying: true
  exp: true
  level: true
  air-level: true
  location: true
  respawn-location: true
  compass-target: true
  game-mode: true
  inventory: true
  ender-chest: true
  potion-effects: true
  attributes: true
  invulnerable: false
  balance: true
```

## 出生位置 {#spawn-locations}

`profile-selection-location` 是玩家加入服务器后选择档案时被传送到的位置。这里应当是封闭或受限区域，让玩家看不到太多内容，因为档案选择界面关闭时，玩家可能仍能移动。

```yml
# Location where players spawn to select their profile
profile-selection-location:
  world: 'world'
  x: 110
  y: 63
  z: -149
```

`new-profile-spawn-point` 是玩家开始使用新建档案时被传送到的位置。也可以将它设置在某个位置，再让命令方块或其他插件将玩家随机传送到别处。

```yml
new-profile-spawn-point:
  world: 'world'
  x: 110
  y: 63
  z: -149
```

## 档案名称 {#profile-names}

启用后，档案有各自的名称，创建时会要求玩家输入名称。关闭后，MMOProfiles 使用“Profile nX”，其中 X 为档案编号。

```yml
use-profile-names: false
```

## 默认档案 {#default-profile}

> **警告**
>
> 存在数据丢失风险！关闭此选项后，现有玩家未关联任何档案的数据会丢失。这也是默认启用此选项的原因。

启用后，之前已在服务器游玩过的玩家会获得一个默认档案，其中保留其原有数据。已有玩家基础的正式服务器安装 MMOProfiles 时，必须启用此项。

```yml
default-profile: true

# The default name of player's main profile
default-main-profile-name: 'Main'
```

## 处理已删除的世界 {#how-to-handle-deleted-worlds}

此选项用于解决玩家在已删除世界中重新出现的问题。

档案插件与地牢插件配合时，玩家有时会在已不存在的临时地牢世界中重新出现。为此，MMOProfiles 会保存玩家最近一次位于临时世界以外的位置，以处理玩家仍在临时世界中就退出的情况。

永久世界不会被临时删除，因此 MMOProfiles 允许玩家在这些世界中重新出现。如果找不到玩家最近所在的永久世界，MMOProfiles 就会将玩家送回档案出生点，这有时并不符合预期。如果该世界仍然存在，玩家就会正常出现在原处。

```yml
permanent-worlds:
  - 'world'
  - 'world_nether'
  - 'world_the_end'
  - 'another_world'
```

## 物品栏槽位黑名单 {#blacklist-for-inventory-slot}

可用此项禁止 MMOProfiles 处理某些槽位，例如 MMOInventory 或 ItemJoin 用作按钮的槽位。设为 [] 即关闭。示例：`[ 9, 10, 11, 12 ]`

```yml
inventory-slot-blacklist: [ ]
```

## 重新打开界面 {#reopen-gui}

玩家尚未选择档案时，MMOProfiles 再次打开档案选择界面前等待的时间，单位为刻（tick）。

```yml
gui-close-timeout: 40
```

## 强制游戏模式 {#force-gamemode}

启用后，会在选择档案时设置玩家的游戏模式。

```yml
force-game-mode:
  enabled: false
  game-mode: SURVIVAL
```

## 单一档案 {#unique-profile}

也可以用此插件在通过 BungeeCord/Velocity 代理连接的多台服务器之间，同步玩家的全部数据。将 `unique-profile` 设为 true 即可。

```yml
unique-profile: false
```

此模式下不会显示档案选择界面，玩家看不到插件的操作界面。插件只负责在多台服务器之间同步玩家的全部原版数据和插件数据。

## 处理资源包 {#how-to-handle-resource-packs}

如果服务器使用资源包，请启用此项。MMOProfiles 会等待资源包完全加载后，再首次打开档案选择界面。

```yml
resource-pack-options:
  wait-for-resource-pack: false
  resource-pack-load-delay: 40
```

## 关闭自动打开档案选择界面 {#disable-opening-profile-select-gui}

此选项兼容代理端档案选择。启用后，MMOProfiles **不会**在登录时自动打开档案选择界面，可以用 `/mmoprofiles open <player_name>` 手动打开。使用此选项时，没有额外的保护措施！

```yml
no-gui-on-login: false
```

可将此项用于登录过场动画和事件。它与 `wait-for-resource-pack` 选项不兼容。

> **警告**
>
> 存在玩家数据丢失风险！如果没有插件或命令打开档案选择界面，玩家在选择档案前产生的任何进度都会丢失。

## 可用档案或角色栏位数量 {#amount-of-profile-character-slots-available}

```yml
default-slots: 5
```

此项决定所有玩家默认拥有的档案栏位数。如果服务器设置了不同等级的会员组，可以使用下一个选项。

```yml
ranks:
  vip:
    permission: 'rank.vip' # You can change this permission to anything you'd like.
    slots: 7 # Amount of profiles the player has access to
    name: 'VIP' # Purely visual, used in the profile section UI
  vip_plus:
    permission: 'rank.vip_plus'
    slots: 10
    name: 'VIP+'
  mvp:
    permission: 'rank.mvp'
    slots: 12
    name: 'MVP'
  mvp_plus:
    permission: 'rank.mvp_plus'
    slots: 15
    name: 'MVP+'
```

可以添加任意数量的组。`vip` 和 `vip_plus` 只是内部使用的键名，具体名称不限，但必须互不相同。每组都需要填写显示名称和档案栏位数量；显示名称通过 `{rank}` 占位符显示在档案界面中尚未解锁的栏位上。无需手动按顺序排列各组，MMOProfiles 会自动排序。

## 脚本 {#scripts}

可以为特定操作指定脚本，脚本必须采用 [MythicLib 格式](../../mythiclib/scripts/intro.md)。`login` 脚本在玩家登录后、MMOProfiles 玩家数据成功加载时运行，可能需要等待几刻。`profile-select` 脚本在玩家选择档案后、所有兼容插件的数据加载完成时运行，也可能需要等待几刻。

```yml
script:

  # MythicLib script ran when the player creates a new profile.
  profile-create:
    mechanics:
      send_message:
        type: tell
        format: 'Welcome to your new profile!'

  # MythicLib script ran when the player logs in (before profile selection).
  login:
    mechanics:
      send_message:
        type: tell
        format: 'Welcome! Please choose the profile you''d like to play on.'

  # MythicLib script ran when the player chooses a profile (after login).
  profile-select:
    mechanics:
      play_sound:
        type: sound
        sound: ENTITY_PLAYER_LEVELUP
      send_message:
        type: tell
        format: 'Have fun!'
```

## 代理端档案 {#proxy-based-profiles}

启用后，MMOProfiles 会改用代理端模式，让玩家能够切换或伪装 UUID。其他插件会将其视为另一名玩家加入服务器，从而让任意插件都能按档案记录进度。代理端档案有[单独的说明页](proxy-based.md)。

---

原文：[⚙️ Config Options](https://docs.phoenixdevt.fr/mmoprofiles/features/config) · 原文归档：2026-10-19
