---
title: 不稳定的实体类型
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 不稳定的实体类型 {#unstable-entity-types}

MythicMobs 支持许多实体类型，但每种都可能存在特殊问题。配置者需要了解这些问题，以尽量减少它们造成的影响，或更合理地使用实体。

下面列出目前发现的特殊问题。这里暂不讨论常见或明显的问题，只列出较少见的情况。如果发现其他问题，请通过 [Discord](https://discord.com/invite/K3tqXfT)告知。

1. [按组划分的生物](unstable-entity-types.md#mobs-by-group)
   1. [所有僵尸](unstable-entity-types.md#all-zombies)
   2. [所有被动动物](unstable-entity-types.md#all-passive-animals)
   3. [所有可繁殖动物](unstable-entity-types.md#all-breedable-animals)
   4. [大多数 Boss](unstable-entity-types.md#most-bosses)
   5. [会受到水伤害的实体](unstable-entity-types.md#entities-damaged-by-water)
2. [特定生物](unstable-entity-types.md#specific-mobs)
   1. [ARMOR_STAND](unstable-entity-types.md#armor-stand)
   2. [AXOLOTL](unstable-entity-types.md#axolotl)
   3. [BEE](unstable-entity-types.md#bee)
   4. [BLAZE](unstable-entity-types.md#blaze)
   5. [CAT](unstable-entity-types.md#cat)
   6. [CHICKEN](unstable-entity-types.md#chicken)
   7. [COW](unstable-entity-types.md#cow)
   8. [DROWNED](unstable-entity-types.md#drowned)
   9. [ENDER_DRAGON](unstable-entity-types.md#ender-dragon)
   10. [ENDERMAN](unstable-entity-types.md#enderman)
   11. [ENDERMITE](unstable-entity-types.md#endermite)
   12. [FOX](unstable-entity-types.md#fox)
   13. [GHAST](unstable-entity-types.md#ghast)
   14. [GIANT](unstable-entity-types.md#giant)
   15. [IRON_GOLEM](unstable-entity-types.md#iron-golem)
   16. [MAGMA_CUBE](unstable-entity-types.md#magma-cube)
   17. [PARROT](unstable-entity-types.md#parrot)
   18. [PHANTOM](unstable-entity-types.md#phantom)
   19. [PIGLIN](unstable-entity-types.md#piglin)
   20. [PILLAGER](unstable-entity-types.md#pillager)
   21. [PUFFERFISH](unstable-entity-types.md#pufferfish)
   22. [RABBIT](unstable-entity-types.md#rabbit)
   23. [SKELETON](unstable-entity-types.md#skeleton)
   24. [SLIME](unstable-entity-types.md#slime)
   25. [SQUID](unstable-entity-types.md#squid)
   26. [VEX](unstable-entity-types.md#vex)
   27. [WARDEN](unstable-entity-types.md#warden)
   28. [WITHER](unstable-entity-types.md#wither)
   29. [WOLF](unstable-entity-types.md#wolf)

## 按类别划分的生物 {#mobs-by-group}

### 所有僵尸 {#all-zombies}

可以作为领导者生成，拥有数倍于配置的生命值。

### 所有被动动物 {#all-passive-animals}

可能遭到其他实体攻击或追赶。

### 所有可繁殖动物 {#all-breedable-animals}

通常可用某种物品喂食，随后尝试繁殖。可通过 [~onBreed](../../skills/triggers/onbreed.md) 拦截繁殖事件，再取消事件或使用其他机制处理；也可以用 [Age](../options.md#age) 选项完全阻止繁殖。

### 大多数 Boss {#most-bosses}

拥有硬编码的人工智能或其他一些硬编码的功能。

### 会受到水伤害的实体 {#entities-damaged-by-water}

受影响的实体包括末影人、雪傀儡和烈焰人。这类伤害的类型为 `DROWNING`，可把 [DamageModifier](../damagemodifiers.md) 设为负值，或使用以下技能，完全阻止伤害。

```yaml
   - cancelevent{sync=true} ~ondamaged ?damagecause{c=drowning}
```

## 特定生物 {#specific-mobs}

### ARMOR_STAND {#armor-stand}

默认不会被多实体目标选择器选中，必须使用[特定过滤器](../../skills/targeters.md#target-filters)。

### AXOLOTL {#axolotl}

可以被装进桶中。使用 [onBucket](../../skills/triggers/onbucket.md) 触发器处理这种情况。

### BEE {#bee}

当允许随机飞行时，它会进入放置的蜂箱并为花朵授粉。   除了清除其AI并建立一个新的之外，不存在明确的答案。

### BLAZE {#blaze}

可能会被水、雪球等损坏。使用[伤害修正](../damagemodifiers.md)来防止这种情况发生。

### CAT {#cat}

会吓跑苦力怕和幻翼。

### CHICKEN {#chicken}

会下蛋，也会被其他动物捕食。下蛋问题可使用[骑乘选项](../options.md#jockey)处理。

### COW {#cow}

可以挤奶。

### DROWNED {#drowned}

默认情况下，如果目标不在水区中，它不会在白天攻击目标。必须设置 [自定义 ai](../custom-ai.md) 才能消除此行为

### ENDER_DRAGON {#ender-dragon}

有一个硬编码的ai。

### ENDERMAN {#enderman}

会躲避弹射物，并受到水伤害。

### ENDERMITE {#endermite}

吸引末影人的仇恨。

### FOX {#fox}

具有独特的攻击模式，可能有用，但也存在问题。

### GHAST {#ghast}

具有硬编码的 AI，可能被火球一击杀死。

### GIANT {#giant}

有一个硬编码的ai。

### IRON_GOLEM {#iron-golem}

可以通过使用铁锭来治疗，并且默认会吸引大多数敌对生物的仇恨。

### MAGMA_CUBE {#magma-cube}

有一个硬编码的ai。

### PARROT {#parrot}

可能被曲奇一击杀死。

### PHANTOM {#phantom}

有一个硬编码的ai。

### PIGLIN {#piglin}

具有硬编码的仇恨优先级

### PILLAGER {#pillager}

掠夺者手持已装填的弩时，如果因任何原因失去目标，就会僵住。

### PUFFERFISH {#pufferfish}

具有非常独特的交互和行为，可能会导致问题。

### RABBIT {#rabbit}

吸引其他中立生物（例如狐狸）的仇恨。

### SKELETON {#skeleton}

吸引狼的仇恨

### SLIME {#slime}

有一个硬编码的ai。

### SQUID {#squid}

不要使用 [lunge](../../skills/mechanics/lunge.md)、[throw](../../skills/mechanics/throw.md) 等机制。这也适用于 GLOW_SQUID。

### VEX {#vex}

有一个硬编码的ai。

### WARDEN {#warden}

拥有硬编码的仇恨系统。

### WITHER {#wither}

有一个硬编码的ai。

### WOLF {#wolf}

可以用特定物品治疗；一旦被“驯服”，生命值会重置。
