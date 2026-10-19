---
title: Setgliding
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setgliding
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setgliding {#setgliding}

## 说明 {#description}

使配备鞘翅的实体滑翔或停止滑翔。这仅适用于在胸甲插槽中装备了鞘翅的玩家或实体。目标实体当时也必须在空中！

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| gliding | g | 是否强制实体滑翔 | true |

## 示例 {#examples}

如果生物装备了鞘翅并且当时在空中，这个例子将使生物滑翔。

```yaml
MakeMobGlide:
  Skills:
  - setgliding{g=true} @self
```
