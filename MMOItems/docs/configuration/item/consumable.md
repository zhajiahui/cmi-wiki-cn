---
title: item/consumable.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: item/consumable.yml
source_version: 6.10.1-SNAPSHOT
---

# item/consumable.yml

文件：`item/consumable.yml`。版本：`6.10.1-SNAPSHOT`。

随包物品或内容配置。

## `SANDWITCH` { #sandwitch }

```yaml title="item/consumable.yml · SANDWITCH"
SANDWITCH:
  base:
    material: BREAD
    name: "&c沙&6三明治"
    effects:
      POISON:
        duration: 10
        amplifier: 2
    lore:
      - "&7你真有这么饿吗？！"
    item-cooldown: 15
    restore-food: 5.0
```

## `A_BIG_CARROT` { #a_big_carrot }

```yaml title="item/consumable.yml · A_BIG_CARROT"
A_BIG_CARROT:
  base:
    material: CARROT
    lore:
      - "&7&o总会剩下些胡萝卜"
    disable-right-click-consume: true
    vanilla-eating: true
    restore-food: 1.0
```

## `ROCK` { #rock }

```yaml title="item/consumable.yml · ROCK"
ROCK:
  base:
    material: COBBLESTONE
    name: "&f石头"
    lore:
      - "&7可以用来磨利武器，"
      - "&7或&n伤害&7敌人。"
    tier: TRASH
    item-cooldown: 3
    repair: 3.0
    ability:
      right-click:
        type: ITEM_THROW
        mode: RIGHT_CLICK
        damage: 2.0
        cooldown: 3
```

## `SCROLL_OF_IDENTIFICATION` { #scroll_of_identification }

```yaml title="item/consumable.yml · SCROLL_OF_IDENTIFICATION"
SCROLL_OF_IDENTIFICATION:
  base:
    material: PAPER
    name: "&f鉴定卷轴"
    tier: UNCOMMON
    can-identify: true
    crafting:
      shaped:
        '1':
          - AIR AIR AIR
          - PAPER DIAMOND PAPER
          - AIR AIR AIR
    inedible: true
```

## `ITEM_CRUSHER` { #item_crusher }

```yaml title="item/consumable.yml · ITEM_CRUSHER"
ITEM_CRUSHER:
  base:
    material: IRON_AXE
    required-level: 3.0
    can-deconstruct: true
    name: "&f&l物品粉碎器"
```

## `RECALL_POTION` { #recall_potion }

```yaml title="item/consumable.yml · RECALL_POTION"
RECALL_POTION:
  base:
    material: POTION
    hide-potion-effects: true
    name: "&9回城药水"
    lore:
      - "&7带你回家。"
    potion-color: 100 100 255
    commands:
      '1':
        format: spawn
    item-cooldown: 60.0
```

## `FIREBALL_SCROLL` { #fireball_scroll }

```yaml title="item/consumable.yml · FIREBALL_SCROLL"
FIREBALL_SCROLL:
  base:
    material: PAPER
    item-cooldown: 30.0
    required-level: 15.0
    tier: MAGICAL
    ability:
      right-click:
        type: FIREBOLT
        mode: RIGHT_CLICK
        damage: 5.0
        cooldown: 0.0
        ignite: 3.0
    name: "&c火球卷轴 I"
```

## `FIREBALL_SCROLL_II` { #fireball_scroll_ii }

```yaml title="item/consumable.yml · FIREBALL_SCROLL_II"
FIREBALL_SCROLL_II:
  base:
    material: PAPER
    item-cooldown: 25.0
    required-level: 17
    tier: MAGICAL
    ability:
      right-click:
        type: FIREBOLT
        mode: RIGHT_CLICK
        damage: 10.0
        cooldown: 0.0
        ignite: 5.0
    name: "&c火球卷轴 II"
```

## `FIREBALL_SCROLL_III` { #fireball_scroll_iii }

```yaml title="item/consumable.yml · FIREBALL_SCROLL_III"
FIREBALL_SCROLL_III:
  base:
    material: PAPER
    item-cooldown: 20.0
    required-level: 20.0
    tier: MAGICAL
    ability:
      right-click:
        type: FIREBOLT
        mode: RIGHT_CLICK
        damage: 15.0
        cooldown: 0.0
        ignite: 7.0
    name: "&c火球卷轴 III"
```

