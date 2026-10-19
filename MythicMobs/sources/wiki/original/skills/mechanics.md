Skill Mechanics (or base skills) are simple skills that are built into
MythicMobs. You can call these basic skills by themselves in your mob's
Skill List, or you can create your own meta-skill by combining these
mechanics together.

Some Mechanics are able to target Entities, Locations, or both! Some
don't target anything. You control what your skill targets using a
[Targeter](https://wiki.mythiccraft.io/mythicmobs/skills/targeters).

You can also find some of the mechanics listed by tag [here](https://wiki.mythiccraft.io/mythicmobs/Skills/Tags/Mechanic-Tags)

1. [Additional Mechanics](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics#additional-mechanics)
2. [Mechanics](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics#mechanics)
   1. [Meta Mechanics](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics#meta-mechanics)
3. [Universal Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics#universal-attributes)
4. [Examples](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics#examples)

# Additional Mechanics {#additional-mechanics}

Links to mechanics added by addon plugins. Any mechanics from these links will not work without that plugin installed.

- [ModelEngine 4](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics)
- [Mythic Crucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Mechanics)
- [Mythic Enchantments](https://wiki.mythiccraft.io/mythicenchants/Mechanics/Mechanics)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#mechanics)

# Mechanics {#mechanics}

These skills usually target entities (players or other mobs), but some
are able to target locations as well.

| Mechanic | Description |
| --- | --- |
| [ActivateSpawner](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/activatespawner) | Activates a MythicMobs spawner at the targeted location |
| [AddTrade](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/AddTrade) | Changes the trades of a villager |
| [AnimateArmorStand](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/animatearmorstand) | Animates an armorstand |
| [ArmAnimation](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ArmAnimation) | Makes the caster swing their arm |
| [ArrowVolley](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/arrowvolley) | Fires a volley of arrows |
| [Attribute](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Attribute) | Sets an attribute on the target entity, if attributable |
| [AttributeModifier](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/AttributeModifier) | Adds an attribute modifier to the attributable target |
| [AuraRemove](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/auraremove) | Removes an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) from the target entity |
| [BarCreate](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/barcreate) | Creates a custom boss bar on the casting mob |
| [BarRemove](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/barremove) | Removes a custom boss bar on the casting mob |
| [BarSet](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/barset) | Modifies a custom boss bar on the casting mob |
| [BlackScreen](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Blackscreen) | Blacks out the target's screen for the duration |
| [BlockDestabilize](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/blockdestabilize) | Causes the targeted blocks to fall, as if affected by gravity |
| [BlockMask](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/BlockMask) | Temporarily masks a block as a different block |
| [BlockUnmask](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/BlockUnmask) | Unmasks blocks that have been masked |
| [BlockPhysics](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/blockphysics) | Triggers a block physics update at the target location |
| [BlockWave](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/BlockWave) | Creates a wave of blocks at the target location |
| [BloodyScreen](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/BloodyScreen) | Makes the target's screen glow red |
| [BoneMeal](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/bonemeal) | Applies a bone meal effect to the target blocks |
| [BossBorder](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/bossborder) | Creates an inescapable border around the mob |
| [Bouncy](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Bouncy) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that makes it bouncy |
| [BreakBlock](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/breakblock) | Breaks the block at the target location |
| [BreakBlockAndGiveItem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/breakBlockAndGiveItem) | Breaks the block at the target location and gives an item/droptable |
| [ClearExperience](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ClearExperience) | Clears the experience for the targeted players |
| [ClearExperienceLevels](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ClearExperienceLevels) | Clears the experience levels for the targeted players |
| [ClearTarget](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ClearTarget) | Forces the target of the mechanic to reset its current target |
| [GiveExperienceLevels](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/GiveExperienceLevels) | Gives experience levels to the targeted players |
| [TakeExperienceLevels](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/TakeExperienceLevels) | Takes experience levels to the targeted players |
| [CloseInventory](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/closeinventory) | Closes the target player's inventory |
| [Command](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/command) | Executes a command for each target |
| [Consume](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/consume) | Deals damage and restores health per target hit |
| [ConsumeSlot](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/consumeslot) | Remove an item from a specific slot of the player's inventory |
| [DirectionalVelocity](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/DirectionalVelocity) | Changes the velocity on the target entity on a specific vector |
| [Disengage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/disengage) | Causes the caster to leap backwards away from the target entity |
| [Disguise](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/disguise) | Changes the caster's disguise |
| [DisguiseModify](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/DisguiseModify) | Modifies the caster's already applied disguise |
| [DisguiseTarget](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/disguisetarget) | Changes the target's disguise |
| [Undisguise](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/undisguise) | Remove the caster's disguise |
| [Dismount](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/dismount) | Makes the caster dismount whatever they're riding |
| [DisplayTransformation](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/DisplayTransformation) | Sets the targeted display entity's transformations |
| [ClearThreat](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/clearthreat) | Makes a mob clear its threat table |
| [CurrencyGive](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/currencygive) | Give money to a player. Requires Vault and a currency plugin |
| [CurrencyTake](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/currencytake) | Take money from a player. Requires Vault and a currency plugin |
| [Damage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/damage) | Damages the target for an amount |
| [BaseDamage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/basedamage) | Damages the target for a percent of the mob's damage stat |
| [PercentDamage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/percentdamage) | Damages the target for a percent of their health |
| [Decapitate](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/decapitate) | Drops a player head item based on target |
| [Doppleganger](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/doppleganger) | Copies the appearance of the target player |
| [DropItem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/dropitem) | Drops an item or droptable at the target location |
| [EjectPassenger](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ejectpassenger) | Ejects anything riding the caster |
| [Ender](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Ender) | Causes the "Ender" effect |
| [EnderBeam](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/EnderBeam) | Creates a EnderCrystal's beam effect to the target |
| [EnderDragonResetCrystals](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/EnderDragonResetCrystals) | Generates the EnderDragon crystals |
| [EnderDragonSetPhase](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/EnderDragonSetPhase) | Sets the EnderDragon phase |
| [EnderDragonSetRespawnPhase](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/EnderDragonSetRespawnPhase) | Sets the EnderDragon respawn phase |
| [EnderDragonSpawnPortal](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/EnderDragonSpawnPortal) | Generates the portal of the EnderDragon battle |
| [Equip](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/equip) | Causes the casting mob to equip an item |
| [EquipCopy](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/equipcopy) | Causes the caster to equip a copy of the target's equipment |
| [Explosion](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/explosion) | Causes an explosion |
| [FakeExplosion](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/FakeExplosion) | Causes a fake explosion |
| [Extinguish](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/extinguish) | Removes fire ticks from the target entity |
| [FawePaste](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/fawepaste) | Pastes a Schematic using FAWE (Fast Async World Edit) |
| [Feed](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/feed) | Feeds the target player |
| [Fear](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Fear) | Applies an aura that makes the target run around in fear |
| [FillChest](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/fillChest) | Fills a chest with items, or a droptable |
| [Firework](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/firework) | Creates a firework effect at the target |
| [Flames](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/flames) | Creates the flames effect at the location of the targeter |
| [Fly](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/fly) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) that allows the targeted player to fly |
| [ForcePull](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/forcepull) | Teleports the target to the caster |
| [Freeze](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/freeze) | Freezes the target for the given number of ticks using the Powdered Snow freezing effect |
| [Geyser](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/geyser) | Creates a "geyser" of water or lava |
| [GiveItem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/giveitem) | Gives an item to the target |
| [GiveItemFromSlot](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/giveitemfromslot) | Gives an item to the target from the item in the given slot of caster |
| [GiveItemFromTarget](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/giveitemfromtarget) | Gives the caster an item while playing the pickup-item animation from the target entity or location |
| [Glow](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/glow) | Makes the target glow |
| [GoatRam](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/GoatRam) | Causes the casting goat mob to ram the targeted entity |
| [GoTo](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/goto) | Move toward the location of the targeter (entity or location) |
| [GuardianBeam](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/guardianbeam) | Draws a guardian beam between the origin and the target |
| [Heal](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/heal) | Heals the target |
| [HealPercent](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/healpercent) | Heals the target for a percentage of its max-health |
| [Hide](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/hide) | Hides the caster from the targeted player(s) for a set duration. |
| [Hit](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/hit) | Simulates a physical hit from the mob. |
| [Hologram](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/hologram) | Summons a hologram to the targeted location |
| [Ignite](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ignite) | Sets the target on fire |
| [ItemSpray](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/itemspray) | Causes an explosion of temporary items at the target location |
| [JSONMessage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/jsonmessage) | Sends a JSON-format message to the target player(s) |
| [Jump](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/jump) | Causes the caster to jump |
| [Leap](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/leap) | Causes the caster to leap towards the target |
| [Lightning](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/lightning) | Strikes lightning at the target |
| [FakeLightning](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/FakeLightning) | Strikes a fake lightning at the target |
| [Log](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Log) | Logs a message to console. |
| [Look](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/look) | Causes the caster to look at the target |
| [Lunge](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/lunge) | Causes the caster to lunge forward at the target |
| [MatchRotation](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/MatchRotation) | Sets the caster's yaw and pitch to the same value of the target's |
| [Message](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/message) | Sends a message to the target player(s) |
| [ModifyDamage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ModifyDamage) | Modifies the damage event that triggered the skill |
| [ModifyGlobalScore](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/modifyglobalscore) | Modifies a scoreboard value of the fake player: __GLOBAL__ |
| [ModifyTargetScore](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/modifytargetscore) | Modifies a scoreboard value of the target |
| [ModifyMobScore](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/modifymobscore) | Modifies a scoreboard value of the casting mob |
| [ModifyScore](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/modifyscore) | Modifies the score of a dummy player |
| [Mount](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/mount) | Summons a mob for the caster and mounts it |
| [MountMe](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/mountme) | Forces the targeted entity to mount the caster |
| [MountTarget](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/mounttarget) | Mounts the target |
| [MovePin](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/MovePin) | Moves the given pin to the target location |
| [OpenCustomMenu](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/OpenCustomMenu) | Opens a [custom menu] |
| [OpenTrades](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/OpenTrades) | Opens the trades of the casting villager to the target player |
| [Oxygen](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/oxygen) | Gives oxygen to a player target |
| [Particle](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Particle) | Creates particle effects around the target |
| [ParticleBox](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleBox) | Draws a box of particles around the target |
| [ParticleEquation](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleEquation) | Generates particles based on equations |
| [ParticleLine](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleLine) | Draws a line of particle effects to the target |
| [ParticleLineHelix](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleLineHelix) | Draws a line based helix effect |
| [ParticleLineRing](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleLineRing) | Draws a particle ring connected by lines |
| [ParticleOrbital](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleOrbital) | Draws orbiting particle effects around the target |
| [ParticleRing](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleRing) | Draws a ring of particles around the target |
| [ParticleSphere](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleSphere) | Draws a sphere of particles around the target |
| [ParticleTornado](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleTornado) | Draws a persistent "tornado" of particles at the target |
| [Atom](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Atom) | Creates some particles in the shape of an atom |
| [PickUpItem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/pickupitem) | Pick up the targeted item |
| [PlayAnimation](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PlayAnimation) | Forces the entity to play an animation |
| [PlayBlockBreakSound](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PlayBlockBreakSound) | Plays a block breaking sound |
| [PlayBlockFallSound](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PlayBlockFallSound) | Plays a block falling sound |
| [PlayBlockHitSound](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PlayBlockHitSound) | Plays a block hit sound |
| [PlayBlockPlaceSound](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PlayBlockPlaceSound) | Plays a block place sound |
| [PlayBlockStepSound](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PlayBlockStepSound) | Plays a block step sound |
| [PoseArmorStand](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/posearmorstand) | Changes the pose of the target ArmorStand |
| [Potion](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/potion) | Applies a potion effect to the target |
| [PotionClear](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/potionclear) | Removes all potion effects from target entity |
| [Prison](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/prison) | Imprisons the target inside a block |
| [PrintParentTree](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PrintParentTree) | Prints debug information regarding the Metaskill executing the mechanic and its SkillTree |
| [Propel](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/propel) | Propels the caster towards the target |
| [Pull](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/pull) | Pulls the target towards the mob |
| [PushBlock](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PushBlock) | Pushes the block at the target location in the given direction |
| [PushButton](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/pushbutton) | Pushes a button at the target location |
| [RayTrace](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/raytrace) | Traces a straight line to the target |
| [RayTraceTo](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/raytraceto) | Executes a skill with the result of a raytrace to the target location |
| [Rally](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/rally) | Causes other nearby mobs to attack the target |
| [RandomMessage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/randommessage) | Sends a random message to the target player |
| [Recoil](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Recoil) | Kicks the target's screen in order to simulate a recoil |
| [Remount](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/remount) | Remounts the mob the caster originally spawned riding, if it is still alive |
| [Remove](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/remove) | Removes the target mob |
| [RemoveHeldItem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/removehelditem) | Removes some of the item the target player is holding |
| [RemoveOwner](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/removeowner) | Removes the ownership of the target mob |
| [ResetAI](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ResetAI) | Attempts to resets the AI of a casting mob to the base type's default |
| [RotateTowards](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/RotateTowards) | Rotates the caster towards the target location |
| [RunAIGoalSelector](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/runaigoalselector) | Change the caster's [AIGoalSelectors](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ai-goal-selectors) |
| [RunAITargetSelector](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/runaitargetselector) | Change the caster's [AITargetSelectors](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ai-target-selectors) |
| [Saddle](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/saddle) | Equips or remove a saddle on the target entity |
| [SendActionMessage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/sendactionmessage) | Sends an Actionbar Message to the target player |
| [SendResourcePack](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/sendresourcepack) | Sends a Resource Pack to the target player |
| [SendTitle](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SendTitle) | Sends a Title/Subtitle Message to the target player |
| [SendToast](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/sendtoast) | Sends an achievement toast to the target player |
| [SetAI](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setai) | Disables/enables the AI of the target mob |
| [SetBlockOpen](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetBlockOpen) | Sets the target block's open state |
| [SetBlockType](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setblocktype) | Change block type at target location |
| [SetChunkForceLoaded](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetChunkForceLoaded) | Sets the force-loaded status of a location's chunk |
| [SetCollidable](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setcollidable) | Sets if the target should have a collidable hitbox or not |
| [SetCustomMenuButton](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SetCustomMenuButton) | Sets a specific slot of the opened [custom menu] to the specified button |
| [SetDragonPodium](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetDragonPodium) | Sets the position of the dragon's podium at the target location |
| [SetGameMode](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setgamemode) | Sets the Game Mode of the target player |
| [SetGliding](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setgliding) | Makes the target glide if they have elytra |
| [SetGlobalScore](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setglobalscore) | Sets a scoreboard value on the fake player: __GLOBAL__ |
| [SetGravity](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setgravity) | Sets whether gravity affects the target entity |
| [SetHealth](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/sethealth) | Sets the health of the target entity |
| [SetInteractionSize](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetInteractionSize) | Sets the size of the target `INTERACTION` entity. |
| [SetItemGroupCooldown](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetItemGroupCooldown) | Sets the cooldown on an item group for the target player |
| [setDisplayEntityItem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setDisplayEntityItem) | Sets the item component of `ITEM_DISPLAY` entities. |
| [SetLeashHolder](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setleashholder) | Changes the holder of a mobs lead |
| [SetLevel](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setlevel) | Changes the casting mob's level |
| [SetMaterialCooldown](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setmaterialcooldown) | Sets a cooldown for usable materials like ender pearls, chorus fruit, etc |
| [SetMaxHealth](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setmaxhealth) | Sets the max health of the target entity |
| [SetMobColor](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setmobcolor) | Changes the color of the target if it is a colorable mob |
| [SetMobScore](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setmobscore) | Sets a scoreboard value on the casting mob |
| [SetName](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setname) | Changes the caster entity's name |
| [setRaiderCanJoinRaid](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/setRaiderCanJoinRaid) | Sets if the target raider entity can join a raid or not |
| [SetRaiderPatrolBlock](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setraiderpatrolblock) | Sets the target raider to patrol a location |
| [SetRaiderPatrolLeader](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setraiderpatrolleader) | Sets the raider patrol leader |
| [SetFaction](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setFaction) | Changes the target entity's faction |
| [SetFlying](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetFlying) | Sets whether the target player is flying |
| [SetNoDamageTicks](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setnodamageticks) | Sets the nodamageticks of the target |
| [SetOwner](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setowner) | Makes the target the owner of the casting mob |
| [SetParent](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetParent) | Makes the target the parent of the casting mob |
| [SetPathfindingMalus](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetPathfindingMalus) | Sets the pathfinding malus of a mob for given terrain types |
| [SetPitch](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetPitch) | Sets the head pitch of the target entity |
| [SetPose](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetPose) | Sets the entity's pose |
| [SetRotation](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setrotation) | Sets the rotation of the target |
| [SetTarget](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/settarget) | Sets the caster's target |
| [SetTargetScore](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/settargetscore) | Sets the score of the target |
| [SetTextDisplay](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetTextDisplay) | Sets the text component of target Text Display entity |
| [SetTongueTarget](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/settonguetarget) | Sets the tongue target for a frog caster to the target entity |
| [SetScore](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setscore) | Sets the scoreboard value of a dummy player |
| [SetSpeed](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setspeed) | Sets the target entity's speed attribute |
| [SetStance](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setstance) | Sets the stance of the target mob |
| [Shield](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shield) | Applies an absorb shield to the target entity |
| [ShieldBreak](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shieldbreak) | Forces the player to lower their shield and puts it on cooldown |
| [ShieldPercent](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shieldpercent) | Applies an absorb shield to the target entity for a percentage of their max health |
| [ShootFireball](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shootfireball) | Shoots a fireball at the target |
| [ShootPotion](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shootpotion) | Throws a potion at the target |
| [ShootSkull](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shootskull) | Shoots a wither skull at the target |
| [ShootShulkerBullet](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shootshulkerbullet) | Shoots a shulker bullet at the target entity |
| [ShowEntity](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/showentity) | Shows the hidden caster to the targeted players |
| [Signal](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/signal) | Sends a signal to a mob |
| [Skybox](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Skybox) | Alters the target player's skybox |
| [Smoke](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Smoke) | Creates a puff of smoke |
| [SmokeSwirl](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SmokeSwirl) | Creates a persistent "swirl" of smoke |
| [Sound](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Sound) | Plays a sound effect from both vanilla Minecraft and resource packs |
| [StealItem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/StealItem) | Steals an item from the target and puts it in the mob's hand |
| [StopSound](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/StopSound) | Stops a sound effect from playing |
| [Speak](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/speak) | Causes the mob to speak in chat, with options for speech bubbles |
| [Spin](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Spin) | Causes the target to spin |
| [Spring](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/spring) | Creates a temporary spring of liquid at the target |
| [Stun](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/stun) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) that stuns the target entity |
| [StopUsingItem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/stopusingitem) | Stops the targeted entity from using an item |
| [Suicide](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/suicide) | Causes the caster to die |
| [Summon](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/summon) | Summons other mobs at the target |
| [SummonAreaEffectCloud](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/summonareaeffectcloud) | Summons a cloud of particles at the target |
| [SummonFallingBlock](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SummonFallingBlock) | Summons a falling block |
| [SummonPassenger](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/summonpassenger) | Summons a mob to ride the target. |
| [Swap](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/swap) | Swaps locations with the target |
| [SwingOffhand](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SwingOffhand) | Makes the casting player swing their offhand |
| [AddTag](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/addtag) | Adds a scoreboard tag to the target |
| [RemoveTag](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/removetag) | Removes a scoreboard tag from the target |
| [TakeItem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/takeitem) | Removes an item from the targeted player's inventory |
| [Taunt](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Taunt) | Modifies the threat level that the caster holds with the target entities |
| [Teleport](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/teleport) | Teleports to the target |
| [TeleportY](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/teleporty) | Teleports the caster vertically |
| [TeleportIn](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/teleportin) | Teleports the target relative to the caster's yaw |
| [TeleportTo](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/teleportto) | Teleports the target to a specified location |
| [Time](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/time) | Changes the time |
| [Threat](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/threat) | Modifies the mob's threat towards the target |
| [Throw](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/throw) | Throws the target entity |
| [ThunderLevel](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ThunderLevel) | Creates a client-side, per-player rainless storm |
| [ToggleLever](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/togglelever) | Toggles a lever at the target location |
| [TogglePiston](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/TogglePiston) | Toggles a piston at the target location |
| [ToggleSitting](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/togglesitting) | Toggles the sitting state for cats, dogs, foxes, and parrots. |
| [TotemOfUndying](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/TotemOfUndying) | Plays the effect of a player resurrecting |
| [TrackLocation](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/tracklocation) | Sets the mob's tracked location to the targeted location |
| [UndoPaste](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/undopaste) | Undoes a previously made paste |
| [Velocity](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/velocity) | Modifies the velocity of the target entity(s) |
| [Weather](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/weather) | Modifies the weather in the target world |
| [WolfSit](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/wolfsit) | Forces a targeted wolf to sit. |
| [WorldEditReplace](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/WorldEditReplace) | Replaces blocks in a region using WorldEdit |

## Meta Mechanics {#meta-mechanics}

These skill mechanics have special advanced functions, and most are used
to call other skills. If you specify a target, all other skills called
by these will "inherit" the targets (if applicable).

| Mechanic | Description |
| --- | --- |
| **[Skill](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/skill)** | Executes a meta-skill. The butter for your bread. |
| **[VariableSkill](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/variableskill)** | Executes a meta-skill. Supports placeholders. |
| [Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) | Applies an aura to the targeted entity, allowing for skills to be run onStart/onTick/onEnd/Etc which all originate from the target. |
| [Beam](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Beam) | Creates a beam of a material between the caster and the target |
| [CancelEvent](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/cancelevent) | Cancels the Event that triggered the current skill-tree. Only works for certain triggers. |
| [CancelSkill](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/CancelSkill) | Cancels the execution of the Metaskill when triggered. |
| [Cast](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/cast) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) that "Casts" a meta-skill using various advanced options. |
| [Chain](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/chain) | Chains a skill between multiple targets that are near each other. |
| [ChainMissile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/chainmissile) | A missile that chains between entities. **Premium-Only** mechanic! |
| [Delay](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/delay) | Delays execution of the current skill list by a set number of ticks. |
| [DetermineCondition](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/DetermineCondition) | Determines the outcome of a Metaskill that is used as a Condition via the [MetaskillCondition](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/MetaskillCondition) condition |
| [EndProjectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/endprojectile) | Terminates the projectile. Only usable in projectile mechanics. |
| [ForEach](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ForEach) | Executes a metaskill once for each target of the mechanic |
| [ForEachValue](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ForEachValue) | Executes a metaskill once for each entry or key-value pair in the specified value |
| [ForEachPin](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ForEachPin) | Executes a metaskill once for each pin of a multi-pin |
| [GlobalCooldown](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/globalcooldown) | Sets the caster's Global Cooldown timer |
| [Missile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/missile) | Fires a homing projectile towards the target. |
| [ModifyProjectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/modifyprojectile) | Modifying the projectile / missile / orbital |
| [OnAttack](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/onattack) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that triggers skills when they attack |
| [OnDamaged](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ondamaged) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that triggers skills when they take damage |
| [OnShoot](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/onshoot) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that triggers skills when they shoot a bow |
| [OnBlockBreak](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/onblockbreak) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that triggers skills when they break a block |
| [OnBlockPlace](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/onblockplace) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that triggers skills when they place a block |
| [OnChat](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/OnChat) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that triggers skills when they chat |
| [OnSwing](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/onswing) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that triggers skills when they swing / left click |
| [OnInteract](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/oninteract) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that triggers skills when they interact / right click while holding a block or looking at an outlined block (NOT AIR) |
| [OnJump](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/onjump) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that triggers a skill when they jump (PAPER ONLY MECHANIC) |
| [OnDeath](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ondeath) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) to the target that triggers a skill when they die |
| [Orbital](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/orbital) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) that causes a projectile to orbit around the target |
| [FollowPath](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/FollowPath) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) that causes the mob to follow a path |
| [FormLine](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/FormLine) | Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) that causes the mob to follow a *straight* path |
| [Polygon](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/polygon) | Creates a highly-customizable polygon-shaped pattern that can execute metaskills. |
| [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) | Fires a highly-customizable projectile towards the target |
| [ProjectileVelocity](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectilevelocity) | Modifies the velocity of the calling Projectile or Missile |
| [RandomSkill](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/randomskill) | Executes a random skill from a list |
| [SetSkillCooldown](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setskillcooldown) | Sets the given metakill's cooldown to the given value |
| [SetProjectileDirection](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetProjectileDirection) | Sets the calling projectile's movement direction to the given target |
| [SetProjectileBulletModel](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setprojectilebulletmodel) | Sets the model of the projectile. (DISPLAY bullets only) |
| [Shoot](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shoot) | Shoots a item-projectile at the target, similar to arrows/eggs/snowballs. |
| [Slash](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/slash) | Creates a highly-customizable slash pattern that can execute metaskills. |
| [SudoSkill](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/sudoskill) | Makes the target execute a skill |
| [Switch](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Switch) | Acts as a switch/case |
| [StatAura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/StatAura) | Applies an aura to the target that applies a specific stat to them |
| [Totem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/totem) | Creates a static "totem" at a location that can execute other skills |
| [Terminable](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/terminable) | Creates an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) that cancels the execution of its onStart metaskill is some conditions are met |
| [Volley](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/volley) | Shoots a volley of projectile-items at the target with various options |
| [VariableAdd](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/variableadd) | Adds an amount to a numeric variable |
| [VariableMath](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/variablemath) | Performs math on a numeric variable |
| [SetVariable](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setvariable) | Sets the value of a variable |
| [SetVariableLocation](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setvariablelocation) | Sets a variable to the target location |
| [VariableUnset](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/variableunset) | Unsets the variable |
| [VariableSubtract](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/variablesubtract) | Subtracts an amount from a numeric variable |
| [VariableMove](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/VariableMove) | Moves an already created variable across names and/or registries |
| [Wait](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Wait) | Puts the metaskill on hold until a set of conditions is met |
| [CinematicCamera](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/CinematicCamera) | Plays a cinematic camera path for the target player |
| [CinematicCancel](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/CinematicCancel) | Cancels an active cinematic for the target player |
| [CloseDialog](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/CloseDialog) | Closes any open dialog for the target player |
| [OnKeyPress](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/OnKeyPress) | Applies an aura that triggers a skill when the player presses a key |
| [OnKeyRelease](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/OnKeyRelease) | Applies an aura that triggers a skill when the player releases a key |

