# Living Near Target Location

## Description {#description}

Targets all living entities near the inherited target

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the targeter | 5 |

## Examples {#examples}

This mechanic will damage every entity in a 2 block radius from the target of the mob once executed

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @target

ExampleSkill2:
  Skills:
  - damage{a=10} @LivingNearTargetLocation{r=2}
```

## Aliases {#aliases}

- livingentitiesneartargetlocation
- LNTL
- ENTL
- ENT
