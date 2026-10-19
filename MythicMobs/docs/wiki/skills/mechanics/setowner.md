---
title: Setowner
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/setowner
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setowner {#setowner}

## 说明 {#description}

将目标设为 Mythic 生物的所有者。这是 MythicMobs 专用属性，与原版生物所有者不同。

施法者不是 Mythic 生物时不执行操作。如果施法生物是 `Wolf`、`Cat` 或 `Parrot`，且目标是玩家，还会同时将原版所有者设为该玩家。

与 [@Owner Targeter](../targeters/owner.md) 和 [Owner Condition](../conditions/owner.md) 配合使用。

当所有者被设置时，生物将永远不会攻击或瞄准它，即使另有指定。生物仍然会保留在设置之前对所有者产生的任何仇恨。

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

```yaml
PetSheep:
  Mobtype: sheep
  Display: 'Pet'
  Health: 20
  Damage: 18
  Skills:
  - skill{s=SetOwner} @trigger ~onInteract
  - skill{s=HealOwner} @Owner ~onTimer:50
```

```yaml
SetOwner:
  Skills:
  - setowner
  - message{m=You are now the owner of this mob!}
```

> 此技能会将生物的所有者更改为右键单击它的人。

##  {#section}

```yaml
HealOwner:
  Cooldown: 10
  TargetConditions:
  - health{h=<20} true
  Skills:
   - heal{a=10}
   - message{m=I healed you!}
```

> 该技能只会每10秒治疗一次生物主人，并且只有当他们的生命值少于20时
