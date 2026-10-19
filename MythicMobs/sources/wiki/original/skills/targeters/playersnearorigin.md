# Players Near Origin

## Description {#description}

Targets all players in the given radius around the origin of the metaskill.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the targeter | 5 |

## Examples {#examples}

In this example, when the created projectile ends for whatever reason, it will damage every player in a 2 block radius around itself

```yaml
  Skills:
  - projectile{...;
    onTick=[
      - effect:particles @origin
    ];
    onEnd=[
      - damage{a=10} @PlayersNearOrigin{r=2}
    ]
    } @target
```

## Aliases {#aliases}

- playersnearsource
- PNO
