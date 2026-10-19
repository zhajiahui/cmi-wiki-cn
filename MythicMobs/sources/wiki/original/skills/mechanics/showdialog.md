# Show Dialog

## Description {#description}

Shows the target player a [dialog](https://wiki.mythiccraft.io/mythicmobs/Dialogs) from the `dialogs` folder: a window with text, items, inputs and buttons. Needs 1.21.6 or newer. On Folia, it opens on the player's region thread.

In dialog text, `<target.*>` is the viewer and `<caster.*>` is this mechanic's caster. With no shown `Buttons` entry, nothing opens and an error is logged. The `ExitButton` does not count.

> **This is a [Paper-Only](https://papermc.io/downloads/all) mechanic!**

> **This is a [Premium-Only](https://wiki.mythiccraft.io/mythicmobs/Premium-Features) mechanic!**

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<dialog.button>` |
| `<dialog.[key]>` |
| `<dialog.page>` |
| `<dialog.pages>` |

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| dialog | d, name | Dialog name. Case-sensitive. Supports placeholders | default |

## Response Variables {#response-variables}

Button and clickable text skills get these values:

| Variable | Value |
| --- | --- |
| `dialog.button` | The clicked button's position among shown buttons, from 0. `-1` for the `ExitButton`, `-2` for [clickable text](https://wiki.mythiccraft.io/mythicmobs/Dialogs#clickable-text) |
| `dialog.[key]` | Each shown input, by its `Key`. Clickable text sends only its `key=value` arguments |
| `dialog.page`, `dialog.pages` | Page (from 1) and page count, set only by dialogs with [`PageSize`](https://wiki.mythiccraft.io/mythicmobs/Dialogs#generated-lists) |
| Other `dialog.*` | Every value the dialog opened with |

Input values are text:

- `text`: the typed text. Tags, `<skill>` included, get a `\` in front
- `bool`: `true` or `false`
- `range`: a decimal such as `5.0`
- `option`: the option's key

In `var=` attributes, write `skill.dialog.[key]`.

The skills keep this mechanic's caster. Mechanics without a targeter act on the clicking player. Clicks expire 10 minutes after the dialog opens.

## Navigation {#navigation}

For Back or Refresh buttons, use `showDialog` with the previous or same dialog. The `dialog.*` values [are kept](https://wiki.mythiccraft.io/mythicmobs/Dialogs#passing-values-between-dialogs), so entries stay filled in.

## Examples {#examples}

Shows `WelcomeNotice` to the triggering player.

```yaml
  Skills:
  - showDialog{dialog=WelcomeNotice} @trigger
```

##  {#section}

Shows `CharacterSetup` to every player within 10 blocks.

```yaml
  Skills:
  - showDialog{d=CharacterSetup} @PlayersInRadius{r=10}
```

##  {#section-2}

Shows `PunishMenu` to the caster, which must be a player, with the trigger's name as `<dialog.target>`.

```yaml
  Skills:
  - setvariable{var=skill.dialog.target;type=STRING;value="<trigger.name>"}
  - showDialog{dialog=PunishMenu} @self
```

## Aliases {#aliases}

- openDialog
- dialog
