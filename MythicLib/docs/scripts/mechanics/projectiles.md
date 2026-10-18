---
title: 投射物
source: https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/projectiles
source_snapshot: '2026-10-19'
---

# 投射物 {#🏹-projectiles}

## 射箭 {#shoot-arrow}

使用此机制让技能施法者发射箭。

|参数|别名 |描述 |默认 |
| --- | --- | --- | --- |
| from_item | - | 当true、MMOItems会考虑弓属性的暴击，攻击伤害... | false |
| player_attack_damage | - | 是否使用玩家的攻击伤害基础属性作为箭头的基础伤害。 | false |
| velocity | vel, speed, sp | 箭头速度的乘数。 | 1.0 |
| hit | - | 当箭头击中实体或块时调用脚本。 | - |
| land | - | 当箭落在地面上但没有击中任何物体时调用脚本。 | - |
| tick | - | 脚本在箭头飞行时调用每个刻。 | - |
| damage_types | - | Comma-separated适用于箭头的伤害类型列表。 | `*` |

`*`默认伤害类型是MythicLib配置文件中为弓箭攻击提供的伤害类型。

MMOItems使用以下脚本来处理来自 *Crossbow*武器类型的攻击。它确保仅在不处于创造模式或箭头具有`MMOITEMS_DISABLE_ARROW_CONSUMPTION`标签时才消耗箭头。它还在玩家的`arrow_velocity`属性的基础上使箭射得更快，并为飞行的箭添加了粒子效果。

```yml
crossbow_attack:
  public: true
  conditions:
    - 'ammo{item=ARROW;creative_infinite=true;item_ignore_tag=MMOITEMS_DISABLE_ARROW_CONSUMPTION}'
  mechanics:
    - 'take_ammo{item=ARROW;creative_infinite=true;item_ignore_tag=MMOITEMS_DISABLE_ARROW_CONSUMPTION}'
    - 'play_sound{sound=ENTITY_ARROW_SHOOT;pitch=.5}'
    - 'shoot_arrow{from_item=true;player_attack_damage=true;tick=crossbow_arrow_tick;velocity="non_zero(<stat.arrow_velocity>, 1) * 3"}'

crossbow_arrow_tick:
  mechanics:
    - 'particle{particle=CRIT;speed=.05}'
```

## 潜影贝导弹 {#shulker-bullet}

使用此机制让技能施法者发射潜影贝导弹。

| Parameter | Alias | 描述 | Default |
| --- | --- | --- | --- |
| life_span | lifetime, l, ticks, duration, dur, d | 潜影贝导弹的寿命（以刻为单位）。 | 60 |
| hit_entity | - | 当潜影贝导弹击中实体时调用的脚本。 | - |

```yml
shoot_shulker_bullet:
  mechanics:
    - 'shoot_shulker_bullet{life_span=100;hit_entity=shulker_bullet_hit}'

shulker_bullet_hit:
  mechanics:
    - 'damage{dmg=10}'
```

---

原文：[🏹 Projectiles](https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/projectiles) · 原文归档：2026-10-19
