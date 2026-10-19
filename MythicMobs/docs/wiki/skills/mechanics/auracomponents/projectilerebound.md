---
title: Projectile Rebound
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/ProjectileRebound
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Projectile Rebound {#projectile-rebound}

## 说明 {#description}

应用一个[光环](../aura.md)，将传入的弹射物从光环持有者处反弹开，可以选择将它们发送回发射它们的人身上。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onReboundSkill | onrebound, orb, onreflect, ondeflect | 每次弹射物被反弹时执行的技能。 |  |
| returnMode | mode | 反弹后弹射物的瞄准方式：`ORIGINAL_CASTER` 将其反弹给发射者，`MIRROR` 则像镜面一样反射。 | ORIGINAL_CASTER |
| reparseFaction | reparse, rf, changeshooter, cs | 将反弹后弹射物的发射者重新指定为光环持有者，以便重新评估阵营和目标选择。 | true |
| cancelIncoming | cancelhit, cancel, cancelevent, ce | 取消原本传入的弹射物命中事件。 | true |
| vanillaProjectiles | vanilla, vp | 是否反弹原版弹射物。 | true |
| mythicProjectiles | mythic, mp | 是否反弹 Mythic 弹射物。 | true |
| speedFactor | speed, sf | 应用于反弹后弹射物速度的倍率。 | 1.0 |
| powerFactor | power, pf | 应用于反弹后弹射物威力的倍率。 | 1.0 |
| reboundDistance | distance, offset, push | 生成反弹弹射物的位置与光环持有者之间的距离。 | 0.6 |
| maxRebounds | max, mr | 单个弹射物可被反弹的最大次数。 | 1 |
| reboundConditions | conditions, cond, c | 弹射物反弹前检查的[条件](../../conditions.md)。 |  |

## 别名： {#aliases}

- projectilereflect
- reboundprojectiles
- reboundingprojectiles
