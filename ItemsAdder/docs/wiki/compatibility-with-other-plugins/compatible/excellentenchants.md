---
title: "ExcellentEnchants"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/excellentenchants"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# ExcellentEnchants

[此处下载](https://www.spigotmc.org/resources/goldenenchants-%E2%80%A2-more-vanilla-like-enchantments-1-14-1-16.61693/)

（曾用名 **GoldenEnchants**）

## 如何使用附魔

这是 ItemsAdder 自定义物品附魔的配置示例。

警告：附魔不会显示在物品描述中，这是另一个插件的“问题”。

<mark style="color:green;">附魔仍会生效！</mark>

因此应自行编写物品描述。

```yaml
  ruby_pickaxe:
    display_name: display-name-ruby_pickaxe
    permission: ruby_pickaxe
    resource:
      material: DIAMOND_PICKAXE
      generate: true
      textures:
      - item/ruby_pickaxe.png
    enchants:
    - tunnel:1
```

本例中，我设置了等级为 1 的 `tunnel` 附魔。

你可能还需要指定附魔的命名空间。它应该是 `excellentenchants`。\
例如：`excellentenchants:tunnel:1`。

请参考插件教程：


