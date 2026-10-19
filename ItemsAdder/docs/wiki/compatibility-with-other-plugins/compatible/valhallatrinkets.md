---
title: "ValhallaTrinkets"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/valhallatrinkets"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# ValhallaTrinkets

### [此处下载](https://www.spigotmc.org/resources/valhallatrinkets.115790/)

通过 [ItemsAdderAdditions](https://itemsadderadditions.com/en/docs/compatibility/valhalla) 可兼容 ValhallaTrinkets。

ItemsAdderAdditions 可在创建 ItemsAdder 物品堆时，将 ValhallaTrinkets 元数据写入其中。在 ItemsAdder 物品的 `valhalla` 部分下的 `trinkets` 键中配置。

```yaml
items:
  amulet:
    display_name: "<gold>Amulet"
    valhalla:
      trinkets:
        trinket_id: 1001
        trinket_unique_id: 1001
        unique: true
        unstackable: true
```

元数据会直接写入物品堆。要在游戏中产生效果，服务器上必须安装 ValhallaTrinkets。

完整文档见[此处](https://itemsadderadditions.com/en/docs/compatibility/valhalla)。
