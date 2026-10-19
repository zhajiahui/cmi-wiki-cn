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
<p><b>Denizen</b> is an extension for Citizens that allows scripting of NPCs to handle tasks, quests, player interaction and more! It operates as a full-featured Minecraft server scripting system!
</p><p><b>Current version:</b> 1.x.x Release
</p><p><b>Original Creator:</b> aufdemrand
</p><p><b>Head of Development:</b> mcmonkey
</p><p><b>Previous developers:</b> David Cernat, Jeebiss, Morphan1, Xenmai, Mergu
</p><p><b>Source:</b> <a class="external text" href="https://github.com/DenizenScript/Denizen-For-Bukkit" rel="nofollow">Github</a>
</p><p><b>Spigot Release:</b> <a class="external text" href="https://www.spigotmc.org/resources/denizen.21039/" rel="nofollow">Spigot</a>
</p><p><b>Latest release build:</b> <a class="external text" href="http://ci.citizensnpcs.co/view/All/job/Denizen/" rel="nofollow">1.x.x Builds</a>
</p><p><b>Latest developmental build:</b> <a class="external text" href="http://ci.citizensnpcs.co/view/All/job/Denizen_Developmental/" rel="nofollow">1.x.x Dev Builds</a>
</p><p><b>Citizens build:</b> <a class="external text" href="http://ci.citizensnpcs.co/job/Citizens2/" rel="nofollow">2.x.x</a>
</p><p><b>Support tickets:</b> <a class="external text" href="http://github.com/DenizenScript/Denizen-For-Bukkit/issues/" rel="nofollow">Tickets on Github</a>
</p><p><b>Discord:</b> <a class="external text" href="https://discord.gg/Q6pZGSR" rel="nofollow">Denizen Discord</a>
</p><p><b>Thank you:</b> A lot of people have stepped forward to help out with Denizen, and that's awesome! Special thanks to everyone who has beta tested, and a huge amount to these people: fullwall, AgentKid, aPunch, Instinx, tenowg, groggluebutt, Wreyth, jrbudda, spidi, ... the list could go on!
<br/>
</p>
</div></td></tr></tbody></table>
</div>
</td></tr></tbody></table>

