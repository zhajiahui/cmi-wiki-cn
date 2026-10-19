# Close Dialog

## Description {#description}

Closes the target player's open [dialog](https://wiki.mythiccraft.io/mythicmobs/Dialogs), if any, even from another plugin.

Servers before 1.21.8 leave it on screen. Clicks then run no MythicMobs skills, and [hasDialogOpen](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/HasDialogOpen) becomes false.

Without a targeter, it uses the [inherited targets](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#inheritance), or else the caster. In button skills, that is the clicking player.

> **This is a [Paper-Only](https://papermc.io/downloads/all) mechanic!**

> **This is a [Premium-Only](https://wiki.mythiccraft.io/mythicmobs/Premium-Features) mechanic!**

## Attributes {#attributes}

*This mechanic has no attributes*

## Examples {#examples}

Closes the triggering player's dialog.

```yaml
  Skills:
  - closeDialog @trigger
```

##  {#section}

Closes the dialogs of players within 10 blocks.

```yaml
  Skills:
  - closeDialog @PlayersInRadius{r=10}
```

## Aliases {#aliases}

- hideDialog
