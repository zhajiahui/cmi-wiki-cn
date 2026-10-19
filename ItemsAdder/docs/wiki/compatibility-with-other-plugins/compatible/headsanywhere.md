---
title: "HeadsAnywhere 兼容"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/headsanywhere"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# HeadsAnywhere 兼容

如何使用 HeadsAnywhere 插件在聊天、告示牌、书籍等位置显示玩家头颅。

## [此处下载](https://www.spigotmc.org/resources/headsanywhere-use-players-heads-anywhere.109951/)

HeadsAnywhere 插件可将玩家头颅作为聊天中的字符，方便你在游戏中的各处使用和显示玩家头颅。

它兼容 ItemsAdder，也允许你使用自定义玩家头颅。

要使用自定义玩家头颅，需要在其 config.yml 中禁用资源包，并将其资源包与 ItemsAdder 的资源包合并。

编辑其 default.json，以获得更准确的头颅偏移位置

```json
{
  "providers": [
    {
      "type": "ttf",
      "file": "minecraft:headsanywhere.ttf",
			"shift": [-2, 2],
			"size": 11.0,
			"oversample": 2.0,
			"skip": ""
    }
  ]
}
```