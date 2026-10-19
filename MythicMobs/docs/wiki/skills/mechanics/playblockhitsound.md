---
title: Play Block Hit Sound
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PlayBlockHitSound
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Play Block Hit Sound {#play-block-hit-sound}

## 说明 {#description}

播放目标块的撞击（损坏）声音。

> **这是一个[仅支持 Paper](https://papermc.io/downloads/all)机制！**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| pitch | p | 声音的音高，范围为 0.01 到 2.0。 | 1.0 |
| volume | v | 声音的音量。 | 1.0 |

### Volume 属性 {#volume-attribute}

“音量”属性并不定义声音响度的百分比，而是确定在最大音量下可以听到声音的距离（以块为单位）。

其公式为`v * 16 = max volume distance`。例如，如果你使用“1”作为音量属性，则可以在源周围 16 块半径内以最大音量听到声音。然而，如果你使用“20”，则可以在320方块半径内以最大音量听到声音！ (20 * 16)

## 示例 {#example}

```yaml
  Skills:
  - blockhitsound @targetlocation
```

## 别名 {#aliases}

- blockhitsound
