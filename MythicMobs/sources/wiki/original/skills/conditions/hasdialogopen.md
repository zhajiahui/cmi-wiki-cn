# Has Dialog Open

## Description {#description}

Checks if the target player has a MythicMobs [dialog](https://wiki.mythiccraft.io/mythicmobs/Dialogs) open. [showDialog](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ShowDialog) makes it true until:

- a button or [clickable text](https://wiki.mythiccraft.io/mythicmobs/Dialogs#clickable-text) click, with `AfterAction: CLOSE`
- a click running no skills, with `AfterAction: WAIT_FOR_RESPONSE`
- an `ExitButton` click
- [closeDialog](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CloseDialog) runs
- the player leaves the server

Unless `CanClose: false`, Escape closes the dialog on screen and [clicks a button](https://wiki.mythiccraft.io/mythicmobs/Dialogs#closing-with-escape). Escape clicks nothing on a [multi-action dialog](https://wiki.mythiccraft.io/mythicmobs/Dialogs#buttons) without an `ExitButton`. If no click from the list above happens, the condition stays true until `closeDialog` runs, the player leaves the server, or a later dialog closes.

> **This is a [Paper-Only](https://papermc.io/downloads/all) condition!**

> **This is a [Premium-Only](https://wiki.mythiccraft.io/mythicmobs/Premium-Features) condition!**

## Attributes {#attributes}

*This condition has no attributes*

## Examples {#examples}

```yaml
  Conditions:
  - hasDialogOpen true
```

## Aliases {#aliases}

- dialogOpen
