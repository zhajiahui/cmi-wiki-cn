---
title: item-types.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item-types.yml
source_version: 6.10.1-SNAPSHOT
---

# item-types.yml

文件：`item-types.yml`。版本：`6.10.1-SNAPSHOT`。

随包配置。

## `SWORD` { #sword }

```yaml title="item-types.yml · SWORD"
##########################################################
# 默认物品类型
#
# 这些类型不可移除。可以将它们用作 "parents"，
# 创建与其他物品类型
# 行为相同的新物品类型
##########################################################

# 执行 /mmoitems 命令时使用的引用名称
SWORD:

    # display 参数用于在物品浏览器和
    # 潜行点击工作台时显示的配方列表中
    # 显示物品。可以使用耐久度实现自定义材质。
    # 在 1.14 中，耐久度由 CustomModelData 取代。
    display: IRON_SWORD:0

    # 物品描述中显示的名称。
    name: "剑"

    # 是否在物品浏览器中显示此类型？
    hide-in-game: false

    # 未鉴定物品的模板。
    unident-item:

        #item: DIAMOND_SWORD                  # 如有需要，可以在此覆盖物品类型
        #custom_model_data_float: 0.45        # 1.20.4+ 浮点数形式的自定义模型数据。此选项与上方的字符串选项均可使用
        #custom_model_data: 0                 # 1.14-1.20.3 自定义模型数据。1.20.4+ 建议使用 custom_model_data_string
        #tooltip: 'myplugin:tooltip_asset_id' # 可以用此方式编辑槽位图标的提示框
        #custom_model_data_string: 'test'     # 1.20.4+ 字符串形式的自定义模型数据
        #item_model: 'minecraft:dirt'         # 1.21.2+ 物品模型
        #skull_texture: '......'              # 头颅纹理值或 URL
        #hide_tooltip: false                  # True 或 false，用于原版提示框
        #unbreakable: false                   # 是否无法破坏？
        #fake_attribute: false                # 是否让 MythicLib 添加一个虚拟属性修正器？可用于在 1.20 或更低版本中隐藏物品的原版属性
        #item_flags: [HIDE_ENCHANTS, ....]    # 为物品添加物品标志。https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/inventory/ItemFlag.html

        name: "&f#prefix#未鉴定的剑"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    # 此物品类型的行为
    on-attack: slashing_attack_effect

    # 此类型的所有物品都会继承此提示框
    # 其优先级不高于单个物品或品质专用的提示框
    # https://gitlab.com/phoenix-dvpmt/mmoitems/-/wikis/Item-Tooltips
    # 此提示框不存在
    #tooltip: COMMON

    # 使用此类型物品攻击时造成的伤害类型
    attack-damage-types: [ WEAPON, PHYSICAL ]
```

## `DAGGER` { #dagger }

```yaml title="item-types.yml · DAGGER"
DAGGER:
    display: STONE_SWORD
    name: "匕首"
    unident-item:
        name: "&f#prefix#未鉴定的匕首"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: piercing_attack_effect
    attack-damage-types: [ WEAPON, PHYSICAL ]
```

## `SPEAR` { #spear }

```yaml title="item-types.yml · SPEAR"
SPEAR:
    display: TRIDENT
    name: "矛"
    unident-item:
        name: "&f#prefix#未鉴定的矛"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: piercing_attack_effect
    attack-damage-types: [ WEAPON, PHYSICAL ]
```

## `HAMMER` { #hammer }

```yaml title="item-types.yml · HAMMER"
HAMMER:
    display: IRON_AXE
    name: "锤"
    unident-item:
        name: "&f#prefix#未鉴定的锤"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: blunt_attack_effect
    attack-damage-types: [ WEAPON, PHYSICAL ]
```

## `GAUNTLET` { #gauntlet }

```yaml title="item-types.yml · GAUNTLET"
GAUNTLET:
    display: IRON_SHOVEL
    name: "拳套"
    unident-item:
        name: "&f#prefix#未鉴定的拳套"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: blunt_attack_effect
    on-entity-interact: gauntlet_special_attack
    attack-damage-types: [ WEAPON, PHYSICAL ]
```

## `WHIP` { #whip }

```yaml title="item-types.yml · WHIP"
WHIP:
    display: LEAD
    name: "鞭子"
    unident-item:
        name: "&f#prefix#未鉴定的鞭子"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    disable-melee-attacks: true
    on-left-click: whip_attack
    on-attack: slashing_attack_effect
```

## `STAFF` { #staff }

