# Origin Location

## Description {#description}

Checks if the [origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Origin) is at a given location

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| location | loc, l, c | The location to match, written as `x,y,z`. |  |
| x |  | The x coordinate of the location, ignored if the location attribute is set | 0 |
| y |  | The y coordinate of the location, ignored if the location attribute is set | 0 |
| z |  | The z coordinate of the location, ignored if the location attribute is set | 0 |
| exact | e | Whether to match the location exactly | false |

## Examples {#examples}

```yaml
  Conditions:
  - originLocation{loc=10,20,30} true
```
