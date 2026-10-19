---
title: "ItemBridge"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/itembridge"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# ItemBridge

## [此处下载](https://www.spigotmc.org/resources/77080/)

## 使用 ItemBridge 获取 ItemsAdder 物品

要使用 **Mimic** 获取自定义物品，必须执行以下命令：

`/ib get`` `<mark style="color:blue;">`ia:<item namespaced id>`</mark>

`/ib give <player>`` `<mark style="color:blue;">`ia:<item namespaced id>`</mark>

`/ib drop <world> <x> <y> <z>`` `<mark style="color:blue;">`ia:<item namespaced id>`</mark>` ``[amount]`

### 示例

`/ib give LoneDev ia:itemsadder:ruby_sword`

在 ItemsAdder 物品前添加 `ia:` 非常重要，否则 **ItemBridge** 无法识别。

本例中 `itemsadder:ruby_sword` 必须为 `ia:itemsadder:ruby_sword`。



