# For Each Pin

## Description {#description}

Runs a given metaskill for each pin in a multi-pin

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| name | n, pin, p, key, k | The name of the pin |  |

> This mechanic inherits every attribute of the [Skill](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/skill) mechanic

## Examples {#examples}

```yaml
  Skills:
  - foreachpin{name=YourCoolPin;skill=[
    - particle{p=flame;a=20}
    ]} @self
```
