---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 1.7.1-SNAPSHOT
---

# config.yml

文件：`config.yml`。版本：`1.7.1-SNAPSHOT`。

主配置。

## `config-version` { #config-version }

```yaml title="config.yml · config-version"
# 请勿修改
config-version: 5
```

## `debug` { #debug }

```yaml title="config.yml · debug"
# 启用后，会向控制台输出详细调试消息。
# 此选项适用于所有 MMO- 插件。
debug: false
```

## `max-sync-tries` { #max-sync-tries }

```yaml title="config.yml · max-sync-tries"
# MMOInventory 和 MMOCore 使用此选项，在通过代理连接的服务器之间
# 同步玩家数据。玩家切换
# 服务器后，插件每隔 1s 尝试获取新数据，共尝试 X 次，
# 默认最多尝试 5 次。
#
# 如果 SQL 连接不稳定，请提高此值，
# 以免丢失玩家数据。
max-sync-tries: 5
```

## `number-format` { #number-format }

```yaml title="config.yml · number-format"
# 在此编辑插件的通用数字格式。
# 更改在服务器重启后生效。
number-format:
  decimal-separator: .
```

## `defense-application` { #defense-application }

```yaml title="config.yml · defense-application"
# 定义防御的作用方式。公式应根据
# 以下输入值返回最终造成的伤害：
# - 造成的伤害 #damage#
# - 玩家当前的防御 #defense#
#
# 默认公式参考《流放之路》，可以在其 Wiki
# 了解更多：https://pathofexile.fandom.com/wiki/Armour
#
# natural   <-> 非元素伤害
# elemental <-> 火/水/等元素伤害
defense-application:
  natural: '#damage# - #defense#'
  elemental: '#damage# * (1 - (#defense# / (5 * #damage# + #defense#)))'
```

## `skip_elemental_damage_application` { #skip_elemental_damage_application }

```yaml title="config.yml · skip_elemental_damage_application"
# 默认情况下，MythicLib 会计算玩家的元素伤害
# 属性，先将其自动作为命中伤害应用，再执行
# 普通攻击或暴击的自定义命中脚本。
#
# 启用后，MythicLib 不会应用元素伤害，需要
# 由用户自行处理。因此，普通攻击的
# 命中脚本会优先执行。
skip_elemental_damage_application: false
```

## `health-scale` { #health-scale }

```yaml title="config.yml · health-scale"
# 允许将生命值显示缩放到指定
# 数量，避免额外生命值占满屏幕。
# 更改在服务器重启后生效。
# 如果玩家仍然遇到爱心数量显示过多的问题，应设置延迟。MySQL Inventory Bridge 等插件可能导致此问题
# 延迟单位为刻。20 刻 = 1 秒
health-scale:
  enabled: false
  scale: 20
  delay: 0
```

## `critical-strikes` { #critical-strikes }

```yaml title="config.yml · critical-strikes"
critical-strikes:
  weapon:
    coefficient: 2 # 默认为 2，表示暴击造成原始伤害的 200%
    cooldown: 3
  skill:
    coefficient: 1.5 # 默认为 1.5，表示暴击造成原始伤害的 150%
    cooldown: 3
```

## `ignore_shift_triggers` { #ignore_shift_triggers }

```yaml title="config.yml · ignore_shift_triggers"
# 启用后，禁用 SHIFT_<RIGHT_CLICK/DROP_ITEM/...> 触发类型，
# 即使玩家正在潜行，也会触发对应的基础触发器。
#
# 使用此选项时，SHIFT_<...> 触发器仍然存在，但不会
# 触发任何技能，忽略它们即可。
ignore_shift_triggers: false
```

## `ignore_offhand_click_triggers` { #ignore_offhand_click_triggers }

```yaml title="config.yml · ignore_offhand_click_triggers"
# 启用后，不会触发副手物品
# 提供的技能。默认为 false。
ignore_offhand_click_triggers: false
```

## `casting-delay` { #casting-delay }

```yaml title="config.yml · casting-delay"
# 玩家等待技能施放期间的行为
# 技能延迟(技能参数)设为 0 时不生效
casting-delay:
  slowness: 60 # 施法时按百分比降低的移动速度
  cancel-on-move: false # 玩家移动时是否取消施法
  
  cast-script: # 倒计时开始时调用的 MythicLib 脚本
    enabled: true
    script:
      mechanics:
      - sound{sound=BLOCK_END_PORTAL_FRAME_FILL;volume=1;pitch=2}
  
  cancel-script: # 倒计时取消时调用的 MythicLib 脚本
    enabled: true
    # 另一种格式：
    # script: <public_script_name>
    script:
      mechanics:
      - sound{sound=ENTITY_VILLAGER_NO;volume=1;pitch=2}
  
  bossbar: # 施法延迟期间显示
    enabled: true
    format: "施法中"
    style: SEGMENTED_20
    color: PURPLE
```

## `mitigation` { #mitigation }

