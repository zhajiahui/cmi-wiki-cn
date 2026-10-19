# Modifyprojectile

## Description {#description}

Modifies the projectile, missile, or orbital that activated the mechanic.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| trait | t | The trait to modify: `INERTIA`, `POWER`, `VELOCITY`, `RADIUS` and `YOFFSET` | `VELOCITY` |
| action | a | The action to perform for modifying the projectile trait: `ADD`, `SET`, `MULTIPLY` | `MULTIPLY` |
| value | v | The value to use for the modification | 0 |

### Trait Attribute {#trait-attribute}

The possible values are:

- `INERTIA` - The inertia of the [missile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/missile).
- `POWER` - The power of the [projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile), [missile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/missile), [orbital](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/orbital)
- `VELOCITY` - The power of the [projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile), [missile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/missile)
- `RADIUS` - The power of the [orbital](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/orbital)
- `YOFFSET` - The height of the [orbital](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/orbital)

## Examples {#examples}

In this example when you shoot the projectile you will watch it slow down gradually to a halt. To test this you can cast it using the in game command below after adding it to a skills.yml file.

`/mm test cast TestingModifyProjectile`

```yaml
TestingModifyProjectile:
  Skills:
  - projectile{oT=TMP_oT;i=1;v=8;d=200;mr=100} @forward{f=100;y=0}
TMP_oT:
  Skills:
  - particles{particle=flame;a=2;hs=0;vs=0;s=0;y=0} @origin
  - modifyProjectile{trait=VELOCITY;action=MULTIPLY;value=0.95}
```
