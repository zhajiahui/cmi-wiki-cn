---
title: 取消事件
source_url: https://wiki.mythiccraft.io/mythicmobs/Guides/Cancelling-Events
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 取消事件

**难度：入门**

大多数生物类型都在 Minecraft 中内置了默认行为，其中许多行为可以通过 [CancelEvent](../skills/mechanics/cancelevent.md) 机制阻止，让你用自定义行为替换原版行为！

一个常见示例是通过 ~onAttack 取消生物的攻击，再替换为自己的攻击技能。

请记住，CancelEvent 要求在最初的机制上添加 `sync=true` 通用属性，而且并非所有触发器都受支持。可用触发器列表见 [CancelEvent](../skills/mechanics/cancelevent.md) 机制页面。你还可能遇到一些特殊情况，例如取消死亡来创建自定义死亡事件，或取消伤害事件后创建自己的伤害，却又被取消，从而陷入循环。下文提供了应对这些情况的技巧。

# 攻击 {#attack}

下面示范如何取消生物攻击，并替换为自己创建的攻击技能。

在生物配置中运行以下机制：

`- skill{s=FireAttack;sync=true} @target ~onAttack`

然后在技能文件中创建如下元技能：

```yaml
FireAttack:
  Skills:
  - cancelevent
  - damage{a=5}
  - ignite @target
```

对于远程生物，也可以使用 onShoot 触发器。它们的默认射击无法直接修改，但可以先取消，再用 [Projectile](../skills/mechanics/projectile.md) 或 [Shoot](../skills/mechanics/shoot.md) 等机制创建自己的射击！

将这个示例用于骷髅，会让它一次射出多支伤害更高的箭，而不是进行原本的单箭攻击。

`- skill{s=ArrowVolley;sync=true} @target ~onShoot`

```yaml
ArrowVolley:
  Skills:
  - cancelevent
  - volley{type=EGG;velocity=5;damage=10;amount=20}
```

# Damage {#damage}

可以取消生物的受伤事件，让生物无敌，或改变它承受伤害的方式。

用这种方法让生物无敌很简单，只需在生物的技能部分添加以下内容：

`- cancelevent{sync=true} @self ~onDamaged`

还可以在此基础上添加条件，使生物只在特定情况下无敌。这个示例会让生物在被玩家用钻石剑攻击时无敌，使用了[行内触发者条件](https://wiki.mythiccraft.io/mythicmobs/Skills/Inline-Conditions#conditions-triggerconditions)。

`- cancelevent{sync=true} @self ~onDamaged ?~holding{m=DIAMOND_SWORD}`

下面的示例会取消生物受到的所有伤害，替换为 damage 机制，让生物无论受到什么武器攻击，都始终承受固定伤害。由于先取消伤害，再直接伤害生物会陷入循环，因此我们会使用 damageTag 并检查该标签是否存在。若存在，就不取消伤害，让生物正常受伤。

`- skill{s=SelfDamage;sync=true} @self ~onDamaged`

```yaml
SelfDamage:
  Conditions:
  - damageTag{tag=SELFDAMAGE} false
  Skills:
  - cancelevent
  - damage{a=10;tag=SELFDAMAGE} @self
```

# 死亡 {#death}

你可能想取消死亡事件，以便制作带有华丽效果的自定义死亡过程。我们需要使用 remove 机制移除生物，而不是让它因伤害被移除。因此，取消死亡时请注意，onDeath 技能不会生效，需要将这些技能调整后放到这里，例如发放奖励等。

`- skill{s=DeathSkill;sync=true} @self ~onDeath`

```yaml
DeathSkill:
  Skills:
  - cancelevent
  - delay 10
  - fakeexplosion @self
  - particlesphere{particle=flame;amount=200;radius=5;repeat=5;repeatinterval=5} @self
  - delay 20
  - remove @self
```
