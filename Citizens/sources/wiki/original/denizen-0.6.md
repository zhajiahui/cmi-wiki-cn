For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

<s><div style="text-align: center;">
<div class="alert" style="border-color: red; background-color: white; color: {{{fgc}}}">
<div style="margin-left: 20px; font-size: 120%;">
<p><b>Version warning.:</b> This documentation is for Denizen 0.6 and is out of date. 
</p><p>Denizen 0.6 is not compatible with the latest builds of C2 or Bukkit 1.3.1.
</p><p>See this link for the latest download of Denizen 0.7.
<a class="external text" href="http://ci.citizensnpcs.net/job/Denizen" rel="nofollow">Link</a><b></b>
</p><p>Preliminary documentation for Denizen 0.7 is available <a href="https://wiki.citizensnpcs.co/Denizen/0.7" title="Denizen/0.7">here</a> <b>Please be aware this page may contain errors.</b>
</p>
</div>
</div>
</div></s>

[![](https://wiki.citizensnpcs.co/images/4/47/Denizen.png)](https://wiki.citizensnpcs.co/File:Denizen.png)
  
  
**Denizen**

|  |  |
| --- | --- |
| **Author** | aufdemrand |
| **Version** | 0.6 Build #124 |
| **Citizens build** | 2.0 Beta |
| **Other dependencies** | Vault |
| **Download** | [Link](http://ci.citizensnpcs.net/view/Characters/job/Denizen/124/artifact/target/denizen-0.6.jar) |
| **Download example scripts:** | [Link](http://dl.dropbox.com/u/44002922/Start-up%20Kit.zip) |
|  | |

**Description:** Scriptable, interactive citizens!

<s><div style="float:left clear:both; margin-left:0.5em; margin-bottom:2.0em">
</div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Denizens are a great way to add <a class="external text" href="http://en.wikipedia.org/wiki/MUD" rel="nofollow">MUD-style</a> RPG Citizens (and some other features) to your server. Denizen NPCs use mini scripts with steps and events to interact with the player and world. Imagine interactive gate-keepers, magical wizards, experience trainers, bankers, talking townspeople and more! They can be used in thousands of different ways, from tutorials, to questing, to administrating.. your imagination is just about the limit!
</p>
</div></s>

<s><div class="mw-heading mw-heading2"><h2 id="Script_Repository">Script Repository</h2></div></s>

~~![](https://wiki.citizensnpcs.co/images/5/5f/Script_Repository.png)~~

<s><div class="mw-heading mw-heading2"><h2 id="Change_Log">Change Log</h2></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Here's what's new!
</p><p><b>Note to beta users pre-build 98:</b> File structure has changed over the last few builds up to 98. The <code>Denizens:</code> node now has its own YML file called assignments. You will need to create this file and cut/paste the node from your config.yml. It's also recommended that you download the new <a href="https://wiki.citizensnpcs.co/Denizen_config.yml" title="Denizen config.yml">Denizen config.yml</a> since some nodes have changed or been expanded upon. Denizen location and block bookmarks are also now stored in saves.yml. You will need to migrate those there, or recreate them before using scripts that use bookmarks. See <a href="#File_Structure">#File Structure</a> for more information on the new file structure.
</p><p><b>0.6 Build #104</b>
</p>
<ul><li>Added PLAYERTASK command. LOCATION QUESTS! (This is for you, Ratkoon)</li></ul>
<p><b>0.6 Build #98</b>
</p>
<ul><li>Update to file structure. saves.yml now contains all information that the denizen plugin writes. This includes player progression/completion/etc. information, denizen location bookmarks, etc. If edited by hand, probably best to shut down the server first. Any existing information in the players: node and denizen location bookmark information needs to be either recreated or migrated into saves.yml.</li>
<li>Added HEAL and HURT commands. Use HEAL [# of health] or HURT [# of health].</li>
<li>Added CHANGE command to change the type of block at a block bookmark. Use CHANGE [Block Bookmark] [#:#|MATERIAL_TYPE].</li>
<li>Added ATTACK command. Use like FOLLOW.</li>
<li>GIVE and TAKE should now also accept #:# format as well as MATERIAL_TYPE.</li>
<li>Added ENGAGE and DISENGAGE commands. When a Denizen is ENGAGE'd, no other interaction will be registered with the NPC until DISENGAGED. This could be useful for keeping players from 'repeating steps' while mid-script. Use ^ENGAGE at the beginning of the script and DISENGAGE at the end.</li>
<li>Requirements using items can now use #:# syntax to check item typeId and data.</li>
<li>Requirements WORLD, POTION_EFFECT, NAME, PERMISSION, and GROUP can check for multiple names/nodes.</li>
<li>FINISHED can now check for a specific amount of times a player has finished. Use: FINISHED # [name of script].</li>
<li>Script combiner should now only pick up .yml files.</li>
<li>Various other bug fixes.</li></ul>
<p><b>0.6 Build #82</b>
</p>
<ul><li>Requirements code reformat is done, thanks for being patient if you were watching the Jenkins!</li>
<li>FINISH command now increments a counter so you can check for a certain number of FINISHes. Use: <code>FINISHED (# of times) [name of script]</code>. The # is optional and will assume 1 if not specified. There's a chance that this broke any recorded FINISHes that may be in your config. Sorry about that. You can manually change them from True to 1 to fix this. New FINISHes will overwrite without any issues.</li>
<li>TIME requirement can now check for DAWN and DUSK in addition to DAY and NIGHT.</li>
<li>Requirements that use items can now use the #:# (typeId:data) format. So, for gray wool, 35:7. You can still specify just WOOL and any color will do.</li>
<li>Script combiner will now only read .yml files, this fixes issues with hidden files in your scripts file corrupting the combined read-only-scripts.yml.</li>
<li>NAME, WORLD, PERMISSION, GROUP, POTION_EFFECT can now all use multiple arguments. For example, <code>WORLD world_1 world_2 world_3 world_4</code> will return true if one of the worlds listed matches. You can use up to 24 arguments.</li></ul>
<p><b>0.6 Build #71</b>
</p>
<ul><li>Started code reformat, this will make it easier to extend.</li>
<li>Added ability to use multiple scripts! Denizen will read any .yml file in the /plugins/Denizen/scripts/ folder. You will need to place your existing scripts.yml in that folder. Denizen will generate a read-only-scripts.yml to the main Denizen folder. This should be left alone. Also made config.yml generate automatically upon startup.</li>
<li>Added config node chat_globally_if_no_chat_triggers</li></ul>
<p><br/>
You can see more at the full <a href="https://wiki.citizensnpcs.co/Denizen_changelog" title="Denizen changelog">Denizen changelog</a>.
</p>
</div></s>

<s><div class="mw-heading mw-heading2"><h2 id="Known_caveats">Known caveats</h2></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>There are some 'issues' with Denizen that we are aware of, and thought that you should be too. Keep in mind that we're working hard to fix these, as soon as possible.
</p>
<ul><li>I've been having problems getting the NPCs to WALKTO a bookmarked location that is far away.</li>
<li>When close to a Denizen that is RESPAWNing, it sometimes won't actually spawn until you back away from it.</li>
<li>Multi-line CHATting loses color codes second line on.</li></ul>
</div></s>

<s><div class="mw-heading mw-heading2"><h2 id="Before_using_Denizens">Before using Denizens</h2></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Denizens are in BETA! Expect a few bugs here and there! There is little error handling for scripts that contain bad syntax, so if you are getting errors while processing a script, the first thing you should do it check the script syntax. I'm working hard to catch errors, but every once in awhile you'll find one that requires a /reload or server restart. If you do come across any errors beyond bad syntax, please  report them to the <a class="external text" href="http://www.github.com/aufdemrand/Denizen/issues" rel="nofollow">Github Issues page for Denizens</a>. You can also get assistance with Denizens on the <a class="external text" href="irc://irc.esper.net" rel="nofollow">#citizens IRC channel on EsperNET</a> from me (aufdemrand) when available. I'm usually there working hard to add awesome features and squashing bugs.
</p><p>Denizen is not a drag-and-go type of plugin. In fact, Denizen won't do anything unless you assign and define scripts to NPCs. It's highly customizable and you should expect that to be able to write scripts, it is suggested you read the entirety of this wiki document. I'm always around IRC to help out, but please don't ask about the basics unless you have consulted here first.
</p><p>Denizens <b>REQUIRES</b> you to have <a class="external text" href="http://dev.bukkit.org/server-mods/vault/" rel="nofollow">Vault</a> installed. You also should have a Permissions System and and Economy System for best results.
</p>
</div></s>

<s><div class="mw-heading mw-heading2"><h2 id="Getting_started_with_Denizen">Getting started with Denizen</h2></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>The easiest way to use Denizen for the first time is to download the <a class="external text" href="http://dl.dropbox.com/u/44002922/Start-up%20Kit.zip" rel="nofollow">Start-up Kit</a> with sample .yml configuration files and scripts. This includes the default config file, sample scripts, and sample assignments to get you started. Denizen relies on a few files to run properly, so let's first go over the file structure.
</p>
</div></s>

<s><div class="mw-heading mw-heading3"><h3 id="File_Structure">File Structure</h3></div></s>

~~[![](https://wiki.citizensnpcs.co/images/c/c2/Figure_1_-_Denizen_file_structure.png)](https://wiki.citizensnpcs.co/File:Figure_1_-_Denizen_file_structure.png)

Denizen File Structure~~

<s><div style="margin-right:2.0em; padding:10px">
<p>Denizen requires the use of a few different YML files to operate properly. This includes a config.yml, assignments.yml, scripts, and saves.yml. 
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="config.yml">config.yml</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>The Denizen config.yml contains nodes to alter the stock behavior and look of Denizen. You'll notice that Denizen does not create its own config.yml. Why is this? Denizen stores its entire config inside memory, so it's not necessary to have a copy inside the Denizen folder unless you need to change the defaults. You can use the config.yml to override those defaults. Not having Denizen write to the config.yml itself (as well as scripts files, and assignments.yml) ensures that upon a <code>/denizen reload</code>, the config.yml, between a save and reload, is never changed when you don't want it to. This also keeps code comments inside the YML files stay intact, exactly the way you left them from last edit allowing you to leave yourself and others detailed notes and ideas.
</p><p>This file can be reloaded into from disk to Denizen memory at any time by using <code>/denizen reload</code>.
</p><p>See: <a href="https://wiki.citizensnpcs.co/Denizen_config.yml" title="Denizen config.yml">Denizen config.yml</a> for a stock copy and explanation of all available options.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="assignments.yml">assignments.yml</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>This YML is where you can define all the options and information for your Denizen NPCs. This will be explained further along in this document, but the most common information in this file is [Interact Script Assignments], [Activity Script Schedule], and [Custom Interact Texts].
</p><p>This file can be reloaded from disk into Denizen memory at any time by using <code>/denizen reload</code>.
</p><p>See: <a href="#A_basic_assignment">#A basic assignment</a> for information on how to get started with assignments.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="saves.yml">saves.yml</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>This file is not meant to be edited by hand, Denizen will create and populate this file automatically as needed. It stores important information such as player progression, Denizen location and block bookmarks, active activity script progression and more. If you absolutely need to make changes by hand, it's best to stop the server, edit, and then restart your server, as this file is constantly being written to by Denizen which will overwrite any changes you make.
</p><p>This file saves periodically, and automatically, upon progression and a server stop.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="read-only-scripts.yml">read-only-scripts.yml</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>This is another files that Denizen creates and should not be edited by hand. This is a combination of the files contained in the scripts folder that Denizen reads from. 
</p><p>This file is populated on a server restart, or by using the <code>/denizen reload</code> command.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="/scripts/_folder"><span id=".2Fscripts.2F_folder"></span>/scripts/ folder</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>This folder is where Denizen will read all the script information from. Upon a server load or <code>/denizen reload</code>, the files are combined and put into the read-only-scripts.yml for the Denizen to read from. This allows better organization of scripts to be maintained, since the amount of scripts can easily get into the triple digits. 
</p><p>The files in the plugins/Denizen/scripts/ folder can be named whatever you please, as long as they end in <code>.yml</code>. Be sure not to duplicate script names from file to file as this will cause problems. 
</p><p>See: <a href="#A_basic_trigger_script">#A basic trigger script</a> for information on how to get started with scripts.
</p>
</div></s>

<s><div class="mw-heading mw-heading2"><h2 id="Writing_Scripts_and_Assignments">Writing Scripts and Assignments</h2></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Still reading? Great! You're on your way to writing some sweet scripts. Let's start out with the basics: Trigger Scripts and Assignments. Denizen needs two things to be functional. A script, and an assignment. Scripts, obviously, hold instructions that are carried out when triggered. Assignments hold information on which scripts should trigger, and when. Bear with me, and keep reading!
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="A_basic_trigger_script">A basic trigger script</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>First, we need a script. The great thing about a Denizen script is that it can be simple or advanced, short or long, thanks to a wide array of commands and functions at your disposal. Scripts can work with, extend, and rely on one another to create rich, interactive gameplay. Each script has at least 2 parts, Requirements and Steps. For now, let's take this very simple script as an example. We'll get more detailed later on.
</p><p>Remember: Scripts are defined in <code>plugins/Denizen/scripts/</code> folder. They can be put into any YML file contained in that directory. You may need to create the directory yourself if no scripts yet exist.
</p>
<pre>'Daytime in the City':   
  Type: Trigger
  Requirements:
    Mode: All
    List:
    - TIME Day
  Steps:
    1:
      Click Trigger:
        Script:
        - CHAT Welcome to the city! Isn't it beautiful in the daytime?
</pre>
<p>So what just happened there? A quick literal translation: This script is named <code>'Daytime in the City'</code>. This name is used when assigning Denizen NPCs their scripts to use. When the script is called by a trigger, in this case a <code>'Click Trigger'</code>, for it to activate the Requirements set must be met, more specifically <code>ALL</code> of the requirements set. In this example, the only requirement is <code>TIME DAY</code> which requires the current time in the world to be daytime. If the Requirements are met, the script defined in the <code>'Click Trigger'</code> is sent to be run. It will have the Denizen NPC chat to the player 'Welcome to the city! Isn't it beautiful in the daytime?'.
</p><p>But before the script can be triggered, it needs to be assigned.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="A_basic_assignment">A basic assignment</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>In order for a Denizen to be associated with a script, he needs to be assigned to it. The following shows a simple assignment format. 
</p><p>Assignments are defined in the Denizens node found in plugins/Denizen/assignments.yml and must be done by hand. Once you edit the config.yml, immediately save and use /denizen reload in-game.
</p>
<pre>Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
    Texts:
      No Requirements Met: 'Come back during the day!'
</pre>
<p>Let's break this down again. This assignement will work for Denizens named <code>'Steve'</code>. Triggers that involve this NPC, such as a <code>'Click Trigger'</code> will call the script named <code>'Daytime in the City'</code>. The <code>10</code> before the name is the script priority, useful when assigning multiple scripts, but we'll get into that next. If no scripts meet requirements (in this case -- if it's NOT daytime when clicking on Steve), the text defined in the <code>Texts:</code> node called 'No Requirements Met' will trigger instead. So to reiterate, if the player clicks on Steve during the daytime, the player will get a chat containing 'Welcome to the city! Isn't it beautiful in the daytime?' If the player clicks during the nighttime, since the script requirements are not met, the player will see a chat containing 'Come back during the day!'. Note that the default <code>No Requirements Met</code> text can be changed in the <code>config.yml</code>.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Multiple_Script_Assignments">Multiple Script Assignments</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>The key to Denizens being dynamic is their ability to handle multiple scripts in different situations. This is done by assigning a priority to script assignments. Let's take this example configs below to see how script priority is handled. The below code references <code>assignments.yml</code> and a <code>script.yml</code>.
</p>
<pre>---- assignments.yml ----

Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 0 Regular Joe
    - 10 Joe the Builder  

---- script.yml ----

'Regular Joe':
  Type: Trigger   
  Requirements:
    Mode: None
  Steps:
    1:
      Click Trigger:
        Script:
        - CHAT Hello &lt;PLAYER&gt;! I supply builders only!

'Joe the Builder':
  Type: Trigger   
  Requirements:
    Mode: All
    List:
    - PERMISSION modifyworld.*
  Steps:
    1:
      Click Trigger:
        Script:
        - ENGAGE
        - CHAT Hello &lt;PLAYER&gt; the Builder! Take this shovel!
        - GIVE WOOD_SPADE 1
        - FINISH
        - DISENGAGE
</pre>
<p>Denizen <code>Steve</code> has been assigned two scripts. Upon player interaction, each script is checked for met requirements. If only one script has their requirements met, it's clear what script will be returned. But what if both meet requirements? That's where the number before each script assigned comes in. Higher priority always wins. To break down this specific situation, if a player with the 'modifyworld.*' permission clicks on Steve, both scripts meet the requirements, but since the script 'Joe the Builder' has a priority of 10, and 'Regular Joe' only has a priority of 0, 'Joe the Builder' sends its script. 'Regular Joe' is simply ignored. Denizens can be issued as many scripts as you want.  If two scripts have the same priority, the first in the list will be the one to trigger, if both scripts meet their requirements.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Things_to_Note,_Thus_Far"><span id="Things_to_Note.2C_Thus_Far"></span>Things to Note, Thus Far</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Denizens with the same name use the same script assignments. The plus to this is the ability to quickly make 'generic NPCs' such as a 'Townsman' or 'Miner'.
</p><p>All the scripts and configuration nodes are in YAML. Remember! Spacing is CRITICAL when dealing with YAML files. Each parent node and sibling node should follow the spacing and formatting guidelines set forth by the YAML 1.0 standard.
</p><p>In all the examples used in this guide, 2 spaces are used for indenting.  Generally, whatever you choose should be maintained through your YAML document. No tabs are allowed in YAML files.
</p><p>In the YAML files, nodes are case sensitive! 'Scripts:' will work. 'scripts:' will not! All nodes are first letter capital, rest of the word lowercase. Scripts names follow this rule too! 
</p><p>YAML tutorials can be intimidating, but <a class="external text" href="http://wiki.ess3.net/wiki/YAML_Tutorial" rel="nofollow">this small tutorial on the Essentials wiki</a> is pretty useful for basic YAML, which is the extent of which Denizens uses.
</p>
</div></s>

<s><div class="mw-heading mw-heading2"><h2 id="Assignments_in_Detail">Assignments in Detail</h2></div></s>

<s><div class="mw-heading mw-heading2"><h2 id="Trigger_Scripts_in_detail">Trigger Scripts in detail</h2></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>The general structure of a script should always include the 'Name', 'Type', 'Requirements', and 'Steps' nodes. These are required.
</p><p>Scripts are defined in the plugins/Denizen/scripts/ folder. Any .yml file in that directory will be loaded into Denizen. For example purposes on this website, reference to script.yml is made.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="General_layout_of_a_Trigger_Script">General layout of a Trigger Script</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<pre>'Name of script':   # Name Node
  Type: Trigger     # Type Node
  Requirements:     # Requirements Node
    ...:
    ...:
      - ...
      - ...
  Steps:            # Steps Node
    ...:
      - ...
    ...:
  Options:          # Options Node
    ...:
</pre>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Name_Node">Name Node</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>This node is pretty self-explanatory, but here are some things to keep in mind.
</p>
<ul><li>Names, just like nodes are case-sensitive! <code>'This script name'</code> is different than <code>'THIS SCRIPT NAME'</code>.</li>
<li>Names that contain spaces must have single or double quotes around it. ie: <code>"This script":</code> or <code>'This script':</code> is acceptable.</li>
<li>If the name includes a single quote in it, you must use double quotes around it, or 'escape' the quote with another quote. ie: <code>"John's Script":</code> or <code>'John''s Script':</code></li></ul>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Type_Node">Type Node</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Let's Denizen know the type of script. For trigger scripts, as explained in this section, use <code>TYPE: TRIGGER</code>.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Requirements_Node">Requirements Node</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>This node sets the rules for the player to qualify for the script. There are a couple different options that you should know when using requirements. For example:
</p>
<pre>  Requirements:
    Mode: All
    List:
    - TIME Night
    - MONEY 1000000
    - STORMY
</pre>
<p>This would be a difficult script to obtain, for sure. To trigger, the time would have to be after 16000, but before 0, the player would need one million dollars on hand (or whatever economy you use), and the weather must be storming! But it shows the flexibility of requirements. First is the 'Mode'. Currently there are three different types. Second is the requirement type, with arguments if applicable.

</p>
</div></s>

<s><div class="mw-heading mw-heading5"><h5 id="Mode_Types">Mode Types</h5></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p><code>[] indicates required field
</code></p><code>
</code><ul><code></code><li><code>ALL
</code><dl><code></code><dd><code></code>Requires all requirements listed to be met.<code></code></dd></dl></li><code>
</code><li><code>ANY [#]
</code><dl><code></code><dd><code></code>Requires the specified number of requirements to be met, out of the total of requirements listed.<code></code></dd></dl></li><code>
</code><li><code>NONE
</code><dl><code></code><dd><code></code>Requires NO requirements to be met.<code></code></dd></dl></li></ul><code>
</code><p><code></code>
</p>
</div></s>

<s><div class="mw-heading mw-heading5"><h5 id="Requirements_Types">Requirements Types</h5></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p><code>[] indicates required field, () indicates an optional field, OR indicates alternative usage.
</code></p><code>
</code><ul><code></code><li><code>NAME [Player Name] (or this Player Name) ...
</code><dl><code></code><dd><code></code>Requires a specific player.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>ITEM [<a href="https://wiki.citizensnpcs.co/ITEM_NAME" title="ITEM NAME">#:#</a>] (# of that item, or more)
</code><dl><code></code><dd><code></code>Requires the player to have an item in their inventory.  You can also specify an amount.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>WEARING [<a href="https://wiki.citizensnpcs.co/ITEM_NAME" title="ITEM NAME">#</a>]
</code><dl><code></code><dd><code></code>Requires the player to be wearing a specific piece of armor.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>HOLDING [<a href="https://wiki.citizensnpcs.co/ITEM_NAME" title="ITEM NAME">#:#</a>] (# of that item, or more)
</code><dl><code></code><dd><code></code>Requires the player to have an item in their hand. You can also specify an amount.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>TIME [Day|Night|Dusk|Dawn]  OR  TIME [0-23999] [1-24000]
</code><dl><code></code><dd><code></code>Requires day or night. Alternatively you can specify a time window.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>HUNGER [Full|Hungry|Starving]
</code><dl><code></code><dd><code></code>Requires a specific hunger state.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>PRECIPITATION
</code><dl><code></code><dd><code></code>Requires a rain or snow.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>SUNNY
</code><dl><code></code><dd><code></code>Requires clear skies.  Note: This can still trigger at night as it does not check time.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>WORLD [World Name] (or this World Name) (or this World Name) ...
</code><dl><code></code><dd><code></code>Requires the player to be in a specific world, or worlds.  You can check as many as you'd like with one line.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>PERMISSION [this.permission.node] (or this permission.node) ...
</code><dl><code></code><dd><code></code>Requires one of the listed permission nodes. Only one is required. If you require multiple permission nodes, use multiple entries.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>LEVEL [This Level # or higher]  OR  LEVEL [At least this Level #] [But no more than this Level #]
</code><dl><code></code><dd><code></code>Requires a specific Minecraft XP level, or a range of levels.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>FINISHED (# of times) [Script Name]
</code><dl><code></code><dd><code></code>Requires a specific script to be <code>FINISH</code>ed. Remember: Script names are case-sensitive! You can specify a certain number of times, as well. Using this as a negative requirement is a good way to put a limit on how many times a player can do a script.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>FAILED [Script Name]
</code><dl><code></code><dd><code></code>Requires a specific script to be <code>FAIL</code>ed. Remember: Script names are case-sensitive!<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>GROUP [Name of Group] (or this Group) ...
</code><dl><code></code><dd><code></code>Requires the player be a member of a group. Requires a Permissions system that allows groups, such as PermissionsEX.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>MONEY [Amount of Money, or more]
</code><dl><code></code><dd><code></code>Requires the player to have at least a certain amount of money on hand. Requires an economy system, such as iConomy.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>POTIONEFFECT [POTION_EFFECT]
</code><dl><code></code><dd><code></code>Requires the player to be under the influence of a specific potion. You can use 'ANY' to specify the player just be under the influence of a potion, without being specific as to which type.</dd></dl></li></ul>
</div></s>

<s><div class="mw-heading mw-heading5"><h5 id="Negative_Requirements_Types">Negative Requirements Types</h5></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Requirements can also be 'negative' requirements. In the Requirements List, just place a '-' in front of the requirement to inverse its logic. For example, 'HOLDING IRON_SWORD' would require the player to be holding an Iron Sword. '-HOLDING IRON_SWORD' would require the player to NOT be holding an Iron Sword. All requirements have a negative alternative, even ones whose function overlaps, such as '-WEATHER Precipitating' and 'WEATHER Sunny' technically being the same thing. If anything, it can add to script readability.
</p>
<pre>  Requirements:
    Mode: All
    List:
    - -TIME Night
    - -MONEY 1000000
    - -STORMY
</pre>
<p>Negative requirements completely change our original example around. For this script to trigger, time needs to be Day, the weather in the current world must NOT be storming, and the player must not have more than 1000000 units of currency on them.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Steps_Node">Steps Node</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Steps are the meat of the script. They control what to listen for and what actions to take. Each script can have multiple steps, each with multiple triggers. Let's use an example.
</p>
<pre>'Welcome to Harbortown':
  Type: Trigger
  Requirements:
    Mode: NONE
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT What's your name, stranger?
      Chat Trigger:
        '1':
          Trigger: My name is /&lt;PLAYER&gt;/.
          Script:
          - CHAT Ah ha, your name sounds familiar! 
          - CHAT Are you from around this area?
          - ZAP
    '2':
      Click Trigger:
        Script:
        - HINT
      Chat Trigger:
        '1':
          Trigger: /Yes/, I grew up in Harbortown!
          Script:
          - CHAT I thought so, welcome back! 
            Have you heard about Tom the Taylor? 
            Isn't that just horrible?
          - ZAP 3 
        '2':
          Trigger: /No/, you must be mistaken. 
          Script:
          - CHAT Oh, sorry about that. 
          - CHAT Hey, if you're looking for some work, 
            Bill the Baker is understaffed! 
            This is the bakery's busy season.
          - ZAP 4
    '3':
      Click Trigger:
        Script:
        - CHAT I wonder if Tom the Taylor is doing any better.
        - NARRATE Perhaps you should check on Tom the Taylor.
    '4':
      Click Trigger:
        Script:
        - CHAT Oh, nice to see you again &lt;PLAYER&gt;!
        - CHAT Have you stopped by the bakery?
</pre>
<p>The sub-sections below reference this example.
</p>
</div></s>

<s><div class="mw-heading mw-heading5"><h5 id="Trigger_Types">Trigger Types</h5></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Steps handle the flow of commands and messages with triggers.
</p><p><b>Denizen Triggers</b> trigger from interaction with Denizens. They are defined in the Steps: node.
</p>
<ul><li><b>Click Trigger</b>s activate when the Denizen is clicked on.</li></ul>
<pre>Click Trigger:
  Script:
  - CHAT Scripts are nested as a list.
  - CHAT You can use any command that
    you'd wish.
</pre>
<p><br/>
</p>
<ul><li><b>Chat Trigger</b>s activate when players chat with Denizens. Players' chat within the configurable range will be directed to the Denizen instead of global chat. Chat also follows the configuration setting <code></code></li></ul><code>
<pre>Chat Trigger:
  '1':
    Trigger: The word needed to /Trigger/ is inside slashes. 
    Script:
    - CHAT Scripts are nested as a list.
    - CHAT You can use any command that
      you'd wish.
</pre>
</code><p><code></code>
For a list of commands, see <a href="#Script_Commands">#Script Commands</a>
</p>
</div></s>

<s><div class="mw-heading mw-heading2"><h2 id="Task_Scripts_in_detail">Task Scripts in detail</h2></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Task scripts are script that are called by either the RUNTASK command or PLAYERTASK command. These are more basic than trigger scripts since they have no requirements or step nodes. The types of commands are also more limited since there is no NPC Denizen associated with the script, but useful for certain situations.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="General_layout_of_a_Trigger_Script_2">General layout of a Trigger Script</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<pre>'Name of script':   # Name Node
  Type: Task        # Type Node
  Script:           # Script Node
  - ...
  - ...
</pre>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Using_a_Task_Script_with_RUNTASK">Using a Task Script with RUNTASK</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px">
<p>Imagine a scenario where you'd like to check a single outcome from multiple sources. Say, for instance, you have multiple 'quests' that all have the same outcome. You could check the completion for each quest, or, you could have all the quests call a Task Script and check against that.
</p><p>This is a very basic example for something that can in theory be very complex. Imagination, hoooo!
</p>
<pre>'Apple Reward': 
  Type: Task    
  Script:       
  - NARRATE You've received some APPLES. Nice!
  - GIVE APPLE 10
  - FINISH

'Apple Quest 1':
  Type: Trigger
  Requirements:
    Mode: All
    List:
    - -FINISHED Apple Reward
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT Welcome to my house, have some apples!
        - RUNTASK Apple Reward
  
'Apple Quest 2':
  Type: Trigger
  Requirements:
    Mode: All
    List:
    - -FINISHED Apple Reward
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT Welcome to my orchard, have some apples!
        - RUNTASK Apple Reward
</pre>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Using_a_Task_Script_with_PLAYERTASK">Using a Task Script with PLAYERTASK</h4></div></s>

<s>
<p>Tasks scripts are very straight forward when using with a PLAYERTASK command. The script that is called when the 'player task' is complete is a Task script.
</p>
<pre>'Graveyard Investigation':
  Type: Trigger
  Requirements:
    Mode: NONE
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT Go investigate the graveyard for me!
        - PLAYERTASK LOCATION graveyard 20 120 Graveyard Search

'Graveyard Search': 
  Type: Task    
  Script:       
  - NARRATE You are thoroughly spooked out. Maybe you should return to Dave.
  - FINISH

'Graveyard Investigated Complete':
  Type: Trigger
  Requirements:
    Mode: All
    List:
    - FINISHED Graveyard Search
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT Ahhh, dang. You couldn't find anything? Ah well, thanks for your help!
</pre>
<div class="mw-heading mw-heading2"><h2 id="Script_Commands">Script Commands</h2></div>
<div style="margin-right:2.0em; padding:10px">
<p>Note: There are plenty more to come, be patient, more are coming! Have ideas for a good command? Let me know!
</p><p><code>[] indicates required field, () indicates an optional field, OR indicates alternative usage.
</code></p><code>
</code><ul><code></code><li><code>ZAP (Step #)
</code><dl><code></code><dd><code></code>Progresses the player through the steps. ZAP used alone will progress to the next step. ZAP with a number following will progress the player to a specific step.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>FINISH
</code><dl><code></code><dd><code></code>Marks the script as completed to check against with the requirement type 'FINISHED'.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>ENGAGE
</code><dl><code></code><dd><code></code>Blocks player interaction from triggering the NPC.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>DISENGAGE
</code><dl><code></code><dd><code></code>Opens the NPC back up to player interaction.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>PLAYERTASK LOCATION [Location Bookmark] [Duration in seconds] [Block leeway] [Task Script to trigger]
</code><dl><code></code><dd><code></code>Starts a player task to the Denizen's location bookmark in which the player must stay within a certain amount of blocks (Block Leeway) for a specific duration. Once accomplished, a Task Script is called.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>FAIL
</code><dl><code></code><dd><code></code>Marks the script as failed to check against with the requirement type 'FAILED'. Note: A script can be both completed and failed!<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>RESET [FINISHED|FAILED] [Name of Script]
</code><dl><code></code><dd><code></code>Sets either FINISHED or FAILED of the specified script to False. Remember: Script names are case sensitive!<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>WAIT [# of seconds]
</code><dl><code></code><dd><code></code>Will hold a player's Command Que for a specific amount of seconds. You can use this to put delays in your script. All lines of a script after the hold will execute after the time has passed.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>LOOK [CLOSE|AWAY] or LOOK [Location Bookmark]
</code><dl><code></code><dd><code></code>Toggle 'lookclose' on the Denizen. Alternate use specifies a pitch/yaw from a Location bookmark.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>GIVE [ITEM_NAME] (Quantity)
</code><dl><code></code><dd><code></code>Denizen will drop specified items.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>TAKE [ITEM_NAME|MONEY] (Quantity)
</code><dl><code></code><dd><code></code>Takes specific item or money from the player.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>CHAT [The text to chat.]
</code><dl><code></code><dd><code></code>Makes the Denizen talk to the player. Long messages will be formatted for multiple lines automatically.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>NARRATE [The text to narrate.]
</code><dl><code></code><dd><code></code>Sends text to the player without branding the Denizen. Long messages will be formatted for multiple lines automatically.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>FOLLOW [PLAYER|NOBODY]
</code><dl><code></code><dd><code></code>Makes the Denizen follow the player, or stop following the player.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>WALKTO [Location Bookmark]
</code><dl><code></code><dd><code></code>Makes the Denizen walk to a specified location.<code></code></dd></dl></li></ul><code>
<p>Note: I've been having problems getting the NPCs to WALKTO a bookmarked location that is far away, perhaps in a different chunk? Working on it with the C2 team. I may have another workaround as well.
</p>
</code><ul><code></code><li><code>WALK [Z] [X] [Y]   Note: Z(-NORTH(2)/+SOUTH(0)) X(-WEST(1)/+EAST(3)) Y (+UP/-DOWN)
</code><dl><code></code><dd><code></code>Makes the Denizen walk. This is not for making the Denizen to specific coordinates. The values for X Y and Z will get added or subtracted from the Denizen's current location.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>RETURN
</code><dl><code></code><dd><code></code>Can be used after initiating a WALK command.  This will make the denizen return to its previous location.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>EXECUTE [ASPLAYER|ASNPC|ASSERVER] [command to execute]    Ex: EXECUTE ASSERVER toggledownfall
</code><dl><code></code><dd><code></code>Executes a command, issues from either the Player, NPC, or Server. No need for a /.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>STRIKE
</code><dl><code></code><dd><code></code>Strikes the player with lightning.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>WEATHER [Sunny|Stormy|Precipitating]
</code><dl><code></code><dd><code></code>Sets the weather for the world.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>RESPAWN [Location Bookmark]
</code><dl><code></code><dd><code></code>Despawns the Denizen and respawns it to a bookmarked location.<code></code></dd></dl></li></ul><code>
<p>Note: There is something funny going on with NPCs spawning to a location you are very near to. You sometimes have to back away before they show up. This seems to be an issue with Craftbukkit and/or Minecraft Server.
</p>
</code><ul><code></code><li><code>TELEPORT [Location Bookmark]
</code><dl><code></code><dd><code></code>Teleports the player interacting to the Denizen's specified Location Bookmark/ <code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>SPAWN [ENTITY_TYPE] [AMOUNT] (Location Bookmark)
</code><dl><code></code><dd><code></code>Spawns a specified amount of entities. If the location bookmark is missing, they will spawn near the Denizen.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>PERMISS [permission.node.to.add]
</code><dl><code></code><dd><code></code>Gives to the player interacting the specified permission node for the current world.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>REFUSE [permission.node.to.take]
</code><dl><code></code><dd><code></code>Takes from the player interacting the specified permission node for the current world.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>CAST [POTION_TYPE] [Duration in seconds] [Amplifier]
</code><dl><code></code><dd><code></code>Gives the player interacting a potion effect. Note: <a href="https://wiki.citizensnpcs.co/Alchemist#Valid_Effects" title="Alchemist"> Valid potion types are the same as the Alchemist's.</a> Amplifier specifies 'level, strength, or duration', depending on the type of potion effect. Try 1-5 for most types.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>SWITCH [Block Bookmark]
</code><dl><code></code><dd><code></code>If a lever is found at the block location, it will be switched ON or OFF.<code></code></dd></dl></li></ul><code>
</code><ul><code></code><li><code>PRESS [Block Bookmark]
</code><dl><code></code><dd><code></code>If a button is found at the block location, it will be pressed. Note: You may need a - WAIT 1 and a 2nd - PRESS [Block Bookmark] or the Denizen will hold the button.<code></code></dd></dl></li></ul><code>
</code><p><code></code>
</p>
</div>
<div class="mw-heading mw-heading2"><h2 id="Denizen_in-game_bukkit_commands">Denizen in-game bukkit commands</h2></div>
<div style="margin-right:2.0em; padding:10px">
<p><code>/denizen reload|save</code>
</p>
<ul><li>Reloads|saves the config.yml and scripts.yml. Useful for testing scripts without rebooting your server.</li></ul>
<p><code>/denizen bookmark location [name]</code>
</p>
<ul><li>Stores a location to the selected Denizen for use with script commands such as RESPAWN and WALKTO. Note: Names can only be one word, and are unique to the Denizen.</li></ul>
<p><code>/denizen bookmark block [name]</code>
</p>
<ul><li>Stores the Player crosshair's block location to the selected Denizen for use with script commands such as SWITCH. Note: Names can only be one word, and are unique to the Denizen.</li></ul>
<p><code>/denizen adddata|decdata|getdata</code>
</p>
<ul><li>Nothing to do with Denizens, really, but handy for checking/switching block data. Try it on a tree.</li></ul>
<p><code>/denizen version</code>
</p>
<ul><li>Gives you an approximation of what build you are using. I'll probably ask you this if you come to #citizens for any tech support.</li></ul>
</div></s>
