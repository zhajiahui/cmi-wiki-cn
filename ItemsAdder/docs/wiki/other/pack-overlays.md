---
title: "资源包覆盖层"
source_url: "https://wiki.itemsadder.com/other/pack-overlays"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 资源包覆盖层

此功能面向熟悉资源包制作的作者。

ItemsAdder 支持原版覆盖层。

可以自行创建 `pack.mcmeta`，并在其中添加 `overlays` 条目。\
ItemsAdder 会将其全部合并到资源包 `.zip` 文件最终生成的 **pack.mcmeta** 中。

#### Minecraft Wiki 资料


#### 各 Minecraft 版本对应的资源包格式版本


### 示例

`contents/myassets/resourcepack/assets/minecraft/pack.mcmeta`

```json
{
   "pack":{
      "pack_format":63,
      "description":"My Pack"
   },
   "overlays":{
      "entries":[
         {
            "directory":"my_overlay_1",
            "formats":[
               42,
               43
            ]
         },
         {
            "directory":"my_overlay_3",
            "formats":[
               44,
               47
            ]
         }
      ]
   }
}
```
