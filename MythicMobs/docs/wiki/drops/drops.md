---
title: 掉落物
source_url: https://wiki.mythiccraft.io/mythicmobs/drops/Drops
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 掉落物 {#drops}

可以为自定义生物添加 Drops 标签，使其死亡时掉落指定物品。MythicMobs 提供三类自定义掉落，需要加以区分。

1. [掉落配置](drops.md#drops-configuration)
   1. [掉落内容](drops.md#drop)
   2. [数量](drops.md#amount)
   3. [概率](drops.md#chance)
   4. [动态概率](drops.md#dynamic-chances)
2. [掉落类型](drops.md#drop-types)
   1. [示例](drops.md#example)
3. [行内掉落](drops.md#in-line-drops)
   1. [示例](drops.md#example-2)

Drops 是实现自定义掉落最简单的方式。

## 掉落物配置 {#drops-configuration}

```yaml
internal_mobname:
  Type: <mobtype>
  Drops:
  - <drop> <amount> <chance>
  - <drop> <amount> <chance>
  - ...
```

### 掉落物 {#drop}

可以填写 MythicMobs 物品、原版物品、经验、掉落表，或受支持插件中的物品和经验。可用的[掉落类型](drops.md#drop-types)列于下方

### 数量 {#amount}

要掉落的物品数量。

可以设置数值范围，例如 `1-3` 或 `1to3`。此时，掉落数量不会小于左侧数值，也不会**大于或等于**右侧数值

> 填写 `1to3` 会至少掉落 1 个、最多掉落 2 个物品

### Chance {#chance}

指定物品的掉落概率。

- 必须为 0 到 1 之间的数值
- **注意：**支持百分比概率，例如用 10% 代替 0.1。

### 动态概率 {#dynamic-chances}

> 需要 MythicMobs Premium，数值中使用数学表达式和变量属于 Premium 版功能。

概率也可以使用最终解析为数值的数学表达式、占位符或变量。每次计算掉落时，都会为掉落生物重新求值，因此掉落率可以随等级、属性或变量变化。解析结果大于或等于 `1` 时必定掉落，小于或等于 `0` 时绝不掉落。随机判定发生在战利品生成阶段，因此动态概率也适用于 [FancyDrops](fancydrops.md)。

```yaml
YourMob:
  Type: ZOMBIE
  Drops:
  # 5% per mob level (reaches 100% at level 20+)
  - diamond 1 0.05*<caster.level>
  # chance pulled from a variable set elsewhere on the mob
  - emerald 1 <caster.var.scaledDrop>
```

> 免费版无法计算这些表达式，会将该掉落视为必定掉落，概率为 100%，并在加载时记录警告。

## 掉落类型 {#drop-types}

| **类型** | **说明** | **示例** |
| --- | --- | --- |
| [MythicMob](droptypes/mythicmob.md) | 掉落一个 MythicMob |  |
| [Mythic Item](droptypes/mythicitem.md) | 掉落一个 Mythic 物品 |  |
| [VanillaLootTable](droptypes/vanillaloottable.md) | 从原版战利品表和数据包中掉落物品 | `- vanillaLootTable minecraft:table_name` |
| **champions-exp** | 掉落 `Champions` 插件的经验值。 |  |
| [skillapi-exp](droptypes/skillapiexp.md) | 掉落 `SkillAPI` 插件的经验值 |  |
| **heroesexp** | 掉落 `Heroes` 插件的经验值。 |  |
| [mcmmo-exp](droptypes/mcmmoexp.md) | 掉落 `MCMMO` 插件的经验值。 | `- mcmmo-exp 69` |
| **exp** | 掉落普通的 Minecraft 经验值。 | `- exp 420` |
| [money](droptypes/money.md) | 掉落 `Vault` 插件的金钱。 | `- money 1500` |
| **mythicdrop <item>** | 掉落 `MythicDrops` 插件中的 <item>。 | `- mythicdrop CoolSword 1` |
| [phatloot](droptypes/phatloot.md) | 掉落 `PhatLoot` 插件中的 &item。 | `- phatloot LootTableName 1` |
| [command](droptypes/command.md) | 在控制台执行命令。 | `- cmd{cmd="warp <trigger.name> spawn"} 1` |
| [mmoitems](https://gitlab.com/phoenix-dvpmt/mmoitems/-/wikis/Item%20Drop%20Tables#adding-mmoitems-to-mythicmobs-drop-tables) | 掉落一个 `mmoitems` 物品 | `- mmoitems{type=SWORD;id=CUTLASS} 1 1` |
| **nothing** | 不掉落任何东西。可用于创建带权重的掉落表 | `- nothing` |
| [ItemVariable](droptypes/itemvariable.md) | 掉落指定物品变量中定义的物品 | `- itemvariable{variable=caster.stolenitem} 1 1` |

### 示例 {#example}

本例有 20% 的概率掉落 3 颗钻石、60% 的概率执行命令，以及 12% 的概率掉落 100 到 600 点经验

```yaml
YourMob:
  Type: ZOMBIE
  Drops:
  - diamond 3 0.2
  - cmd{cmd="crate give <trigger.name> RewardCrate 1"} 1 0.6
  - exp 100to600 0.12
```

## 内联掉落物 {#in-line-drops}

对于非常基础的装备，可以添加行内物品数据，无须每次都创建 Mythic 物品。支持[行内物品配置](../mobs/equipment.md#in-line-items)中的所有物品数据！

```yaml
 Drops:
 - leather_chestplate{name="Dark Leather";lore="&8A vest made of darkened leather";color=BLACK} 1 1
```

### 示例 {#example-2}

下面的掉落配置会掉落一个带有 2 项附魔的熊猫玩家头颅，还会掉落 3 件带有名称、物品描述和附魔的钻石装备！

```yaml
  Drops:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==;enchants=WATER_WORKER:1,OXYGEN:3} 1 1
  - DIAMOND_CHESTPLATE{name="Panda<&sq>s Will";lore="A Panda must be vigilant";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} 1 1
  - DIAMOND_LEGGINGS{name="Panda<&sq>s Strength";lore="A Panda must be strong";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} 1 1
  - DIAMOND_BOOTS{name="Panda<&sq>s Speed";lore="A Panda must be fast";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,PROTECTION_FALL:4,DEPTH_STRIDER:3} 1 1
```
