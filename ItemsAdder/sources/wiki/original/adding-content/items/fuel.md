
# Fuel

## Creating the item

You must use a material which can already be smelted in vanilla Minecraft or it won't work.\
For example: `STICK`, `COAL`, `CHARCOAL` etc.

For example this configuration will make this item usable in **BLAST\_FURNACE** and will burn in **20 ticks** (**1 second**).

```yaml
  magic_fuel:
    display_name: Fuel
    material: COAL
    graphics:
      texture: item/diamond
    behaviours:
      fuel: 
        burn_ticks: 20
        machines:
          - BLAST_FURNACE
```

```yaml
  magic_fuel:
    display_name: Fuel
    resource:
      material: COAL
      generate: true
      textures:
      - item/diamond
    behaviours:
      fuel: 
        burn_ticks: 20
        machines:
          - BLAST_FURNACE
```
