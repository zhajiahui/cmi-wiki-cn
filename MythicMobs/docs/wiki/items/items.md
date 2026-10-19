---
title: 物品
source_url: https://wiki.mythiccraft.io/mythicmobs/Items/Items
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 物品 {#items}

![](http://fs5.directupload.net/images/160306/or6m6n2s.jpg)

在 Mythic Mobs 中制作自定义物品相当简单。不过，与生物和技能不同，此插件制作的物品没有特殊或独有的选项。你通过 MythicMobs 创建的任何物品，也都可以通过 Minecraft 命令创建，只是使用 MythicMobs 配置制作会方便得多。

以下物品选项中，只有 `internal_name` 和 `Id` 是必填项，其他所有选项和属性都完全可选。

可以在 `\plugins\MythicMobs\Items` 文件夹中创建任意数量的文件，名称也可以任意设置，只要以 .yml 结尾即可。

## 物品配置详解 {#breaking-down-the-item-configuration}

#### Internal_Name {#internal-name}

这个字符串用于在 MythicMobs 内部引用物品，可以使用你喜欢的名称，但必须由字母和数字组成，**不允许有空格**。

```yml
example_item:
```

#### Id {#id}

物品使用的基础材质，可以是[这里](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html)列出的任意有效材质。

```yml
example_item:
  Id: leather_chestplate
```

#### 模板 {#template}

物品可以像生物一样使用[模板](../mobs/templates.md)，引用其他物品。

```yaml
MyItem:
  Template: MyOtherItem
```

```yaml
MyOtherItem:
  Template: YetAnotherItem, AndAnotherOne
```

#### 显示名称 {#display}

设置物品的显示名称。

```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
```

#### 物品描述 {#lore}

设置物品的描述。可以使用 `{min-max}`、`<random.#to#>` 或 `<random.float.#to#>` 生成随机数。

```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Lore:
    - <rainbow>This line is a rainbow</rainbow>
    - <red>This line should be red</red>
    - This is a random generated number > <random.-1to50>
    - <gradient:#5e4fa2:#f79459>A really nice gradient</gradient>
    - There are some symbols, like <&sq>, that should never be put as is into a configuration. Use a placeholder!
```

#### ItemName {#itemname}

用于设置 [item_name 物品组件](https://minecraft.wiki/w/Data_component_format#item_name)。与 [Display](items.md#display) 不同，它不会显示为斜体，在铁砧或谓词检查中也不会被视为自定义名称；支持与 [Display](items.md#display) 相同的颜色格式。

```yaml
DirtyDiamond:
  Id: diamond
  ItemName: <#DAA06D>Dirt
```

#### CustomModelData {#custommodeldata}

设置物品的 CustomModelData 组件。`Model` 也是 `CustomModelData` 的别名。

除了普通数字，也可以在值前添加 `type/` 前缀来指定其他数据类型，用法类似 [NBT](items.md#nbt)。CustomModelData 也可以是列表。

```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  CustomModelData: 5
```

```yml
example_item:
  Id: leather_chestplate
  CustomModelData:
  - float/1,2,3
  - string/something
  - boolean/true
```

#### MaxDurability {#maxdurability}

修改物品的最大使用次数。注意：物品必须不可堆叠。

```yaml
example_item:
  Id: diamond_sword
  MaxDurability: 600
```

#### 耐久度 {#durability}

设置要从物品中扣除的耐久度。下面的示例会让钻石剑拥有 1461 点耐久度，因为它默认有 1561 点。

```yml
example_item:
  Id: diamond_sword
  Durability: 100
  Display: <green>An Example Item</green>
```

#### 属性 {#attributes}

特殊字段，用于为特定盔甲槽位添加物品属性。参见[物品属性](attributes.md)。

```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Attributes:
    Chest:
      Health: 25
```

#### 数量 {#amount}

设置插件调用此物品时，默认给予的物品数量。

```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Amount: 1
```

#### 隐藏 {#hidden}

如果为 true，物品将不会出现在命令补全、`/mm items list` 和物品浏览菜单中，适用于模板物品和内部工具物品。仍然可以通过内部名称完整使用该物品。默认值为 `false`。

请注意，这是物品的顶层键，不是 `Options:` 下的键。

```yml
example_item:
  Id: leather_chestplate
  Hidden: true
```

#### 选项 {#options}

包含多个子选项的特殊字段。参见[物品选项](options.md)。

```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Options:
    AppendType: true
    Color: 255,0,0
```

#### 附魔 {#enchantments}

任何物品都可以具有任何附魔。[这里](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/enchantments/Enchantment.html)列出了可用附魔。物品附魔的配置方式另见[附魔](enchantments.md)页面。

```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Options:
    Color: 255,0,0
  Enchantments:
    - PROTECTION_ENVIRONMENTAL:2
    - THORNS:3
```

#### Hide {#hide}

特殊字段，用于隐藏物品提示中的特定内容。所有可用标志见：

- [使用 **Spigot** 时查看这里](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/ItemFlag.html)
- [使用 **Paper** 时查看这里](https://jd.papermc.io/paper/1.21.3/org/bukkit/inventory/ItemFlag.html)

> 如果服务器版本 <1.20.5，还可以使用 `HIDE_POTION_EFFECTS`。

```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Attributes:
    Chest:
      Health: 25
  Enchantments:
    - THORNS:3
  Options:
    Color: 255,0,0
  Hide:
    - ATTRIBUTES
    - ENCHANTS
```

#### PotionEffects {#potioneffects}

设置物品的药水效果。如果[基础物品](items.md#id)不是 `potion`、`splash_potion`、`lingering_potion` 或 `tipped_arrow`，这些效果就不会生效。参见[药水](potions.md)。

```yml
example_item:
  Id: potion
  Display: <#f99cb3>Pink potion
  Options:
    Color: 249,156,179
  PotionEffects:
    - CONFUSION 100 2
```

| 效果参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| duration | d | 效果的持续时间。 | 60 |
| level | l | 效果等级。实际等级为此值 +1。 | 0 |
| ambientparticles | ambient, a | 是否显示环境粒子。 | false |
| hasparticles | particles, p | 是否显示粒子。 | true |
| hasicon | icon, i | 是否显示效果图标。 | true |

#### BannerLayers {#bannerlayers}

设置旗帜或盾牌的旗帜图案层。参见[旗帜图案层](banner-layers.md)。

```yml
example_item:
  Id: yellow_banner
  BannerLayers:
    - RED BASE
    - WHITE CURLY_BORDER
    - WHITE STRIPE_CENTER
```

#### CanPlaceOn {#canplaceon}

设置玩家在冒险模式下可以将此物品放置在哪些方块上。条目可以是方块 ID，`minecraft:` 命名空间可省略；也可以是以 `#` 开头的方块标签，这会添加该标签中的所有方块。标签需要用引号括起来，因为 `#` 在 YAML 中表示注释的开始。

```yaml
MyCoolAnvil:
  Id: ANVIL
  CanPlaceOn:
  - diamond_block
  - '#minecraft:logs'
```

#### CanBreak {#canbreak}

设置玩家在冒险模式下可以用此物品破坏哪些方块。接受的条目与 [CanPlaceOn](items.md#canplaceon) 相同。

```yaml
MyCoolStick:
  Id: STICK
  CanBreak:
  - grass_block
  - diamond_block
  - obsidian
  - '#minecraft:wool'
```

#### BlockStates {#blockstates}

允许指定物品的方块状态。

```yaml
TestBlockStates:
  Material: OAK_SLAB
  Display: 'Waterlogged Slab'
  Options:
    Placeable: true # Crucible Option
  BlockStates:
  - type top
  - waterlogged true
```

#### Glider {#glider}

允许将物品用作鞘翅，用于处理物品的 [glider 组件](https://minecraft.wiki/w/Data_component_format/glider)。

```yaml
MyItem:
  Glider: true
```

> 不会读取此键的值：只要存在该键，物品就能滑翔，因此 `Glider: false` 仍会应用滑翔功能。
> 要禁用滑翔，请完全移除此键。

#### Group {#group}

设置物品在 `/mm items browse` 中所属的分组。

```yml
example_item:
  Id: leather_chestplate
  Display: <green>An Example Item</green>
  Group: 'Armor'
```

#### NBT {#nbt}

设置要为物品添加的 NBT 标签。可以借此与许多其他插件互通，也可以单纯用于保存自定义信息。

为物品添加 NBT 标签前，需要了解 [SNBT 格式](https://minecraft.wiki/NBT_format#SNBT_format)。在标签值前添加前缀，可以改变该值的类型：

| 前缀 | int/ | float/ | double/ | byte/ | bool/ | boolean/ |
| --- | --- | --- | --- | --- | --- | --- |

将以下 SNBT 转换为 Mythic 格式：`{name1:123,name2:"sometext1",name3:{subname1:456,subname2:"sometext2"}}`

```yml
example_item:
  Id: STICK
  NBT:
    name1: int/123
    name2: sometext1
    name3:
      subname1: int/456
      subname2: sometext2
```

```yml
#An item with MYTHIC_TYPE tag
example_item:
  Id: stick
  NBT:
    MYTHIC_TYPE: example_item
```

```yml
example_item:
  Id: diamond_sword
  NBT:
    CanDestroy:
      - stone
      - dirt
    Base:
      ATag: int/20
      SomeOtherTag: something
    SomeModifier:
      Value: double/0.25
      CanDoThis: boolean/true
    Denizen NBT:
      somedenizentag: a_string
```

```yml
another_example_item:
  Id: diamond_sword
  NBT:
    Base:
      ATag: 20
      SomeOtherTag: something
    GemSlots:
      RedGem: 0
    Denizen NBT:
      somedenizentag: a_string
```

#### Trim {#trim}

设置物品的盔甲纹饰。

```yaml
example_item:
  Material: GOLDEN_CHESTPLATE
  Options:
    Trim:
      Material: iron
      Pattern: wild
```

#### Firework {#firework}

设置 firework 或 firework_charge 物品的各项内容。每个选项的详细说明见[烟花](firework.md)。

```yml
example_item:
  Id: firework
  Firework:
    Colors:
    - 255,0,255
    - 0,0,0
    FadeColors:
    - 200,0,0
    Flicker: true
    Trail: true
```

#### Book {#book}

书的选项集合。

```yaml
SomeBook:
  Id: WRITTEN_BOOK
  Title: <green>How to make YouTube Videos
  Author: CarsonJF
  Pages:
  - "Page 1"
  - "Page 2\n\nwith some other lines"
  - "Page 3"
```

#### AttackRange {#attackrange}

修改物品的攻击范围，用于处理物品的 [attack_range 组件](https://minecraft.wiki/w/Data_component_format/attack_range)。

```yaml
AMythicItem:
  AttackRange:
    Min: 0
    Max: 4
    MinCreative: 0
    MaxCreative: 5
    HitboxMargin: 0.3
    MobFactor: 1
```

#### Consumable {#consumable}

允许食用物品，支持自定义动画和声音。用于处理物品的 [consumable 组件](https://minecraft.wiki/w/Data_component_format/consumable)。

```yaml
MyExampleItem:
  Consumable:
    ConsumeSeconds: 3
    HasParticles: false
    Animation: SPEAR
    Sound: item.crossbow.quick_charge_3
    ConsumeEffects:
    # The following are SPECIAL MECHANICS and are the only ones that you can use in this field
    - potion{type=absorption;d=200}
    - randomteleport{radius=5}
    - removePotion{type=wither}
    - clearAllEffects
    - sound{sound=entity.ghast.scream}     
```

#### DeathProtection {#deathprotection}

存在此项时，物品会像不死图腾一样，通过恢复一点生命值保护持有者免于死亡。用于处理物品的 [death_protection 组件](https://minecraft.wiki/w/Data_component_format/death_protection)。

```yaml
MyTotemItem:
  DeathProtection:
    ConsumeEffects: # Same as Consumable's
    - potion{type=absorption;d=200}
    - randomteleport{radius=5}
    - removePotion{type=wither}
    - clearAllEffects
    - sound{sound=entity.ghast.scream}     
```

#### Food {#food}

用于处理物品的 [food 组件](https://minecraft.wiki/w/Data_component_format/food)。要实际消耗原本不可消耗的物品，必须设置 [Consumable](items.md#consumable)。

```yaml
MyThiccApple:
  Material: apple
  Display: 'Red Delicious'
  Food:
    Nutrition: 10
    Saturation: 20
    CanAlwaysEat: false
```

```yaml
NetheritePops:
  Material: NETHERITE_SCRAP
  Display: 'Delicious Scraps'
  Consumable:
    ConsumeSeconds: 0.5
    HasParticles: true
    Animation: EAT
  Food:
    Nutrition: 20
    Saturation: 20
    CanAlwaysEat: true
```

#### Equippable {#equippable}

用于处理物品的 [equippable 物品组件](https://minecraft.wiki/w/Data_component_format/equippable)。

| 标签 | 说明 | 默认值 |
| --- | --- | --- |
| Model | 装备时使用的装备模型资源位置。未指定命名空间时，默认为 `minecraft:`。 |  |
| Slot | 放置物品的[槽位](../skills/equipslot.md)。未指定时，插件会根据基础材质是否包含以下字符串来尝试推断：`_HELMET`、`_CHESTPLATE`、`_LEGGINGS`、`_BOOTS` 或 `SHIELD`。 |  |
| CameraOverlay | 装备时使用的叠加纹理资源位置。未指定命名空间时，默认为 `minecraft:`。 |  |
| Dispensable | 物品是否可由发射器发射。 | true |
| Swappable | 是否可以通过右键将物品装备到对应槽位。 | true |
| DamageOnHurt | 穿戴此物品的实体受伤时，物品是否损失耐久。 | true |
| EquipSound | 装备物品时播放的声音。 | item.armor.equip_generic |
| EntityTypes | 可以装备此物品的实体类型列表。 |  |
| EquipOnInteract | 对生物使用此物品时，是否将其装备到该生物身上（1.21.5+）。 | false |
| CanBeSheared | 是否可以用剪刀移除生物穿戴的此物品（1.21.6+）。 | false |
| ShearSound | 用剪刀剪下物品时播放的声音（1.21.6+）。 | item.shears.snip |

```yaml
KING_HELMET:
  Id: PAPER
  Display: '&dKing Helmet'
  Equippable:
    Model: yourNamespace:thePathToYourCustomModel
    Slot: HEAD
    CameraOverlay: yournamespace:thePathToYourTexture
    Dispensable: true
    Swappable: true
    DamageOnHurt: true
    EquipSound: "item.armor.equip_iron"
    EntityTypes: 
      - "PLAYER"
    EquipOnInteract: true
    CanBeSheared: true
    ShearSound: "entity.sheep.shear"
```

#### UseCooldown {#usecooldown}

用于处理物品的 [use_cooldown 物品组件](https://minecraft.wiki/w/Data_component_format/use_cooldown)。

| 标签 | 说明 | 默认值 |
| --- | --- | --- |
| CooldownGroup | 用于标识此冷却组的唯一资源位置。设置后，物品会归入该冷却组，不再与其基础物品类型共用冷却，而是与同一冷却组中的其他物品共用冷却。未指定命名空间时，默认为 `minecraft:`。 |  |
| CooldownSeconds | 冷却时长，单位为秒。必须为整数，因此无法精确到刻。 |  |

```yaml
ExampleItem:
  Material: STICK
  UseCooldown:
    CooldownGroup: coolwands # write only in lowercase!
    CooldownSeconds: 3
```

#### Tool {#tool}

用于处理物品的 [tool 物品组件](https://minecraft.wiki/w/Data_component_format/tool)。

| 标签 | 说明 | 默认值 |
| --- | --- | --- |
| DamagePerBlock | 每次用此工具破坏方块时扣除的耐久。必须为非负整数。 |  |
| DefaultMiningSpeed | 此工具的默认挖掘速度，在没有规则覆盖时使用。 | 1.0 |
| Rules | 工具的规则列表。 |  |

| 规则参数 | 说明 | 默认值 |
| --- | --- | --- |
| materials | 此规则适用的材质和方块标签列表，以逗号分隔。标签以 `#` 开头，可以使用任意命名空间，例如 `#minecraft:logs`。不带 `#` 的单个条目也会尝试按原版标签解析。 |  |
| speed | 被挖掘的材质匹配时，覆盖默认挖掘速度。 | 1.0 |
| isCorrectForBlock | 被挖掘的材质匹配时，覆盖此工具是否被视为合适工具的判定；该判定决定是否以最高效率挖掘，以及在方块战利品表要求合适工具时是否掉落物品。 | false |

```yaml
OBSIDIAN_BREAKER:
  Id: COD
  Display: '&8Obsidian Breaker'
  Tool:
    DamagePerBlock: 1
    DefaultMiningSpeed: 0.0
    Rules:
      - materials: "OBSIDIAN,CRYING_OBSIDIAN"
        speed: 10000.0
        isCorrectForBlock: true
```

```yaml
TREE_BREAKER:
  Id: COD
  Display: '&aTree Breaker'
  Tool:
    DamagePerBlock: 1
    DefaultMiningSpeed: 0.0
    Rules:
      - materials: "completes_find_tree_tutorial" # Example of a Tag being used
        speed: 10000.0
        isCorrectForBlock: true
```

```yaml
LUMBER_AXE:
  Id: IRON_AXE
  Tool:
    Rules:
      - materials: "#minecraft:logs,STONE"
        speed: 8
        isCorrectForBlock: true
```

#### TooltipStyle {#tooltipstyle}

用于处理物品的[提示框样式](https://minecraft.wiki/w/Data_component_format/tooltip_style)。它指定提示框背景和边框的自定义精灵的资源位置，引用的纹理为 `/assets/<namespace>/textures/gui/sprites/tooltip/<id>_background` 和 `/assets/<namespace>/textures/gui/sprites/tooltip/<id>_frame`，对应的 TooltipStyle 值可写为：

```yaml
ExampleItem:
  Id: STONE_SWORD
  TooltipStyle: minecraft:verycooltooltip
```

#### Spawner {#spawner}

配置 SPAWNER 物品的选项。

```yaml
TestSpawner:
  Material: SPAWNER
  Display: 'Testing Spawner'
  Spawner:
    Delay: 0
    MinSpawnDelay: 20
    MaxSpawnDelay: 80
    RequiredPlayerRange: 16
    SpawnCount: 4
    SpawnRange: 8
    MaxNearbyEntities: 8
    Mobs:
    - Type: TestingDummy
      Weight: 5
      MinBlockLight: 10
      MaxBlockLight: 10
      MinSkyLight: 10
      MaxSkyLight: 10
```

#### DropOptions {#dropoptions}

让物品掉落时自带特定的[花式掉落选项](../drops/fancydrops.md#drop-attributes)。

```yaml
LegendarySword:
  Id: DIAMOND_SWORD
  Display: '<red>Legendary Sword'
  DropOptions:
    # Default drop settings for this item
    DropGlowColor: GOLD
    DropBeamColor: '#FFA500' # Orange beam
    DropLootsplosion: true
    DropHologram: true
    DropVFX: true
    DropVFXMaterial: DIAMOND
    DropVFXData: 0
    DropVFXColor: '#55FF55'
    DropBillboarding: CENTER
    DropBrightness: 15
    DropClientSide: false
```

#### Repairable {#repairable}

设置哪些物品可以在铁砧中修复此物品，也适用于修复已驯服的狼在身体槽位装备的物品。用于处理物品的 [repairable 组件](https://minecraft.wiki/w/Data_component_format/repairable)。接受物品 ID 列表、单个物品 ID，或以 `#` 开头的物品标签。未指定命名空间的条目会被视为使用 `minecraft:`。

```yaml
MySword:
  Id: DIAMOND_SWORD
  Repairable:
  - EMERALD
  - GOLD_INGOT

MyOtherSword:
  Id: DIAMOND_SWORD
  Repairable: '#planks'
```

> 请勿与 [Options.Repairable](options.md#repairable) 混淆，后者控制
> 物品是否可以修复。将该选项设为 `false`，会将物品的修复成本设为最大值，使得
> 铁砧尚未检查这些材料就会停止操作，因此不应将两者结合使用。

#### Rarity {#rarity}

设置物品的稀有度。可以为 COMMON、UNCOMMON、RARE 和 EPIC。

```yaml
TheMusical:
  Rarity: EPIC
  Material: COMPASS
```

#### PiercingWeapon {#piercingweapon}

适用于 Minecraft 1.21.11 及更新版本。让物品的近战攻击能够穿透目标。`Knockback` 控制是否击退目标，`Dismounts` 控制被击中的目标是否脱离坐骑。

用于处理 [piercing_weapon 物品组件](https://minecraft.wiki/w/Data_component_format#piercing_weapon)。

```yaml
MyThiccSpear:
  PiercingWeapon:
    Knockback: true
    Dismounts: false
    Sound: item.crossbow.shoot
    HitSound: entity.arrow.hit_player
```

#### KineticWeapon {#kineticweapon}

适用于 Minecraft 1.21.11 及更新版本。允许物品进行动能冲锋攻击。其条件组控制攻击在什么情况下能够伤害、击退目标，或使其脱离坐骑。

用于处理 [kinetic_weapon 物品组件](https://minecraft.wiki/w/Data_component_format#kinetic_weapon)。

| 标签 | 说明 | 默认值 |
| --- | --- | --- |
| ContactCooldownTicks | 武器再次接触目标前的冷却时间，单位为刻。 | 10 |
| DelayTicks | 动能攻击开始前的延迟，单位为刻。 | 0 |
| ForwardMovement | 攻击期间施加的向前移动量。 | 0.0 |
| DamageMultiplier | 应用于攻击伤害的倍率。 | 1.0 |
| Sound | 使用动能攻击时播放的声音。 | 可选 |
| HitSound | 动能攻击命中目标时播放的声音。 | 可选 |
| DamageConditions | 攻击可以对目标造成伤害的条件。 |  |
| KnockbackConditions | 攻击可以击退目标的条件。 |  |
| DismountConditions | 攻击可以使目标下坐骑的条件。 |  |

`DamageConditions`、`KnockbackConditions` 和 `DismountConditions` 使用以下选项：

| 条件参数 | 说明 | 默认值 |
| --- | --- | --- |
| MaxDurationTicks | 条件可生效的最长攻击持续时间，单位为刻。 | 必填 |
| MinSpeed | 条件生效所需的最低速度。 | 0.0 |
| MinRelativeSpeed | 条件生效所需的相对于目标的最低速度。 | 0.0 |

```yaml
MyThiccSpear:
  KineticWeapon:
    ContactCooldownTicks: 10
    DelayTicks: 5
    ForwardMovement: 0.9
    DamageMultiplier: 1.25
    Sound: item.mace.smash_ground
    HitSound: item.mace.smash_air
    DamageConditions:
      MaxDurationTicks: 20
      MinSpeed: 0.6
      MinRelativeSpeed: 0.3
    KnockbackConditions:
      MaxDurationTicks: 10
      MinSpeed: 0.4
      MinRelativeSpeed: 0.2
    DismountConditions:
      MaxDurationTicks: 5
      MinSpeed: 0.2
      MinRelativeSpeed: 0.1
```

#### OminousBottleAmplifier {#ominousbottleamplifier}

设置不祥之瓶给予的不祥之兆效果的增幅等级。

```yaml
MyThiccOminousBottle:
  Type: OMINOUS_BOTTLE
  OminousBottleAmplifier: 4
```

#### PotDecorations {#potdecorations}

设置饰纹陶罐每个侧面显示的物品，也支持掉落自定义陶片。

用于处理 [pot_decorations 物品组件](https://minecraft.wiki/w/Damage_type)。

```yaml
MyThiccPot:
  PotDecorations:
    Back: brick
    Left: arms_up_pottery_sherd
    Right: skull_pottery_sherd
    Front: prize_pottery_sherd
```

#### UseRemainder {#useremainder}

设置此物品使用后留下的物品。仅适用于原版物品。

```yaml
Item:
  Id: pumpkin_pie
  UseRemainder: sugar
```

要留下多个物品，请使用包含 `Item` 和 `Amount` 的配置节：

```yaml
StewPot:
  Id: mushroom_stew
  UseRemainder:
    Item: bowl
    Amount: 2
```

#### Weapon {#weapon}

让物品作为武器使用。`ItemDamagePerAttack` 是每次攻击损失的耐久度，`DisableBlockingForSeconds` 是攻击时使格挡物品失效的时长。

用于处理 [weapon 物品组件](https://minecraft.wiki/w/Data_component_format#weapon)。

```yaml
MyThiccWeapon:
  Id: stick
  Weapon:
    ItemDamagePerAttack: 2
    DisableBlockingForSeconds: 0.5
```

#### Enchantability {#enchantability}

设置物品在附魔台中的附魔能力值。

```yaml
MyThiccEnchant:
  Enchantability: 5
```

#### BreakSound {#breaksound}

设置物品耐久耗尽并损坏时播放的声音。

```yaml
MyThiccBreakSound:
  BreakSound: "minecraft:block.glass.break"
```

#### JukeboxPlayable {#jukeboxplayable}

设置将物品插入唱片机时播放的歌曲。

用于处理 [jukebox_playable 物品组件](https://minecraft.wiki/w/Data_component_format#jukebox_playable)。

```yaml
MyThiccJukeboxSong:
  Id: fermented_spider_eye  
  JukeboxPlayable: "minecraft:thirteen"
```

#### NoteBlockSound {#noteblocksound}

设置此物品位于音符盒上方的玩家头颅中时，音符盒播放的声音。

用于处理 [note_block_sound 物品组件](https://minecraft.wiki/w/Data_component_format#note_block_sound)。

```yaml
MyThiccNoteHead:
  Id: player_head
  NoteBlockSound: "minecraft:block.note_block.harp"
```

#### BlocksAttacks {#blocksattacks}

允许物品格挡攻击。减伤条目用于选择受影响的[伤害类型](https://minecraft.wiki/w/Damage_type)，并控制格挡的伤害量和角度。`ItemDamage` 控制格挡时受到的耐久损耗。

用于处理 [blocks_attacks 物品组件](https://minecraft.wiki/w/Data_component_format#blocks_attacks)。

| 标签 | 说明 | 默认值 |
| --- | --- | --- |
| BlockDelaySeconds | 格挡生效前的延迟，单位为秒。 | 0.0 |
| DisableCooldownScale | 物品被攻击禁用时，对其冷却时间应用的倍率。设为 0 后，此物品永远不会被攻击禁用。 | 1.0 |
| DamageReductions | 控制格挡哪些伤害及格挡量的规则列表。 | 完全格挡所有伤害。 |
| ItemDamage | 控制格挡物品受到的耐久损耗。 | 必填 |
| HitBlockSound | 成功格挡攻击时播放的声音。 | None |
| DisabledSound | 格挡被禁用时播放的声音。 | None |
| BypassedBy | 会绕过此组件的伤害类型或伤害类型标签。 | None |

`DamageReductions` 中的每个条目支持以下选项：

| 伤害减免参数 | 说明 | 默认值 |
| --- | --- | --- |
| Type | 此规则适用的[伤害类型](https://minecraft.wiki/w/Damage_type)列表。 | 所有伤害类型 |
| Base | 计算格挡伤害时使用的固定值。 | 必填 |
| Factor | 计算格挡伤害时使用的倍率。 | 必填 |
| HorizontalBlockingAngle | 可以格挡攻击的水平角度范围，单位为度。 | 90.0 |

`ItemDamage` 支持以下选项：

| 物品伤害参数 | 说明 | 默认值 |
| --- | --- | --- |
| Threshold | 计算耐久损耗时使用的传入伤害阈值。 | 0.0 |
| Base | 计算耐久损耗时使用的固定值。 | 0.0 |
| Factor | 计算耐久损耗时使用的倍率。 | 1.5 |

```yaml
MyThiccShield:
  Id: stick
  BlocksAttacks:
    BlockDelaySeconds: 0
    DisableCooldownScale: 1

    DamageReductions:
    - Type: "#minecraft:is_projectile"
      Base: 0
      Factor: 1
      HorizontalBlockingAngle: 90

    - Type:
      - "minecraft:player_attack"
      - "minecraft:mob_attack"
      Base: 0
      Factor: 0.8
      HorizontalBlockingAngle: 90

    ItemDamage:
      Threshold: 0
      Base: 0
      Factor: 1.5

    HitBlockSound: "minecraft:item.shield.block"
    DisabledSound: "minecraft:item.shield.break"
    BypassedBy: "#minecraft:bypasses_shields"
```

#### UseEffects {#useeffects}

控制玩家按住右键使用物品时发生的行为。（1.21.11+）

用于处理 [use_effects 物品组件](https://minecraft.wiki/w/Data_component_format#use_effects)。

```yaml
MyThiccEffect:
  Id: stick
  UseEffects:
    CanSprint: true #Defauts to `false`
    InteracVibrations: false #Defaults to `true`
    SpeedMultiplier: 1.0 #Defaults to `0.2`
```

#### SwingAnimation {#swinganimation}

控制物品的攻击挥动动画。（1.21.11+）

用于处理 [swing_animation 物品组件](https://minecraft.wiki/w/Data_component_format#swing_animation)。

```yaml
MyThiccSwing:
  Id: stick
  SwingAnimation:
    Type: WHACK #Defaults to `WHACK` but `NONE` and `STAB` are also available
    Duration: 12 #Defaults to `6`. Measured in Ticks.
```

#### MinimumAttackCharge {#minimumattackcharge}

一个从 `0.0` 到 `1.0` 的数值。只有攻击冷却至少恢复到此比例后，物品才能攻击。原版长矛使用 `1.0`，因此只能在完全蓄满时攻击。（1.21.11+）

用于处理 [minimum_attack_charge 物品组件](https://minecraft.wiki/w/Data_component_format#minimum_attack_charge)。

```yaml
MyThiccCharge:
  Id: stick
  MinimumAttackCharge: 1.0
```

#### UnsetComponents {#unsetcomponents}

移除基础物品默认具有的[数据组件](https://minecraft.wiki/w/Data_component_format)，例如牛排的食物组件。条目为组件 ID，`minecraft:` 命名空间可省略。即使该物品的其他 MythicMobs 选项设置了被移除的组件，它也会保持移除状态。无法移除 `custom_data`，因为 Mythic 在其中存储物品数据。（Paper 1.21.3+）

```yaml
InedibleSteak:
  Id: cooked_beef
  UnsetComponents:
  - food
  - consumable
```

#### DamageResistant {#damageresistant}

让物品抵抗某个伤害类型标签中的所有伤害类型，效果类似下界合金抗火：掉落的物品不会被这些伤害摧毁。`#` 可省略。也可以写为 `Options.DamageResistant`。（1.21.2+）

`DamageResistant: is_fire` 与 [Options.FireResistant](options.md#fireresistant) 的作用相同。只使用其中一项：若同时设置，会采用 `DamageResistant` 并记录错误。

用于处理 [damage_resistant 物品组件](https://minecraft.wiki/w/Data_component_format#damage_resistant)。

```yaml
BlastProofDiamond:
  Id: diamond
  DamageResistant: '#minecraft:is_explosion'
```

#### PaintingVariant {#paintingvariant}

设置 `painting` 物品放置的具体[画](https://minecraft.wiki/w/Painting)，而不是随机选择。`minecraft:` 命名空间可省略。也可以写为 `Options.PaintingVariant`。（1.21.5+）

用于处理 [painting/variant 物品组件](https://minecraft.wiki/w/Data_component_format#painting/variant)。

```yaml
SunsetPainting:
  Id: painting
  PaintingVariant: sunset
```

> [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Items/Paintings) 的画物品会根据自身定义的画，自动设置此项。

#### Compostable {#compostable}

允许将物品放入堆肥桶。`Layers` 表示每个物品增加的层数，也可以填写原版堆肥概率的 ID，例如 `minecraft:compostable/medium`。如果基础物品本身已可堆肥，可以省略此项以保留原版数值。（26.3+）

用于处理 [compostable 物品组件](https://minecraft.wiki/w/Data_component_format#compostable)。

```yaml
CompostableLeaf:
  Id: paper
  Compostable:
    Layers: minecraft:compostable/medium
```

#### CookingFuel {#cookingfuel}

允许物品在熔炉、烟熏炉或高炉中作为燃料燃烧。（26.3+）

用于处理 [cooking_fuel 物品组件](https://minecraft.wiki/w/Data_component_format#cooking_fuel)。

| 标签 | 说明 | 默认值 |
| --- | --- | --- |
| BurnTime | 燃烧时间，单位为刻；也可以填写 `minecraft:cooking/time_coal` 这样的原版燃烧时间 ID。 | 基础物品的燃烧时间。基础物品不是燃料时必填。 |
| SpeedMultiplier | 燃烧期间物品的烹饪速度，也可以填写原版 ID。 | 使用基础物品的值，否则使用 `minecraft:cooking/speed_default`；此值在烟熏炉和高炉中会翻倍。 |

```yaml
Ember:
  Id: paper
  CookingFuel:
    BurnTime: 1600
    SpeedMultiplier: 1.5
```

#### BrewingFuel {#brewingfuel}

允许物品作为酿造台燃料。（26.3+）

用于处理 [brewing_fuel 物品组件](https://minecraft.wiki/w/Data_component_format#brewing_fuel)。

| 标签 | 说明 | 默认值 |
| --- | --- | --- |
| Uses | 每个物品可支持的酿造次数，也可以填写 `minecraft:brewing/uses_default` 这样的原版 ID。 | 基础物品的使用次数。基础物品不是酿造燃料时必填。 |
| SpeedMultiplier | 药水酿造速度，也可以填写原版 ID。 | 使用基础物品的值，否则使用 `minecraft:brewing/speed_default`。 |

```yaml
FlameDust:
  Id: paper
  BrewingFuel:
    Uses: 20
```

## 示例 {#examples}

更多物品示例见[示例](../examples/common-examples.md#items)部分。
