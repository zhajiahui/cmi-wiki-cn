---
title: "收纳袋"
source_url: "https://wiki.itemsadder.com/adding-content/items/other-items-examples/bundle"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 收纳袋

## 配置

```yaml
items:
  example_bundle:
    display_name: "&6&lExample Bundle"
    permission: example_bundle
    resource:
      material: BUNDLE
      generate: true
      textures:
      - item/bundle_test.png
```

<div align="left"><img src="../../../assets/e138e104380a81c2e7ee.png" alt=""></div>

需要额外创建带 `_filled` 后缀的文件，本例为 `bundle_test_filled.png`。

## 效果

![](../../../assets/c9f250c908f7228ff28f.png)
