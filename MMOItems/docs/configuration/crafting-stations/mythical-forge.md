---
title: crafting-stations/mythical-forge.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: crafting-stations/mythical-forge.yml
source_version: 6.10.1-SNAPSHOT
---

# crafting-stations/mythical-forge.yml

文件：`crafting-stations/mythical-forge.yml`。版本：`6.10.1-SNAPSHOT`。

随包配置。

## `name` { #name }

```yaml title="crafting-stations/mythical-forge.yml · name"
# 打开合成站时
# 显示的名称
name: "神话熔炉"
```

## `max-queue-size` { #max-queue-size }

```yaml title="crafting-stations/mythical-forge.yml · max-queue-size"
# 合成队列中物品的最大数量，即
# 玩家可以同时制作的物品数量上限。
# 必须介于 1 和 64 之间。
max-queue-size: 6
```

## `recipes` { #recipes }

```yaml title="crafting-stations/mythical-forge.yml · recipes"
# 合成站配方
recipes:
  soulstealer:
    output: 'mmoitems{type=SWORD,id=SOULSTEALER}'
    crafting-time: 20
    conditions:
      - 'level{level=24}'
    ingredients:
      - "mmoitem{type=MISCELLANEOUS,id=HUMAN_SOUL,amount=8,display=\"人类灵魂\"}"
      - "mmoitem{type=SWORD,id=STEEL_SWORD,amount=1,display=\"钢剑\"}"
  fire-essence:
    output: 'mmoitems{type=MATERIAL,id=FIRE_ESSENCE}'
    crafting-time: 5
    conditions:
      - 'level{level=15}'
    ingredients:
      - "vanilla{type=BLAZE_POWDER,amount=4,display=\"烈焰粉\"}"
  fire-totem:
    output: 'mmoitems{type=CATALYST,id=FIRE_TOTEM}'
    crafting-time: 30
    conditions:
      - 'level{level=10}'
    ingredients:
      - "mmoitem{type=MATERIAL,id=FIRE_ESSENCE,amount=8,display=\"火焰精华\"}"
      - "vanilla{type=BLAZE_ROD,amount=1,display=\"烈焰棒\"}"
      - "vanilla{type=BLAZE_POWDER,amount=4,display=\"烈焰粉\"}"
  blaze-soul:
    output: 'mmoitems{type=GEM_STONE,id=BLAZE_SOUL}'
    crafting-time: 20
    conditions:
      - 'level{level=12}'
    ingredients:
      - "mmoitem{type=MATERIAL,id=FIRE_ESSENCE,amount=5,display=\"火焰精华\"}"
  hell-bow:
    output: 'mmoitems{type=BOW,id=HELL_BOW}'
    crafting-time: 20
    conditions:
      - 'level{level=24}'
    ingredients:
      - "mmoitem{type=MATERIAL,id=FIRE_ESSENCE,amount=2,display=\"火焰精华\"}"
      - 'vanilla{type=BOW,amount=1,display="Bow"}'
  fire-greatlance:
    output: 'mmoitems{type=LANCE,id=FIRE_GREATLANCE}'
    crafting-time: 35
    conditions:
      - 'level{level=30}'
    ingredients:
      - "mmoitem{type=MATERIAL,id=FIRE_ESSENCE,amount=4,display=\"火焰精华\"}"
  molten-blade:
    output: 'mmoitems{type=GREATSWORD,id=MOLTEN_BLADE}'
    crafting-time: 20
    conditions:
      - 'level{level=20}'
    ingredients:
      - "mmoitem{type=MATERIAL,id=FIRE_ESSENCE,amount=13,display=\"火焰精华\"}"
      - "mmoitem{type=SWORD,id=STEEL_SWORD,amount=1,display=\"钢剑\"}"
  wither-essence:
    output: 'mmoitems{type=MATERIAL,id=WITHER_ESSENCE}'
    crafting-time: 5
    conditions:
      - 'level{level=20}'
    ingredients:
      - 'vanilla{type=WITHER_SKELETON_SKULL}'
  marking-bow:
    output: 'mmoitems{type=BOW,id=MARKING_BOW}'
    crafting-time: 20
    conditions:
      - 'level{level=20}'
    ingredients:
      - 'vanilla{type=BOW,amount=1,display="Bow"}'
      - "mmoitem{type=MATERIAL,id=WITHER_ESSENCE,amount=1,display=\"凋灵精华\"}"
  cursed-wither-skull:
    output: 'mmoitems{type=ARMOR,id=CURSED_WITHER_SKULL}'
    crafting-time: 10
    conditions:
      - 'level{level=15}'
    ingredients:
      - 'vanilla{type=IRON_HELMET}'
      - "mmoitem{type=MATERIAL,id=WITHER_ESSENCE,display=\"凋灵精华\"}"
  dead-pharaoh-helmet:
    output: 'mmoitems{type=ARMOR,id=DEAD_PHARAOH_HELMET}'
    crafting-time: 10
    conditions:
      - 'level{level=10}'
    ingredients:
      - 'vanilla{type=DIAMOND}'
      - 'vanilla{type=SKELETON_SKULL}'
  mossy-skeleton-skull:
    output: 'mmoitems{type=ARMOR,id=MOSSY_SKELETON_SKULL}'
    crafting-time: 10
    conditions:
      - 'level{level=17}'
    ingredients:
      - 'vanilla{type=MOSSY_COBBLESTONE}'
      - 'vanilla{type=SKELETON_SKULL}'
```

