---
title: Wait
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Wait
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Wait {#wait}

## 说明 {#description}

暂停元技能（如[延迟](delay.md)机制），直到满足一组条件。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| conditions | cond, c, until | 要检查的条件。满足条件后，元技能会继续执行 |  |
| interval | i | 技能机制检查条件的间隔，以刻为单位 | 1 |
| timeout | timeouttime, tt | 最多等待多少刻；超时后即使条件未满足，也会解除元技能的暂停状态 | 200 |
| cancelSkill | cancel, cs | 超时后是否取消执行元技能，而不是继续执行 | false |
| cancelConditions | cc, unless | 一组条件；满足时会立即结束等待并继续执行元技能，效果与满足主要 `conditions` 相同 |  |

## 示例 {#examples}

```yaml
GroundSlam:
  Skills:
  - jump{v=5}
  - delay 5
  - wait{cond=[ - onground ];tt=300}
  - explode
```
