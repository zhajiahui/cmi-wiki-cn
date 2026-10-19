# Jump

## Description {#description}

Causes the mob to jump with the given velocity. Using the velocity
*0.75* will make the mob jump approximately 1 block high. Can be a
negative number, too.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| velocity | v | The velocity of the mob's jump | 1 |

## Examples {#examples}

```yaml
SuperJump:
  Skills:
  - jump{velocity=20}
```
