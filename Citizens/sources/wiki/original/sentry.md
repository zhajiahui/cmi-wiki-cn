[![](https://wiki.citizensnpcs.co/images/e/e5/Sentry.png)](https://wiki.citizensnpcs.co/File:Sentry.png)  
  
**Sentry**

|  |  |
| --- | --- |
| **Author** | aufdemrand, jrbudda |
| **Version** | 1.8.6 |
| **Citizens build** | [2.0.16](http://ci.citizensnpcs.co/job/Citizens2/) (Use with CraftBukkit 1.8.6) |
| **Other dependencies** | None required, Vault and a permissions plugin suggested. |
| **Download** | [Link](http://ci.citizensnpcs.co/job/Sentry/28/artifact/target/sentry.jar) |
| **Description:** Citizens NPCs that attack monsters and can be killed. This has been replaced by [Sentinel](https://wiki.citizensnpcs.co/Sentinel "Sentinel")! | |

**SENTRY** HAS BEEN REPLACED BY [Sentinel](https://wiki.citizensnpcs.co/Sentinel "Sentinel")!

---

**SENTRY** HAS BEEN REPLACED BY [Sentinel](https://wiki.citizensnpcs.co/Sentinel "Sentinel")!

---

**SENTRY** HAS BEEN REPLACED BY [Sentinel](https://wiki.citizensnpcs.co/Sentinel "Sentinel")!

---

Old page:

**Sentry** is a Citizens 2.0 [character trait](https://wiki.citizensnpcs.co/Characters "Characters") that gives NPCs the ability to:

- Attack specific monsters, players, or groups automatically.
- Kill, and be killed by, players, monsters, and the environment.
- Guard locations, paths, players, or other NPCs.
- Use ranged or melee weapons.
- Be configured with stats such as strength, armor, speed, and night vision.
- Ride mounts!
- [Work with Denizen](https://wiki.citizensnpcs.co/Sentry/Sentry_and_Denizen "Sentry/Sentry and Denizen") to create NPCs that run scripts upon death.

Dev builds are now at: <http://ci.citizensnpcs.co/job/Sentry/>

The official source code repo is [Github/jrbudda/Sentry](https://github.com/jrbudda/Sentry) though Sentry is currently maintained at [Github/mcmonkey4eva/Sentry](https://github.com/mcmonkey4eva/Sentry)

[![](https://wiki.citizensnpcs.co/images/f/fd/KnightSentry.png)](https://wiki.citizensnpcs.co/File:KnightSentry.png)

Can I see your hall pass?

## DEPRECATION

DEPRECATION NOTICE:

Sentry has been replaced by Sentinel, information here: <https://github.com/mcmonkey4eva/Sentinel/blob/master/README.md>

## Updates

|  |  |
| --- | --- |
| **v. 1.8.6** 05/25/15 [download](http://ci.citizensnpcs.co/job/Sentry/28/artifact/target/sentry.jar)   - Update for MC 1.8.6   **v. 1.8.5** [download](http://ci.citizensnpcs.co/job/Sentry/27/artifact/target/sentry.jar)   - Update for MC 1.8.3   **v. 1.8.4 build 2** [download](http://ci.citizensnpcs.co/job/Sentry/24/artifact/target/sentry.jar)   - Update to work with Denizen updates.   **v. 1.8.4** [download](http://ci.citizensnpcs.co/job/Sentry/23/artifact/target/sentry.jar)   - Update to work with factions and Denizen updates.   **v. 1.8.3** [download](http://ci.citizensnpcs.co/job/Sentry/19/artifact/target/sentry.jar)   - Update to work with Bukkit for MC 1.8   **v. 1.8.2 build 3** [download](http://ci.citizensnpcs.co/job/Sentry/14/artifact/target/sentry.jar)   - Update to work with Bukkit for MC 1.7.10   **v. 1.8.2 build 2** 06/13/14 [download](http://ci.citizensnpcs.co/job/Sentry/13/artifact/target/sentry.jar)   - mini-update to patch compatibility with latest Denizen dev builds   **v. 1.8.2** 03/24/14 [download](http://ci.citizensnpcs.co/job/Sentry/12/artifact/target/sentry.jar)   - Update to work with Bukkit for MC 1.7.8 -> (EDIT: then to 1.7.9 as well)   **v. 1.8.1** 03/24/14 [download](http://ci.citizensnpcs.co/job/Sentry/8/artifact/target/sentry.jar)   - Update to work with Bukkit for MC 1.7.5   **v. 1.8.0** 12/10/13 [download](http://www.sendspace.com/file/t2aky8)   - Re-work guard targeting. Guard target no longer needs to be in range of Sentry when set (if its a player). You should no longer need to go find your bodyguard if you get separated and log out. - Fix mounted sentries not attacking correctly. - Add targeting support for minecraft scoreboard teams. (via TEAM:NAME) (War teams are now specified via WARTEAM:NAME) - Move respawn location when /npc copy is used. - Fix event targets not firing when in a worldguard or other pvp-protected situation.   **v. 1.7.1** 11/07/13 [download](https://dl.dropboxusercontent.com/u/54130586/Sentry/1.7.1/Sentry.jar)   - Update to work with Bukkit for MC 1.7.2   **v. 1.6.1** 11/07/13 [download](https://dl.dropboxusercontent.com/u/54130586/Sentry/1.6.1/Sentry.jar)   - code formatting work   **v. 1.5.4** 11/07/13 [download](https://dl.dropboxusercontent.com/u/54130586/Sentry/1.5.4/Sentry.jar)   - mini-update to fix compatibility with the new build of Citizens   **v. 1.5.3** 9/20/2013 [download](http://www.sendspace.com/file/fuk6r9)   - Update for craftbukkit 1.6.4   **v. 1.5.2** 8/27/2013 [download](http://www.sendspace.com/file/xx3ooi)   - Add *targetable* option to prevent mobs from attacking sentries. (this used to be done via */npc playerlist* but that stopped working in mc 1.6) - Fix Denizen actions not using correct killer when projectiles involved.   **v. 1.5.1** 8/3/2013 [download](http://www.sendspace.com/file/5sljfn)   - Sentries properly remember their spawn location. - Lots of little fixes to mounted sentries   - Mounts don't take damage from guard target   - Mounts move at 2x the */npc speed* of their rider while patrolling and 2x the */sentry speed* of their rider while attacking.   - Rider animation syncs up with the mounts better.   - Mounted bodyguards will properly teleport (requires VERY latest Citizens2 builds)   - Mounts are properly deleted when sentry is killed with respawn -1   **v. 1.5** 7/29/2013 [download](http://www.sendspace.com/file/4hvq4p)   - The Calvary has arrived! Sentries can now have and be mounts! See the <#Mounts> section - Disable death animation to prevent client-side ghost drops - Fix compatibility issue with latest builds of Denizen - Sentries always use 'old' pathfinder. - Fix health not saving.   **v. 1.4.1** 7/9/2013 [download](http://www.sendspace.com/file/jvpqc7)   - Compatible with 1.6.2   **v. 1.4.0.1** 7/4/2013 [download](http://www.sendspace.com/file/pnoyt5)   - (Mostly)Compatible with 1.6.1 and Citizens 2.0.9 - Compatible (only!) with Denizen .9   **v. 1.3.7** 7/3/2013 [download](http://www.sendspace.com/file/7kd6g1)   - Sentries can now optionally be immune to damage from things on their ignore list. - Sentry projectiles will go though* things on their ignore list. (*some accuracy loss may be observed) - Sentries will properly ignore event: targets if the perpetrator is on the ignore list. - Bodyguards can optionally NOT follow damage protection (for compatibility with modifyworld and other annoying plugins.) - Fix default config.yml (put quotes "" around your default targets and ignores!) - Compatible with Factions 2.0.X   **v. 1.3.6** 5/21/2013 [download](http://www.sendspace.com/file/adgqyl)   - Added configurable follow distance for bodyguards. Use /sentry follow [0-32] - Fix crash in Denizen DIE command. - Sentry now removes the Denizen 'Health' trait as it conflicts on a sentry. This should fix some bugs relating to health and re-spawning. - Added several Denizen 'actions'. see the Advanced Usage section. - No longer using NMS code for max health > 20. should be more compatible with other plugins.   **v. 1.3.5** 5/7/2013 [download](http://www.sendspace.com/file/2s90lz)   - Add KillDrops option to remove the item and exp drops from Sentry kills.   **v. 1.3.4** 5/4/2013 [download](http://www.sendspace.com/file/9gxfe6)   - Update for 1.5.2 - Add FACTIONENEMIES: target   **v. 1.3.3.3** 4/9/2013 [download](http://www.sendspace.com/file/4en9is)   - Fix sentries not dying with Denizen installed.   **v. 1.3.3.2** 3/21/2013 [download](http://www.sendspace.com/file/3emb6e)   - Fix error on sentry death if Denizen not installed.   **v. 1.3.3.1** 3/21/2013 [download](http://www.sendspace.com/file/i3t9h5)   - Change packages for craftbukkit 1.5.1   **v. 1.3.3** 3/19/2013 [download](http://www.sendspace.com/file/qot6p8)   - Compatible with Craftbukkit 1.5 and Citizens 2.0.8 - Fixed Sentry not loading if Denizen .76 is still installed.   **v. 1.3.2** 3/14/2013 [download](http://www.sendspace.com/file/ox6uyq)   - Compatibility with Denizen 0.8 and latest Citizens2 (Note that this will NOT work with Denizen 0.7x)   **v. 1.3.1** 1/19/2013 [download](http://www.sendspace.com/file/i3l47p)   - Compatibility with cb 1.4.7   **v. 1.3** 1/17/2013 [download](http://www.sendspace.com/file/s4bj6x)   - Use with CraftBukkit 1.4.6r0.4 and Citizens2 2.0.6 build 663 - Compatible with Denizen .8 and .76. The commands and triggers are the same, but the example scripts will not work with .8 until updated - Sentries will no longer retaliate to the projectiles of other NPCs. If this behavior messes up your setup, let me know and I can make it an option. - Workaround for bodyguards not teleporting with their owner. - New event target: PvE. Use to attack players who attack mobs/animals. - API: Sentries will always raise a NPCDeathEvent upon dying regardless of the die-like-players setting. Modifiing the item list in the NPCDeathEvent will modify the items the sentry drops. - API: Sentries should now have valid last damage cause and killer set. - Memory and CPU optimizations.   **v. 1.2.6b** 12/22/2012 [download](http://www.sendspace.com/file/ikgcxx)   - Compatibility with CraftBukkit 1.4.6r0.1 and Citizens2 2.0.6   **v. 1.2.5** 12/20/2012 [download](http://www.sendspace.com/file/wu8fmh)   - Compatibility with CraftBukkit 1.4.5r1.0 and Citizens2 release 2.0.5   **v. 1.2.4** 12/9/2012   - Compatibility with latest builds of craftbukkit (1.4.5 r0.3) and citizens2 build 606+   **v. 1.2.3** 11/27/2012   - Compatible with craftbukkit 1.4.4 - 1.4.5 r0.2 and citizens2 build 597. - Compatibility fixes for Chunk Unload settings in citizens2.   - Active bodyguards should no longer die if their owner teleports too far away.   - Regular sentries will not try to respawn if the chunk at their spawn location is unloaded.   **v. 1.2.2** 11/14/2012   - Bow draw and sword block animations implemented - Thanks dotblank! - More Towny support: use the NATIONENEMIES: target to automatically attack enemies of the specified nation!   **v. 1.2.1** 10/29/2012   - Update for 1.4.2... NOT compatible with cb 1.3! - Added Warlock level2. Fires wither skulls. be sure to update your config.yml to support them. - Added many default mob attacks. Blazes, enderdragons and ghasts shoot fireballs. Withers shoot wither skulls. Snowmen throw snowballs. Witches throw harm potions. Skeletons shoot arrows. Creepers explode.   - Some of this is not working 100%. Creepers may not respawn correctly and skeletons are not currently 'equippable' - Fix named players on the ignore list.   **v. 1.2** 10/24/2012   - All toggleable options (invincible, drops, retaliate, criticals) can be explicitly set via /sentry [option] true/false - The FriendlyFire option has been removed totally, sentries will never deal damage to or receive damage from bodyguard owners or other bodyguards of that owner. (which was the default behavior anyway) - Fix elemental immunity when Invincible was also set. - Changing a Sentry's weapon will cause it to switch attack types immediately instead of on the next target. - DIE command will now properly honor the setting of RESPAWN, DROPS and DieLikePlayers. - Fixed drops not working if RESPAWN was set to -1.   **v. 1.1.4** 10/15/2012   - Critical hit chances and messages can now be configured or disabled in the [config.yml](https://wiki.citizensnpcs.co/Sentry/Configuration "Sentry/Configuration"). Please update your config.yml or criticals will not work at all. - Note that as of citizens2 build 465 all mob types can attack. All hail our new sheep overlords.   **v. 1.1.3** 10/15/2012   - Fix death trigger not going off if respawn set to -1. - Added support for SimpleClans. Use the CLAN: target or ignore. - Added Npcdeathowner Trigger. This denizen trigger runs when the sentry-denizen dies using its OWNER as the target player.   **v. 1.1.2** 10/14/2012   - Fix NPCDeath trigger. Preliminary code in place to separate out death trigger to optionally run script vs NPC owner instead of killers.   **v. 1.1.1** 10/12/2012   - Bodyguards who have lost their owner will not take damage or engage in combat until the owner returns/logs in. - Stray sentry projectiles should not harm invulnerable basic NPCs. - Lots more optimizations for target finding. If you still experience low TPS with sentry you will have to increase the LogicTicks in the config.yml. If you can profile the server and let me know what exactly is causing the problem that would help. - Small fix with pathfinding ranges.   **v. 1.1** 10/10/2012  Note that this update adds several new items to the config.yml. These will not be added automatically. See the [Configuration](https://wiki.citizensnpcs.co/Sentry/Configuration "Sentry/Configuration") page for new items.   - Several changes aimed at increasing performance:   - - Target checking code has been reworked to make less pointless calls if the Sentry isn't set to target a certain category. The biggest culprit, I think, was some permissions plugins are VERY slow at returning the groups information. Sentries will now only query groups if they have a GROUP: target or ignore set. Same for Towny, Factions, War, and EVENT: targets.     - Also added a option in the config.yml to specify the frequency that Sentries look for targets. Default is 10 ticks (twice per second). increasing this number would decrease server load but also make sentries less responsive and slow the maximum firing rate. - Added Stormcaller Level 3. These crazed wizards call forth lightning so powerful it instantly vaporizes anything it touches, even those things otherwise immune to damage. (hint: creative-mode players) - Now parses '&' as a valid color character in warning and greeting messages. Changed default messages to red/green. - Added options in the config.yml to support 'extended' armors. Also allows disabling specific armor types. Only works with /sentry equip (not /npc equip)   **v. 1.0.3** 10/2/2012   - Fix copied Sentries' target/ignore lists being 'linked' to each other. Probably wont fix existing sentries, only newly copied ones. To fix existing Sentries open the citizens saves.yml and delete the [YAML anchors and references](http://en.wikipedia.org/wiki/YAML#References) on the Targets: and Ignores: nodes on each Sentry.   **v. 1.0.2** 9/28/2012   - Fix towny/factions/war support.   **v. 1.0.1** 9/27/2012   - Fix Witchdoctors (they got drunk and lost their recipe book, we found it though) - Switch to new default teleport action, should fix server hangs near ladders and waterfalls.   **v. 1.0 Release!** 9/21/2012   - Workaround to allow bodyguards to cross worlds. - Workaround for weapons breaking. - Maybe fix server crash teleporting around ladders. - I'm pretty happy with the feature list and stability of Sentry at this point, so this is 1.0. There's a few things still not working (like speed) but these are not fixable with Sentry and should be addressed in future builds of Citizens2.   **v. 0.9.9.2 beta** 9/20/2012   - Introducing the 667th Brigade: the **Warlocks!**   - These artisans of ancient arcane arts prefer a solitary lifestyle deep in The End. Probably because they smell bad. Recently several of their number have come to the mortal realm and SentryCorps has integrated them. Rumor is more powerful Warlocks may be on their way as well!.   - Be sure and add the Warlocks to your [config.yml](#Configuration) to enable this new attack type. - Fixed lvl1 pyromancers' over-zealous use of actual fire. - Other minor bugfixes.   **v. 0.9.9.1 beta** 9/17/2012   - **War** support. use the TEAM: target to automatically attack War players. - Fix item drops - Added server-wide option to make Sentries 'die' like they used to pre v0.9.5. false by default. - Added server-wide option to set the amount of EXP sentries drop on death if Drops is turned on. (yea yea.. you want it per sentry.. I know)   **v. 0.9.9 beta** 9/15/2012   - Added command: equip - Added targets: event:pvnpc, event:pvsentry - Changed some logic regarding pvp:   - Bodyguards should now honor pvp-protected areas, they will not take or deal damage to players or retaliate when left-clicked in a no-pvp zone. This ONLY applies to bodyguards, lookout-type sentries can still perform their duties in pvp-protected areas. You should still not bring a player-hostile bodyguard into a pvp-protected area.. it will run away and annoy people.   - All invincible sentries will not retaliate, no blood no foul. - Fixed config bug for default strength and pyro3   **v. 0.9.8.1 beta** 9/13/2012  Configuration is here!  Sentry now has a config.yml! You can:   - Set default stats/options/targets/texts for new Sentries. - Customize the item that each type of sentry uses (matches only ID for now, id:data.. soon). Can also disable certain Sentry types. - Add Armor, Strength, and Speed buffs to various armor and weapon types. So your players can buff up their sentry without access to /sentry stat commands! - Apply ANY potion effect(s) to ANY weapon sentries use!   See [Configuration](https://wiki.citizensnpcs.co/Sentry/Configuration "Sentry/Configuration") Once the bugs are worked out of this new stuff. Sentry will be released as 1.0.  **v. 0.9.7 beta** 9/11/2012   - The Peacekeepers have arrived! Give your sentry the event:pvp target and it will attack players that damage other players in its range. - Fix for Factions targets. - Fix for NPC targets. - Some fixes for bodyguards. They still don't like being taken across worlds. Think its a problem in citizens2 core.   **v. 0.9.6 beta** 9/10/2012   - ~~Known issue: changing worlds with a bodyguard will throw console errors. Working on fix.~~ - ~~Known issue: If there is a NPC on the server named after a Player, the player may be detected by the NPC: target.~~ - Split out NPC: targets from PLAYER: targets. - Sorta fix for Factions. - Minor bugfizes   **v. 0.9.5 beta** 9/8/2012   - Bodyguards will maintain a respectable distance. - Sentries will try to not stand in fire if they can help it, tends to void the warranty on their bowstrings.   **v. 0.9.4 beta** 9/7/2012   - Fixes for stuck actions, requires build **334** of citizens2 or higher. - Better help for targeting and guard commands.   **v. 0.9.3 beta** 9/2/2012   - Health is no longer limited to 20, should be able to use any value without external mods. - Implemented 'stuck' actions. Sentries should teleport to their guard targets or waypoints if they get stuck. If a Sentry gets stuck trying to path to a hostile target it will give up (and teleport back if it has waypoints) This functionality may still be a little buggy. - Fix mob aggression. - Stormcallers are now immune to all Lightning. Pyromancers are immune to all Fire. Witch Doctors are immune to all Poison.   **v. 0.9.2.1 beta** 9/2/2012   - Fix error from very fast healing - Fix error? from denizen hook.   **v. 0.9.2 beta** 9/2/2012   - Compatible with latest Citizens2   **v. 0.9.1 beta** 9/1/2012   - Through constant exposure Witch Doctors and lvl3 Pyromancers are no longer hurt by their own attacks (unless friendly fire in on.) - Accuracy improved for thrown potions.   **v. 0.9.0 beta** 8/31/2012   - For the first time in 100 years, the venerated Order of the Stormcallers has descended from their monastery on the top of Mt. Creeperhorn. They have come to join their brethren in SentryCorps and share a century's worth of arcane secrets to push back the tide of evil sweeping the land! See [#Equipment for details](#Equipment_for_details)   - Wielding potent scrolls and ancient tomes the Stormcallers bring forth lightning to smite their foes!   - The Stormcallers have taught the Pyromancer brigade to focus their chi and summon more powerful Fire!   - The SentryCorp Ice Magi have learned to infuse their balls of ice with freezing power!   - The secretive Witch Doctors have begun mass producing their potions of war. They make a mighty fine root beer float, too.   **v. 0.8.9 beta** 8/28/2012   - Fix target, ignore, guard, warning and greeting commands to properly handle spaces. - Change damage event priority: All sentries should deal and receive damage independent of any PVP protection plugins, since they are not, by definition, players.   **v. 0.8.8.2 beta** 8/27/2012   - Removed upper limit on respawn. - Removed upper limit on healrate to allow faster healing. Heal rate is still the number of seconds between heals of 1hp but all values between 0.0 and 1.0 are now valid. So a heal rate of 0.5 is 2hp per second. A healrate of 0.1 is 10hp per second. a healrate of 0.01 is 100hp per second. - Fixed error if vault not installed. - Made Vault registration delayed for compatibility with slow perms systems.   **v. 0.8.8.1 beta** 8/23/2012   - Sentries take less knockback based on armor. Also honor the .5 second invulnerable period after hits that other Minecraft entities enjoy. This should make fighting them much more difficult and rewarding. - Removed the upper limit on health, strength, and armor. This is for compatibility with other plugins. Vanilla craftbukkit users should still use 1-20 for health, and 0-10 for strength and armor.   **v. 0.8.8 beta** 8/21/2012   - Due to pending litigation, all Citizens SentryCorps personnel have been sent to Public Relations training. APPARENTLY some people were upset that Sentries were attacking people with no warning.   Added commands warningrange, warning, greeting  See <#Warn/Greet>   - Fixed sentries giving up on retaliation targets after a few seconds. - Other bugfixes.   **v. 0.8.7.1 beta** 8/20/2012   - Fix group ignores. - Added valid target: entity:all   **v. 0.8.7 beta** 8/20/2012   - Added command: ignore - Added target entity:owner   **v. 0.8.6 beta** 8/20/2012   - Added Target Reassessment   When Sentries have an active target, every few seconds they will glance over their shoulders at other possible targets and switch if one has gotten closer. Stab me in the back once, shame on you, stab me in the back twice, shame on me.   - Added Denizen Command: LIVE   **v. 0.8.5.1 beta** 8/19/2012   - Minor fixes to perms, info, debugging info.   **v. 0.8.5 beta** 8/17/2012   - Support for Factions. Use FACTION:FactionTag to target memebers of that faction. - Added Towny Nation support. Use NATION:NationName to target memebers of that Towny Nation.   **v. 0.8.4.1 beta** 8/16/2012   - Last-second heals will no longer allow a sentry to jump back into the fray after death, naked. - Sentries forget their target on death, shouldn't smack people nearby on respawn anymore.   **v. 0.8.4 beta** 8/15/2012   - ~~KNOWN ISSUE: Sentries with a single waypoint can cause VERY bad lag, either remove the single waypoint or make 2 waypoints until we can correct the issue.~~   Corrected in Citizens2 build #288   - ~~KNOWN ISSUE: Human-type NPCs cannot path up stairs or half-blocks~~   Corrected in Citizens2 build #291   - If a Sentry NPC is owned by 'server' anyone with the 'citizens.admin' permission can run sentry commands on it. (if they also have the required Sentry [permissions)](https://wiki.citizensnpcs.co/Sentry/Permissions "Sentry/Permissions")   **v. 0.8.3 beta** 8/15/2012   - Fix for group checking with some perms plugins. - Default pathfinding range much larger.   **v. 0.8.2 beta** 8/15/2012   - Sentries will now take most forms of environmental damage:   Armor will be applied against damage from Cacti and TNT.  Sentries do not drown or take fall damage (yet)  Sentries that die from the environment will still run [Scripted Death](https://wiki.citizensnpcs.co/Sentry/Sentry_and_Denizen#Scripted_Death "Sentry/Sentry and Denizen") scripts if at least one player directly damaged them.  **v. 0.8.1 beta** 8/14/2012   - Changed arrow-cleanup method. Should work better. - Small group permissions compatibility fix.   **v. 0.8.0 beta** 8/13/2012   - Built in [Towny](http://dev.bukkit.org/server-mods/towny-advanced/) support. (Thanks **TerraNetworkOrg**!)   Sentry does not require Towny, but if you use it you can add a "TOWN:TownName" target to your sentries and they will target players from that town.   - Added in a hack to periodically remove bugged arrows when no players are around. Hopefully this is temporary.   **v. 0.7.9.2 beta** 8/12/2012   - Fix Sentries not checking GROUP targets. - Checks for world groups first then global groups if no world groups found. Should be compatible with more perms systems. - Sentries will forget their attackers if they heal back to full health. (This only applies to [Scripted Deaths](https://wiki.citizensnpcs.co/Sentry/Sentry_and_Denizen#Scripted_Death "Sentry/Sentry and Denizen"))   **v. 0.7.9.1 beta** 8/12/2012   - Fix for doppelgangers on /citizens reload - Sentries set to not drop equipment also don't drop EXP.   **v. 0.7.9 beta** 8/11/2012   - Added animations to projectile shot and healing. Added sound effect to blocked hits. - Workaround for Ranged Sentries not pathing after respawn.   **v. 0.7.8.1 beta** 8/11/2012   - Fix for denizen change. Fixed 2 NPEs.   **v. 0.7.8 beta** 8/10/2012   - Full permissions system for each command in /sentry. See [Permissions](https://wiki.citizensnpcs.co/Sentry/Permissions "Sentry/Permissions")   **v. 0.7.7.1 beta** 8/10/2012   - Integration with [Denizen](https://wiki.citizensnpcs.co/Denizen "Denizen"). Now you can trigger scripts on a Sentry's death. Long, drawn-out, guilt-ridden death speeches are go. see [Sentry and Denizen](https://wiki.citizensnpcs.co/Sentry/Sentry_and_Denizen "Sentry/Sentry and Denizen") for more info. - Minor bugfixes.   **v. 0.7.6 beta** 8/8/2012   - Added command: healrate - Sentries can now heal back health over time.   **v. 0.7.5 beta** 8/7/2012   - Added command: spawn - All /sentry commands may now be run from the console. - Sentry damage is now independent of the weapon equipped. Damage is now equal to the sentry's Strength. The default for new Sentries is 1. If you already have Sentries created be sure to set the Strength, the old default was 0. - Lots of bugfixes to speed, pathing, guarding, damage, arrow physics.   **v. 0.7.4.5 beta** 8/7/2012   - Bugfixes all over. - Bodyguards will no longer take damage from other bodyguards guarding the same target. (unless friendly fire is on... and if FF and Retaliate are both on.. they will attack and kill each other (merc's have a temper.)) - Bodyguards are more persistent. If you get separated from your guard move within its Range and it should start following you again. **Remember where you parked your bodyguard!** - Known bugs: Sentries sometimes take multiple hits.. note sure if Sentry or Core C2 problem. Bodyguards may lose their target. - TO DO: keep bodyguards from trying to stand on top of you and each other.   **v. 0.7.4 beta** 8/6/2012   - ~~known bug: cannot target individual hostile monster types, will fix soon~~ - Added commands: respawn, guard, nightvision, friendlyfire. - Archers have gone back to basic training and can now shoot moving targets with deadly accuracy. - Arrows now a move little faster, archers have more range. - Sentries can be set to not see targets in dark conditions. Sneaking makes players harder to see. Thief missions Go! - Sentries can be set as bodyguards. (note this is not currently persistent and may have bugs)   **v. 0.7.3 beta** 8/4/2012   - Added command: attackrate - Pyromancer sentries no longer shoot themselves in the face. - Tweaked the projectile physics and firing system. - Respawn fix and other bugfixes.   **v. 0.7.2 beta** 8/4/2012   - Removed ignore-cone, All Sentries now use Line-Of-Sight to select targets. - Archers no longer stare at the spot of the last enemy. - Code re-arrange.   **v. 0.7.2 beta** 8/4/2012   - Added commands: range - Sentries ignore a cone of space directly below them. This is to stop archers from shooting at their feet. - Fixed sentries being unable to target some mobs such as ghasts. - Archers with targets out of range no longer drop arrows at their feet.   **v. 0.7.1 beta** 8/3/2012   - Added commands: info, armor, strength - All combat (ranged, player-npc, npc-npc, mob-npc) goes through the same calculations for armor, strength, and critical hits. - Sentry no longer creates a folder or config.yml. All options are stored within the Citizens saves.yml. - More bugfixes and cleanup.   **v. 0.7.0 beta** 8/2/2012   - MC 1.3.1 Compatible - Added commands: invincible, retaliate, drops, criticals - Added ability to shoot bows and projectiles. - Sentries respond to damage from arrows. - Lots of bugfixes and minor updates.   **v. 0.5.6 beta**   - Now working with the new builds of C2.   **v. 0.5.5 beta**   - Fixed bugs.   **v. 0.5 beta**   - Added the ability to specify targets. - Added the ability to set the Health and Speed of a Sentry. - 'Stuck' Sentries now respawn after a while. - Fixed the death handling. - Fixed Sentries remembering their guard location on a restart.   **v. 0.3 beta**   - Added ability to kill the NPCs. Swords kill faster. Built-in chance of criticals, etc. - Fixed targeting code, should be more efficient now. - Implemented respawning sequence. |  |

[![](https://wiki.citizensnpcs.co/images/8/87/ArchersLogo.png)](https://wiki.citizensnpcs.co/File:ArchersLogo.png)

The 14th Archer Brigade

## Installation

- Ensure the latest [[Citizens2](http://ci.citizensnpcs.co/job/Citizens2/)] is installed
- Download file. [See top of page](#top)
- Place Sentry.jar in your Plugins folder.
- Start Server

## Permissions

See [Sentry Permissions](https://wiki.citizensnpcs.co/Sentry/Permissions "Sentry/Permissions")

## Configuration

On first load Sentry will make config.yml in plugins/Sentry. This can be used to configure Sentry to your liking.
See [Configuration](https://wiki.citizensnpcs.co/Sentry/Configuration "Sentry/Configuration")

Sentry will only make this file if it cannot find it. So check the page above if anything new has been added.

## Commands

To view help:

:   **`/sentry help`**

To reload the config.yml:

:   **`/sentry reload`**

All /sentry commands below normally require a selected NPC. use /npc select # to do this. Alternatively you may use
`/sentry # [command]` 
to send a sentry command to a specified sentry without selecting it. # is the Sentry's npcid.

Example: `/sentry 3 add target entity:monster`  will add the monsters target to sentry with npcID 3.

### Creation

[![](https://wiki.citizensnpcs.co/images/1/1d/PyromancersLogo.png)](https://wiki.citizensnpcs.co/File:PyromancersLogo.png)

The Flaming 27th, Pyromancer Brigade

To create a sentry, use:

:   **`/npc create NPC Name`**
`:   /trait sentry`

:   or
:   **`/npc create NPC Name --trait sentry`**

To give your sentry a place or path to guard use:

:   **`/npc path`**

And use the [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints") editor.

To equip you Sentry with weapons and armor see <#Equipment>

If you would like the Sentry to respawn in a different place from where it was created. Move it using

:   **`/npc tphere`**

And then call

:   **`/sentry spawn`**

### Targets

Sentries have 2 lists: **Targets** and **Ignores**. These lists contain entities. Entities can be monsters, passive mobs, players, or player groups. Sentries look at all the possible entities they can see in their range, If it NOT on the **Ignores** list and IS on the **Targets** list, the Sentry will attack it. An entity cannot be seen if it is out of line-of-sight or if it is too dark for the Sentry's nightvision

- Melee Sentries will chase targets until the target is dead, has gotten out of range, or another valid target has gotten closer.
- Ranged Sentries do not follow targets, but will stay on their spot/path and fire at the target until it is dead, out of *projectile** range, or another valid target has gotten closer.

:   :   *Note that projectile range is not the same as range (detection range). Projectiles have a fixed range depending on their type. Archers, for example, have a range of about 50 blocks on flat ground. Elevated sentries can hit targets farther away. Sentries that throw things have shorter range.

To add a target:

:   **`/sentry target add [category:type]`**

To add an ignore:

:   **`/sentry ignore add [category:type]`**

**`[category:type]`** can be any of the following:

|  |  |
| --- | --- |
| entity:all | All living things. (adding this to the Ignore list is the same as leaving the Target list empty.) |
| entity:owner | The Sentry's npc Owner. |
| entity:TYPE | any [mob types](https://wiki.citizensnpcs.co/Types "Types") of TYPE |
| entity:monster | All hostile mobs |
| entity:player | All real players. |
| player:Name | The player with the name Name |
| entity:npc | All NPCs. |
| NPC:Name | The NPC named Name. |
| group:Name | All members of permissions group Name. NPCs can be added to permission groups. |
| team:Name | All members of scoreboard team Name. |
| town:Name | All members of [Towny](http://dev.bukkit.org/server-mods/towny-advanced/) town Name |
| nation:Name | All members of [Towny](http://dev.bukkit.org/server-mods/towny-advanced/) nation Name |
| nationenemies:Name | All members of [Towny](http://dev.bukkit.org/server-mods/towny-advanced/) nations that are declared as enemies of Name or have declared Name as an enemy. Only works as a Target, not as an Ignore. |
| faction:Name | All members of [Factions](http://dev.bukkit.org/server-mods/factions/) factiontag Name |
| factionenemies:Name | All members of [Factions](http://dev.bukkit.org/server-mods/factions/) that are currently enemies of Name. |
| warteam:Name | All members of [War](http://dev.bukkit.org/server-mods/war/) team Name |
| event:PvP | The sentry will attack any players that damage another player in range. |
| event:PvE | The sentry will attack any players that damage animals or mobs in range. |
| event:PvNPC | The sentry will attack any players that damage any NPC in range. |
| event:PvSentry | The sentry will attack any players that damage other Sentries in range. |

Examples:
This will make the Sentry attack all players except those in the Admin group

```
/sentry target add entity:player 
/sentry ignore add group:Admin
```

This will make the Sentry attack anything that moves.. except sheep and the player named Bob Johnson.

```
/sentry target add entity:all
/sentry ignore add entity:sheep
/sentry ignore add player:Bob Johnson
```

[![](https://wiki.citizensnpcs.co/images/0/09/StormcallersLogo.png)](https://wiki.citizensnpcs.co/File:StormcallersLogo.png)

The Order of Stormcallers, 99th Brigade

To remove a target:

:   **`/sentry target remove [entity]`**

To remove a ignore:

:   **`/sentry ignore remove [entity]`**

To view the target list:

:   **`/sentry target list`**

To view the ignore list:

:   **`/sentry ignore list`**

To clear the target list:

:   **`/sentry target clear`**

To clear the ignore list:

:   **`/sentry ignore clear`**

#### Warn/Greet

Sentries can optionally warn or greet Players that come nearby, letting the Player know if the Sentry is hostile or friendly. This is off by default. To turn it on set the WARNINGRANGE higher than 0. This is the number of blocks beyond the RANGE that the Sentry will look for Players to warn/greet. For example if the RANGE is 10 and the WARNINGRANGE is 5, Players 10-15 blocks away will be alerted to the Sentry's hostility.

The warning and greeting message can be customized for each Sentry.

To set the warning message:

:   **`/sentry warning 'New Warning Message'`**

To set the greeting message:

:   **`/sentry greeting 'New Greeting Message'`**

- <PLAYER> and <NPC> can be used in the message as a placeholder for the Player's name or Sentry's name.
- Setting either message to "" will disable that message.

### Guarding

Sentries have guarding 2 modes: Lookout and Bodyguard.

#### Lookouts

This is the default mode for a new Sentry. Lookouts will stand on a single waypoint or travel between waypoints at the default NPC speed. They will look for and engage any targets.

- If a lookout becomes 'stuck' it will abandon its target and teleport back to its waypoint(s).
- Lookouts should always be given waypoints, otherwise they will simply stop moving when their target dies. use **`/npc path`** to set one or more waypoints.
- Lookouts ignore PvP protection and will deal and receive damage in all cases.

To set the Sentry back to this mode if it has been changed:

:   **`/sentry guard`**

#### Bodyguards

Bodyguards will guard follow another living entity (their guard target). The guard target can be a player or another NPC. If a bodyguard is set to retaliate}, it will engage anything that attacks either its guard target or itself. It will also actively engage any targets that have been configured.

- Bodyguards will not deal damage to, or receive damage from, their guard target or any other bodyguards guarding that target.
- If a bodyguard becomes stuck it will teleport to its guard target after a few seconds.
- If the guard target is a player, and the player logs out, the bodyguard will remain where it is and will not take damage or engage in combat until the player comes back online and in range.
- Bodyguards will honor any PvP-protection that might be active in the current world or area. (can be changed in the Configuration)

To set a Sentry as a bodyguard for a target NPC or Player:

:   **`/sentry guard [Name]`**

- Notes:
  - [Name] is case-sensitive!
  - Named mobs must be within range of the NPC when set.
  - By default this command checks nearby entities for the specified name and if not found then checks the online player list. If this behavior is undesirable you can use `/sentry guard -p [Name]`  to only check the online player list or `/sentry guard -l [Name]`  to only check entities nearby the sentry.

[![](https://wiki.citizensnpcs.co/images/c/cd/WitchDoctors.png)](https://wiki.citizensnpcs.co/File:WitchDoctors.png)

9th Brigade. The Witch Doctors.

### Stats

Stats are Sentry settings that take a value and affect its performance.

To set a stat use:

:   **`/sentry [stat] [value]`**
:   `Example: /sentry armor 5`

To view the current value of a stat and get help:

:   **`/sentry [stat]`**
:   `Example: /sentry range`

To view all the Sentry's stats, as well as current target, status, and guard target, use:

:   **`/sentry info`**

| Stat | Default Value | Value Range | Notes |
| --- | --- | --- | --- |
| health | 20 | 1-2000000 | The number of hit points the Sentry has. Normal players have 20. |
| armor | 0 | 0-2000000 | This value is subtracted from all incoming damage. An armor of 10 makes the Sentry very hard to hurt. Armor items equipped on the Sentry have no effect on combat. |
| strength | 1 | 0-2000000 | This is the damage the sentry does with each hit, regardless of weapon (or object) held. |
| range | 10 | 1-100 | This is the **detection** range for the Sentry. High values may affect server performance. This is not the same as the projectile range, which is dictated by projectile type and the Sentry's elevation relative to the target. |
| speed | 1.0 | 0.0-1.5 | This is the speed at which a sentry will move while pursuing a target. To set the normal path speed use /npc speed. |
| attackrate | 2.0 | 0.0-30.0 | This is the number of seconds between projectile shots and has no effect if the Sentry uses a melee weapon. The minimum internal rate is 0.5 (twice a second). |
| healrate | 0.0 | 0.0-300.0 | This is the number of seconds between heals of 1 point, values less than 1.0 are acceptable. Set to 0 to turn off healing. |
| nightvision | 16 | 0-16 | This is how well the Sentry can see potential targets in the dark. A value of 16 means the sentry can see perfectly all the time. A value of 12 means a target is invisible below light level 4 (16-12) . A value of 6 means a target is invisible below light level 10 (16-6), etc. If the target is a Player and that player is sneaking, its effective light light level is cut in half, making it harder for the sentry to detect. |
| respawn | 10 | -1-2000000 | When the sentry dies, this is the number of seconds after which it will respawn. Set to 0 to prevent normal respawn. Set to -1 and the Sentry will not respawn and be **permanently** destroyed on death. |
| warningrange | 0 | 0-50 | The number of blocks beyond range the Sentry will look for Players to warn or greet. Set to 0 to disable warn/greet. |
| follow | 4 | 0-32 | The number of blocks a bodyguard will follow behind its guard target. |

### Options

Options are sentry settings that can be toggled on and off and affect its behavior.

:   **`/sentry [option]`**
:   `Example: /sentry invincible`

You can also explicitly set an option using true or false

:   `Example: /sentry invincible false`

To view all the Sentry's stats, options, current target, status, and guard target, use:

:   **`/sentry info`**

| Option | Default Value | Notes |
| --- | --- | --- |
| drops | False | If this is True the Sentry will drop his equipment and some EXP on death. |
| killdrops | True | If this is False any mobs the Sentry kills will not drop items or EXP. |
| invincible | False | If this is True the Sentry will not take any damage, be knocked back, or show a 'hurt' flash. |
| retaliate | True | If this is True, the Sentry will attack to any living thing that attacks it. If the Sentry is acting as a bodyguard, it will also attack any living thing that attacks its guard target. |
| criticals | True | If this is true the Sentry will take critical hits and misses. If False, the normal damage is always applied. |
| mount | False | Whether or not the Sentry is mounted. See <#Mounts> |
| targetable | True | Whether or not the Sentry is attacked by nearby hostile mobs. |

## Combat

Sentries can engage in rewarding combat with players, monsters, and even each other!

### Equipment

Equipment can be added to Sentries using the Citizens `/npc equip` editor. or the `/sentry equip [item|none]` command. What's the difference?

- /npc equip
  - Can only be used by in-game players
  - Takes items from the player and gives it to the NPC
  - Drops all items when removed
- /sentry equip [item|none]
  - Can be used from the console/scripts
  - Does not require the item
  - Does not drop anything on removal.

The choice is yours which you use/allow.

By default, equipped armor is just cosmetic. armor determines the damage reduction from attacks. Armor buffs can be configured for specific types of armor in the [Configuration](https://wiki.citizensnpcs.co/Sentry/Configuration "Sentry/Configuration").

The item a Sentry holds in its hand determines its attack type, but the amount of damage the Sentry does is determined by its strength
Strength buffs for specific weapon types can be set in [Configuration](https://wiki.citizensnpcs.co/Sentry/Configuration "Sentry/Configuration"). By default no weapons add strength.

The following items are usable by Sentries (these can be changed in the [Configuration](https://wiki.citizensnpcs.co/Sentry/Configuration "Sentry/Configuration")):

| Default Item | Type | Notes |
| --- | --- | --- |
| BOW | Archer | The 14th Archer Brigade ("Hawkeyes") of SentryCorps wield long bows and razor arrows. They can hit a chicken square in the nuggets from 50 meters on flat ground. |
| REDSTONE_TORCH_ON | Pyromancer I | The entry-level members of the 27th Pyromancer Brigade shoot small, non-incendiary fireballs from their wands. |
| TORCH | Pyromancer II | The elite of the Flaming 27th, these wizards shoot fireballs that set the land on fire. |
| BLAZE_ROD | Pyromancer III | Spoken of in only hushed whispers, this little-known squad of the 27th has learned to fire large, explosive fireballs. That's a nice everything you have there. |
| SNOW_BALL | Ice Magi | The frosty brethren of the 88th Ice Magi Brigade ("Snowmen") throw snowballs which slow enemies on contract. Snowballs have a range of about 25 blocks on flat ground. |
| EGG | Bombardiers | The 3rd Brigade of Ovarian Bombardiers gets few recruits. Perhaps its the giant chicken suits they have to wear. Eggs have a range of about 25 blocks on flat ground. |
| POTION | Witch Doctor | When not drunk on their own noxious brews, the 9th Witch Doctor Brigade can turn the tide of battle with a single potion. Potions have a range of about 25 blocks on flat ground. The Sentry will throw a splash version of whatever potion type it is equipped with. |
| PAPER | Stormcaller I | The magic incantation written on their scrolls allows members of the 99th Stormcallers to strike single targets with bolts of electricity. |
| BOOK | Stormcaller II | The elite of the 99th can call forth powerful lightning from the sky to smite multiple foes using tomes of untold power. This lightning's damage is atmospheric and therefore is not affected by the Sentry's strength. |
| BOOK_AND_QUILL | Stormcaller III | Few dare call upon the services of the 3rd-tier Stormcaller. Their mighty bolts instantly kill any living thing they touch regardless of health, armor, or play mode; Griefers beware! |
| ENDER_PEARL | Warlock I | The lowest tier of the 667th Warlocks. These sorcerers imbue their magic crystals with the kinetic power of the endermen, flinging their targets high into the air. Remember: it's not the fall that kills you, it's the sudden stop at the end. |
| SKULL_ITEM | Warlock II | The mid-range warlock shoots black explosive wither skulls at the enemy. |
| Anything else | Brawler | All armies need their meat-shields. the 1st Battalion is SentryCorps'. Armed with swords, axes, picks, shovels, rocks, bricks, or even fish, the brawlers take the fight to the enemy, hand to hand, using whatever they can find. |

### Dealing Damage

The damage dealt by a Sentry when attacking a target is equal to the sentry's strength.

Typically players have 20 health. By default a Sentry has 1 strength and therefore does 1 damage.

### Receiving Damage

Sentries can receive damage from any source, just like a monster. If the Sentry is set to retaliate, it will target any living entity that attacks it, ignoring any current target.

If the Sentry is set to invincible, it takes NO damage or knockback at all!

If the Sentry has criticals turned on, any incoming damage is randomized resulting in a normal hit, a miss, or one of several degrees of critical hit. If the attacker is a player, a message is shown based on the type of hit.

If the Sentry has armor > 0 the damage will be reduced by the amount of armor. If the damage is reduced to nothing, the attack results in a block. Blocked hits cause no damage but DO cause knockback!

### Death

If the Sentry's health drops to 0. It dies.

If the Sentry is set to drops on death, when it dies it drops its equipment like a normal monster. Watch out for farmers!

After the respawn delay (default is 10 seconds) the Sentry will respawn. If therespawn is set to 0, the Sentry must be re spawned manually.

Lookouts will respawn at their spawn location, by default this is where they were created. This can be changed with  */sentry spawn*

Bodyguards will respawn near their guard target.

## Mounts

Sentries can be mounted and also used as mounts.

### Mounted Sentries

To make a Sentry mounted use the command */sentry mount*. This command creates a new, permanant horse-type NPC for the sentry to ride. This NPC can be edited in any way you see fit.

- The mount is a horse by default but can be changed to any mob type with the */npc type* command.
- While attacking, mounted Sentries move at double the rider's speed stat. (*/sentry speed*)
- While patrolling or following, mounted Sentries move at double the rider's */npc speed*
- To make a Mounted Sentry patrol give waypoints to the *mount*
- The mount can be be killed and the sentry will continue on foot, however if the Sentry is killed while mounted the mount also dies.
- Mounts respawn with their Sentry.

### Sentries as mounts

- To use a Horse-Sentry as a player's mount it must be that player's bodyguard. (*/sentry guard player*)
- Horse sentries can be ridden normally, but if given targets they may ignore your input and attack on their own.

## Advanced Usage

For combining Sentry and Denizen for truly powerful interactions see [Sentry And Denizen](https://wiki.citizensnpcs.co/Sentry/Sentry_and_Denizen "Sentry/Sentry and Denizen")

## Known Issues

- The Modifyworld plugin that comes with PEX is known to cause '0 damage' issues and prevent sentry mounting.
- Turning PvP off in the server.config will prevent attacking NPCs. This is also true for pvp settings in MultiVerse.
- Heroes does all kinds of funny things to player-type Sentries.
- Using commands on a Sentry NPC while it is dead may cause errors. (/npc spawn is safe)
- Putting a saddle on a Sentry's mount will make it stop moving.

## Planned Additions

- Match weapon and armor buffs to item/data/enchantment instead of just item (for all you spout people)

## Suggestions

Suggestions are, of course, always welcome!

- Visit us in #citizens on [EsperNet](http://webchat.esper.net/?channels=citizens).
- Bugs and suggestions can also be posted [[Here](https://github.com/jrbudda/Sentry/issues)]

[Donate to jrbudda](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=JVBJLN5HJJS52&lc=US&item_name=jrbudda&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted)

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
