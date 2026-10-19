---
title: "EpicBackpacks"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/epicbackpacks"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# EpicBackpacks

## [此处下载](https://www.spigotmc.org/resources/%E2%9C%85must-have%E2%9C%85-epic-backpacks.28981/)

你必须安装 [DefaultPack](../../plugin-usage/first-install.md)！

为创建使用 ItemsAdder 材质的背包，你需要打开 backpacks.yml（在EpicBackpacks文件夹中）并添加如下内容（每个背包都需要）：

```yaml
 cool_backpack:
    display_name: '&fCool Backpack'
    item:
      type: ITEMSADDER_ITEM
      name: "iageneric:plastic_bag"
    size: 3
    craft_recipe:
      pattern:
        - XXX
        - LCL
        - XLX
      ingredients:
        L: LEATHER
        C: CHEST
```
