---
title: Cancelevent
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/cancelevent
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Cancelevent {#cancelevent}

## 说明 {#description}

取消触发技能的事件。为了正确执行该机制有几个重要的要求：

- **此机制或最初的技能必须设置 sync=  true   运行。**

> 示例：-
> skill{s=CancelEventSkill;sync=true} ~onDamaged

- 不允许使用延迟。
- 并非所有触发器都与可以取消的事件关联。
- 即使事件最终被取消，监听同一触发器的其他机制仍将被触发。

### 兼容的触发器 {#compatible-triggers}

- ~onAttack
- ~onBucket
- ~onDamaged
- ~onDeath
- ~onExplode
- ~onInteract
- ~onCombat
- ~onTeleport
- ~onShoot（施法者是玩家时，需要通过 Crucible 制作弓或弩）
- ~onUse（需要 Crucible）
- ~onConsume（需要 Crucible）

> 这不是完整列表，其他触发器也可能起作用，此处列出的只是已确认的触发器

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

Skill.yml:

```yaml
CancelDamageEvent:
  Skills:
  - CancelEvent
  - message{m="&cYou cannot hurt this mob!"} @trigger
```

Mob.yml:

```yaml
NoDamageMob:
  Type: villager
  Skills:
  - skill{s=CancelDamageEvent;sync=true} ~onDamaged
```

也可内联使用！本例会阻止生物射箭，并取消它受到的伤害。

```yaml
customskeleton:
  Type: skeleton
  Skills:
  - cancelevent{sync=true} @self ~onShoot
  - cancelevent{sync=true} @self ~onDamaged
```
