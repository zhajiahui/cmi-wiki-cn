---
title: 物品栏
source: https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/inventory
source_snapshot: '2026-10-19'
---

# 物品栏 {#🎒-inventory}

## 关闭物品栏 {#close-inventory}

使用此机制可以关闭当前玩家的物品栏。这可以在任何 MMO 插件 UI 中使用：MMOItems合成站、MMOProfiles档案选择、MMOCore技能树UI 等...

```yml
script_close_inventory:
  mechanics:
    - 'close_inventory{}'
```

## 返回 {#go-back}

使用此功能可以让玩家导航到上次访问的页面。例如，这可用于从 *职业确认 UI* 返回到MMOCore中的 *职业选择 UI*。

```yml
script_ui_go_back:
  mechanics:
    - 'go_back{}'
```

---

原文：[🎒 Inventory](https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/inventory) · 原文归档：2026-10-19
