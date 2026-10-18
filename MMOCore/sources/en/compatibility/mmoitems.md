# 🏹 MMOItems {#🏹-mmoitems}

MMOCore is built to be used with MMOItems ([Polymart](https://polymart.org/product/3413/mmoitems) / [Spigot](https://www.spigotmc.org/resources/mmoitems-premium.39267)) although it is not a dependency. MMOCore features a lot of compatibility options for MMOItems, here is the detailed list.

### Extra MMOItems Stats {#extra-mmoitems-stats}

When using both MMOCore and MMOItems, extra item stats will automatically enable and will be added to the MMOItems item edition GUI.

| Stat | Description |
| --- | --- |
| Max Mana | Default stat, but it does support MMOCore |
| Max Stamina | Gives extra MMOCore stamina. |
| Max Stellium | Gives extra MMOCore stellium. |
| Resource* Regeneration | Increases flat resource* regen. |
| Max Resource* Regeneration | Regens a % of max resource* every second. |
| Additional Experience | Increases exp earned. |
| Skill Cooldown Reduction | Default stat, but it does support MMOCore |

*Resource stands for either health, mana, stamina or stellium.

### Quest Objectives & Triggers {#quest-objectives-triggers}

MMOItems adds new quest [objectives](https://docs.phoenixdevt.fr/mmocore/features/quests) to MMOCore quests, where players have to get an item and give it to a specific Citizen NPC. You can also setup quest [triggers](https://docs.phoenixdevt.fr/mmocore/features/quests) which give an MMOItem when a specific quest objective is completed.

### MMOCore Drop Tables {#mmocore-drop-tables}

You may add items from MI to MMOCore [drop tables](https://docs.phoenixdevt.fr/mmocore/features/drop-tables).

### Item Restrictions, Mana {#item-restrictions-mana}

MMOItems features item restrictions, including level and class restrictions which **do work** with MMOCore. MMOItems ability and wand weapons may also use mana or stamina/stellium which is also supported by MMOCore.

### Extra features for MMOItems Crafting {#extra-features-for-mmoitems-crafting}

In MMOItems, some recipes have specific conditions which must be met for the player to be able to use the crafting recipe. MMOCore adds profession level crafting restrictions i.e players must be at least Lvl X in some profession like smithing or mining, in order to use the recipes. More info on MMOItems recipe conditions [in the MMOItems wiki](https://docs.phoenixdevt.fr/mmoitems/stations/conditions).

**Recipe example**, where the player must be at least Lvl 5 in *Smithing*.

```
    steel-sword:
        output:
            type: SWORD
            id: STEEL_SWORD
        conditions:
        - 'profession{profession=smithing,level=5}'
        ingredients:
        - 'vanilla{type=STICK,amount=2}'
        - 'mmoitem{type=MATERIAL,id=STEEL_INGOT,amount=4}'
```

MMOCore also adds a new type of crafting trigger (actions made when a recipe is used), which can be used to give experience to a player (either main experience, or experience in a specific profession). More information on MMOItems recipe triggers [in the MMOItems wiki](https://docs.phoenixdevt.fr/mmoitems/stations/triggers).

**Same example**, which grants 10 Smithing EXP when used

```
    steel-sword:
        output:
            type: SWORD
            id: STEEL_SWORD
        ...
        triggers:
        - 'exp{profession=smithing,amount=10}'
```
