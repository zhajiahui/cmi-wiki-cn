## NPC Click Commands

To run commands when clicking Citizens NPCs, use /npc command (`/npc help command`).

## Adding Commands

By default, "/npc command" will run commands as the **server**. Add the "-p" flag to run as the **player who clicked** instead.

For example: Use `/npc command add -p help` to make an NPC automatically execute "/help" as the player when clicked. Note that you don't type the "/" on the command name.

To auto-fill the player name, use "<p>". To autofill the NPC ID, use "<npc>".

For example: Use `/npc command add kick <p>` to make an NPC automatically kick the player when clicked.

Another common example: `/npc command add tp <p> 0 64 0` to automatically teleport the player that clicked the NPC to some coordinates (assumes the vanilla 'tp' command. If you use Essentials, use 'tppos' instead).

Note that this can be any command from Minecraft or any plugin, so for example if you use Multiverse, `/npc command add mvtp <p> myworldname` will use the Multiverse world teleport command.

### Other Placeholders

If you have PlaceholderAPI installed, you can use PAPI placeholders within commands. For example, `/npc command add msg <p> The current TPS is %server_tps%`.

Check [PlaceholderAPI's documentation](https://github.com/PlaceholderAPI/PlaceholderAPI/wiki) for details on available placeholders or how to format them.

### Permissions

By default, anybody can click the NPC to cause a command to execute, without any permission requirement.

If `-p` is used, any permissions check **by the command itself** is checked for the player.

If `-o` is used, it will execute as-op, meaning the player will be treated **temporarily** as if they were a server operator (unless you have a plugin that doesn't respect op, or a protection plugin that disables op). Be warned that `-o` can have side effects or performance problems.

Generally, it's best to execute as-server (don't specify `-p` or `-o` to use the default as-server), which will not require any permissions. You will need to use `<p>` to fill in the player name wherever the command requires one.

If you want to add your own additional permissions **requirement**, use `--permission my.perm.here` when adding the command.

### Speaking to the Player

To make an NPC command that causes an NPC to speak to the player (if you don't need the full options of the NPC command feature, just use `/npc text` instead), you can do:
`/npc command add say MESSAGE HERE`

Citizens automatically redirects the "say" command to speak as the NPC rather than as the server console.

Internally, the way this works is it replaces the `/say MESSAGE HERE` with `/npc speak MESSAGE HERE --target <p> --id <id>`.

If you want to use the vanilla "say" command, you can use `/npc command add minecraft:say ...`

### Bungee

On Bungee servers, this supports the Bungee `server` command, like `/npc command add -p server MyServerName`. Note that this is a special case built into Citizens internally, and bypasses any normal permission requirements automatically.

This might also work on Velocity or other proxy servers, if-and-only-if that proxy server implements the Bungee protocol, which many do.

Note that other bungee-proxy commands (or commands on Velocity or other proxies) will not work. Only commands that can be ran within the confines of the Spigot server instance will function. If you need to execute commands from a Bungee plugin, it is necessary for that plugin to provide a Spigot plugin with interfacing commands of its own, or to use some generic Bungee control relay like [DepenizenBungee](https://github.com/DenizenScript/Depenizen/blob/master/Docs/Bungee.md).

## Removing Commands

To remove a command, type `/npc command` to see the list of currently attached commands with ID numbers. You can click on the remove "-" to remove the command or manually type `/npc command remove ID#`.

## Execution Order

By default, if you add multiple commands with `/npc command`, they will all run at the same time in order.

You can instead set them to happen one click at a time, either in sequential order, or in random order.

To make the commands go in order, one at a time for each click, use `/npc command sequential`.

To make the commands go in a random order, but still only one at a time for each click, use `/npc command random`.

To go back to all-at-once, simply redo whichever command you used to change it (for example if you set it to sequential, just do `/npc command sequential` again to disable it and go back to default).

## Other Options

Other ways you can control `/npc command` include:

- `/npc command permissions x.y.z` to attach temporary permissions to the player (generally don't use this, instead use `-o` ... or just execute as-server)
- `/npc command add -l somethinghere` to make the command respond to left clicks (punch/attack). Note that this may not work if PvP is disabled.
- `/npc command add -r somethinghere` to make the command respond to right clicks (standard interact).
- `/npc command add --n 5 somethinghere` to make a command only usable a certain number of times per player (in this example, 5 usages).
- `/npc command add --cooldown 10s somethinghere` to make the command only usable once per certain time period (in this example, 10 seconds), for each player.
- `/npc command add --gcooldown 10s somethinghere` to make the command only usable once per certain time period (in this example, 10 seconds), globally (nobody can use the NPC again until the cooldown ends).
- `/npc command add --delay 40t somethinghere` to make the command have a delay before it activates (in this example, 40 ticks, aka 2 seconds).
- `/npc command cost 50` to make the command have a cost using any Vault-compatible economy plugin (in this example, $50). This will refuse to run for players that don't have enough money, and automatically take the money before executing the command for those that do have enough.
- `/npc command expcost 50` to make the command have an experience level cost. Works similar to 'cost', but for XP levels.
- `/npc command itemcost` to open a GUI to configure an item-cost (the player has to pay the item for the command to execute).
- `/npc command hideErrors` to hide all error message (no permission, no money, etc.) from players.

There are more options available for `/npc command` - type `/npc help command` in-game to see any such options.

## FAQ And Common Issues

### My left click command doesn't work!

A "left click" in Minecraft terms is not a click at all, it's a **punch**/attack! For a player-type NPC, that means "Left clicking the NPC" is, to Minecraft, *punching a player in the face*. In practice, this means that if you have PvP disabled (in your server.properties or via plugin), it will block "left clicks" as well.

To resolve this, you can either

- A: Just use right clicks (Minecraft calls this an 'entity interaction' and this is usually enabled except in the case of very very restrictive plugins)
- B: Enable PvP in your config. You can then disable **real** PvP via any Citizens-compatible plugin. If you use [Denizen] you can do so via a script like this:

```
no_pvp:
    type: world
    events:
        on player damages player:
        - determine cancelled
```

## Additional Support

If confused, join the [Citizens+Denizen shared Discord](https://discord.gg/Q6pZGSR) to ask for help!
