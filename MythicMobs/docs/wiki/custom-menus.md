---
title: 自定义菜单
source_url: https://wiki.mythiccraft.io/mythicmobs/Custom-Menus
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 自定义菜单

自定义菜单是 MythicMobs Premium 提供的一项功能，也可以通过 MythicRPG 配合免费版 MythicMobs 使用，用于创建自己的菜单！

> **此功能需要 [MythicMobs Premium](premium-features.md) 或 [MythicRPG](https://mythiccraft.io/index.php?resources/mythicrpg-spells-classes-professions-more.129/)！**

1. [按钮技能](custom-menus.md#button-skills)

### 创建菜单 {#creating-menus}

在任意 Mythic 内容包的 `menus` 文件夹中创建 `.yml` 文件，即可定义菜单。

例如，可以在 `plugins/MythicMobs/menus/custom_menus.yml` 新建 `.yml` 文件。

每个顶层节点都会按标准 Mythic 菜单格式加载为一个菜单。例如，要创建名为 `MyCustomMenu` 的菜单，可以在文件中写入：

```yaml
MyCustomMenu:
  Display: "My Custom Menu"
  Size: 27
  Shared: false # Whether the Menu should not be cached and shared across players
  Schema:
    - '1 1 1 1 1 1 1 1 1'
    - '0 0 0 0 B 0 0 0 0'
    - '1 1 1 1 1 1 1 1 1'
  Icons:
    FILLER:
      Mapping: 1
      Material: RED_STAINED_GLASS_PANE
      Display: ''
      Model: 1
    TEST_BUTTON:
      Mapping: B
      Material: GOLD_INGOT
      Model: 4
      Display: 'Test'
      Skills:
      - sound{s=entity.chicken.egg}
      - setcustommenubutton{slot=11;icon=DYNAMIC_BUTTON}
      - message{m="you hit me"} @self
    DYNAMIC_BUTTON:
      Material: IRON_SWORD
      Model: 100
```

此示例包含自定义菜单系统的多项功能。

`Schema` 定义菜单的外观，本质上是一个 `9 x height` 网格，用来排列菜单图标。每个字母或数字都对应 `Icons` 部分定义的一个图标。

例如，Schema 中所有标有 1 的槽位都对应 FILLER：

```yaml
    FILLER:
      Mapping: 1
```

图标包含以下内容：

- `Mapping`：用于将图标映射到布局的字母或数字
- `Material`：图标的材质
- `Model`：图标的 CustomModelData
- `Display`：图标的显示名称
- `Lore`：多行物品描述。如果某一行中的占位符返回多行文本，例如 `<mythicitem.[MythicItem].lore>`，则返回的每一行都会成为单独的一行物品描述
- `Skills`：按下按钮时执行的技能
- `HideFlags`：是否隐藏所有物品标志，使属性、附魔等内容不显示在图标的提示信息中。默认为 `true`；存在 `Hide` 列表时默认为 `false`
- `Hide`：要隐藏的特定提示信息部分，使用与[物品相同的语法](items/items.md#hide)。设置后，该列表会成为图标的标志列表，因此同时设置 `HideFlags: true` 仍会隐藏所有内容
- `Glint`：图标是否显示附魔光效，用法与[物品选项](items/options.md#glint)相同。默认为 `false`
- `Enchantments`：应用到图标上的附魔列表，使用与[物品相同的语法](items/enchantments.md)
- `TooltipStyle`：图标自定义提示信息精灵图的资源位置，用法与[物品组件](items/items.md#tooltipstyle)相同。需要 Paper 1.21.3 或更新版本

```yaml
    SWORD_BUTTON:
      Mapping: S
      Material: DIAMOND_SWORD
      Display: 'Epic Sword'
      Hide:
      - ATTRIBUTES
      Glint: true
      Enchantments:
      - SHARPNESS 5
      - KNOCKBACK 1
      TooltipStyle: minecraft:verycooltooltip
```

### 修改菜单 {#modifying-a-menu}

可以使用 `setcustommenubutton{slot=11;icon=ICON}` 技能机制修改已打开的菜单

### 打开菜单 {#opening-menus}

要打开已创建的自定义菜单，可以使用以下方式之一：

- **`Command`** - `/mm menus open [menu] <player>`
- **`Mechanic`**：使用 `openCustomMenu{menu=name}` 技能机制

# 按钮技能 {#button-skills}

如上所示，菜单中的每个按钮都可以关联一组技能，点击按钮后就会执行这些技能。

| [已实现的占位符](skills/placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.click-type>` |

```yaml
  Skills:
  - sound{s=entity.chicken.egg}
  - message{m="<skill.var.click-type>"} @self
```