```yaml title="item-types.yml · STAFF"
    # 此项不会生效，因为此物品类型使用 'on-left-click' 攻击效果：
    #attack-damage-types: [ WEAPON, PROJECTILE ]
    # 要更改伤害类型，需要编辑名为 'whip_attack' 的脚本。
    # 默认情况下，此脚本位于 'MythicLib/script/mmoitems_scripts.yml' 中。

STAFF:
    display: DIAMOND_HOE
    name: "法杖"
    unident-item:
        name: "&f#prefix#未鉴定的法杖"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    disable-melee-attacks: true
    on-left-click: staff_default # 左键使用法杖时执行的操作
    attack-cooldown-key: "staff"
    on-entity-interact: staff_special_attack # 右键点击实体时执行的特殊操作
```

## `BOW` { #bow }

```yaml title="item-types.yml · BOW"
    # 此项不会生效，因为此物品类型使用 'on-left-click' 攻击效果：
    #attack-damage-types: [ WEAPON, PROJECTILE ]
    # 要更改伤害类型，需要编辑名为 'staff_default' 的脚本。
    # 默认情况下，此脚本位于 'MythicLib/script/mmoitems_scripts.yml' 中。

BOW:
    display: BOW
    name: "弓"
    unident-item:
        name: "&f#prefix#未鉴定的弓"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    disable-melee-attacks: true
    # 此类型物品发射的投射物造成的伤害类型
    attack-damage-types: [ WEAPON, PROJECTILE ]
```

## `CROSSBOW` { #crossbow }

```yaml title="item-types.yml · CROSSBOW"
CROSSBOW:
    display: WOODEN_PICKAXE
    name: "弩"
    unident-item:
        name: "&f#prefix#未鉴定的弩"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    # 此项不会生效，因为此物品类型使用 'on-right-click' 攻击效果：
    #attack-damage-types: [ WEAPON, PROJECTILE ]
    # 要更改伤害类型，需要编辑名为 'crossbow_attack' 的脚本。
    # 默认情况下，此脚本位于 'MythicLib/script/mmoitems_scripts.yml' 中。

    disable-melee-attacks: true
    on-right-click: crossbow_attack
```

## `MUSKET` { #musket }

```yaml title="item-types.yml · MUSKET"
MUSKET:
    display: IRON_HORSE_ARMOR
    name: "火枪"
    unident-item:
        name: "&f#prefix#未鉴定的火枪"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    disable-melee-attacks: true
```

## `LUTE` { #lute }

```yaml title="item-types.yml · LUTE"
    # 鲁特琴和火枪的攻击效果截至
    # MI 6.10 已被硬编码，目前无法修改。

LUTE:
    display: NAME_TAG
    name: "鲁特琴"
    unident-item:
        name: "&f#prefix#未鉴定的鲁特琴"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    disable-melee-attacks: true
```

## `CATALYST` { #catalyst }