## `APPLE_OF_DISCORD` { #apple_of_discord }

```yaml title="item/consumable.yml · APPLE_OF_DISCORD"
APPLE_OF_DISCORD:
  base:
    material: GOLDEN_APPLE
    durability: 1.0
    name: "&6[ 纷争金苹果 ]"
    required-level: 4.0
    item-cooldown: 50.0
    effects:
      ABSORPTION:
        duration: 40
        amplifier: 2
      REGENERATION:
        duration: 40
        amplifier: 2
      SPEED:
        duration: 40
        amplifier: 2
    restore-health: 1.0
    restore-food: 15.0
    restore-saturation: 1.0
```

## `SHARP_FLINT` { #sharp_flint }

```yaml title="item/consumable.yml · SHARP_FLINT"
SHARP_FLINT:
  base:
    material: FLINT
    name: "&f锋利燧石"
    tier: COMMON
    repair: 20.0
```

## `DEATH_STEW` { #death_stew }

```yaml title="item/consumable.yml · DEATH_STEW"
DEATH_STEW:
  base:
    material: MUSHROOM_STEW
    name: "&f死亡浓汤"
    lore:
      - "&8&o你可别喝那东西……"
    tier: UNIQUE
    effects:
      HARM:
        duration: 1
        amplifier: 100
```

## `KARTOFFELSALAT` { #kartoffelsalat }

```yaml title="item/consumable.yml · KARTOFFELSALAT"
KARTOFFELSALAT:
  base:
    material: RABBIT_STEW
    name: "&9土豆沙拉"
    tier: COMMON
    restore-stamina: 10.0
    item-cooldown: 30.0
    lore:
      - "&7味道很冲，却很难吃完。"
    restore-food: 3.0
    restore-saturation: 10.0
```

## `LARGE_HEALTH_POTION` { #large_health_potion }

```yaml title="item/consumable.yml · LARGE_HEALTH_POTION"
LARGE_HEALTH_POTION:
  base:
    material: PLAYER_HEAD
    skull-texture:
      value: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTFlN2ViMmU0NjFlOTZlNjMxY2JhMGMwY2RhYTU0NDg4MDYzMDJlZGFlOTFiNjFkYWZjMjgxYWU1ODRkOCJ9fX0=
      uuid: 701aa558-c1b0-4eb7-81e4-79b1af25283c
    name: "&f大型生命药水"
    item-cooldown: 10.0
    sounds:
      on-consume: entity.generic.drink
    restore-health: 10.0
```

## `LARGE_MANA_POTION` { #large_mana_potion }

```yaml title="item/consumable.yml · LARGE_MANA_POTION"
LARGE_MANA_POTION:
  base:
    material: PLAYER_HEAD
    skull-texture:
      value: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvN2FmNmRjNjdjZTc1YjcyMjJhYzM5ZTA1MzZlMDkwNzI0OWY4NTUxNmVmZDEzODViZWM5MGJlMzNkZDUzZGUwNyJ9fX0=
      uuid: 0b4b6108-eb50-4a35-ae8b-53d5c2ad2a84
    name: "&f大型魔力药水"
    restore-mana:
      base: 35.0
      spread: 0.042
      max-spread: 0.13
    item-cooldown: 15.0
    sounds:
      on-consume: entity.generic.drink
```

## `TACO` { #taco }

```yaml title="item/consumable.yml · TACO"
TACO:
  base:
    material: PLAYER_HEAD
    skull-texture:
      value: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTQ5ZDNkODg5Y2ZmNjU1YzYyMjgzNDE4NDU1MjA1YjAzYWU3N2ZmYjdlZTE4ZGQwM2FjMGE0ZmZiODk1NjE1YiJ9fX0=
      uuid: c8113aeb-0b63-4654-9e8f-54416fd2fde8
    name: "&f墨西哥卷饼"
    item-cooldown: 2.0
    lore:
      - "&7&o热乎 & 美味的墨西哥卷饼！"
    restore-health: 3.0
    restore-food: 8.0
    restore-saturation: 10.0
```

## `BURGER` { #burger }

