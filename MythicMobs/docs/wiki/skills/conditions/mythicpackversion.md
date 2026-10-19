---
title: Mythic Pack Version
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/MythicPackVersion
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mythic Pack Version {#mythic-pack-version}

## 说明 {#description}

检查指定版本的服务器上是否存在指定id的[Pack](../../packs.md)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| packid | pack, id, p | 要检查的包 ID。 |  |
| packversion | packV, version, v | 要检查的版本。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - packversion{p="ThePackId",v="1.2.3"} true
```

## 别名 {#aliases}

- packversion
- packversionis
