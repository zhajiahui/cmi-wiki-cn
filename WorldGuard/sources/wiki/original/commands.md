# Commands { #commands }

WorldGuard provides five categories of commands:

- Gameplay-related (`/god`, `/heal`, etc.)

- Working with [regions](https://worldguard.enginehub.org/en/latest/regions/)

- Time-sensitive emergency response

- Troubleshooting

- WorldGuard-related (version information, reloading configuration)

See the [permissions page](https://worldguard.enginehub.org/en/latest/permissions/) for the necessary permission nodes. Some commands come with built-in aliases, those are listed in the same row.

!!! hint "Hint"

    When a parameter (like `<player>`) is surrounded by `[]`, it means that the parameter is optional. In addition, don’t put `<` or `>` when entering the command.

## Gameplay { #gameplay }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Command</th>
<th markdown="span">Parameters</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">/god</td>
<td markdown="span">[-s] [&lt;player&gt;]</td>
<td markdown="span">Give yourself or another player invicinbility. `-s` can be optionally specified to have no message emitted.</td>
</tr>
<tr>
<td markdown="span">/ungod</td>
<td markdown="span">[-s] [&lt;player&gt;]</td>
<td markdown="span">Remove invicinbility from yourself or another player. `-s` can be optionally specified to have no message emitted.</td>
</tr>
<tr>
<td markdown="span">/heal</td>
<td markdown="span">[-s] [&lt;player&gt;]</td>
<td markdown="span">Heal yourself or another player. `-s` can be optionally specified to have no message emitted.</td>
</tr>
<tr>
<td markdown="span">/slay</td>
<td markdown="span">[-s] [&lt;player&gt;]</td>
<td markdown="span">Slay yourself or another player. `-s` can be optionally specified to have no message emitted.</td>
</tr>
<tr>
<td markdown="span">/locate</td>
<td markdown="span">[&lt;player&gt;]</td>
<td markdown="span">Have your compass point to another player (if specified), or pointed to spawn if no player is specified.</td>
</tr>
<tr>
<td markdown="span">/stack /;</td>
<td markdown="span"></td>
<td markdown="span">Organize your inventory and automatically stack items.</td>
</tr>
</tbody>
</table>

### Selectors { #selectors }

The commands that take a player name support *selectors*, but they differ from Minecraft’s selectors which came about 3 years later.

Players can be matched with:

- By default, players are matched if their name *starts with* the given name

- `*` to match all

- `#<world>` to match everyone on a certain world

- `#near` to match nearby players to the command’s user

- `@<name>` to match a player’s name exactly

## Regions { #regions }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Command</th>
<th markdown="span">Parameters</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">/wg flushstates /wg clearstates</td>
<td markdown="span">[&lt;player&gt;]</td>
<td markdown="span">Debugging command that clears information about players that is stored for the purpose of applying [region flags](https://worldguard.enginehub.org/en/latest/regions/flags/). For example, for the `entry` flag to work, the player’s last ‘block’ is stored every time they move, which is used to determine whether the player has entered a region. This command can be useful when a player is stuck inside or outside a region due to the `entry` or `exit` flags, especially after changes in membership, permission groups, etc. The optional player argument will reset states only for the provided player; if not supplied, all players’ flag states will be reset.</td>
</tr>
<tr>
<td markdown="span">/rg bypass /rg toggle-bypass</td>
<td markdown="span">[on/off]</td>
<td markdown="span">Toggles region protection bypass mode, allowing you to ignore region protections (except for PvP deny)</td>
</tr>
</tbody>
</table>

Additional region commands can be found in the [regions section](https://worldguard.enginehub.org/en/latest/regions/commands/).

## Emergency { #emergency }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Command</th>
<th markdown="span">Parameters</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">/stopfire</td>
<td markdown="span">[&lt;world&gt;]</td>
<td markdown="span">Immediately stop all fire spread on the current or given world.</td>
</tr>
<tr>
<td markdown="span">/allowfire</td>
<td markdown="span">[&lt;world&gt;]</td>
<td markdown="span">Lift the fire spread suspension.</td>
</tr>
<tr>
<td markdown="span">/stoplag /halt-activity /haltactivity</td>
<td markdown="span">[-s]</td>
<td markdown="span">Remove all entities in all worlds and enter a mode where all physics events and liquid flow events are stopped. In addition, when a chunk loads, all entities in that chunk are removed. The purpose of this command is to solve problems involving thousands of entities or items. However, when this command was added, tameable animals were not a thing and the loss of entities was not an issue, but this is no longer the case and this command should be reserved for extremely desperate occasions. `-s` can be provided to make the toggle not issue an announcement in chat.</td>
</tr>
<tr>
<td markdown="span">/stoplag /halt-activity /haltactivity</td>
<td markdown="span">-c [-s]</td>
<td markdown="span">Disable the ‘stop lag’ mode. `-s` can be provided to make the toggle not issue an announcement in chat.</td>
</tr>
<tr>
<td markdown="span">/stoplag /halt-activity /haltactivity</td>
<td markdown="span">-i</td>
<td markdown="span">Display the status of the ‘stop lag’ mode.</td>
</tr>
</tbody>
</table>

<a id="id1"></a>

## Troubleshooting { #troubleshooting }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Command</th>
<th markdown="span">Parameters</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">/wg report</td>
<td markdown="span">[-p]</td>
<td markdown="span">Writes a report file (placed at `plugins/WorldGuard/report.txt`) detailing information about the server setup (list of plugins, their versions, world settings) as well as WorldGuard’s configuration. This command is to easily provide information to others for support purposes. The report does not contain sensitive data. Use `-p` to also submit the report to a pastebin site and have a link generated that you can give to others.</td>
</tr>
<tr>
<td markdown="span">/wg profile</td>
<td markdown="span">[-p] [-i &lt;milliseconds&gt;] [-t &lt;name&gt;] [&lt;minutes&gt;]</td>
<td markdown="block">

<p markdown="span">Starts profiling CPU usage of the current running server, and runs the profiler for the given duration (defaulting to 5 minutes if a duration is not specified). The profiler is based on [WarmRoast](https://github.com/sk89q/warmroast).</p> <p markdown="span">By default, results are only collected for the main thread where the world is ‘ticked’, but `-t` can be specified to filter by a different thread name (case in-sensitive). An asterisk (`*`) can be specified instead to profile all threads (i.e. `-t *`). By default, the profiler uses a sampling interval of 20 milliseconds, but `-i` can be used to specify a custom interval in milliseconds between 1 and 100. Lower intervals are more accurate but more performance intensive, while larger intervals are less accurate and less performance intensive.</p> <p markdown="span">Use `-p` to also submit the profiling result to a pastebin site and have a link generated that you can give to others. This is recommended because the output of the profiler is formatted by the pastebin site to make it readable.</p>

</td>
</tr>
<tr>
<td markdown="span">/wg stopprofile</td>
<td markdown="span"></td>
<td markdown="span">Stops a currently running profiler.</td>
</tr>
<tr>
<td markdown="span">/wg debug testbreak</td>
<td markdown="span">[-t] [-s] &lt;player&gt;</td>
<td markdown="span">Simulates a ‘block break’ event. This is explained below.</td>
</tr>
<tr>
<td markdown="span">/wg debug testplace</td>
<td markdown="span">[-t] [-s] &lt;player&gt;</td>
<td markdown="span">Simulates a ‘block place’ event. This is explained below.</td>
</tr>
<tr>
<td markdown="span">/wg debug testinteract</td>
<td markdown="span">[-t] [-s] &lt;player&gt;</td>
<td markdown="span">Simulates a ‘block interact’ event. This is explained below.</td>
</tr>
<tr>
<td markdown="span">/wg debug testdamage</td>
<td markdown="span">[-t] [-s] &lt;player&gt;</td>
<td markdown="span">Simulates an ‘entity damage’ event (use to test PvP and PvE). This is explained below.</td>
</tr>
</tbody>
</table>

### Event Simulation { #event-simulation }

The event simulation commands are useful if, for example, players can’t break blocks for some reason and you cannot identify the plugin causing it (without more drastic measures). Use of the `/wg debug testbreak` command would simulate the block break and record which, if any, plugins chose to block the virtual block break.

In order to use the commands, a player must be provided. The player is the *source* of the event. The target of the event (i.e. the block that being “broken” or the entity that is being “attacked”), however, is from the perspective of the person running the command. However, if `-t` is specified, then the target is from the perspective of the source player. The target is whichever block or entity is in the player’s crosshair.

Several plugins may be listed in the output of the command, but only the first entry matters. This is because, for example, if Plugin A blocks the action, and Plugin B, which runs afterwards, “unblocks” the action, then Plugin A has no effect. WorldGuard lists the last running plugins first.

An example

If you want to see why PvP seems to be blocked, have another player (who is not able to PvP) look at you and then run the command:

```text
/wg debug testdamage -t other_player_name
```

Be aware that the tests are not entirely complete. This is because Bukkit sometimes throws *other* events for some actions. For example, when filling a bucket, Bukkit fires a *bucket fill event*, which WorldGuard currently does not provide a way to simulate. Lastly, sometimes Minecraft features (like adventure mode or the built-in spawn protection) may be at play.

Use `-s` to print a stacktrace with additional information to the console.

!!! warning "Warning"

    While the events are simulations in that Minecraft won’t place or break the block in question, plugins do act upon the events. For example, a plugin may allow you to right click specially marked signs to teleport, and simulating an interact event on a teleport sign may possibly cause the victim player to be teleported.

## Miscellaneous { #miscellaneous }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Command</th>
<th markdown="span">Parameters</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">/wg version</td>
<td markdown="span"></td>
<td markdown="span">Show WorldGuard’s version.</td>
</tr>
<tr>
<td markdown="span">/wg reload</td>
<td markdown="span"></td>
<td markdown="span">Reload WorldGuard’s configuration, blacklist, and region data.</td>
</tr>
<tr>
<td markdown="span">/wg running /wg queue</td>
<td markdown="span"></td>
<td markdown="span">Show WorldGuard’s running tasks. An example of a running task is a UUID lookup of a player that occurs in the background.</td>
</tr>
</tbody>
</table>