# Universal Attributes {#universal-attributes}

The following attributes are applicable to all mechanics.

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| cooldown | cd | In seconds. Allows for decimal values. | 0 |
| delay |  | Delays the execution of the mechanic by a set number of ticks. | 0 |
| repeat |  | How many times the mechanic should be repeated. If repeatInterval is set to `0`, this becomes the number of executions rather than repetitions | 0 |
| repeatInterval | repeatI | How many ticks must elapse between repetitions | 0 |
| targetInterval | targetI | How many ticks must elapse between target selection | 0 |
| origin |  | *[PREMIUM]** Change the origin to whatever targeter is supplied. Does not work if more than one target is parsed. `origin=@Forward{f=10}` The targeter of the origin attribute will be parsed separately from the mechanic's targeter, so if you use something like `origin=@targetedlocation` it will not return the mechanic's explicit target, but the metaskill's inherited one |  |
| power |  | [Power](https://wiki.mythiccraft.io/mythicmobs/mobs/Power) multiplier | 1 |
| fromorigin | fo, sourceisorigin, castfromorigin | Whether to cast the mechanic from origin. This only works with a select few mechanics, and is usually listed as one of their attributes, too | false |
| targetisorigin |  | Whether to set the target of the mechanic to be the origin | false |
| targetcreative |  | Whether to target creative players | false |
| splitPower | powersplit, powersplitbetweentargets | Whether to split the power between targets | false |
| faulty |  | Whether the mechanic should use the old vector formula | true |
| chance |  | The chance of the mechanic executing. For instance, 0.1 is a 10% chance | 1 |
| forcesync | sync | Whether to force the mechanic to be run synchroniously with the main Minecraft thread. This *generally* worsens performances (albeit usually in a non-perceptible fashion), but **some mechanics needs this to be set to true** *(for instance, the [cancelevent](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/cancelevent) mechanic, since an event cannot be cancelled if the mechanics comes in "late" and the event has already happened)* | false |

# Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - message{m="This message will only be shown once every 5 seconds!";cooldown=5} @trigger ~onInteract
  - message{m="This one 5 times in a row over 2 seconds!";repeat=4;repeatInterval=10} @trigger ~onInteract
```
