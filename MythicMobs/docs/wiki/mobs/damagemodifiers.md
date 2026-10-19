---
title: 伤害修正
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/DamageModifiers
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 伤害修正 {#damage-modifiers}

## 伤害修正 {#damage-modifiers}

伤害修正是可以添加到 MythicMobs 生物上的属性，用于增加或减少它们受到的各种来源的伤害。

假设实体受到类型为 `ENTITY_ATTACK`、数值为 `10` 的伤害。根据其对应 DamageModifier 的值，会产生不同结果：

- `A value > 0`（值大于 0）：伤害量乘以该值。如果值为 `2`，伤害会翻倍；如果为 `0.5`，伤害会减半。
- `A value of 0`（值为 0）：伤害事件不会造成任何伤害，但仍会播放受伤动画。
- `A value < 0`（值小于 0）：对应的伤害事件会被取消，施法者恢复的生命值等于原始伤害乘以伤害修正值的绝对值。如果值为 `-2`，施法者会恢复 `20` 点生命值；如果为 `-0.1`，则恢复 `1` 点生命值。

正常情况下，其中某些类型不会对特定生物生效，例如 SUICIDE，因为没有生物会自然自杀。伤害修正完全可选，只需添加你想使用的类型。

可用伤害类型的完整列表见 [Spigot Javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)。

## 选项 {#options}

| 修正器 | 说明 |
| --- | --- |
| BLOCK_EXPLOSION | 方块爆炸时，处于爆炸范围内造成的伤害。 |
| CAMPFIRE | 实体踩到 `CAMPFIRE` 或 `SOUL_CAMPFIRE` 时造成的伤害。 |
| CONTACT | 实体接触仙人掌、滴水石锥（石笋）或浆果丛等方块时造成的伤害。 |
| CRAMMING | 实体因 maxEntityCramming 游戏规则而与过多实体挤在一起时造成的伤害。 |
| CUSTOM | 自定义伤害。 |
| DRAGON_BREATH | 龙喷火造成的伤害。 |
| DROWNING | 在水中耗尽氧气造成的伤害。 |
| DRYOUT | 本应在水中的实体离开水时造成的伤害。 |
| ENTITY_ATTACK | 实体攻击另一个实体时造成的伤害。 |
| ENTITY_EXPLOSION | 苦力怕等实体爆炸时，处于爆炸范围内造成的伤害。 |
| ENTITY_SWEEP_ATTACK | 实体以横扫攻击命中另一个实体时造成的伤害。 |
| FALL | 实体从超过 3 格的高度摔落时造成的伤害。 |
| FALLING_BLOCK | 被能够造成伤害的下落方块击中时造成的伤害。 |
| FIRE | 直接接触火造成的伤害。 |
| FIRE_TICK | 被火点燃后，持续燃烧造成的伤害。 |
| FLY_INTO_WALL | 实体撞墙时造成的伤害。 |
| FREEZE | 冰冻造成的伤害。 |
| HOT_FLOOR | 实体踩到 `MAGMA_BLOCK` 时造成的伤害。 |
| KILL | /kill 命令造成的伤害。 |
| LAVA | 直接接触熔岩造成的伤害。 |
| LIGHTNING | 被闪电击中造成的伤害。 |
| MAGIC | 被伤害药水或法术击中造成的伤害。 |
| MELTING | 雪傀儡融化造成的伤害。 |
| POISON | 持续中毒效果造成的伤害。 |
| PROJECTILE | 被弹射物攻击时造成的伤害。 |
| SONIC_BOOM | `Warden` 的音波攻击造成的伤害。 |
| STARVATION | 饥饿值耗尽后挨饿造成的伤害。 |
| SUFFOCATION | 被置于方块内部造成的伤害。 |
| SUICIDE | 自杀造成的伤害。 |
| THORNS | 荆棘附魔反击其他攻击时造成的伤害。 |
| VOID | 掉入虚空造成的伤害。 |
| WITHER | 凋零药水效果造成的伤害。 |
| WORLD_BORDER | 世界边界造成的伤害。 |

## 示例 {#examples}

注意：修正值为 1 时，生物会受到该来源的正常伤害。大于 1 时，受到的伤害会乘以该值；小于 1 时，受到的伤害会按该值减少；为 0 时，生物免疫该伤害来源。负值会让生物因该类型伤害而恢复生命。请注意，如果生物本身就免疫该伤害，此功能不会生效，例如铁傀儡免疫 FALL，烈焰人免疫 FIRE、FIRE_TICK 或 LAVA 等。

第一个示例中的装甲僵尸只是一个基本 MythicMob，没有添加其他内容。

```yaml
ArmoredZombie:
  Mobtype: zombie
  Display: '&aArmored Zombie'
  Health: 40
  Damage: 6
```

给它添加 DamageModifiers 属性后，就可以调整弱点和抗性。在这个示例中，我们会让近战和投射物攻击对装甲僵尸只造成通常伤害的 75%。

```yaml
ArmoredZombie:
  Mobtype: zombie
  Display: '&aArmored Zombie'
  Health: 40
  Damage: 6
  DamageModifiers:
  - ENTITY_ATTACK 0.75
  - PROJECTILE 0.75
```

现在，僵尸已经有了伤害抗性。它受到的任何近战和投射物伤害都会减少 25%，包括来自玩家和其他生物的伤害。不过现在它似乎有些过强，所以再给它添加一个弱点。

```yaml
ArmoredZombie:
  Mobtype: zombie
  Display: '&aArmored Zombie'
  Health: 40
  Damage: 6
  DamageModifiers:
  - ENTITY_ATTACK 0.75
  - PROJECTILE 0.75
  - MAGIC 1.25
```

装甲僵尸仍然对投射物和近战攻击有很好的防护，但作为补偿，我们让它更容易受到魔法（喷溅型治疗药水）的伤害。

第二个示例是火元素。这个生物不仅不会受到燃烧伤害，站在火中还会恢复生命，在熔岩中则会恢复更多。注意：这不适用于下界生物，因为它们根本不会受到火焰伤害，因此无法修改其火焰和熔岩伤害。

```yaml
FireElemental:
  Mobtype: zombie
  Display: '&cFire Elemental'
  Health: 20
  DamageModifiers:
  - FIRE -1
  - LAVA -4
  - FIRE_TICK 0
```
