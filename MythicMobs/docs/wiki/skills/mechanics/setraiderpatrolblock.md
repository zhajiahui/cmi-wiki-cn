---
title: Setraiderpatrolblock
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setraiderpatrolblock
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setraiderpatrolblock {#setraiderpatrolblock}

## 说明 {#description}

使目标袭击者前往给定位置巡逻

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| location | block, l, b | 一个[位置目标选择器](../targeters.md#single-location-targeters)，以其选中的位置作为指定位置 |  |

## 示例 {#examples}

```yaml
  Skills:
  - setRaiderPatrolBlock{l=@TrackedLocation} @self
```

## 别名 {#aliases}

- setRaiderBlock
