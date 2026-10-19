<table cellpadding="0" cellspacing="3" style="border: 0; background-color: #ffffff" width="275">
<tbody><tr>
<td style="width: 275; vertical-align: top; border:1px solid #ccc; background-color: #ffffff">
<div style="background-color:#aaa; font-size:1px; height:8px; border-bottom:1px solid #ccc;"></div>
<div style="float:right; margin:8px; margin-top:5px"></div>
<div style="padding:0.5em 0.3em 0.3em 0.3em; margin:0; text-indent:0.1em; font-weight: bold; border-bottom:1px solid #aaaaaa;"><b> </b></div>
<div style="font-size:100%; padding:3px">
<table cellpadding="0" cellspacing="3" width="100%">
<tbody><tr>
<td align="left" valign="top" width="100%">
<figure class="mw-default-size mw-halign-center" typeof="mw:File"><a class="mw-file-description" href="https://wiki.citizensnpcs.co/File:Denizen.png"><img class="mw-file-element" decoding="async" height="88" src="https://wiki.citizensnpcs.co/images/4/47/Denizen.png" width="296"/></a><figcaption></figcaption></figure>
<div class="padded" style="padding: 19px; font-family:camingodos-web; font-size:110%;">
<p><b>Denizen</b> is an extension for Citizens that allows scripting of NPCs to handle tasks, quests, player interaction and more! 
</p><p><b>Current Version:</b> 0.7.6 Pre-release BETA
</p><p><b>Developers:</b> aufdemrand
</p><p><b>Source:</b> <a class="external text" href="https://github.com/aufdemrand/Denizen" rel="nofollow">Github</a>
</p><p><b>Development Builds:</b> <a class="external text" href="http://jenkins.citizensnpcs.com/job/Denizen/" rel="nofollow">Jenkins</a>
</p><p><b>Latest Developmental Build:</b> <a class="external text" href="http://ci.citizensnpcs.com/job/Denizen/lastSuccessfulBuild/" rel="nofollow">2.0.2</a>
</p><p><b>Support tickets:</b> <a class="external text" href="http://github.com/aufdemrand/Denizen/issues/" rel="nofollow">Tickets on Github</a>, but please read the entirety of this document first.
</p><p><b>Donate:</b> A lot of man hours has been put into Denizen. Your donations add a lot to the project and are always welcome! Your donations will probably help remodel my house and feed my kids. :) 
<a class="external text" href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=jeremy%2eschroeder%40gmail%2ecom&amp;lc=US&amp;currency_code=USD&amp;bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted" rel="nofollow">Donate to aufdemrand</a> Don't forget to donate to the Citizens2 project as well, as none of this would be possible without that!
</p><p><b>Thank You:</b> A lot of people have stepped forward to help out with Denizen, and that's awesome! Special thanks to everyone who has beta tested, and a huge to these people: fullwall, AgentKid, aPunch, NeonMaster, Instinx, tenowg, groggluebutt, Wreyth, jrbudda, spidi, the list could go on!
</p><p><b>CitizensUI:</b> For a GUI interface, check out <a href="https://wiki.citizensnpcs.co/CitizensUI" title="CitizensUI">CitizensUI</a> by jrbudda which provides an interface for Citizens NPCs as well as managing scripts and other NPC types.
<br/>
</p>
</div></td></tr></tbody></table>
</div>
</td></tr></tbody></table>

