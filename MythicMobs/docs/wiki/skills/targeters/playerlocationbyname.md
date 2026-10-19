---
title: Player Location By Name
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayerLocationByName
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Player Location By Name {#player-location-by-name}

## 说明 {#description}

通过名字定位特定玩家的位置。可以是占位符。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| name | n | 玩家名称。 | CarsonJF |

## 示例 {#examples}

```yaml
  Skills:
  - setblocktype{m=LAVA} @PlayerLocationByName{name=Lxlp}
```

## 别名 {#aliases}

- specificplayerlocation
