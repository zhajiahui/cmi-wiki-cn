# Sphere

## Description {#description}

Targets points in a sphere around the caster

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the targeter | 5 |
| points | p | The amount of points | 10 |
| yoffset | y | The offset of the targets on the y axis | 0 |
| exact | e | If the targeter should draw a perfect sphere | false |

## Examples {#examples}

```yaml
ExampleSkill:
  Skills:
  - effect:particles @Sphere{r=6;points=50}
```
