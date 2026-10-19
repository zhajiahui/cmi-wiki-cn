---
title: item-tiers.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item-tiers.yml
source_version: 6.10.1-SNAPSHOT
---

# item-tiers.yml

文件：`item-tiers.yml`。版本：`6.10.1-SNAPSHOT`。

随包配置。

## `TRASH` { #trash }

```yaml title="item-tiers.yml · TRASH"
# 'name' 用于在物品描述中显示品质。
#
# 'deconstruct-item' 是分解物品时
# 产出物品所用的掉落表。
#
# 品质 ID(TRASH、COMMON 等)区分大小写。

TRASH:
    name: "&8&l垃圾"
    unidentification:
        range: 6
        name: "垃圾"
        prefix: '&8'
```

## `COMMON` { #common }

```yaml title="item-tiers.yml · COMMON"
    # 此品质未指定生成选项。
    # 此时会使用 config.yml 中设置的默认值
COMMON:
    name: "&7&l普通"
    parent: TRASH

    # 此品质的所有物品都会继承此提示框
    # 优先级高于物品类型专用的提示框
    # 优先级不高于单个物品专用的提示框
    # https://gitlab.com/phoenix-dvpmt/mmoitems/-/wikis/Item-Tooltips
    # 此提示框不存在
    #tooltip: COMMON

    unidentification:
        range: 6
        name: "普通"
        prefix: '&7'
```

## `UNCOMMON` { #uncommon }

```yaml title="item-tiers.yml · UNCOMMON"
    # 此品质未指定生成选项。
    # 此时会使用 config.yml 中设置的默认值
UNCOMMON:

    # 物品描述中显示的品质名称。 
    name: "&8&l罕见"

    #tooltip: UNCOMMON # 不存在
    
    # 未鉴定物品会显示物品品质。
    unidentification:
        
        # 仅适用于有等级要求的
        # 物品。此项对应所需等级
        # 所在的区间。
        range: 6
        
        # 描述中显示的品质名称。
        name: "罕见"
        
        # 未鉴定物品的名称前缀。
        prefix: '&8'
    
    item-glow:
        
        # 启用后，掉落物会显示
        # 物品提示(类似全息文字)。
        hint: true
        
        # 物品的发光颜色。 
        # https://htmlcolorcodes.com/bukkit-color-codes/
        # BLACK DARK_BLUE DARK_GREEN DARK_AQUA DARK_RED DARK_PURPLE GOLD GRAY DARK_GRAY BLUE GREEN AQUA RED LIGHT_PURPLE YELLOW WHITE
        color: 'GRAY'
    
    generation:
        chance: 0.15
        capacity:
            base: 6
            
            # 随物品等级变化
            scale: .1
            
            spread: .1
            max-spread: .3
    
    deconstruct-item:
        success:
            coef: 1
            items:
                MATERIAL:
                    UNCOMMON_WEAPON_ESSENCE: 100,1-1,0
        lose:
            coef: 2
            items:
                MATERIAL:
                    WEAPON_POWDER: 100,1-1,0
```

## `RARE` { #rare }

```yaml title="item-tiers.yml · RARE"
RARE:
    name: "&6&l稀有"
    unidentification:
        name: "稀有"
        range: 6
        prefix: '&6'
    #tooltip: RARE # 不存在
    generation:
        chance: 0.06
        capacity:
            base: 9
            scale: .15
            spread: .1
            max-spread: .3
    deconstruct-item:
        success:
            coef: 1
            items:
                MATERIAL:
                    RARE_WEAPON_ESSENCE: 100,1-1,0
        lose:
            coef: 3
            items:
                MATERIAL:
                    WEAPON_POWDER: 100,1-1,0
```

## `VERY_RARE` { #very_rare }

```yaml title="item-tiers.yml · VERY_RARE"
VERY_RARE:
    name: "&e&l极稀有"
    unidentification:
        name: "极稀有"
        prefix: '&e'
        range: 6
    #tooltip: VERY_RARE # 不存在
    deconstruct-item:
        success:
            coef: 1
            items:
                MATERIAL:
                    VERY_RARE_WEAPON_ESSENCE: 100,1-1,0
        lose:
            coef: 3
            items:
                MATERIAL:
                    WEAPON_POWDER: 100,1-1,0
    generation:
        chance: 0.03
        capacity:
            base: 10
            scale: .17
            spread: .1
            max-spread: .3
```

## `LEGENDARY` { #legendary }

```yaml title="item-tiers.yml · LEGENDARY"
LEGENDARY:
    name: "&b&l传说"
    unidentification:
        name: "传说"
        prefix: '&b'
        range: 6
    #tooltip: LEGENDARY # 不存在
    deconstruct-item:
        success:
            coef: 1
            items:
                MATERIAL:
                    LEGENDARY_WEAPON_ESSENCE: 100,1-1,0
        lose:
            coef: 4
            items:
                MATERIAL:
                    WEAPON_POWDER: 100,1-1,0
    generation:
        chance: 0.01
        capacity:
            base: 12
            scale: .2
            spread: .1
            max-spread: .3
```

## `MYTHICAL` { #mythical }

```yaml title="item-tiers.yml · MYTHICAL"
MYTHICAL:
    name: "&5&l神话"
    unidentification:
        name: "神话"
        prefix: '&5'
        range: 6
    generation:
        chance: 0.003
        capacity:
            base: 15
            scale: .3
            spread: .1
            max-spread: .3
    deconstruct-item:
        success:
            coef: 1
            items:
                MATERIAL:
                    MYTHICAL_WEAPON_ESSENCE: 100,1-1,0
        lose:
            coef: 5
            items:
                MATERIAL:
                    WEAPON_POWDER: 100,1-1,0
```

## `EPIC` { #epic }

```yaml title="item-tiers.yml · EPIC"
EPIC:
    name: "&4&l史诗"
    unidentification:
        name: "史诗"
        prefix: '&4'
        range: 6
    deconstruct-item:
        success:
            coef: 1
            items:
                MATERIAL:
                    EPIC_WEAPON_ESSENCE: 100,1-1,0
        lose:
            coef: 6
            items:
                MATERIAL:
                    WEAPON_POWDER: 100,1-1,0
```

## `MAGICAL` { #magical }

```yaml title="item-tiers.yml · MAGICAL"
    # 此品质未指定生成选项。
    # 此时会使用 config.yml 中设置的默认值
MAGICAL:
    name: "&2&l魔法"
    unidentification:
        name: "魔法"
        prefix: '&2'
        range: 6
    deconstruct-item:
        success:
            coef: 1
            items:
                MATERIAL:
                    MAGICAL_WEAPON_ESSENCE: 100,1-1,0
        lose:
            coef: 3
            items:
                MATERIAL:
                    WEAPON_POWDER: 100,1-1,0
```

## `UNIQUE` { #unique }

```yaml title="item-tiers.yml · UNIQUE"
    # 此品质未指定生成选项。
    # 此时会使用 config.yml 中设置的默认值
UNIQUE:
    name: "&c&l独特"
    unidentification:
        name: "独特"
        prefix: '&c'
        range: 6
    deconstruct-item:
        success:
            coef: 1
            items:
                MATERIAL:
                    UNIQUE_WEAPON_ESSENCE: 100,1-1,0
        lose:
            coef: 9
            items:
                MATERIAL:
                    WEAPON_POWDER: 100,1-1,0
    # 此品质未指定生成选项。
    # 此时会使用 config.yml 中设置的默认值
```
