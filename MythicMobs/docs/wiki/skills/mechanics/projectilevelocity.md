---
title: Projectile Velocity
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectileVelocity
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Projectile Velocity {#projectile-velocity}

## 说明 {#description}

修改调用的[弹射物](projectile.md)或[导弹](missile.md)的速度。在这种情况下，它的工作原理与[速度](velocity.md)机制相同。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| mode | m | 要执行的运算。可设为 SET、ADD、REMOVE、DIVIDE 或 MULTIPLY。 | SET |
| velocityx | vx, x | x 轴上的速度，可以为负数。 | 1 |
| velocityy | vy, y | y 轴上的速度，可以为负数。 | 1 |
| velocityz | vz, z | z 轴上的速度，可以为负数。 | 1 |
| relative | r | 速度变化是否相对于投射物的朝向。此时，`z` 轴表示前后方向（`forward/backward`），`y` 轴表示上下方向（`up/down`），`x` 轴表示左右方向（`left/right`） | true |

## 示例 {#examples}

```yaml
Projectile-onTick:
  Conditions:
  - chance{chance=0.1} true
  Skills:
  - projectilevelocity{mode=ADD;vz=0.3}
```

## 别名 {#aliases}

- pvelocity
