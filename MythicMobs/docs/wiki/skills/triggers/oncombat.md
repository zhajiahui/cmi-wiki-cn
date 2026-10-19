---
title: On Combat
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCombat
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Combat {#on-combat}

## 说明 {#description}

未指定触发器时使用的默认触发器，会在以下事件发生时执行：

- 生物造成伤害
- 生物受到伤害
- 生物生成
- 生物死亡

## 示例 {#examples}

```yml
SkeletalWarrior:
  Mobtype: skeleton
  Display: '<blue>A Skeletal Warrior</blue>'
  Skills:
  - skill{s=Bash} =10%-90%
```
