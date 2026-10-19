---
title: Feed
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/feed
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Feed {#feed}

## 说明 {#description}

喂食目标玩家。   对其他生物不起作用。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要恢复的饥饿值。 | 1 |
| saturation | s | 要恢复的饱和度。 | 0 |
| overfeed | o,of | 是否允许过量喂食。 | false |

## Amount 属性 {#amount-attribute}

数量 1 表示半格饥饿值。允许过量喂食时，多余食物会转化为饱和度。也可以使用负值减少饥饿值。

## 示例 {#examples}

此技能恢复玩家 10 点饥饿值，即 5 个鸡腿图标。

```yaml
  Skills:
  - feed{amount=10} @trigger ~onInteract
```
