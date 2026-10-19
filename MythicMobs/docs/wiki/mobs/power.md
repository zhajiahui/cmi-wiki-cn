---
title: 强度
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/Power
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 强度

# Power {#power}

**技能强度**

技能强度是所有技能都可使用的属性，用于提高技能效果。生物配置中的基础属性不受影响。它主要用于随生物等级提升技能强度，而且只能通过[等级修正](levels.md)设置。部分技能机制的某些属性会乘以技能强度。

未来版本会允许设置缩放系数。目前除 [Projectile](../skills/mechanics/projectile.md) 和 [Missile](../skills/mechanics/missile.md) 外，其他技能机制无法关闭技能强度的影响。不想使用技能强度时，不要在等级修正中设置它。

受技能强度影响的机制及计算公式：

| 技能机制 | 参数 | 强度等级效果 |
| --- | --- | --- |
| [basedamage](../skills/mechanics/basedamage.md) | {multiplier=M} | damage = M * power |
| [consume](../skills/mechanics/consume.md) | {damage=D} | damage = D * power |
| [consume](../skills/mechanics/consume.md) | {heal=H} | heal = H * power |
| [damage](../skills/mechanics/damage.md) | {amount=A} | damage = A * power |
| [leap](../skills/mechanics/leap.md) | {velocity=V} | velocity = V * ( 1 + power * 0.1 ) |
| [projectile](../skills/mechanics/projectile.md) | {velocity=V} | velocity = V * power |
| [projectile](../skills/mechanics/projectile.md) | {maxrange=MR} | maxrange = MR * power |
| [missile](../skills/mechanics/missile.md) | {velocity=V} | velocity = V * power |
| [missile](../skills/mechanics/missile.md) | {maxrange=MR} | maxrange = MR * power |

**示例**

```
ThornySkeleton:
  Type: SKELETON
  Health: 20
  LevelModifiers:
    Health: 10
    Power: 1
  Skills:
  - damage{amount=5} @trigger ~onDamaged
```

本例中，等级 2 的 ThornySkeleton 的技能强度为 2，由基础值 1 加上 LevelModifiers 的 +1 得到。伤害量会乘以技能强度，因此技能造成 10 点伤害。等级 3 时，技能强度为 3，造成 15 点伤害，以此类推。