## `gui-layout` { #gui-layout }

```yaml title="crafting-stations/mythical-forge.yml · gui-layout（1/2）"
gui-layout:
  # 界面显示名称
  name: "神话熔炉 ({page}/{max_page})"

  # 界面的槽位数量。必须
  # 介于 9 和 54 之间，且为 9 的倍数。
  slots: 54

  # 启用后，玩家可以右键点击配方
  # 打开另一个界面(配置方式见下方)，
  # 显示所需的全部材料及正在
  # 制作或升级的物品。这称为“预览”界面。
  enable_right_click_preview: true

  # 启用后，左键或右键点击都会打开预览界面。
  # 适合兼顾基岩版玩家的服务器。
  force_preview_on_click: false

  # 执行特定操作时播放的声音。
  sound:
    craft: ENTITY_EXPERIENCE_ORB_PICKUP
    upgrade: ENTITY_EXPERIENCE_ORB_PICKUP
    queue_cancel: ENTITY_EXPERIENCE_ORB_PICKUP
    queue_claim: ENTITY_EXPERIENCE_ORB_PICKUP
    queue_add: ENTITY_EXPERIENCE_ORB_PICKUP
```

```yaml title="crafting-stations/mythical-forge.yml · gui-layout（2/2）"
gui-layout:

  items:

    # 下一页/上一页
    previous_page:
      item: PLAYER_HEAD
      name: "&6上一页"
      texture: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmQ2OWUwNmU1ZGFkZmQ4NGU1ZjNkMWMyMTA2M2YyNTUzYjJmYTk0NWVlMWQ0ZDcxNTJmZGM1NDI1YmMxMmE5In19fQ==
      slots: [ 9 ]
      click_sound: BLOCK_LEVER_CLICK
      hide_if_no_page: true # 没有上一页时隐藏翻页物品。
      no_page: # 没有上一页时显示的物品。
        item: AIR

    next_page:
      item: PLAYER_HEAD
      name: "&6下一页"
      texture: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTliZjMyOTJlMTI2YTEwNWI1NGViYTcxM2FhMWIxNTJkNTQxYTFkODkzODgyOWM1NjM2NGQxNzhlZDIyYmYifX19
      slots: [ 17 ]
      click_sound: BLOCK_LEVER_CLICK
      hide_if_no_page: true # 没有下一页时隐藏翻页物品。
      no_page: # 没有下一页时显示的物品。
        item: AIR

    # 合成队列相关的物品
    previous_queue_item:
      item: PLAYER_HEAD
      function: previous_queue_item
      name: "&6上一个物品"
      texture: 'eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmQ2OWUwNmU1ZGFkZmQ4NGU1ZjNkMWMyMTA2M2YyNTUzYjJmYTk0NWVlMWQ0ZDcxNTJmZGM1NDI1YmMxMmE5In19fQ=='
    next_queue_item:
      item: PLAYER_HEAD
      name: "&6下一个物品"
      texture: 'eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTliZjMyOTJlMTI2YTEwNWI1NGViYTcxM2FhMWIxNTJkNTQxYTFkODkzODgyOWM1NjM2NGQxNzhlZDIyYmYifX19'

    queued_item:
      slots: [ 38, 39, 40, 41, 42 ]

      existing:
        name: "&6&l队列&f {name}"
        delay_format: 'smhdMy'
        lore:
          - "{ready}&7&o这件物品已制作完成。"
          - "{queue}&7&o这件物品正在合成队列中。"
          - '{queue}'
          - "{queue}&7剩余时间：&c{time_left}"
          - ''
          - "{ready}&e► 点击领取！"
          - "{queue}&e► 点击取消"

      none:
        item: GRAY_STAINED_GLASS_PANE
        name: "&6队列中没有物品"

    recipe:
      function: recipe
      slots: [ 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25 ]
      delay_format: 'smhdMy'

      # 合成配方的显示方式
      craft:
        name: "&a&l制作&f {name}"
        name_multiple: "&a&l制作&f {amount}x {name}"

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

        lore:
          - '{conditions}'
          - "{conditions}&8条件："
          - '{crafting_time}'
          - "{crafting_time}&7制作时间：&c{crafting_time}"
          - '{ingredients}'
          - "{ingredients}&8材料："
          - '{lore}'
          - ''
          - "&e► 左键点击制作！"
          - "&e► 右键点击预览！"

      # 升级配方的显示方式
      upgrade:
        name: "&e&l升级&f {name}"
        lore:
          - '{conditions}'
          - "{conditions}&8条件："
          - '{ingredients}'
          - "{ingredients}&8材料："
          - '{lore}'
          - ''
          - "&e► 左键点击升级！"
          - "&e► 右键点击预览！"

      # 没有配方时
      none:
        item: GRAY_STAINED_GLASS_PANE # 可设为 AIR
        name: "&6没有配方"
```

