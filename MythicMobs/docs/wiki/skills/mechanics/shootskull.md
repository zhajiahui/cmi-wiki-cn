---
title: Shootskull
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shootskull
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Shootskull {#shootskull}

## 说明 {#description}

将凋灵头骨从生物中射向目标实体或位置。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| yield | strength, y, s | 头颅爆炸的威力。 | 1 |
| playsound | ps | 头颅创建时是否播放发射音效 | false |

## 示例 {#examples}

此示例将向目标发射一连串快速移动的 3 凋灵头骨。

```yaml
SkullBarrage:
  Skills:
  - shootskull{y=1;v=4} @target
  - delay 10
  - shootskull{y=1;v=4} @target
  - delay 10
  - shootskull{y=1;v=4} @target
```

## 别名 {#aliases}

- shootwitherskull
- skull
- witherskull
