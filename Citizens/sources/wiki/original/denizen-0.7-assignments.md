For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

<s><div style="font-family:museo-sans; font-size:110%;">
<div class="mw-heading mw-heading2"><h2 id="Interact_Assignment">Interact Assignment</h2></div>
<p>Before a Denizen can run a script, it needs to be assigned first. 
</p><p>Assignments are defined in <b><code>plugins\Denizen\assignments.yml </code></b>
</p><p>This yaml file contains a single node called 'Denizens' and each Denizen gets its own entry under this node.
</p><p>Assignments must be made by hand. We recommend a good text editor like [<a class="external text" href="http://notepad-plus-plus.org/" rel="nofollow">Notepad++</a>]
</p><p>Here is a very basic example, assigning a single <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Interact_Scripts&amp;action=edit&amp;redlink=1" title="Denizen/Interact Scripts (page does not exist)">interact script</a> to a Denizen named Steve.
</p>
<pre>---- assignments.yml ----
Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
</pre>
<p>Let's break this down. 
</p><p>If you are unfamiliar with yaml, first read <a href="https://wiki.citizensnpcs.co/YAML" title="YAML">this</a> and then note 'Interact Scripts:' contains a yaml <b>list</b>. Each item in the list is prefixed with '-'. indentation and spacing is important.
</p><p>This assignment will work for Denizens named <code>'Steve'</code>. <span style="background: white; color: red">Denizen NPC names are case-sensitive!</span> Triggers that involve this NPC, such as a <code>'Click Trigger'</code> will now attempt to call the script named <code>'Daytime in the City'</code>. 
</p><p>The <code>10</code> before the name is the <b>script priority</b>, useful when assigning multiple scripts.
</p><p>If you wanted to assign this same script to another NPC, you would make another entry like this:
</p>
<pre>---- assignments.yml ----
Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
  'Bob':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
</pre>
<p>Now Bob and Steve both have this one script assigned to them.
</p><p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="Multiple_Scripts">Multiple Scripts</h4></div>
<p>The key to Denizens being dynamic is their ability to handle multiple scripts in different situations. Denizens can be assigned multiple interact scripts with varying requirements, changing their behavior based on player, npc, and world conditions.
</p><p>The important thing to remember is that:
</p><p><b>For each interaction with a Denizen: ONE, and only ONE script is picked to run.</b>
</p><p>Which script gets picked is based on several factors: 
</p>
<ul><li>Each script's <b><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Interact_Scripts/Interact_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/Interact Scripts/Interact Requirements (page does not exist)">Requirements</a></b></li>
<li>Each script assignment's <b>priority</b></li>
<li>Which <b>triggers</b> are defined on the script's active step for this player. (Advanced usage, see <a href="#Overlay_Assignment_Mode">#Overlay Assignment Mode</a>)</li></ul>
<p>Ignoring that last item for now, the process goes like this:
</p><p>Starting from highest priority and working towards the lowest, the Denizen engine checks each script's Requirements.
The first script found that meets requirements is picked.
</p><p>Let's look at an example. 
</p>
<pre>---- assignments.yml ----

Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 0 Regular Joe
    - 10 Joe the Builder  

---- script.yml ----

'Regular Joe':
  Type: Interact   
  Requirements:
    Mode: None
  Steps:
    1:
      Click Trigger:
        Script:
        - CHAT "Hello &lt;PLAYER&gt;! I supply builders only!"

'Joe the Builder':
  Type: Interact  
  Requirements:
    Mode: All
    List:
    - PERMISSION modifyworld.*
  Steps:
    1:
      Click Trigger:
        Script:
        - ENGAGE
        - CHAT "Hello &lt;PLAYER&gt; the Builder! Take this shovel!"
        - GIVE WOOD_SPADE QTY:1
        - FINISH
        - DISENGAGE
</pre>
<p>Denizen <code>Steve</code> has now been assigned two scripts. Upon player interaction, both scripts are checked for met requirements in order of descending priority. Since the "Regular Joe" script has NO requirements at all, it will ALWAYS get picked before scripts of lower priority. This is why you can see in this example we gave it a priority of 0.
</p><p>What if both scripts had a priority of 0? In that case the first script to appear in the list would get picked. It's always best to give each assigned script a different priority to avoid any confusion.
</p>
<div class="mw-heading mw-heading4"><h4 id="Overlay_Assignment_Mode">Overlay Assignment Mode</h4></div>
<p><span style="background: white; color: red">Advanced usage!</span> Overlay Script Assignments are new in 0.7 and open a wide array of new possibilities with multiple script interaction. This is completely optional, and probably should be ignored if you are a first time user and instead be revisited when you start to master Denizen Scripting.
</p><p>Normally, requirement-matching scripts are selected to run regardless of whether or not an actual matching trigger exists. If no matching trigger exists on the active step for the player, either nothing happens or some default text is shown, depending on the type of trigger.
</p><p>With an Overlay Assignment, <b>the defined triggers become a part of the requirements for selection.</b>
</p><p>A script assigned with this option will <b>never</b> be selected for a trigger type it cannot process. This makes it easy to tack-on script assignments that only handle one trigger type, without having to mash it in to an existing script.
</p>
<dl><dd><dl><dd>To assign a script as an 'Overlay', place a ^ directly in front of the script name.</dd></dl></dd></dl>
<p>Example time:
</p>
<pre>---- assignments.yml ----

Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 0 Proximity Joe
    - 10 ^Regular Joe
    - 20 ^Joe the Builder  

