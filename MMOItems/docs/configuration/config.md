---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 6.10.1-SNAPSHOT
---

# config.yml

文件：`config.yml`。版本：`6.10.1-SNAPSHOT`。

主配置。

连接信息或服务器标识已替换为示例值，使用时填写自己的信息。

## `config-version` { #config-version }

```yaml title="config.yml · config-version"
# !! 请勿修改 !!
# 修改此项会严重扰乱所有插件配置文件。
config-version: 10
```

## `update-notify` { #update-notify }

```yaml title="config.yml · update-notify"
# 如果有可下载的新版本，在拥有 'mmoitems.update-notify' 权限节点的玩家
# 加入服务器时通知他们。
# 更改在服务器重启后生效。
update-notify: true
```

## `iterate-whole-inventory` { #iterate-whole-inventory }

```yaml title="config.yml · iterate-whole-inventory"
# 启用或禁用插件对玩家整个物品栏的遍历，
# 而不是只检查玩家的盔甲和手持物品。
# Ornament 物品类型需要启用此选项，但
# 它可能造成卡顿和/或占用大量内存。
iterate-whole-inventory: false
```

## `locked-skins` { #locked-skins }

```yaml title="config.yml · locked-skins"
# 设为 true 时，一件物品只能应用一次皮肤。 
locked-skins: true
```

## `inventory-update-delay` { #inventory-update-delay }

```yaml title="config.yml · inventory-update-delay"
# 默认情况下，每隔
# 10 刻更新所有玩家的物品栏，即每秒更新 2 次。
inventory-update-delay: 10
```

## `mysql` { #mysql }

```yaml title="config.yml · mysql"
# MySQL 支持
mysql:
  enabled: false
  host: "HOST"
  port: 3306
  database: "DATABASE"
  user: "USERNAME"
  pass: "PASSWORD"
  maxPoolSize: 10
  maxLifeTime: 300000
  connectionTimeOut: 10000
  leakDetectionThreshold: 150000
  properties:
    cachePrepStmts: true
    prepStmtCacheSize: 250
    prepStmtCacheSqlLimit: 2048

  userdata-table-name: "TABLE_NAME"
```

## `item-level-spread` { #item-level-spread }

```yaml title="config.yml · item-level-spread"
# 生成物品时，物品等级
# 必须与玩家等级大致相符，
# 否则玩家可能无法使用物品，或得到无用的物品。
#
# 物品等级始终处于以下
# 区间 [playerLevel - spread, playerLevel + spread]
item-level-spread: 2
```

## `enable_flag_checks` { #enable_flag_checks }

```yaml title="config.yml · enable_flag_checks"
# 使用 WorldGuard 时，这些标志检查有时会
# 消耗较多性能。如果服务器使用 WorldGuard，但
# 未使用某些标志，可以在此关闭相应检查
# 以提高性能。
#
# 有关 WorldGuard 标志的更多信息：
# https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Plugin-Compatibility#flag-plugins
enable_flag_checks:
    commands: true
    weapons: true
    consumables: true
    tools: true
```

## `consumables` { #consumables }

```yaml title="config.yml · consumables"
consumables:

    # 默认关闭。设为 true 时，如果玩家正看着
    # 可交互方块，右键使用消耗品
    # 不会消耗该物品(例如箱子、工作台等)。
    # 仅适用于 Spigot 1.21+
    disable_clicks_on_blocks: false
```

## `durability` { #durability }

```yaml title="config.yml · durability"
durability:

    # 盔甲耐久度按以下方式扣除：玩家每承受 4 点
    # 伤害，物品就扣除
    # 一点耐久度。同时扣除的
    # 耐久度没有上限。这在
    # 原版 Minecraft 中没有问题，但某些技能
    # 会造成大量伤害，可能一击损坏盔甲，
    # 严重影响游戏体验。
    #
    # 此选项限制单次损失的耐久度上限。
    # 设为 0 可禁用此选项。默认禁用，
    # 以免影响原版默认行为。
    #
    # 执行特定操作时会损失多少耐久度，
    # 可参阅 Minecraft Wiki：
    # https://minecraft.fandom.com/wiki/Durability
    loss_cap: 0
```

## `default-tier-name` { #default-tier-name }

```yaml title="config.yml · default-tier-name"
# 没有品质的物品会使用此名称
# 作为默认品质名称。
default-tier-name: "普通"
```

