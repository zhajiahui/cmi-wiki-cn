---
title: Onjump
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/onjump
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onjump {#onjump}

## 说明 {#description}

对目标施加[光环](aura.md)，在跳跃时触发技能。

> **这是一个[仅支持 Paper](https://papermc.io/downloads/all)机制！**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onJump | oJ, onjumpskill | 目标跳跃时执行的元技能。 |  |
| cancelevent | cE | 触发事件时是否取消该事件。 | false |

> 该机制继承了[光环](aura.md)机制的所有属性

## 示例 {#examples}

为自身施加 onJump 光环。每次跳跃时获得等级 1 的缓降，持续 1 秒。

```yaml
ApplyAura:
  Skills:
  - onJump{oj=SlowFalling;auraname=Jumpies;d=300;i=1} @self

SlowFalling:
  Skills:
  - potion{t=SLOW_FALLING;d=20;l=0;hasParticles=false} @self
```

##  {#section}

为自身施加 onJump 光环。每次跳跃时，传送到 40 格内最近的实体旁并将其击杀。

```yaml
ApplyAura:
  Skills:
  - onJump{oj=Assassin;auraname=Stabbies;d=300;i=1} @self

Assassin:
  Skills:
  - skill{s=Murder} @EIR{r=30;limit=1;sort=NEAREST;targetPlayers=false}

Murder:
  Skills:
  - teleport
  - delay 1
  - damage{a=1000-2000;cause=thorns}
```

##  {#section-2}

为自身施加 onJump 光环。每次跳跃时会跳得更高，随后停在半空，反复向 30 格内的所有实体发弹射物射物。

```yaml
ApplyAura:
  Skills:
  - onJump{oj=PewPew;auraname=Shooties;d=300;i=1} @self

PewPew:
  Skills:
  - jump{v=2;delay=2} @self
  - delay 10
  - velocity{m=SET;x=0;y=0;z=0;repeat=39;repeatInterval=1} @self
  - skill{s=ShotEm;repeat=19;repeatInterval=2} @EIR{r=30;limit=10;sort=RANDOM;targetPlayers=false}

ShotEm:
  Skills:  
  - projectile{bulletType=ITEM;material=FIRE_CHARGE;bulletSpin=29;i=1;v=24;mr=100;d=100;hnp=true;oS=Fireball_oS;oT=Fireball_oT;oH=Fireball_oH}

Fireball_oS:
  Skills:
  - sound{s=entity.skeleton.shoot;v=1;p=1} @origin

Fireball_oT:
  Skills:
  - particles{particle=flame;a=4;hs=0.2;vs=0.2;y=0;s=0.1} @origin

Fireball_oH:
  Skills:
  - damage{a=5-15;cause=magic}
```
