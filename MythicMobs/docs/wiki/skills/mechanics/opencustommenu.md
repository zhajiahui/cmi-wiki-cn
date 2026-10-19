---
title: Open Custom Menu
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/OpenCustomMenu
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Open Custom Menu {#open-custom-menu}

## 说明 {#description}

打开[自定义菜单](../../custom-menus.md)

> **此功能需要 [MythicMobs Premium](../../premium-features.md) 或 [MythicRPG](https://mythiccraft.io/index.php?resources/mythicrpg-spells-classes-professions-more.129/)！**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| menu | m | 要打开的菜单。 | default |

## 示例 {#examples}

```yaml
  Skills:
  - opencustommenu{m=ExampleMenu} @trigger ~onInteract
```

## 别名 {#aliases}

- openMenu
