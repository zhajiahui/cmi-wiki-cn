For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

<s><div class="mw-heading mw-heading2"><h2 id="Interact_Scripts">Interact Scripts</h2></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>Scripts are defined in the plugins/Denizen/scripts/ folder. Any .yml file in that directory will be loaded into Denizen. For example purposes on this website, reference to script.yml is made, but again, jimbobjoe.yml or 'skeeter the cat.yml' would work just the same..
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="General_layout_of_an_Interact_Script">General layout of an Interact Script</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>This small 'outline' below shows the general layout of an Interact Script. Remember: SPACING is INCREDIBLY important with YML. If you are receiving a <code>SnakeYML</code> error in your console when working with any YML file, 99% of the time it is because of bad spacing or a missing ':' colon. YAML tutorials can be intimidating, but <a class="external text" href="http://ess.khhq.net/wiki/YAML_Tutorial" rel="nofollow">this small tutorial</a> on the Essentials wiki is pretty useful for basic YAML, which is the extent of which Denizens uses.
</p>
<pre>'Name of script':   # Name Node
  Type: Interact    # Type Node
  Requirements:     # Requirements Node
    Mode: ...
    List: 
    - ...
    - ...
  Steps:            # Steps Node
   1:               # Step Node
    Some Trigger:   # Trigger Node
      Trigger: ...
      Script:     # Script Node
        - ...
        - ...
     Another Trigger:
      Script:
        - ...
        - ...
</pre>
<p>For information on what goes in Requirements and Steps, keep reading. What is show above is just a an outline of the correct spacing, not a valid script! Let's take a look at a few small scripts, below.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="A_few_small_scripts">A few small scripts</h4></div></s>

~~...just to get a small look of some basic ways to use scripts. The rest of this document will go into detail about the specifics of each part. Some of the functionality described may require additional reading.

This scripts below is a neat little way to leave a hint. Upon a Player coming into proximity, this script will trigger the NPC looking at a target while holding a small conversation with the player.~~

<s><pre>"A Hint in the Sky":
  Type: Interact   
  Requirements:
    Mode: None
  Steps:
    1:
      Proximity Trigger:
        Script:
        - ^COOLDOWN 15
        - LOOK CLOSE
        - ^CHAT "Look up there! What could that possibly be used for?"
        - LOOK BOOKMARK:upthere DURATION:10
        - WAIT 1
        - CHAT "If only I could figure out how to make it, I can't find any stairs!"
</pre></s>

~~Below is a script for a nice fellow who will help an adventurer out in the night-time. Keep in mind that Interact Scripts only define one set of rules for a Denizen NPC... player-interaction. Imagine this next script combined with some activities that make the Denizen NPC scope out and wander an area in some woods.~~

<s><pre>"Night-time Helper":
  Type: Interact
  Requirements:
    Mode: All
    List:
    - TIME NIGHT
  Steps:
    1:
      Click Trigger:
        Script:
        - ^ZAP DURATION:60
        - ENGAGE DURATION: 5
        - LOOK CLOSE DURATION:5
        - CHAT "It's dark out here, man!"
        - CHAT "You really gotta watch out for those Zombies... they're all over the place!"
    2:
      Click Trigger:
        Script:
        - ^COOLDOWN 3600
        - LOOK CLOSE DURATION:5
        - CHAT "You again, eh? Hey man.. you need some torches?"
        - WAIT 1
        - GIVE TORCH QTY:12
</pre></s>

~~Scripts can also start a story-line of adventures, all activated by scripts working together, thanks to the FLAG, FAIL, and FINISH commands. This small script below could be the start of a Quest, with two different outcomes, if utilized properly.~~

<s><div class="mw-heading mw-heading4"><h4 id="Name_Node">Name Node</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>This node is pretty self-explanatory, but here are some things to keep in mind.
</p>
<ul><li>Names, just like nodes are case-sensitive! <code>'This script name'</code> is different than <code>'THIS SCRIPT NAME'</code>.</li>
<li>Names that contain spaces should have single or double quotes around it. ie: <code>"This script":</code> or <code>'This script':</code> is acceptable.</li>
<li>If the name includes a single quote in it, you must use double quotes around it, or 'escape' the quote with another quote. ie: <code>"John's Script":</code> or <code>'John''s Script':</code></li></ul>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Type_Node">Type Node</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>Let's Denizen and you to easily know the type of script. For interact scripts, as explained in this section, use <code>TYPE: INTERACT</code>. For reference, there are also TASK scripts and ACTIVITY scripts, which are covered in their appropriate sections.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Requirements_Node">Requirements Node</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>This node sets the rules for the player to qualify for the script. There are a couple different options that you should know when using requirements. For example:
</p><p><code>
</code></p><code>
<pre> Requirements:
   Mode: All
   List:
   - TIME Night
   - MONEY 1000000
   - STORMY
