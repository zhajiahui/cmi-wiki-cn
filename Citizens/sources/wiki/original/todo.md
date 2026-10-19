## fullwall's TODO (please add under your name if you modify this)

- Make rename update in save file
- In-place conversion db<->yml<->nbt
- waypoints move location somehow ('draggable waypoints')
- Giants don't attack back

*jrbudda*

- Fix NPCs always looking south on load. - something to do with chunks unloading. When the chunk loads, the NPC's yaw gets messed up? Although the chunk never seems to unload...
- /npc copy creates yaml references on sentry lists, makes them 'linked' in memory. i.e. Copy sentry A to make B, change sentry A's targets and B's changes as well.
- NPCs still wont pathfind if you teleport them across worlds. Respawning them across worlds works (Bukkit issue, still waiting on a fix/response)
- Fix /reload duplicating NPCs
- Giants don't move.
- Add call to API to get the selected NPC for a CommandSender. (have to build against citizens.jar and get the NPCSelector now)
- Fix stuck-teleporting instantly when using waypoints?
- Make an Editor for wander
- Work out kinks in SQL storage. Read: redo SQL storage because it's incredibly hacky
- Documentation.

*davidcernat*

- Please make NPCs position themselves relative to other NPCs so that they don't overlap their location or walk through them.
- When you attack an NPC with a bow and move quickly to the side, have the NPC path to where you are now instead of where you used to be when you shot it.

## User suggestions
