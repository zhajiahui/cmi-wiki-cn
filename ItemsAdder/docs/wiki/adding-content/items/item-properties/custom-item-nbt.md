---
title: "自定义物品 NBT"
source_url: "https://wiki.itemsadder.com/adding-content/items/item-properties/custom-item-nbt"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 自定义物品 NBT

## 向物品添加自定义 NBT 属性

可以指定自定义 **NBT** 属性，并合并到自定义物品中。

此功能同时支持旧版 NBT 和 1.20.5+ 的新版 NBT。\
需要时会自动转换旧版 NBT。

各游戏版本的兼容性并非完全一致，建议手动更新 NBT 配置。

1.20.5+ 的改动见[官方说明](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-20-5)（向下滚动）。

请确保提供有效的 **NBT**（`json`），否则不会生效。

## 从文件注入 NBT 属性

**此功能至少需要 ItemsAdder 4.0.8。**

```yaml
info:
  namespace: test
items:
  test_inject_nbt_from_file:
    display_name: "Test inject NBT from file"
    components_nbt_file: "test_inject_nbt_from_file.json"
    resource:
      material: IRON_CHESTPLATE
      generate: false
      model_path: minecraft:item/diamond
```

```json
{
  "components":{
     "minecraft:custom_name": {"text":"Черепаший нагрудник", "italic":false},
     "minecraft:item_name": {"text":"Черепаший нагрудник", "italic":false},
     "minecraft:max_damage":440,
     "minecraft:attribute_modifiers":[
        {
           "id":"turtle_chestplate",
           "type":"minecraft:armor",
           "amount":6,
           "operation":"add_value",
           "slot":"chest"
        },
        {
           "id":"turtle_chestplate",
           "type":"minecraft:oxygen_bonus",
           "amount":1,
           "operation":"add_value",
           "slot":"chest"
        }
     ],
     "minecraft:repairable":{
        "items":"minecraft:turtle_scute"
     }
  }
}
```

## 旧方法：从 NBT 字符串注入

**注意**

使用 `\` 转义 `"` 字符。\
在 YML 中使用字符串前，可用作者的[转义／反转义工具](https://escape-mc-components.lonedev.workers.dev/)处理。

### 自定义属性示例

例如，要将以下标签合并到物品中：\
`nbt: '{my-custom-nbt-tag:"hello this is a custom tag", another-tag:"useless"}'`

```yaml
items:
  custom_nbt_item_data:
    display_name: "Injected nbt data into this item"
    lore:
    - 'test item: custom_nbt_item_data'
    - 'test line from IA config 1'
    - 'test line from IA config 2'
    - 'test line from IA config 3'
    permission: examples.test
    nbt: '{my-custom-nbt-tag:"hello this is a custom tag", another-tag:"useless"}'
    resource:
      material: DIAMOND_SWORD
      generate: false
      model_path: "minecraft:item/diamond"
    durability:
      durability: 650
      max_durability: 1324
    attribute_modifiers:
      mainhand:
        attackDamage: 30
        attackSpeed: 25
```

### 自定义 NBT 与 name 组件

`nbt: '{components:{"minecraft:custom_name":{"text":"TEST", "font": "alt", "italic":false}, "minecraft:custom_data": {"bro":"asd"}}}'`

```yaml
  custom_nbt_item_custom_name:
    enabled: true
    display_name: example_item_custom_name
    lore:
    - 'test item: custom_nbt_item_custom_name'
    - 'test line from IA config 1'
    - 'test line from IA config 2'
    - 'test line from IA config 3'
    permission: custom.test
    nbt: '{components:{"minecraft:custom_name":{"text":"TEST", "font": "alt", "italic":false}, "minecraft:custom_data": {"bro":"asd"}}}'
    resource:
      material: DIAMOND_SWORD
      generate: false
      model_path: "minecraft:item/diamond"
    durability:
      durability: 650
      max_durability: 1324
    attribute_modifiers:
      mainhand:
        attackDamage: 30
        attackSpeed: 25
```

### 旧版 1.20.4 组件：请勿继续使用

这是旧方法，请勿继续使用。

YAML 单引号字符串内部的单引号需要写成两个单引号（`''`）：

`nbt: '{display:{Name:''{"text":"TEST", "font": "alt", "italic":false}''}}'`

```yaml
items:
  custom_nbt_item_custom_name_legacy_nbt:
    enabled: true
    display_name: custom_nbt_item_custom_name_legacy_nbt
    lore:
    - 'test item: custom_nbt_item_custom_name_legacy_nbt'
    - 'test line from IA config 1'
    - 'test line from IA config 2'
    - 'test line from IA config 3'
    permission: custom.test
    nbt: '{display:{Name:''{"text":"TEST", "font": "alt", "italic":false}''}}'
    resource:
      material: DIAMOND_SWORD
      generate: false
      model_path: "minecraft:item/diamond"
    durability:
      durability: 650
      max_durability: 1324
    attribute_modifiers:
      mainhand:
        attackDamage: 30
        attackSpeed: 25
```
