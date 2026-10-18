---
title: MMOItems
source: https://docs.phoenixdevt.fr/mmoinventory/compatibility/mmoitems
source_snapshot: '2026-10-19'
---

# MMOItems {#⚔️-mmoitems}

本页介绍如何配置MMOInventory以与 [MMOItems](https://www.spigotmc.org/resources/39267/)一起使用。

## 配置MMOInventory {#configuring-mmoinventory}

MMOInventory附带的默认定制物品栏包含原版、护甲和手槽以及额外的配件槽，例如戒指、护身符、手镯、手套和神器槽。这些*配件插槽*配置为仅接受特定类型的MMOItems物品。

例如，以下代码片段显示如何将 *Left Ring* 和 *Right Ring* 插槽配置为仅接受MMOItems物品类型的`RING`。

```yml
# Ring slots
RIGHT_RING:
    type: accessory
    material: DIAMOND_HOE
    durability: 7
    name: '&6Right Ring Slot'
    slot: 25
    restrictions:
    - 'mmoitemstype{type=RING}'
    lore:
    - Drag & drop an item to equip it.
LEFT_RING:
    type: accessory
    material: DIAMOND_HOE
    durability: 8
    name: '&6Left Ring Slot'
    slot: 34
    restrictions:
    - 'mmoitemstype{type=RING}'
    lore:
    - Drag & drop an item to equip it.
```

## 配置MMOItems {#configuring-mmoitems}

上一节中的代码片段仅在MMOInventory的自定义物品栏内注册自定义插槽。为了使该代码正常工作，你还需要在MMOItems注册表中注册相应的物品类型。MMOItems附带已注册的相应*配件物品类型*，因此你无需从头开始创建它们。

> **警告**
>
> 与MMOInventory中的自定义配件槽（戒指、手镯、护身符...）相对应的所有MMOItems物品类型 **必须** 将其父类型设置为`ACCESSORY`。这对于MMOItems正确注册放置在自定义物品栏GUI内的物品的属性是必需的。

例如，以下代码片段为我们在上一节中配置的两个 *Left Ring* 和 *Right Ring* 插槽注册`RING`物品类型。

```yml
RING:
    display: EMERALD
    name: 'Artifact'
    parent: 'ACCESSORY' # Parent type set to ACCESSORY
    unident-item:
        name: '&f#prefix#Unidentified Ring'
        lore:
        - '&7This item is unidentified. I must'
        - '&7find a way to identify it!'
        - '{tier}'
        - '{tier}&8Item Info:'
        - '{range}&8- &7Lvl Range: &e#range#'
        - '{tier}&8- &7Item Tier: #prefix##tier#'
```

### 重要提示 {#important-note}

---

原文：[⚔️ MMOItems](https://docs.phoenixdevt.fr/mmoinventory/compatibility/mmoitems) · 原文归档：2026-10-19
