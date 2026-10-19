---
title: "物品模型定义（ItemsAdderAdditions）"
source_url: "https://wiki.itemsadder.com/adding-content/items/item-model-definitions"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 物品模型定义（ItemsAdderAdditions）

物品模型定义功能由 [ItemsAdderAdditions](https://itemsadderadditions.com/en/docs/item-model-definitions) 提供。

物品模型定义是 Minecraft 1.21.4 引入的原版资源包文件，用于把物品映射到模型，并根据物品状态选择模型。IAA 会读取自定义物品中的 YAML 配置段，生成这些 JSON 文件并写入资源包。

```yaml
items:
  my_item:
    item_model_definition:
      model:
        type: model
        model: my_pack:item/my_item
```

需要 **1.21.4 或更高**版本服务端。旧版会忽略该配置段并在控制台警告。执行 `/iazip` 重新生成资源包。

完整文档见[此处](https://itemsadderadditions.com/en/docs/item-model-definitions)。