```yaml title="config.yml · mitigation"
# 护甲/伤害减免属性的默认值和最大值。这些
# 属性都有冷却时间，可以使用
# '*** Cooldown Reduction' 物品属性缩短冷却。
mitigation:
  
  # 在此编辑伤害减免提示消息。留空则不发送消息。
  message:
    
    # 是否在快捷栏上方显示，而不是在聊天栏显示
    action-bar: true
    
    parry: "&c你招架了 #damage# 点伤害。"
    block: "&c你格挡了 #damage# 点伤害。" # Use #power# to display block power.
    dodge: "&c你闪避了 #damage# 点伤害。"
  
  block:
    cooldown: 5.0
  
  dodge:
    knockback: 1.0
    cooldown: 5
  
  parry:
    knockback: 1.0
    cooldown: 8.0
```

## `vanilla-damage-modifiers` { #vanilla-damage-modifiers }

```yaml title="config.yml · vanilla-damage-modifiers"
# 更改特定伤害来源造成的伤害。此功能
# 便于调整原版伤害来源的平衡。
# 可以为任何可用的伤害来源使用任意数学公式。
# 可用的伤害来源：https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html
# 更改在服务器重启后生效。
#
# 使用 {event_damage} 可返回事件原始伤害。
vanilla-damage-modifiers:
  enabled: false
  source:
    VOID: '%mythiclib_stat_max_health% * .05' # 造成玩家最大生命值 5% 的伤害
    FIRE: '{event_damage} * 2' # 将火焰伤害乘以 2
    WITHER: '%mythiclib_stat_max_health% * .05'
    LAVA: '%mythiclib_stat_max_health% * .2'
    DROWNING: '%mythiclib_stat_max_health% * .1'
```

## `hologram-provider` { #hologram-provider }

```yaml title="config.yml · hologram-provider"
# 可用选项：
# - TEXT_DISPLAYS (1.19.4+)
# - HOLOGRAPHIC_DISPLAYS
# - DECENT_HOLOGRAMS
# - CMI
# - HOLOGRAMS
# - TRHOLOGRAM
# - LEGACY_ARMOR_STANDS
#
# 更改在服务器重启后生效。
hologram-provider: TEXT_DISPLAYS
```

## `game-indicators` { #game-indicators }

```yaml title="config.yml · game-indicators"
# 显示游戏中的伤害或治疗数值。
# 更改在服务器重启后生效。
game-indicators:
  
  # 实体受到伤害时
  # 使用格式：'ᜌ{icon} &f{value}ᜌ'，并搭配 Wiki 中
  # 提供的资源包，即可移除灰色背景
  damage:
    enabled: true
    decimal-format: 0.#
    format: '{icon} &f{value}'
    custom-font:
      enabled: false
      normal:
        '0': ᜀ
        '1': ᜁ
        '2': ᜂ
        '3': ᜃ
        '4': ᜄ
        '5': ᜅ
        '6': ᜆ
        '7': ᜇ
        '8': ᜈ
        '9': ᜉ
        dot: ᜊ
        inter: ᜍ
      crit:
        '0': ᜐ
        '1': ᜑ
        '2': ᜒ
        '3': ᜓ
        '4': ᜔
        '5': ᜕
        '6': ᜖
        '7': ᜗
        '8': ᜘
        '9': ᜙
        dot: ᜋ
        inter: ᜍ
    icon:
      weapon:
        normal: '&c🗡'
        crit: '&c&l🗡'
      skill:
        normal: '&6★'
        crit: '&6&l★'
    split-holograms: true
    move: true
    radial-velocity: 1
    gravity: 1
    initial-upward-velocity: 1
    y-offset: 0.1
    entity-height-percent: 0.75
    r-offset: 0.5
    entity-width-percent: 0.75
    tick-period: 3
    lifespan: 20
  
  # 实体恢复生命值时
  regen:
    enabled: false
    decimal-format: 0.#
    format: '&a+#'
    custom-font:
      enabled: false
      '0': ᜀ
      '1': ᜁ
      '2': ᜂ
      '3': ᜃ
      '4': ᜄ
      '5': ᜅ
      '6': ᜆ
      '7': ᜇ
      '8': ᜈ
      '9': ᜉ
      dot: ᜊ
      inter: ᜍ
    move: true
    radial-velocity: 1
    gravity: 1
    initial-upward-velocity: 1
    y-offset: 0.1
    entity-height-percent: 0.75
    r-offset: 0.5
    entity-radius-percent: 0.75
    tick-period: 3
    lifespan: 20
```

## `damage-particles-cap` { #damage-particles-cap }

```yaml title="config.yml · damage-particles-cap"
# 限制每刻发送给玩家的伤害粒子数量。
# 默认为 10 个粒子/刻。这些粒子
# 可能相当烦人，数量过多时甚至会导致客户端崩溃。
damage-particles-cap:
  max-per-tick: 10
  enabled: false
```

## `fix-movement-speed` { #fix-movement-speed }

```yaml title="config.yml · fix-movement-speed"
# 由于 1.1.6 中对移动速度属性的改动，
# 玩家登录时，其移动速度会被重置为 .1
#
# 如果有其他插件干扰玩家移动速度，
# 请将此项设为 false
fix-movement-speed: false
```

## `fix-too-large-packets` { #fix-too-large-packets }

