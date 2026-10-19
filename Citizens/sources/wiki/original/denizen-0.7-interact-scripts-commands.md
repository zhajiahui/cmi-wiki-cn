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
<p>CANCELTASK
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['SCRIPT:Name of Script']
</th></tr>
<tr>
<td colspan="3">Cancels a task that has been scheduled for the interacting player using RUNTASK DELAY
<p><b>Example Usages</b>
</p>
<pre>- CANCELTASK SCRIPT:RaceEnd
</pre>
</td></tr></tbody></table>

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

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>RESET
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[FINISHED or FAILED or FLAG:FlagName] ('SCRIPT:Name of Script')
</th></tr>
<tr>
<td colspan="3"><p>Sets the FINISHED or FAILED count of the specified script to 0, or sets the specified boolean flag to False. Remember: Script and Flag names are case sensitive!</p>
<p><b>Example Usages</b>
</p>
<pre>- RESET FINISHED 'SCRIPT:Magic Feathers'
- RESET FLAG:SomeFlag
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>RUNTASK
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['SCRIPT:Name of Script'] (DELAY:#) (NPCID:#)
</th></tr>
<tr>
<td colspan="3">Runs a TASK script as the Denizen on the interacting player.
<p>Modifiers:
</p>
<ul><li>DELAY waits this number of seconds before running the task. specific to the interacting player. If this task is already pending for this player, it is canceled and re-applied with the new delay.</li>
<li>NPCID runs the task as a different Denizen.</li></ul>
<p><b>Example Usages</b>
</p>
<pre>- RUNTASK 'SCRIPT:Apple Reward'
- RUNTASK SCRIPT:RaceEnd DELAY:60
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WAIT
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[# of Seconds] (QUEUE:TASK) (QUEUE:TRIGGER)
</th></tr>
<tr>
<td colspan="3"><p>Pauses a Queue for a specified amount of seconds. If no <tt>QUEUE</tt> is specified, the sending queue is used. For example, if the command is sent from an Interact (Triggered) Script, the queue that will be held is the 'Trigger Queue'. Could be useful in advanced usage situations when using both Task Scripts and Interact Scripts together.</p>
<p><b>Example Usages</b>
</p>
<pre>- WAIT 6
- WAIT 30 QUEUE:TASK</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>ZAP
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(Step #) ('SCRIPT:Name of Script') (DURATION:#) (RANDOM:#-#)
</th></tr>
<tr>
<td colspan="3"><p>A very powerful command, indeed. This is how Scripts progress through their steps. It is not done automatically, instead, you get to decide how to progress. ZAP used alone will simply progress the Player to the next step in the Script. Note: Denizen does not check whether the step exists, so you can use that to your advantage in an Overlay Script Assignment. If an Integer is used, that step will be used.</p>
<p>Specify a <tt>SCRIPT</tt> to change the active step for a Player in a specific Script. If not specified, the triggering Script is used. A <tt>DURATION</tt> can be set to provide an automatic "DEZAP" of sorts, reverting the step back after a specific amount of seconds, unless, in that duration another ZAP command has taken place. This can be used as a 'timeout' of sorts. <tt>RANDOM</tt> can be used to let chance select the step to progress the Player to. If one Integer is included, steps 1 through the chosen number will be randomly selected. You can also use a range of numbers if two Integers are used.</p>
<p><b>Example Usages</b>
</p>
<pre>- ZAP
- ZAP 5
- ZAP RANDOM:6
- ZAP RANDOM:3-6 DURATION:60
- ZAP 6 'SCRIPT:Another Script'
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

The commands below require [[Vault](http://dev.bukkit.org/server-mods/vault/)] and a valid permissions system.

<table align="left" class="wikitable collapsible collapsed" style="background: aliceblue;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>PERMISS
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[permission.node or 'GROUP:Group Name'] (WORLD) ('WORLD:World Name')
</th></tr>
<tr>
<td colspan="3"><p>Gives the Player either a permissions node or adds a group, if supported by your permissions system. Note: You should not include both a permissions node and a group. If you specify a <tt>WORLD</tt> argument, it will apply the permissions node/group only to the current world. You can alternatively specify a world with <tt>WORLD:worldName</tt>.</p>
<p><b>Example Usages</b>
</p>
<pre>- PERMISS modifyworld.*
- PERMISS GROUP:HillsideEnemy
- PERMISS citizens.* WORLD:testworld
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background: aliceblue;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>REFUSE
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[permission.node or 'GROUP:Group Name'] (WORLD) ('WORLD:World Name')
</th></tr>
<tr>
<td colspan="3">Removes from the Player either a permissions node or a group, if supported by your permissions system. Note: You should not include both a permissions node and a group. If you specify a <tt>WORLD</tt> argument, it will remove the permissions node/group only to the current world. You can alternatively specify a world with <tt>WORLD:worldName</tt>. Generally, however you add your permissions or group with <tt>PERMISS</tt>, you should do the same when removing with <tt>REFUSE</tt>.
<p><b>Example Usages</b>
</p>
<pre>- REFUSE modifyworld.*
- REFUSE GROUP:HillsideEnemy
- REFUSE citizens.* WORLD:testworld
</pre>
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
<p>EMOTE 
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['The text to emote.'] (NPCID:#)
</th></tr>
<tr>
<td colspan="3">Let's the Denizen NPC show emotion. Similar to the /me command in IRC, for example. Could be useful for describing to the player what an NPC Denizen may need, or how the NPC Denizen is feeling. <tt>NPCID</tt> can be specified to change the Denizen NPC doing the  'emote'.
<p><b>Example Usages</b>
</p>
<pre>- EMOTE 'is looking a bit nervous.'
- EMOTE NPCID:82 'thinks you should ask a few questions.'
- EMOTE "could use a stiff drink."
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>HINT
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(SHORT)
</th></tr>
<tr>
<td colspan="3">If called from an Interact Script Step with a Chat Trigger, this will output a list of all possible things the player can say to activate a chat trigger.
<p>Modifiers:
</p>
<ul><li>SHORT</li></ul>
<dl><dd><dl><dd>The Denizen will only say the list of trigger words, instead of the full sentence.</dd></dl></dd></dl>
<p><b>Example Usages</b>
</p>
<pre>- HINT
- HINT SHORT
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

<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>SHOUT 
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">["The text to chat."] (NPCID:#) (NOPLAYER)
</th></tr>
<tr>
<td colspan="3">Shouts the text to players nearby. The range that a bystander can hear an NPC Denizen shout is larger then that of a standard <tt>CHAT</tt>, so it also has some technical advantages. <tt>NPCID</tt> can be specified. Using <tt>NOPLAYER</tt> will drop reference to the Player when talking. You can still reference &lt;PLAYER&gt;, however, if need be. See the example below for an idea for usage.
<p><b>Example Usages</b>
</p>
<pre>- SHOUT "EEEK! a spider!"
- SHOUT NOPLAYER "&lt;PLAYER&gt; is a thief! Get him!"
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WHISPER 
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">["The text to whisper."] (NPCID:#) (NOPLAYER)
</th></tr>
<tr>
<td colspan="3">Whispers the text to the player. Really just an alternative to CHAT. By default, bystanders can't hear what the NPC whispers to the interacting Player. As with the <tt>CHAT</tt> command, NPCID can be specified. Using NOPLAYER is possible too, since it may be of use in some circumstances. But remember: by default, no bystanders can see the actual text the NPC Denizen whispers. This can be changed in the <a class="mw-redirect" href="https://wiki.citizensnpcs.co/Config.yml" title="Config.yml">config.yml</a>.
<p><b>Example Usages</b>
</p>
<pre>- WHISPER "The password is.. 42."
- WHISPER NPCID:2 "Hey, I didn't want to blurt this out so everyone could hear, but..."
</pre>
</td></tr></tbody></table>

#### Denizen Interaction

Denizen interaction commands are meant to help bring your Denizen to life by allowing fine control of movement and actions during scripts. These are not meant for making the Denizen do continuous movement and actions, that should instead be done via [Activities](https://wiki.citizensnpcs.co/index.php?title=Denizen/Activity_Scripts/Activities&action=edit&redlink=1 "Denizen/Activity Scripts/Activities (page does not exist)").

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>HOLD
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[ID or ID:Data or MATERIAL or MATERIAL:Data]
</th></tr>
<tr>
<td colspan="3">Makes the Denizen hold a specific block or item.
<p><b>Example Usages</b>
</p>
<pre>- HOLD IRON_PICKAXE
- HOLD 98:3
</pre>
</td></tr></tbody></table>

|  | LOOK | [DIRECTION or BOOKMARK:BookamrkName or 'BOOKMARK:Denizen Name:BookmarkName' or CLOSE or AWAY] (NPCID:#) (DURATION:#) |
| --- | --- | --- |
| This command controls where the NPC Denizen is looking. It requires either a Direction, Bookmark, or look-close trait state. Valid directions: UP, DOWN, LEFT, RIGHT, NORTH, SOUTH, EAST, WEST, AT, and BACK. Looking AT or BACK takes the Player's position for reference. AT will look at the Player, BACK will look away from the player. Using CLOSE | | |

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

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>RESUME
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">
</th></tr>
<tr>
<td colspan="3">Cancels a previous PAUSE command.
<p><b>Example Usages</b>
</p>
<pre>- RESUME
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>RETURN
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(SPEED:#)
</th></tr>
<tr>
<td colspan="3">Makes the denizen walk back to the position it was at before a call to WALKTO or WALK. Will resume NPC pathing if set.
<p>Modifiers:
</p>
<ul><li>SPEED: is the movement speed, generally should be between 0.1 and 1.5</li></ul>
<p><b>Example Usages</b>
</p>
<pre>- WALKTO BOOKMARK:Somewhere
- RETURN
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WALK
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(FORWARD:#) (NORTH:#) (SOUTH:#) (EAST:#) (WEST:#) (UP:#) (DOWN:#) (X:#) (Y:#) (Z:#) (SPEED:#)
</th></tr>
<tr>
<td colspan="3">Makes the denizen walk some distance from its current position.  Interrupts any current movement, and pauses the NPC pathing if active. All provided directions are added into one movement. Decimal and negative values are accepted.
<p>Modifiers:
</p>
<ul><li>SPEED: is the movement speed, generally should be between 0.1 and 1.5</li>
<li>FORWARD: makes the Denizen walk in whatever direction it is currently facing. Combine LOOK CLOSE and a negative value to walk directly away from the player.</li>
<li>+X is the same as EAST</li>
<li>+Y is the same as UP</li>
<li>+Z is the same as NORTH</li></ul>
<p><b>Example Usages</b>
</p>
<pre>- WALK NORTH;4 EAST:2.5
- WALK FORWARD:1
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WALKTO
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[BOOKMARK:LocationBookmark or 'BOOKMARK:DenizenName:LocationBookmark' or PLAYER]  (SPEED:#)
</th></tr>
<tr>
<td colspan="3">Makes the denizen walk to the specified location bookmark, or to the interacting player. Interrupts any current movement, and pauses the NPC pathing if active.
<p>Modifiers:
</p>
<ul><li>SPEED: is the movement speed, generally should be between 0.1 and 1.5</li></ul>
<p><b>Example Usages</b>
</p>
<pre>- WALKTO PLAYER
- WALKTO 'BOOKMARK:Gary:GarysHouse'
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
<li>ID: - The name of the kill listener; without it, the listener will take on the name of the script run upon completion.</li></ul>
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
<p>SPAWN
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[ENTITY_TYPE] (QTY:#) (BOOKMARK:LocationBookmark) ('BOOKMARK:Denizen Name:LocationBookmark') (SPREAD:#) ('EFFECT:[POTION_EFFECT] [LEVEL]') ('OPTION:[OPTIONS]')
</th></tr>
<tr>
<td colspan="3">Spawns a specified amount of entities. If the location bookmark is missing, they will spawn near the Denizen.
<p>Modifiers:
</p>
<ul><li>SPREAD:[#] Increases the 'spread' of the area that the monster can spawn.</li>
<li>'EFFECT:[POTION_EFFECT] [LEVEL]' Applies a potion effect on the monster when spawning.</li>
<li>'OPTION:OptionName OptionsValue' Applies a flag to the Mob. Note: Only works for mobs that can accept the flag.
<ul><li>Valid OptionNames are:
<ul><li>POWERED, SADDLED, BABY, 'PROFESSION [PROFESSION_TYPE]', SHEARED, 'COLORED [DYE_COLOR]', ANGRY')
<ul><li>CREEPER can have POWERED</li>
<li>PIG can have SADDLED</li>
<li>PIG, SHEEP, COW, VILLAGER, CHICKEN, OCELOT and WOLF can have BABY</li>
<li>VILLAGER can have PROFESSION
<ul><li>Valid PROFESSION_TYPEs: FARMER, LIBRARIAN, PRIEST, BLACKSMITH, BUTCHER</li></ul></li>
<li>SHEEP can have SHEARED and COLORED</li>
<li>WOLF and PIG_ZOMBIE can have ANGRY</li></ul></li></ul></li></ul></li></ul>
<p><b>Example Usages</b>
</p>
<pre>- SPAWN BOAT
- SPAWN QTY:3 COW BOOKMARK:Cage
- SPAWN VILLAGER 'BOOKMARK:El Notcho:Gate'
- SPAWN QTY:10 PIG_ZOMBIE SPREAD:5
- SPAWN QTY:25 ZOMBIE SPREAD:20 'EFFECT:INCREASE_DAMAGE 2'
- SPAWN QTY:2 SHEEP 'OPTION:COLORED RED'
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>STRIKE
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(DENIZEN) (BOOKMARK:LocationBookmark) ('BOOKMARK:Denizen Name:LocationBookmark') (NODAMAGE) (NPCID:#)
</th></tr>
<tr>
<td colspan="3">Lightning at your fingertips.
<p>Modifiers:
</p>
<ul><li>DENIZEN</li></ul>
<dl><dd><dl><dd>Strike lightning at the Denizen's location instead of the player.</dd></dl></dd></dl>
<ul><li>LocationBookmark</li></ul>
<dl><dd><dl><dd>Strike lightning at the location bookmark instead of the player.</dd></dl></dd></dl>
<ul><li>NPCID:#</li></ul>
<dl><dd><dl><dd>Strike lightning at the location of the specified NPC (using the npc id)</dd></dl></dd></dl>
<ul><li>NODAMAGE</li></ul>
<dl><dd><dl><dd>Lightning is cosmetic and does no damage.</dd></dl></dd></dl>
<p><b>Example Usages</b>
</p>
<pre>- STRIKE
- STRIKE BOOKMARK:BigTree
- STRIKE DENIZEN NODAMAGE
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>SWITCH
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[BOOKMARK:BlockBookmark] or [BOOKMARK:DenizenName:BlockBookmark] (DURATION:#)
</th></tr>
<tr>
<td colspan="3">This command will activate a button, switch or pressure plate at the designated <b>block</b> bookmark.
<p>Modifiers:
</p>
<ul><li>DURATION:#</li></ul>
<dl><dd><dl><dd>Will switch the device again after the specified number of seconds.</dd></dl></dd></dl>
<p><b>Example Usages</b>
</p>
<pre>- SWITCH BOOKMARK:LightSwitch DURATION:30
- SWITCH BOOKMARK:Jimbo:JimbosButton 
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WEATHER
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[SUNNY or STORMY or PRECIPITATING]
</th></tr>
<tr>
<td colspan="3">Changes the Denizen's world's weather to the designated type.
<p><b>Example Usages</b>
</p>
<pre>- WEATHER SUNNY
</pre>
</td></tr></tbody></table>

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
<p>GIVE
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[MONEY or XP or HEROESEXP or ID or ID:Data or MATERIAL or MATERIAL:Data] (QTY:#)
</th></tr>
<tr>
<td colspan="3">
<p>Gives something to the Player. If QTY: is not specified, its default value is 1. You can also give Minecraft XP by using 'XP'.
Using HEROESEXP type will give the Player (or Hero) Questing Experience. Note: This requires HEROES to be installed on your server!
<b>Example Usages</b>
</p>
<pre>- GIVE MONEY QTY:10
- GIVE 17:2 QTY:3
- GIVE LEAVES:2
- GIVE HEROESEXP QTY:25
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>HARM
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(DENIZEN) (AMOUNT:#)
</th></tr>
<tr>
<td colspan="3">Hurts the the interacting player.
<p>Modifiers:
</p>
<ul><li>DENIZEN</li></ul>
<dl><dd><dl><dd>Hurts the Denizen instead of the player.</dd></dl></dd></dl>
<ul><li>AMOUNT:</li></ul>
<dl><dd><dl><dd>The amount to hurt, if not specified defaults to 1 point.</dd></dl></dd></dl>
<p><b>Example Usages</b>
</p>
<pre>- HARM AMOUNT:5
- HARM DENIZEN
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

<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>TAKE 
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[MONEY or ITEMINHAND or ID or ID:Data or MATERIAL or MATERIAL:Data] (QTY:#)
</th></tr>
<tr>
<td colspan="3">
<p>Takes something from the Player. If QTY: is not specified, its default value is 1.
</p><p><b>Example Usages</b>
</p>
<pre>- TAKE MONEY QTY:1000
- TAKE 17:2 QTY:1
- TAKE LOG:2
- TAKE ITEMINHAND
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>TELEPORT 
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(DENIZEN)  [BOOKMARK:LocationBookmark or 'BOOKMARK:Denizen Name:LocationBookmark']
</th></tr>
<tr>
<td colspan="3">Teleports the interacting to player or denizen to the specified bookmark.
<p>Modifiers:
</p>
<ul><li>DENIZEN</li></ul>
<dl><dd><dl><dd>Teleport the Denizen instead of the player.</dd></dl></dd></dl>
<p><b>Example Usages</b>
</p>
<pre>- TELEPORT BOOKMARK:FarAwayPlace
- TELEPORT DENIZEN 'BOOKMARK:Jim:JimsBasement'
</pre>
</td></tr></tbody></table>