---- script.yml ----
'Proximity Joe':
  Type: Interact
  Requirements:
    Mode: None
  Steps:
    1:
      Proximity Trigger:
        Script:
        - CHAT "Nice to see you, &lt;PLAYER&gt;!"

'Regular Joe':
  Type: Interact  
  Requirements:
    Mode: None
  Steps:
    1:
      Click Trigger:
        Script:
        - CHAT "Hello &lt;PLAYER&gt;! I supply builders only!"

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
        - CHAT "Hello &lt;PLAYER&gt; the Builder! Take this shovel!"
        - GIVE WOOD_SPADE QTY:1
        - FINISH
        - DISENGAGE
</pre>
<p>Here the 2 scripts from the last example will now only be selected for Click interaction, while the new 0 priority script will be selected for any interaction. 
</p><p>Let's see what happens in a few different scenarios.
</p><p><b>First Scenario</b>
Let's say a Player clicks, doesn't have the permissions 'modifyworld.*', so therefore only two scripts meet requirements: 'Regular Joe' and 'Proximity Joe'. It should be pretty obvious what happens. 'Regular Joe' has higher priority, so a Click Trigger will use that script. The Player will see "Hello Player! I supply builders only!". That's the only trigger, right? Wrong. This leads us into the next scenario.
</p><p><b>Second Scenario</b>
The first thing to trigger the Denizen NPC would actually be the Proximity Trigger. In a regular assignment situation, with the same permissions situation as the first scenario, 'Regular Joe' would beat out 'Proximity Joe' and since there is no Proximity Trigger in 'Regular Joe', no script would trigger. But this is an Overlay Assignment. Since there is no Proximity Trigger in the script 'Regular Joe', the next script available, 'Proximity Joe', would attempt to trigger instead. And what do we have here? A Proximity Trigger! The Player would see "Nice to see you, Player!".
</p><p><b>Third Scenario</b>
Player triggers a Proximity Trigger. Player has permission 'modifyworld.*', so the highest matching script is 'Joe the Builder' since it has a priority of 30. But there is no Proximity Trigger for this script, so the next script in line is checked. 'Regular Joe', of course, has no Proximity Trigger either! And since both 'Joe the Builder' and 'Regular Joe' are Overlay Assignments, we're back to 'Proximity Joe' triggering, alerting the player "Nice to see you, Player!".
</p><p>Do you see now the possibilities of the Denizen Script Engine? I love it!
</p><p>Simple stuff, right? To get your teeth wet, take a look at this additional example situation which uses FLAGS and magic :)
<a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Example_Scripts/Advanced_Scripts&amp;action=edit&amp;redlink=1" title="Denizen/Example Scripts/Advanced Scripts (page does not exist)">Advanced Scripts</a>
</p><p><br/>
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Default_Texts">Default Texts</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>In addition to handling the script assignments, there are also a few other things that can be declared in the Denizens node of assignments.yml. Under the text node you can define single chat lines that will be displayed for each of 3 core trigger types if there is not matching script found. Click, Damage and Chat. Additionally a message can be defined for when the Denizen is Engaged or its interaction cooldown isn't finished.
</p><p>Settings here override the default setting found in <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/config.yml&amp;action=edit&amp;redlink=1" title="Denizen/config.yml (page does not exist)">Denizen/config.yml</a> for this Denizen.
</p>
<pre>---- assignments.yml ----
Denizens: 
  Castle Guard: 
    Interact Scripts: 
      - 10 Guard Script
      - 20 Elite Guard
      - 30 Quest for Guard
    Texts: 
      No Click Trigger: Don't poke, me, &lt;PLAYER&gt;!
      No Damage Trigger: Ouch! you lookin' to get smacked?
      No Chat Trigger: Eh, what's that?
      Denizen Unavailable: I'm busy right now.
</pre>
</div></s>

<s><div class="mw-heading mw-heading2"><h2 id="Activity_Assignment">Activity Assignment</h2></div></s>

~~Activity scripts are assigned to Denizens much in the same way as Interact scripts.
The difference here is for each script you must specify a Time to load the script.~~

<s><pre>---- assignments.yml ----
Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
    Scheduled Activities:
    - 12:00 Wander_aimlessly
</pre></s>

<s><div class="mw-heading mw-heading3"><h3 id="Default_Activity">Default Activity</h3></div></s>

~~If you plan on only having one activity for your Denizen, you can use 'Default Activity:' instead of using the scheduler. When using this, the activity is set on 'Spawn'. You can also use the scheduler, which will override the default activity.~~

<s><pre>---- assignments.yml ----
Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
    Scheduled Activities:
    - 12:00 Go_home
    Default Activity: Wander_Around
</pre></s>
