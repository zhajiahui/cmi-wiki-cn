---
title: 伤害
source: https://docs.phoenixdevt.fr/mythiclib/api/damage
source_snapshot: '2026-10-19'
---

# 伤害 {#⚔️-damage}

## 玩家攻击事件 {#playerattackevent}

每当玩家对另一个实体造成伤害时，就会调用`PlayerAttackEvent`bukkit 事件。该事件包含有关玩家攻击、造成的伤害和攻击目标的所有信息。

`AttackMetadata`包含：

- 玩家攻击
- 被攻击的实体
- 当玩家施放技能/攻击时生成的玩家属性的缓存地图
- DamageMetadata 的一个实例

`DamageMetadata`处理所有伤害计算。访问此类时，你可以：

- 使特定类型造成的任何伤害增加 X%
- 添加额外的元素/类型损坏包
- 获取所有伤害值

损坏元数据由一组损坏数据包组成。伤害数据包是双精度的，指示造成的伤害量以及一组伤害类型。这种数据包方法可以让MythicLib区分伤害源并仅对其中一些伤害源应用修改器。

使用伤害数据包，你可以在一个 DamageMetadata 下让你的技能造成类似于10weapon-physical伤害 +15skill-magical伤害的伤害。如果玩家恰好有属性类似 +50%技能损坏，则此属性将仅适用于至少有技能作为损坏类型的数据包！这允许疯狂的on-hit额外的RPG风格的伤害计算。使用示例：

```java
@EventHandler
public void onAttack(PlayerAttackEvent event) {
    AttackMetadata attack = event.getAttack();
    DamageMetadata damage = attack.getDamage();

    damage.add(10, DamageType.WEAPON, DamageType.PHYSICAL); // add 10 weapon-physical damage
    damage.multiplicativeModifier(1.5, DamageType.SKILL); // increase skill damage by 50%
    damage.collectTypes().foreach(type -> whatever); // collect all damage types present in the damage packets
}
```

## 使用伤害管理器 {#using-damagemanager}

它是MythicLib用来集中来自MMOItems和MMOCore的所有玩家攻击的类。以下代码片段可用于强制玩家对特定实体造成伤害。你首先必须指定要造成的伤害以及伤害类型。然后在定义 AttackMetadata 并使用MythicLib的伤害管理器注册它之前缓存玩家的属性。

```java
PlayerData playerData = /* TODO */; // player attacking

DamageMetadata damage = new DamageMetadata(12, DamageType.SKILL, DamageType.MAGIC);
StatMap.CachedStatMap statMap = playerData.getMMOPlayerData().getStatMap().cache(EquipmentSlot.MAIN_HAND);
AttackMetadata attack = new AttackMetadata(damage, statMap);

boolean knockback = true; // If you want your attack to deal knockback
LivingEntity target = ...; // Entity being targeted

MythicLib.plugin.getDamage().damage(damage, target, knockback); // Finally deal damage
```

## 与其他具有损坏系统的插件的兼容性 {#compatibility-with-other-plugins-which-have-a-damage-system}

采用任何其他实现魔法技能的插件，例如Fabled或Heroes。MMOCore需要一种方法来检测玩家何时使用技能损坏实体，以便它可以应用`Skill Damage`属性等。这就是`DamageManager`类的全部内容：监视玩家造成的所有伤害。

每当实体被玩家损坏时，其他具有损坏系统的插件都需要在MythicLib中注册其损坏信息，以便MythicLib知道正在应用一些自定义损坏。如果MythicLib检测到玩家损坏但找不到源插件，则视为近战武器攻击。

为了在MythicLib中注册该损坏信息，你需要创建`DamageHandler`类的实例，并使用以下方法将其注册到MythicLib的`DamageManager`实例中：

```java
MythicLib.plugin.getDamage().registerHandler(damageHandler);
```

损坏处理程序可以在**MythicLib加载后**随时注册。

## 伤害减免 {#damage-mitigation}

每当玩家触发缓解类型时，就会调用`DamageMitigationEvent`的实例。你可以使用`event#getType()`检索缓解类型。此活动可以取消。

## 命中效果 {#on-hit-effects}

每当触发on-hit效果时，就会调用`OnHitEffectEvent`的实例。你可以使用`event#getEffect()`检索on-hit效果。此活动可以取消。

## 伤害显示 {#damage-indicators}

当实体上显示指示器时，将调用`IndicatorDisplayEvent`的实例。你可以使用`event#getMessage()`检索指示器消息并使用`event#setMessage(String)`进行设置。此活动可以取消。

---

原文：[⚔️ Damage](https://docs.phoenixdevt.fr/mythiclib/api/damage) · 原文归档：2026-10-19
