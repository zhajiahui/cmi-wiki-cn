---
title: "透明方块"
source_url: "https://wiki.itemsadder.com/adding-content/blocks/transparent-block"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 透明方块

<div><figure><img src="../../assets/ca47f9a9b15cbc98001d.png" alt=""><figcaption></figcaption></figure></div>

要创建一个透明方块，你需要使用 `REAL_TRANSPARENT` 方块模型类型。

```yaml
info:
  namespace: test_transparent
items:
  test_block_transparent:
    enabled: true
    display_name: test_block_transparent
    resource:
      generate: true
      textures:
        - test
      material: PAPER
    behaviours:
      block:
        placed_model:
          type: REAL_TRANSPARENT
        cancel_drop: false
```

