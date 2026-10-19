# Unstable Entity Types

While a great deal of entity types can be used in MythicMobs, each one of them can have its quirks, and it is needed for every configurator to be aware of those quirks in order to minimize the damage they might cause or, in general, to better use the entity.

The following is a list of every quirk that has been currently discovered. The more mainstream and obvious problems will not be covered at this time, and only the niche ones will be treated. If you discover any other, let us know on our [Discord](https://discord.com/invite/K3tqXfT)

1. [Mobs by Group](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#mobs-by-group)
   1. [All Zombies](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#all-zombies)
   2. [All passive animals](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#all-passive-animals)
   3. [All breedable animals](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#all-breedable-animals)
   4. [Most bosses](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#most-bosses)
   5. [Entities damaged by water](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#entities-damaged-by-water)
2. [Specific Mobs](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#specific-mobs)
   1. [ARMOR_STAND](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#armor-stand)
   2. [AXOLOTL](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#axolotl)
   3. [BEE](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#bee)
   4. [BLAZE](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#blaze)
   5. [CAT](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#cat)
   6. [CHICKEN](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#chicken)
   7. [COW](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#cow)
   8. [DROWNED](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#drowned)
   9. [ENDER_DRAGON](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#ender-dragon)
   10. [ENDERMAN](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#enderman)
   11. [ENDERMITE](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#endermite)
   12. [FOX](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#fox)
   13. [GHAST](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#ghast)
   14. [GIANT](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#giant)
   15. [IRON_GOLEM](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#iron-golem)
   16. [MAGMA_CUBE](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#magma-cube)
   17. [PARROT](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#parrot)
   18. [PHANTOM](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#phantom)
   19. [PIGLIN](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#piglin)
   20. [PILLAGER](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#pillager)
   21. [PUFFERFISH](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#pufferfish)
   22. [RABBIT](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#rabbit)
   23. [SKELETON](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#skeleton)
   24. [SLIME](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#slime)
   25. [SQUID](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#squid)
   26. [VEX](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#vex)
   27. [WARDEN](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#warden)
   28. [WITHER](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#wither)
   29. [WOLF](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types#wolf)

## Mobs by Group {#mobs-by-group}

### All Zombies {#all-zombies}

Can spawn as leaders, having several times the amount of configured health.

### All passive animals {#all-passive-animals}

Could get aggroed by other entities.

### All breedable animals {#all-breedable-animals}

They can usually be fed by some item and, subsequently, try to breed.  
This can be handled by intercepting the event [~onBreed](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onBreed) (and then either cancelling it or some other mechanic) or completely prevented by using the [Age](https://wiki.mythiccraft.io/mythicmobs/Mobs/Options#age) option

### Most bosses {#most-bosses}

Have an hardcoded ai or some other hardcoded features.

### Entities damaged by water {#entities-damaged-by-water}

Affected entities include Enderman, Snowman and Blaze.  
The damage type in those instances if of the `DROWNING` type, and can thus be fully prevented by using a negative value for it as a [DamageModifier](https://wiki.mythiccraft.io/mythicmobs/Mobs/DamageModifiers) or by using the following skill

```yaml
   - cancelevent{sync=true} ~ondamaged ?damagecause{c=drowning}
```

## Specific Mobs {#specific-mobs}

### ARMOR_STAND {#armor-stand}

Does not get targeted by default by multi entity targeters, and a [specific filter](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#target-filters) must be used.

### AXOLOTL {#axolotl}

Can be Bucketed. Defend against this by using a [onBucket](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onBucket) trigger

### BEE {#bee}

When allowed to randomfly, it will enter placed beehives and pollinate flowers.  
No definitive answer exists, apart from clearing its AI and building a new one.

### BLAZE {#blaze}

Can be damaged by water, snowballs and the like. Use a [Damage Modifier](https://wiki.mythiccraft.io/mythicmobs/Mobs/DamageModifiers) in order to prevent this.

### CAT {#cat}

Scares Creepers and Phantoms away

### CHICKEN {#chicken}

Can lay eggs and is hunted by other animals.  
For the "egg problem", use the [Jockey Option](https://wiki.mythiccraft.io/mythicmobs/Mobs/Options#jockey).

### COW {#cow}

Can be milked.

### DROWNED {#drowned}

By default, it does not attack its target in the day if they are not in a water block. A [custom ai](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI) must be set up in order to remove this behavior

### ENDER_DRAGON {#ender-dragon}

Has a hardcoded ai.

### ENDERMAN {#enderman}

Avoids projectiles and is damaged by water.

### ENDERMITE {#endermite}

Draws aggro from Endermen.

### FOX {#fox}

Has an unique attack pattern, can be useful but also problematic.

### GHAST {#ghast}

Has a hardcoded ai.
Can be one-shotted by a fireball.

### GIANT {#giant}

Has a hardcoded ai.

### IRON_GOLEM {#iron-golem}

Can be healed via the use of iron ingots and draws aggro by default from most hostile mobs.

### MAGMA_CUBE {#magma-cube}

Has a hardcoded ai.

### PARROT {#parrot}

Can be one-shotted by a cookie.

### PHANTOM {#phantom}

Has a hardcoded ai.

### PIGLIN {#piglin}

Has a hardcoded aggro priority

### PILLAGER {#pillager}

If, for any reason, a pillager loses his target while holding a charged crossbow, then it will freeze

### PUFFERFISH {#pufferfish}

Has very unique interactions and behaviors that may cause problems.

### RABBIT {#rabbit}

Draws aggro from other neutral mobs, such as foxes.

### SKELETON {#skeleton}

Draws aggro from wolves

### SLIME {#slime}

Has a hardcoded ai.

### SQUID {#squid}

Do not work with mechanics such as [lunge](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/lunge) and [throw](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/throw).  
This also applies to GLOW_SQUID

### VEX {#vex}

Has a hardcoded ai.

### WARDEN {#warden}

Has a hardcoded aggro system.

### WITHER {#wither}

Has a hardcoded ai.

### WOLF {#wolf}

Can be healed via the use of specific items
Once it becomes "Tamed", the health resets.
