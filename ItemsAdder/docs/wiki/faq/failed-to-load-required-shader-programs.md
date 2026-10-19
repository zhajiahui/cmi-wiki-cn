---
title: "无法加载所需的着色器程序（Failed to load required shader programs）"
source_url: "https://wiki.itemsadder.com/faq/failed-to-load-required-shader-programs"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 无法加载所需的着色器程序（Failed to load required shader programs）

`Caught error loading resourcepacks, removing all selected resourcepacks java.util.concurrent.CompletionException: java.lang.RuntimeException: Failed to load required shader programs:`

* `minecraft:core/rendertype_armor_cutout_no_cull (VertexFormat[Position, Color, UV0, UV1, UV2, Normal]): Could not find shader: minecraft:rendertype_armor_cutout_no_cull (VERTEX)`
* `minecraft:core/rendertype_text (VertexFormat[Position, Color, UV0, UV2]): Could not find shader: minecraft:rendertype_text (VERTEX)`

## 为什么会发生？

这是因为 Minecraft 1.21.2 更改了着色器 `.vsh` 和 `.fsh` 文件的存放位置。

默认着色器路径已从 `assets/minecraft/shaders/core/<name>.vsh` 改为 `assets/minecraft/shaders/<name>.vsh`。

因此，`core` 文件夹不再是必需的，游戏也不会自动将其纳入考虑。

要修复此问题，必须打开 `core` 文件夹中每个自定义着色器的 `.json` 文件，并更新 `vertex` 和 `fragment` 路径，以 `core/` 作为文件夹前缀。

在最终的 `.zip` 文件中，覆盖层文件夹名为 `ia_overlay_1_21_2`。

## 自动修复方法

ItemsAdder 提供了一个设置，可自动修复这些着色器。

它会自动更新 `.json` 文件，并创建覆盖层，使旧客户端仍能识别旧格式，新客户端（1.21.2+）也能识别旧格式。

这需要运行 `/iazip` 重新生成资源包。

```yaml
pre_1_21_2_shaders_fix:
  enabled: true
```
