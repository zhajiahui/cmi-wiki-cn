# Variableadd

## Description {#description}

Adds an amount to a [variable](https://wiki.mythiccraft.io/mythicmobs/skills/variables) on the specified
scope.

> This mechanic has different behavior based on the variable type. [More Info Here](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-types-behavior)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a, value, val, v | The value to add | 0 |

> This mechanic inherits every *inheritable* attribute of the [SetVariable](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setvariable) mechanic

## Examples {#examples}

```yaml
  Skills:
  - variableadd{var=skill.testVar;amount=1} ~onInteract
```

## Aliases {#aliases}

- addVariable
- varAdd
- addVar
- incrementVariable