[![](https://wiki.citizensnpcs.co/images/3/30/Denizen-Logo-Large.png)](https://wiki.citizensnpcs.co/File:Denizen-Logo-Large.png)

~~This Wiki should be regarded as a quick reference guide / learning tool for Denizen.~~

For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

~~Denizen is a powerful engine to write your own plugins via scripting. It is also a great way to add complex interactive role-playing NPCs to your server. Denizen NPCs use scripts with steps and events to interact with the player and world. Imagine interactive gate-keepers, magical wizards, experience trainers, bankers, talking townspeople and more! They can be used in thousands of different ways, from tutorials, to questing, to administrating... your imagination is just about the limit! Denizen uses its own YAML-based scripting language which is designed to be easily read and edited by hand.~~

<s>
<div class="mw-heading mw-heading3"><h3 id="Table_of_Contents">Table of Contents</h3></div>
<ol><li><a href="https://wiki.citizensnpcs.co/Denizen/Introduction" title="Denizen/Introduction">Introduction</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/Types_of_Scripts" title="Denizen/Types of Scripts">Types of Scripts</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/Triggers" title="Denizen/Triggers">NPC Interact Script Triggers</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/Commands" title="Denizen/Commands">Commands</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/Replaceable_Tags" title="Denizen/Replaceable Tags">Replaceable Tags</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/Additional_Traits" title="Denizen/Additional Traits">Additional Traits</a></li>
<li><a href="https://wiki.citizensnpcs.co/Denizen/Script_Samples" title="Denizen/Script Samples">Script Samples</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Other&amp;action=edit&amp;redlink=1" title="Denizen/Other (page does not exist)">Other Pages</a></li></ol>
<p><br/>
</p>
</s>

<s>
<div class="mw-heading mw-heading3"><h3 id="How_it_works">How it works</h3></div>
<p>Denizen is an extension of Citizens2 that adds an incredible amount of interactivity and automation to NPCs and Players with some of these major features:
</p>
<ul><li><b>The Script Engine</b> carries out and sends all the commands to be executed in an orderly and predictable fashion; this is the backbone of Denizen. There's not much to see on the outside, this is the interworkings of Denizen, but rest assured that this is high performance machine behind the scenes!</li>
<li><b>Assignment and Interact Scripts</b> are the meat of Denizen, allowing Players and NPCs to interact with each other and the world. These are highly customizable with 20+ requirement types, 90+ script commands, and thousands of different ways to use them together. This with the Denizen Script Engine also allows commands to help control the rest of Denizen with script flow commands and such.</li>
<li><b>Task Scripts</b> are simple scripts that can be carried out in a variety of different ways. These can be used along side any other script types, but perhaps the most powerful way to use them is by allowing your plugin to utilize them, if you're a developer, or using other plugins that harness the ability to run a Denizen Task Script as well.</li>
<li><b>World Scripts</b> are scripts that call Denizen commands when random things happen throughout the world - anything, even down to a player mining a block, and a separate script for them picking up the item it dropped! With the power of world scripts, a skilled user could make entire server plugins using nothing but Denizen scripts!</li>
<li><b>Listeners</b> are currently in an 'experimental phase', but are already allowing control over minecraft and bukkit events like nothing other. This already allows scripts to keep track of and assign 'quest-like' objectives, such as a 'kill quest', if you're familiar with the C1 Quester. But whereas many quest plugins are limited to this feature alone, Denizen, of course, allows you to use this in addition and along side the rest of the plugin, making room for extremely dynamic and intricate 'quest scripts'.</li>
<li><b>Flag System</b> is the key to Denizen being dynamic. An intricate, yet easy to learn 'Flag/Variable' system has been implemented into Denizen to help keep track of events, items, numbers, players, and more. The new Flag System is still getting more powerful each and every day... it's the key to a spectacular script is sure to have a flag or two.</li>
<li><b>Extensible Commands/Requirements/Activities and more</b> make it easy to add-on to Denizen with very little Java knowledge. This also makes it extremely easy to let users utilize your plugin with script commands. Denizen also has API Events to use.</li>
<li><b>Denizen Debugger</b> is an extremely friendly and informative way to test out scripts and interactions. Commands, events, and interactions are all logged in an easy to read format to show the exact progression of a script and its surroundings. No more guessing! Less headaches!</li>
<li><b>A note on YML</b> Most of the time when a server owner uses YML, they edit an existing configuration. In Denizen, it is required to frequently *add* additional content. Be careful of your spacing, and never use tabs. You can use ChatBots in <a class="external text" href="https://discord.gg/Q6pZGSR" rel="nofollow">our Discord group</a> to check your YML files or you can use <a class="external text" href="http://yaml-online-parser.appspot.com/" rel="nofollow">this online YAML parser.</a> (The ChatBots do much more, as well! Just go into <a class="external text" href="https://discord.gg/Q6pZGSR" rel="nofollow">our Discord group</a> and type <b>!help</b>)</li>
<li><b>An additional note on YAML</b> Denizen no longer users pure YAML, but rather its own custom parsing code. The YAML parsers available are not perfect, only the ChatBot on IRC, mentioned above, currently has a <b>!dScript</b> checker.</li></ul>
<p><br/>
</p></s>

~~Seem overwhelming? Stop! Start small! Denizen is easy, Denizen is simple. But. Denizen is hard, Denizen is complex. Simply put: Denizen is what you make it! Our advice? Start small, and build upon what you have. Read the wiki articles, watch the youtube videos, test our your scripts, and test out some of the sample scripts! Before you know it, you'll be a Denizen poweruser, drunken with power, just like us!~~

(Legacy 0.7 wiki found [here](http://wiki.citizensnpcs.co/Denizen/0.7))
