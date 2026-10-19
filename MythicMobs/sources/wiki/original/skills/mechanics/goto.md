# Goto

## Description {#description}

Causes the mob to pathfind to a location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| speed | s | The movement speed modifier | 1 |
| spreadH | sh | Amount of horizontal spread it can be away from the target its moving towards | 0 |
| spreadV | sv | Amount of vertical spread it can be away from the target its moving towards | 0 |

## Examples {#examples}

```yml
  Skills:
  - goto{speed=1;sh=5;sv=5} @owner
  - goto{speed=1;sh=5;sv=5} @location{c=100,65,100}
```

## Aliases {#aliases}

- pathto
- navigateto
