# Blacklist { #blacklist }

The blacklist allows an action (or several) to be performed whenever a player does something (place a block, use an item, etc.). Some example applications include:

- Blocking players from mining gold ore

- Notifying all administrators when a diamond block is found

- Sending the player a message when they place an enchantment table

An example of a blacklist file is:

```text
# Deny lava buckets
[lava_bucket]
ignore-groups=admins,mods
on-use=deny,tell
message=Sorry, you can't use lava buckets!

# Deny some ore
[gold_ore,iron_ore]
ignore-groups=admins
on-break=deny,tell,notify

# No TNT!
[tnt]
ignore-groups=admins
on-place=deny,notify,kick
```

## Blacklist Files { #blacklist-files }

For every world, you will find per-world configuration files:

- `worlds/world/blacklist.txt`

- `worlds/world_nether/blacklist.txt`

- `worlds/mining_world/blacklist.txt`

!!! hint "Hint"

    Unfortunately, you cannot share one blacklist file for several worlds from within WorldGuard. However, you may be able to create a “symlink” on your operaitng system to have two files refer to the same one.

## The Format { #the-format }

A blacklist file consists of several sections in the format of:

```text
[a list of items/blocks to match]
event to watch=what to do
event to watch=what to do
event to watch=what to do
option=value
```

Lines starting with `#` are ignored by WorldGuard. You can use this to place notes for yourself.

### Matching Syntax { #matching-syntax }

Items and blocks can be matched by specifying one of the entries on [Bukkit’s material list](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html). Multiple items and blocks can be matched by separating each entry by a comma:

```text
[oak_wood,brick,glass]
```

## Events { #events }

Now that you have specified the items or blocks to watch out for, you must specify the situations in which you would like to catch, as well as the action to perform.

The available events are listed below.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Event</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">on-break</td>
<td markdown="span">When the matched block is being mined</td>
</tr>
<tr>
<td markdown="span">on-destroy-with</td>
<td markdown="span">When the matched item or block is being held by the player during mining</td>
</tr>
<tr>
<td markdown="span">on-place</td>
<td markdown="span">When the matched block is being placed</td>
</tr>
<tr>
<td markdown="span">on-use</td>
<td markdown="span">When an item in the player’s inventory is used</td>
</tr>
<tr>
<td markdown="span">on-interact</td>
<td markdown="span">When a player interacts (i.e. right click) with the matched block (door, lever, etc.)</td>
</tr>
<tr>
<td markdown="span">on-drop</td>
<td markdown="span">When the player drops the matched item</td>
</tr>
<tr>
<td markdown="span">on-acquire</td>
<td markdown="span">When the player acquires the matched item</td>
</tr>
<tr>
<td markdown="span">on-dispense</td>
<td markdown="span">When a dispenser dispenses the matched item</td>
</tr>
<tr>
<td markdown="span">on-equip</td>
<td markdown="span">When the player equips the matched item</td>
</tr>
</tbody>
</table>

When specifying an event, a list of “actions” must be specified afterwards, as illustrated below:

```text
[enchantment_table]
on-place=deny,tell
on-drop=notify
```

### Available Actions { #available-actions }

Multiple actions can be specified for each event.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Action</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">deny</td>
<td markdown="span">Denies the action (only if the blacklist **not** in “whitelist mode” (explained later))</td>
</tr>
<tr>
<td markdown="span">allow</td>
<td markdown="span">Permits the action (only if the blacklist is in “whitelist mode”)</td>
</tr>
<tr>
<td markdown="span">notify</td>
<td markdown="span">Notify admins with the `worldguard.notify` permission</td>
</tr>
<tr>
<td markdown="span">log</td>
<td markdown="span">Log to console, file, or database</td>
</tr>
<tr>
<td markdown="span">tell</td>
<td markdown="span">Tell the player that the action was not allowed</td>
</tr>
<tr>
<td markdown="span">kick</td>
<td markdown="span">Kick the player</td>
</tr>
<tr>
<td markdown="span">ban</td>
<td markdown="span">Ban the player</td>
</tr>
</tbody>
</table>

## Options { #options }

Options are specified in the same place as events, as illustrated below:

```text
[enchantment_table]
on-place=deny,tell
message=Sorry, you can't use enchantment tables!
```

In this case, `message` is an option that overrides the message used by the “tell” action.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Option</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">ignore-groups</td>
<td markdown="span">Comma-separated list of permission groups to not affect</td>
</tr>
<tr>
<td markdown="span">ignore-perms</td>
<td markdown="span">Comma-separated list of permissions to not affect – make up your very own permissions!</td>
</tr>
<tr>
<td markdown="span">comment</td>
<td markdown="span">Message for yourself that is printed with `log` and `notify` actions (to override the default message)</td>
</tr>
<tr>
<td markdown="span">message</td>
<td markdown="span">Message to show the user (to override the default message). Put %s in the message to have it be replaced with the item name (in English)</td>
</tr>
</tbody>
</table>

## Whitelist Mode { #whitelist-mode }

Switching the blacklist to whitelist mode (via the [Configuration](https://worldguard.enginehub.org/en/latest/config/)) will invert the behavior. Only entries with the `allow` action will be permitted.

!!! tip "Tip"

    Whitelist mode may seem very restrictive. To place a block, you would need to allow using the block (the item in the player’s hand), interacting with the existing block (in the world, that’s being clicked to place “on”), and placing the block. You may find [Build Permissions](https://worldguard.enginehub.org/en/latest/build-perms/) easier to use since it supports wildcards (in permission nodes) depending on your use case.

## Examples { #examples }

Example: Blocking some bucket use

```text
[lava_bucket,water_bucket,bucket]
on-use=deny,tell
```

Example: Kicking players using TNT and notify administrators

```text
[tnt]
ignore-groups=admins
on-place=deny,notify,kick
```

Example: Allowing only the people in the “obsidian” group and administrators to use obsidian

```text
[obsidian]
ignore-groups=admins,obsidian
on-place=deny,tell
on-break=deny,tell
```

## Logging { #logging }

With the `log` action, messages can be logged to several places:

- Console

- File

- Database

These log targets can be enabled or disabled in the [Configuration](https://worldguard.enginehub.org/en/latest/config/). Multiple log targets can be enabled at one time. By default, only the console log target is enabled.

### Console Logging { #console-logging }

Console logging merely prints the log entries to the server console.

### File Logging { #file-logging }

File logging writes the log entries to a file. In the [Configuration](https://worldguard.enginehub.org/en/latest/config/), the path for the log file can be specified with special variables in it (like today’s date), so you can have logs automatically rotated every day.

The following variables can be used:

- %Y the year (YYYY)

- %m the month (MM)

- %d the day (DD)

- %W the week of the year (00-52)

- %H 24-hour time (HH)

- %h 12-hour time (HH)

- %i the minute (mm)

- %s the second (ss)

- %u the user’s name

- %% translates to a single percent sign “%”

### Database Logging { #database-logging }

WorldGuard can write the log entries to a MySQL database. However, you will have to create the database and table yourself first. The SQL needed to create the table is provided below:

```text
CREATE TABLE IF NOT EXISTS `blacklist_events` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `world` varchar(10) NOT NULL,
 `event` varchar(25) NOT NULL,
 `player` varchar(16) NOT NULL,
 `x` int(11) NOT NULL,
 `y` int(11) NOT NULL,
 `z` int(11) NOT NULL,
 `item` int(11) NOT NULL,
 `time` int(11) NOT NULL,
 `comment` varchar(255) DEFAULT NULL,
 PRIMARY KEY (`id`)
);
```
