---
title: "家具权限"
source_url: "https://wiki.itemsadder.com/adding-content/furnitures/furniture-permissions"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 家具权限

此属性允许您为家具放置和家具破坏事件启用权限。\
默认情况下未指定此设置，因为我们希望玩家能够自由地破坏和放置家具。\
指定这些属性后，玩家需要明确授予相应权限：

* `ia.user.furniture.break.iasurvival.my_furniture`
* `ia.user.furniture.place.iasurvival.my_furniture`

```yaml
    behaviours:
      furniture:
        permission_suffix:
          break: iasurvival.my_furniture
          place: iasurvival.my_furniture
```
