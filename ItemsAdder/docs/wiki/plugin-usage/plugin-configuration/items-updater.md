---
title: "物品更新器"
source_url: "https://wiki.itemsadder.com/plugin-usage/plugin-configuration/items-updater"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 物品更新器

自 ItemsAdder 4.0.12 起可用

ItemsAdder 会自动更新世界中的物品。\
这样就无需手动向玩家发放更新后的物品。

## 禁用单个 ItemStack 实例的更新

要禁用背包中某个物品的自动更新，必须使用此命令：\
`/iaitem set-itemstack-auto-update <true|false>`

## 完全禁用某种自定义物品的更新

你也可以在配置文件中完全禁用某些物品的自动更新

例如，你想提高一把剑的攻击伤害，但不想让已合成的剑获得新伤害，因为玩家可能已经合成了很多，这样会让它们过于强大。

这样，已合成的剑仍会保留原来的攻击伤害。

#### 示例

```yaml
  test_item2:
    name: Test Item 2
    resource:
      generate: false
      model_path: minecraft:item/diamond
      material: IRON_SWORD
    max_stack_size: 16
    lore:
    - lol
    - lol
    enchants:
    - BREACH
    attribute_modifiers:
      head:
        armor_toughness: 8
    auto_update:
      enabled: false # <--- here
```

也可以在 `config.yml` 中全局禁用配置中所有物品的自动更新。

```yaml
items:
# ....
  auto_update:
    enabled: true # <--- here
```

## 一些特殊设置

### `enchantment_mode`

```yaml
    auto_update:
      enchantment_mode: MERGE # MERGE or REPLACE (MERGE by default)
```

* `MERGE` - 合并旧物品与新物品的附魔
* `REPLACE` - 用新物品的附魔完全替换旧物品的附魔

### `fix_unstackable_items_on_click`&#xD;

这会强制将光标上的自定义物品与点击的物品合并，前提是两者具有相同的 `namespace` + `id`。
