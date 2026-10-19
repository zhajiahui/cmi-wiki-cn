# Mobs Near Origin

## Description {#description}

Targets all MythicMobs or vanilla overrides of the given type(s) in a radius around the origin

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the targeter | 5 |
| types | type, t | The type(s) of the target MythicMobs. Can be a list |  |

## Examples {#examples}

This skill will ignite every mob of the given type in a radius around itself when it ends

```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onEnd=[
      - ignite @MobsNearOrigin{r=10;types=IncredibleZombie,SpookyScarySkeleton}
    ]}
```

## Aliases {#aliases}

- mobssnearsource
