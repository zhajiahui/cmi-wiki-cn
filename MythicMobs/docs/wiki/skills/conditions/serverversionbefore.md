---
title: Server Version Before
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ServerVersionBefore
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Server Version Before {#server-version-before}

## 说明 {#description}

检查服务器是否为特定版本之前

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| version | v, sv | 用于检查的版本。 | 1.19.3 |
| inclusive | i | 此条件是否检查当前版本与指定版本完全相同。 | true |

## 示例 {#examples}

```yaml
  Conditions:
  - serverBefore{version=1.21.1}
  Skills:
  - message{m="Ngl y'all gotta update"} @world
```

## 别名 {#aliases}

- serverBefore
- versionBefore
