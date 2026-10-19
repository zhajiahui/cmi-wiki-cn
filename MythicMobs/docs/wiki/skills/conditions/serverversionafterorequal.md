---
title: Server Version After Or Equal
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ServerVersionAfterOrEqual
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Server Version After Or Equal {#server-version-after-or-equal}

## 说明 {#description}

检查服务器版本是否晚于或等于特定版本

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| version | v, sv | 用于检查的版本。 | 1.19.3 |
| inclusive | i | 此条件是否检查当前版本与指定版本完全相同。 | true |

## 示例 {#examples}

```yaml
  Conditions:
  - serverAfter{version=1.21.1} false
  Skills:
  - message{m="Ngl y'all gotta update"} @world
```

## 别名 {#aliases}

- serverAfterEq
- serverAfter
- versionAfterEq
- versionAfter
