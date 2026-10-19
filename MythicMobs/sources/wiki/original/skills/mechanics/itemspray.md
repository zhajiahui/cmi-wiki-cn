# Itemspray

## Description {#description}

Causes an explosion of temporary items at the target location.  
Unless otherwise specified with the `allowpickup` option, those items will be packets, only existing on the client of the players and not on the server.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| items | item, i | The list of items to drop. This attribute works like the [DropItem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/dropitem)'s one | iron_sword |
| amount | a | How many items will render from the spray | 10 |
| duration | d | How long (in ticks) the items will exist | 20 |
| radius | r | The radius/spread the items will start in | 0 |
| velocity | v, force, f | The velocity of the items | 1 |
| yVelocity | yv, yforce, yf | The Y velocity of the items | `velocity` |
| yOffset | yo, y | The y offset the items will start at | 1 |
| allowpickup | ap | Whether the itemspray's items should be real items, enabling players to pick them up | false |
| gravity | g | Whether the items should be affected by gravity | true |
| audience |  | The [audience](https://wiki.mythiccraft.io/mythicmobs/Skills/Audience) of the effect | world |

## Examples {#examples}

```yaml
  Skills:
  - itemspray{item=iron_sword;amount=20;velocity=5;d=100} @self
```

## Aliases {#aliases}

- effect:itemspray
- e:itemspray