```yaml title="item/consumable.yml · BURGER"
BURGER:
  base:
    material: PLAYER_HEAD
    item-cooldown: 3.0
    skull-texture:
      value: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTUwMzkxYjEzODNkOWVmOWU2ZTdiZjVmODJkMWNmODgyZDgxZTJiMDA0ZGUzNjlmNzI5ZWRhMDRiMmVhNjNkMyJ9fX0=
      uuid: 076dd3bf-0d76-497b-9745-40ed9402a311
    restore-stamina: 30.0
    name: "&f美味汉堡"
    lore:
      - "&7&o嗯，好吃！"
    restore-health: 4.0
    restore-food: 10.0
    restore-saturation: 9.0
```

## `WEIRD_CANDY_BAG` { #weird_candy_bag }

```yaml title="item/consumable.yml · WEIRD_CANDY_BAG"
WEIRD_CANDY_BAG:
  base:
    material: PLAYER_HEAD
    skull-texture:
      value: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODdmNTA0Y2RiZjViMjExMjFiODIxODUyOGRjZTU2NzUwNWQ0NTY3ZDdlNzJjZDQzYTQ2M2NkNTFjODAxM2E2In19fQ==
      uuid: efdf121e-209f-49a2-9c56-d0bf058f33ae
    name: "&9古怪糖果袋"
    item-cooldown: 3.0
    effects:
      CONFUSION:
        duration: 30
        amplifier: 1
    restore-food: 4
```

## `SUSHI_ROLL` { #sushi_roll }

```yaml title="item/consumable.yml · SUSHI_ROLL"
SUSHI_ROLL:
  base:
    material: PLAYER_HEAD
    skull-texture:
      value: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMmVlYzc2NDBlNDMyNDBjODE2N2IxNjc3ZWFiZmZhYWQ5ZjYyODA2Y2NiZTI2NzMyNGM5N2NlYjcyOWQzMDNhIn19fQ==
      uuid: b7c55ea2-d4cc-467e-85c7-dd8052c1675b
    name: "&f寿司卷"
    lore:
      - "&7&o寿司绝对是"
      - "&7&o地球上最好吃的食物。"
    item-cooldown: 0.5
    effects:
      SPEED:
        duration:
          base: 10
          scale: 10
        amplifier: 1
    restore-health: 1
```

## `SOULBINDER1` { #soulbinder1 }

```yaml title="item/consumable.yml · SOULBINDER1"
SOULBINDER1:
  base:
    material: ENDER_EYE
    name: "&f学徒灵魂绑定器"
    disable-interaction: true
    soulbound-level: 1.0
    soulbinding-chance: 70.0
```

## `SOULCRUSHER1` { #soulcrusher1 }

```yaml title="item/consumable.yml · SOULCRUSHER1"
SOULCRUSHER1:
  base:
    material: ENDER_PEARL
    name: "&f新手灵魂粉碎器"
    disable-interaction: true
    soulbound-level: 1.0
    soulbound-break-chance: 30.0
```

## `SOULBINDER2` { #soulbinder2 }

```yaml title="item/consumable.yml · SOULBINDER2"
SOULBINDER2:
  base:
    material: ENDER_EYE
    name: "&f中级灵魂绑定器"
    disable-interaction: true
    soulbound-level: 2.0
    soulbinding-chance: 80.0
```

## `SOULCRUSHER2` { #soulcrusher2 }

```yaml title="item/consumable.yml · SOULCRUSHER2"
SOULCRUSHER2:
  base:
    material: ENDER_PEARL
    name: "&f中级灵魂粉碎器"
    disable-interaction: true
    soulbound-level: 2.0
    soulbound-break-chance: 40.0
```

## `SOULBINDER3` { #soulbinder3 }

```yaml title="item/consumable.yml · SOULBINDER3"
SOULBINDER3:
  base:
    material: ENDER_EYE
    name: "&f奥术灵魂绑定器"
    disable-interaction: true
    soulbound-level: 3.0
    soulbinding-chance: 90.0
```

## `SOULCRUSHER3` { #soulcrusher3 }

```yaml title="item/consumable.yml · SOULCRUSHER3"
SOULCRUSHER3:
  base:
    material: ENDER_PEARL
    name: "&f奥术灵魂粉碎器"
    disable-interaction: true
    soulbound-level: 3.0
    soulbound-break-chance: 50.0
    effects:
      SPEED:
        duration:
          base: 10.0
          scale: 10.0
          spread: 0.0
          max-spread: 0.0
        amplifier: 1.0
```

## `SANTA_COOKIE` { #santa_cookie }