[![](https://wiki.citizensnpcs.co/images/3/30/Denizen-Logo-Large.png)](https://wiki.citizensnpcs.co/File:Denizen-Logo-Large.png)



Load video

YouTube

YouTube might collect personal data. [Privacy Policy](https://www.youtube.com/howyoutubeworks/user-settings/privacy/)

Continue
Dismiss

A small glimpse of Denizen.

For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

This is the old Wiki for Denizen 0.7.6! Information found here does not apply to later versions of Denizen.
~~Denizen is a great way to add [MUD-style](http://en.wikipedia.org/wiki/MUD) RPG Citizens to your server. Denizen NPCs use mini scripts with steps and events to interact with the player and world. Imagine interactive gate-keepers, magical wizards, experience trainers, bankers, talking townspeople and more! They can be used in thousands of different ways, from tutorials, to questing, to administrating.. your imagination is just about the limit! Though Denizen uses Scripting, it is not to be confused with [Citizens2 Core Scripting](https://wiki.citizensnpcs.co/Scripting "Scripting") which utilizes JavaScript and other major scripting languages to implement Goals. Instead, Denizen uses its own YML 'scripting language' which is designed to be easily read and edited by hand.~~

<s>
<div style="padding:20px; font-family:camingodos-web; font-size:110%; background-color:#EEDDEE; border-style:dotted; border-width:1px; width:55%; font-weight:500;">If you are coming from Denizen 0.6, we've attempted to compile a <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Migration" title="Denizen/0.7/Migration">list for helping with migration</a> for users upgrading who need a brief on what needs to be changed to become compatible.
</div>
</s>

<s><div style="padding:10px; font-family:camingodos-web; font-size:110%;">
<div class="mw-heading mw-heading3"><h3 id="How_it_works">How it works</h3></div>
<p>Denizen is an extension of Citizens2 that adds an incredible amount of interactivity and automation to NPCs and Players with some of these major features:
</p>
<ul><li><b>The Script Engine</b> carries out and sends all the commands to be executed in an orderly and predictable fashion; this is the backbone of Denizen. Currently has 3 queues, one for the Player, one for Denizen, and one for Tasks. There's not much to see on the outside, this is the interworkings of Denizen, but rest assured that this is high performance machine behind the scenes!</li>
<li><b>Interact Scripts</b> are the meat of Denizen, allowing Players and NPCs to interact with each other and the world. These are highly customizable with 20+ requirement types, 40+ script commands, and thousands of different ways to use them together. This with the Denizen Script Engine also allows commands to help control the rest of Denizen with script flow commands and such.</li>
<li><b>Activity Scripts</b> are exciting. Imagine Johnny Appleseed planting trees, on his own, or simple villagers wandering around and socializing. Activities, of course, work with the rest of Denizen's other functions and features, allowing hundreds of ways to use Activities to add automation and liveliness to your world.</li>
<li><b>Activity Scheduler</b> takes Activity Scripts one step further, allowing Denizen NPCs to have daily schedules, based on the Minecraft day, to allow certain functionality to different times of the day. This also enables certain Script Commands to be executed and carried out, as well.</li>
<li><b>Task Scripts</b> are simple scripts that can be carried out in a variety of different ways. These can be used along side both Activity and Interact Scripts, but perhaps the most powerful way to use them is by allowing your plugin to utilize them, if you're a developer, or using other plugins that harness the ability to run a Denizen Task Script as well.</li>
<li><b>Listeners</b> are currently in an 'experimental phase', but are already allowing control over minecraft and bukkit events like nothing other. This already allows scripts to keep track of and assign 'quest-like' objectives, such as a 'kill quest', if you're familiar with the C1 Quester. But whereas many quest plugins are limited to this feature alone, Denizen, of course, allows you to use this in addition and along side the rest of the plugin, making room for extremely dynamic and intricate 'quest scripts'.</li>
<li><b>Flag System</b> is the key to Denizen being dynamic. An intricate, yet easy to learn 'Flag/Variable' system has been implemented into Denizen to help keep track of events, items, numbers, players, and more. The new Flag System is still getting more powerful each and every day.. it's the key to a spectacular script is sure to have a flag or two.</li>
<li><b>Extensible Commands/Requirements/Activities and more</b> make it easy to add-on to Denizen with very little Java knowledge. This also makes it extremely easy to let users utilize your plugin with script commands. Denizen also has API Events to use.</li>
<li><b>Denizen Debugger'</b> is an extremely friendly and informative way to test out scripts and interactions. Commands, events, and interactions are all logged in an easy to read format to show the exact progression of a script and its surroundings. No more guessing! Less headaches!</li></ul>
<p><br/>
Seem overwhelming? Stop! Start small! Denizen is easy, Denizen is simple. But. Denizen is hard, Denizen is complex. Simply put: Denizen is what you make it! Our advice? Start small, and build upon what you have. Read the wiki articles, watch the youtube videos, test our your scripts, and test out some of the sample scripts! Before you know it, you'll be a Denizen poweruser, drunken with power, just like us!
</p>
</div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; border-style:none; font-size:110%; font-weight:500;width:100%;border-width:0px;">
<div class="mw-heading mw-heading1"><h1 id="Denizen">Denizen</h1></div>
<p>If you are new to Denizen, see <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Before_Using_Denizen" title="Denizen/0.7/Before Using Denizen">Before Using Denizen: Getting Started</a>. 
<br/>If you are having problems getting a script working please see <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Troubleshooting" title="Denizen/0.7/Troubleshooting">Troubleshooting</a>.<br/>
If you're hooked, we recommend you read all the sections in order and try out some sample scripts!
</p>
</div></s>

<s><table class="wikitable" style="text-align: left; border-color:white; border-style:none; vertical-align: text-top; background-color:white;">
<tbody><tr style="vertical-align:top;">
<td style="width: 60%;">
<div style="vertical-align: text-top; padding:16px; border-style:none; border-color:white;font-family:camingodos-web; font-size:110%; font-weight:500;width:85%;border-width:0px;">
<div class="mw-heading mw-heading3"><h3 id="Table_of_Contents">Table of Contents</h3></div>
<ol><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Before_Using_Denizen" title="Denizen/0.7/Before Using Denizen">Before Using Denizen &amp; Getting Started</a>
<ul><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Start-up_kit" title="Denizen/0.7/Start-up kit">The Start-up Kit</a></li></ul></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Troubleshooting" title="Denizen/0.7/Troubleshooting">Denizen Troubleshooting</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/File_Structure" title="Denizen/0.7/File Structure">The File Structure</a>
<ul><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/config.yml" title="Denizen/0.7/config.yml">Default config.yml</a></li></ul></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/In_Game_Commands" title="Denizen/0.7/In Game Commands">In Game and Console Commands</a></li>
<li>Writing Scripts
<ul><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts" title="Denizen/0.7/Interact Scripts">Introduction to Interact Scripts</a>
<ul><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Triggers" title="Denizen/0.7/Interact Scripts/Triggers">Interact Triggers</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Interact_Requirements" title="Denizen/0.7/Interact Scripts/Interact Requirements">Interact Script Requirements</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Commands" title="Denizen/0.7/Interact Scripts/Commands">Script Commands</a></li></ul></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Task_Scripts" title="Denizen/0.7/Task Scripts">Task Scripts and the Task Queue</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Activity_Scripts" title="Denizen/0.7/Activity Scripts">Activity Scripts and the Scheduler</a>
<ul><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Activity_Scripts/Activities" title="Denizen/0.7/Activity Scripts/Activities">Activities and Goals</a></li></ul></li></ul></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Assignments" title="Denizen/0.7/Assignments">Assigning Scripts</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Flags&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Flags (page does not exist)">Denizen Flag System</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Replaceables" title="Denizen/0.7/Replaceables">Replaceable Data Tags</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Listeners&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Listeners (page does not exist)">Denizen Listeners and Events</a></li>
<li>Examples
<ul><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts" title="Denizen/0.7/Example Scripts/Beginner Scripts">Beginner Scripts</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Advanced_Scripts" title="Denizen/0.7/Example Scripts/Advanced Scripts">Advanced Scripts</a></li>
<li><a href="https://wiki.citizensnpcs.co/Sentry/Sentry_and_Denizen" title="Sentry/Sentry and Denizen">Denizen and Sentry</a></li>
<li><a class="mw-redirect" href="https://wiki.citizensnpcs.co/Sentry/Builder_and_Denizen" title="Sentry/Builder and Denizen">Denizen and Builder</a></li></ul></li>
<li>Extending Denizen
<ul><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scritps/Custom_Commands" title="Denizen/0.7/Interact Scritps/Custom Commands">Extending Custom Commands</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Interact_Scripts/Custom_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Interact Scripts/Custom Requirements (page does not exist)">Extending Custom Requirements</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Interact_Scripts/Custom_Triggers&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Interact Scripts/Custom Triggers (page does not exist)">Extending Custom Triggers</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Activity_Scripts/Custom_Activities&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Activity Scripts/Custom Activities (page does not exist)">Extending Custom Activities</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Activity_Scripts/Event_API&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Activity Scripts/Event API (page does not exist)">Utilizing Denizen Event API</a></li></ul></li>
<li>Bonus Content
<ul><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Bonus_Content/Pictures" title="Denizen/0.7/Bonus Content/Pictures">Denizen Bonus Pictures</a></li></ul></li></ol>
</div>
</td>
<td style="width: 40%;">
<div style="padding:16px; vertical-align: text-top;border-color:white; border-style:none; font-family:camingodos-web; font-size:110%; font-weight:500;width:95%;border-width:0px;">
<div class="mw-heading mw-heading3"><h3 id="Sample_Scripts">Sample Scripts</h3></div>
<p><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts#Denizen_Basics" title="Denizen/0.7/Example Scripts/Beginner Scripts">Denizen Basics</a>
</p>
<ul><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts#Denizen_Basics" title="Denizen/0.7/Example Scripts/Beginner Scripts">The Click and Damage Triggers</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts#Denizen_Basics" title="Denizen/0.7/Example Scripts/Beginner Scripts">The Chat and Proximity Triggers</a></li></ul>
<p><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts#Simple,_random_conversations" title="Denizen/0.7/Example Scripts/Beginner Scripts">Simple, random conversations</a>
</p>
<ul><li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts#A_conversation_with_RANDOM" title="Denizen/0.7/Example Scripts/Beginner Scripts">A conversation with RANDOM</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts#A_conversation_with_ZAP_RANDOM" title="Denizen/0.7/Example Scripts/Beginner Scripts">A conversation with ZAP RANDOM</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts#The_server_rules" title="Denizen/0.7/Example Scripts/Beginner Scripts">The Server Rules</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts#Simple_Bank_teller" title="Denizen/0.7/Example Scripts/Beginner Scripts">Simple Bank Teller</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts#Advanced_Bank_teller" title="Denizen/0.7/Example Scripts/Beginner Scripts">Advanced Bank Teller</a></li></ul>
</div>
</td>
<td style="width: 20%;">
<div style="padding:16px; vertical-align: text-top;border-color:white; border-style:none; font-family:camingodos-web; font-size:110%; font-weight:500;width:95%;">
<div class="mw-heading mw-heading3"><h3 id="Index">Index</h3></div>
<p>If you are having problems getting a script working please see <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Troubleshooting" title="Denizen/0.7/Troubleshooting">Denizen/Troubleshooting</a>.
</p>
</div>
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading3"><h3 id="Change_Log">Change Log</h3></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
<p>Here's what's changed!
</p><p><br/>
<b>0.7.5 BETA build #455</b>
</p>
<ul><li><span style="background: white; color: red"><b>New!</b></span> OWNER requirement will require ownership of the NPC interacting. Could be used for 'command interfaces' that only the owner can access.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> SNEAKING requirement requires the player be crouched when clicking. Careful on conflict with info-click for ops! Info-click can be disabled in the config.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> Queue-time flag replacement can let you dynamically use flag data in a script entry. For example: - GIVE &lt;FLAG:ExampleItemFlag&gt; QTY:&lt;FLAG:ExampleQtyFlag&gt;</li></ul>
<ul><li><span style="background: white; color: red"><b>Experimental!</b></span> Denizen NPCs now have their own Command Queue, and a TASK activity. This allows NPC's to use the activity scheduler to do tasks at certain times of the day.</li></ul>
<ul><li><span style="background: white; color: red"><b>Experimental!</b></span> LISTEN command implemented, KILL type implemented. Return of the 'Quester'. More types coming soon. Example usage: - LISTEN KILL ID:UniqueId TYPE:ENTITY NAME:ZOMBIE QTY:5 SCRIPT:FinishIt would require the player to kill 5 zombies. When completed, it will run the task script 'FinishIt'.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> Use &lt;*&gt; to use Chat Trigger text in EXECUTE or talk commands.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> Use &lt;*&gt; in FLAG command to remember player input. Example usage: - FLAG PLAYER_RESPONSE:&lt;*&gt;</li></ul>
<p><br/>
<b>0.7.5 BETA build #440:</b>
</p>
<ul><li><span style="background: white; color: red"><b>New!</b></span> API Events make extending Denizen more powerful than ever!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> RUNTASK/CANCELTASK allows delayed tasks to be set, and cancelled.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> HOLD command can change what a Denizen NPC is wielding.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> Replaceable data for dynamically putting flags into texts!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> ISLIQUID requirement can sense if a block bookmark is solid, or liquid.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> IF command can evaluate a FLAG and run a TASK script.</li></ul>
<p><br/>
<b>0.7 BETA builds #125 - #280:</b>
</p>
<ul><li><span style="background: white; color: red"><b>Updated!</b></span> Less bugs! We're still in beta, but there has been some major code cleanup!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> Triggers, Commands, Requirements and Activities are now extensible by plugin programmers. See: <a class="external text" href="http://wiki.citizensnpcs.net/Custom_Denizen_Commands" rel="nofollow">Custom Denizen Commands on the Citizens2 Wiki</a>. Documentation coming soon!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Debug_Mode">Debug Mode</a> will let you see the logic of interaction and script execution to help you find problems in scripts faster than ever. I'm striving to make this as informational and clean as possible to help you test your scripts and get good feedback on behavior.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Info-click">Info-Click</a> lets you see Denizen stats and specifics, such as script assignments, trigger status, activity schedule and associated bookmarks with just a crouch and a click. Requires OP.. use this!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Proximity_Trigger">Proximity Triggers</a> can trigger a script when a Player comes near. The most requested trigger type I got during the previous betas.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Location_Trigger">Location Triggers</a> can trigger a script when a Player walks over a Location Bookmark. This is kind of like a PLAYERTASK LOCATION, but better! :)</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Damage_Trigger">Damage Triggers</a> separate the left and right clicks for more control over interaction. Look forward to a whole new set of commands to go along with this!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Assignments&amp;action=edit&amp;redlink=1" title="Denizen/Assignments (page does not exist)">Script 'Overlay' Assignment</a> mode is a whole new way to assign a script. Less copying/pasting when working with multiple scripts, not to mention more control! If you're an advanced script-user, this is for you!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Interact_Script_Commands">ANNOUNCE command</a> can make global server announcements.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Interact_Script_Commands">RANDOM command</a> will leave command execution to chance. Duck-duck-goose.</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Interact_Script_Commands">HINT command</a> will hint to the Player acceptable Chat Triggers for the current step and script. Language support coming soon!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Interact_Script_Commands">FLAG command</a> lets you set 'flags', on players to store progress, important information, or other variables that can be used with the FLAG requirement. This is HUGE!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Requirement_Types">FLAG requirement</a> can require special flags and values to be set in order to be eligible for a script. Again, this is HUGE!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#Requirement_Types">POWERED requirement</a> can check if a block bookmark has redstone power. Great idea, instinx!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> The activity engine has been implemented which will allow your Denizen to do things on their own. There's a whole lot more to this concept, but you can try out the new WANDER activity in all its glory. This thing is cool, and customizable!</li></ul>
<ul><li><span style="background: white; color: red"><b>New!</b></span> <a href="#In-game_Commands">In-game commands</a> now let you easily manage triggers, bookmarks, and debug info.</li></ul>
<ul><li><span style="background: white; color: red"><b>Updated!</b></span> Extended/unified command syntax for almost every existing command. Once you get over the pain of upgrading, you will drop a jaw at the new capabilities!</li></ul>
<p><br/>
You can see more at the full <a class="external text" href="https://github.com/aufdemrand/Denizen/commits/master" rel="nofollow">Denizen Changelog</a>.
</p>
</div></s>
