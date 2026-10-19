# Modifytargetscore

## Description {#description}

Modifies the a scoreboard-objective value of the specified targeter(s).

A list of possible operations for the action-syntax:

- `SET`
- `ADD`
- `SUBTRACT`
- `MULTIPLY`
- `DIVIDE`
- `MOD` [^mod]

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| objective | obj, o | Specifies the scoreboard objectiv to be changed. If the objective doesn't exist it will automatically be created by the mechanic |  |
| action | a | The operation to perform | ADD |
| value | v | The value to perform the operation with |  |

## Examples {#examples}

This example will track how often and whom damaged
the casting mob in battle.

```yaml
  Skills:
  - modifytargetscore{objective=damagescore;action=add;value=1} @trigger ~onDamaged
```

## Aliases {#aliases}

- mts

[^mod]: shorthand for "Modular Division"