## `default-item-capacity` { #default-item-capacity }

```yaml title="config.yml · default-item-capacity"
# 生成未指定品质的物品时，
# 将使用此容量计算公式。
default-item-capacity:
    base: 3
    scale: 0
    spread: 0
    max-spread: 0
```

## `default` { #default }

```yaml title="config.yml · default"
# 更改部分属性的默认值。这主要
# 用于法杖、火枪等无需选定目标的武器。
default:
    attack-speed: 0.67 # 仅用于旧版远程武器（鲁特琴、火枪等），以后将移除
    range: 16
    recoil: 0.1
```

## `dropped-items` { #dropped-items }

```yaml title="config.yml · dropped-items"
# 更改在服务器重启后生效。
dropped-items:

    # 根据物品品质设置掉落物的发光效果
    tier-glow: true

    # 在掉落物上方显示物品名称
    hints: true
```

## `enable_item_granted_permissions` { #enable_item_granted_permissions }

```yaml title="config.yml · enable_item_granted_permissions"
# 关闭此项可完全禁用物品权限。
# 此属性与物品命令一样，如果允许管理人员或管理员使用，
# 可能引发严重的安全问题。如果
# 不打算使用此属性，可以考虑完全禁用。
enable_item_granted_permissions: true
```

## `item_commands` { #item_commands }

```yaml title="config.yml · item_commands"
item_commands:

  # 关闭此项可完全禁用物品命令。
  # 此属性与物品命令一样，如果允许管理人员或管理员使用，
  # 可能引发严重的安全问题。如果
  # 不打算使用此属性，可以考虑完全禁用。
  enabled: true

  # 物品命令白名单的正则表达式列表。
  # 为了提高安全性，请谨慎选择允许
  # 通过物品命令执行的命令。任何
  # 未匹配此列表中任何表达式的命令都无法执行。
  # 正则表达式示例：
  # - "dm open .*" 匹配所有以 "dm open" 开头的命令
  # - ".*hello world" 匹配所有以 "hello world" 结尾的命令
  # - "hat" 精确匹配命令 "hat"
  # 设为 [] 可禁用白名单
  whitelist: []
```

## `op-item-stats` { #op-item-stats }

```yaml title="config.yml · op-item-stats"
# 某些物品属性，如 'Commands' 或 NBTTags，可能被滥用以获取 op。
# 可以为这些属性绑定特定权限，限制谁可以编辑它们。
# 此选项需要支持 Vault 的权限插件才能生效。
# 对应权限为 "mmoitems.edit.op"。
op-item-stats:
  enabled: false
  stats:
    - COMMANDS
    - CUSTOM_NBT
    - GRANTED_PERMISSIONS
```

## `item-upgrading` { #item-upgrading }

```yaml title="config.yml · item-upgrading"
item-upgrading:

    # 升级物品的显示名称后缀。
    name-suffix: ' &8(&e+#lvl#&8)'

    # 显示在物品名称中还是描述中
    # 如果玩家可以重命名物品，请禁用。
    # 如果设为 'false'，记得在
    # 物品描述中加入 {upgrade_level}。
    display-in-name: true

    # 是否在描述中显示
    # 哪些属性发生了变化。
    display-stat-changes: false
    stat-change-suffix: ' &8(<p>#stat#&8)'
    stat-change-positive: '&a'
    stat-change-negative: '&c'
```

## `stats-displaying` { #stats-displaying }

```yaml title="config.yml · stats-displaying"
stats-displaying:

    # 此项作为数值属性的前缀，
    # 在属性变化不利时改变其颜色。
    color-positive: ''
    color-negative: ''

    # 在合成站显示带有随机数值的物品时，
    # 此项是数值下限与
    # 上限之间的分隔符：Attack Damage  +5⎓7.5
    range-dash: '⎓'
```

## `soulbound` { #soulbound }

```yaml title="config.yml · soulbound"
soulbound:

    # 修改玩家尝试使用未绑定到自己的
    # 物品时受到的灵魂绑定伤害。
    damage:
        base: 1
        per-lvl: 1

    # 玩家死亡时是否保留
    # 灵魂绑定物品。
    keep-on-death: true

    # [实验性功能]
    # 关闭后，玩家无法丢弃灵魂绑定物品，
    # 也无法将其移出物品栏。
    # 需要启用 `keep-on-death`。
    # 更改在服务器重启后生效。
    can-drop: true
```

