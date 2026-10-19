For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

## List of commands

<s><big><div style="color:red">Denizen is continuously being updated. This page shows only basic script commands (We will try to update the page when something changes)!</div></big></s>

<s><div class="mw-heading mw-heading3"><h3 id="Entity">Entity</h3></div></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="cast">cast</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">cast
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[effect] (duration:#{60s}) (power:#{1}) (target(s):npc|player|n@&lt;npc.id&gt;|p@&lt;player.name&gt;|entity_name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Gives a potion effect to a target, which can be a player, an NPC or another entity. All valid potion effect names are found <a class="external text" href="http://jd.bukkit.org/rb/apidocs/org/bukkit/potion/PotionEffectType.html" rel="nofollow">here</a>.
<p>If you do not choose a target, the potion effect is given to the player talking to this NPC. You can use more targets at once by putting them between | characters.
</p><p>You can choose the effect's duration, which is 60 seconds by default, and its power, which is 1 by default. Often, a power of 3 is the most you can have for a potion effect, and a value greater than that will not do anything.
</p><p><br/>
<b>Examples</b>
</p>
<pre>- cast blindness power:3 duration:7
</pre>
<p>In the above example, the player talking to this NPC will be blinded strongly for 7 seconds.
</p>
<pre>- cast regeneration power:1 duration:10 target:p@&lt;npc.owner&gt;
</pre>
<p>In this example, the NPC will give a weak regeneration effect to its owner for 10 seconds.
</p><p><br/>
</p>
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading3"><h3 id="Item">Item</h3></div></s>

<s><div class="mw-heading mw-heading3"><h3 id="NPC">NPC</h3></div></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="assignment">assignment</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">assignment
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[{set}|remove] (script:name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Sets or removes an assignment for the NPC. If set or remove aren't specified, it will set by default.
<p><br/>
<b>Examples</b>
</p>
<pre>- assignment set "script:Evil Wizard"
- assignment remove
- assignment "script:Pet Cat"
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="attack">attack</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">attack
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(stop)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Makes the NPC attack or stop attacking the player.
<p><br/>
<b>Examples</b>
</p>
<pre>- attack
- attack stop
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="chat">chat</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">chat
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">["&lt;text&gt;"] (no_target/targets:&lt;entity&gt;|...)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Sends a message from this NPC to the player.
<p>If a different NPC's ID is chosen in the npcid argument, the message is sent from that NPC. The message can also be sent to a different player or even to another NPC if you use the target argument.
</p><p><br/>
<b>Examples</b>
</p>
<pre>- chat "It's nice to see you again, &lt;player.name&gt;."
- chat "I would like to introduce you to &lt;player.name&gt;." target:n@7
- chat "Bob, do you know &lt;player.name&gt;?" target:p@Bob
- chat npcid:9 "Our enemy is giving orders to his companion." target:p@Bob
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="follow">follow</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">follow
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(stop)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Makes the NPC follow or stop following the player.
<p><br/>
<b>Examples</b>
</p>
<pre>- follow
- follow stop
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="look">look</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">look
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[location:x,y,z,world]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Makes the NPC look towards a certain location.
<p><br/>
<b>Examples</b>
</p>
<pre>- look location:300,60,500,world
- look location:&lt;player.location&gt;
- look location:&lt;anchor:Lever&gt;
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="shoot">shoot</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">shoot
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[entity:name] (ride) (burn) (explode) (location:x,y,z,world) (script:name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Makes the NPC shoot out an entity. All valid entity names are found <a class="external text" href="http://jd.bukkit.org/rb/apidocs/org/bukkit/entity/EntityType.html" rel="nofollow">here</a>.
<p>Entities can be shot towards a location. If no location is specified, they will be shot in the direction the NPC is looking. You can also choose a script that will be run when the entity reaches the location.
</p><p>Moreover, you can use the ride argument to ride an entity, the burn one to set it on fire, and the explode one to have it explode once it reaches the location or gets stuck.
</p><p><b>Examples</b>
</p>
<pre>- shoot entity:zombie
- shoot entity:arrow location:&lt;player.location&gt;
- shoot entity:fireball location:&lt;player.location&gt; "script:Shoot Another Fireball"
- shoot entity:minecart ride location:&lt;anchor:Rollercoaster&gt;
- shoot entity:cow ride burn explode location:&lt;anchor:Hill&gt; "script:Bovine Destruction"
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="sit">sit</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">sit
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(sit|stand) (location:x,y,z,world)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Makes the NPC sit or stand at a location.
<p><br/>
<b>Examples</b>
</p>
<pre>- sit location:300,65,300,world
- sit location:&lt;anchor:Chair&gt;
- stand
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="trigger">trigger</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">trigger
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[name:chat/click/damage/proximity] (state:true/false) (cooldown:&lt;#.#&gt;) (radius:&lt;#&gt;)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Enables or disables an interact trigger.
<p>Use this command to enable or disable an interact trigger, usually in the <a class="external text" href="http://wiki.citizensnpcs.com/Denizen/Types_of_Scripts#Assignment_Script" rel="nofollow">assignment script</a>.
</p><p><b>Examples</b>
</p>
<pre>- trigger name:chat state:true
- trigger name:proximity statue:true radius:10
</pre>
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading3"><h3 id="Player">Player</h3></div></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="feed">feed</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">feed
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(amt:#) (target:npc|{player})
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Fills the player's food bar, or this NPC's food bar if the NPC is specified as the target. An amount can also be set by which the player or NPC will be fed. A completely full food bar has an amount of 20. Thus, an amount of 1 is half a shank in the food bar.
<p><br/>
<b>Examples</b>
</p>
<pre>- feed
- feed amt:15 target:npc
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="heal">heal</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">heal
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(amt:#) (target:npc|{player})
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Fills the player's health bar, or this NPC's health bar if the NPC is specified as the target. An amount can also be set by which the player or NPC will be healed. A completely full health bar has an amount of 20. Thus, an amount of 1 is half a heart in the health bar.
<p><br/>
<b>Examples</b>
</p>
<pre>- heal
- heal amt:7 target:npc
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="narrate">narrate</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">narrate
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">["narration text"] (player:name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Sends a message to this player, or to another player if one is specified.
<p><br/>
<b>Examples</b>
</p>
<pre>- narrate "A musty odor hangs in the air and you can hear the distant sound of trickling sewer water."
- narrate player:Bob "&lt;player.name&gt; has been hired to track you down!"
</pre>
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading3"><h3 id="Script_flow">Script flow</h3></div></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="anchor">anchor</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">anchor
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[id:name] [assume|add|remove|walkto|walknear] (range:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Assumes, Adds, Removes and orders an NPC to walkto or to walknear an anchor that has been specified using the Citizens 2 npc command
<p>"/npc anchor" Allows for dynamic specified pathing based on predefined points. Allows for a specified range in which the NPC in question 
can walk to an anchor point.
</p><p><br/>
<b>Examples</b>
</p>
<pre>A command having an NPC assume an Anchor:
- anchor id:postoffice assume range:20
-------------------------------------
Two commands demonstrating how one may add an anchor based on the NPC's location:
- Chat "Wow &lt;player.name&gt;, Now that I've walked to this location I am going to create an anchor point at this location so 
  I can walk back here later."
- anchor id:example_anchor add
-------------------------------------
Two commands demonstrating how one may remove a specified anchor via an NPC"
- chat "You know &lt;player.name&gt;, I actually don't think I'll ever need to return here again, I will delete this anchor point"
- anchor id:example_anchor remove
-------------------------------------
An example of a command for an NPC to walk towards a specified anchor point. Walkto has the NPC walk directly to the point; 
whereas Walknear has the npc be less precise when walking to the point:
- anchor id:Treasure_Chest walkto range:30
- anchor id:Wheat_Fields walknear
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="queue">queue</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">queue
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(queue:&lt;id&gt;) [clear/pause/resume/delay:&lt;#&gt;]
<p><b>WARNING THIS COMMAND IS DEPRECATED, ALL SCRIPTWRITERS SHOULD NOW USE THE QUEUE COMMAND</b>
</p>
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Empties a queue of all the commands in it that haven't been executed. If no queue name is specified, the current queue is emptied. You can also use the queue argument more than once to specify more queues to empty.
<p>Use this command to stop a script from another script or a script from an action.
</p><p><b>Examples</b>
</p>
<pre>- queue queue:magicalattacks clear
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="cooldown">cooldown</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">cooldown
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(duration:#{60s}) (global|player:name{attached player}) (script:name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Makes this script not get executed again by this player for a duration of time, which is 60 seconds by default.
<p>You can also make the script not get executed for another player, or make it unavailable globally, and you can also choose another script instead of this one.
</p><p><br/>
<b>Examples</b>
</p>
<pre>- cooldown
- cooldown duration:30s player:Bob "script:Offer Quest"
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="define">define</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">define
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[&lt;id&gt;] [&lt;value&gt;]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Similar to a flag, this command sets a global variable to any value that can later be called back anywhere by using %id%.
<p><br/>
<b>Examples</b>
</p>
<pre>- define "lastplayer" "&lt;player.name&gt;"
- define "player_&lt;player.name&gt;'s_home" "&lt;player.location&gt;"
- announce "%lastplayer% set their home at %player_&lt;player.name&gt;'s_home%! Go raid it!"
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="determine">determine</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">determine
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">["value"]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">This command only works together with the <a href="https://wiki.citizensnpcs.co/Denizen/Replaceable_Tags#procedure" title="Denizen/Replaceable Tags">procedure</a> replaceable tag. It is put in the procedure script run by the tag and sets the tag's value to anything you choose. It is generally used as the result of an <a href="#if">if</a> command or together with the <a href="#random">random</a> command.
<p><br/>
<b>Examples</b>
</p>
<pre>- if &lt;player.name&gt; == "Bob" determine "Bobby"
- if &lt;flag.p:Enemy&gt; == "Galerion" determine "the fearsome Galerion"
  else if &lt;flag.p:Enemy&gt; == "Narkon" determine "the evil Narkon"
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="disengage">disengage</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">disengage
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(npcid:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Stops an <a href="#engage">engage</a> command used formerly on this NPC. If the npcid is specified, a different NPC can be disengaged.
<p><br/>
<b>Examples</b>
</p>
<pre>- disengage
- disengage npcid:8
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="engage">engage</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">engage
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(duration:#) (npcid:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Temporarily deactivates this NPC's triggers, making it impossible for players to interact with it for the chosen duration or until the <a href="#disengage">disengage</a> command is used on it. If the npcid is specified, a different NPC can be engaged.
<p><br/>
<b>Examples</b>
</p>
<pre>- engage
- engage duration:40s npcid:7
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="fail">fail</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">fail
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(script:script_name{attached script}) (player:name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Adds 1 to the number of times this script or another script has been failed by this player, or by another player if one is specified. You can then check the times a script has been failed using the <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Script_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/Script Requirements (page does not exist)">script</a> requirement.
<p><br/>
<b>Examples</b>
</p>
<pre>- fail
- fail "script:Defend the Castle" player:Bob
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="finish">finish</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">finish
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(script:script_name{attached script}") (player:name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Adds 1 to the number of times this script or another script has been finished by this player, or by another player if one is specified. You can then check the times a script has been finished using the <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Script_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/Script Requirements (page does not exist)">script</a> requirement.
<p><br/>
<b>Examples</b>
</p>
<pre>- finish
- finish "script:Siege the Castle" player:Bob
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="flag">flag</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">flag
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">({player}|npc|global) [name([#])](:action)[:value] (duration:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Sets the value of a flag, a variable that can be checked elsewhere in this script and in other scripts by using <a href="https://wiki.citizensnpcs.co/Denizen/Replaceable_Tags#Flags" title="Denizen/Replaceable Tags">flag replaceable tags</a> or the <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Script_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/Script Requirements (page does not exist)">flagged requirement</a>.
<p>A flag can be placed on the player, the NPC or globally. Flags placed on a player only apply to that player, and flags placed on an NPC only apply to that individual NPC based on its ID, so NPCs with the same name have different flags because they have different IDs. However, a global flag applies to the entire server and can easily be read from any script.
</p><p>If a flag's type (player, npc or global) is not specified, the flag is placed on the player by default, and if a value for the flag is not specified, the value is "true" by default.
</p><p>For more info, <a href="https://wiki.citizensnpcs.co/Denizen/Commands/Flag" title="Denizen/Commands/Flag">click here</a>.
</p><p><b>Examples</b>
</p>
<pre>- flag "Finished Baker's Quest"
- flag global "Skeleton Invasion Ended"
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="if">if</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">if
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[&lt;value&gt;] (!)(&lt;operator&gt; &lt;value&gt;) (&amp;&amp;/|| ...) [&lt;commands&gt;] (else &lt;commands&gt;)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Compares one value to another and if the outcome is true, the commands inside the 'if' statement will be run and no more comparables will be checked. If it is false, the next 'else if', if there is one, will be compared, and if that is true, the commands in that 'else if' will be run and no more comparables will be checked. This will continue happening until the script either runs out of comparables or reaches an 'else', in which case the commands inside the 'else' will be run and the script will continue.
<p>For more info, <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Commands/If&amp;action=edit&amp;redlink=1" title="Denizen/Commands/If (page does not exist)">click here</a>.
</p><p><b>Examples</b>
</p>
<pre>- if "&lt;player.inventory.contains[1]&gt; announce "Hahaha! &lt;player.name&gt; has no stone!"
- if &lt;player.name&gt; == "davidcernat" execute as_server "ban &lt;player.name&gt;"
- if &lt;context.message.contains[Bob]&gt; announce "&lt;player.name&gt; said Bob! Smite them!"
  else if &lt;player.name.contains[Bob]&gt; announce "&lt;player.name&gt;'s name contains Bob! Smite them!"
  else {
    - announce "No mention of Bob can be found. Proceeding with life..."
    - run Life delay:0s
  }
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="log">log</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">log
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[&lt;text&gt;] (type:severe/info/warning/fine/finer/finest) [file:&lt;name&gt;]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Logs whatever text you want into a file inside the main server folder. If the file doesn't exist, it will create it.
<p><br/>
<b>Examples</b>
</p>
<pre>- log "Something happened!" "file:Denizen.log"
- log "Bob punched Joe!" "file:logs/DenizenLog.txt"
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="random">random</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">random
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[#]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Runs a single one out of a number of commands, chosen at random.
<p><br/>
<b>Examples</b>
</p>
<pre>- random 3
- chat "One."
- chat "Two."
- chat "Three."
</pre>
<p>In the above example, only one of the three chat commands will be run.
</p>
<pre>- random 2
- chat "One."
- chat "Two."
- chat "Three."
</pre>
<p>In this example, either "One" or "Two" will be displayed, but "Three" will always be displayed.
</p>
<pre>- random 3
- attack
- chat "Get out of here!"
- runtask "script:Call Reinforcements"
</pre>
<p>Here, the NPC will either attack the player, tell the player to leave, or run a script in which it calls for reinforcements.
</p>
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading3"><h3 id="Server">Server</h3></div></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="announce">announce</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">announce
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">["announcement text"] (to_ops)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Sends a message to every player on the server. If the to_ops argument is used, the message is sent only to operators.
<p><br/>
<b>Examples</b>
</p>
<pre>- announce "The skeleton invasion has ended."
- announce "&lt;player.name&gt; has joined the blue team!"
- announce to_ops "&lt;player.name&gt; is requesting help from operators."
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="chunkload">chunkload</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">chunkload
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">({add}|remove|removeall) [location:x,y,z,world] (duration:{-1s})
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Loads the chunk of the location as specified into the server memory so that it does not despawn. NPCs do not stay spawned if a chunk
<p>despawns. As such this command is useful for ensuring a NPC spawn and do what it ought to regardless if a player is around to keep
the chunk that that NPC is in, spawned. This command allows for adding of a chunk to memory by specifying a block location within a chunk, removing a chunk loaded to memory by also specifying a location within the chunk, as well as the ability to remove all chunks
currently loaded into server memory by this command (removeall). Additionally a duration can be set in which a chunk loaded into memory
will automatically despawn; the default is set to -1 meaning the chunk will stay loaded until the chunkload command is used again
to remove it from memory.
</p><p><b>This does not create nor delete new or already generated chunks of terrain it merely brings it into memory for the server so that</b>
an NPC may spawn regardless if someone is around<b></b>
</p><p><b>Examples</b>
</p>
<pre>- chunkload add location:1000,64,1000,world duration:-1s
- chunkload add location:323,4,745,creative_world duration:10m
- chunkload remove location: 1000,64,1000,world
- chunkload removeall
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="execute">execute</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">execute
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[as_player|as_op|as_npc|as_server] ["Bukkit command"]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Executes a Bukkit command on behalf of the player (as_player), the player as an operator (as_op), the NPC as an operator (as_npc), or the server (as_server).
<p>Any Bukkit command that you can use in the server console or in the chat with a slash works here. You can thus use the execute command to make NPCs that act as interfaces for other plugins.
</p><p><br/>
<b>Examples</b>
</p>
<pre>- execute as_player "home"
- execute as_op "gamemode 1"
- execute as_npc "spawnmob zombie 3"
- execute as_server "jail &lt;player.name&gt;"
</pre>
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading3"><h3 id="World">World</h3></div></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="animatechest">animatechest</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">animatechest
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[location:x,y,z,world] ({open}|close) (sound:{true}|false)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Causes a chest located at the specified coordinates to animate as either open or closed; defaults to open if not specified. Allows for the animated chest to play the "open chest" sound (true) or to open silently (false); defaults to true. <b>There must be a chest located at the coordinates, this command does not spawn a chest.</b>
<p><b>Examples</b>
</p>
<pre>- animatechest location:1000,63,1000,world open sound:true
- animatechest location:100,74,777,world close sound:false
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="copyblock">copyblock</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">copyblock
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[location:x,y,z,world] [to:x,y,z,world]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Simply copies whatever type of block is at one location and essentially pastes it at another defined location.
<p><b>Examples</b>
</p>
<pre>- copyblock location:204,68,12,world to:55,64,100,castle_world
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="displayitem">displayitem</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">displayitem
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[item_name|remove] [location:x,y,z,world] (duration:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Has the server create a "Phantom Item" at the specified location which will remain there until removed. The Phantom Item
<p>only appears to the player and cannot be picked up by the player. Currently the "Duration:#" setting is unreliable and as such 
players should expect to have to use the "- displayitem remove" command if they wish to remove the displayed item.
</p><p><b>Examples</b>
</p>
<pre>- displayitem 10 location:77,64,2453,world duration:20s
- displayitem Stick location:&lt;player.location&gt;
- displayitem remove location:77,64,2453,world
- displayitem remove location:&lt;player.location&gt;
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="drop">drop</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">drop
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[item:#(:#)|item:material(:#)|xp] (qty:#{1}) (location:x,y,z,world)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Drops an item or some experience at a location, in a certain quantity (which is 1 if not specified). You can choose either the item's ID or its material. All block and item IDs are found <a class="external text" href="http://www.minecraftwiki.net/wiki/Data_values" rel="nofollow">here</a> and all valid material names are found <a class="external text" href="http://jd.bukkit.org/rb/apidocs/org/bukkit/Material.html" rel="nofollow">here</a>.
<p>The ID or material can also be followed by a <a class="external text" href="http://www.minecraftwiki.net/wiki/Data_values#Data" rel="nofollow">special data value</a> for the item, so you can - for instance - drop a specific kind of wood or color of wool.
</p><p><b>Examples</b>
</p>
<pre>- drop item:38 location:500,63,500,world
- drop item:diamond qty:5 location:&lt;anchor:Treasury&gt;
- drop xp qty:30 location:&lt;anchor:Altar&gt;
- drop item:wood:3 qty:30 location:&lt;anchor:Jungle&gt;
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="strike">strike</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">strike
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(no_damage) [location:x,y,z,world]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Makes lightning strike a location, optionally without causing any damage.
<p><br/>
<b>Examples</b>
</p>
<pre>- strike location:200,73,200,world
- strike location:&lt;player.location&gt;
- strike no_damage location:&lt;anchor:Mountaintop&gt;
</pre>
</td></tr></tbody></table></s>

<s><div style="display: none;">
<div class="mw-heading mw-heading4"><h4 id="switch">switch</h4></div>
</div></s>

<s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%">
<tbody><tr>
<th align="center" scope="col">switch
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[location:x,y,z,world] (state:[{toggle}|on|off]) (duration:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">Changes the state of the lever, stone button, stone plate, wood plate, wooden door, iron door or trap door at the specified location. By default the state is toggled from on/open to off/closed and back again, but you can choose to set the state just to on or off. You can also specify a duration for which the state will remain like that.
<p><br/>
<b>Examples</b>
</p>
<pre>- switch location:500,45,700,world
- switch state:on location:&lt;anchor:Secret Lever&gt; duration:30
</pre>
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading1"><h1 id="Creating_your_own_Denizen_command">Creating your own Denizen command</h1></div></s>

~~Aufdemrand made a tutorial for the 0.9 version of Denizen on how to create a new command for denizen.
Check it out here: [Denizen 0.9 Command Tutorial](https://www.youtube.com/watch?v=Sd7zoWT24Xw).~~
