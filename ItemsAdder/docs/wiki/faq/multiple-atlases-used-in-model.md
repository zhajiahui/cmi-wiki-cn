---
title: "1.21.11 - 模型使用了多个纹理图集（Multiple atlases used in model）"
source_url: "https://wiki.itemsadder.com/faq/multiple-atlases-used-in-model"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 1.21.11 - 模型使用了多个纹理图集（Multiple atlases used in model）

此问题发生在 1.21.11+ 客户端

`[Worker-Main-108/WARN]: Unable to bake item model: 'minecraft:netherite_sword'`

`java.lang.IllegalStateException: Multiple atlases used in model, expected minecraft:textures/atlas/blocks.png, but also got minecraft:textures/atlas/items.png`

## 如何修复

将模型名称（本例中为 `netherite_sword`）添加到 `config.yml` 中，然后重新生成资源包。

```yml
      fix_1_21_11_plus_atlas_items_models:
        enabled: true
        models:
          - "paper"
          - "potion"
          - "netherite_sword"
```

另一种解决办法是确保同一模型不混用方块纹理和物品纹理。
