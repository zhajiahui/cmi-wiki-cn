<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v6"></path><path d="M12 17h.01"></path></svg>Important

This is something important you should know.

The following is a list of the implemented particles, associated with their DataType group. Based on the DataType they have, the attributes that can be used with them change accordingly.

**The most up to date version of this list is always going to be in the spigot Javadoc located [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html)**

- [DataTypes](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Test-Page#datatypes)
  - [ItemStack](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Test-Page#itemstack)
  - [BlockData](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Test-Page#blockdata)
  - [MaterialData](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Test-Page#materialdata)
  - [DustOptions](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Test-Page#dustoptions)
  - [DustTransition](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Test-Page#dusttransition)
- [Particles](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Test-Page#particles)

# DataTypes {#datatypes}

## ItemStack {#itemstack}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| material | m | The material the particle will be based on | STONE |

## BlockData {#blockdata}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| material | m | The material the particle will be based on | STONE |

```yaml
  - effect:particles{particle=block_crack;material=COBBLESTONE}
```

## MaterialData {#materialdata}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| material | m | The material the particle will be based on | STONE |

## DustOptions {#dustoptions}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| color | c | The color of the particle | #FF0000 |
| size |  | The size of the particle | 1 |

## DustTransition {#dusttransition}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| color | c, color1, c1, fromcolor, fc | The color the particles starts as | #FF0000 |
| color2 | c2, tocolor, tc | The color the particles transitions to | #0000FF |
| size |  | The size of the particle | 1 |

##  {#section}

# Particles {#particles}

| Ash | Block Crack |  |  |
| --- | --- | --- | --- |
|  |  |  |  |

### ash {#ash}

![ash](https://imgur.com/ggCYoIB.gif)

##  {#section-2}

### block_crack {#block-crack}

![block_crack](https://imgur.com/bHpnok7.gif)

### [BlockData](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Test-Page#blockdata) {#blockdata-2}

### Aliases {#aliases}

- block
- blockcrack

##  {#section-3}

### block_dust {#block-dust}

![block_crack](https://imgur.com/oHIBddK.gif)

### [BlockData](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Test-Page#blockdata) {#blockdata-3}

### Aliases {#aliases-2}

- dust
- blockdust

##  {#section-4}

### shriek {#shriek}

![image](https://imgur.com/eSmLMUL.gif)

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| rotation | rot, r | the rotation of the particle | 0 |

##  {#section-5}

### sculk_charge {#sculk-charge}

![image](https://example.org/)

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| rotation | rot, r | the rotation of the particle | 0 |

### Aliases {#aliases-3}

- sculkcharge
