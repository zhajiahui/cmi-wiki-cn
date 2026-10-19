---
title: "2D 家具图标"
source_url: "https://wiki.itemsadder.com/adding-content/furnitures/furniture-2d-icon"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 2D 家具图标

此方法用于兼容低于 1.21.2 的客户端。\
Minecraft 1.21.2 已支持直接设置 2D 图标。

请参阅[新版教程](../items/item-properties/2d-icon.md)。


### 步骤 1

为家具创建 2D 图标

将 `myitems` 替换为你的[命名空间](../../plugin-usage/beginners/configs-and-resourcepack.md#what-is-a-namespace)。

```yaml
info:
  namespace: myitems
items:
  2d_furniture:
    display_name: 2d_furniture
    permission: 2d_furniture
    resource:
      material: PAPER
      generate: true
      textures:
      - item/2d_furniture
    events:
      interact:
        right:
          place_furniture:
            furniture: furniture
            decrement_amount: true
        right_shift:
          place_furniture:
            furniture: furniture
            decrement_amount: true
```

接着在 `contents\myitems\resourcepack\myitems\textures\item\` 文件夹中创建 `2d_furniture.png` 文件。

### 步骤 2

创建显示已放置家具模型的物品。它是与您在背包中看到的物品（在**步骤 1** 中创建的物品）不同的物品。

```yaml
info:
  namespace: myitems
items:
  furniture:
    display_name: furniture
    permission: furniture
    lore:
    - 'lore-decorative-item'
    resource:
      material: PAPER
      generate: false
      model_path: decoration/furniture
    behaviours:
      furniture:
        solid: true
        cancel_drop: true
        hitbox:
          length: 1
          width: 1
          height: 1
    events:
      placed_armorstand:
        break:
          drop_item:
            item: 2d_furniture
  2d_furniture:
    display_name: 2d_furniture
    permission: 2d_furniture
    resource:
      material: PAPER
      generate: true
      textures:
      - item/2d_furniture
    events:
      interact:
        right:
          place_furniture:
            furniture: furniture
            decrement_amount: true
        right_shift:
          place_furniture:
            furniture: furniture
            decrement_amount: true
```

接着在 `dcontents\myitems\resourcepack\myitems\models\decoration\` 文件夹中创建 `furniture.json` 文件。

### 完成！

现在尝试手持 `2d_furniture` 物品右键点击，你会看到放置出的 `furniture` 模型。
