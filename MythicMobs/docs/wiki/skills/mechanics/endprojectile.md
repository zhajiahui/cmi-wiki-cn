---
title: Endprojectile
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/endprojectile
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Endprojectile {#endprojectile}

## 说明 {#description}

终止调用此机制的弹射物，并触发它的 onEnd 技能。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| conditions | condition, cond, con | 终止弹射物之前要检查的条件。 |  |

## 示例

**生物文件**

```yaml
Mob:
  Type: HUSK
  Skills:
  - skill{s=ExplodingProjectile} @target ~onTimer:20
  - aura{auraName=explode;d=2} @self ~onTimer:200
```

**技能文件**

```yaml
ExplodingProjectile:
  Skills:
  - projectile{onTick=ExplodingProjectile_Tick;onEnd=ExplodingProjectile_End;v=4;i=1;hp=false;sb=false;se=false;d=200}
ExplodingProjectile_Tick:
  Skills:
  - effect:particles{p=flame;amount=20;speed=0;hS=0.2;vS=0.2} @origin
  - sound{s=entity.blaze.burn;v=0.5} @origin
  - damage{a=2} @EntitiesNearOrigin{r=2}
  - endprojectile ?hasaura{auraName=explode}
ExplodingProjectile_End:
  Skills:
  - damage{a=20} @EntitiesNearOrigin{r=5}
  - throw{fromorigin=true} @EntitiesNearOrigin{r=5}
  - effect:explosion @origin
```

## 别名 {#aliases}

- terminateProjectile
- terminateproj
- endproj
- stopprojectile
- stopproj
