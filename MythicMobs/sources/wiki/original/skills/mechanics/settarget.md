# Settarget

## Description {#description}

Sets the mob's target to the target entity.
If using threat tables, will increase threat to the threshold to change targets for the targeted entity.

## Attributes {#attributes}

> *This mechanic has no attributes*

## Examples {#examples}

Sets the caster's target to the trigger when right clicked.

```yaml
  Skills:
  - setTarget @trigger ~onInteract
```

## Aliases {#aliases}

- target
