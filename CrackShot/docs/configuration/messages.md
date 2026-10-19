---
title: messages.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: messages.yml
source_version: 0.98.13-x6
---

# messages.yml

文件：`messages.yml`。版本：`0.98.13-x6`。

随包配置。

## `NP_Weapon_Use` { #np_weapon_use }

```yaml title="messages.yml · NP_Weapon_Use"
# 完整的配置说明见《CrackShot 完全指南》（英文）：
# https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot

# 这里是普通玩家最常看到的提示，可以按自己服务器的风格改。
#
# 说明：
# - 有些提示里带变量，例如 "<amount>"、"<item>"、"<cross>"，分别代表数量、武器名和乘号。
# - 建议每条提示都用英文双引号括起来。
# - 想隐藏某条提示，就把内容留空，例如 Store_Created: ""
# - 这里不支持颜色代码。

# 权限相关。
NP_Weapon_Use: "你没有使用这件武器的权限。"
```

## `NP_Weapon_Craft` { #np_weapon_craft }

```yaml title="messages.yml · NP_Weapon_Craft"
NP_Weapon_Craft: "你没有合成这件武器的权限。"
```

## `NP_Store_Create` { #np_store_create }

```yaml title="messages.yml · NP_Store_Create"
NP_Store_Create: "你没有创建这个商店的权限。"
```

## `NP_Store_Purchase` { #np_store_purchase }

```yaml title="messages.yml · NP_Store_Purchase"
NP_Store_Purchase: "你没有购买这件物品的权限。"
```

## `Store_Created` { #store_created }

```yaml title="messages.yml · Store_Created"
# 商店相关。
Store_Created: "商店已创建。"
```

## `Store_Cannot_Afford` { #store_cannot_afford }

```yaml title="messages.yml · Store_Cannot_Afford"
Store_Cannot_Afford: "你买不起这件物品。"
```

## `Store_Items_Needed` { #store_items_needed }

```yaml title="messages.yml · Store_Items_Needed"
Store_Items_Needed: "需要 <amount> 个 <item>。"
```

## `Store_Purchased` { #store_purchased }

```yaml title="messages.yml · Store_Purchased"
Store_Purchased: "已购买：<item>"
```

## `Cannot_Reload` { #cannot_reload }

```yaml title="messages.yml · Cannot_Reload"
# 对不能换弹的武器使用换弹命令时的提示。
# 注意和 "/shot config reload" 区分，后者是重新加载配置。
Cannot_Reload: "这件武器不能换弹。"
```

## `Weapon_Received` { #weapon_received }

```yaml title="messages.yml · Weapon_Received"
# 玩家通过给予命令收到武器时的提示。
# 命令格式是 "/shot give <玩家> <武器> <数量>"。
Weapon_Received: "收到武器：<item> <cross><amount>"
```
