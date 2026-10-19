---
title: Cast
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/cast
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Cast {#cast}

## 说明 {#description}

cast 是一种类似 [skill](skill.md) 的[光环](aura.md)机制，同样会执行技能，但会像 RPG 角色或怪物一样，先经历“施法”过程。施法成功完成，也就是光环正常结束后，才执行指定技能；施法可以被打断。

一次只能施展一个法术，并且该法术作为施法者身上的光环运行，名为**#casting**。移除实体的光环会中断施法。任何导致施法提前停止的光环设置也会中断施法，例如在移动或传送时取消。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onCastSkill | oncast, oc | 施法成功完成时执行的技能。 |  |
| onInterruptedSkill | oninterrupted, oninterrupt, oi | 施法被打断时执行的技能。 |  |
| onnotargetsskill | onnotargets, onnotarget, ont | 未找到目标时执行的技能。 |  |
| skillname | spellname, sn | 施法条中显示的法术名称。 |  |
| showCastBar | castbar, cb | 是否显示施法条。 | true |
| cancelOnMove | com | 施法者移动时是否取消光环。 | false |

> 该机制继承了[光环](aura.md)机制的所有属性
>

> > - `auraName` 属性**设置**于 `#casting` 并且**无法更改**
> > - `charges` 属性**设置**于 `1` 并且**无法更改**
> > - `maxStacks` 属性**设置**于 `1` 并且**无法更改**
> > - `mergeAll` 属性**设置**于 `true` 并且**无法更改**

## 示例 {#examples}

```yml
myCoolMob:
  Type: ZOMBIE
  Skills:
    - cast{
          skillName="&aFrost Blast";
          duration=40;
          onCast=FrostBlast-Cast;
          onTick=FrostBlast-Tick;
          onInterrupted=FrostBlast-Interrupted;
          onNoTargets=FrostBlast-NoTargets;
          showCastBar=true
        } @target ~onTimer:100
```

```yaml
# This will be cast once the duration has elapsed
FrostBlast-Cast:
  Skills:
  - damage{a=20}
  - message{m="MUHAHA, TAKE THAT!"}

# This will be cast while the main casting is still in progress
FrostBlast-Tick:
  Skills:
  - particle{p=end_rod;a=4;hs=1;vs=1} @selflocation{y=1}

# This will be cast if the aura is somehow removed
FrostBlast-Interrupted:
  Skills:
  - message{m="Tsk, you got me!"}

# This will be cast if the original target for the aura no longer exist
FrostBlast-NoTargets:
  Skills:
  - message{m="...Where has everyone gone to?"} @World
```
