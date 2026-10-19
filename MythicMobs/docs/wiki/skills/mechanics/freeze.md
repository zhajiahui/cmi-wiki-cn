---
title: Freeze
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/freeze
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Freeze {#freeze}

## 说明 {#description}

设置陷入细雪后的冰冻游戏刻数。玩家最多为 140 游戏刻。需要 1.17。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| ticks | t, duration, d | 在细雪中被冻结的刻数。 | 60 |

## 示例 {#examples}

将使用此技能的生物正在攻击的实体冻结100游戏刻（5秒）。

```yaml
  Skills:
  - freeze{ticks=100} @trigger ~onAttack
```

由于游戏处理冻结状态的方式，上述方法可能不起作用。如果发生这种情况，仍然可以执行以下操作

```yaml
#Inline version for premium users
Freeze_CauseFreezeEffect_Inline:
  Skills:
  - aura{d=100;i=1;onTick=[  - freeze{ticks=280} - damage{a=1;cd=2;damagecause=FREEZE} ]} @self

#Normal version
Freeze_CauseFreezeEffect_Normal:
  Skills:
  - aura{d=100;i=1;onTick=Freeze_CauseFreezeEffect_Normal_onTick} @self
Freeze_CauseFreezeEffect_Normal_onTick:
  Skills:
  - freeze{ticks=280}
  - damage{a=1;cd=2;damagecause=FREEZE}
```
