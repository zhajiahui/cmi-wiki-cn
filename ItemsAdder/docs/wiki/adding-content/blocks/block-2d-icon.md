---
title: "方块的 2D 图标"
source_url: "https://wiki.itemsadder.com/adding-content/blocks/block-2d-icon"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 方块的 2D 图标

此方法用于兼容低于 1.21.2 的客户端。\
Minecraft 1.21.2 已支持直接设置 2D 图标。

请参阅[新版教程](../items/item-properties/2d-icon.md)。


### 步骤 1

为方块创建 2D 图标

将 `myitems` 替换为你的[命名空间](../../plugin-usage/beginners/configs-and-resourcepack.md#what-is-a-namespace)！

```yaml
info:
  namespace: myitems
items:
  rocks:
    display_name: Rocks
    permission: blocks.rocks
    lore:
     - 'lore-decorative-item'
    resource:
      material: PAPER
      generate: true
      textures:
      - item/rocks
    events:
      interact:
        right:
          set_block:
            block: rocks_placed
            target: RELATIVE
            decrement_amount: true
        right_shift:
          set_block:
            block: rocks_placed
            target: RELATIVE
            decrement_amount: true
```

接着在 `contents\myitems\resourcepack\myitems\textures\item` 文件夹中创建 `rocks.png` 文件。

### 步骤 2

创建用于显示被放置的岩石模型的物品。这与我们在背包中看到的物品(**步骤 1** 创建的物品)不同。

```yaml
info:
  namespace: myitems
items:
  rocks_placed:
    display_name: ""
    permission: admin.blocks.rocks_placed
    resource:
      material: PAPER
      generate: false
      model_path: block/rocks_placed
    behaviours:
      block:
        placed_model:
          type: REAL_WIRE
        cancel_drop: true
        sound:
          place:
            name: block.stone.place
    events:
      placed_block:
        break:
          drop_item:
            item: rocks
  rocks:
    display_name: Rocks
    permission: blocks.rocks
    lore:
     - 'lore-decorative-item'
    resource:
      material: PAPER
      generate: true
      textures:
      - item/rocks
    events:
      interact:
        right:
          set_block:
            block: rocks_placed
            target: RELATIVE
            decrement_amount: true
        right_shift:
          set_block:
            block: rocks_placed
            target: RELATIVE
            decrement_amount: true
```

接着在 `contents\myitems\resourcepack\myitems\models\block\` 文件夹中创建 `placed_rocks.json` 文件。

### 完成！

现在尝试右键放置 `rocks`，你应该能够看到 `rocks_placed` 模型。
