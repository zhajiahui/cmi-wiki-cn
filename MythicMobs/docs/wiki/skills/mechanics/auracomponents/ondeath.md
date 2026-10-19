---
title: On Death
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/OnDeath
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Death {#on-death}

## 说明 {#description}

对目标施加光环成分，在目标死亡时触发技能

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onDeathSkill | od | 目标死亡时执行的技能。 |  |
| cancelEvent | cE, cancel | 在 Paper 服务器上，技能成功执行时取消死亡事件并复活生物。 | false |

## 示例 {#examples}

通过 sudoskill 对你周围的所有实体施加 onDeath 光环。当你杀死他们时，他们都会掉落钻石。

```yaml
ForceApplyAura:
  Skills:
  - sudoskill{s=ApplyAura} @EIR{r=50}
ApplyAura:
  Skills:
  - aura{d=1200;i=1;auraname=rip;components=[
    - onDeath{od=DropDiamonds}
    ]} @self
DropDiamonds:
  Skills:
  - dropitem{i=DIAMOND 3-5} @self
```

在 Paper 服务器上，可以通过 `cancelEvent` 让生物复活，避免死亡。本例只有一次可用次数，因此可抵消一次死亡并播放效果，下次则正常死亡。

```yaml
Undying:
  Skills:
  - aura{d=-1;charges=1;auraname=undying;components=[
    - onDeath{od=Revive;ce=true}
    ]} @self
Revive:
  Skills:
  - effect:particles{p=totem_of_undying;amount=50} @self
```

## 别名 {#aliases}

- onDead
