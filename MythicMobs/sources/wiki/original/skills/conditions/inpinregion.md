# In Pin Region

## Description {#description}

Checks if the target location is within a region delimited by two [pins](https://wiki.mythiccraft.io/mythicmobs/Pins).

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| pin1 | p1 | The first [pin](https://wiki.mythiccraft.io/mythicmobs/Pins) |  |
| pin2 | p2 | The second [pin](https://wiki.mythiccraft.io/mythicmobs/Pins) |  |

## Examples {#examples}

```yaml
  TargetConditions:
  - inpinregion{p1=mypin;p2=anotherpin}
```
