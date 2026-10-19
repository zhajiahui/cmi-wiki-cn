---
title: "资源"
source_url: "https://wiki.itemsadder.com/adding-content/items/item-properties/resource"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 资源

本节介绍面向低于 1.21.4 版本客户端的方法。

ItemsAdder 4.0.13+ 和 Minecraft 1.21.4+ 支持新的物品外观制作方式。\
[更多信息](../modern-items-creation.md)。

物品名称、命名空间、纹理文件（`.png`）和模型文件（`.json`）请勿使用大写字母或特殊字符。

## 自动生成

添加 `resource` 属性，以指定物品使用的纹理／模型。\
示例：

```yaml
  resource:
    material: DIAMOND_SWORD
    generate: true
    textures:
    - item/example_item.png
```

`material` 是此物品使用的原版基础材质。

`generate` 控制 IA 是否根据列出的纹理自动生成物品模型。

`textures` 列出 IA 用于自动生成模型的纹理。

### 纹理放在哪里？

`textures` 中列出的纹理必须放在正确目录。\
例如，使用示例中的 `textures`，且**命名空间**为 `my_items`，则应将 `example_item.png` 放入 `contents/my_items/textures/item`。

路径不存在时，请创建所需文件夹。

`textures` 中可以省略 `.png`，ItemsAdder 会自动识别。

## 使用自己的 3D 模型（`.json` 文件）

已有自定义剑或其他物品的模型时，可以让 IA 不再自动生成模型。\
示例：

```yaml
  resource:
    material: DIAMOND_SWORD
    generate: false
    model_path: item/floating_sword
```

### 模型放在哪里？

`model_path` 指定的模型必须放在正确目录。\
例如，使用示例中的 `model_path`，且**命名空间**为 `my_items`，则应将 `floating_sword.json` 放入 `contents/my_items/models/item`。

路径不存在时，请创建所需文件夹。

### **纹理没有正常显示！**

若自定义模型的纹理未显示，请打开模型文件，修正纹理路径。\
例如原先为：

```json
{
  "textures": {
    "4": "item/alchemy_candles/white_candle",
    "6": "item/alchemy_candles/candle_top",
    "7": "item/alchemy_candles/red_candle",
    "8": "item/alchemy_candles/fire"
  }
}
```

需要改成以下形式（`your_namespace` 为你的命名空间）：

```json
{
  "textures": {
    "4": "your_namespace:item/alchemy_candles/white_candle",
    "6": "your_namespace:item/alchemy_candles/candle_top",
    "7": "your_namespace:item/alchemy_candles/red_candle",
    "8": "your_namespace:item/alchemy_candles/fire"
  }
}
```

## 透明纹理（玻璃等）

### 家具

[transparent-furniture.md](../../furnitures/transparent-furniture.md)

### 方块

[transparent-block.md](../../blocks/transparent-block.md)

## 手动指定 custom\_model\_data

如需强制使用指定的 `custom_model_data`（`CustomModelData`），可以这样配置：

```yaml
    resource:
      material: CLOCK
      model_id: 4000
      generate: false
      model_path: "item/my_custom_item_model"
```

也可以让 ItemsAdder 根据纹理自动生成模型：

```yaml
info:
  namespace: my_items
items:
  my_item_4000_example:
    resource:
      material: DIAMOND
      generate: true
      model_id: 4000
      textures:
      - item/my_custom_texture.png
```

**重要**

若先前已创建物品并执行过 `/iazip`，之后修改了 `model_id`，就需要执行以下命令。\
务必执行 `/iacleancache items`，以**移除未使用的 ID**并**更新修改过的 ID**。

## 创建 3D 模型

作者使用免费的 [BlockBench](https://blockbench.net/) 创建 Minecraft 自定义模型。


### 从纹理创建 3D 模型


**重要**

若使用**非原版**纹理（自己的 **.png** 文件），需要打开模型的 **.json** 文件做少量修改。

模型使用自定义纹理时，务必在纹理名称前加上命名空间。\
例如，3D 模型使用的纹理位于 `contents/my_items/textures/item/custom_item_1.png`：

```json
{
  "textures": {
    "0": "item/custom_item_1"
  }
}
```

需要在前面添加**命名空间**（原文此处示例使用 `myitems`，请替换为你自己的命名空间）。

```json
{
  "textures": {
    "0": "myitems:item/custom_item_1"
  }
}
```
