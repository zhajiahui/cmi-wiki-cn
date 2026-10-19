# Commands { #commands }

<a id="contents"></a>

- <a id="id1"></a> [General Commands](https://worldedit.enginehub.org/en/latest/commands/#general-commands)

- <a id="id2"></a> [Navigation Commands](https://worldedit.enginehub.org/en/latest/commands/#navigation-commands)

- <a id="id3"></a> [Selection Commands](https://worldedit.enginehub.org/en/latest/commands/#selection-commands)

- <a id="id4"></a> [Region Commands](https://worldedit.enginehub.org/en/latest/commands/#region-commands)

- <a id="id5"></a> [Generation Commands](https://worldedit.enginehub.org/en/latest/commands/#generation-commands)

- <a id="id6"></a> [Schematic and Clipboard Commands](https://worldedit.enginehub.org/en/latest/commands/#schematic-and-clipboard-commands)

- <a id="id7"></a> [Tool Commands](https://worldedit.enginehub.org/en/latest/commands/#tool-commands)

- <a id="id8"></a> [Super Pickaxe Commands](https://worldedit.enginehub.org/en/latest/commands/#super-pickaxe-commands)

- <a id="id9"></a> [Brush Commands](https://worldedit.enginehub.org/en/latest/commands/#brush-commands)

- <a id="id10"></a> [Biome Commands](https://worldedit.enginehub.org/en/latest/commands/#biome-commands)

- <a id="id11"></a> [Chunk Commands](https://worldedit.enginehub.org/en/latest/commands/#chunk-commands)

- <a id="id12"></a> [Snapshot Commands](https://worldedit.enginehub.org/en/latest/commands/#snapshot-commands)

- <a id="id13"></a> [Scripting Commands](https://worldedit.enginehub.org/en/latest/commands/#scripting-commands)

- <a id="id14"></a> [Utility Commands](https://worldedit.enginehub.org/en/latest/commands/#utility-commands)

!!! note "Note"

    Arguments enclosed in `[ ]` are optional, those enclosed in `< >` are required.

!!! tip "Tip"

    You can access a command listing in-game via the `//help` command.

## [General Commands](https://worldedit.enginehub.org/en/latest/commands/#id1) { #general-commands }

<a id="command-/worldedit"></a>

`/worldedit` (or `/we`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">WorldEdit commands</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/worldedit <help|version|trace|reload|cui|tz|report>`</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-help"></a>

`/worldedit help`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Displays help for WorldEdit commands</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.help`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/worldedit help [-s] [-p <page>] [command...]`</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">List sub-commands of the given command, if applicable</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">The page to retrieve</td>
</tr>
<tr>
<td markdown="span">`[command...]`</td>
<td markdown="span">The command to retrieve help for</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-version"></a>

`/worldedit version` (or `/worldedit ver`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Get WorldEdit version</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/worldedit version`</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-trace"></a>

`/worldedit trace`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Toggles trace hook</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/worldedit trace [hookMode]`</td>
</tr>
<tr>
<td markdown="span">`[hookMode]`</td>
<td markdown="span">The mode to set the trace hook to</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-reload"></a>

`/worldedit reload`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Reload configuration</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.reload`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/worldedit reload`</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-cui"></a>

`/worldedit cui`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Complete CUI handshake (internal usage)</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/worldedit cui`</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-tz"></a>

`/worldedit tz`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set your timezone for snapshots</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/worldedit tz <timezone>`</td>
</tr>
<tr>
<td markdown="span">`<timezone>`</td>
<td markdown="span">The timezone to set</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-report"></a>

`/worldedit report`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Writes a report on WorldEdit</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.report`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/worldedit report [-p]`</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">Pastebins the report</td>
</tr>
</tbody>
</table>

<a id="command-/undo"></a>

`/undo` (or `//undo`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Undoes the last action (from history)</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.history.undo`, `worldedit.history.undo.self`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/undo [times] [player]`</td>
</tr>
<tr>
<td markdown="span">`[times]`</td>
<td markdown="span">Number of undoes to perform</td>
</tr>
<tr>
<td markdown="span">`[player]`</td>
<td markdown="span">Undo this player’s operations</td>
</tr>
</tbody>
</table>

<a id="command-/redo"></a>

`/redo` (or `//redo`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Redoes the last action (from history)</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.history.redo`, `worldedit.history.redo.self`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/redo [times] [player]`</td>
</tr>
<tr>
<td markdown="span">`[times]`</td>
<td markdown="span">Number of redoes to perform</td>
</tr>
<tr>
<td markdown="span">`[player]`</td>
<td markdown="span">Redo this player’s operations</td>
</tr>
</tbody>
</table>

<a id="command-/clearhistory"></a>

`/clearhistory` (or `//clearhistory`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Clear your history</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.history.clear`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/clearhistory`</td>
</tr>
</tbody>
</table>

<a id="command-//limit"></a>

`//limit`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Modify block change limit</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.limit`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//limit [limit]`</td>
</tr>
<tr>
<td markdown="span">`[limit]`</td>
<td markdown="span">The limit to set</td>
</tr>
</tbody>
</table>

<a id="command-//timeout"></a>

`//timeout`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Modify evaluation timeout time.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.timeout`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//timeout [limit]`</td>
</tr>
<tr>
<td markdown="span">`[limit]`</td>
<td markdown="span">The timeout time to set</td>
</tr>
</tbody>
</table>

<a id="command-//fast"></a>

`//fast`

!!! warning "Warning"

    This command is deprecated. //fast duplicates //perf and will be removed in WorldEdit 8.

    Please use `//perf` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Toggle fast mode</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.fast`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//fast [fastMode]`</td>
</tr>
<tr>
<td markdown="span">`[fastMode]`</td>
<td markdown="span">The new fast mode state</td>
</tr>
</tbody>
</table>

<a id="command-//perf"></a>

`//perf`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Toggle side effects for performance</p> <p markdown="span">Note that this command is GOING to change in the future. Do not depend on the exact format of this command yet.</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.perf`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//perf [-h] [sideEffect] [newState]`</td>
</tr>
<tr>
<td markdown="span">`[sideEffect]`</td>
<td markdown="span">The side effect</td>
</tr>
<tr>
<td markdown="span">`[newState]`</td>
<td markdown="span">The new side effect state</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Show the info box</td>
</tr>
</tbody>
</table>

<a id="command-//reorder"></a>

`//reorder`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Sets the reorder mode of WorldEdit</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.reorder`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//reorder [reorderMode]`</td>
</tr>
<tr>
<td markdown="span">`[reorderMode]`</td>
<td markdown="span">The reorder mode</td>
</tr>
</tbody>
</table>

<a id="command-//drawsel"></a>

`//drawsel`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Toggle drawing the current selection</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.drawsel`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//drawsel [drawSelection]`</td>
</tr>
<tr>
<td markdown="span">`[drawSelection]`</td>
<td markdown="span">The new draw selection state</td>
</tr>
</tbody>
</table>

<a id="command-//world"></a>

`//world`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Sets the world override</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.world`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//world [world]`</td>
</tr>
<tr>
<td markdown="span">`[world]`</td>
<td markdown="span">The world override</td>
</tr>
</tbody>
</table>

<a id="command-//watchdog"></a>

`//watchdog`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Changes watchdog hook state.</p> <p markdown="span">This is dependent on platform implementation. Not all platforms support watchdog hooks, or contain a watchdog.</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.watchdog`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//watchdog [hookMode]`</td>
</tr>
<tr>
<td markdown="span">`[hookMode]`</td>
<td markdown="span">The mode to set the watchdog hook to</td>
</tr>
</tbody>
</table>

<a id="command-/gmask"></a>

`/gmask` (or `//gmask`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set the global mask</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.global-mask`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/gmask [mask]`</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">The mask to set</td>
</tr>
</tbody>
</table>

<a id="command-/toggleplace"></a>

`/toggleplace` (or `//toggleplace`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Switch between your position and pos1 for placement</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/toggleplace`</td>
</tr>
</tbody>
</table>

<a id="command-/placement"></a>

`/placement` (or `//placement`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Select which placement to use</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.placement`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/placement <placementType> [multiplier] [offset]`</td>
</tr>
<tr>
<td markdown="span">`<placementType>`</td>
<td markdown="span">Which placement type to use</td>
</tr>
<tr>
<td markdown="span">`[multiplier]`</td>
<td markdown="span">number of times to apply the offset</td>
</tr>
<tr>
<td markdown="span">`[offset]`</td>
<td markdown="span">How much to offset from it placement to use</td>
</tr>
</tbody>
</table>

<a id="command-/searchitem"></a>

`/searchitem` (or `//searchitem`, `//l`, `//search`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Search for an item</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.searchitem`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/searchitem [-bi] [-p <page>] <query...>`</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Only search for blocks</td>
</tr>
<tr>
<td markdown="span">`[-i]`</td>
<td markdown="span">Only search for items</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">Page of results to return</td>
</tr>
<tr>
<td markdown="span">`<query...>`</td>
<td markdown="span">Search query</td>
</tr>
</tbody>
</table>

<a id="command-//registry"></a>

`//registry`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Search through the given registry</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.registry`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//registry <registry> [-p <page>] [queryBits...]`</td>
</tr>
<tr>
<td markdown="span">`<registry>`</td>
<td markdown="span">The registry to search through</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">Page of results to return</td>
</tr>
<tr>
<td markdown="span">`[queryBits...]`</td>
<td markdown="span">Search query</td>
</tr>
</tbody>
</table>

## [Navigation Commands](https://worldedit.enginehub.org/en/latest/commands/#id2) { #navigation-commands }

<a id="command-/unstuck"></a>

`/unstuck` (or `/!`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Escape from being stuck inside a block</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.navigation.unstuck`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/unstuck`</td>
</tr>
</tbody>
</table>

<a id="command-/ascend"></a>

`/ascend` (or `/asc`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Go up a floor</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.navigation.ascend`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/ascend [levels]`</td>
</tr>
<tr>
<td markdown="span">`[levels]`</td>
<td markdown="span"># of levels to ascend</td>
</tr>
</tbody>
</table>

<a id="command-/descend"></a>

`/descend` (or `/desc`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Go down a floor</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.navigation.descend`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/descend [levels]`</td>
</tr>
<tr>
<td markdown="span">`[levels]`</td>
<td markdown="span"># of levels to descend</td>
</tr>
</tbody>
</table>

<a id="command-/ceil"></a>

`/ceil`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Go to the ceiling</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.navigation.ceiling`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/ceil [-fg] [clearance]`</td>
</tr>
<tr>
<td markdown="span">`[clearance]`</td>
<td markdown="span"># of blocks to leave above you</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">Force using flight to keep you still</td>
</tr>
<tr>
<td markdown="span">`[-g]`</td>
<td markdown="span">Force using glass to keep you still</td>
</tr>
</tbody>
</table>

<a id="command-/thru"></a>

`/thru`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Pass through walls</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.navigation.thru.command`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/thru`</td>
</tr>
</tbody>
</table>

<a id="command-/jumpto"></a>

`/jumpto` (or `/j`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Teleport to a location</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.navigation.jumpto.command`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/jumpto`</td>
</tr>
</tbody>
</table>

<a id="command-/up"></a>

`/up`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Go upwards some distance</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.navigation.up`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/up [-fg] <distance>`</td>
</tr>
<tr>
<td markdown="span">`<distance>`</td>
<td markdown="span">Distance to go upwards</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">Force using flight to keep you still</td>
</tr>
<tr>
<td markdown="span">`[-g]`</td>
<td markdown="span">Force using glass to keep you still</td>
</tr>
</tbody>
</table>

## [Selection Commands](https://worldedit.enginehub.org/en/latest/commands/#id3) { #selection-commands }

<a id="command-//pos"></a>

`//pos`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set positions</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.pos`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//pos [pos1] [pos2...] [-s <selectorChoice>]`</td>
</tr>
<tr>
<td markdown="span">`[pos1]`</td>
<td markdown="span">Coordinates to set the primary position to. Defaults to the player position if not passed.</td>
</tr>
<tr>
<td markdown="span">`[pos2...]`</td>
<td markdown="span">Coordinates to add as secondary positions. Defaults to the player position if not passed.</td>
</tr>
<tr>
<td markdown="span">`[-s <selectorChoice>]`</td>
<td markdown="span">Selector to switch to</td>
</tr>
</tbody>
</table>

<a id="command-//pos1"></a>

`//pos1`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set position 1</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.pos`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//pos1 [coordinates]`</td>
</tr>
<tr>
<td markdown="span">`[coordinates]`</td>
<td markdown="span">Coordinates to set position 1 to</td>
</tr>
</tbody>
</table>

<a id="command-//pos2"></a>

`//pos2`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set position 2</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.pos`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//pos2 [coordinates]`</td>
</tr>
<tr>
<td markdown="span">`[coordinates]`</td>
<td markdown="span">Coordinates to set position 2 to</td>
</tr>
</tbody>
</table>

<a id="command-//hpos1"></a>

`//hpos1`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set position 1 to targeted block</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.hpos`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//hpos1`</td>
</tr>
</tbody>
</table>

<a id="command-//hpos2"></a>

`//hpos2`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set position 2 to targeted block</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.hpos`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//hpos2`</td>
</tr>
</tbody>
</table>

<a id="command-//chunk"></a>

`//chunk`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Set the selection to your current chunk.</p> <p markdown="span">This command selects 256-block-tall areas, which can be specified by the y-coordinate. E.g. -c x,1,z will select from y=256 to y=511.</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.chunk`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//chunk [-cs] [coordinates]`</td>
</tr>
<tr>
<td markdown="span">`[coordinates]`</td>
<td markdown="span">The chunk to select</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">Expand your selection to encompass all chunks that are part of it</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">Use chunk coordinates instead of block coordinates</td>
</tr>
</tbody>
</table>

<a id="command-//wand"></a>

`//wand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Get the wand item</p> <p markdown="span">You must have also have permission to use at least one of the features of the requested wand.</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.wand`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//wand [-n]`</td>
</tr>
<tr>
<td markdown="span">`[-n]`</td>
<td markdown="span">Get a navigation wand</td>
</tr>
</tbody>
</table>

<a id="command-/toggleeditwand"></a>

`/toggleeditwand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Remind the user that the wand is now a tool and can be unbound with /tool none.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.wand.toggle`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/toggleeditwand`</td>
</tr>
</tbody>
</table>

<a id="command-//contract"></a>

`//contract`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Contract the selection area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.contract`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//contract <amount> [reverseAmount] [direction]`</td>
</tr>
<tr>
<td markdown="span">`<amount>`</td>
<td markdown="span">Amount to contract the selection by</td>
</tr>
<tr>
<td markdown="span">`[reverseAmount]`</td>
<td markdown="span">Amount to contract the selection by in the other direction</td>
</tr>
<tr>
<td markdown="span">`[direction]`</td>
<td markdown="span">Direction to contract</td>
</tr>
</tbody>
</table>

<a id="command-//shift"></a>

`//shift`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Shift the selection area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.shift`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//shift <amount> [direction]`</td>
</tr>
<tr>
<td markdown="span">`<amount>`</td>
<td markdown="span">Amount to shift the selection by</td>
</tr>
<tr>
<td markdown="span">`[direction]`</td>
<td markdown="span">Direction to contract</td>
</tr>
</tbody>
</table>

<a id="command-//outset"></a>

`//outset`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Outset the selection area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.outset`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//outset [-hv] <amount>`</td>
</tr>
<tr>
<td markdown="span">`<amount>`</td>
<td markdown="span">Amount to expand the selection by in all directions</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Only expand horizontally</td>
</tr>
<tr>
<td markdown="span">`[-v]`</td>
<td markdown="span">Only expand vertically</td>
</tr>
</tbody>
</table>

<a id="command-//inset"></a>

`//inset`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Inset the selection area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.inset`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//inset [-hv] <amount>`</td>
</tr>
<tr>
<td markdown="span">`<amount>`</td>
<td markdown="span">Amount to contract the selection by in all directions</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Only contract horizontally</td>
</tr>
<tr>
<td markdown="span">`[-v]`</td>
<td markdown="span">Only contract vertically</td>
</tr>
</tbody>
</table>

<a id="command-//trim"></a>

`//trim`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Minimize the selection to encompass matching blocks</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.trim`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//trim [mask]`</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">Mask of blocks to keep within the selection</td>
</tr>
</tbody>
</table>

<a id="command-//size"></a>

`//size`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Get information about the selection</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.size`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//size [-c]`</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">Get clipboard info instead</td>
</tr>
</tbody>
</table>

<a id="command-//count"></a>

`//count`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Counts the number of blocks matching a mask</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.analysis.count`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//count <mask>`</td>
</tr>
<tr>
<td markdown="span">`<mask>`</td>
<td markdown="span">The mask of blocks to match</td>
</tr>
</tbody>
</table>

<a id="command-//distr"></a>

`//distr`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Get the distribution of blocks in the selection</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.analysis.distr`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//distr [-cd] [-p <page>] [-m <sourceMask>]`</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">Get the distribution of the clipboard instead</td>
</tr>
<tr>
<td markdown="span">`[-d]`</td>
<td markdown="span">Separate blocks by state</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">Gets page from a previous distribution.</td>
</tr>
<tr>
<td markdown="span">`[-m <sourceMask>]`</td>
<td markdown="span">Only include blocks matching the given mask</td>
</tr>
</tbody>
</table>

<a id="command-//sel"></a>

`//sel` (or `/;`, `//desel`, `//deselect`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Choose a region selector</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//sel [-d] [selectorChoiceOrList]`</td>
</tr>
<tr>
<td markdown="span">`[selectorChoiceOrList]`</td>
<td markdown="span">Selector to switch to</td>
</tr>
<tr>
<td markdown="span">`[-d]`</td>
<td markdown="span">Set default selector</td>
</tr>
</tbody>
</table>

<a id="command-//expand"></a>

`//expand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Expand the selection area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.selection.expand`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//expand <vert|<amount> [reverseAmount] [direction]>`</td>
</tr>
<tr>
<td markdown="span">`<amount>`</td>
<td markdown="span">Amount to expand the selection by, can be vert to expand to the whole vertical column</td>
</tr>
<tr>
<td markdown="span">`[reverseAmount]`</td>
<td markdown="span">Amount to expand the selection by in the other direction</td>
</tr>
<tr>
<td markdown="span">`[direction]`</td>
<td markdown="span">Direction to expand</td>
</tr>
</tbody>
</table>

<a id="command-//expand-vert"></a>

`//expand vert`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Vertically expand the selection to world limits.</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//expand vert`</td>
</tr>
</tbody>
</table>

## [Region Commands](https://worldedit.enginehub.org/en/latest/commands/#id4) { #region-commands }

<a id="command-//set"></a>

`//set`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Sets all the blocks in the region</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.set`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//set <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
</tbody>
</table>

<a id="command-//line"></a>

`//line`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Draws line segments between cuboid selection corners or convex polyhedral selection vertices</p> <p markdown="span">Can only be used with a cuboid selection or a convex polyhedral selection</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.line`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//line [-h] <pattern> [thickness]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to place</td>
</tr>
<tr>
<td markdown="span">`[thickness]`</td>
<td markdown="span">The thickness of the line</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Generate only a shell</td>
</tr>
</tbody>
</table>

<a id="command-//curve"></a>

`//curve`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Draws a spline through selected points</p> <p markdown="span">Can only be used with a convex polyhedral selection</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.curve`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//curve [-h] <pattern> [thickness]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to place</td>
</tr>
<tr>
<td markdown="span">`[thickness]`</td>
<td markdown="span">The thickness of the curve</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Generate only a shell</td>
</tr>
</tbody>
</table>

<a id="command-//replace"></a>

`//replace` (or `//re`, `//rep`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Replace all blocks in the selection with another</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.replace`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//replace [from] <to>`</td>
</tr>
<tr>
<td markdown="span">`[from]`</td>
<td markdown="span">The mask representing blocks to replace</td>
</tr>
<tr>
<td markdown="span">`<to>`</td>
<td markdown="span">The pattern of blocks to replace with</td>
</tr>
</tbody>
</table>

<a id="command-//overlay"></a>

`//overlay`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set a block on top of blocks in the region</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.overlay`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//overlay <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to overlay</td>
</tr>
</tbody>
</table>

<a id="command-//center"></a>

`//center` (or `//middle`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set the center block(s)</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.center`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//center <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
</tbody>
</table>

<a id="command-//naturalize"></a>

`//naturalize`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">3 layers of dirt on top then rock below</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.naturalize`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//naturalize`</td>
</tr>
</tbody>
</table>

<a id="command-//walls"></a>

`//walls`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Build the four sides of the selection</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.walls`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//walls <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
</tbody>
</table>

<a id="command-//faces"></a>

`//faces` (or `//outline`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Build the walls, ceiling, and floor of a selection</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.faces`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//faces <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
</tbody>
</table>

<a id="command-//smooth"></a>

`//smooth`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Smooth the elevation in the selection</p> <p markdown="span">Example: ‘//smooth 1 grass_block,dirt,stone’ would only smooth natural surface terrain.</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.smooth`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//smooth [iterations] [mask]`</td>
</tr>
<tr>
<td markdown="span">`[iterations]`</td>
<td markdown="span"># of iterations to perform</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">The mask of blocks to use as the height map</td>
</tr>
</tbody>
</table>

<a id="command-//snowsmooth"></a>

`//snowsmooth`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Smooth the elevation in the selection with snow layers</p> <p markdown="span">Example: ‘//snowsmooth 1 -m snow_block,snow’ would only smooth snow terrain.</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.snowsmooth`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//snowsmooth [iterations] [-l <snowBlockCount>] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[iterations]`</td>
<td markdown="span"># of iterations to perform</td>
</tr>
<tr>
<td markdown="span">`[-l <snowBlockCount>]`</td>
<td markdown="span">Set the amount of snow blocks under the snow</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">The mask of blocks to use as the height map</td>
</tr>
</tbody>
</table>

<a id="command-//move"></a>

`//move`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Move the contents of the selection</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.move`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//move [-abes] [multiplier] [offset] [replace] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[multiplier]`</td>
<td markdown="span">number of times to apply the offset</td>
</tr>
<tr>
<td markdown="span">`[offset]`</td>
<td markdown="span">The offset to move</td>
</tr>
<tr>
<td markdown="span">`[replace]`</td>
<td markdown="span">The pattern of blocks to leave</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">Shift the selection to the target location</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">Ignore air blocks</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">Also copy entities</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Also copy biomes</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">Set the include mask, non-matching blocks become air</td>
</tr>
</tbody>
</table>

<a id="command-//stack"></a>

`//stack`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Repeat the contents of the selection</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.stack`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//stack [-abers] [count] [offset] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[count]`</td>
<td markdown="span"># of copies to stack</td>
</tr>
<tr>
<td markdown="span">`[offset]`</td>
<td markdown="span">How far to move the contents each stack</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">Shift the selection to the last stacked copy</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">Ignore air blocks</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">Also copy entities</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Also copy biomes</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Use block units</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">Set the include mask, non-matching blocks become air</td>
</tr>
</tbody>
</table>

<a id="command-//regen"></a>

`//regen`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Regenerates the contents of the selection</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.regen`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//regen [-bc] [seed]`</td>
</tr>
<tr>
<td markdown="span">`[seed]`</td>
<td markdown="span">The seed to regenerate with, otherwise uses world seed</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Regenerate biomes as well</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">Regenerate to the clipboard</td>
</tr>
</tbody>
</table>

<a id="command-//deform"></a>

`//deform`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Deforms a selected region with an expression</p> <p markdown="span">The expression is executed for each block and is expected to modify the variables x, y and z to point to a new block to fetch. For details, see [https://ehub.to/we/expr](https://ehub.to/we/expr)</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.deform`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//deform [-clor] <expression...>`</td>
</tr>
<tr>
<td markdown="span">`<expression...>`</td>
<td markdown="span">The expression to use</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Use the game’s coordinate origin</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">Use the placement’s coordinate origin</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">Use the selection’s center as origin</td>
</tr>
<tr>
<td markdown="span">`[-l]`</td>
<td markdown="span">Fetch from the clipboard instead of the world</td>
</tr>
</tbody>
</table>

<a id="command-//hollow"></a>

`//hollow`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Hollows out the object contained in this selection</p> <p markdown="span">Thickness is measured in manhattan distance.</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.hollow`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//hollow [thickness] [pattern]`</td>
</tr>
<tr>
<td markdown="span">`[thickness]`</td>
<td markdown="span">Thickness of the shell to leave</td>
</tr>
<tr>
<td markdown="span">`[pattern]`</td>
<td markdown="span">The pattern of blocks to replace the hollowed area with</td>
</tr>
</tbody>
</table>

<a id="command-//forest"></a>

`//forest`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Make a forest within the region</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.forest`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//forest [type] [density]`</td>
</tr>
<tr>
<td markdown="span">`[type]`</td>
<td markdown="span">The type of tree to place</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">The density of the forest</td>
</tr>
</tbody>
</table>

<a id="command-//flora"></a>

`//flora`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Make flora within the region</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.region.flora`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//flora [density]`</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">The density of the forest</td>
</tr>
</tbody>
</table>

<a id="command-//update"></a>

`//update`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Apply side effects to your selection</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.update`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//update [sideEffectSet]`</td>
</tr>
<tr>
<td markdown="span">`[sideEffectSet]`</td>
<td markdown="span">The side effects</td>
</tr>
</tbody>
</table>

## [Generation Commands](https://worldedit.enginehub.org/en/latest/commands/#id5) { #generation-commands }

<a id="command-//hcyl"></a>

`//hcyl`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generates a hollow cylinder.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.cylinder`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//hcyl <pattern> <radii> [height]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to generate</td>
</tr>
<tr>
<td markdown="span">`<radii>`</td>
<td markdown="span">The radii of the cylinder. 1st is N/S, 2nd is E/W</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">The height of the cylinder</td>
</tr>
</tbody>
</table>

<a id="command-//cyl"></a>

`//cyl`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generates a cylinder.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.cylinder`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//cyl [-h] <pattern> <radii> [height]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to generate</td>
</tr>
<tr>
<td markdown="span">`<radii>`</td>
<td markdown="span">The radii of the cylinder. 1st is N/S, 2nd is E/W</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">The height of the cylinder</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Make a hollow cylinder</td>
</tr>
</tbody>
</table>

<a id="command-//cone"></a>

`//cone`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generates a cone.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.cone`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//cone [-h] <pattern> <radii> [height] [thickness]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to generate</td>
</tr>
<tr>
<td markdown="span">`<radii>`</td>
<td markdown="span">The radii of the cone. 1st is N/S, 2nd is E/W</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">The height of the cone</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Make a hollow cone</td>
</tr>
<tr>
<td markdown="span">`[thickness]`</td>
<td markdown="span">Thickness of the hollow cone</td>
</tr>
</tbody>
</table>

<a id="command-//hsphere"></a>

`//hsphere`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generates a hollow sphere.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.sphere`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//hsphere [-r] <pattern> <radii>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to generate</td>
</tr>
<tr>
<td markdown="span">`<radii>`</td>
<td markdown="span">The radii of the sphere. Order is N/S, U/D, E/W</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Raise the bottom of the sphere to the placement position</td>
</tr>
</tbody>
</table>

<a id="command-//sphere"></a>

`//sphere`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generates a filled sphere.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.sphere`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//sphere [-hr] <pattern> <radii>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to generate</td>
</tr>
<tr>
<td markdown="span">`<radii>`</td>
<td markdown="span">The radii of the sphere. Order is N/S, U/D, E/W</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Raise the bottom of the sphere to the placement position</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Make a hollow sphere</td>
</tr>
</tbody>
</table>

<a id="command-/forestgen"></a>

`/forestgen`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generate a forest</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.forest`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/forestgen [size] [type] [density]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">The size of the forest, in blocks</td>
</tr>
<tr>
<td markdown="span">`[type]`</td>
<td markdown="span">The type of forest</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">The density of the forest, between 0 and 100</td>
</tr>
</tbody>
</table>

<a id="command-/pumpkins"></a>

`/pumpkins`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generate pumpkin patches</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.pumpkins`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/pumpkins [size]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">The size of the patch</td>
</tr>
</tbody>
</table>

<a id="command-//feature"></a>

`//feature`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generate Minecraft features</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.feature`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//feature <feature>`</td>
</tr>
<tr>
<td markdown="span">`<feature>`</td>
<td markdown="span">The feature</td>
</tr>
</tbody>
</table>

<a id="command-//structure"></a>

`//structure`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generate Minecraft structures</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.structure`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//structure <feature>`</td>
</tr>
<tr>
<td markdown="span">`<feature>`</td>
<td markdown="span">The structure</td>
</tr>
</tbody>
</table>

<a id="command-//hpyramid"></a>

`//hpyramid`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generate a hollow pyramid</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.pyramid`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//hpyramid <pattern> <size>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
<tr>
<td markdown="span">`<size>`</td>
<td markdown="span">The size of the pyramid</td>
</tr>
</tbody>
</table>

<a id="command-//pyramid"></a>

`//pyramid`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Generate a filled pyramid</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.pyramid`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//pyramid [-h] <pattern> <size>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
<tr>
<td markdown="span">`<size>`</td>
<td markdown="span">The size of the pyramid</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Make a hollow pyramid</td>
</tr>
</tbody>
</table>

<a id="command-//generate"></a>

`//generate` (or `//gen`, `//g`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Generates a shape according to a formula.</p> <p markdown="span">For details, see [https://ehub.to/we/expr](https://ehub.to/we/expr)</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.shape`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//generate [-chor] <pattern> <expression...>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
<tr>
<td markdown="span">`<expression...>`</td>
<td markdown="span">Expression to test block placement locations and set block type</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Generate a hollow shape</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Use the game’s coordinate origin</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">Use the placement’s coordinate origin</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">Use the selection’s center as origin</td>
</tr>
</tbody>
</table>

<a id="command-//generatebiome"></a>

`//generatebiome` (or `//genbiome`, `//gb`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Sets biome according to a formula.</p> <p markdown="span">For details, see [https://ehub.to/we/expr](https://ehub.to/we/expr)</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.generation.shape.biome`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//generatebiome [-chor] <target> <expression...>`</td>
</tr>
<tr>
<td markdown="span">`<target>`</td>
<td markdown="span">The biome type to set</td>
</tr>
<tr>
<td markdown="span">`<expression...>`</td>
<td markdown="span">Expression to test block placement locations and set biome type</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Generate a hollow shape</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Use the game’s coordinate origin</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">Use the placement’s coordinate origin</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">Use the selection’s center as origin</td>
</tr>
</tbody>
</table>

## [Schematic and Clipboard Commands](https://worldedit.enginehub.org/en/latest/commands/#id6) { #schematic-and-clipboard-commands }

<a id="command-/schematic"></a>

`/schematic` (or `/schem`, `//schematic`, `//schem`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Schematic commands for saving/loading areas</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.schematic.delete`, `worldedit.schematic.list`, `worldedit.clipboard.load`, `worldedit.schematic.save`, `worldedit.schematic.formats`, `worldedit.schematic.load`, `worldedit.clipboard.save`, `worldedit.clipboard.share`, `worldedit.schematic.share`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/schematic <list|formats|load|delete|save|share>`</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-list"></a>

`/schematic list` (or `/schematic all`, `/schematic ls`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">List saved schematics</p> <p markdown="span">Note: Format is not fully verified until loading.</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.schematic.list`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/schematic list [-dn] [-p <page>]`</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">Page to view.</td>
</tr>
<tr>
<td markdown="span">`[-d]`</td>
<td markdown="span">Sort by date, oldest first</td>
</tr>
<tr>
<td markdown="span">`[-n]`</td>
<td markdown="span">Sort by date, newest first</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-formats"></a>

`/schematic formats` (or `/schematic listformats`, `/schematic f`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">List available formats</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.schematic.formats`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/schematic formats`</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-load"></a>

`/schematic load`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Load a schematic into your clipboard</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.clipboard.load`, `worldedit.schematic.load`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/schematic load <schematic> [format]`</td>
</tr>
<tr>
<td markdown="span">`<schematic>`</td>
<td markdown="span">File name.</td>
</tr>
<tr>
<td markdown="span">`[format]`</td>
<td markdown="span">Format name.</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-delete"></a>

`/schematic delete` (or `/schematic d`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Delete a saved schematic</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.schematic.delete`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/schematic delete <schematic>`</td>
</tr>
<tr>
<td markdown="span">`<schematic>`</td>
<td markdown="span">File name.</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-save"></a>

`/schematic save`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Save your clipboard into a schematic file</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.clipboard.save`, `worldedit.schematic.save`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/schematic save [-f] <filename> [format]`</td>
</tr>
<tr>
<td markdown="span">`<filename>`</td>
<td markdown="span">File name.</td>
</tr>
<tr>
<td markdown="span">`[format]`</td>
<td markdown="span">Format name.</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">Overwrite an existing file.</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-share"></a>

`/schematic share`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Share your clipboard as a schematic online</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.clipboard.share`, `worldedit.schematic.share`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/schematic share [schematicName] [destination] [format]`</td>
</tr>
<tr>
<td markdown="span">`[schematicName]`</td>
<td markdown="span">Schematic name. Defaults to name-millis</td>
</tr>
<tr>
<td markdown="span">`[destination]`</td>
<td markdown="span">Share location</td>
</tr>
<tr>
<td markdown="span">`[format]`</td>
<td markdown="span">Format name</td>
</tr>
</tbody>
</table>

<a id="command-//copy"></a>

`//copy`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Copy the selection to the clipboard</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.clipboard.copy`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//copy [-be] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">Also copy entities</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Also copy biomes</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">Set the include mask, non-matching blocks become air</td>
</tr>
</tbody>
</table>

<a id="command-//cut"></a>

`//cut`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Cut the selection to the clipboard</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.clipboard.cut`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//cut [-be] [leavePattern] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[leavePattern]`</td>
<td markdown="span">Pattern to leave in place of the selection</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">Also cut entities</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Also copy biomes, source biomes are unaffected</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">Set the exclude mask, non-matching blocks become air</td>
</tr>
</tbody>
</table>

<a id="command-//paste"></a>

`//paste`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Paste the clipboard’s contents</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.clipboard.paste`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//paste [-abenosv] [-m <sourceMask>]`</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">Skip air blocks</td>
</tr>
<tr>
<td markdown="span">`[-v]`</td>
<td markdown="span">Include structure void blocks</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">Paste at the original position</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">Select the region after pasting</td>
</tr>
<tr>
<td markdown="span">`[-n]`</td>
<td markdown="span">No paste, select only. (Implies -s)</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">Paste entities if available</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Paste biomes if available</td>
</tr>
<tr>
<td markdown="span">`[-m <sourceMask>]`</td>
<td markdown="span">Only paste blocks matching this mask</td>
</tr>
</tbody>
</table>

<a id="command-//rotate"></a>

`//rotate`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Rotate the contents of the clipboard</p> <p markdown="span">Non-destructively rotate the contents of the clipboard. Angles are provided in degrees and a positive angle will result in a clockwise rotation. Multiple rotations can be stacked. Interpolation is not performed so angles should be a multiple of 90 degrees.</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.clipboard.rotate`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//rotate <rotateY> [rotateX] [rotateZ]`</td>
</tr>
<tr>
<td markdown="span">`<rotateY>`</td>
<td markdown="span">Amount to rotate on the y-axis</td>
</tr>
<tr>
<td markdown="span">`[rotateX]`</td>
<td markdown="span">Amount to rotate on the x-axis</td>
</tr>
<tr>
<td markdown="span">`[rotateZ]`</td>
<td markdown="span">Amount to rotate on the z-axis</td>
</tr>
</tbody>
</table>

<a id="command-//flip"></a>

`//flip` (or `//mirror`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Flip the contents of the clipboard across the origin</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.clipboard.flip`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//flip [direction]`</td>
</tr>
<tr>
<td markdown="span">`[direction]`</td>
<td markdown="span">The direction to flip, defaults to look direction.</td>
</tr>
</tbody>
</table>

<a id="command-/clearclipboard"></a>

`/clearclipboard`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Clear your clipboard</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.clipboard.clear`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/clearclipboard`</td>
</tr>
</tbody>
</table>

<a id="command-//revolve"></a>

`//revolve`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Revolve the selection around a vertical axis</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.revolve`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//revolve [-ber] <pasteCount> [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`<pasteCount>`</td>
<td markdown="span">The number of pastes</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">Set the source mask, non-matching blocks are not revolved</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Perform revolutions in reverse (counter-clockwise)</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">Copy entities</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Copy biomes</td>
</tr>
</tbody>
</table>

## [Tool Commands](https://worldedit.enginehub.org/en/latest/commands/#id7) { #tool-commands }

<a id="command-/tool"></a>

`/tool`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Binds a tool to the item in your hand</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool <cycler|repl|farwand|floodfill|deltree|stacker|selwand|tree|none|info|lrbuild|navwand>`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-cycler"></a>

`/tool cycler`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Block data cycler tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.data-cycler`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool cycler`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-repl"></a>

`/tool repl`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Block replacer tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.replacer`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool repl <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to place</td>
</tr>
</tbody>
</table>

<a id="command-/tool-farwand"></a>

`/tool farwand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Wand at a distance tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.farwand`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool farwand`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-floodfill"></a>

`/tool floodfill` (or `/tool flood`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Flood fill tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.flood-fill`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool floodfill <pattern> <range>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern to flood fill</td>
</tr>
<tr>
<td markdown="span">`<range>`</td>
<td markdown="span">The range to perform the fill</td>
</tr>
</tbody>
</table>

<a id="command-/tool-deltree"></a>

`/tool deltree`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Floating tree remover tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.deltree`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool deltree`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-stacker"></a>

`/tool stacker`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Block stacker tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.stack`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool stacker [range] [mask]`</td>
</tr>
<tr>
<td markdown="span">`[range]`</td>
<td markdown="span">The max range of the stack</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">The mask to stack until</td>
</tr>
</tbody>
</table>

<a id="command-/tool-selwand"></a>

`/tool selwand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Selection wand tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool selwand`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-tree"></a>

`/tool tree`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Tree generator tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.tree`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool tree [type]`</td>
</tr>
<tr>
<td markdown="span">`[type]`</td>
<td markdown="span">Type of tree to generate</td>
</tr>
</tbody>
</table>

<a id="command-/tool-none"></a>

`/tool none` (or `/tool unbind`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Unbind a bound tool from your current item</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool none`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-info"></a>

`/tool info`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Block information tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.info`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool info`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-lrbuild"></a>

`/tool lrbuild`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Long-range building tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.lrbuild`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool lrbuild <primary> <secondary>`</td>
</tr>
<tr>
<td markdown="span">`<primary>`</td>
<td markdown="span">Pattern to set on left-click</td>
</tr>
<tr>
<td markdown="span">`<secondary>`</td>
<td markdown="span">Pattern to set on right-click</td>
</tr>
</tbody>
</table>

<a id="command-/tool-navwand"></a>

`/tool navwand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Navigation wand tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tool navwand`</td>
</tr>
</tbody>
</table>

<a id="command-/none"></a>

`/none`

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool none` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Unbind a bound tool from your current item</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/none`</td>
</tr>
</tbody>
</table>

<a id="command-/selwand"></a>

`/selwand` (or `//selwand`)

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool selwand` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Selection wand tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/selwand`</td>
</tr>
</tbody>
</table>

<a id="command-/navwand"></a>

`/navwand` (or `//navwand`)

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool navwand` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Navigation wand tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/navwand`</td>
</tr>
</tbody>
</table>

<a id="command-/info"></a>

`/info`

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool info` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Block information tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.info`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/info`</td>
</tr>
</tbody>
</table>

<a id="command-/tree"></a>

`/tree`

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool tree` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Tree generator tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.tree`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tree [type]`</td>
</tr>
<tr>
<td markdown="span">`[type]`</td>
<td markdown="span">Type of tree to generate</td>
</tr>
</tbody>
</table>

<a id="command-/repl"></a>

`/repl`

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool repl` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Block replacer tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.replacer`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/repl <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to place</td>
</tr>
</tbody>
</table>

<a id="command-/cycler"></a>

`/cycler`

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool cycler` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Block data cycler tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.data-cycler`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/cycler`</td>
</tr>
</tbody>
</table>

<a id="command-/floodfill"></a>

`/floodfill` (or `/flood`)

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool floodfill` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Flood fill tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.flood-fill`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/floodfill <pattern> <range>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern to flood fill</td>
</tr>
<tr>
<td markdown="span">`<range>`</td>
<td markdown="span">The range to perform the fill</td>
</tr>
</tbody>
</table>

<a id="command-/deltree"></a>

`/deltree`

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool deltree` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Floating tree remover tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.deltree`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/deltree`</td>
</tr>
</tbody>
</table>

<a id="command-/farwand"></a>

`/farwand`

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool farwand` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Wand at a distance tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.farwand`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/farwand`</td>
</tr>
</tbody>
</table>

<a id="command-/lrbuild"></a>

`/lrbuild` (or `//lrbuild`)

!!! warning "Warning"

    This command is deprecated. Global tool names cause conflicts and will be removed in WorldEdit 8.

    Please use `/tool lrbuild` instead.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Long-range building tool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.tool.lrbuild`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/lrbuild <primary> <secondary>`</td>
</tr>
<tr>
<td markdown="span">`<primary>`</td>
<td markdown="span">Pattern to set on left-click</td>
</tr>
<tr>
<td markdown="span">`<secondary>`</td>
<td markdown="span">Pattern to set on right-click</td>
</tr>
</tbody>
</table>

<a id="command-//"></a>

`//` (or `/,`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Toggle the super pickaxe function</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.superpickaxe`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`// [superPickaxe]`</td>
</tr>
<tr>
<td markdown="span">`[superPickaxe]`</td>
<td markdown="span">The new super pickaxe state</td>
</tr>
</tbody>
</table>

<a id="command-/mask"></a>

`/mask`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set the brush mask</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.options.mask`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/mask [mask]`</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">The mask to set</td>
</tr>
</tbody>
</table>

<a id="command-/material"></a>

`/material` (or `//material`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set the brush material</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.options.material`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/material <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to use</td>
</tr>
</tbody>
</table>

<a id="command-/range"></a>

`/range`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set the brush range</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.options.range`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/range <range>`</td>
</tr>
<tr>
<td markdown="span">`<range>`</td>
<td markdown="span">The range of the brush</td>
</tr>
</tbody>
</table>

<a id="command-/size"></a>

`/size`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set the brush size</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.options.size`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/size <size>`</td>
</tr>
<tr>
<td markdown="span">`<size>`</td>
<td markdown="span">The size of the brush</td>
</tr>
</tbody>
</table>

<a id="command-/tracemask"></a>

`/tracemask`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set the mask used to stop tool traces</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.options.tracemask`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/tracemask [mask]`</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">The trace mask to set</td>
</tr>
</tbody>
</table>

## [Super Pickaxe Commands](https://worldedit.enginehub.org/en/latest/commands/#id8) { #super-pickaxe-commands }

<a id="command-/superpickaxe"></a>

`/superpickaxe` (or `/pickaxe`, `/sp`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Super-pickaxe commands</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.superpickaxe.area`, `worldedit.superpickaxe.recursive`, `worldedit.superpickaxe`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/superpickaxe <single|area|recursive>`</td>
</tr>
</tbody>
</table>

<a id="command-/superpickaxe-single"></a>

`/superpickaxe single`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Enable the single block super pickaxe mode</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.superpickaxe`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/superpickaxe single`</td>
</tr>
</tbody>
</table>

<a id="command-/superpickaxe-area"></a>

`/superpickaxe area`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Enable the area super pickaxe pickaxe mode</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.superpickaxe.area`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/superpickaxe area <range>`</td>
</tr>
<tr>
<td markdown="span">`<range>`</td>
<td markdown="span">The range of the area pickaxe</td>
</tr>
</tbody>
</table>

<a id="command-/superpickaxe-recursive"></a>

`/superpickaxe recursive` (or `/superpickaxe recur`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Enable the recursive super pickaxe pickaxe mode</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.superpickaxe.recursive`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/superpickaxe recursive <range>`</td>
</tr>
<tr>
<td markdown="span">`<range>`</td>
<td markdown="span">The range of the recursive pickaxe</td>
</tr>
</tbody>
</table>

## [Brush Commands](https://worldedit.enginehub.org/en/latest/commands/#id9) { #brush-commands }

<a id="command-/brush"></a>

`/brush` (or `/br`, `//brush`, `//br`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Brushing commands</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush <forest|splatter|butcher|paint|none|clipboard|snowsmooth|gravity|heightmap|extinguish|feature|sphere|raise|smooth|cylinder|set|apply|deform|lower|erode|dilate|snow|biome|morph>`</td>
</tr>
</tbody>
</table>

<a id="command-/brush-forest"></a>

`/brush forest`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Forest brush, creates a forest in the area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.forest`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush forest <shape> [radius] [density] <type>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">The shape of the region</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">The density of the brush</td>
</tr>
<tr>
<td markdown="span">`<type>`</td>
<td markdown="span">The type of tree to use</td>
</tr>
</tbody>
</table>

<a id="command-/brush-splatter"></a>

`/brush splatter` (or `/brush splat`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Choose the splatter brush</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.splatter`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush splatter <pattern> [radius] [decay]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The radius of the splatter</td>
</tr>
<tr>
<td markdown="span">`[decay]`</td>
<td markdown="span">The decay of the splatter between 0 and 10</td>
</tr>
</tbody>
</table>

<a id="command-/brush-butcher"></a>

`/brush butcher` (or `/brush kill`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Butcher brush, kills mobs within a radius</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.butcher`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush butcher [-abfgnprtw] [radius]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">Radius to kill mobs in</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">Also kill pets</td>
</tr>
<tr>
<td markdown="span">`[-n]`</td>
<td markdown="span">Also kill NPCs</td>
</tr>
<tr>
<td markdown="span">`[-g]`</td>
<td markdown="span">Also kill golems</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">Also kill animals</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Also kill ambient mobs</td>
</tr>
<tr>
<td markdown="span">`[-t]`</td>
<td markdown="span">Also kill mobs with name tags</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">Also kill all friendly mobs (Applies the flags -abgnpt)</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Also destroy armor stands</td>
</tr>
<tr>
<td markdown="span">`[-w]`</td>
<td markdown="span">Also kill water mobs</td>
</tr>
</tbody>
</table>

<a id="command-/brush-paint"></a>

`/brush paint`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Paint brush, apply a function to a surface</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.paint`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush paint <shape> [radius] [density] <forest|item|set>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">The shape of the region</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">The density of the brush</td>
</tr>
</tbody>
</table>

<a id="command-/brush-none"></a>

`/brush none` (or `/brush unbind`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Unbind a bound brush from your current item</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush none`</td>
</tr>
</tbody>
</table>

<a id="command-/brush-clipboard"></a>

`/brush clipboard` (or `/brush copy`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Choose the clipboard brush</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.clipboard`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush clipboard [-abeov] [-m <sourceMask>]`</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">Don’t paste air from the clipboard</td>
</tr>
<tr>
<td markdown="span">`[-v]`</td>
<td markdown="span">Include structure void blocks</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">Paste starting at the target location, instead of centering on it</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">Paste entities if available</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Paste biomes if available</td>
</tr>
<tr>
<td markdown="span">`[-m <sourceMask>]`</td>
<td markdown="span">Skip blocks matching this mask in the clipboard</td>
</tr>
</tbody>
</table>

<a id="command-/brush-snowsmooth"></a>

`/brush snowsmooth`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Choose the snow terrain softener brush</p> <p markdown="span">Example: ‘/brush snowsmooth 5 1 -l 3’</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.snowsmooth`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush snowsmooth [radius] [iterations] [-l <snowBlockCount>] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The radius to sample for softening</td>
</tr>
<tr>
<td markdown="span">`[iterations]`</td>
<td markdown="span">The number of iterations to perform</td>
</tr>
<tr>
<td markdown="span">`[-l <snowBlockCount>]`</td>
<td markdown="span">The number of snow blocks under snow</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">The mask of blocks to use for the heightmap</td>
</tr>
</tbody>
</table>

<a id="command-/brush-gravity"></a>

`/brush gravity` (or `/brush grav`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Gravity brush, simulates the effect of gravity</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.gravity`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush gravity [radius] [-h <height>]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The radius to apply gravity in</td>
</tr>
<tr>
<td markdown="span">`[-h <height>]`</td>
<td markdown="span">Affect blocks between the given height, upwards and downwards, rather than the target location Y + radius</td>
</tr>
</tbody>
</table>

<a id="command-/brush-heightmap"></a>

`/brush heightmap`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Heightmap brush, raises or lowers terrain using an image heightmap</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.heightmap`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush heightmap [-efr] <imageName> [radius] [intensity]`</td>
</tr>
<tr>
<td markdown="span">`<imageName>`</td>
<td markdown="span">The name of the image</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
<tr>
<td markdown="span">`[intensity]`</td>
<td markdown="span">The intensity of the brush</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">Erase blocks instead of filling them</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">Don’t change blocks above the selected height</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Randomizes the brush’s height slightly.</td>
</tr>
</tbody>
</table>

<a id="command-/brush-extinguish"></a>

`/brush extinguish` (or `/brush ex`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Shortcut fire extinguisher brush</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.ex`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush extinguish [radius]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The radius to extinguish</td>
</tr>
</tbody>
</table>

<a id="command-/brush-feature"></a>

`/brush feature`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Feature brush, paints Minecraft generation features</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.feature`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush feature <shape> [radius] [density] <type>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">The shape of the region</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">The density of the brush</td>
</tr>
<tr>
<td markdown="span">`<type>`</td>
<td markdown="span">The type of feature to use</td>
</tr>
</tbody>
</table>

<a id="command-/brush-sphere"></a>

`/brush sphere` (or `/brush s`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Choose the sphere brush</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.sphere`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush sphere [-h] <pattern> [radius]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The radius of the sphere</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Create hollow spheres instead</td>
</tr>
</tbody>
</table>

<a id="command-/brush-raise"></a>

`/brush raise`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Raise brush, raise all blocks by one</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.raise`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush raise <shape> [radius]`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">The shape of the region</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
</tbody>
</table>

<a id="command-/brush-smooth"></a>

`/brush smooth`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Choose the terrain softener brush</p> <p markdown="span">Example: ‘/brush smooth 2 4 grass_block,dirt,stone’</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.smooth`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush smooth [radius] [iterations] [mask]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The radius to sample for softening</td>
</tr>
<tr>
<td markdown="span">`[iterations]`</td>
<td markdown="span">The number of iterations to perform</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">The mask of blocks to use for the heightmap</td>
</tr>
</tbody>
</table>

<a id="command-/brush-cylinder"></a>

`/brush cylinder` (or `/brush cyl`, `/brush c`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Choose the cylinder brush</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.cylinder`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush cylinder [-h] <pattern> [radius] [height]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The radius of the cylinder</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">The height of the cylinder</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">Create hollow cylinders instead</td>
</tr>
</tbody>
</table>

<a id="command-/brush-set"></a>

`/brush set`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Set brush, sets all blocks in the area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.set`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush set <shape> [radius] <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">The shape of the region</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The pattern of blocks to set</td>
</tr>
</tbody>
</table>

<a id="command-/brush-apply"></a>

`/brush apply`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Apply brush, apply a function to every block</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.apply`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush apply <shape> [radius] <forest|item|set>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">The shape of the region</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
</tbody>
</table>

<a id="command-/brush-deform"></a>

`/brush deform`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Deform brush, applies an expression to an area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.deform`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush deform [-or] <shape> [radius] [expression]`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">The shape of the region</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
<tr>
<td markdown="span">`[expression]`</td>
<td markdown="span">Expression to apply</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Use the game’s coordinate origin</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">Use the placement position as the origin</td>
</tr>
</tbody>
</table>

<a id="command-/brush-lower"></a>

`/brush lower`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Lower brush, lower all blocks by one</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.lower`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush lower <shape> [radius]`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">The shape of the region</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
</tbody>
</table>

<a id="command-/brush-erode"></a>

`/brush erode`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Erode preset for morph brush, erodes blocks in the area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.morph`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush erode [brushSize]`</td>
</tr>
<tr>
<td markdown="span">`[brushSize]`</td>
<td markdown="span">The size of the brush</td>
</tr>
</tbody>
</table>

<a id="command-/brush-dilate"></a>

`/brush dilate`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Dilate preset for morph brush, dilates blocks in the area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.morph`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush dilate [brushSize]`</td>
</tr>
<tr>
<td markdown="span">`[brushSize]`</td>
<td markdown="span">The size of the brush</td>
</tr>
</tbody>
</table>

<a id="command-/brush-snow"></a>

`/brush snow`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Snow brush, sets snow in the area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.snow`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush snow [-s] <shape> [radius]`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">The shape of the region</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">Whether to stack snow</td>
</tr>
</tbody>
</table>

<a id="command-/brush-biome"></a>

`/brush biome`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Biome brush, sets biomes in the area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.biome`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush biome [-c] <shape> [radius] <biomeType>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">The shape of the region</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The size of the brush</td>
</tr>
<tr>
<td markdown="span">`<biomeType>`</td>
<td markdown="span">The biome type</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">Whether to set the full column</td>
</tr>
</tbody>
</table>

<a id="command-/brush-morph"></a>

`/brush morph`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Morph brush, morphs blocks in the area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.brush.morph`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/brush morph [brushSize] [minErodeFaces] [numErodeIterations] [minDilateFaces] [numDilateIterations]`</td>
</tr>
<tr>
<td markdown="span">`[brushSize]`</td>
<td markdown="span">The size of the brush</td>
</tr>
<tr>
<td markdown="span">`[minErodeFaces]`</td>
<td markdown="span">Minimum number of faces for erosion</td>
</tr>
<tr>
<td markdown="span">`[numErodeIterations]`</td>
<td markdown="span">Erode iterations</td>
</tr>
<tr>
<td markdown="span">`[minDilateFaces]`</td>
<td markdown="span">Minimum number of faces for dilation</td>
</tr>
<tr>
<td markdown="span">`[numDilateIterations]`</td>
<td markdown="span">Dilate iterations</td>
</tr>
</tbody>
</table>

## [Biome Commands](https://worldedit.enginehub.org/en/latest/commands/#id10) { #biome-commands }

<a id="command-/biomelist"></a>

`/biomelist` (or `/biomels`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Gets all biomes available.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.biome.list`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/biomelist [-p <page>]`</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">Page number.</td>
</tr>
</tbody>
</table>

<a id="command-/biomeinfo"></a>

`/biomeinfo`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Get the biome of the targeted block.</p> <p markdown="span">By default, uses all blocks in your selection.</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.biome.info`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/biomeinfo [-pt]`</td>
</tr>
<tr>
<td markdown="span">`[-t]`</td>
<td markdown="span">Use the block you are looking at.</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">Use the block you are currently in.</td>
</tr>
</tbody>
</table>

<a id="command-//setbiome"></a>

`//setbiome`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Sets the biome of your current block or region.</p> <p markdown="span">By default, uses all the blocks in your selection</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.biome.set`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//setbiome [-p] <target>`</td>
</tr>
<tr>
<td markdown="span">`<target>`</td>
<td markdown="span">Biome type.</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">Use your current position</td>
</tr>
</tbody>
</table>

<a id="command-//replacebiome"></a>

`//replacebiome`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="block">

<p markdown="span">Replaces the biome of your current block or region.</p> <p markdown="span">By default, uses all the blocks in your selection</p>

</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.biome.set`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//replacebiome [-p] <from> <target>`</td>
</tr>
<tr>
<td markdown="span">`<from>`</td>
<td markdown="span">The mask representing where to replace biomes</td>
</tr>
<tr>
<td markdown="span">`<target>`</td>
<td markdown="span">Biome type to set</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">Use your current position</td>
</tr>
</tbody>
</table>

## [Chunk Commands](https://worldedit.enginehub.org/en/latest/commands/#id11) { #chunk-commands }

<a id="command-/chunkinfo"></a>

`/chunkinfo`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Get information about the chunk you’re inside</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.chunkinfo`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/chunkinfo`</td>
</tr>
</tbody>
</table>

<a id="command-/listchunks"></a>

`/listchunks`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">List chunks that your selection includes</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.listchunks`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/listchunks [-p <page>]`</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">Page number.</td>
</tr>
</tbody>
</table>

<a id="command-/delchunks"></a>

`/delchunks`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Delete chunks that your selection includes</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.delchunks`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/delchunks [-o <beforeTime>]`</td>
</tr>
<tr>
<td markdown="span">`[-o <beforeTime>]`</td>
<td markdown="span">Only delete chunks older than the specified time.</td>
</tr>
</tbody>
</table>

## [Snapshot Commands](https://worldedit.enginehub.org/en/latest/commands/#id12) { #snapshot-commands }

<a id="command-/restore"></a>

`/restore` (or `//restore`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Restore the selection from a snapshot</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/restore [snapshot]`</td>
</tr>
<tr>
<td markdown="span">`[snapshot]`</td>
<td markdown="span">The snapshot to restore</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot"></a>

`/snapshot` (or `/snap`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Snapshot commands for restoring backups</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.snapshots.restore`, `worldedit.snapshots.list`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/snapshot <before|use|sel|after|list>`</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot-before"></a>

`/snapshot before`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Choose the nearest snapshot before a date</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/snapshot before <date>`</td>
</tr>
<tr>
<td markdown="span">`<date>`</td>
<td markdown="span">The soonest date that may be used</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot-use"></a>

`/snapshot use`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Choose a snapshot to use</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/snapshot use <name>`</td>
</tr>
<tr>
<td markdown="span">`<name>`</td>
<td markdown="span">Snapshot to use</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot-sel"></a>

`/snapshot sel`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Choose the snapshot based on the list id</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/snapshot sel <index>`</td>
</tr>
<tr>
<td markdown="span">`<index>`</td>
<td markdown="span">The list ID to select</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot-after"></a>

`/snapshot after`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Choose the nearest snapshot after a date</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/snapshot after <date>`</td>
</tr>
<tr>
<td markdown="span">`<date>`</td>
<td markdown="span">The soonest date that may be used</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot-list"></a>

`/snapshot list`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">List snapshots</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.snapshots.list`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/snapshot list [-p <page>]`</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">Page of results to return</td>
</tr>
</tbody>
</table>

## [Scripting Commands](https://worldedit.enginehub.org/en/latest/commands/#id13) { #scripting-commands }

<a id="command-/cs"></a>

`/cs`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Execute a CraftScript</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.scripting.execute`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/cs <filename> [args...]`</td>
</tr>
<tr>
<td markdown="span">`<filename>`</td>
<td markdown="span">Filename of the CraftScript to load</td>
</tr>
<tr>
<td markdown="span">`[args...]`</td>
<td markdown="span">Arguments to the CraftScript</td>
</tr>
</tbody>
</table>

<a id="command-/.s"></a>

`/.s`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Execute last CraftScript</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.scripting.execute`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/.s [args...]`</td>
</tr>
<tr>
<td markdown="span">`[args...]`</td>
<td markdown="span">Arguments to the CraftScript</td>
</tr>
</tbody>
</table>

## [Utility Commands](https://worldedit.enginehub.org/en/latest/commands/#id14) { #utility-commands }

<a id="command-//fill"></a>

`//fill`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Fill a hole</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.fill`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//fill <pattern> <radius> [depth]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The blocks to fill with</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">The radius to fill in</td>
</tr>
<tr>
<td markdown="span">`[depth]`</td>
<td markdown="span">The depth to fill</td>
</tr>
</tbody>
</table>

<a id="command-//fillr"></a>

`//fillr`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Fill a hole recursively</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.fill.recursive`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//fillr <pattern> <radius> [depth]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">The blocks to fill with</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">The radius to fill in</td>
</tr>
<tr>
<td markdown="span">`[depth]`</td>
<td markdown="span">The depth to fill</td>
</tr>
</tbody>
</table>

<a id="command-//drain"></a>

`//drain`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Drain a pool</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.drain`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//drain [-w] <radius>`</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">The radius to drain</td>
</tr>
<tr>
<td markdown="span">`[-w]`</td>
<td markdown="span">Also un-waterlog blocks</td>
</tr>
</tbody>
</table>

<a id="command-/fixlava"></a>

`/fixlava` (or `//fixlava`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Fix lava to be stationary</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.fixlava`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/fixlava <radius>`</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">The radius to fix in</td>
</tr>
</tbody>
</table>

<a id="command-/fixwater"></a>

`/fixwater` (or `//fixwater`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Fix water to be stationary</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.fixwater`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/fixwater <radius>`</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">The radius to fix in</td>
</tr>
</tbody>
</table>

<a id="command-/removeabove"></a>

`/removeabove` (or `//removeabove`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Remove blocks above your head.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.removeabove`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/removeabove [size] [height]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">The apothem of the square to remove from</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">The maximum height above you to remove from</td>
</tr>
</tbody>
</table>

<a id="command-/removebelow"></a>

`/removebelow` (or `//removebelow`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Remove blocks below you.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.removebelow`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/removebelow [size] [height]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">The apothem of the square to remove from</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">The maximum height below you to remove from</td>
</tr>
</tbody>
</table>

<a id="command-/removenear"></a>

`/removenear` (or `//removenear`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Remove blocks near you.</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.removenear`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/removenear <mask> [radius]`</td>
</tr>
<tr>
<td markdown="span">`<mask>`</td>
<td markdown="span">The mask of blocks to remove</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The radius of the square to remove from</td>
</tr>
</tbody>
</table>

<a id="command-/replacenear"></a>

`/replacenear` (or `//replacenear`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Replace nearby blocks</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.replacenear`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/replacenear <radius> [from] <to>`</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">The radius of the square to remove in</td>
</tr>
<tr>
<td markdown="span">`[from]`</td>
<td markdown="span">The mask matching blocks to remove</td>
</tr>
<tr>
<td markdown="span">`<to>`</td>
<td markdown="span">The pattern of blocks to replace with</td>
</tr>
</tbody>
</table>

<a id="command-/snow"></a>

`/snow` (or `//snow`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Simulates snow</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.snow`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/snow [-s] [size] [height]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">The radius of the cylinder to snow in</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">The height of the cylinder to snow in</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">Stack snow layers</td>
</tr>
</tbody>
</table>

<a id="command-/thaw"></a>

`/thaw` (or `//thaw`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Thaws the area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.thaw`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/thaw [size] [height]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">The radius of the cylinder to thaw in</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">The height of the cylinder to thaw in</td>
</tr>
</tbody>
</table>

<a id="command-/green"></a>

`/green` (or `//green`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Converts dirt to grass blocks in the area</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.green`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/green [-f] [size] [height]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">The radius of the cylinder to convert in</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">The height of the cylinder to convert in</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">Also convert coarse dirt</td>
</tr>
</tbody>
</table>

<a id="command-/extinguish"></a>

`/extinguish` (or `//ex`, `//ext`, `//extinguish`, `/ex`, `/ext`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Extinguish nearby fire</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.extinguish`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/extinguish [radius]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">The radius of the square to remove in</td>
</tr>
</tbody>
</table>

<a id="command-/butcher"></a>

`/butcher`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Kill all or nearby mobs</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.butcher`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/butcher [-abfgnprtw] [radius]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">Radius to kill mobs in</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">Also kill pets</td>
</tr>
<tr>
<td markdown="span">`[-n]`</td>
<td markdown="span">Also kill NPCs</td>
</tr>
<tr>
<td markdown="span">`[-g]`</td>
<td markdown="span">Also kill golems</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">Also kill animals</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">Also kill ambient mobs</td>
</tr>
<tr>
<td markdown="span">`[-t]`</td>
<td markdown="span">Also kill mobs with name tags</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">Also kill all friendly mobs (Applies the flags -abgnpt)</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">Also destroy armor stands</td>
</tr>
<tr>
<td markdown="span">`[-w]`</td>
<td markdown="span">Also kill water mobs</td>
</tr>
</tbody>
</table>

<a id="command-/remove"></a>

`/remove` (or `/rem`, `/rement`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Remove all entities of a type</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.remove`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`/remove <remover> <radius>`</td>
</tr>
<tr>
<td markdown="span">`<remover>`</td>
<td markdown="span">The type of entity to remove</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">The radius of the cuboid to remove from</td>
</tr>
</tbody>
</table>

<a id="command-//calculate"></a>

`//calculate` (or `//calc`, `//eval`, `//evaluate`, `//solve`)

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Evaluate a mathematical expression</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.calc`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//calculate <input...>`</td>
</tr>
<tr>
<td markdown="span">`<input...>`</td>
<td markdown="span">Expression to evaluate</td>
</tr>
</tbody>
</table>

<a id="command-//help"></a>

`//help`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Description**</td>
<td markdown="span">Displays help for WorldEdit commands</td>
</tr>
<tr>
<td markdown="span">**Permissions**</td>
<td markdown="span">`worldedit.help`</td>
</tr>
<tr>
<td markdown="span">**Usage**</td>
<td markdown="span">`//help [-s] [-p <page>] [command...]`</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">List sub-commands of the given command, if applicable</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">The page to retrieve</td>
</tr>
<tr>
<td markdown="span">`[command...]`</td>
<td markdown="span">The command to retrieve help for</td>
</tr>
</tbody>
</table>
