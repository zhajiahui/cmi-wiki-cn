For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

~~In Denizen, the Script Command system is extensible by design. It's very easy to make your own commands (and soon Requirements) extend the built-in features. On top of that, Denizen has some features available that may be of use to Plugin Developers.~~

<s><div class="mw-heading mw-heading1"><h1 id="Building_your_own_Commands">Building your own Commands</h1></div></s>

<s><div class="mw-heading mw-heading3"><h3 id="The_ScriptCommand_Object">The ScriptCommand Object</h3></div></s>

~~When Denizen reads scripts, each line is turned into a SciptCommand object that contains the command, the arguments, and various other data and objects, as described below. Your command is an extension of this base Command class, and each time your command is called in for execution, it's this class that is executed and handled a ScriptCommand. How the Command uses the ScriptCommand information is of course, up to you.~~

<s><div class="mw-heading mw-heading4"><h4 id="What_a_ScriptCommand_holds">What a ScriptCommand holds</h4></div></s>

~~ScriptCommands hold data about the situation surrounding the event that activates your command. Which type of script activates your Command, the ScriptCommand can have a multitude of information available. Keep in mind that the ScriptCommand object sent along may not have ALL this information, depending on the circumstances sent.~~

<s><ul><li><code>.getCommand()</code> of course, contains a <code>String</code> of the name of your command.
<dl><dd>Useful if your command module contains instructions for more than one command. You can register multiple commands to your module, as discussed later in this document. See the <code>ENGAGE</code> command for a useful example of utilizing this information.</dd></dl></li></ul></s>

<s><ul><li><code>.arguments()</code> has a <code>String[]</code> of all the arguments the player provided.
<dl><dd>This pre-formats arguments that have used quotes, for instance, if the script command is <code>YOURCOMMAND argument1 argument2 'this is argument3'</code>, this object would have 3 items in the array.</dd></dl></li></ul></s>

<s><ul><li><code>.sendingQueue()</code> returns a <code>QueueType</code> of either <code>QueueType.TRIGGER</code>, <code>QueueType.TASK</code>, or <code>QueueType.ACTIVITY</code>
<dl><dd>This contains the type of queue that sent the command. If the command was issues from a TASK script, for example, this would contain <code>QueueType.TASK</code></dd></dl></li></ul></s>

<s><ul><li><code>.getScript()</code> contains a <code>String</code> name of the script.</li></ul></s>

<s><ul><li><code>.getStep()</code> contains an <code>Integer</code> of the step of the script.
<dl><dd>Note that if this was a <code>TASK</code> script, for example, this would be null.</dd></dl></li></ul></s>

<s><ul><li><code>.getTriggerType()</code> contains a <code>TriggerType</code> of the script, that is, what type of 'TRIGGER' triggered it.
<dl><dd>This will be either <code>TriggerType.ATTACK</code>, <code>TriggerType.CLICK</code>, <code>TriggerType.CHAT</code>, <code>TriggerType.PROXIMITY</code>, <code>TriggerType.TASK</code>, or <code>TriggerType.LOCATION</code>. More types are likely to be implemented.</dd></dl></li></ul></s>

<s><ul><li><code>.getPlayer()</code> contains a <code>Player</code> object of the triggering Player, if triggered by a player, that is.
<dl><dd>If triggered from a <code>ACTIVITY</code> script, this would be null.</dd></dl></li></ul></s>

<s><ul><li><code>.getDenizen()</code> contains a <code>NPC</code> Citizens2 object, again, if a NPC object is sent with it.
<dl><dd>If triggered from a <code>TASK</code> script, this is null.</dd></dl></li></ul></s>

<s><ul><li><code>.getInitiatedTime()</code> contains a <code>Long System.currentTimeMillis()</code> of the system time in which it was sent to your Command for processing.</li></ul></s>

<s><ul><li><code>.getDelayedTime()</code> contains a <code>Long System.currentTimeMillis()</code> of the system time that was set by using the <code>.setDelay(Long newTime)</code>. This is null by default. Check out the <code>WAIT</code> command for a functional example of usage.</li></ul></s>

<s><ul><li><code>.getTexts()</code> contains a <code>String[]</code> of 2 elements.
<dl><dd>First element, <code>.getTexts[0]</code> for example, has the 'raw text' that the player typed to initiate the command. Second element, <code>.getTexts[1]</code> contains the 'friendly text', most likely the Chat Trigger that was set in the script. As you can probaly guess, if <code>.getTriggerType()</code> isn't a <code>TriggerType.CHAT</code> this will most likely be null.</dd></dl></li></ul></s>

~~To summarize, here's a list of methods that can be used to get information about the ScriptCommand.~~

- ~~`.getCommand()` `.arguments()` `.sendingQueue()` `.getScript()` `.getStep()` `.getTriggerType()` `.getPlayer()` `.getDenizen()` `.getInitiatedTime()` `.getDelayedTime()` `.getTexts()`~~
