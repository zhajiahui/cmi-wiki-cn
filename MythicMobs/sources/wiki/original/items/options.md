All available options will be listed here.
These options must be placed under the `Options:` tag inside your item configurations.

```yml
example_item:
  Id: diamond
  Options:
    SomeOption: value
```

# Universal Options {#universal-options}

These options are applicable to all items:

#### Repairable {#repairable}

Sets whether the item can be repaired.  
When set to `false`, the repair cost of the item is set to maximum, and the RepairCost option is overridden.
In an anvil this blocks repairing the item with materials, combining it with another of the same item, and
applying enchanted books to it. Renaming is unaffected, and a grindstone resets the cost.  
Defaults to `true`.  
Not to be confused with the [Repairable](https://wiki.mythiccraft.io/mythicmobs/Items/Items#repairable) item component, which instead sets which
items can repair this one. Setting this to `false` also blocks that component, since the anvil rejects the
operation on cost before it checks the repair materials.

```yaml
  Options:
    Repairable: false
```

#### RepairCost {#repaircost}

Sets the repair cost of the item.  
If left at `-1`, the vanilla one will be used. Any other value is applied as-is, including other negative numbers.  
Defaults to `-1`.

```yaml
  # Not an option, apparently, but kept here because of repairable
  RepairCost: 10
```

#### Unbreakable {#unbreakable}

Sets the unbreakable tag on the item.  
Items with this set to true will not lose durability.  
Defaults to `false`.

```yaml
  Options:
    Unbreakable: true
```

#### Glint {#glint}

Adds the enchantment glint visual effect to an item
Defaults to `false`.

```yaml
  Options:
    Glint: true
```

#### HideFlags {#hideflags}

**Note: this feature does not exist >=1.20.5!** [Use this instead](https://wiki.mythiccraft.io/mythicmobs/Items/Items#hide)

Hides all the item flags, making things like enchants not visible in the item's lore (please note however that the item will still have an enchanted glow).  
Defaults to `false`.

```yaml
  Options:
    HideFlags: true
```

#### PreventStacking {#preventstacking}

Prevents the item from stacking to similar items.  
Defaults to `false`.

```yaml
  Options:
    PreventStacking: true
```

#### StackSize {#stacksize}

Sets the maximum stack size of the item in the inventory. Does not work when used alongside attributes.

```yaml
  Options:
    StackSize: 16
```

#### GenerateUUID {#generateuuid}

Applies a random UUID to the item upon generation. Useful to easily detect duped items. Enabling this option automatically prevents similar items from stacking, as they share different UUIDs.

```yaml
  Options:
    GenerateUUID: true
```

#### GenerateTimestamp {#generatetimestamp}

Applies the current unix time to the item on generation. Useful to backtrack the exact time an item was created. Enabling this option will prevent items from stacking if they were generated at different times.

```yaml
  Options:
    GenerateTimestamp: true
```

#### ItemModel {#itemmodel}

The model that should be applied to the item, which [works like this item component](https://minecraft.wiki/w/Data_component_format#item_model)

```yaml
MODELED_ITEM:
  Id: PAPER
  Display: '&dKing Helmet'
  Options:
    ItemModel: SomeModel
```

#### FireResistant {#fireresistant}

Whether the item is resistant to fire, as netherite is.  
Defaults to `false`.  
To resist other damage types, use [DamageResistant](https://wiki.mythiccraft.io/mythicmobs/Items/Items#damageresistant) instead of this option.

```yaml
  Options:
    FireResistant: true
```

#### DamageType {#damagetype}

Changes the [damage type](https://minecraft.wiki/w/Damage_type) the item deals.  
Used to handle the [damage_type item component](https://minecraft.wiki/w/Data_component_format#damage_type). (1.21.11+)

```yaml
  Options:
    DamageType: spear
```

# Playerheads {#playerheads}

Only applicable to playerhead type items

#### Player {#player}

Sets the texture of the player head.  
The value must be the IGN of the target player.  
Player heads must use data value 3 for this to work.

```yaml
  Options:
    Player: Herobrine
```

#### SkinTexture {#skintexture}

Also sets the texture of the player head, but instead uses a SkinURL.

> - Type into browser: <https://sessionserver.mojang.com/session/minecraft/profile/trimmeduuidofplayerhere>.
> - Use [http://mcuuid.net/](https://mcuuid.net/) to find the trimmed uuid of the player.

Player heads must use data value 3 for this to work.  
This option also supports hashes.

```yaml
  Options:
    SkinTexture: eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODdlMGFhOTQzM2RiYTliNzU5MzJhMTFkYzk0ZDQwNmJkZTE5ZTg2MzUxNDIxNDkyYjNlZDM3OGM4ZTFhN2NjIn19fQ==
```

### SkinURL {#skinurl}

The URL to the skin

```yaml
TestHeadURL:
  Id: PLAYER_HEAD
  Options:
    Placeable: true
    SkinURL: "https://textures.minecraft.net/texture/1c45ee6a2592e890f2aaa5a68aaa98f9e2f964327c15d18fdf7665c577af23cc" 
```

#### SkinID {#skinid}

The ID of the skin. It's the last part of the canonical [skin URL](https://wiki.mythiccraft.io/mythicmobs/Items/Options#skinurl)

```yaml
TestHeadID:
  Id: PLAYER_HEAD
  Options:
    Placeable: true
    SkinID: 1c45ee6a2592e890f2aaa5a68aaa98f9e2f964327c15d18fdf7665c577af23cc
```

# Dyeable Items {#dyeable-items}

#### Color {#color}

Dyes the armor piece to a color according to RGB settings. 0-255.  
Alternately can use a predefined color. Found [here](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html).  
Can pick colors using the Paint program on Windows. Open it up then choose "Edit Colors" to get your RGB value.  
Only usable on leather armor type, banners, shields and such.

```yaml
  Options:
    Color: RED
```

```yaml
  Options:
    Color: 102,102,153
```

# Examples {#examples}

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

Lots of possible options included:

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

An example of a firework rocket

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
