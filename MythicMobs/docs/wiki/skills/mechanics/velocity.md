---
title: Velocity
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/velocity
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Velocity {#velocity}

## 说明 {#description}

修改目标实体的速度，也适用于玩家，可用于真正的（  true  ）击退抗性、力量技能或模拟风等效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| mode | m | 要执行的运算。可设为 SET、ADD、REMOVE、DIVIDE 或 MULTIPLY。 | SET |
| velocityx | vx, x | x 轴上的速度，可以为负数。 | 1 |
| velocityy | vy, y | y 轴上的速度，可以为负数。 | 1 |
| velocityz | vz, z | z 轴上的速度，可以为负数。 | 1 |
| relative | r | 速度变化是否相对于目标的朝向。此时，`z` 轴表示前后方向（`forward/backward`），`y` 轴表示上下方向（`up/down`），`x` 轴表示左右方向（`left/right`） | false |

## 示例 {#examples}

此示例将在受到伤害时停止施法生物的所有动力。该效果只会持续到生物决定再次移动或被其他来源移动为止。

```yaml
internal_mobname:
  Type: Zombie
  Skills:
  - velocity{m=set;x=0;y=0;z=0} @self ~onDamaged
```

##  {#section}

上例在大多数情况下有效，但弓的 ARROW_KNOCKBACK 附魔仍可移动实体。可以稍作如下修改来阻止。

```yaml
internal_mobname:
  Type: Zombie
  Skills:
  - velocity{m=set;x=0;y=0;z=0;delay=1} @self ~onDamaged
```
