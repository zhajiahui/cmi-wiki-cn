---
title: Throw
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/throw
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Throw {#throw}

## 说明 {#description}

将所有目标扔离生物（或原点）。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| velocity | v | 抛出实体的水平速度 | 1 |
| velocityY | vy, yv, yvelocity | 抛出实体的垂直速度 | 1 |
| fromOrigin | fo | 设置是否从原点抛出实体 | false |

## 示例 {#examples}

在此示例中，生物将在其周围产生爆炸效果，对 5 方块半径内的玩家造成 10 伤害（5 心），并将他们击退。给人一种强烈爆炸的错觉。

```yaml
GroundSlam:
  Skills:
  - effect:explosion @Self
  - damage{amount=10} @PlayersInRadius{r=5}
  - throw{velocity=15;velocityY=5} @PlayersInRadius{r=5}
```

##  {#section}

这个复杂的例子展示了如何将投掷机制与其他机制结合使用以产生相当惊人的效果。施法者释放出强大的冲击波，对10范围内的所有玩家造成50伤害（25心），并使用**投掷**机制使他们被抛到空中。还添加了额外的效果，使攻击更具吸引力和威慑力。

```yaml
SuperShockslam:
  Skills:
  - throw{velocity=5;velocityY=5} @PIR{r=10}
  - damage{a=50;i=false} @PIR{r=10}
  - effect:particles{p=hugeexplode;a=5;vs=0.5;hs=0.5;s=0;y=1} @Self
  - effect:sound{s=entity.generic.explode;v=2;p=0.5} @Self
  - effect:sound{s=entity.generic.explode;v=2;p=1;repeat=7;repeatInterval=2} @Self
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=1} @Self
  - delay 2
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=3} @Self
  - delay 2
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=5} @Self
  - delay 2 
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=7} @Self
  - delay 2
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=9} @Self
  - delay 2
  - effect:particlering{p=largeexplode;a=40;vs=0.5;hs=0.5;s=0;y=0.3;points=20;radius=11} @Self
```
