---
title: Geyser
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/geyser
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Geyser {#geyser}

## 说明 {#description}

使液体间歇泉从目标实体或位置的地面喷出。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t | 液体类型，可以为“WATER”或“LAVA”。 | WATER |
| height | h | 喷泉的高度。即使指定了其他值，也会被设为*至少* 1。 | 3 |
| interval | i, speed, s | 喷泉动画各次迭代之间的间隔，单位为刻。 | 10 |
| audience |  | 效果的[可见对象](../audience.md)。 | nearby |

## 示例 {#examples}

```yaml
GeyserSkill:
  Skills:
  - geyser{type=LAVA;height=3;speed=10} @selflocation
```

## 别名 {#aliases}

- effect:geyser
- e:geyser