</pre>
</code><p><code></code>
</p><p>This would be a difficult script to obtain, for sure. To trigger, the time must be night-time, the player would need one million units of currency, and the weather must be storming, but it shows the flexibility of requirements. First is the 'Mode'. Currently there are three different types. Second is the requirement type, with arguments if applicable.

</p><p><br/>
</p>
<div class="mw-heading mw-heading5"><h5 id="Requirements_Mode">Requirements Mode</h5></div>
<div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p><code>[] indicates required field.</code>
</p>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="17%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:white; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>ALL
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">    Requires all requirements listed to be met.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="17%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:white; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>ANY #
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">    Requires the specified number of requirements to be met out of the total of requirements.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="17%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:white; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>NONE
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">    No requirements need to be met. There is also no need to have a <tt>LIST</tt> node if using <tt>NONE</tt>.
 </div>
</td></tr></tbody></table>
</div>
</div>
<div class="mw-heading mw-heading5"><h5 id="Requirements">Requirements</h5></div>
<div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>Denizen has a large assortment of Requirements at your disposal. For a complete list, and information on those requirements,
see: <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Interact_Requirements" title="Denizen/0.7/Interact Scripts/Interact Requirements">Denizen/0.7/Interact Scripts/Interact Requirements</a>
</p><p>Remember, requirements are also easily extensible by plugin programmers, or maybe even you!<br/>
See: <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Interact_Scripts/Custom_Interact_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Interact Scripts/Custom Interact Requirements (page does not exist)">Denizen/0.7/Interact Scripts/Custom Interact Requirements</a>
</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="Steps_Node">Steps Node</h4></div>
<div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>Each script can have multiple steps, each with multiple triggers. A player can only ever be on 1 step for a script. When a script is selected to run, a query is made to the Denizen saves to see if the Player has completed any steps. If no entry is found, the player starts on Step 1. 
</p><p>Here's an example of s script making good use of steps. Note the ZAP command is what moves a player from one step to the next, it is NOT automatic!
</p>
<pre>'Welcome to Harbortown':
  Type: Interact
  Requirements:
    Mode: NONE
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT "What's your name, stranger?"
      Chat Trigger:
        '1':
          Trigger: My name is /&lt;PLAYER&gt;/.
          Script:
          - CHAT "Ah ha, your name sounds familiar!"
          - CHAT "Are you from around this area?"
          - ZAP
    '2':
      Click Trigger:
        Script:
        - HINT
      Chat Trigger:
        '1':
          Trigger: /Yes/, I grew up in Harbortown!
          Script:
          - CHAT "I thought so, welcome back! 
            Have you heard about Tom the Taylor? 
            Isn't that just horrible?"
          - ZAP 3 
        '2':
          Trigger: /No/, you must be mistaken. 
          Script:
          - CHAT "Oh, sorry about that." 
          - CHAT "Hey, if you're looking for some work, 
            Bill the Baker is understaffed! 
            This is the bakery's busy season."
          - ZAP 4
    '3':
      Click Trigger:
        Script:
        - CHAT "I wonder if Tom the Taylor is doing any better."
        - NARRATE "Perhaps you should check on Tom the Taylor."
    '4':
      Click Trigger:
        Script:
        - CHAT "Oh, nice to see you again &lt;PLAYER&gt;!"
        - CHAT "Have you stopped by the bakery?"
</pre>
</div>
<ul><li>For a list of the available Triggers see <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Triggers" title="Denizen/0.7/Interact Scripts/Triggers">Triggers</a></li>
<li>For a list of the available Commands see <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Commands" title="Denizen/0.7/Interact Scripts/Commands">Commands</a></li></ul>
<div class="mw-heading mw-heading2"><h2 id="Assigning">Assigning</h2></div>
<p>See <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Assignments#Interact_Assignment" title="Denizen/0.7/Assignments">Denizen/0.7/Assignments#Interact_Assignment</a>
</p><p><br/>
</p>
</div></s>
