---
title: Mythic Pack Version Greater
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/MythicPackVersionGreater
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mythic Pack Version Greater {#mythic-pack-version-greater}

## 说明 {#description}

检查服务器上是否存在具有指定 ID 的 [Pack](../../packs.md)，其版本大于或等于指定版本。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| packid | pack, id, p | 要检查的包 ID。 |  |
| packversion | packV, version, v | 要检查的版本。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - packversiongreater{p="ThePackId";v="1.2.3"} true
```

## 别名 {#aliases}

- packversiongreater
- packversionisgreater
