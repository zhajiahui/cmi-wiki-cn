---
title: Mythic Pack
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/MythicPack
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mythic Pack {#mythic-pack}

## 说明 {#description}

检查服务器上是否存在指定id的[Pack](../../packs.md)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| packid | pack, id, p | 要检查的包 ID。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - mythicpack{p="ThePackId"} true
```

## 别名 {#aliases}

- pack
- haspack
