---
title: "组件（ItemsAdderAdditions）"
source_url: "https://wiki.itemsadder.com/adding-content/items/item-properties/components"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 组件（ItemsAdderAdditions）

自定义物品中的 Minecraft 数据组件由 [ItemsAdderAdditions](https://itemsadderadditions.com/en/docs/components) 提供。

在物品定义中添加 `components` 段，然后执行 `/iazip`。IAA 通过 ItemsAdder 的物品修改器钩子，在资源包生成时应用组件。

```yaml
items:
  my_item:
    components:
      rarity: RARE
      use_cooldown:
        cooldown: 1.5
```

ItemsAdder 重建资源包／物品数据时才会应用组件。修改组件 YAML 后需执行 `/iazip`。通用 NMS 组件需要 **1.21.3 或更高**版本服务端。

完整文档见[此处](https://itemsadderadditions.com/en/docs/components)。