## `gem-sockets` { #gem-sockets }

```yaml title="config.yml · gem-sockets"
gem-sockets:

    # 在此定义一种文本，将其填入物品的
    # 宝石孔后可创建无颜色的
    # 宝石孔，即可镶嵌任何类型宝石的孔。
    uncolored: 'Uncolored'
```

## `custom-blocks` { #custom-blocks }

```yaml title="config.yml · custom-blocks"
custom-blocks:

    # 是否按照自定义方块的
    # 生成模板
    # 在世界中生成这些方块。
    enable-world-gen: false

    # 使用精准采集挖掘蘑菇方块时，
    # 是否从掉落列表中
    # 移除蘑菇方块掉落物。
    # 强烈建议使用自定义方块的服务器启用，
    # 因为蘑菇方块可能破坏整个系统。
    replace-mushroom-drops: true
```

## `item-upgrade-requirements-check` { #item-upgrade-requirements-check }

```yaml title="config.yml · item-upgrade-requirements-check"
# 设为 true 后，如果物品升级后的
# 要求(等级、副职业要求)
# 高于玩家当前水平，玩家将无法升级该物品。
item-upgrade-requirements-check: true
```

## `two-handed-item-restriction` { #two-handed-item-restriction }

```yaml title="config.yml · two-handed-item-restriction"
# 同时持有双手物品和另一件物品时，
# 玩家无法使用武器或技能。
# 关闭后，玩家仍会受到缓慢 4 效果。
two-handed-item-restriction: true
```

## `cooldown-progress-bar-char` { #cooldown-progress-bar-char }

```yaml title="config.yml · cooldown-progress-bar-char"
# 可以选择用于组成
# 物品技能冷却进度条的字符。
cooldown-progress-bar-char: █
```

## `action-bar-display` { #action-bar-display }

```yaml title="config.yml · action-bar-display"
# 在快捷栏上方显示消息，而不是发送到聊天栏。
# 可用于减少聊天刷屏。
# 可能与其他快捷栏消息插件互相干扰。
action-bar-display:
    ability-cooldown: true
    item-cooldown: true
    not-enough-mana: true
    not-enough-stamina: true
    two-handed: true
    cant-use-item: true
    item-break: false
```

## `recipes` { #recipes }

```yaml title="config.yml · recipes"
recipes:

    # 为 MMOItems 配方启用原版配方书
    use-recipe-book: true
```

## `disable-interactions` { #disable-interactions }

```yaml title="config.yml · disable-interactions"
# "repair" 阻止玩家修复 MMOItems 物品。
# "smelt" 阻止玩家熔炼 MMOItems 物品。
# 'enchant" 禁止为 MMOItems 物品附魔。
# "craft" 阻止玩家将 MMOItems 物品用作合成材料。
# "arrow-shooting" 阻止玩家射出作为箭矢的 MMOItems 物品。
disable-interactions:
    interact: false
    repair: false
    enchant: false
    smelt: false
    smith: false
    craft: false
    arrow-shooting: false
```

## `block-blacklist` { #block-blacklist }

```yaml title="config.yml · block-blacklist"
# 无法被技能或物品效果破坏的方块类型
block-blacklist:
    - OBSIDIAN
```

## `permissions` { #permissions }

```yaml title="config.yml · permissions"
# 启用或禁用使用物品、技能所需的权限检查。
# 技能的通用权限节点：mmoitems.ability.ability-id
# 例如：- mmoitems.ability.fire-meteor
#     - mmoitems.ability.slow
#     - mmoitems.ability.cursed-fangs
#     等。
permissions:
    abilities: false
    items: true
```

## `additive-spread-formula` { #additive-spread-formula }

```yaml title="config.yml · additive-spread-formula"
#
# 物品属性具有数值范围时的示例。
# attack-damage:
#    base: 10
#    spread: 1
#
# 利用 spread、等级和随机数，
# 得到一个随机值(与 spread 密切相关)：1.7
#
# additive-spread-formula 为 true 时，将该值加到基础值上：
#    RESULT: 10 + 1.7  =  11.7 attack damage
#
# additive-spread-formula 为 false 时，将基础值乘以该值：
#    RESULT: 10 * 1.7  =  17 attack damage
#
additive-spread-formula: false
```

## `disable-vanilla-recipes` { #disable-vanilla-recipes }

