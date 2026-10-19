# Disguisetarget

## Description {#description}

Runs a disguise string on the target mob. This skill requires Libs'
Disguises be installed to enable Disguise functionality.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| disguise | d, type | The disguise to apply to the target. | player Ashijin |
| audience |  | The [audience](https://wiki.mythiccraft.io/mythicmobs/Skills/Audience) of the disguise |  |

## Examples {#examples}

```yaml
Skills:
  - disguisetarget{d=SHEEP} @target
```

> This example would cause the target to turn into a sheep.

##  {#section}

```yaml
Skills:
  - disguisetarget{d="player libraryaddict setCustomName '&7Jeb' setSkin Notch.png"} @target
```

> This one would turn it into a player using the skin of Notch and giving it the display name *Jeb*. Color codes are useable in the nametag field.