```yaml title="item-types.yml · CATALYST"
    # 鲁特琴和火枪的攻击效果截至
    # MI 6.10 已被硬编码，目前无法修改。

# 在双手中均应用属性
CATALYST:
    display: PRISMARINE_SHARD
    name: "触媒"
    unident-item:
        name: "&f#prefix#未鉴定的触媒"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `OFF_CATALYST` { #off_catalyst }

```yaml title="item-types.yml · OFF_CATALYST"
# 仅在副手中应用属性
OFF_CATALYST:
    display: PRISMARINE_CRYSTALS
    name: "触媒 (副手)"
    unident-item:
        name: "&f#prefix#未鉴定的触媒"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `MAIN_CATALYST` { #main_catalyst }

```yaml title="item-types.yml · MAIN_CATALYST"
# 仅在主手中应用属性
MAIN_CATALYST:
    display: PRISMARINE_CRYSTALS
    name: "触媒 (主手)"
    unident-item:
        name: "&f#prefix#未鉴定的触媒"
        lore:
            - "&7这件物品尚未鉴定。我必须"
            - "&7找到鉴定它的方法！"
            - '{tier}'
            - "{tier}&8物品信息："
            - "{range}&8- &7等级范围：&e#range#"
            - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `ORNAMENT` { #ornament }

```yaml title="item-types.yml · ORNAMENT"
ORNAMENT:
    display: GOLD_NUGGET
    name: "饰物"
    unident-item:
        name: "&f#prefix#未鉴定的饰物"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `ACCESSORY` { #accessory }

```yaml title="item-types.yml · ACCESSORY"
ACCESSORY:
    display: DIAMOND
    name: "饰品"
    unident-item:
        name: "&f#prefix#未鉴定的饰品"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `ARMOR` { #armor }

```yaml title="item-types.yml · ARMOR"
ARMOR:
    display: IRON_CHESTPLATE
    name: "盔甲"
    unident-item:
        name: "&f#prefix#未鉴定的盔甲"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `TOOL` { #tool }

```yaml title="item-types.yml · TOOL"
TOOL:
    display: IRON_PICKAXE
    name: "工具"
    unident-item:
        name: "&f#prefix#未鉴定的工具"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `CONSUMABLE` { #consumable }

```yaml title="item-types.yml · CONSUMABLE"
CONSUMABLE:
    display: APPLE
    name: "消耗品"
    unident-item:
        name: "&f#prefix#未鉴定的消耗品"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `MISCELLANEOUS` { #miscellaneous }

```yaml title="item-types.yml · MISCELLANEOUS"
MISCELLANEOUS:
    display: WATER_BUCKET
    name: "杂项"
    unident-item:
        name: "&f#prefix#未鉴定的杂项物品"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `SKIN` { #skin }

```yaml title="item-types.yml · SKIN"
SKIN:
    display: LEATHER
    name: "皮肤"
    unident-item:
        name: "&f#prefix#未鉴定的皮肤物品"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `GEM_STONE` { #gem_stone }

```yaml title="item-types.yml · GEM_STONE"
GEM_STONE:
    display: EMERALD
    name: "宝石"
    unident-item:
        name: "&f#prefix#未鉴定的宝石"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `BLOCK` { #block }

```yaml title="item-types.yml · BLOCK"
BLOCK:
    display: STONE:0
    name: "方块"
    unident-item:
        name: "&f#prefix#未鉴定的方块"
        lore:
            - "&7这件物品尚未鉴定。我必须"
            - "&7找到鉴定它的方法！"
            - '{tier}'
            - "{tier}&8物品信息："
            - "{range}&8- &7等级范围：&e#range#"
            - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `GREATSWORD` { #greatsword }

```yaml title="item-types.yml · GREATSWORD"
##########################################################
# 默认物品子类型
##########################################################

GREATSWORD:
    display: DIAMOND_SWORD
    name: "巨剑"
    parent: 'SWORD'
    unident-item:
        name: "&f#prefix#未鉴定的巨剑"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: slashing_attack_effect
```

## `LONG_SWORD` { #long_sword }

```yaml title="item-types.yml · LONG_SWORD"
LONG_SWORD:
    display: STONE_SWORD
    name: "长剑"
    parent: 'SWORD'
    unident-item:
        name: "&f#prefix#未鉴定的长剑"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: slashing_attack_effect
```

## `KATANA` { #katana }

```yaml title="item-types.yml · KATANA"
KATANA:
    display: IRON_SWORD
    name: "武士刀"
    parent: 'SWORD'
    unident-item:
        name: "&f#prefix#未鉴定的武士刀"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: slashing_attack_effect
```

## `THRUSTING_SWORD` { #thrusting_sword }

```yaml title="item-types.yml · THRUSTING_SWORD"
THRUSTING_SWORD:
    display: GOLDEN_SWORD
    name: "刺剑"
    parent: 'DAGGER'
    unident-item:
        name: "&f#prefix#未鉴定的刺击匕首"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: piercing_attack_effect
```

## `AXE` { #axe }

```yaml title="item-types.yml · AXE"
AXE:
    display: STONE_AXE
    name: "斧"
    parent: 'SWORD'
    unident-item:
        name: "&f#prefix#未鉴定的斧"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: slashing_attack_effect
```

## `GREATAXE` { #greataxe }

```yaml title="item-types.yml · GREATAXE"
GREATAXE:
    display: DIAMOND_AXE
    name: "巨斧"
    parent: 'SWORD'
    unident-item:
        name: "&f#prefix#未鉴定的巨斧"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: slashing_attack_effect
```

## `HALBERD` { #halberd }

```yaml title="item-types.yml · HALBERD"
HALBERD:
    display: IRON_AXE
    name: "戟"
    parent: 'SWORD'
    unident-item:
        name: "&f#prefix#未鉴定的戟"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: blunt_attack_effect
```

## `LANCE` { #lance }

```yaml title="item-types.yml · LANCE"
LANCE:
    display: STICK
    name: "骑枪"
    parent: 'SPEAR'
    unident-item:
        name: "&f#prefix#未鉴定的骑枪"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: piercing_attack_effect
```

## `GREATHAMMER` { #greathammer }

```yaml title="item-types.yml · GREATHAMMER"
GREATHAMMER:
    display: DIAMOND_AXE
    name: "巨锤"
    parent: 'HAMMER'
    unident-item:
        name: "&f#prefix#未鉴定的巨锤"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: blunt_attack_effect
```

## `GREATSTAFF` { #greatstaff }

```yaml title="item-types.yml · GREATSTAFF"
GREATSTAFF:
    display: DIAMOND_HOE
    name: "巨杖"
    parent: 'HAMMER'
    unident-item:
        name: "&f#prefix#未鉴定的巨杖"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: blunt_attack_effect
```

## `STAVE` { #stave }

```yaml title="item-types.yml · STAVE"
STAVE:
    display: IRON_HOE
    name: "杖"
    parent: 'HAMMER'
    unident-item:
        name: "&f#prefix#未鉴定的杖"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    on-attack: blunt_attack_effect
```

## `TOME` { #tome }

```yaml title="item-types.yml · TOME"
TOME:
    display: BOOK
    name: "魔法书"
    parent: 'CATALYST'
    unident-item:
        name: "&f#prefix#未鉴定的魔法书"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `TALISMAN` { #talisman }

```yaml title="item-types.yml · TALISMAN"
TALISMAN:
    display: TOTEM_OF_UNDYING
    name: "护符"
    parent: 'CATALYST'
    unident-item:
        name: "&f#prefix#未鉴定的护符"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `WAND` { #wand }

```yaml title="item-types.yml · WAND"
WAND:
    display: STICK
    name: "魔杖"
    parent: 'STAFF'
    unident-item:
        name: "&f#prefix#未鉴定的魔杖"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    disable-melee-attacks: true
    on-left-click: staff_default
    attack-cooldown-key: "staff"
    on-entity-interact: staff_special_attack # 右键点击实体时执行的特殊操作
```

## `GREATBOW` { #greatbow }

```yaml title="item-types.yml · GREATBOW"
GREATBOW:
    display: BOW
    name: "巨弓"
    parent: 'BOW'
    unident-item:
        name: "&f#prefix#未鉴定的巨弓"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"

    disable-melee-attacks: true
```

## `SHIELD` { #shield }

```yaml title="item-types.yml · SHIELD"
SHIELD:
    display: SHIELD
    name: "盾牌"
    parent: CATALYST
    unident-item:
        name: "&f#prefix#未鉴定的盾牌"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `MATERIAL` { #material }

```yaml title="item-types.yml · MATERIAL"
MATERIAL:
    display: PAPER
    name: "材料"
    parent: 'MISCELLANEOUS'
    unident-item:
        name: "&f#prefix#未鉴定的材料"
        lore:
        - "&7这件物品尚未鉴定。我必须"
        - "&7找到鉴定它的方法！"
        - '{tier}'
        - "{tier}&8物品信息："
        - "{range}&8- &7等级范围：&e#range#"
        - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `RING` { #ring }

```yaml title="item-types.yml · RING"
##########################################################
# MMOInventory 类型
##########################################################

RING:
    display: EMERALD
    name: "戒指"
    parent: 'ACCESSORY'
    unident-item:
        name: "&f#prefix#未鉴定的戒指"
        lore:
            - "&7这件物品尚未鉴定。我必须"
            - "&7找到鉴定它的方法！"
            - '{tier}'
            - "{tier}&8物品信息："
            - "{range}&8- &7等级范围：&e#range#"
            - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `AMULET` { #amulet }

```yaml title="item-types.yml · AMULET"
AMULET:
    display: EMERALD
    name: "项链"
    parent: 'ACCESSORY'
    unident-item:
        name: "&f#prefix#未鉴定的项链"
        lore:
            - "&7这件物品尚未鉴定。我必须"
            - "&7找到鉴定它的方法！"
            - '{tier}'
            - "{tier}&8物品信息："
            - "{range}&8- &7等级范围：&e#range#"
            - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `BRACELET` { #bracelet }

```yaml title="item-types.yml · BRACELET"
BRACELET:
    display: EMERALD
    name: "手镯"
    parent: 'ACCESSORY'
    unident-item:
        name: "&f#prefix#未鉴定的手镯"
        lore:
            - "&7这件物品尚未鉴定。我必须"
            - "&7找到鉴定它的方法！"
            - '{tier}'
            - "{tier}&8物品信息："
            - "{range}&8- &7等级范围：&e#range#"
            - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `GLOVES` { #gloves }

```yaml title="item-types.yml · GLOVES"
GLOVES:
    display: EMERALD
    name: "手套"
    parent: 'ACCESSORY'
    unident-item:
        name: "&f#prefix#未鉴定的手套"
        lore:
            - "&7这件物品尚未鉴定。我必须"
            - "&7找到鉴定它的方法！"
            - '{tier}'
            - "{tier}&8物品信息："
            - "{range}&8- &7等级范围：&e#range#"
            - "{tier}&8- &7物品品质：#prefix##tier#"
```

## `ARTIFACT` { #artifact }

```yaml title="item-types.yml · ARTIFACT"
ARTIFACT:
    display: EMERALD
    name: "圣物"
    parent: 'ACCESSORY'
    unident-item:
        name: "&f#prefix#未鉴定的圣物"
        lore:
            - "&7这件物品尚未鉴定。我必须"
            - "&7找到鉴定它的方法！"
            - '{tier}'
            - "{tier}&8物品信息："
            - "{range}&8- &7等级范围：&e#range#"
            - "{tier}&8- &7物品品质：#prefix##tier#"
```
