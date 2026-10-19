---
title: "配方菜单"
source_url: "https://wiki.itemsadder.com/plugin-usage/plugin-configuration/recipes-menu"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 配方菜单

## 菜单设置和“All”类别

`ia_gui.yml` 包含 `/ia` 命令界面的设置。\
它还包含 **“all”** 类别，用于显示所有 ItemsAdder 物品。

ItemsAdder 默认内容包的类别位于各 `namespace` 文件夹中的 `categories.yml` 文件里。\
例如: `contents/iasurvival/configs/categories.yml`

### 在 `all` 类别中隐藏物品

你可以从 `all` 类别中隐藏特定物品。

```yaml
hide_items:
- _iainternal:icon_left_grey
- _iainternal:icon_left_blue
- _iainternal:icon_right_grey
- _iainternal:icon_right_blue
- _iainternal:icon_up_grey
- _iainternal:icon_up_blue
```

### 在 `all` 类别中按匹配隐藏物品

你可以隐藏 ID 以特定字符串开头的所有物品。例如，以下配置会隐藏 ID 以 `myitems:hidden_item_` 开头的每个物品。

需要 ItemsAdder 4.0.18+

```yaml
    hide_items:
    - "myitems:hidden_item_*"
```

## 创建自定义类别

如果想创建自己的类别，必须在自己的[命名空间](../beginners/configs-and-resourcepack.md#what-is-a-namespace)中的 `.yml` 文件里创建并添加。\
<mark style="color:red;">不要将类别添加到</mark> <mark style="color:red;">`ia_gui.yml`</mark> <mark style="color:red;">文件中！</mark>\
示例：

```yaml
info:
  namespace: my_items
categories:
  swords:
    enabled: true
    icon: "my_items:custom_item"
    name: 'Swords'
    permission: "ia.menu.seecategory.swords"
    # THIS IS OPTIONAL. Plugin will take the one in ia_gui.yml if not set.
    font_image:
      name: "mcguis:blank_menu"
      x_position_pixels: -16
    # THIS IS OPTIONAL. Plugin will take the one in ia_gui.yml if not set.
    title_position_pixels: 0
    items:
      - "my_items:custom_item"
      - "my_items:custom_item_2"
      - "my_items:custom_item_3"
```

如果希望用户看到这些类别，记得为他们授予每个类别的权限。\
此示例类别的权限是：`ia.menu.seecategory.swords`

**`font_image` 和 `title_position_pixels` 均为可选项。**\
如果未设置，插件会使用 `ia_gui.yml` 中的值。

如果想让每个类别使用不同的背景，此选项就很有用。

**名称相同**而命名空间不同的**类别会被合并**。如果有两个“swords”类别，这会很**有用**。\
这样，打开 **`/ia`** 菜单后，所有剑会归在同一类别中，而不会出现 2 个剑类别。

## 向类别批量添加物品

### 通配符

匹配 `example` 命名空间中的任意物品。

```yaml
categories:
  test:
    enabled: true
    skip_if_already: false
    icon: example:my_item
    name: TEST
    permission: ia.menu.seecategory.test
    items:
      - "example:*"
```

匹配任意命名空间中名为 `some_item` 的物品。

```yaml
categories:
  test:
    enabled: true
    skip_if_already: false
    icon: example:my_item
    name: TEST
    permission: ia.menu
```

### 正则表达式（高级用户）

匹配 `iasurvival` 命名空间中的任意盔甲物品。

使用[此网站](https://regex101.com/)测试正则表达式。

```yaml
  armors:
    enabled: true
    skip_if_already: false
    icon: iasurvival:ruby_helmet
    name: display-category-armors
    permission: ia.menu.seecategory.armors
    items:
      - 'iasurvival\:(.*)_helmet'
      - 'iasurvival\:(.*)_chestplate'
      - 'iasurvival\:(.*)_leggings'
      - 'iasurvival\:(.*)_boots'
```

## 重新排列类别

需要 ItemsAdder 4.0.15+

在 `ItemsAdder/ia_gui.yml` 中，可以为插件的类别设置自定义顺序。\
这是全局设置，会应用于所有命名空间。

### 自动按字母排序

设置 `alphabetical: true`。

```yaml
order:
  alphabetical: true
  force_override:
    enabled: false
```

### 强制使用自定义顺序

设置 `alphabetical: false`，并自定义 `force_override`。

未列入列表的类别会按字母顺序附加到已列出类别的末尾（如果 `alphabetical: true`）。

```yaml
order:
  alphabetical: true
  force_override:
    enabled: true
    list:
      - armors
      - swords
      - blocks
      - minerals
```

### 自定义 `all` 类别的位置

只需将 `all` 类别添加到列表中，即可使其成为第一个类别

```yaml
order:
  alphabetical: true
  force_override:
    enabled: true
    list:
      - all
      - armors
      - swords
      - blocks
      - minerals
```
