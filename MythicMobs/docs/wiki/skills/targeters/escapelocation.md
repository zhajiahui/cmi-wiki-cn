---
title: Escape Location
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EscapeLocation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Escape Location {#escape-location}

## 说明 {#description}

选中附近的安全逃离位置，方式类似于末影人选择传送目的地

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 随机搜索传送目的地时，相对于施法者的最大水平偏移和竖直偏移。 | 32 |
| iterations | i | 插件尝试寻找合适传送目的地的次数。 | 64 |
| height | h | 目的地竖直方向必须存在的空气方块数量，以保证有足够空间安全容纳实体。 | 3 |

## 示例 {#examples}

```yaml
  Skills:
  - teleport @escapelocation{radius=32;iterations=64;height=3}
```

## 别名 {#aliases}

- EndermanTeleport
