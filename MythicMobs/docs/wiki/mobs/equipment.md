---
title: 装备
source_url: https://wiki.mythiccraft.io/mythicmobs/mobs/equipment
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 装备 {#equipment}

生物配置中的 Equipment 部分用于定义生物生成时携带的装备。装备只会在生物生成或重载时应用，之后可以使用 [Equip 机制](../skills/mechanics/equip.md)更换。

如果未启用 PreventOtherDrops 选项，生物死亡时会自然掉落其装备的所有物品。

如果希望生物不穿戴任何装备，可以使用 "PreventRandomEquipment" 选项，参见[生物选项](options.md)。另一种方法是给生物装备 AIR 等*占位物品*。

装备槽位也接受[掉落表](../drops/droptables.md#equipment-droptables)，可以由此创建“装备集合”，从中随机选择一件物品。例如，创建一个包含所有原版头盔的掉落表，再将其用于生物的装备部分，就能随机选取一顶头盔佩戴。

1. [语法](equipment.md#syntax)
   1. [物品](equipment.md#item)
   2. [槽位](equipment.md#slot)
2. [行内物品](equipment.md#in-line-items)
   1. [可用的行内属性](equipment.md#available-inline-attributes)
3. [MMOItems](equipment.md#mmoitems)
4. [示例](equipment.md#examples)

## 语法 {#syntax}

```yaml
internal_mobname:
  Type: <mobtype>
  Equipment:
  - <item> <slot>
  - <item> <slot>
  - ...
```

### Item {#item}

可以是 [MythicMobs 物品](https://wiki.mythiccraft.io/mythicmobs/Items/Items#internal_name)的名称，也可以是原版物品。

### 槽位 {#slot}

定义生物携带该物品的槽位。

| 槽位 | 说明 |
| --- | --- |
| HEAD | 头部槽位。接受普通头盔、玩家头颅，甚至方块类型。 |
| CHEST | 胸部槽位。只会显示胸甲，但可以携带任何物品。 |
| LEGS | 腿部槽位。只会显示护腿，但可以携带任何物品。 |
| FEET | 脚部槽位。只会显示靴子，但可以携带任何物品。 |
| HAND | 主手（右手）槽位。 |
| OFFHAND | 副手（左手）槽位。 |

```yaml
awesome_boss:
  Type: pig_zombie
  Equipment:
  - awesome_boss_helmet HEAD
  - diamond_sword HAND
```

## 行内物品 {#in-line-items}

对于非常基本的装备，可以添加行内物品数据，无需每次都创建 Mythic 物品。所有在 `Equipment` 下有效的行内物品数据，也都可以用于 [Drops](../drops/drops.md) 部分。

```yaml
 Equipment:
 - leather_chestplate{name="Dark Leather";lore="&8A vest made of darkened leather";color=BLACK} CHEST
```

### 可用的行内属性 {#available-inline-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| name | display, n, d | 物品的显示名称。 |  |
| data |  | 物品的“Data”，不要与 CustomModelData 混淆。 | 0 |
| model |  | 物品的 CustomModelData。 | 0 |
| amount | a | 物品数量。 | 1 |
| lore | l | 物品的描述。 |  |
| enchantments | enchants, ench, e | 物品的[附魔](../items/enchantments.md)列表。 |  |
| potioneffects | peffects, potion, pe | 物品为药水时，其[药水效果](../items/potions.md)列表。 |  |
| color | c, potioncolor, pcolor, pc | 物品为药水时，其颜色。 |  |
| skullowner |  | 物品为头颅时，其所有者。 |  |
| skulltexture |  | 物品为头颅时，其纹理的 SkinURL。 |  |

## MMOItems {#mmoitems}

要为生物装备 MMOItems 物品，请使用以下语法：

```yaml
  Equipment:
  - mmoitems{type=ARMOR;id=STEEL_HELMET} HEAD
  - mmoitems{type=ARMOR;id=STEEL_CHESTPLATE} CHEST
  - mmoitems{type=ARMOR;id=STEEL_LEGGINGS} LEGS
  - mmoitems{type=ARMOR;id=STEEL_BOOTS} FEET
  - mmoitems{type=SWORD;id=RUBY_SWORD} HAND
```

请注意，盔甲上的 MMO 属性不会在 MythicMobs 生物上生效，因此生物不会由此获得额外生命值、防御或攻击伤害。

## 示例 {#examples}

下面的示例会生成一个僵尸，在头部槽位装备熊猫玩家头颅。

```yaml
PandaZombie:
  Type: ZOMBIE
  Options:
    PreventSunburn: true
  Equipment:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==} HEAD
```

现在，为这个熊猫僵尸添加一些带有名称、描述和附魔的自定义盔甲。

```yaml
PandaZombie:
  Type: ZOMBIE
  Options:
    PreventSunburn: true
  Equipment:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==;enchants=WATER_WORKER:1,OXYGEN:3} HEAD
  - DIAMOND_CHESTPLATE{name="Panda<&sq>s Will";lore="A Panda must be vigilant";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} CHEST
  - DIAMOND_LEGGINGS{name="Panda<&sq>s Strength";lore="A Panda must be strong";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} LEGS
  - DIAMOND_BOOTS{name="Panda<&sq>s Speed";lore="A Panda must be fast";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,PROTECTION_FALL:4,DEPTH_STRIDER:3} FEET
```

最后，请记住，行内物品数据也可以用于掉落部分。击杀 PandaZombie 后，它会掉落所有物品，保留名称、描述和附魔，全程无需创建任何 Mythic 物品！

```yaml
PandaZombie:
  Type: ZOMBIE
  Options:
    PreventSunburn: true
  Equipment:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==;enchants=WATER_WORKER:1,OXYGEN:3} HEAD
  - DIAMOND_CHESTPLATE{name="Panda<&sq>s Will";lore="A Panda must be vigilant";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} CHEST
  - DIAMOND_LEGGINGS{name="Panda<&sq>s Strength";lore="A Panda must be strong";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} LEGS
  - DIAMOND_BOOTS{name="Panda<&sq>s Speed";lore="A Panda must be fast";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,PROTECTION_FALL:4,DEPTH_STRIDER:3} FEET
  Drops:
  - PLAYER_HEAD{skullTexture=eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjY0NjNlNjRjZTI5NzY0ZGIzY2I0NjgwNmNlZTYwNmFmYzI0YmRmMGNlMTRiNjY2MGMyNzBhOTZjNzg3NDI2In19fQ==;enchants=WATER_WORKER:1,OXYGEN:3} 1 1
  - DIAMOND_CHESTPLATE{name="Panda<&sq>s Will";lore="A Panda must be vigilant";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} 1 1
  - DIAMOND_LEGGINGS{name="Panda<&sq>s Strength";lore="A Panda must be strong";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,THORNS:2} 1 1
  - DIAMOND_BOOTS{name="Panda<&sq>s Speed";lore="A Panda must be fast";enchants=PROTECTION_ENVIRONMENTAL:4,DURABILITY:3,MENDING:1,PROTECTION_FALL:4,DEPTH_STRIDER:3} 1 1
```
