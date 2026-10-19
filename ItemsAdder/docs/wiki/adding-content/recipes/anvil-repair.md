---
title: "铁砧修复"
source_url: "https://wiki.itemsadder.com/adding-content/recipes/anvil-repair"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 铁砧修复

## 示例

该配方允许你的玩家在铁砧上使用材料修复物品。

```yaml
recipes:
  anvil_repair:
    emerald_sword:
      enabled: true
      permission: iasurvival.swords.emerald_sword
      ingredient: EMERALD_BLOCK
      item: iasurvival:emerald_sword
```

本例创建了 `anvil_repair` 配方，名为 `emerald_sword`。
