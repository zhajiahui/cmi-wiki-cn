For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>Task scripts are just a simple list of <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Commands" title="Denizen/0.7/Interact Scripts/Commands">Script Commands</a>. They can be called by the RUNTASK command, the IF command, or the TASK activity. They are useful for creating a set of commands that is used in multiple places.
</p>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="General_layout">General layout</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<pre>'Name of script':  
  Type: Task    
  Script:        
  - COMMAND1
  - COMMAND2
  - etc...
</pre>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Using_the_RUNTASK_command">Using the RUNTASK command</h4></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>Imagine a scenario where you'd like to check a single outcome from multiple sources. Say, for instance, you have multiple 'quests' that all have the same outcome. You could check the completion for each quest, or, you could have all the quests call a Task Script and check against that.
</p><p>This is a very basic example for something that can in theory be very complex. Imagination, hoooo!
</p>
<pre>'Apple Reward': 
  Type: Task    
  Script:       
  - NARRATE "You've received some APPLES. Nice!"
  - GIVE APPLE QTY:10
  - FINISH

'Apple Quest 1':
  Type: Interact
  Requirements:
    Mode: All
    List:
    - -FINISHED Apple Reward
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT "Welcome to my house, have some apples!"
        - RUNTASK 'SCRIPT:Apple Reward'
  
'Apple Quest 2':
  Type: Interact
  Requirements:
    Mode: All
    List:
    - -FINISHED Apple Reward
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT "Welcome to my orchard, have some apples!"
        - RUNTASK 'SCRIPT:Apple Reward'
</pre>
</div></s>

<s><div class="mw-heading mw-heading4"><h4 id="Using_the_TASK_Activity">Using the TASK Activity</h4></div></s>

~~This is a special case, as Activities occur without a player. Therefor any commands that require a Player will not function in a Task Script called from the activity.
Many script commands have a DENIZEN modifier to run the command on the NPC instead of the Player, and these should always be used when calling a Task Script from the TASK Activity.~~

<s><pre>WalkHome: 
  Type: Task    
  Script:       
  - CHAT NOPLAYER "Welp.. time to head home!"
  - WALKTO BOOKMARK:Home

GoHomeActivity:
  Type: Activity
  Requirements:
    Mode: None
  Activities:
    List:
    - 1 TASK SCRIPT:WalkHome REPEATS:0
  </pre></s>
