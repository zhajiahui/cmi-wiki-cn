---
title: item-sets.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item-sets.yml
source_version: 6.10.1-SNAPSHOT
---

# item-sets.yml

文件：`item-sets.yml`。版本：`6.10.1-SNAPSHOT`。

随包配置。

## `ARCANE` { #arcane }

```yaml title="item-sets.yml · ARCANE"
# 物品套装可将不同的自定义物品关联起来。
# 玩家穿戴同一套装中的多件物品后，可以获得
# 套装加成，从而鼓励玩家使用同类物品。
# 这套系统很适合 RPG 物品。
#
# 也可以将药水效果用作套装加成，例如
# - "potion-speed: 2" 提供永久的速度 II
# - "potion-increase_damage: 3" 提供永久的力量 III
# https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html
#
# 还可以将技能用作集齐套装后的加成。技能 ID
# 必须以 'ability-' 开头，但仅用作引用。
# 可以像往常一样配置技能的施放模式、类型和修正器。


ARCANE:
    name: "&2奥术套装"
    bonuses:
        '3':
            magic-damage: 20
        '4':
            max-mana: 30
            potion-speed: 1
    lore-tag:
    - "&7奥术套装加成："
    - "&8[3] +20% 魔法伤害"
    - "&8[4] 30 最大魔力"
    - "&8[4] 永久速度 I"
```

## `STEEL` { #steel }

```yaml title="item-sets.yml · STEEL"
STEEL:
    name: "&8钢铁套装"
    bonuses:
        '3':
            damage-reduction: 5
        '4':
            damage-reduction: 5
    lore-tag:
    - "&7钢铁套装加成："
    - "&8[3] +5% 伤害减免"
    - "&8[4] +10% 伤害减免"
```

## `GINGERBREAD` { #gingerbread }

```yaml title="item-sets.yml · GINGERBREAD"
GINGERBREAD:
    name: "&c姜饼套装"
    bonuses:
        '4':
            damage-reduction: 6
            potion-jump: 3
    lore-tag:
    - "&7姜饼套装加成："
    - "&8[4] +5% 伤害减免"
    - "&8[4] 永久跳跃提升 III"
```

## `DRAGON` { #dragon }

```yaml title="item-sets.yml · DRAGON"
DRAGON:
    name: "&5巨龙套装"
    bonuses:
        '4':
            ability-1:
                type: MAGICAL_SHIELD
                cooldown: 10
                duration: 5
                power: 60
                radius: 5
                mode: WHEN_HIT
    lore-tag:
        - "&3巨龙整套加成："
        - "&7敌人攻击你时，你身上会出现一道&b魔法"
        - "&b护盾&7，在接下来的"
        - "&7使你免受 &c60%&7 的所有伤害，持续"
        - "&c5s&7。&7&o冷却时间为 10s。"
```

## `PSYCHIC` { #psychic }

```yaml title="item-sets.yml · PSYCHIC"
PSYCHIC:
    name: "&d灵能"
    bonuses:
        '2':
            ability-1:
                type: TELEKINESY
                duration: 8.0
                cooldown: 12.0
                knockback: 2.0
                mode: RIGHT_CLICK
            ability-2:
                type: BLINK
                cooldown: 8.0
                range: 60
                mode: SHIFT_RIGHT_CLICK
    lore-tag:
        - "&d灵能："
        - "&7装备&d控制装置&7并"
        - "&7手持&f轻薄透明手套&7时，"
        - "&7可以对实体使用念力，"
        - "&7通过&3右键点击&7施展；也可通过"
        - "&7通过&3潜行右键点击&7传送到正看着的方块。"
        - "&8&o真是的……"
```

## `UNDEADSLAYER` { #undeadslayer }

```yaml title="item-sets.yml · UNDEADSLAYER"
UNDEADSLAYER:
    name: "&4&l&k||| &4> &c&l亡灵杀手套装"
    bonuses:
        '4':
            pve-damage: 10
        '5':
            undead-damage: 15
    lore-tag:
        - "&4&l&k||| &4> &c&l亡灵杀手套装"
        - "&7完整的&c盔甲套装&7提供 &c+10%&7 PvE 伤害。"
        - "&7使用&c亡灵杀手&7武器时额外获得"
        - "&c+15% &7对亡灵伤害。"
```

## `SPELLCASTER` { #spellcaster }

```yaml title="item-sets.yml · SPELLCASTER"
SPELLCASTER:
    name: "&d施法者套装"
    bonuses:
        '3':
            max-mana: 10
        '4':
            magic-damage: 25
        '5' :
            potion-speed: 1
    lore-tag:
        - "&d施法者套装加成："
        - "&3[3] +10 最大魔力"
        - "&3[4] +25% 魔法伤害"
        - "&3如果手持施法者魔杖&7，"
        - "&7&b获得永久速度 I&7。"
```

## `OMNIELEMENTAL` { #omnielemental }

```yaml title="item-sets.yml · OMNIELEMENTAL"
OMNIELEMENTAL:
    name: "&e全元素套装"
    bonuses:
        '4':
            water-defense: 100
            fire-defense: 100
            wind-defense: 100
            earth-defense: 100
        '5':
            ice-defense: 100
            thunder-defense: 100
        '6':
            lightness-defense: 100
            darkness-defense: 100
    lore-tag:
        - "&e全元素套装加成："
        - "&7[4] 使你免受&c火&7、&3水&7、风和&2土的伤害。"
        - "&7[5] 还会使你免受&b冰&7和&e雷&7的伤害。"
        - "&7[6] 使你免受&f光明&7和&8黑暗&7的伤害。"
```

## `HATRED` { #hatred }

```yaml title="item-sets.yml · HATRED"
# 默认不使用
HATRED:
    name: "&c憎恨套装"
    bonuses:
        '2':
            damage-reduction: 6
            ability-1:
                type: LIFE_ENDER
                cooldown: 30
                mode: ATTACK
    lore-tag:
        - "&7憎恨套装加成："
        - "&8[2] -6% 受到的伤害"
        - "&8[2] 命中时召唤毁灭性的火焰陨石。"
```
