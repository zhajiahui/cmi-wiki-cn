---
title: Set Custom Menu Button
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SetCustomMenuButton
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Set Custom Menu Button {#set-custom-menu-button}

## 说明 {#description}

将打开的[自定义菜单](../../custom-menus.md)的特定槽位设置为指定按钮。   只要玩家打开了[自定义菜单](../../custom-menus.md)，即使它不是从菜单本身中投射的，它也会起作用。

> **此功能需要 [MythicMobs Premium](../../premium-features.md) 或 [MythicRPG](https://mythiccraft.io/index.php?resources/mythicrpg-spells-classes-professions-more.129/)！**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| slot | s | 要修改的槽位 | 0 |
| icon | i | 要在槽位上设置的按钮 | default |

## 示例 {#examples}

```yaml
MyCustomMenu:
  Display: "My Custom Menu"
  Size: 27
  Schema:
    - '0 0 0 0 0 0 0 0 0'
    - '0 0 0 0 B 0 0 0 0'
    - '0 0 0 0 0 0 0 0 0'
  Icons:
    TEST_BUTTON:
      Mapping: B
      Material: GOLD_INGOT
      Model: 4
      Display: 'Test'
      Skills:
      - setcustommenubutton{slot=11;icon=DYNAMIC_BUTTON}
    DYNAMIC_BUTTON:
      Material: IRON_SWORD
      Model: 100
```