## `preview-gui-layout` { #preview-gui-layout }

```yaml title="crafting-stations/mythical-forge.yml · preview-gui-layout"
# 如果在前面的界面布局配置中关闭了
# `enable_right_click_preview` 选项，可以删除此整个配置节。
preview-gui-layout:
  name: "预览"
  slots: 45
  items:

    # 材料周围的边框(仅作装饰)
    cosmetic_border:
      item: GRAY_STAINED_GLASS_PANE
      name: '&6'
      slots: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 17, 18, 19, 20, 24, 25, 26, 27, 29, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44 ]

    # 确认/返回按钮
    confirm:
      item: EMERALD
      name: "&6确认"
      slots: [ 34 ]
    back:
      item: PLAYER_HEAD
      name: "&6返回"
      slots: [ 10 ]
      texture: 'eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmQ2OWUwNmU1ZGFkZmQ4NGU1ZjNkMWMyMTA2M2YyNTUzYjJmYTk0NWVlMWQ0ZDcxNTJmZGM1NDI1YmMxMmE5In19fQ=='

    # 预览正在制作或升级的物品
    preview_output:
      slots: [ 16 ]

    # 显示配方
    recipe:
      slots: [ 28 ]
      material: KNOWLEDGE_BOOK # 可选项。注释掉此行后，不会替换物品类型。
      remove_lore_lines: 3 # 从物品描述中移除的行数

    # 正在处理的物品
    ingredient:
      slots: [ 12, 13, 14, 21, 22, 23, 30, 31, 32 ]

      # 没有材料时
      none:
        material: AIR
```
