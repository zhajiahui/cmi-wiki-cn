# On Hear

## Description {#description}

Executes the skill when the mob hears a sound, [if this feature has been enabled](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#hearing).  
The `<skill.var.volume>` [placeholder](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) can be used in the triggered skill to return a float value between 1 and 15 representing the distance from the sound source

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the entity that generated the sound

> The associated [@origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Origin) is the location where the sound was generated

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<skill.var.volume>` |
| `<skill.var.sound-type>` |

## Examples {#examples}

```yaml
ICanHearYou:
  Type: ZOMBIE
  Hearing:
    Enabled: true
  Skills:
  - message{m="I can hear you <trigger.name>! <skill.var.volume>? Way too loud!"} @trigger ~onHear
```

## Aliases {#aliases}

- onVibration
