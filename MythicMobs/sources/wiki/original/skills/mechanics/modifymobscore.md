# Modifymobscore

## Description {#description}

Modifies the scoreboard-objective value of the casting mob.
Does not support targeters.

## Attributes {#attributes}

> This mechanic inherits every attribute of the [ModifyGlobalScore](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/modifyglobalscore) mechanic

## Examples {#examples}

```yaml
  Skills:
  - modifymobscore
      {
      objective=someobjective;
      action=multiply;
      v=2
      } ~onAttack
```

## Aliases {#aliases}

- mms
