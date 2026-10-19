# Region

## Description {#description}

Special targeter to target a region. Only works with specific mechanics

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| min |  | The location of the first point | 0,0,0 |
| max |  | The location of the second point | 0,0,0 |
| world |  | The world the region is in | `<caster.l.w>` |

### Min and Max attributes {#min-and-max-attributes}

The returned region will be the one contained between those two points

## Examples {#examples}

```yaml
  Skills:
  - worldEditReplace{from=STONE;to=AIR} @Region{min=0,0,0;max=100,100,100;world=resources}
```