```yaml title="config.yml · fix-too-large-packets"
# 启用此选项后，插件会尝试修复
# 发送给客户端的数据包过大的问题。
# 配方过大且客户端
# 无法处理时，可能发生此问题。
# 更改在服务器重启后生效。
fix-too-large-packets: false
```

## `fix_reset_attribute_modifiers` { #fix_reset_attribute_modifiers }

```yaml title="config.yml · fix_reset_attribute_modifiers"
# 在 1.21 中，Minecraft 将旧修正器转换为新格式，
# 完全清除修正器 ID，仅保留修正器 UUID。此
# 改动使插件无法单独识别自身的修正器，
# 只能完全重置玩家数据中的属性修正器。
#
# 这会清除其他插件的属性修正器，不只是
# MMO 插件的修正器。随后 MMO 插件会为玩家重新应用
# 最新的属性修正器。
#
# 属性在玩家登录时重置。
#
# 重启服务器以应用更改。
fix_reset_attribute_modifiers:
  
  enabled: false
  
  # 每次需要再次重置玩家的
  # 属性修正器时，都提高此数值。
  rev_id: 1
  
  # 设为 [] 以应用
  attributes:
  - MAX_HEALTH
  - ATTACK_DAMAGE
  - MOVEMENT_SPEED
```

## `interaction_rules` { #interaction_rules }

```yaml title="config.yml · interaction_rules"
# 执行攻击或辅助操作的玩家
# 是否可以影响另一名玩家。这适用于技能、
# MI 法杖攻击及其他一些行为。
#
# 更多信息见 Wiki
# https://gitlab.com/phoenix-dvpmt/mmocore/-/wikis/Combat
interaction_rules:
  
  # 启用后，对技能、近战命中和投射物命中应用 PvP 交互规则。
  # 默认关闭此选项，以免新用户感到困惑。
  enabled: true
  
  # 禁用后，辅助技能 (增益或治疗)
  # 只能作用于玩家。
  support_skills_on_mobs: true
  
  # PvP 关闭时
  pvp_off:
    
    offense:
      self: false # PvP 关闭时对自身造成的友方伤害
    
    # PvP 关闭时是否允许治疗自己或其他玩家
    support:
      party_member: true
      party_other: true
      guild_ally: true
      guild_neutral: true
      guild_enemy: true
      self: true # 能否对自身施加增益
  
  # # PvP 开启时
  pvp_on:
    
    # PvP 开启时是否允许治疗自己或其他玩家
    support:
      party_member: true
      party_other: false
      guild_ally: true
      guild_neutral: true
      guild_enemy: false
      self: true
    
    # 公会/队伍的友军伤害
    offense:
      party_member: false
      guild_ally: false
      guild_neutral: true
      self: false # PvP 开启时对自身造成的友方伤害
```

## `damage_types` { #damage_types }

```yaml title="config.yml · damage_types"
damage_types:
  
  # 除非另有指定(由 MMOItems 物品类型或技能指定)，
  # 原版近战攻击或投射物
  # 应使用哪些伤害类型？
  #
  # 例如，使用原版武器进行的近战攻击
  # (MMOItems 武器都有自定义伤害类型)，以及
  # 使用原版弓和弩造成的伤害等。
  default:
    melee_weapon:
    - WEAPON
    - PHYSICAL
    melee_unarmed:
    - UNARMED
    - PHYSICAL
    melee_default:
    - PHYSICAL
    bow:
    - WEAPON
    - PROJECTILE
    - PHYSICAL
    skills:
    - SKILL
    - MAGIC
  
  # 将 Bukkit 的 DamageCause 映射到 MythicLib 伤害类型。
  # 例如，可以将末影龙龙息造成的
  # 伤害映射为 MAGIC 伤害类型。
  #
  # 可用的 Bukkit 伤害来源见：
  # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html
  bukkit:
    MAGIC:
    - MAGIC
    DRAGON_BREATH:
    - MAGIC
    POISON:
    - MAGIC
    - DOT
    WITHER:
    - MAGIC
    - DOT
    FIRE_TICK:
    - PHYSICAL
    - DOT
    MELTING:
    - PHYSICAL
    - DOT
    STARVATION:
    - DOT
    DRYOUT:
    - DOT
    FREEZE:
    - DOT
    FIRE:
    - PHYSICAL
    LAVA:
    - PHYSICAL
    HOT_FLOOR:
    - PHYSICAL
    SONIC_BOOM:
    - PHYSICAL
    LIGHTNING:
    - PHYSICAL
    FALL:
    - PHYSICAL
    THORNS:
    - PHYSICAL
    CONTACT:
    - PHYSICAL
    ENTITY_EXPLOSION:
    - PHYSICAL
    ENTITY_SWEEP_ATTACK:
    - PHYSICAL
    FALLING_BLOCK:
    - PHYSICAL
    FLY_INTO_WALL:
    - PHYSICAL
    BLOCK_EXPLOSION:
    - PHYSICAL
    SUFFOCATION:
    - PHYSICAL
    CRAMMING:
    - PHYSICAL
    DROWNING:
    - PHYSICAL
```
