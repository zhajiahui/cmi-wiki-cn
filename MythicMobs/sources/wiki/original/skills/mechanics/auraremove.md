# Auraremove

## Description {#description}

Removes an aura from the target.

You can decide if the aura executes its `onEnd` metaskill via the `DoEndSkillOnTerminate` attribute of the [Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) mechanic.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| auraName | aura, b, buff, buffname, debuff, debuffname, n, name | The name of the aura | default |
| stacks | s | The amount of stacks | Max stacks |

### Aura Attribute {#aura-attribute}

You can specify `ANY` as the value of the attribute in order to remove every aura on the target

## Examples {#examples}

```yaml
  Skills:
  - auraremove{aura=Ice;stacks=10} @self ~onTimer:200
```

## Aliases {#aliases}

- removeaura
- removebuff
- removedebuff
