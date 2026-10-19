---
title: "MMOItems"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/mmoitems"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# MMOItems

在[此处](https://www.spigotmc.org/resources/mmoitems-premium.39267/)下载 **MMOItems**

### 你可以在此处下载教程中的示例


## 已知限制


## 将MMOItem与ItemsAdder物品连接

### 使用命令 /mmoitems browse

![](../../assets/acafc5511ecaf77a9751.png)

### 创建一个新的 MMOItem

![](../../assets/fe392675fbdd248c5608.png)

![](../../assets/0708043484cbf7f35efc.png)

### 添加你想要的所有属性,如魔法伤害等

![](../../assets/5f27fdbd2b26ab791ab9.png)

### 在 /mmoitems browse 中预览 MMOItem

![](../../assets/dfb4607ba129fcbf4d8a.png)

### 照常创建 .yml 文件，并添加 ItemsAdder 物品的全部属性

`ItemsAdder/contents/mmoitems_example/configs/example.yml`

如你所见, 我设置了一个叫做 **`mmoitem`** 的新属性, 同时还有 **`type`** 与 **`id`** 。\
这些设置用于**关联这两个物品**。

```yaml
info:
  namespace: mmoitems_example
items:
  test:
    display_name: ""
    permission: example_item
    mmoitem:
      type: SWORD
      id: TEST
    resource:
      material: DIAMOND_SWORD
      generate: true
      textures:
      - item/test.png
    durability:
      max_custom_durability: 1324
```

### 正常创建你的.png纹理

`ItemsAdder/contents/mmoitems_example/resourcepack/mmoitems_example/textures/item/test.png`

### 获得物品

使用指令`/iaget mmoitems_example:test`来得到成品

![](../../assets/d5c76c008f8531e12d96.png)

![](../../assets/317fb6b25713704012e3.png)
