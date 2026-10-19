For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

Interact Script Commands are used to make the Denizen perform actions in an Interact Script. They are written in a [YAML](https://wiki.citizensnpcs.co/YAML "YAML") sequence under the Script node of an [Interact Trigger](https://wiki.citizensnpcs.co/index.php?title=Denizen/Interact_Scripts/Triggers&action=edit&redlink=1 "Denizen/Interact Scripts/Triggers (page does not exist)"). A single entry in the sequence contains a Command and Modifiers. Some commands have no available modifiers.

### Syntax

Syntax is very important for proper execution.

- Placing a caret ^ in front of the command name causes that command to ignore the normal 0.5 second delay between commands.
- The command must be upper-case (i.e CHAT not chat)
- Modifiers are not case sensitive.
- Modifiers in **[Brackets]** are **required** for the command to execute. [A or B] means *either* A or B is required.
- Modifiers in **(Parentheses)** are optional, and generally change the default behavior of the command.
- Modifiers that take a value are of the form MODIFIER:VALUE.
  - If the VALUE of the modifier contains a space, such as in the case of a NPC or script name, the whole modifier must be put in quotes.

:   :   Example: `- TELEPORT BOOKMARK:Bob:Bobshouse` is okay, but `- TELEPORT 'BOOKMARK:Bob Jones:Bobshouse'` requires the quotes to function properly.

Example:

```
Some Trigger:
  Script:
  - COMMAND1 MODIFIER1 MODIFIER2:VALUE
  - COMMAND2 'MODIFIER1:Value With Spaces'
  - ^COMMAND3 'This will run instantly after COMMAND2'
```

### List of Commands

#### Script Flow

These commands have no external effect on the world, but can control the flow of scripts within Denizen. Though not required, and with the exception of WAIT, it is generally recommended to run these as Instant Commands to ensure smooth Script feedback to players.

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>COOLDOWN
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[# or DURATION:#] (GLOBAL) ('SCRIPT:Name of Script')
</th></tr>
<tr>
<td colspan="3">Sets a cooldown period for this script. Defaults to the currently running script and the interacting player. Until the script has cooled down, it will not be selected to run again. Requires a number of seconds to be specified with or without the DURATION: modifier name.
<p>Modifiers:
</p>
<ul><li>GLOBAL makes the script unavailable to everyone, instead of just the interacting player.</li>
<li>SCRIPT: Sets the cooldown a different script.</li></ul>
<p><b>Example Usages</b>
</p>
<pre>- COOLDOWN 60
- COOLDOWN GLOBAL 100
- COOLDOWN 'SCRIPT:A Different Script' 600
- COOLDOWN DURATION:15
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>DISENGAGE
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(NPCID:#)
</th></tr>
<tr>
<td colspan="3"><p>Allowed an <tt>ENGAGED</tt> Denizen to be interacted with again, the counterpart to the <tt>ENGAGE</tt> command. Can also specify the NPCID of a different Denizen</p>
<p><b>Example Usages</b>
</p>
<pre>- ENGAGE
- (Other Commands)
- DISENGAGE

- DISENGAGE NPCID:7
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>ENGAGE
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(DURATION:#) (NPCID:#)
</th></tr>
<tr>
<td colspan="3"><p>Blocks player interaction from triggering the NPC. This may be useful if a long script required the player to listen or watch a series of events and you didn't want the Player to be able to interact while these commands were being taken out. Use with either a <tt>DURATION</tt> or <tt>DISENGAGE</tt>. <tt>DURATION</tt> will automatically <tt>DISENGAGE</tt> after the specified amount of seconds. If no <code>NPCID</code> is included, the Denizen triggered is used. Remember: While <tt>ENGAGED</tt>, no scripts will trigger, so be diligent in using!</p>
<p><b>Example Usages</b>
</p>
<pre>- ENGAGE
- (Other Commands)
- DISENGAGE

- ENGAGE DURATION:12 
- ENGAGE NPCID:2</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>FAIL
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">('SCRIPT:Name of Script')
</th></tr>
<tr>
<td colspan="3"><p>Marks a script as 'Failed' to check against with the <tt>FAILED</tt> requirement. This is identical to the <tt>FINISH</tt> command, except keeps track of 'fails' instead. Again, this is kind of like a built-in flag for scripts, and acts much like a Counter, ie. You can <tt>FAIL</tt> a script multiple times and it will keep track of the total number, unless <tt>RESET</tt>. Note: A script can be both 'finished' and 'failed', the two commands work independently.</p>
<p><b>Example Usages</b>
</p>
<pre>- FAIL
- FAIL 'SCRIPT:Magic Feathers'</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>FINISH
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">('SCRIPT:Name of Script')
</th></tr>
<tr>
<td colspan="3"><p>Marks a script as 'Finished' to check against with the <tt>FINISHED</tt> requirement. This is kind of like a built-in flag for scripts, and acts much like a Counter, ie. You can <tt>FINISH</tt> a script multiple times and it will keep track of the total number, unless <tt>RESET</tt>.</p>
<p><b>Example Usages</b>
</p>
<pre>- FINISH
- FINISH 'SCRIPT:Another Script'</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>FLAG
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['Flag Name' or 'Flag Name:Flag Value' or 'Flag Name:++' or 'Flag Name:--'] (PLAYER or DENIZEN or GLOBAL) (DURATION:#)
</th></tr>
<tr>
<td colspan="3"><p>Requires one of the above arguments. <tt>FLAG</tt> stores variables, or 'flags', by default to a Player. This can be used to keep track of information that can be check against with the FLAGGED requirement. Usage of the command is easy, and can be used in 3 different ways. A Boolean (true/false) value can be set with only a flag name. If set, the value is <tt>TRUE</tt>. When <tt>RESET</tt>, it is <tt>FALSE</tt>. <tt>FLAG</tt> can also set Integer (or number) variables, and easily increment or decrease them with the use of the <tt>++</tt> and <tt>--</tt> arguments accordingly. The command can also store a String value, see the example below. Using a <tt>DURATION</tt> will revert the value of the flag to the previous value, if during the duration the flag has not changed. Using the PLAYER modifier will set the flag on the Player (which is the default behavior). Using the DENIZEN modifier will set a flag on the Denizen instead of the Player. Using the GLOBAL modifier will set a flag independent of a Player or Denizen.</p>
<p><b>Example Usages</b>
</p>
<pre>- FLAG 'Sample Boolean Flag'
- FLAG Alignment:++
- FLAG Alignment:--
- FLAG 'Active Item:60 Feathers'
- FLAG WorldBossDead GLOBAL
- FLAG HasHealingFlag DURATION:180
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>IF
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(EXACTLY) (PLAYER or DENIZEN or GLOBAL) (-)[FLAG:Name or FLAG:Name:Value] (IS_NUMBER) ['SCRIPT:Script Run When Condition Met'] (QUEUE:TRIGGER or QUEUE:TASK) (APPEND) (ELSE 'SCRIPT:Script Run When Condition Not Met')
</th></tr>
<tr>
<td colspan="3">Checks the value of a FLAG and runs a TASK script if the condition is met. By default the TASK script will run before the interact script continues.
<p>Modifiers:
</p>
<ul><li>EXACTLY - For integer flags, the IF condition is met only if the value matches exactly. By default, the condition is met if the flag's value is greater than or equal to the value it is checked against, i.e. IF 'FLAG:AGE:13' will pass for any AGE that is at least 13, but IF EXACTLY 'FLAG:AGE:13' will only pass if the AGE is 13.</li>
<li>PLAYER - Check a flag set on this Player (which is the default behavior)</li>
<li>DENIZEN - Check a DENIZEN flag set on the Denizen itself instead of a flag on this Player</li>
<li>GLOBAL - Check a GLOBAL flag instead of a flag on this Player</li>
<li>IS_NUMBER - The IF condition is met only if the value of the flag is an integer or double.</li>
<li>APPEND - Runs the TASK after this script completes, instead of before the next command.</li>
<li>QUEUE - Specify which queue to run the commands in, defaults to the executing queue type.</li>
<li>ELSE - Choose a TASK script to run when the IF condition is not met.</li></ul>
<p><b>Example Usages</b>
</p>
<pre>- IF FLAG:BossDead SCRIPT:Reward APPEND
- IF EXACTLY FLAG:Stage:4 SCRIPT:Stage4Instructions
- IF 'FLAG:AGE:13' 'SCRIPT:Meets Minimum Age' ELSE 'SCRIPT:Does Not Meet Minimum Age'
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>RANDOM
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[#]
</th></tr>
<tr>
<td colspan="3">Selects a single command to run from the next # lines in the script and discards the rest.
<p><b>Example Usages</b>
</p>
<pre>- CHAT "I'm going to say the name of an animal"
- RANDOM 3
- CHAT "Cow"
- CHAT "Zebra"
- CHAT "Elephant"
- CHAT "Wasn't that fun?"
</pre>
</td></tr></tbody></table>

#### Server

<table align="left" class="wikitable collapsible collapsed" style="background:aliceblue;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>EXECUTE
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[ASPLAYER or ASSERVER or ASNPC] ["command and arguments"]
</th></tr>
<tr>
<td colspan="3"><p>Runs a Minecraft/Bukkit command. Specifying <tt>ASPLAYER, ASSERVER, or ASNPC</tt> defines how the command should be executed. ASNPC will run the command as the Denizen interacting, temporarily granting OP privileges, if the Denizen NPC is a Human-type NPC. Running ASSERVER will run as a console command, and running ASPLAYER will simply run the command as the Player. When specifying the command and arguments, it is not necessary to use the '/' that is generally used when running commands in-game. You may also use &lt;PLAYER&gt;, &lt;WORLD&gt;, or &lt;NPCID&gt; as variables inside the command arguments.</p>
<p><b>Example Usages</b>
</p>
<pre>EXECUTE ASSERVER 'gamemode &lt;PLAYER&gt; 2'
EXECUTE ASNPC 'toggledownfall'
EXECUTE ASPLAYER 'spawn'</pre>
</td></tr></tbody></table>

#### Speech

These commands show some text to the player interacting, and usually to bystanders around. Text commands also have some auto-formatting, such as making sure no words will be cut off on long messages, and applying color codes. See: [Denizen Color Codes](https://wiki.citizensnpcs.co/Color_Codes "Color Codes"). Formatting for how NPCs and Players talk can be customized in the [Denizen/config.yml](https://wiki.citizensnpcs.co/index.php?title=Denizen/config.yml&action=edit&redlink=1 "Denizen/config.yml (page does not exist)").

- All Speech commands **require quotes** (single (' ') or double (" ")) around the text. If your text has an apostrophe (') in it, you **MUST** use double quotes (" ")!!

There are various placeholders you can use to fill in specific information. The basic ones are:

- <NPC> - The Denizens's name.
- <PLAYER> - The interacting Player's name
- <DISPLAYNAME> - The interacting Player's display name
- <HEALTH> - The interacting Player's heath
- <WORLD> - The name of the Denizen's world

If you use the NOPLAYER modifier on a text command the <PLAYER>, <DISPLAYNAME> and <HEALTH> tags are not available.

A list of all available placeholders can be found in [Replaceables](https://wiki.citizensnpcs.co/Replaceables "Replaceables").

<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>ANNOUNCE 
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['The text to announce.']
</th></tr>
<tr>
<td colspan="3">Sends the text as a sever announcement to all players, regardless of their place in the world. Could be especially useful for any kind of administration script.
<p><b>Example Usages</b>
</p>
<pre>- ANNOUNCE "&lt;PLAYER&gt; has found a secret!"
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>CHAT
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">["The text to chat."] (NPCID:#) (NOPLAYER)
</th></tr>
<tr>
<td colspan="3">Makes the Denizen talk to the player. This is the standard chat mechanism in Denizen. You can also change the NPC doing the talking by specifying a Denizen's C2 NPCID. If you would rather the Denizen NPC not speak to the Player directly, use the <tt>NOPLAYER</tt> argument.
<p><b>Example Usages</b>
</p>
<pre>- CHAT NOPLAYER "Here ye, hear ye!"
- CHAT "Hello there, children!"
- CHAT NPCID:6 'I only supply tools to builders!'
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>NARRATE
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['The text to narrate.']
</th></tr>
<tr>
<td colspan="3">Makes a message appear to player without sender information.
<p><b>Example Usages</b>
</p>
<pre>- NARRATE "There is a small mailbox here."
</pre>
</td></tr></tbody></table>

#### Denizen Interaction

Denizen interaction commands are meant to help bring your Denizen to life by allowing fine control of movement and actions during scripts. These are not meant for making the Denizen do continuous movement and actions, that should instead be done via [Activities](https://wiki.citizensnpcs.co/index.php?title=Denizen/Activity_Scripts/Activities&action=edit&redlink=1 "Denizen/Activity Scripts/Activities (page does not exist)").

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>PAUSE
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(DURATION:#)
</th></tr>
<tr>
<td colspan="3">Causes the Denizen to stop any pathing or activities. Useful for keeping it in place during an interaction.
<p>Modifiers:
</p>
<ul><li>DURATION:</li></ul>
<dl><dd><dl><dd>Automatically RESUME after the specified number of seconds.</dd></dl></dd></dl>
<p><b>Example Usages</b>
</p>
<pre>- PAUSE
- PAUSE DURATION:30
</pre>
</td></tr></tbody></table>

#### World Interaction

<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>DROP
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[ID or ID:Data or MATERIAL or MATERIAL:Data or XP] (QTY:#) (BOOKMARK:LocationBookmark)
</th></tr>
<tr>
<td colspan="3">Drop an item at the Denizen's location, or at a location bookmark if one is specified.
<p><b>Example Usages</b>
</p>
<pre>- DROP DIAMOND QTY:3
- DROP 18:3 QTY:1 BOOKMARK:LargeTree
- DROP XP QTY:10
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>LISTEN KILL
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[TYPE:GROUP or TYPE:PLAYER or TYPE:ENTITY or TYPE:NPC] [NAME:Name or NPCID:#] (QTY:#) [SCRIPT:Task Script] (ID:Name)
</th></tr>
<tr>
<td colspan="3">This command starts the Denizen listening for the player to kill the specified number of specified targets, then runs a task script. Use the NAME:Name modifier when specifying a group name, player name, or <a href="https://wiki.citizensnpcs.co/Types" title="Types">entity type</a> (like 'ZOMBIE'). Use NPCID:# modifier when using TYPE:NPC.
<p>Optional Modifiers:
</p>
<ul><li>QTY: - The number things the player must kill before the script is run.</li>
<li>REGION: - The World Guard region the player must be in for the kill to count.</li></ul>
<p><b>Example Usages</b>
</p>
<pre>- LISTEN KILL TYPE:ENTITY NAME:ZOMBIE QTY:5 SCRIPT:ZombieReward
- LISTEN KILL ID:BossListener TYPE:NPC NPCID:12 'SCRIPT:Kill Boss Reward'
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>LISTEN BLOCK
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[TYPE:BREAK or TYPE:BUILD or TYPE:COLLECT] (QTY:#) [BLOCKS:Item Names] (REGION:WorldGuardRegion) [SCRIPT:Task Script] [ID:Name]
</th></tr>
<tr>
<td colspan="3">This command starts the Denizen listening for the player to interact with a given number of blocks, then runs a task scripts.
<p>Optional Modifiers:
</p>
<ul><li>QTY: - The number things the player must 'do' to finish, default 1.</li>
<li>REGION: - The World Guard region the player must be in for the interaction to count.</li></ul>
<p><b>Example Usages</b>
</p>
<pre>- LISTEN BLOCK TYPE:BREAK BLOCKS:sand|stone|stonebrick QTY:5 SCRIPT:BlockFinished
- LISTEN BLOCK ID:BuildListner TYPE:BUILD 'SCRIPT:Kill Boss Reward' REGION:KillRegion
</pre>
</td></tr></tbody></table>

|  | SWITCH | [LOCATION:x,y,z,world] (STATE:ON |
| --- | --- | --- |
| OFF | | |

#### Player Interaction

These commands default to affecting the interacting player. Most have modifiers to affect the executing Denizen instead.

<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>CAST
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[SpellName] (DURATION:#) (POWER:#) (NPC:#) (PLAYER:PlayerName)
</th></tr>
<tr>
<td colspan="3">Gives the specified target a potion effect.  <a href="https://wiki.citizensnpcs.co/Alchemist#Valid_Effects" title="Alchemist"> Valid potion names are the same as the Alchemist's.</a>
<p>Modifiers:
</p>
<ul><li>DURATION:#</li></ul>
<dl><dd><dl><dd>The effect duration, in seconds. Default is 60.</dd></dl></dd></dl>
<ul><li>POWER:#</li></ul>
<dl><dd><dl><dd>The level of the effect, usually 1-5. Default is 1.</dd></dl></dd></dl>
<ul><li>NPC:#</li></ul>
<dl><dd><dl><dd>The NPC to cast the effect on, instead of the interacting player. Specify with the NPC id.</dd></dl></dd></dl>
<ul><li>PLAYER:PlayerName</li></ul>
<dl><dd><dl><dd>The Player to cast the effect on, instead of the interacting player.</dd></dl></dd></dl>
<p><b>Example Usages</b>
</p>
<pre>- CAST SPELL:confusion DURATION:300 POWER:3
- CAST SPELL:speed
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>FEED
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(AMOUNT:#)
</th></tr>
<tr>
<td colspan="3">Feeds the interacting player. Provides food and saturation.
<p>Modifiers:
AMOUNT: The amount to feed. Default is 20.
<b>Example Usages</b>
</p>
<pre>- FEED
- FEED 5
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>HEAL
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(DENIZEN) (AMOUNT:#)
</th></tr>
<tr>
<td colspan="3">Heals the interacting player.
<p>Modifiers:
</p>
<ul><li>DENIZEN</li></ul>
<dl><dd><dl><dd>Heals the Denizen instead of the player.</dd></dl></dd></dl>
<ul><li>AMOUNT:</li></ul>
<dl><dd><dl><dd>The amount to heal, will not heal beyond the maximum. Defaults to a full heal if not specified.</dd></dl></dd></dl>
<p><b>Example Usages</b>
</p>
<pre>- HEAL
- HEAL DENIZEN AMOUNT:1
</pre>
</td></tr></tbody></table>
