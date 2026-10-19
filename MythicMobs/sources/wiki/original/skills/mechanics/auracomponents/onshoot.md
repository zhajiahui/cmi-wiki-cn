# On Shoot

## Description {#description}

Applies an aura component to the target that triggers a skill when they shoot with a bow. Can use any [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) attribute

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<skill.var.bow-tension>` |

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| onShootSkill | onshoot, osh, onbowshoot, onbowshootskill | Skill to execute when the entity shoots |  |
| cancelEvent | cE | Whether or not to cancel the event that triggered the aura | false |

## Examples {#examples}

```yaml
  Skills:
    - aura{auraName=fireball_bow;duration=200;charges=5;components=[
      - onShoot{onShoot=[ shootfireball ];cancelEvent=true} @self
      ]} @self
```

In this example, the caster's next 5 bow shots will shoot fireballs
instead of arrows.

## Aliases {#aliases}

- onbowshoot
