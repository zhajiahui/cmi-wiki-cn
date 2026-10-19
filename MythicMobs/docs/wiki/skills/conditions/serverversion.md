---
title: Server Version
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ServerVersion
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Server Version {#server-version}

## 说明 {#description}

检查服务器是否正在运行特定的minecraft版本

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| version | sv, v | 要检查的版本。 | 1.19.3 |

## 示例 {#examples}

```yaml
  Conditions:
  - serverversion{v="v1.19.4"} true
```

## 别名 {#aliases}

- server
- version
