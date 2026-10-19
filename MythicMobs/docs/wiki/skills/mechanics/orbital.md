---
title: Orbital
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/orbital
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Orbital {#orbital}

## 说明 {#description}

Orbital 发射绕目标环行的特殊[弹射物](projectile.md)，也可作为[光环](aura.md)，继承其全部属性。它会对运行轨道上命中的实体触发其他技能，适合制作火焰护盾等复杂技能，使用方式也比较复杂。

在 MM 4.11 中向轨道添加了弹射物子弹。请在[弹射物机制](projectile.md)页面查看如何使用它们。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onHit | oH, onhitskill | 弹射物命中其他对象时执行的元技能。元技能会继承被命中的目标。 |  |
| radius | r | 围绕目标运行的轨道半径。 | 4 |
| hitRadius | hr | 环绕弹射物周围可命中目标的半径。 | 1 |
| verticalHitRadius | vhr, vr | 命中半径的 y 分量。 | `hitradius` |
| points | p | 组成环绕轨道圆形的点数。点越多，圆形越精细，但完成一圈环绕所需的时间也越长。 | 32 |
| startingpoint | sp | 环绕弹射物光环的初始步数。 | 0 |
| tickinterpolation | interpolation, ti | 在弹射物相邻两次刻更新之间插入额外的点，并多次执行 onTick。 | 0 |
| rotationx | rotx, rx | 沿 X 轴旋转环绕轨道，单位为弧度。`3.14` 表示半圈，`6.28` 表示一整圈。 | 0 |
| rotationy | roty, ry | 沿 Y 轴旋转环绕轨道，单位为弧度。3.14 表示半圈，6.28 表示一整圈。 | 0 |
| rotationz | rotz, rz | 沿 Z 轴旋转环绕轨道，单位为弧度。3.14 表示半圈，6.28 表示一整圈。 | 0 |
| offsetx | ox, offx | 沿目标的 X 轴偏移环绕轨道。 | 0 |
| offsety | oy, offy | 沿目标的 Y 轴偏移环绕轨道。 | 0 |
| offsetz | oz, offz | 沿目标的 Z 轴偏移环绕轨道。 | 0 |
| angularVelocityX | avx, vx | 修改环绕轨道在 X 轴上的角速度。 | 0 |
| angularVelocityY | avy, vy | 修改环绕轨道在 Y 轴上的角速度。 | 0 |
| angularVelocityZ | avz, vz | 修改环绕轨道在 Z 轴上的角速度。 | 0 |
| rotate |  | 环绕轨道是否旋转。 | true |
| reversed | reverse, backwards | 环绕轨道是否反向旋转。 | false |
| hitPlayers | hp | 是否可以命中玩家。 | true |
| hitNonPlayers | hnp | 是否可以命中非玩家实体。 | false |
| hitSelf | hs | 是否可以命中施法者。 | false |
| hugsurface | hs | 环绕弹射物是否沿地面移动。 | false |
| hugliquid | hugwater, huglava | 使用 `hugSurface` 时，环绕弹射物是否也在液体表面移动。 | false |
| heightfromsurface | hfs | `HugSurface` 设为 `true` 时，环绕弹射物在表面上方滑行的高度。 | 0.5 |
| maxclimbheight | mch | 弹射物贴着方块或液体表面移动时，在自行终止前尝试每次将其 y 坐标**升高** 1 的次数。 | 3 |
| maxdropheight | mdh | 弹射物贴着方块或液体表面移动时，在自行终止前尝试每次将其 y 坐标**降低** 1 的次数。 | 10 |
| bullettype | bullet, b | [弹射物弹体类型](projectile.md#projectile-bullets)，也会使环绕弹射物继承所有相关属性。 | NONE |
| castAsOrbital | cao | 是否像弹射物一样，由环绕弹射物自身而非施法者施放元技能。 | false |
| immunedelay | immune, iD | 设置命中免疫间隔，即目标可以再次被弹射物命中前需等待的时间。 | 2000 |
| drawhitbox |  | 绘制环绕弹射物的碰撞箱，便于调试。 | false |
| hitconditions | conditions, cond, c | 目标必须满足这些条件，环绕弹射物才能命中它。**仅 Premium 版**机制。 |  |
| stopconditions | stpcond | 目标必须满足这些条件，环绕弹射物才会在命中它时结束。 |  |
| hitTargeter | htr | 实体目标选择器。环绕弹射物命中后，所选实体会成为 onHit 元技能的目标，并像环绕弹射物的主要目标一样获得命中免疫间隔。 |  |
| shareSubHitboxCooldown | shcd | 所有 meg 子碰撞箱是否与基础实体共用相同的命中免疫间隔。 | true |

> 该机制继承了[光环](aura.md)机制的所有属性

### onStart 属性 {#onstart-attribute}

onStart 技能以特殊方式发挥作用 - onStart 发射的任何有持续时间的增益或“特效”机制（例如 ParticleTornado）都会在其持续时间内附着在弹射物上，从而产生一些有趣的效果。

### onTick 属性 {#ontick-attribute}

使用 **@origin** 目标选择器将导致任何技能或效果瞄准弹射物的位置。这是配置弹射物外观的预期方法。

### onHit 属性 {#onhit-attribute}

弹射物击中的任何目标都会固有地传递给技能。你放入onHit技能中的任何目标都会“覆盖”这些并导致你的技能可能无法按你的预期发挥作用。

### onEnd 属性 {#onend-attribute}

弹丸末端的特效也使用**@origin**。另外，如果你希望以某种方式击中弹射物末端附近的实体（例如最终的大型火球爆炸），你可以使用 **@PlayersNearOrigin{r=[radius]}** 瞄准器。

## 示例 {#examples}

这个例子在生物有时被击中时会在其周围放置一个看起来冰冷的轨道护盾，该护盾将持续10秒或直到它被触发一次：

```yaml
# Mob File
Mob:
  Type: SKELETON
  Skills:
  - skill{s=IceShield} @self ~onDamaged 0.2
```

```yaml
# Skills File
IceShield:
  Skills:
  - orbital{onTick=IceShield-Tick;onHit=IceShield-Hit;points=20;interval=1;duration=200;charges=1}
IceShield-Tick:
  Skills:
  - effect:particles{p=snowballpoof;amount=20;speed=0;hS=0.2;vS=0.2} @origin
IceShield-Hit:
  Skills:
  - damage{a=10}
  - potion{type=SLOW;duration=100;lvl=2}
```

##  {#section}

此示例展示了如何通过 [Auraremove](auraremove.md) 机制移除轨道。
  
`ExampleMob` 受伤时，有 20% 的概率创建前例中的护盾。与前例不同，这次 orbital 还设置了 auraName。收到 REMOVESHIELD 信号时，通过 auraremove 和对应 auraName 移除 orbital，并向元技能的触发实体发送 SHIELDREMOVED 信号。

```yaml
# Mob File
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=IceShield} @self ~onDamaged 0.2
  - skill{s=IceShield-Remove} @self ~onSignal:REMOVESHIELD
```

```yaml
# Skills File
IceShield:
  Skills:
  - orbital{
    auraName=IceShield;
    onTick=IceShield-Tick;onHit=IceShield-Hit;points=20;interval=1;duration=200;charges=1}

IceShield-Remove:
  Skills:
  - auraremove{aura=IceShield}
  - signal{s=SHIELDREMOVED} @trigger
```

## 别名 {#aliases}

- o
