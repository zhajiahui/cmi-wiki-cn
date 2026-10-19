---
title: "Graves"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/graves"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# Graves

## [在此下载 Graves Legacy](https://www.spigotmc.org/resources/graves.74208/)

## [在此下载 GravesX](https://www.spigotmc.org/resources/gravesx.118271/)

## 如何添加兼容？

> \[!NOTE] Graves 配置位于 `/plugins/Graves`，GravesX 配置位于 `/plugins/GravesX`。除插件名称不同外，两者的文件结构相同。

在 config/config.yml 中启用兼容功能

```yaml
itemsadder: # https://www.spigotmc.org/resources/itemsadder.73355/
  enabled: true # Should ItemsAdder integration be enabled.
```

编辑 config/grave.yml 中的默认选项。也可以按需自定义物品，但必须使用正确类型：家具属性使用家具，方块属性使用方块。

```yaml
  ##############
  # ItemsAdder #
  ##############
  # The option requires ItemsAdder, you must have this installed to use models.
  itemsadder:
    furniture:
      enabled: true # Should we use ItemsAdder Furniture?
      name: "itemsadder:mysterious_stone" # Furniture name.
    block:
      enabled: true # Should we use ItemsAdder Blocks?
      name: "itemsadder:nice_stone" # Block name
```
