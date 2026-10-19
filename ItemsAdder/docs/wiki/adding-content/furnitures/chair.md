---
title: "椅子"
source_url: "https://wiki.itemsadder.com/adding-content/furnitures/chair"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 椅子

创建椅子时，按家具制作教程操作，再添加一个属性，使家具可供乘坐。

添加 `furniture_sit` 行为，并指定 `sit_height`。

```yaml
behaviours:
  furniture:
    # .....
  furniture_sit:
    sit_height: 0.5
```

### `sit_height`

乘坐位置的高度

### `opposite_direction`

默认：true。启用后，玩家坐上家具时旋转 180 度。

### `passenger_front_view_on_sit`

默认：true。玩家坐上家具时，转向家具正面。

### `passenger_rotate_body`

默认：false。玩家坐在家具上时旋转身体。
