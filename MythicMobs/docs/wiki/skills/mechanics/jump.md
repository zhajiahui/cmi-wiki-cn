---
title: Jump
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/jump
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Jump {#jump}

## 说明 {#description}

使生物以给定的速度跳跃。使用速度 *0.75* 将使生物跳跃大约 1 方块高。也可以是负数。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| velocity | v | 生物跳跃的速度。 | 1 |

## 示例 {#examples}

```yaml
SuperJump:
  Skills:
  - jump{velocity=20}
```
