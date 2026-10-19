# Onskilldamage

## Description {#description}

Executes the skill when the mob deals damage to other entities via a mechanic.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the entity that was damaged

## Examples {#examples}

```yaml
ExampleMob:
  Type: 
  Skills:
  - damage @PIR{r=10} ~onTimer:20
  - message{m="Get damaged! MUHAHAHA"} @trigger ~onSkillDamage
```

## Aliases {#aliases}

- onSkillHit
- onSkill_Damage
