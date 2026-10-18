# 🔥 Skills {#🔥-skills}

Skills are amazing and unique abilities that players can use to defeat their enemies or buff their party mates fighting and surviving.

Skills are either **active or passive**. Active skills refer to skills proactively [cast by the player](https://docs.phoenixdevt.fr/mmocore/skills/casting). Passive skills cannot be cast - instead, they automatically trigger on specific events (attacks, clicks, movements, other skills...).

Skills are class-specific. When changing class, the player will "lose" the progress they made on their skills and unlock new ones. Previous progress is recovered when switching classes again.

## Custom Skills {#custom-skills}

While MMOCore comes with more than 90 built-in skills, you can create as many custom skills as you want using the most popular skill/scripting languages available, including MythicMobs, MythicLib or Fabled.

Note that custom skills are registered in MythicLib. Any skill you register in MythicLib will be automatically forwarded to both MMOCore and MMOItems. Please read [this wiki page](https://docs.phoenixdevt.fr/mythiclib/skills/intro) to learn how to create and register custom skills.

## Overview {#overview}

In order to use a skill, players need to:

1. Choose a [class](https://docs.phoenixdevt.fr/mmocore/features/classes) optional
2. [Unlock](https://docs.phoenixdevt.fr/mmocore/skills/unlocking) a skill optional
3. [Bind](https://docs.phoenixdevt.fr/mmocore/skills/binding) the skill to a compatible skill slot optional
4. [Cast](https://docs.phoenixdevt.fr/mmocore/skills/casting) the skill

However, the MMOCore skill system is really permissive:

1. The default class can also have skills, so technically players do not need to choose a class to be able to cast skills. If you don't plan on using the class system, you can still use MMOCore skills.
2. Skills can be unlocked when reaching a certain level, finishing a quest, unlocking a node in a skill tree or virtually anything else. Skills can also be made unlocked by default.
3. Skills can be manually bound using commands, or hard-set to automatically bound to skill slots if you don't like the MMOCore skill binding feature.
4. Obviously skill casting is a mandatory step, it is the only one that you cannot skip!

## Skill GUI {#skill-gui}

Players can open up the skills GUI by using `/skills`. This UI allows players to visualize their available skills and their effects, upgrade their available skills, and bind their skills to skill slots.

## Upgrading a skill {#upgrading-a-skill}

Upgrading a skill **increases its power**. Players can choose the skill they would like to upgrade based on their play style and skill path they want to follow. Upgrading a skill takes **one skill point**.

Skill points are a currency which players can use to upgrade their skills. One upgrade costs one skill point. Skill points can be granted using the following [admin command](https://docs.phoenixdevt.fr/mmocore/general/commands):

```cmd
/mmocore admin skill-points give <player> <amount>
```

![upgrade1](https://docs.phoenixdevt.fr/assets/upgrade1.Cr3v1DRG.gif)

In the GUI, select the skill you'd like to upgrade by clicking it. The name of the selected skill displays in the UI name. You can then upgrade the selected skill by clicking the *Upgrade Skill* button. Items next to the *Upgrade Skill* button let the user visualize how strong the skill would be with a higher level.

## Skill Buffs {#skill-buffs}

A skill buff modifies the value of a certain skill modifier. It can target one or multiple skills using [category formulas](https://docs.phoenixdevt.fr/mmocore/skills/) and can only target 1 modifier. Skill Buffs can only be granted through [skill slots](https://docs.phoenixdevt.fr/mmocore/skills/binding#skill-slots) and [triggers](https://docs.phoenixdevt.fr/mmocore/misc/triggers) (and per extension, skill trees).

```yml
triggers: 
  # -10% cooldown to ALL skills
- 'skill_buff{formula="true";modifier="cooldown";amount=-10;type=RELATIVE}'
  # +20 Flat damage to skill with name FIRE_STORM
- 'skill_buff{formula="<FIRE_STORM>";modifier="damage";amount=20;type=FLAT}'
  # 20 Flat damage to skills with category MY_OWN_CATEGORY
- 'skill_buff{formula="<MY_OWN_CATEGORY>";modifier="damage";amount=20;type="FLAT"}'
```

Note that the syntax for targeting a skill category or a specific skill name is the same.

## Editing the skill GUI {#editing-the-skill-gui}

The skill GUI can be edited by modifying the `gui/skill-view.yml` config file.

> **TIP**
>
> We recommend opening this file with a text editor on the side while reading the rest of this section.

First, please refer to [this wiki page](https://docs.phoenixdevt.fr/mythiclib/misc/ui-syntax) to learn about the general MMOCore UI syntax.

### Item Functions {#item-functions}

The `next` and `previous` functions are used for pagination.

`skill` is the item displayed for every skill available to the player. Its lore is a bit complicated:

- The line starting with `{unlocked}` only displays if the player has unlocked the skill
- The line starting with `{locked}` only displays if the player has NOT unlocked the skill yet
- The line starting with `{max_level}` displays when the player has reached the max skill level
- `{lore}` just copies and pastes the entire skill description

![image](https://docs.phoenixdevt.fr/assets/item_skill.CJXgT6sZ.png)

`switch` is the item that you'd click when switching from binding to upgrading mode

![image](data:image/png;base64,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)

`skill-slot` is the item used in the binding mode

![image](https://docs.phoenixdevt.fr/assets/item_slot.DWnJakgS.png)

`skill-level` are the items used to tell the player how the selected skill would behave if it had a higher level

![image](https://docs.phoenixdevt.fr/assets/item_level.BPUwfCvz.png)

`upgrade` is the item clicked when you want to upgrade the selected skill

![image](https://docs.phoenixdevt.fr/assets/item_upgrade.CauTLTdJ.png)
