---
title: 物品选项
source_url: https://wiki.mythiccraft.io/mythicmobs/Items/Options
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 物品选项

这里列出了所有可用选项。这些选项必须放在物品配置的 `Options:` 下。

```yml
example_item:
  Id: diamond
  Options:
    SomeOption: value
```

# 通用选项 {#universal-options}

以下选项适用于所有物品：

#### Repairable {#repairable}

设置物品是否可以修复。设为 `false` 时，物品的修复成本会设为最大值，并覆盖 RepairCost 选项。在铁砧中，这会阻止使用材料修复物品、与另一个同类物品合并，以及应用附魔书。重命名不受影响，砂轮则会重置该成本。默认值为 `true`。请勿与 [Repairable](items.md#repairable) 物品组件混淆，后者设置哪些物品可以修复此物品。设为 `false` 同样会阻止该组件生效，因为铁砧在检查修复材料之前，就会因成本而拒绝操作。

```yaml
  Options:
    Repairable: false
```

#### RepairCost {#repaircost}

设置物品的修复成本。保留为 `-1` 时，会使用原版成本。其他任何值都会原样应用，包括其他负数。默认值为 `-1`。

```yaml
  # Not an option, apparently, but kept here because of repairable
  RepairCost: 10
```

#### Unbreakable {#unbreakable}

设置物品的不可破坏标签。设为 true 的物品不会损失耐久度。默认值为 `false`。

```yaml
  Options:
    Unbreakable: true
```

#### Glint {#glint}

为物品添加附魔光效。默认值为 `false`。

```yaml
  Options:
    Glint: true
```

#### HideFlags {#hideflags}

**注意：>=1.20.5 的版本中没有此功能！**[请改用此功能](items.md#hide)

隐藏所有物品标志，使附魔等信息不再出现在物品描述中（但请注意，物品仍会显示附魔光效）。默认值为 `false`。

```yaml
  Options:
    HideFlags: true
```

#### PreventStacking {#preventstacking}

防止此物品与同类物品堆叠。默认值为 `false`。

```yaml
  Options:
    PreventStacking: true
```

#### StackSize {#stacksize}

设置物品在物品栏中的最大堆叠数量。与属性一起使用时无效。

```yaml
  Options:
    StackSize: 16
```

#### GenerateUUID {#generateuuid}

物品生成时，为其应用随机 UUID，可用于方便地识别复制出的物品。启用后，由于各物品的 UUID 不同，同类物品会自动无法堆叠。

```yaml
  Options:
    GenerateUUID: true
```

#### GenerateTimestamp {#generatetimestamp}

物品生成时，记录当前 Unix 时间，可用于追溯物品创建的准确时间。启用后，在不同时间生成的物品将无法堆叠。

```yaml
  Options:
    GenerateTimestamp: true
```

#### ItemModel {#itemmodel}

要应用到物品上的模型，其[工作方式与此物品组件相同](https://minecraft.wiki/w/Data_component_format#item_model)。

```yaml
MODELED_ITEM:
  Id: PAPER
  Display: '&dKing Helmet'
  Options:
    ItemModel: SomeModel
```

#### FireResistant {#fireresistant}

物品是否像下界合金一样抗火。默认值为 `false`。要抵抗其他伤害类型，请使用 [DamageResistant](items.md#damageresistant) 代替此选项。

```yaml
  Options:
    FireResistant: true
```

#### DamageType {#damagetype}

修改物品造成的[伤害类型](https://minecraft.wiki/w/Damage_type)，用于处理 [damage_type 物品组件](https://minecraft.wiki/w/Data_component_format#damage_type)。（1.21.11+）

```yaml
  Options:
    DamageType: spear
```

# 玩家头颅 {#playerheads}

仅适用于玩家头颅类型的物品。

#### Player {#player}

设置玩家头颅的纹理。值必须是目标玩家的游戏内名称。玩家头颅必须使用数据值 3，此项才会生效。

```yaml
  Options:
    Player: Herobrine
```

#### SkinTexture {#skintexture}

同样用于设置玩家头颅纹理，但改用 SkinURL。

> - 在浏览器中输入：<https://sessionserver.mojang.com/session/minecraft/profile/trimmeduuidofplayerhere>。
> - 使用 [http://mcuuid.net/](https://mcuuid.net/) 查找玩家去掉连字符后的 UUID。

玩家头颅必须使用数据值 3，此项才会生效。此选项也支持哈希值。

```yaml
  Options:
    SkinTexture: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODdlMGFhOTQzM2RiYTliNzU5MzJhMTFkYzk0ZDQwNmJkZTE5ZTg2MzUxNDIxNDkyYjNlZDM3OGM4ZTFhN2NjIn19fQ==
```

### SkinURL {#skinurl}

皮肤的 URL。

```yaml
TestHeadURL:
  Id: PLAYER_HEAD
  Options:
    Placeable: true
    SkinURL: "https://textures.minecraft.net/texture/1c45ee6a2592e890f2aaa5a68aaa98f9e2f964327c15d18fdf7665c577af23cc" 
```

#### SkinID {#skinid}

皮肤的 ID，即标准[皮肤 URL](options.md#skinurl) 的最后一部分。

```yaml
TestHeadID:
  Id: PLAYER_HEAD
  Options:
    Placeable: true
    SkinID: 1c45ee6a2592e890f2aaa5a68aaa98f9e2f964327c15d18fdf7665c577af23cc
```

# 可染色物品 {#dyeable-items}

#### Color {#color}

根据 RGB 设置为盔甲部件染色，范围为 0-255。也可以使用预定义颜色，列表见[这里](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html)。可以通过 Windows 画图程序选择颜色：打开程序，选择“编辑颜色”，即可获取 RGB 值。仅适用于皮革盔甲、旗帜、盾牌等类型。

```yaml
  Options:
    Color: RED
```

```yaml
  Options:
    Color: 102,102,153
```

# 示例 {#examples}

```yaml
ClothSlippers:
  Id: 301
  Data: 0
  Display: '&fCloth Slippers'
  Lore:
  - ''
  - 'So Soft!'
  - ''
  Enchantments:
  - DURABILITY:1
  Options:
    Color: 200,200,200
```

包含许多可用选项：

```yaml
TestHead:
  Id: 397
  Data: 3
  Options:
    Player: Rickyling
```

```yaml
dat_item_though:
  Id: banner
  Data: 4
  Display: '&c&lThe Banner&r'
  Lore:
  - ''
  - '&rIt<&sq>s the perfect stone.'
  - '&cNever question that.'
  - ''
  Amount: 8
  Options:
    Color: 200,200,200
    Unbreakable: true
  Enchantments:
  - DURABILITY:1
  - ARROW_FIRE:10
```

烟花火箭示例。

```yaml
FireworkGoBoom:
  Id: FIREWORK_ROCKET
  Display: 'Rocket'
  Firework:
    Colors:
    - 255,0,255
    - 0,0,0
    FadeColors:
    - 200,0,0
    Flicker: true
    Trail: true
```
