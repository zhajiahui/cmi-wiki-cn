---
title: "禁用方块"
source_url: "https://wiki.itemsadder.com/faq/disable-blocks"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 禁用方块

## 完全禁用方块

需要 ItemsAdder 4.0.13+

如果不使用自定义方块，可以通过禁用它们来优化插件。

```yaml
blocks:
  custom:
    note: false
    mushroom: false
    chorus: false
    wire: false
    fire: false
  worlds: []
```

同时删除每个世界中的 `itemsadder` 文件夹（以防万一，操作前先<mark style="color:orange;">备份</mark>）。
