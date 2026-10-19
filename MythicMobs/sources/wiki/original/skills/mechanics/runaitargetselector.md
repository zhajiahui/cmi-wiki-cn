# Runaitargetselector

## Description {#description}

Change target pathfindergoals. It is not possible to use every goal on
every entity. To change the ai of an entity, you need to use clear
first. After that you can use the runaitargetselector and add the goals
you need. Unlike the mob configuration, if you use the
runaitargetselector skill, you can only use one pathfindergoal in the
mechanic. But aslong as you dont use clear, the pathfindergoal is added
to the end of the already existing goals of the entity.

A list of available targets can be found [here](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ai-target-selectors)

> **This is a no-target mechanic, and the affected entity will always be the caster**

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| target | aitargetselector, s, string, targetselector, goal, g | The target selector you want to append |  |

## Examples {#examples}

```yaml
TargetPossibleThreats:
  Skills:
  - runaitargetselector{target=clear}
  - runaitargetselector{target=players}
  - runaitargetselector{target=monsters}
```

## Aliases {#aliases}

- aitarget
