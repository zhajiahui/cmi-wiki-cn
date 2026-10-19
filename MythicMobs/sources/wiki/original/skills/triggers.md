Triggers are used to determine how a skill is triggered from within the
mobs skill configuration section.

**TRIGGERS CANNOT BE USED IN META-SKILLS AND SHOULD NOT BE INCLUDED
IN THEM.**

Triggers can only be used *to activate* the meta-skill
itself (in the mob's configuration file).

> Each trigger starts with a `on` string. That string is **case sensitive**, so make sure to write it correctly or the trigger will not work

## Using Triggers {#using-triggers}

Triggers are defined in the skill section of the mob configuration and
must use a tilde (~) in front of them. In the case of the Timer, a time
in ticks is also required.

```yml
SkeletalWizard_Fire:
  Type: WITHER_SKELETON
  Display: '&Skeletal Fire Wizard'
  Health: 50
  Damage: 0.5
  Skills:
  - ignite{ticks=100} @target ~onAttack
  - skill{s=FireShield} @trigger ~onDamaged 0.1
  - skill{s=AOEFire} ~onTimer:300
```

In this example the mob will also set its target on fire when
melee-attacking, will use a "FireShield" skill when taking damage, and
will use the "AOEFire" skill every 300 ticks, or every 15 seconds.

## Not using Triggers... {#not-using-triggers}

Skill triggers give far more flexibility in determining exactly when a
skill should go off. It is **highly** recommended that you trigger all
your skills using advanced triggers as opposed to the old, legacy
methods.

If a skill does not have a trigger, it will default to the `~onCombat`
trigger which will execute when these events occur:

- When the mob deals or takes damage
- When the mob spawns
- When the mob dies

```yml
SkeletalWarrior:
  Mobtype: skeleton
  Display: '<blue>A Skeletal Warrior</blue>'
  Skills:
  - skill{s=Bash} =10%-90%
```

In this instance the Bash skill is triggered when the mob deals or takes
damage when it is between 10% and 90% health.

# The @trigger Targeter {#the-at-trigger-targeter}

You may have noticed there is an [`@trigger`](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) targeter in the examples
shown above, and listed in the [targeters](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters) section. The `@trigger` will target the
entity that "caused" the skill to trigger, i.e. when a player damages a mob and
that mob has an ~onDamaged skill, it will target that player.
If a signal is being sent to a mob, it will target the mob that sent
the signal, and so on.

# Additional Triggers {#additional-triggers}

Links to triggers added by addon plugins. Any triggers from these links will not work without that plugin installed.

- [Mythic Crucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers)
- [Mythic Enchantments](https://git.mythiccraft.io/mythiccraft/mythicenchants/-/wikis/Triggers/Triggers)

# Triggers {#triggers}

**Table of all available triggers:**

| Trigger | When it fires... |
| --- | --- |
| [onCombat](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCombat) | Default |
| [onAttack](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onattack) | When the mob hits something |
| [onDamaged](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/ondamaged) | When the mob is damaged |
| [onSpawn](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onspawn) | When the mob spawns |
| [onDespawn](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/ondespawn) | When the mob is despawned |
| [onReady](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onready) | Triggered the first time a mob is spawned from a spawner |
| [onLoad](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onload) | When the mob is loaded after a server restart |
| [onSpawnOrLoad](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onspawnorload) | When the mob either [spawns](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onspawn) or [loads](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onload) |
| [onDeath](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/ondeath) | When the mob dies |
| [onTimer](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer) | Every # ticks (where # is the interval in ticks) |
| [onInteract](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/oninteract) | When the mob is right-clicked |
| [onPlayerKill](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onplayerkill) | When the mob kills a player |
| [onEnterCombat](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onentercombat) | When the mob enters combat (requires threat tables be on) |
| [onDropCombat](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/ondropcombat) | When the mob leaves combat (requires threat tables be on) |
| [onChangeTarget](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onchangetarget) | When the mob changes targets (requires threat tables be on) |
| [onExplode](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onexplode) | When the mob explodes (typically only used for creepers) |
| [onPrime](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onprime) | When the creeper charges up for an explosion |
| [onCreeperCharge](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/oncreepercharge) | When the creeper is charged (when lightning hits a creeper) |
| [onTeleport](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onteleport) | When the mob teleports (typically only used for endermen) |
| [onSignal](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onsignal) | When the mob receives a signal |
| [onShoot](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onshoot) | When the mob fires a projectile |
| [onBowHit](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onbowhit) | When the mob's fired projectile hits an entity |
| [onTame](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/ontame) | When the mob gets tamed |
| [onBreed](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onbreed) | When the mob breeds with another mob. |
| [onTrade](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/ontrade) | When the Villager completes a trade. Requires Paper |
| [onChangeWorld](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onchangeworld) | When the mob changes world |
| [onBucket](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onbucket) | When the cow is milked or an entity is bucketed (axolotl etc.) |
| [onSkillDamage](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onskilldamage) | When the mob deals damage to other entities via a mechanic |
| [onHear](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onhear) | When the mob hears a sound, [if enabled](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#hearing) |
| [onProjectileHit](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onProjectileHit) | When a mob's special projectile hits an entity |
| [onProjectileLand](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onProjectileLand) | When a mob's special projectile hits a block |
| [onDismounted](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDismounted) | When the mob is dismounted from |
| [onCinematicStart](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCinematicStart) | When a cinematic camera path begins playing on a player |
| [onCinematicEnd](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCinematicEnd) | When a cinematic camera path ends on a player (finish, cancel, quit, or death) |
| [onEnterBounds](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onEnterBounds) | When the mob moves into a defined region |
| [onExitBounds](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onExitBounds) | When the mob moves out of a defined region |
| [onPlayerEnter](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onPlayerEnter) | When a player moves into a defined region |
| [onPlayerExit](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onPlayerExit) | When a player moves out of a defined region |
