# Stun

## Description {#description}

Holds the target in place temporarily.

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><path d="M21.73 18 13.73 4a2 2 0 0 0-3.46 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"></path><path d="M12 9v4"></path><path d="M12 17h.01"></path></svg>Warning

This mechanic can cause Spigot to kick the player (`PlayerName moved wrongly!`)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| stopai | ai | Removes entity AI while stunned | false |
| gravity | g | Remove gravity from target when stunned (1.9+) | false |
| facing | face, f | When false, entity cannot rotate or look around when stunned | false |
| noknockback | nokb, kb | When true, entity cannot be knocked back when stunned | false |

## Examples {#examples}

Stuns the target for 3 seconds, during which the target cannot rotate.

```yaml
ExampleSkill:
  Skills:
  - aura{d=60;components=[
    - stun{f=false}    
    ]} @target
```

## Aliases {#aliases}

- stunned
