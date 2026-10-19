For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

~~Activity Scripts contain a set of Activities.
Activities are continuous actions the Denizen can do that give it life. Wandering, collecting wheat, mining a block, these are all possible activities.~~

<s><div class="mw-heading mw-heading4"><h4 id="General_layout_of_an_Activity_Script">General layout of an Activity Script</h4></div></s>

<s>
<pre>'Name of script':   # Name Node
  Type: Activity    # Type Node
  Requirements:     # Requirements Node
    Mode: ...
    List: 
    - ...
    - ...
  Activities:       # Activities Node
    List:
     - ...
     - ...
</pre>
<div class="mw-heading mw-heading2"><h2 id="About">About</h2></div>
<p>An Activity script defines a set of Activities that a Denizen can do simultaneously.
</p><p>Each Activity is assigned a goal priority that dictates which activity will be active at any given time. If a certain Activity cannot be done, the next lower priority Activity will be used instead.
</p><p>An activity Script.
</p>
<pre>'Citizen':
  Type: Activity
  Requirements:
    Mode: None
  Activities:
    List:
    - 1 WANDER DELAY:12 RADIUS:10 SPEED:.75 FILTER:COBBLESTONE,GRAVEL,WOOL
</pre>
<div class="mw-heading mw-heading2"><h2 id="Assigning">Assigning</h2></div>
</s>

~~See [Denizen/0.7/Assignments#Activity_Assignment](https://wiki.citizensnpcs.co/Denizen/0.7/Assignments#Activity_Assignment "Denizen/0.7/Assignments")~~
