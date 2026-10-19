# Runaigoalselector

## Description {#description}

Change pathfindergoals. It is not possible to use every goal on every
entity. To change the ai of an entity, you need to use clear first.
After that you can use the runaigoalselector and add the goals you need.
Unlike the mob configuration, if you use the runaigoalselector skill,
you can only use one pathfindergoal in the mechanic. But aslong as you
dont use clear, the pathfindergoal is added to the end of the already
existing goals of the entity.

A list of AI Goals can be found
[here](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ai-goal-selectors)
More complex goals, such as a patrol with locations, may need to be inputted as a string, such as the below example.

> **This is a no-target mechanic, and the affected entity will always be the caster**

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| goal | aigoalselector, g, goalselector, s, string, t, target | The ai goal selector you want to append |  |

## Examples {#examples}

```yaml
ChangePathfinderGoalExample:
  Skills:
  - runaigoalselector{goal=clear} # wipes previous pathfinding objectives
  - runaigoalselector{goal=fleesun} # prioritizes avoiding sunlight exposure
  - runaigoalselector{goal=randomstroll} # randomly wanders
  - runaigoalselector{goal="patrol 1494,38,10;1494,38,-10;1514,38,-10;1514,38,10"} # passively wanders between various coordinates
```

## Aliases {#aliases}

- aigoal
- aigoals
