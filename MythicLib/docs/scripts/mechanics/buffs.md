---
title: 增益与属性
source: https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/buffs
source_snapshot: '2026-10-19'
---

# 增益与属性 {#💖-buffs-stats}

> **警告**
>
> 建设中

## 添加临时属性 {#add-temporary-stats}

这将属性添加到玩家。你可以使用MMOCore和MMOItems中的所有属性。当服务器重新启动时它将被删除。

对于临时属性增益/减益，你可以使用`lifetime`参数添加持续时间（以刻为单位）。将`relative`设置为`true`，该增益将授予10%攻击力伤害，而不是平的 +10攻击力伤害。

`key`参数是可选的。这是你需要提供的密钥，以便稍后在需要时删除修饰符。可以有多个属性使用同一把钥匙，并且使用带有该钥匙的`remove_stat`机械师将删除所有这些。

如果你希望一次仅激活一个具有相同键的修改器，请将`unique`设置为`true`。 **如果使用相同的键添加新的修改器，它将取代之前的修改器。** 这对于你想要定期刷新的增益效果非常有用。

```yml
script_give_stat:
  mechanics:
  - 'add_stat{amount="10 + <modifier.extra>";time="20 *  (1 + <modifier.extra_time> )";stat=ATTACK_DAMAGE;key=my_custom_skill;relative=false;target=caster;unique=false}'
```

## 删除临时属性 {#remove-temporary-stats}

以下机制删除所有属性修正器及其关联的`key`。属性修正器是临时的还是永久的并不重要。

```yml
script_rem_stat:
  mechanics:
  - 'remove_stat{stat=ATTACK_DAMAGE;key=my_custom_skill;target=caster}'
```

## 治疗目标 {#heal-target}

`reason`（目标被治疗的原因）是可选的（默认为`CUSTOM`）。最好指出它，以便其他插件知道治疗来源。可用来源[此处](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/event/entity/EntityRegainHealthEvent.RegainReason.html)。

```yml
script_health_target:
  mechanics:
  - 'heal{amount="10 + <caster.health> / 50";reason=CUSTOM;target=caster}'
```

## 给目标食物 {#give-food-to-target}

最高食物等级是20。玩家的食物等级始终是整数（与生命值不同）。该机械师 **SETS**玩家的食物等级。

```yml
give_food_script:
  mechanics:
  - 'feed{amount="10 + 8 / 2";target=caster}'
```

## 恢复目标饱和度 {#restore-saturation-of-target}

该机制**设置**目标的饱和度。

```yml
set_sat_level:
  mechanics:
  - 'saturate{amount="10 + 1";target=caster}'
```

---

原文：[💖 Buffs & Stats](https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/buffs) · 原文归档：2026-10-19
