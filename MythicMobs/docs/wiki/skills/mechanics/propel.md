---
title: Propel
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/propel
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Propel {#propel}

## 说明 {#description}

将此机制的施法者推向目标。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| velocity | magnitude, v | 生物被推动的速度 | 1 |

## 示例 {#examples}

如果伤害者距离超过 6 格，则将施法者推向伤害者。

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - propel{v=1;delay=1} @trigger ~onDamaged ?~distance{d=>6}
```
