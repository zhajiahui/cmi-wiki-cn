---
title: 玩家属性
source: https://docs.phoenixdevt.fr/mythiclib/api/stats
source_snapshot: '2026-10-19'
---

# 玩家属性 {#📊-player-stats}

MythicLib属性API的设计与Spigot属性修饰符API类似。  来自每个数字MMOItems/MMOCore属性的属性数据存储在可使用以下方法访问的`StatMap`中。

```java
MMOPlayerData playerData = MMOPlayerData.get(/* player or UUID */);
StatMap statMap = playerData.getStatMap();
```

使用该类，你可以访问与一个特定属性相对应的`StatInstance`实例。

## 属性实例 {#stat-instances}

就像Spigot的属性实例一样，属性实例具有一个 **存储属性修正器** 的映射。属性修正器有两种不同类型：

- 修复了属性修正器，增加了固定/固定金额（+10Atk Damage）
- % stat modifiers, which multiply the total stat value by a certain constant (+10%攻击力伤害)

使用属性的优点是任何插件都可以添加自己的属性，MythicLib可以轻松收集所有属性并根据这些属性计算属性总值。例如，MMOCore使用属性来处理体验队伍增益：

```java
// Modifier that adds +10% exp gained
StatModifier experienceModifier = new StatModifier("myCustomPluginKey", "ADDITIONAL_EXPERIENCE", 10, ModifierType.FLAT);

// Register the modifier
experienceModifier.register(playerData);

// Access all currently registered modifiers this way
statMap.getInstance("ADDITIONAL_EXPERIENCE").getModifiers().forEach(mod -> /* code */);
```

请注意任何插件如何访问所有插件创建的所有修饰符。这意味着你必须确保你的插件仅操作你创建的属性，这可以通过选择非常具体的**修饰键**（如“mmocorePartyBuff”或“mmoitemsItemSetBonus”）来完成。

## 添加属性修正器 {#adding-a-stat-modifier}

生成属性修正器的方法有多种。最详尽的构造函数如下

```java
StatModifier(UUID, String, String, double, ModifierType, ModifierSource, EquipmentSlot)
```

第一个参数是UUID。如果未提供，则会将随机UUID分配给你的新修饰符。每个修饰符都由UUID标识。第二个参数，**修饰键**也可以用于快速识别注册修饰符的插件，但它**不是唯一的！！** 插件键应该是你的插件名称，以确保不会与其他系统或插件发生冲突。同样，自MythicLib1.6.2构建以来，此修饰键**不再是唯一的**。

第三个参数是正在修改的属性。例如，这可以是`ATTACK_DAMAGE`或`SKILL_CRITICAL_STRIKE_CHANCE`。

**设备槽**的实现是为了跟踪该修改器的来源。它主要由MMOItems和MMOInventory使用，根据玩家物品栏中配备的位置，从物品应用正确的属性。

**修改器源**的实现是为了区分近战和远程武器给出的属性修正器。 MI 和MMOInventory也使用此方法来解决类似问题。

> **提示**
>
> 使用`ModifierSource#OTHER`和`EquipmentSlot#OTHER`进行一般增益，或者如果你不确定使用什么。

如果你不需要指定UUID、修饰符源和设备槽，你也可以使用这个更简单的构造函数。

```java
StatModifier modifier = new StatModifier(String, String, double, ModifierType);
```

### 注册属性修正器 {#register-the-stat-modifier}

为了注册你的属性修正器，你可以使用以下方法。

```java
MMOPlayerData playerData = MMOPlayerData.get(/* player UUID */);
modifier.register(playerData);
```

你也可以使用此方法来完成完全相同的事情：

```java
StatModifier modifier = /* TODO */;
StatInstance instance = statMap.getInstance(modifier.getStat());
instance.addModifier(modifier);
```

## 临时属性修正器 {#temporary-stat-modifiers}

请注意，你还可以使用以下方法添加**临时属性修正器**。 long 参数对应于修饰符的持续时间（以刻为单位）。

```java
new TemporaryStatModifier(String, String, double, ModifierType, EquipmentSlot, ModifierSource).register(MMOPlayerData, long);
```

## 删除属性修正器 {#remove-a-stat-modifier}

以下代码使用我们正在讨论的密钥来删除由特定插件注册的所有属性修正器，或者哪个密钥以特定前缀开头等。

```java
statInstance.removeIf(key -> key.startsWith("mmoitems"));
statInstance.removeIf("MyAwesomePlugin"::equals);
```

你还可以精确定位特定修饰符并使用其UUID将其删除。

```java
statInstance.removeModifier(/* modifier UUID */);
```

你还可以直接从修改器实例取消注册属性修正器。这与之前的方法完全相同，并且你不需要提供修饰符UUID。

```java
modifier.unregister(playerData);
```

## 计算玩家属性 {#calculating-player-stats}

以下代码片段显示了如何计算属性的总价值。

```java
// calculate the player's crit strike chance
double critChance = statMap.getStat("CRITICAL_STRIKE_CHANCE");
```

属性值取决于玩家的动作手。大多数时候，他们使用主手（右手）进行交互，但有时他们可能会使用副手（左手），例如射弓或扔雪球时。在这种情况下，MythicLib必须忽略一些属性修正器，具体取决于正在使用哪只手。

默认情况下，MythicLib假定动作手是右手。如果需要以左手作为动作手计算属性值，可以使用以下方法：

```java
double attackSpeed = statMap.getInstance("ATTACK_SPEED").getTotal(EquipmentSlot.OFF_HAND);
```

MythicLib根据注册的属性修正器的设备槽和修改器源进行奇特的计算，以确定忽略哪些修改器以及保留哪些修改器。所有这些都已经在内部处理好，所以你不必担心！

## *总计* 与 *最终*属性值 {#total-vs-final-stat-value}

原版attribute-based属性像攻击伤害、最大生命值，移动速度有点难对付。这是因为，由于它们是由Minecraft本身处理的，因此MythicLib不能保证它是修改这些属性的唯一插件。其他插件也可能会添加自己的属性修饰符，而Minecraft本身会根据玩家的装备应用一些默认修饰符。

因此，*最终*属性值指的是 **Minecraft将返回的值**，即考虑到所有插件和Minecraft本身的所有属性修饰符。 *总*属性值是指MythicLib计算的值，仅考虑通过MythicLib的API注册的属性修正器。

例如，如果带有20底座最大生命值的玩家佩戴 +10最大生命值护甲(MythicLibAPI)，而另一个插件添加 +5最大生命值通过其自身的Minecraft属性修饰符，那么总的最大生命值将是30，而最终的最大生命值将是35。

> **信息**
>
> 对于non-vanilla属性，例如 *暴击几率* 或 *技能Damage*，属性的总值和最终值始终相同，因为这些属性不由Minecraft本身处理。

以下方法返回属性的最终属性值

```java
double moveSpeedFinal = statMap.getStat("MOVEMENT_SPEED");
double moveSpeedFinal = statMap.getInstance("MOVEMENT_SPEED").getFinal();
```

以下方法返回属性的总属性值。

```java
double moveSpeedTotal = statMap.getInstance("MOVEMENT_SPEED").getTotal();
```

---

原文：[📊 Player Stats](https://docs.phoenixdevt.fr/mythiclib/api/stats) · 原文归档：2026-10-19
