# Not Living Near Origin

## Description {#description}

Targets all non living entities in a radius near the origin

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the targeter | 5 |

## Examples {#examples}

This mechanic will say in the global chat the UUID of every non living entity in a 10 block radius from itself once it ends

```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onEnd=[
      - command{c="say <target.uuid>"} @NotLivingNearOrigin{r=10}
    ]}
```

## Aliases {#aliases}

- nonLivingNearOrigin
- NLNO
