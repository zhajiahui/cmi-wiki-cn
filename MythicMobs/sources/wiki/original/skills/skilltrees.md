SkillTrees are an implicit feature of Mythic and, while they cannot be directly invoked like [Metaskills](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) or other features, play just as important a role.

SkillTrees are **created each time a mechanic is fired by a trigger**, and it is the place where skill scoped [variables](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables) are stored and inside which [metaskills](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) exist

1. [SkillTree Structure](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees#skilltree-structure)
   1. [Skill Scoped Variables](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees#skill-scoped-variables)
   2. [Event Data](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees#event-data)
   3. [MetaSkills](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees#metaskills)
      1. [Caster](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees#caster)
      2. [Target](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees#target)
      3. [Trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees#trigger)
      4. [Origin](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees#origin)
      5. [Skill Parameters](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees#skill-parameters)

# SkillTree Structure {#skilltree-structure}

```mermaid
stateDiagram-v2
    state SkillTree {
        SkillScopedVariables
        EventData
        state MetaSkills {
            state MetaSkill {
                MetaSkillInfo: MetaSkill Info
                state MetaSkillInfo {
                    Caster
                    Targets
                    Trigger
                    Origin
                    SkillParameters
                }
                state Mechanics {
                    Mechanic1 Mechanic2 Mechanic3
                }
            }
            
        }
    }
```

## Skill Scoped Variables {#skill-scoped-variables}

Since they exist in the skilltree itself, skill-scoped variables can be accessed and modified by any [metaskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) in the skilltree from the moment they are created, regardless of which [metaskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) created them

## Event Data {#event-data}

The skilltree always knows which event triggered it, and allows the [cancelevent](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/cancelevent) mechanic to be used in any of the metaskill it calls in order to cancel it, as long as this occurs in a synched manner

## MetaSkills {#metaskills}

Each [Metaskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) that is being called in the SkillTree has its own set of data regarding different elements.
Normally, the value of those elements is copied over from the calling metaskill unless overridden.  
Those elements are:

### `Caster` {#caster}

The entity casting the metaskill.

- Can be changed via the use of the [sudoskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SudoSkill) mechanic

### `Target` {#target}

It is the [Inherited Target](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#inheritance) of the metaskill

### `Trigger` {#trigger}

Is first set as the entity that triggered the SkillTree initially, and one can fetch this entity via the [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) targeter or other similar targeters. Depending on the [~Trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers) used, a [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) may not exist.

- The `Trigger` can be changed via the use of the [sudoskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SudoSkill) mechanic's `casterastrigger` attribute, which will make the called metaskill have, as the `Trigger`, the `Caster` of the original metaskill

### `Origin` {#origin}

It's the [@origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Origin) of the metaskill. By default, it is the position of the `Caster`.

- Can be set via the `origin` [universal attribute](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics#universal-attributes)
- It is automatically set in mechanics such as [projectile](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Projectile)

### `Skill Parameters` {#skill-parameters}

The [Skill Parameters](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#skill-parameters-premium-feature) of the metaskill. Please note that, contrary to [Skill Scoped Variables](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees#skill-scoped-variables), they do not exist on the skilltree itself.
