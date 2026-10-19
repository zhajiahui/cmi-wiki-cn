---
title: Missile
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Missile
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Missile {#missile}

## 说明 {#description}

Missile 与 Projectile 类似，可使用[弹射物可继承属性](projectile.md#inheritable-attributes)，但导弹会自动追踪目标，目标可以是位置或实体。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| Inertia | in, intertia | 设置追踪弹的转向速率。值越小，追踪弹转向越快。想让追踪弹缓慢转向时，应使用较大的值（10-100）。 | 1.5 |
| Bounces | bounce | 弹射物是否弹跳。弹跳半径取决于弹射物的碰撞箱。**仅 Premium 版**支持。 | false |
| BounceVelocity | bv | 弹射物每次弹跳时，其速度都会乘以此值。**仅 Premium 版**支持。 | 0.9 |
| startWithParentVelocity | swpv, spv | 追踪弹由另一个弹射物调用时，初始速度是否与父弹射物相同。 | false |
| HugSurface | hs | 弹射物是否沿地面移动。 | false |
| HugLiquid | hugwater, huglava | 使用 hugSurface 时，也会在液体表面移动。 | false |
| HeightFromSurface | hfs | 对于 NORMAL 弹射物，此项表示 HugSurface 设为 TRUE 时，弹射物在表面上方滑行的高度；对于 METEOR 弹射物，此项表示弹射物在目标上方的初始高度。 | 0.5 |
| MaxClimbHeight | mch | 弹射物贴着方块或液体表面移动时，在自行终止前尝试**升高**其 y 坐标的次数。 | 3 |
| MaxDropHeight | mdh | 弹射物贴着方块或液体表面移动时，在自行终止前尝试**降低**其 y 坐标的次数。 | 10 |
| highAccuracyMode | ham | 是否使用高精度模式。此模式每刻执行射线检测，保证弹射物不会穿过任何物体。可设为 `true`、`false`、`PLAYERS_ONLY`。 | PLAYERS_ONLY |
| hitnonplayers | hnp | 追踪弹是否命中非玩家实体。 | true |

> 该机制继承了[弹射物](projectile.md#inheritable-attributes)机制的所有可继承属性
>

> > - `hitnonplayers` 属性**默认为** `true`。

## 示例 {#examples}

此示例发射的导弹看起来像一条细长的火焰轨迹，并且具有高转弯率。它击中目标后会产生强烈的爆炸。

```yaml
# Mob File
Mob:
  Type: ZOMBIE
  Skills:
  - skill{s=Homer} @target ~onTimer:100
```

```yaml
# Skills File
Homer:
  Skills:
  - missile{ot=Homer_TICK;oh=Homer_HIT;v=4;i=1;hR=1;vR=1;in=0.75}

Homer_TICK:
  Skills:
  - effect:particles{p=flame;a=1} @origin

Homer_HIT:
  Skills:
  - effect:particles{p=lava;a=50;hS=1;vS=1}
  - effect:sound{s=entity.generic.explode;v=1;p=0}
  - damage{a=1337;i=false}
```

## 别名 {#aliases}

- mi
