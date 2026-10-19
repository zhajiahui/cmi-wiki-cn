---
title: Set Raider Can Join Raid
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/setRaiderCanJoinRaid
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Set Raider Can Join Raid {#set-raider-can-join-raid}

## 说明 {#description}

设置目标袭击者实体是否可以加入袭击

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bool | b, can, c | 实体是否可以加入袭击 | true |

## 示例 {#examples}

```yaml
  Skills:
  - setRaiderCanJoinRaid{c=false} @self
```

## 别名 {#aliases}

- setCanJoinRaid
