# Dialogs

Dialogs are interactive windows from the [Paper Dialog API](https://docs.papermc.io/paper/dev/dialogs). They are a **[Premium Feature](https://wiki.mythiccraft.io/mythicmobs/Premium-Features)** and need **Paper 1.21.6** or newer. Open one with the [showDialog](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ShowDialog) mechanic or `/mm dialogs show`.

Dialog text supports [MiniMessage](https://docs.advntr.dev/minimessage/format.html) and [placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders). [Legacy color codes](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#color-codes) such as `&c` stop a dialog from opening (the console logs `could not be shown`). Placeholders that return them also stop it, such as a mob name from `Display: '&6Guard'`.

1. [Configuration](https://wiki.mythiccraft.io/mythicmobs/Dialogs#configuration)
2. [Body Elements](https://wiki.mythiccraft.io/mythicmobs/Dialogs#body-elements)
3. [Inputs](https://wiki.mythiccraft.io/mythicmobs/Dialogs#inputs)
   1. [Input Values](https://wiki.mythiccraft.io/mythicmobs/Dialogs#input-values)
4. [Buttons](https://wiki.mythiccraft.io/mythicmobs/Dialogs#buttons)
   1. [After a Click](https://wiki.mythiccraft.io/mythicmobs/Dialogs#after-a-click)
   2. [Values in Button Skills](https://wiki.mythiccraft.io/mythicmobs/Dialogs#values-in-button-skills)
   3. [Closing with Escape](https://wiki.mythiccraft.io/mythicmobs/Dialogs#closing-with-escape)
   4. [Exit Button](https://wiki.mythiccraft.io/mythicmobs/Dialogs#exit-button)
5. [Conditions](https://wiki.mythiccraft.io/mythicmobs/Dialogs#conditions)
6. [Generated Lists](https://wiki.mythiccraft.io/mythicmobs/Dialogs#generated-lists)
   1. [Targeter Rows](https://wiki.mythiccraft.io/mythicmobs/Dialogs#targeter-rows)
   2. [Value Rows](https://wiki.mythiccraft.io/mythicmobs/Dialogs#value-rows)
   3. [Row Conditions](https://wiki.mythiccraft.io/mythicmobs/Dialogs#row-conditions)
   4. [Pages](https://wiki.mythiccraft.io/mythicmobs/Dialogs#pages)
   5. [Paged Player List](https://wiki.mythiccraft.io/mythicmobs/Dialogs#paged-player-list)
7. [Passing Values Between Dialogs](https://wiki.mythiccraft.io/mythicmobs/Dialogs#passing-values-between-dialogs)
8. [Validating Input](https://wiki.mythiccraft.io/mythicmobs/Dialogs#validating-input)
9. [Icons, Heads and Layout](https://wiki.mythiccraft.io/mythicmobs/Dialogs#icons-heads-and-layout)
   1. [Sprites and Heads](https://wiki.mythiccraft.io/mythicmobs/Dialogs#sprites-and-heads)
   2. [Named Icons](https://wiki.mythiccraft.io/mythicmobs/Dialogs#named-icons)
   3. [Layout with a Resource Pack](https://wiki.mythiccraft.io/mythicmobs/Dialogs#layout-with-a-resource-pack)
   4. [Clickable Text](https://wiki.mythiccraft.io/mythicmobs/Dialogs#clickable-text)
10. [Drawing Menus with MythicCrucible](https://wiki.mythiccraft.io/mythicmobs/Dialogs#drawing-menus-with-mythiccrucible)
    1. [Setup](https://wiki.mythiccraft.io/mythicmobs/Dialogs#setup)
    2. [Clickable Images](https://wiki.mythiccraft.io/mythicmobs/Dialogs#clickable-images)
    3. [Images That Change](https://wiki.mythiccraft.io/mythicmobs/Dialogs#images-that-change)
    4. [Placing Images](https://wiki.mythiccraft.io/mythicmobs/Dialogs#placing-images)
    5. [Background Panel](https://wiki.mythiccraft.io/mythicmobs/Dialogs#background-panel)
    6. [Tips](https://wiki.mythiccraft.io/mythicmobs/Dialogs#tips)
11. [Mechanics, Conditions and Commands](https://wiki.mythiccraft.io/mythicmobs/Dialogs#mechanics-conditions-and-commands)
12. [Developer API](https://wiki.mythiccraft.io/mythicmobs/Dialogs#developer-api)

## Configuration {#configuration}

MythicMobs loads all `.yml` files in the `dialogs` folders of `plugins/MythicMobs` and of [packs](https://wiki.mythiccraft.io/mythicmobs/Packs), subfolders included, and `.dialog.yml` files in a pack's `files` folder. Each dialog starts with its name (case-sensitive):

```yaml
WelcomeNotice:
  Title: "<gold>Welcome!"
  Body:
  - Type: text
    Message: "<gray>Welcome to the server, <target.name>!"
  Buttons:
  - Label: "<green>Got it!"
```

- `Title`: text at the top
- `ExternalTitle`: name on buttons that open it from other screens, such as the pause menu. Not shown when MythicMobs opens it
- `CanClose`: whether Escape closes it (default `true`), see [Closing with Escape](https://wiki.mythiccraft.io/mythicmobs/Dialogs#closing-with-escape)
- `Pause`: pauses the game, in singleplayer only (default `false`)
- `AfterAction`: what a click does (default `CLOSE`), see [After a Click](https://wiki.mythiccraft.io/mythicmobs/Dialogs#after-a-click)
- `Columns`: button columns of a multi-action dialog (default `1`)

In dialog text and `ForEach`, `<target.*>` is the viewing player and `<caster.*>` is whoever cast `showDialog`, such as a mob. With `/mm dialogs show`, both are that player.

## Body Elements {#body-elements}

`Body` lists text and item elements:

- `Type`: `text` or `item` (default `text`)
- `Message`: the text
- `Width`: up to 1024 pixels for text, 256 for items (default 256, items 64)
- `Item`: see below. Supports placeholders
- `Height`: item height, up to 256 pixels (default 64)
- `Decoration`: draws the item's count and durability bar (default `false`)
- `ShowTooltip`: shows the tooltip on hover (default `true`)

`Item` takes:

- a vanilla material or a Mythic item
- `mmoitems.TYPE.ID`
- a vanilla drop line, such as `DIAMOND{amount=3}`
- a [drop table](https://wiki.mythiccraft.io/mythicmobs/drops/DropTables), which gives a new random item each time

Other drop lines, such as `mmoitems{type=...;id=...}`, and unknown items show `STONE` and log an error.

## Inputs {#inputs}

A button click sends each input's value to its skills as `dialog.<key>`, where `<key>` is the input's `Key`. Inputs take:

- `Type`: `text` (text field), `bool` (checkbox), `range` (slider) or `option` (choice)
- `Key`: letters, digits and `_` only
- `Label`: text shown with the input
- `Initial`: starting value. Supports placeholders, not MiniMessage. See [Input Values](https://wiki.mythiccraft.io/mythicmobs/Dialogs#input-values)
- `Width`: up to 1024 pixels (default 200). Not for `bool`
- `LabelVisible`: shows the label (default `true`). Only for `text` and `option`

A `text` input also takes:

- `MaxLength`: maximum characters (default 256)
- `Multiline`: allows several lines (default `false`)
- `MaxLines`, `Height`: with `Multiline`, the maximum lines and the height, up to 512 pixels (default: the client's)

A `range` input also takes:

- `Start`, `End`: lowest and highest value (default 0 and 100)
- `Step`: step size, counted from `Initial`
- `LabelFormat`: slider text, in quotes, without placeholders or MiniMessage (default: `Label: value`). `"%s: %s"` shows the `Label` and the value, `"Volume %2$s"` only the value

Without `Initial`, steps count from the middle: `Start: 1`, `End: 10` and `Step: 1` give 1.5, 2.5 ... 9.5.

An `option` input also takes `Options` (required): `key: "Label"` pairs.

### Input Values {#input-values}

An input starts with its `dialog.<key>` value if set, otherwise with `Initial`. A click in the previous dialog, `setvariable{var=skill.dialog.<key>}` or `/mm dialogs show` can set it (see [Passing Values](https://wiki.mythiccraft.io/mythicmobs/Dialogs#passing-values-between-dialogs)).

| Type | Starting value | Submitted value |
| --- | --- | --- |
| `text` | Cut to `MaxLength` | Cut to `MaxLength` |
| `bool` | Only `true` checks it | `true` or `false` |
| `range` | Kept between `Start` and `End` | A decimal such as `5.0`, also kept in range |
| `option` | An unknown key selects the first option | The option key |

Typed tags, such as `<red>` and `<skill>`, get a `\` in front, so they add no colors, clicks or hovers. A reopened field shows that `\`. Typed `&` codes stay plain in dialogs but become colors in mechanics such as `message`.

Inputs hidden by `Conditions` send nothing and keep the value the dialog opened with. If a modified client sends invalid values, the skills do not run.

```yaml
CharacterSetup:
  AfterAction: WAIT_FOR_RESPONSE
  Inputs:
  - Type: text
    Key: nickname
    Label: "Display Name"
    Initial: "<target.name>"
  - Type: bool
    Key: pvpEnabled
    Label: "Enable PvP?"
    Initial: true
  - Type: range
    Key: difficulty
    Label: "Difficulty"
    Start: 1
    End: 10
    Initial: 5
    Step: 1
  - Type: option
    Key: classChoice
    Label: "Class"
    Initial: mage
    Options:
      warrior: "<red>Warrior"
      mage: "<blue>Mage"
  Buttons:
  - Label: "<green>Confirm"
    Skills:
    - message{m="<green>Saved <dialog.nickname> as <dialog.classChoice>"}
    - closeDialog
  - Label: "<red>Cancel"
```

## Buttons {#buttons}

The number of shown `Buttons` sets the type: 1 makes a notice, 2 a confirmation, and 3 or more a multi-action dialog with `Columns`. A shown `ExitButton` or a `ForEach` button also makes it multi-action. If no `Buttons` entry is shown (the `ExitButton` does not count), the dialog does not open.

- `Label`: button text
- `Tooltip`: text shown on hover
- `Width`: up to 1024 pixels (default 150)
- `Skill`: a skill to run on click, if its conditions pass
- `Skills`: mechanics to run on click, after `Skill`

```yaml
QuestOffer:
  Title: "<gold>New Quest Available"
  Buttons:
  - Label: "<green>Accept"
    Tooltip: "Accept this quest"
    Skills:
    - message{m="<green>Quest accepted!"}
  - Label: "<red>Decline"
```

### After a Click {#after-a-click}

- `CLOSE`: the dialog closes.
- `NONE`: the dialog stays open.
- `WAIT_FOR_RESPONSE`: a waiting screen shows until the skills run `showDialog` or `closeDialog`, so end them with one of these. If no skill runs (none set, failed conditions, invalid values or a cancelled click), the dialog closes.

Servers before 1.21.8 cannot close a dialog, so it stays open:

- after `closeDialog`
- after the `ExitButton` with `NONE`
- after a `WAIT_FOR_RESPONSE` click that runs no skill

Clicks expire after 10 minutes, or when the dialog is closed or replaced.

### Values in Button Skills {#values-in-button-skills}

Button skills keep the opening skill's caster and trigger, and target the clicking player, so mechanics without a targeter act on that player. They get:

- `dialog.button`: the clicked button's position among the shown buttons, from 0. `-1` for the `ExitButton`, `-2` for [clickable text](https://wiki.mythiccraft.io/mythicmobs/Dialogs#clickable-text)
- `dialog.<key>`: the value of each shown input
- `dialog.page`, `dialog.pages`: see [Pages](https://wiki.mythiccraft.io/mythicmobs/Dialogs#pages)
- every other `dialog.*` value the dialog opened with

In text, write `<dialog.nickname>`. In `var=` options, as in `setvariable`, write `skill.dialog.nickname`.

### Closing with Escape {#closing-with-escape}

With `CanClose: true`, Escape closes the dialog and clicks a notice's button, a confirmation's second button or the `ExitButton`. That click sends the input values.

### Exit Button {#exit-button}

`ExitButton` is one extra button with the same fields, except `ForEach` and `PageSize`. It closes the dialog under every `AfterAction`.

## Conditions {#conditions}

`Conditions` hide a body element, input, button or `ExitButton` from players who do not meet them.

```yaml
  Buttons:
  - Label: "<green>VIP Shop"
    Skill: OpenVIPShop
    Conditions:
    - hasTag{tag=vip}
```

Conditions treat the viewing player as the caster, even when a mob opened the dialog: `hasItem`, `holding`, caster variables and `<caster.*>` check that player. In dialog text, `<caster.*>` stays the mob. Conditions also see the `dialog.*` values.

## Generated Lists {#generated-lists}

A body element or button with `ForEach` repeats once per row. `PageSize` sets the rows per page (default: all). Keep one shown `Buttons` entry without `ForEach`, so the dialog still opens when the list is empty.

### Targeter Rows {#targeter-rows}

A `ForEach` starting with `@` is a targeter, such as `@PlayersInRadius{r=20}`. Each entity is a row with `<skill.value>` (its name), `<skill.uuid>` and `<skill.index>` (from 0). The targeter runs from the caster of `showDialog` and skips it unless you add `targetself=true`. With `/mm dialogs show`, include the viewer with `@PlayersOnServer{targetself=true}`.

```yaml
  Body:
  - Type: text
    ForEach: "@PlayersInRadius{r=20}"
    Message: "<skill.value>"
```

### Value Rows {#value-rows}

Any other `ForEach` has its placeholders filled in, then is split like the `values` of [forEachValue](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ForEachValue):

- `key=value;key2=value2`: a row per pair, with `<skill.key>` and `<skill.value>`
- `a,b,c`: a row per entry, with `<skill.value>`
- `a`: one row, with `<skill.value>`

Rows also have `<skill.index>`. Variables work, such as `ForEach: "<target.var.warps>"`.

```yaml
  Body:
  - Type: item
    ForEach: "DIAMOND,EMERALD,GOLD_INGOT"
    Item: "<skill.value>"
```

### Row Conditions {#row-conditions}

Placeholders and `Conditions` apply per row, so `Conditions` can filter rows. This keeps values of 100 or more:

```yaml
  Buttons:
  - ForEach: "<global.var.bounties>"
    Label: "<skill.key> <gold><skill.value>"
    Conditions:
    - compareValues{v1=<skill.value>;op=>=;v2=100}
```

### Pages {#pages}

`dialog.page` is the page (default 1, kept between 1 and the last page) and `dialog.pages` the page count. Only dialogs with `PageSize` change them. So a Back button to the list returns to the same page, and another paged dialog opened by a click starts on that page number. To start on page 1:

```yaml
    Skills:
    - setvariable{var=skill.dialog.page;type=INTEGER;value=1}
    - showDialog{dialog=WarpList}
```

### Paged Player List {#paged-player-list}

Six online players per page, with Previous and Next buttons that hide at the ends:

```yaml
OnlinePlayers:
  Title: "<gold>Players <gray>(<dialog.page>/<dialog.pages>)"
  AfterAction: WAIT_FOR_RESPONSE
  Buttons:
  - ForEach: "@PlayersOnServer{targetself=true}"
    PageSize: 6
    Label: "<skill.value>"
    Skills:
    - message{m="<gold>You picked <skill.value>"}
    - closeDialog
  - Label: "<gray>Previous"
    Conditions:
    - compareValues{v1=<dialog.page>;op=>;v2=1}
    Skills:
    - variableSubtract{var=skill.dialog.page;amount=1}
    - showDialog{dialog=OnlinePlayers}
  - Label: "<gray>Next"
    Conditions:
    - compareValues{v1=<dialog.page>;op=<;v2=<dialog.pages>}
    Skills:
    - variableAdd{var=skill.dialog.page;amount=1}
    - showDialog{dialog=OnlinePlayers}
  ExitButton:
    Label: "Close"
```

## Passing Values Between Dialogs {#passing-values-between-dialogs}

A click's `dialog.*` values carry into any `showDialog` its skills cast. A Back button is `showDialog{dialog=PreviousDialog}`, a Refresh button is `showDialog` of the same dialog, and the entries stay filled in.

From other skills, set the values first. In a mob skill, target the player with a targeter such as `@trigger`, not `@self`. Here the caster is a player:

```yaml
  Skills:
  - setvariable{var=skill.dialog.target;type=STRING;value="<trigger.name>"}
  - showDialog{dialog=PunishMenu} @self
```

The dialog reads `<dialog.target>`. The command takes `key=value` pairs without spaces: `/mm dialogs show PunishMenu Notch reason=griefing` sets `<dialog.reason>` to `griefing`.

## Validating Input {#validating-input}

Check values in a [metaskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills). `Conditions` hold the checks, and `FailedConditionsSkills` (mechanics) or `FailedConditionsSkill` (a skill name) run when one fails:

- Not empty: `stringNotEmpty{s="<dialog.name>"}`
- 3 or more characters: `compareValues{v1=<dialog.name.size>;op=>=;v2=3}`
- Digits only: `stringEquals{v1=<dialog.code.regex.^\d+$>;v2=true}`
- Number of 10 or more: `compareValues{v1=<dialog.amount>;op=>=;v2=10;type=DOUBLE}`

Without `type=DOUBLE`, non-numbers are compared as text, so `abc` passes.

To show an error, set `dialog.error` and reopen the dialog. The first body element shows only when the error is set:

```yaml
NameForm:
  Title: "<gold>Pick a name"
  AfterAction: WAIT_FOR_RESPONSE
  Body:
  - Type: text
    Message: "<dialog.error>"
    Conditions:
    - variableIsSet{var=skill.dialog.error}
  Inputs:
  - Type: text
    Key: name
    Label: "Name"
  Buttons:
  - Label: "<green>Save"
    Skill: SaveName
  - Label: "<red>Cancel"
```

In the `Skills` folder:

```yaml
SaveName:
  Conditions:
  - compareValues{v1=<dialog.name.size>;op=>=;v2=3}
  FailedConditionsSkills:
  - setvariable{var=skill.dialog.error;type=STRING;value="<red>Use at least 3 characters"}
  - showDialog{dialog=NameForm}
  Skills:
  - message{m="<green>Saved <dialog.name>"}
  - closeDialog
```

## Icons, Heads and Layout {#icons-heads-and-layout}

### Sprites and Heads {#sprites-and-heads}

Two MiniMessage tags draw images. Server and client both need 1.21.9 or newer:

- `<sprite:[atlas:]sprite>` draws a game or resource pack texture, such as `<sprite:"block/stone">`. The atlas is the texture's group, `minecraft:blocks` if left out. Quote names that contain `:`.
- `<head:name[:hat]>` draws a player's face, with the hat layer unless `hat` is `false`.

Item textures are in `minecraft:items` from 1.21.11, as in `<sprite:"minecraft:items":"item/diamond">`, and in `minecraft:blocks` before: `<sprite:"item/diamond">`.

Resource packs can add sprites to existing atlases, not new ones: `assets/mypack/textures/gui/sprites/icons/coin.png` becomes `<sprite:"minecraft:gui":"mypack:icons/coin">`. Both tags draw at 8x8. For other sizes, use [MythicCrucible font images](https://wiki.mythiccraft.io/mythicmobs/Dialogs#drawing-menus-with-mythiccrucible).

`<head>` takes a player name, such as `<head:<target.name>>`, or an online-mode UUID. Anything else, such as an offline-mode UUID or a name with spaces or colors, can stop the dialog from opening.

```yaml
  Body:
  - Type: text
    Message: '<sprite:"minecraft:gui":"hud/heart/full"> <red>Full health'
```

Placeholders work inside any MiniMessage tag, in all MythicMobs text: `<head:<skill.value>>` or `<click:run_command:/warp <skill.value>>`.

### Named Icons {#named-icons}

Define an icon once as a [static placeholder](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#custom-placeholders) in your pack's `placeholders.yml`:

```yaml
heart: "<sprite:'minecraft:gui':'hud/heart/full'>"
```

Then use it in any text: `Message: "<placeholder.heart> Full health"`. Static placeholders are pasted into the file before it loads. In double-quoted text, quotes inside a placeholder's value must be single quotes, as above, or the file fails to load.

### Layout with a Resource Pack {#layout-with-a-resource-pack}

Dialogs have no x/y positions. `<font:namespace:name><char.XXXX></font>` prints a resource pack font character by its hex code, such as `F801` or `1F600`. A `space` font's characters have a width but no image, and a negative width moves the next text left. Name a shift you reuse in `placeholders.yml`, such as `back2: '<font:mythic:space><char.F802></font>'`, then write `<placeholder.back2>`. [Placing Images](https://wiki.mythiccraft.io/mythicmobs/Dialogs#placing-images) shows a space font.

### Clickable Text {#clickable-text}

In body text, `<skill:SkillName>...</skill>` makes the text inside clickable. A click runs the skill like a [button skill](https://wiki.mythiccraft.io/mythicmobs/Dialogs#values-in-button-skills). Add `:key=value` pairs after the skill name to pass values as `dialog.<key>`:

```yaml
  Body:
  - Type: text
    Message: "<skill:OpenShop:shop=weapons><gold>[Weapons]</skill> <skill:OpenShop:shop=armor><gold>[Armor]</skill>"
```

In `OpenShop`, `<dialog.shop>` is `weapons` or `armor`.

- Elsewhere, such as in the `Title`, the tag shows as plain text.
- A text click sends no input values. Use a button for that.
- `AfterAction` applies to text clicks too. With `NONE`, the skill can change a value and reopen the dialog.
- Only the text and images inside the tag are clickable.
- Quote an argument that contains `:`, such as `<skill:Warp:'to=world:spawn'>`.
- An unknown skill logs an error and gives no click.
- Only [text inputs](https://wiki.mythiccraft.io/mythicmobs/Dialogs#input-values) escape tags. Keep other player-written text, such as chat, out of body text.

This toggle flips a saved variable. The tag passes the current value, and the skill's conditions pick the new one:

```yaml
ToggleMenu:
  AfterAction: NONE
  Body:
  - Type: text
    Message: "PvP <skill:TogglePvp:current=<target.var.pvp|false>><yellow>[<target.var.pvp|false>]</skill>"
  Buttons:
  - Label: "Done"
    Skills:
    - closeDialog
```

In the `Skills` folder:

```yaml
TogglePvp:
  Conditions:
  - stringEquals{v1=<dialog.current>;v2=true}
  Skills:
  - setvariable{var=target.pvp;type=STRING;value=false;save=true}
  - showDialog{dialog=ToggleMenu}
  FailedConditionsSkills:
  - setvariable{var=target.pvp;type=STRING;value=true;save=true}
  - showDialog{dialog=ToggleMenu}
```

## Drawing Menus with MythicCrucible {#drawing-menus-with-mythiccrucible}

[MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/home) turns PNG files into font images: characters that draw as pictures. Players need Crucible's generated resource pack. More options are in the [Crucible font docs](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/ResourcePack/ResourcePack-Generator#fonts).

### Setup {#setup}

1. Put the PNG under `assets/textures/` in a [pack](https://wiki.mythiccraft.io/mythicmobs/Packs), such as `plugins/MythicMobs/packs/MyUI/assets/textures/myui/panel.png`. Write `textures` and everything after it in lowercase, without spaces.
2. Create `font-images.yml` in the pack folder (Crucible does not create it):

   ```yaml
   panel:
     File: myui/panel
     Height: 143
     Ascent: 11
   ```

   - `File` (required): path under `assets/textures/`, without `.png`
   - `Height`: drawn height in pixels (default: the PNG height)
   - `Ascent`: moves the image up (default: half the `Height`). If above `Height`, all font images break
   - `Char`: the character that shows the image (default: picked by Crucible)

   Each image replaces its character everywhere, chat included. Crucible counts up from `Generation.FontImages.StartingCharacter` in `plugins/MythicMobs/config/config-generation.yml`, by default `"\u5001"` (Chinese). If players write Chinese or Japanese, set `"\uE000"`, which no language uses. Keep the double quotes, or images replace normal characters.
3. Write `<fontimage.panel>` (lowercase `fontimage`) in a dialog `Message`, outside any `<font>` tag. Image names must not contain dots. Start the `Message` with `<!shadow>` so images get no shadow.
4. Run `/mm reload`, then `/mm items generate`. Server starts also build the resource pack.
5. By default, Crucible uploads the resource pack to mcpacks.dev and sends it to players on join and after each build. This needs `Deployment.Enabled`, `AutoSend.Enabled` and `AutoSend.SendOnUpdate` set to `true` in `config-generation.yml`. To host it yourself, see [Self Hosting](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/ResourcePack/ResourcePack-Generator#self-hosting). `/mmc pack @a` sends it by hand.

### Clickable Images {#clickable-images}

`<skill:OpenShop><fontimage.shop></skill>` makes the whole image rectangle clickable, transparent pixels included. Where clickable images overlap, the later one in the `Message` gets the click. Images without a click do not block clicks.

### Images That Change {#images-that-change}

Placeholders in the image name are filled in first. With font images `toggle_true` and `toggle_false`, change the [ToggleMenu](https://wiki.mythiccraft.io/mythicmobs/Dialogs#clickable-text) `Message` to:

```yaml
    Message: "<!shadow>PvP <skill:TogglePvp:current=<target.var.pvp|false>><fontimage.toggle_<target.var.pvp|false>></skill>"
```

Make both images the same width so nothing moves. Static placeholders cannot do this: `<placeholder.toggle_<target.var.pvp|false>>` does not work.

### Placing Images {#placing-images}

A text element is a box `Width` pixels wide. Text wraps at `Width - 8`. Each line is centered on its own, so give every line the same total width. Lines are 9 px tall.

- **Up and down:** `Ascent: 7` puts the image's top on the line's top. Higher values move it up, lower values down, 1 px per step.
- **Left and right:** use a space font. Create `plugins/MythicCrucible/myui_space/assets/mythic/font/space.json`:

  ```json
  {
    "providers": [
      {"type": "space", "advances": {"\uf801": -1, "\uf802": -2, "\uf821": 1, "\uf822": 2}}
    ]
  }
  ```

  Add the folder to the existing `FromLocation` list in `config-generation.yml` (replace `[]` if empty), so Crucible copies it into the resource pack:

  ```yaml
  Generation:
    Import:
      FromLocation:
      - plugins/MythicCrucible/myui_space
  ```

  Then `<font:mythic:space><char.F801></font>` moves the next character 1 px left. Close `</font>` before the next image.
- An image takes its width times its scale (`Height` / PNG height), plus 1 px. Empty columns at the PNG's right edge do not count. A 20 px wide PNG at 2x takes 41 px. The first image of a line may be wider than `Width - 8`.

Character widths in the normal font, with the 1 px gap after each:

| Width | Characters |
| --- | --- |
| 2 | `! ' , . : ; i |` |
| 3 | `` ` `` `l` |
| 4 | space, `" ( ) * I [ ] t { }` |
| 5 | `< > f k` |
| 6 | all other ASCII letters, digits and symbols |
| 7 | `@ ~` |

### Background Panel {#background-panel}

A background image covers the whole text box when it is:

- alone on the first line (end that line with `<newline>`)
- exactly `Width` px wide, with an even `Width` of at most 256
- `9 x lines + 8` px tall, counting all lines of the element, its own included
- set to `Ascent: 11`, with square corners (no transparent corner pixels)

For `Width: 256` and 15 lines, the PNG is 256 x 143. It also hides the white outline that Minecraft 26.3 draws around a clicked text box. Other lines start 4 px from the edge when exactly `Width - 8` wide.

### Tips {#tips}

- A PNG can be at most 256 x 256 pixels, or it shows as an empty box. Use `Height` to draw it bigger.
- Make `Height` 1, 2 or 3 times the PNG height so pixels stay sharp. Scaling down loses pixels.
- Text whose width changes (names, numbers) moves its whole line. Keep it on its own line or in the `Title`.

## Mechanics, Conditions and Commands {#mechanics-conditions-and-commands}

- Mechanics: [showDialog](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ShowDialog) and [closeDialog](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CloseDialog). `closeDialog` also closes other plugins' dialogs.
- Condition: [hasDialogOpen](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/HasDialogOpen). It counts only MythicMobs dialogs.

| Command | Description | Permission |
| --- | --- | --- |
| `/mm dialogs list` (`l`) | Lists the loaded dialogs | `mythicmobs.command.dialogs.list` |
| `/mm dialogs show <dialog> [player] [key=value...]` (`s`, `open`) | Shows a dialog to the player, or to you. See [Passing Values](https://wiki.mythiccraft.io/mythicmobs/Dialogs#passing-values-between-dialogs) | `mythicmobs.command.dialogs.show` |

Players also need `mythicmobs.command.base` and `mythicmobs.command.dialogs`, or `mythicmobs.admin`. `/mm dialogs` also works as `/mm dialog` or `/mm dl`.

## Developer API {#developer-api}

Both events are in `io.lumine.mythic.bukkit.events` and have `getPlayer()` and `getDialog()` (the dialog name):

- `MythicDialogOpenEvent` fires before a dialog is sent. Cancel it to stop the dialog.
- `MythicDialogClickEvent` fires on a button or [clickable text](https://wiki.mythiccraft.io/mythicmobs/Dialogs#clickable-text) click. Cancel it to skip the skills, as if the click had none. `getButton()` is the `dialog.button` value, and `getValues()` a mutable map of the `dialog.<key>` values the skills get: input values, or clickable text arguments.

`open` shows a dialog from Java, with the map entries as `dialog.<key>` values. It returns `false` without Premium or for an unknown dialog:

```java
boolean opened = MythicBukkit.inst().getDialogManager().open(player, "DialogName", Map.of("key", "value"));
```

Custom mechanics, conditions, targeters and placeholders from the [API](https://wiki.mythiccraft.io/mythicmobs/API) also work in dialogs.
