For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

**0.5.3 Build #60**

- PlayerQue now uses ConcurrentHashMap to avoid ConcurrentModificationException. (Thanks tenowg!)
- `/denizen reload` and `/denizen save` can now be used in the console.
- Check for interact_delay_in_ticks = 0 and change it to 1. (Thanks Sparta!) Probably a good idea to keep this at least 10, though.

**0.5.3 Build #56**

- Added FAIL command. Sets the script as 'FAILED' for checking with requirements. Note: A script can still be FAILED and FINISHED, they are seperate.
- Added FAILED requirement. Use FAILED [Name of Script]. Remember: SCRIPT NAMES ARE CaSe SeNsItIvE!
- Added RESET command. This can be used to reset the FAILED or FINISHED status of a script. Use RESET FAILED|FINISHED [Name of Script].
- Added small warning on the /denizen help stating that many commands listed there do not yet work -- this is a beta, people, I'm working on them :P
- Documenting /denizen adddata|decdata|getdata. Nothing to do with Denizens, really, but handy for checking/switching block data. Try it on a tree.
- Fixed WAIT command. It actually works as intended now.

**0.5.3 Build #48**

- Extended use of LOOK command. Can now specify a location bookmark to set Pitch and Yaw of a Denizen. Note: When making Location Bookmarks, your Pitch and Yaw are recorded along with your XYZ position. Use: LOOK [Location Bookmark]. Existing arguments, CLOSE and AWAY, are still valid. Additional note: LOOK CLOSE will override the set pitch/yaw, so be sure LOOK AWAY is used beforehand, or be sure LOOK CLOSE was not engaged.
- Fixed issue with RESPAWN command.
- Fixed issue with talking to Denizens close to one another. Players now only speak to the very closest Denizen.
- Added TELEPORT command to teleport the player to a Denizen's location bookmark. Use TELEPORT [Location Bookmark].
- Added REFUSE command to take a permission from the player. Use REFUSE [name.of.permission.node].

It is suggested you use the latest builds of C2.

**0.5.3 Build #42**

- SWITCH now activates redstone. Sorry about that folks.
- WAIT command added.
- SPAWN command added.
- Other code optimizations/cleanup.

Big thanks to the hardworking beta testers in #citizens! Thank you!

**0.5.3 Build #25**

- NARRATE command now replaces <NPC> properly.
- Denizens no longer requires you to be the owner of the NPC to use commands.
- Tweaked multi-line engine to accomodate for extra long names.
- ZAP now uses getName instead of getDisplayName (Sorry if this causes issues with current progress.)

**0.5.3 Alpha**

- Added SWITCH command. Denizens can now flip levers!
- Added Denizen Project to [Citizens Jenkins](http://ci.citizensnpcs.net/job/Denizen/)!

**0.5.2 Alpha:**

- Fixed requirements WEARING and -TIME. Note: PermissionsBukkit users are still having problems with GROUP.
- Added FOLLOW, TAKE, NARRATE, and CAST commands.

Smaller update than I planned, stay tuned for more!

**0.5.1 Alpha:**

- Fixed requirements... they should all work now, except haven't tested requirements which can have an enchantment.
- Added the ability to give Denizens 'Location Bookmarks'. Use /denizen bookmark location [name].
- Added WALKTO, PERMISS, FINISH, RESPAWN, WEATHER and EXECUTE commands.
- Started to flesh out /denizen help
- Added activity scheduler.
