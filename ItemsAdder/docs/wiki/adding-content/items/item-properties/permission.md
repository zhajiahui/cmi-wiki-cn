---
title: "权限"
source_url: "https://wiki.itemsadder.com/adding-content/items/item-properties/permission"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 权限

### 物品权限示例

```yaml
  my_armor_simple_helmet:
    display_name: my_armor_simple helmet
    permission_suffix: my_armor_simple
    resource:
      generate: true
    durability:
      max_custom_durability: 275
    specific_properties:
      armor:
        slot: head
        color: '#ff0001'
    attribute_modifiers:
      head:
        armor: 9
        armorToughness: 1
```

## 让物品显示在 `/ia` 界面中

要让玩家在 `/ia` 界面中**看到**该物品，需授予 `ia.user.ia.seeitem.my_armor_simple` 权限。

还需授予 `ia.user.ia`，以便玩家使用 `/ia` 命令。

记得为 `/ia` 界面创建[分类](../../../plugin-usage/plugin-configuration/recipes-menu.md)。

## 配方权限 <a id="recipes-permissions"></a>

### 示例

**权限：**`ia.user.recipe.iasurvival.cooked_sausage`

```yaml
info:
  namespace: iasurvival
recipes:
  cooking:
    cooked_sausage:
      permission: iasurvival.cooked_sausage
      ingredient:
        item: iasurvival:sausage
      machines:
        - FURNACE
        - BLAST_FURNACE
      exp: 1
      cook_time: 200
      result:
        item: iasurvival:cooked_sausage
        amount: 1
```

## 更多权限说明

[permissions.md](../../../plugin-usage/plugin-configuration/permissions.md)