```yaml title="config.yml · disable-vanilla-recipes"
# 禁止在原版工作台中合成非 MMOItems 物品。
# 列表为空时填入 []。
disable-vanilla-recipes: []
```

## `item-revision` { #item-revision }

```yaml title="config.yml · item-revision"
# - DIAMOND_PICKAXE
# - IRON_BLOCK

# 物品修订系统的选项
item-revision:

    # 取出的宝石会保留最初镶入物品时的属性，
    # 禁用此选项
    # 可强制重新生成宝石。
    regenerate-gems-when-unsocketed: false

    # 用于继承品质的旧选项；若未在其他 keep- 标志旁指定，
    # 此选项将优先生效。
    keep-tiers: true

    # 物品更新后，如果新版本
    # 不保留宝石，此项会将宝石归还
    # 给玩家，避免宝石永久丢失。
    drop-extra-gems: true

    # 保留描述数据时，只保留
    # 以此内容开头的描述行。
    kept-lore-prefix: '&7'

    # 物品更新到最新修订版本时，
    # 是否保留特定属性。
    keep-data:

        # 物品名称，通常通过铁砧重命名
        display-name: true

        # 玩家为物品添加的附魔
        enchantments: true

        # 物品上的灵魂绑定
        soulbound: true

        # 物品上的宝石
        gems: true

        # 物品的升级等级
        upgrades: true

        # 物品的特定描述行……
        # 警告：这会使描述中显示的属性不再更新！
        lore: false

        # 其他插件可能写入的数据。
        exsh: true

        # 由随机数决定的属性会重新随机
        reroll: false

        # 物品修饰器 ~ Sharp、Light、Heavy、Arcane
        modifications: true

        # 由 MMOItems 应用的皮肤
        skins: true

        # 物品品质
        tier: true

        # 第三方插件兼容
        advanced-enchantments: true

    # 物品中镶嵌的宝石更新到最新修订版本时，
    # 是否保留特定属性。
    keep-gem-data:

        # 物品名称，通常通过铁砧重命名
        display-name: true

        # 玩家为物品添加的附魔
        enchantments: true

        # 物品的特定描述行……
        # 警告：这会使描述中显示的属性不再更新！
        lore: false

        # 由随机数决定的属性会重新随机
        reroll: false

    phat-loots:
        display-name: false
        enchantments: false
        soulbound: false
        gems: true
        upgrades: false
        lore: false
        exsh: false
        tier: true
        skins: false
        reroll: true
        modifications: false
        advanced-enchantments: false

    # 这些内容在 PhatLoots 中完全不会更新，
    # 以兼容需要检查
    # 精确 NBT 的任务插件
    disable-phat-loot:
        - MANGO
        - STEEL_HELMET

    # 在此可分别禁用一些事件，
    # 这些事件会在发现更高修订 ID 时更新物品
    disable-on:
        pickup: false
        craft: true # 建议设为 'true'
        click: false
        join: false
```

## `lootsplosion` { #lootsplosion }

```yaml title="config.yml · lootsplosion"
# Offset 是沿 X 和 Y 坐标移动的距离
# Height 是 Y 方向的速度。战利品喷发
# 仅对 MythicMobs 怪物触发。
# 更改在服务器重启后生效。
lootsplosion:
    enabled: true
    color: true
    offset: .2
    height: .6
```

## `gem-upgrade-default` { #gem-upgrade-default }

```yaml title="config.yml · gem-upgrade-default"
# 升级与宝石同时使用时，需要决定
# 是否也提高宝石提供的属性。
gem-upgrade-default: 'NEVER'
```

## `disable-removed-items` { #disable-removed-items }

```yaml title="config.yml · disable-removed-items"
# 此选项可禁止使用
# 已经从配置中移除的 MMOItems 物品。
disable-removed-items: true
```

## `default-pickaxe-power` { #default-pickaxe-power }

```yaml title="config.yml · default-pickaxe-power"
# 根据物品材质设置默认挖掘等级(仅用于自定义方块)。
# 挖掘等级不作用于原版方块，只作用于 MMOItems 方块。
# 可以在此列表中任意添加或移除材质。
default-pickaxe-power:
    WOODEN_PICKAXE: 5
    STONE_PICKAXE: 10
    GOLDEN_PICKAXE: 15
    IRON_PICKAXE: 20
    DIAMOND_PICKAXE: 25
    NETHERITE_PICKAXE: 30
    # 可以按需添加任意数量。
```
