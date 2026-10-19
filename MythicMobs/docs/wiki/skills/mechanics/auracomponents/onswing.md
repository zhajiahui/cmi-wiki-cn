---
title: On Swing
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/OnSwing
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Swing {#on-swing}

## 说明 {#description}

将光环组件应用于目标，当目标摆动时触发技能（左键单击）

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onSwing | onswingskill, osw | 目标挥动手臂或左键点击时执行的技能。 |  |

## 示例 {#examples}

Simple:

为自身施加 onSwing 光环，挥动时会点燃前方 10 格内的实体。

```yaml
ApplyAura:
  Skills:
  - aura{auraname=Ignite;d=300;i=1;components=[
    - onSwing{osw=CatchOnFire}
    ]} @self
CatchOnFire:
  Skills:
  - ignite{t=60} @EntitiesInCone{angle=90;range=10;rotation=0}
```

##  {#section}

Intermediate:

为自身施加 onSwing 光环，挥动时发弹射物射物。生成时播放骷髅射箭声音，飞行时产生火焰粒子并点燃目标，造成 2-4 点 MAGIC 伤害。

```yaml
ApplyAura:
  Skills:
  - aura{auraname=Fireballs;d=300;i=1;components=[
    - onSwing{osw=ShootProjectile}
    ]} @self
ShootProjectile:
  Skills:
  - projectile{bulletType=ITEM;material=FIRE_CHARGE;bulletSpin=29;i=1;v=24;mr=100;d=100;hnp=true;oS=Fireball_oS;oT=Fireball_oT;oH=Fireball_oH} @forward{f=300;y=0}
Fireball_oS:
  Skills:
  - sound{s=entity.skeleton.shoot;v=1;p=1} @origin
Fireball_oT:
  Skills:
  - particles{particle=flame;a=4;hs=0.2;vs=0.2;y=0;s=0.1} @origin
Fireball_oH:
  Skills:
  - damage{a=2-4;cause=magic}
```

## 别名 {#aliases}

- onleftclick
