---
title: "ValhallaMMO"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/valhallammo"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# ValhallaMMO

### [此处下载](https://www.spigotmc.org/resources/valhallammo.99843/)

通过 [ItemsAdderAdditions](https://itemsadderadditions.com/en/docs/compatibility/valhalla) 可兼容 ValhallaMMO。

ItemsAdderAdditions 可在创建 ItemsAdder 物品堆时，将 ValhallaMMO 持久数据写入其中。在 ItemsAdder 物品的 `valhalla` 部分下配置属性、装备类别、物品标志和永久效果。

```yaml
items:
  ruby_sword:
    display_name: "<red>Ruby Sword"
    valhalla:
      equipment_class: SWORD
      item_flags:
        - DISPLAY_ATTRIBUTES
      stats:
        - stat: DAMAGE_BASE
          amount: 4.0
          operation: ADD_NUMBER
```

元数据会直接写入物品堆。要在游戏中产生效果，服务器上必须安装 ValhallaMMO。

完整文档见[此处](https://itemsadderadditions.com/en/docs/compatibility/valhalla)。
