```yaml
 TNT:
      # When set to true will allow TNT and minecart with TNT to explode below 62 (default) level outside of residence
      # This will allow mining with TNT and more vanilla play
      ExplodeBelow: false
      level: 62
    Creeper:
      # When set to true will allow Creeper explode below 62 (default) level outside of residence
      # This will give more realistic gameplay
      ExplodeBelow: false
      level: 62
    Flow:
      # Level from which one to start lava and water flow blocking
      # This don't have effect in residence area
      Level: 63
      # With this set to true, lava flow outside residence is blocked
      NoLavaFlow: false
      # With this set to true, water flow outside residence is blocked
      NoWaterFlow: false
      Worlds:
      - LT_Craftas
    Place:
      # Level from which one to start block lava and water place
      # This don't have effect in residence area
      Level: 63
      # With this set to true, players can't place lava outside residence
      NoLavaPlace: true
      # With this set to true, players can't place water outside residence
      NoWaterPlace: true
      Worlds:
      - LT_Craft
    BlockFall:
      # With this set to true, falling blocks will be deleted if they will land in different area
      Use: true
      # Level from which one to start block block's fall
      # This don't have effect in residence area or outside
      Level: 62
      Worlds:
      - LT_Craft
    ResCleaning:
      # With this set to true, after player removes its residence, all blocks listed below, will be replaced with air blocks
      # Effective way to prevent residence creating near griefing target and then remove it
      Use: true
      # Level from which one you want to replace blocks
      Level: 63
      # Block list to be replaced
      # By default only water and lava will be replaced
      Blocks:
      - 8
      - 9
      - 10
      - 11
      Worlds:
      - LT_Craft
    Flags:
      # By setting this to true flags from list will be protected from change while there is some one inside residence besides owner
      # Protects in example from people inviting some one and changing pvp flag to true to kill them
      Prevent: true
      list:
      - pvp
```
