---
title: "TrMenu"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/trmenu"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# TrMenu

### 下载插件


### 在 GUI 中使用 ItemsAdder 物品


```yaml
material: 'source:ITEMADDER:itemId'
material: 'source:IA:anotherItemId'
```

### 如何重绘 GUI

```yaml
Title: '%img_offset_-16%%img_blank_menu%'
```

需要 PlaceholderAPI！

简单来说，`%img_offset_-16%` 用于将纹理 `%img_blank_menu%` 向后移动 **16** 像素。