```yaml title="item/consumable.yml · SANTA_COOKIE"
SANTA_COOKIE:
  base:
    material: COOKIE
    name: "&c圣&f&c诞&f&c老&f&c人&f的&c&f饼&c&f干"
    lore:
      - "&7&o那些该死的饼干去哪了！"
    sounds:
      on-consume: entity.player.burp
    item-cooldown: 2.0
    effects:
      SPEED:
        duration: 1
        amplifier: 2
    restore-saturation: 12
```

## `ENDER_NOTE` { #ender_note }

```yaml title="item/consumable.yml · ENDER_NOTE"
ENDER_NOTE:
  base:
    material: PAPER
    ability:
      right-click:
        type: BLINK
        mode: RIGHT_CLICK
        cooldown: 180
        range: 150.0
    name: "&5末影之书"
    item-cooldown: 180
    sounds:
      on-consume: entity.enderman.teleport
    lore:
      - "&7将你传送到&5数英里&7之外。"
    effects:
      HARM:
        duration: 1
        amplifier: 2
```

## `THROW_COAL` { #throw_coal }

```yaml title="item/consumable.yml · THROW_COAL"
THROW_COAL:
  base:
    material: COAL
    ability:
      right-click:
        type: ITEM_THROW
        cooldown: 3.0
        damage: 3.0
        mode: RIGHT_CLICK
    name: "&f可投掷的煤炭"
    lore:
      - "&f朝你的朋友扔过去吧"
    item-cooldown: 3.0
```

## `EGGNOG` { #eggnog }

```yaml title="item/consumable.yml · EGGNOG"
EGGNOG:
  base:
    material: EGG
    name: "&6蛋奶酒"
    disable-interaction: true
    item-cooldown: 3.0
    commands:
      '1':
        format: me Mmmmmh!
        cooldown: 3.0
    lore:
      - "&e于 2018 年圣诞节获得！"
      - "&e&o一杯清新 & 冰凉的蛋奶酒！"
    crafting:
      shapeless:
        '1':
          - EGG
          - SUGAR
          - AIR
          - AIR
          - AIR
          - AIR
          - AIR
          - AIR
          - AIR
    restore-health: 2.0
    restore-food: 2.0
    restore-saturation: 4.0
```

## `MANGO` { #mango }

```yaml title="item/consumable.yml · MANGO"
MANGO:
  base:
    material: PLAYER_HEAD
    name: "&f芒果"
    skull-texture:
      value: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYTk1MzM4OGNjZDZmZjY0ZmMxOTUwZGQ0Y2VjNGFkZWFhMzQ4YWFhYmNjNTMyODI4ZTcxNDRmNTA5ZjIzYyJ9fX0=
      uuid: 1c6aa7d0-582e-4111-8376-74a2a2f74a58
    tier: COMMON
    lore:
      - "&7&o酸酸甜甜，嗯，完美的组合"
    effects:
      REGENERATION:
        duration: 20
        amplifier: 1
    vanilla-eating: false
    restore-food: 8
    restore-saturation: 10
```

## `RECALL_STAR` { #recall_star }

```yaml title="item/consumable.yml · RECALL_STAR"
RECALL_STAR:
  base:
    material: NETHER_STAR
    name: "§f§l回城之星"
    lore:
      - "§a右键点击时执行 §2/spawn§a。"
      - "§b除此之外，还可以用它§9鉴定§b物品。"
    max-consume: 5.0
    can-identify: true
    tier: EPIC
    commands:
      cmd0:
        format: spawn
        delay: 0.0
        op: true
    item-cooldown: 5.0
```

## `GEM_REMOVER` { #gem_remover }

```yaml title="item/consumable.yml · GEM_REMOVER"
GEM_REMOVER:
  base:
    material: SHEARS
    lore:
      - "§7随机移除任意物品上镶嵌的一颗宝石。"
    name: "§6宝石移除器"
    disable-interaction: true
    random-unsocket: 1.0
    inedible: true
```

## `SKIN_REMOVER` { #skin_remover }

```yaml title="item/consumable.yml · SKIN_REMOVER"
SKIN_REMOVER:
  base:
    material: SHEARS
    lore:
    - "§7移除任意物品上应用的皮肤。"
    name: "§6皮肤移除器"
    disable-interaction: true
    can-deskin: true
    inedible: true
```
