---
title: Playerkills
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/playerkills
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Playerkills {#playerkills}

## 说明 {#description}

匹配目标生物杀死的玩家数量。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| kills | k | 要匹配的数值范围。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - playerkills{k=>10} true
```
