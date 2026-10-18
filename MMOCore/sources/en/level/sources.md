# 🪴 Experience Sources {#🪴-experience-sources}

An experience source gives you experience for certain professions when certain events occur. Each experience source has its own specific parameters that you can specify in the config with `exp_source_name{param1=P1;param2=p2..}`. You must specify the parameter `amount=min-max` corresponding to the bounds between which the amount of experience will be randomly chosen each time.

You can also use experience sources for your main classes.

## Examples {#examples}

Let's have a look at an example. These are the default experience sources for the *Woodcutting* profession. It basically gives the player anywhere from 1 to 3 experience points whenever he cuts a log.

```yml
exp-sources:
- 'mineblock{type=OAK_LOG;amount=1-3}'
- 'mineblock{type=SPRUCE_LOG;amount=1-3}'
- 'mineblock{type=BIRCH_LOG;amount=1-3}'
- 'mineblock{type=JUNGLE_LOG;amount=1-3}'
- 'mineblock{type=ACACIA_LOG;amount=1-3}'
- 'mineblock{type=BIRCH_LOG;amount=1-3}'
- 'mineblock{type=DARK_OAK_LOG;amount=1-3}'
```

These are the default experience sources for the farming profession, which grants some experience points whenever the player harvests any type of crops.

```yml
exp-sources:
- 'mineblock{type=CARROTS;amount=1-3;crop=true;player-placed=true}'
- 'mineblock{type=POTATOES;amount=1-3;crop=true;player-placed=true}'
- 'mineblock{type=WHEAT;amount=1-3;crop=true;player-placed=true}'
```

`crop=true` means that it'll only grant EXP once it's at its full growth stage. `player-placed=true` means that it'll grant EXP even if the player placed the block

## Experience Sources Tables {#experience-sources-tables}

You can create experiences-sources tables in `exp-sources.yml`. This file allows you to create list of exp sources that you can use anywhere else in the plugin. Here is an example:

```yml
exp-sources-1: 
  - 'damagedealt{type=physical;amount=250}'
  - 'move{type=WALK;amount=300}'
  # anything from 'exp-sources-2'
  - 'from{source=exp-sources-2}'

exp-sources-2:
  - 'eat{type=CARROT;amount="50"}'
```

## Every experience source {#every-experience-source}

### From {#from}

Loads all the experience source in `exp-sources.yml` matching to `exp-source-id`.

```yml
from{source=exp-source-id}
```

### Mine Block {#mine-block}

Get exp from mining specific blocks. More information in the [Mining](https://docs.phoenixdevt.fr/mmocore/features/mining) wiki page.

```yml
mineblock{type=BLOCK_MATERIAL}
```

### Kill Mob {#kill-mob}

Killing a mob grants exp. This will work on any vanilla mob.

```yml
killmob{type=MOB_ENTITY_TYPE;amount=1-3}
```

### Kill Mythic Mob {#kill-mythic-mob}

Killing a MythicMob grants exp. You need to provide the ID of the mob using the `type` parameter.

```yml
killmythicmob{type=MobInternalName;amount=1-3}
```

### Fish Item {#fish-item}

Fishing an item of the specified type grants exp.

```yml
fishitem{type=ITEM_MATERIAL;amount=1-3}
```

### Smelt Item {#smelt-item}

When an item is smelted (furnaces).

```yml
smeltitem{type=ITEM_MATERIAL;amount=1-3}
```

### Craft Item {#craft-item}

When an item is crafted.

```yml
craftitem{type=ITEM_MATERIAL;amount=1-3}
```

### Brew potion {#brew-potion}

[More info on Alchemy](https://docs.phoenixdevt.fr/mmocore/profession/alchemy). You can specify multiple potion effects here, separated by a comma.

```yml
brewpotion{effect="SPEED,REGEN,...";amount=1-3}
```

### Place Block {#place-block}

Placing a block of the specified type grants xp.

```yml
placeblock{type=BLOCK_MATERIAL;amount=1-3}
```

### Repair Item {#repair-item}

You can define in `smithing.yml` the amount of xp for each material. More information in the [Smithing](https://docs.phoenixdevt.fr/mmocore/profession/smithing) wiki page.

```yml
repairitem{type=ITEM_MATERIAL}
```

### Enchant Item {#enchant-item}

Get exp when enchanting items. [More info on Enchanting](https://docs.phoenixdevt.fr/mmocore/profession/enchanting).

```yml
enchantitem{type=...}
```

### Climb {#climb}

When you climb one block. The type can be `ladder`, `vines`, `weeping-vines`, `twisting-vines`. If you don't specify any type it will trigger for all types.

```yml
climb{type=BLOCK_TYPE;amount=1-3}
```

### Eat {#eat}

Give experience when some specific food is eaten. If you don't specify a material for the type it will give exp disregarding what you eat.

```yml
eat{type=ITEM_MATERIAL;amount=1-3}
```

### Move {#move}

Give experience for each block travelled, the type can be `sneak`, `fly`, `swim`, `sprint` or `walk`. If it is not specified will trigger all the time.

```yml
move{type=MOVING_TYPE;amount=1-3}
```

### Resource {#resource}

Gives exp for each resource of type "RESOURCE_TYPE" consumed. Resource type can be `health`, `mana`, `stamina` or `stellium`.

```yml
resource{type=RESOURCE_TYPE;amount=1-3}
```

### Ride {#ride}

When you move riding a certain entity. Check the [EntityType](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html) enum to specify the type.

```yml
ride{type=ENTITY_TYPE}
```

### Tame {#tame}

Exp given when taming mobs (like a wolf). Triggers once per click. `type` is optional, if not provided it applies to all mob types.

```yml
tame{amount=1-3}
```

### Tamed Entity Damage {#tamed-entity-damage}

Exp given when a tamed mob of yours deals damage. Amount of exp provided is multiplied by the final damage output. `type` is optional, if not provided it applies to all mob types.

```yml
tame{type=WOLF;amount=1-3}
```

### Damage Taken {#damage-taken}

Exp given for each damage a player takes damage from a certain cause. Type can be `DROWNING`, `FALL`, `FIRE`, etc.... You can find the list of possible damage causes [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html).

```yml
damagetaken{type=DAMAGE_CAUSE}
# or all damage causes
damagetaken{amount=1}
```

### Damage Dealt {#damage-dealt}

Exp given per damage dealt of a certain MMO damage type. The damage type can be `magic`, `physical`, `weapon`, `skill`, `projectile`, `unarmed`, `on-hit`, `minion` or `dot`.

```yml
damagedealt{type=DAMAGE_TYPE}
# or all damage types
damagedealt{amount=1}
```
