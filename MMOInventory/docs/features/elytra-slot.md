---
title: 鞘翅槽位
source: https://docs.phoenixdevt.fr/mmoinventory/features/elytra-slot
source_snapshot: '2026-10-19'
---

# 鞘翅槽位 {#🪽-elytra-slot}

这是一种特殊类型的老虎机。玩家只能在此类插槽内装备鞘翅。当此插槽配备鞘翅时，玩家从足够高的地方掉落时能够切换到鞘翅。

## 如何使用 {#how-to-use}

在这些插槽之一中装备鞘翅。如果玩家的坠落时间超过4格，并且它们没有“缓慢坠落”药水效果，则鞘翅将自动装备到玩家的胸甲槽位。然后，玩家可以在剩余的飞行中使用鞘翅。当玩家最终接触地面时，鞘翅被放回定制物品栏中，并且之前的胸甲物品被恢复。

## 插槽示例 {#slot-example}

你将在默认的`inventory/default_mmoinventory.yml`配置文件中找到以下语法片段。

```yml
slots:
  #.....
  ELYTRA:
  type: elytra
  material: GOLD_NUGGET
  custom_model_data_string: "elytra"
  name: "&6Elytra Slot"
  restrictions:
    - 'material{materials="ELYTRA"}'
  slot: 14
  lore:
    - 'Only &bElytras&7 are allowed here.'
    - '&bDeploy automatically&7 when falling.'
    - 'Drag & drop an item to equip it.'
```

## 如何禁用 {#how-to-disable}

删除或取消注释所有物品栏中使用插槽类型`elytra`的任何插槽。

## 主要配置 {#main-config}

在`config.yml`中，你可以更改自动装备鞘翅所需的最小下落距离。

```yml
elytra_deployment:

  # If "Slow falling" is detected on the player, fall time
  # is reset, temporarily preventing elytras from deploying
  # until the player hits the ground, or the effect wears off.
  skip_if_slow_falling: true

  # Fall distance threshold (in blocks) after which
  # elytras automatically deploy.
  fall_distance_threshold: 4
```

---

原文：[🪽 Elytra Slot](https://docs.phoenixdevt.fr/mmoinventory/features/elytra-slot) · 原文归档：2026-10-19
