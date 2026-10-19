---
title: "家具执行动作"
source_url: "https://wiki.itemsadder.com/adding-content/furnitures/furniture-execute-actions"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 家具执行动作

## 交互时执行命令

使用 `placed_furniture` -> `interact` 事件即可。

```yaml
items:
  lamp:
    display_name: "Lamp"
    permission: myitems.decorative.lamp
    lore:
    - lore-decorative-item
    resource:
      material: PAPER
      generate: false
      model_path: lamp
    behaviours:
      furniture:
        light_level: 13
        solid: true
    events:
      placed_furniture:
        interact:
          execute_commands:
            the_first_command:
              command: help
              as_console: false
```

本例中的家具会让与其交互的玩家执行命令 `/help`。

[placed_furniture](../items/item-properties/actions/actions.md) 交互事件还可以添加其他[动作](../items/item-properties/events.md)，不局限于 `execute_commands`。

## 交互时打开交易菜单

```yaml
  energy_extractor:
    display_name: display-name-energy_extractor
    permission: energy_extractor
    resource:
      material: PAPER
      generate: false
      model_path: item/energy_extractor
    behaviours:
      furniture:
        solid: true
      furniture_trade_machine:
        title: Energy Extractor
        trades_list:
          cobblestone:
            ingredients:
              slot1:
                item: COBBLESTONE
                amount: 64
            result:
              item: energy_orb
              amount: 6
          cobblestone_slab:
            ingredients:
              slot1:
                item: COBBLESTONE_SLAB
                amount: 64
            result:
              item: energy_orb
              amount: 3
```

本例展示如何将交易 GUI 绑定到家具上，可用于创建自定义机器。

## 让家具可以被食用

需要 ItemsAdder 4.0.16+。

```yaml
items:
  strawberry_pie:
    name: Strawberry Pie
    graphics:
      texture: block/strawberry_pie
    events:
      interact:
        right:
          place_furniture:
            furniture: strawberry_pie_full
            decrement_amount: true
  strawberry_pie_template:
    template: true
    name: Strawberry Pie
    show_in_ia_gui: false
    graphics:
      model: block/strawberry_pie
      icon: item/strawberry_pie
    behaviours:
      furniture:
        enabled: true
        entity: item_display
        fixed_rotation: true
        drop_when_mined: false
        sound:
          break:
            name: block.wool.break
            pitch: 0.8
            volume: 0.6
          place:
            name: block.wool.place
            pitch: 0.8
            volume: 0.6
        display_transformation:
          transform: HEAD
          translation:
            y: 0.5
  strawberry_pie_full:
    variant_of: strawberry_pie_template
    behaviours:
      furniture_consumable:
        hunger: 3
        saturation: 0.6
        furniture_list:
        - strawberry_pie_slice1
        - strawberry_pie_slice2
        - strawberry_pie_slice3
        - strawberry_pie_slice4
        - strawberry_pie_slice5
        - strawberry_pie_slice6
  strawberry_pie_slice1:
    variant_of: strawberry_pie_template
    graphics:
      model: block/strawberry_pie_slice1
  strawberry_pie_slice2:
    variant_of: strawberry_pie_template
    graphics:
      model: block/strawberry_pie_slice2
  strawberry_pie_slice3:
    variant_of: strawberry_pie_template
    graphics:
      model: block/strawberry_pie_slice3
  strawberry_pie_slice4:
    variant_of: strawberry_pie_template
    graphics:
      model: block/strawberry_pie_slice4
  strawberry_pie_slice5:
    variant_of: strawberry_pie_template
    graphics:
      model: block/strawberry_pie_slice5
  strawberry_pie_slice6:
    variant_of: strawberry_pie_template
    graphics:
      model: block/strawberry_pie_slice6
```

本例让家具按列表依次切换模型，并恢复玩家的饥饿值。

利用此行为可以模仿原版蛋糕等物品。

切换完整个模型列表后，家具会消失，表示已被吃完。

`strawberry_pie` 用于让物品在手中及物品栏中都显示 2D 图标。

如果希望手中显示 3D 模型、物品栏显示 2D 图标，可以直接使用 `strawberry_pie_full` 放置家具。
