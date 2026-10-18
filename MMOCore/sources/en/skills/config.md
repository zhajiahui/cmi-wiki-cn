# 🗃️ Configuration {#🗃️-configuration}

## Class-Specific Skills {#class-specific-skills}

Skills are class-specific - a given class can only execute a set of predefined skills.

To define what skills each class can use, open up the class config file inside the `MMOCore/classes` folder, and look for the `skills` config section. Each entry under this section corresponds to a single class skill.

```yml
skills:

  # First skill
  FIRE_STORM:
    level: 1
    max-level: 30
    unlocked-by-default: true

    # Skill modifiers
    damage:
      base: 5.0
      per-level: 3.0
    cooldown:
      base: 5.0
      per-level: -0.1
      max: 5.0
      min: 1.0
    #....
  
  # Second skill
  POWER_MARK:
    level: 3
    max-level: 30
    unlocked-by-default: true
    needs-bound: true
    #.....
  
  # Some test passive skill
  A_PASSIVE_SKILL:
    level: 10
    max-level: 30
    trigger: TIMER # Runs on a timer
    timer: 5 # Runs once every 5 seconds
    cooldown:
      base: 5.0
      per-level: -0.1
      max: 5.0
      min: 1.0

  #..........
```

### Skill Level {#skill-level}

`level` indicates the level at which the class naturally unlocks this skill. `max-level` is the maximum level for that class skill. Once reached, the player can no longer [upgrade](https://docs.phoenixdevt.fr/mmocore/skills/intro#upgrading-a-skill) this skill.

### Unlocked by Default {#unlocked-by-default}

`unlocked-by-default` indicates if this skill should be unlocked by default. It is set to `true` by default. When toggled off, this skill has to be [unlocked](https://docs.phoenixdevt.fr/mmocore/skills/unlocking) through the use of a command, quest trigger, skill book, exp table...

### Needs Binding {#needs-binding}

Another option is `needs-bound`. This option is only relevant for passive skills, as active skills must all be bound. When set to `false`, the passive skill takes effect even if not bound (and therefore can no longer be bound to any skill slot).

### Skill Parameters {#skill-parameters}

You might also want to change the skill numerical parameters, so that a fireball cast by the *Mage* class deals more damage than a fireball cast by the *Paladin* class. Each parameter of each skill can be edited by adding the corresponding entry to the class skill config. For instance (see above), the `damage` parameter for the *Fire Storm* skill is set to equal 5 Dmg, plus 3 Dmg per skill level. These skill parameters do not scale with the player's level but rather with the skill level. The skill level increases when a skill is [upgraded](https://docs.phoenixdevt.fr/mmocore/skills/intro#upgrading-a-skill).

![PhIpbOr](https://docs.phoenixdevt.fr/assets/skill_ui_item.C1NBhUEq.png)

## Skill Folder {#skill-folder}

You might feel like the configs above might be lacking essential information, like its name, description icon, what it does, etc.

Note that the configs above ("class skill" configs) do not create skills, they simply allow skills to be used by a certain class. Skills are created/defined inside the `MythicLib/skill` folder. Please refer to [this wiki page](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic.html#_2-declare-it-as-a-mythiclib-skill) for more information.

Any skill that you use inside a class configuration must be registered somewhere inside the `MythicLib/skill` folder. If not, MMOCore will throw an error when trying to load the class.

## Passive Skills {#passive-skills}

To create a passive skill, all you have to do is specify a [trigger](https://docs.phoenixdevt.fr/mythiclib/skills/triggers) for that skill. Any skill with no trigger is considered an active skill, while any skill with a trigger is considered a passive skill. The trigger defines when the skill takes effect.

The following class skill is a passive skill that is triggered every time the player attacks an entity. It uses the `ATTACK` trigger.

```yml
skills:
  MY_CUSTOM_SKILL_2:
    level: 1
    max-level: 30
    trigger: ATTACK # <<==== Here
    ...
```

The following skill is a passive skill that runs once every 5 seconds. It uses the `TIMER` trigger with the `timer` modifier set to `5`.

```yml
skills:
  MY_CUSTOM_SKILL_1:
    level: 1
    max-level: 30
    trigger: TIMER # <<==== Here
    timer: 5
    ...
```

Note that the `trigger` config option overrides the `trigger` option specified in the MythicLib skill config. If a trigger is specified in MythicLib but not in the MMOCore class config, the skill will still be considered a passive skill, and it will use the trigger specified in MythicLib. If both are specified, MMOCore takes precedence.
