# Clear Target

## Description {#description}

Forces the target of the mechanic to reset its current target

## Attributes {#attributes}

> *This mechanic has no attributes*

## Examples {#examples}

```yaml
  Skills:
  - cleartarget @self ~onTimer:20 ?targetalive ?!targetwithin{d=20}
```

## Aliases {#aliases}

- resetTarget
