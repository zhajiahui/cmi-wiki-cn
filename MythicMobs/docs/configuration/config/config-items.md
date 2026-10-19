---
title: config/config-items.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config/config-items.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# config/config-items.yml

文件：`config/config-items.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包配置。

## `Configuration` { #configuration }

```yaml title="config/config-items.yml · Configuration"
#
# 物品配置选项
#
# 关于 Mythic 物品功能的更多说明：
# https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/Items/Items
#
Configuration:

  #================================================================================
  # 物品更新器
  #================================================================================
  ItemUpdating:
    Enabled: false
    OnLogin: true
    OnScroll: true
    OnInvClose: true

  #================================================================================
  # 所有物品均使用特殊掉落效果（实验性）
  #================================================================================
  EnableFancyDropEffectsEverywhere: false

  #================================================================================
  # 物品默认设置：选择物品选项的默认值
  #================================================================================
  DefaultItemOptions:
    Material: STONE
    PreventEnchanting: false            # 可设为 true 或 false
    PreventCrafting: modeled            # 可设为 true、false、modeled 或 default
    PreventAnviling: default            # 可设为 true、false、modeled 或 default
    PreventSmithing: default            # 可设为 true、false、modeled 或 default

  #================================================================================
  # 物品技能（需要 Crucible）
  #================================================================================
  ItemSkills:
    JoinDelay: 20                       # 玩家加入后，开始扫描物品前的延迟

  #================================================================================
  # 物品属性（需要 Crucible）
  #================================================================================
  ItemStats:
    Rounding: 2                         # 生成属性时默认保留的小数位数
    SaveRatios: false                   # 为物品更新器保存生成的属性比例

  #================================================================================
  # 物品描述模板（需要 Crucible）
  #================================================================================
  LoreTemplates:
    EnableDefaultTemplate: false        # 是否将默认模板应用于所有物品
    DefaultTemplateName: DEFAULT        # 默认模板的名称
    DefaultTemplate:                    # 默认描述模板
    - Line:
        - '{stats}'
        - "{stats}<gray>额外属性："
        - '{stats-each}<green> <stat.display>'
    - Filler: ''
    - Line:
        - "{augments:GEM}<gray>宝石："
        - '{augments-each:GEM}<yellow><augment.display>'
    - Filler: ''
    - Line:
        - '{lore}'

  #================================================================================
  # 自定义方块（需要 Crucible）
  #================================================================================
  CustomBlocks:
    SwapIsPickBlock: true               # 可设为 true 或 false

  #================================================================================
  # 自定义装备（需要 Crucible）
  #================================================================================
  Equippables:
    Enabled: false
    CustomSlots:
    - Id: NECKLACE
      Display: "项链"
      EquipConditions:
      - itemGroup{group=NECK}
    - Id: RING_1
      Display: "戒指"
      EquipConditions:
      - itemGroup{group=RING}
    - Id: RING_2
      Display: "戒指"
      EquipConditions:
      - itemGroup{group=RING}

  #================================================================================
  # 自定义家具（需要 Crucible）
  #================================================================================
  Furniture:
    DefaultType: DISPLAY                # 可设为 DISPLAY、ARMOR_STAND 或 ITEM_FRAME
```
