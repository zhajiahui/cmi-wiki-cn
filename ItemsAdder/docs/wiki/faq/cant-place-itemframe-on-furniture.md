---
title: "无法在家具上放置物品展示框"
source_url: "https://wiki.itemsadder.com/faq/cant-place-itemframe-on-furniture"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 无法在家具上放置物品展示框


这是 Minecraft 的行为：游戏会强制移除位于另一个实体内部的物品展示框，此处另一个实体就是家具所用的物品展示框。

### 解决方法

将家具物品展示框的高度降低 `0.1`。\
例如 `1` -> `0.9`, `2` -> `1.9` 等。

```yaml
        hitbox:
          length: 1
          width: 1
          height: 1.9
```
