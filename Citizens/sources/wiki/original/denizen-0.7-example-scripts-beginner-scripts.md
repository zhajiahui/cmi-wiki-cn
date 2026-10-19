For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

<s>
<div style="float:right;margin-left:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
</div>
<div style="margin-right:2.0em; margin-top:35px; padding:10px; font-family:camingodos-web; font-size:110%;">
<p><span style="font-family:natalya-alternate-one; font-size:650%; margin-right:-7px; margin-left:-10px;">S</span>ometimes the best way to learn is by looking at some examples. The following beginner scripts use basic denizen commands and requirements to provide some nice basic functionality for your Denizens.
<br/><br/>
</p>
<div style="padding:20px; font-family:camingodos-web; font-size:110%; background-color:#EEDDEE; border-style:dotted; border-width:1px; width:55%; font-weight:500;">Example scripts are provided with both the assignments and the scripts in the same box. Be sure and put the text in the correct file in your plugins folder.
<ul><li>Assignments should always be appended to plugins\Denizen\assignments.yml</li>
<li>Scripts can be placed in any .yml file in the plugins\Denizen\scripts\ directory. Remember: You can have multiple scripts per file!</li></ul>
</div>
<p><br/><br/>
and now... the scripts!
</p>
</div>
<div class="mw-heading mw-heading2"><h2 id="Denizen_Basics">Denizen Basics</h2></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
<p>Though Denizen can be very advanced, it can perform very simple tasks, as well. Most of the basics can be covered with a QUICK SCRIPT. Check out these examples.
</p>
<div class="mw-heading mw-heading4"><h4 id="The_Click_and_Damage_Triggers">The Click and Damage Triggers</h4></div>
<p>Clicking on a Denizen NPC can activates the Click Trigger or Damage Trigger, depending on which buttom was pressed. This is probably the easiest and most straight-forward way to interact with a NPC. Be sure to turn on the Damage Trigger! (Use /denizen trigger toggle damage)
</p><p><br/>
</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> Right click to speak, left click hurts!</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="The_Chat_and_Proximity_Triggers">The Chat and Proximity Triggers</h4></div>
<p>The two remaining Quick Script triggers are the Chat and Proximity Triggers. Chat will catch any text said near the Denizen NPC and intercept it. The Player's text is directed towards the NPC and the NPC can respond back. Proximity is triggered when the Player comes into a specified range. (Note: Proximity is not enabled by default, so select the NPC you desire to have the Prox. Trigger and type /denizen trigger toggle proximity)
</p><p><br/>
</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> The worst therapist ever.</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading2"><h2 id="Simple,_random_conversations"><span id="Simple.2C_random_conversations"></span>Simple, random conversations</h2></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
<p>A great way to provide some nice immersion into your world is as simple as a basic interaction with a Denizen NPC outputting a random response. There are a couple different ways this can be done, as provided in the examples below. Since this concept is simple, it can be done with a Quick Script as well as an Interact Script.
</p>
<div class="mw-heading mw-heading4"><h4 id="A_conversation_with_RANDOM">A conversation with RANDOM</h4></div>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> Quick Script conversation with the RANDOM command.</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="A_conversation_with_ZAP_RANDOM">A conversation with ZAP RANDOM</h4></div>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> Interact Script conversation with the ZAP command.</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="Notch's_Cookies"><span id="Notch.27s_Cookies"></span>Notch's Cookies</h4></div>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> Notch loves cookies, and RANDOM chat.</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading2"><h2 id="Multiple_Scripts_&amp;_Requirements"><span id="Multiple_Scripts_.26_Requirements"></span>Multiple Scripts &amp; Requirements</h2></div>
</s>

<s>
<p>Random chat is nice, but controlling the flow of conversation and events is just as important. One of the best features of Denizen's Interact Scripts is the requirements system, which can be used to control multiple scripts. Imagine NPCs greeting players based on weather, or having conversations only when on a quest. For further understanding, you should check out [Denizen/Script Assignments#Multiple Scripts], but take these examples below to get a basic understanding.
</p><p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="A_Simple_Multiple_Requirement_Script">A Simple Multiple Requirement Script</h4></div>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> Two scripts are better than one.</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="Script_sequencing_with_the_SCRIPT_requirement">Script sequencing with the SCRIPT requirement</h4></div>
<p>Another good way to control the flow of multiple scripts is by using the SCRIPT requirement, which can check if the player has completed or failed scripts. Since 'Quest, part 2' requires the completion of 'Quest, part 1', the player will be forced to complete the scripts in an order set forth by the arguments in the requirement.
</p><p><br/>
</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> You must do them in order!</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="Script_sequencing_with_FLAGS">Script sequencing with FLAGS</h4></div>
<p>This script is more of an intermediate script, but shows how flags can be used to control sequence of a script. In this example, multiple NPCs are part of this karma example. Note: Scottie's Script/Jason's Script/etc. are not shown, and aren't necessarily important to this example, but it is assumed that the player collects karma from these characters, somehow, <b>one at a time</b>.
</p><p><br/>
</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> A sample 'Karma' reward system.</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p><p><br/>
</p><p><br/>
</p>
<table class="wikitable collapsible collapsed">
<tbody><tr>
<th>Joe the Builder Script and Assignment
</th></tr>
<tr>
<td><pre>---- assignments.yml ----
Denizens:                         
  'Steve':    #This is the name of the Denizen               
    Interact Scripts: #These are the assigned interact scripts. The number before the script is the priority.                      
      - 0 Regular Joe
      - 10 ^Joe the Builder  


---- script.yml ----
'Regular Joe':
  Type: Interact   
  Requirements:  #There is no list of requirements, so this script can always be picked. That's why we assign it with low priority.
    Mode: None
  Steps:
    1:
      Click Trigger:
        Script:  #This sends a basic message to the interacting player.
        - CHAT "Hello &lt;PLAYER&gt;! I supply builders only!"   
      Proximity Trigger:
        Script:  #This sends a basic message to the player when he walks near.
        - CHAT "Hello &lt;PLAYER&gt;! Welcome to &lt;WORLD&gt;!"  
        
'Joe the Builder':
  Type: Interact   
  Requirements:
    Mode: All
    List: #Here we check if the player has this permission. If he does, this script is selected because it is higher priority.
    - PERMISSION modifyworld.*   
  Steps:
    1:
      Click Trigger:
        Script:
        - ENGAGE   
        #Engage prevents all interaction with this NPC until DISENGAGE is called.
        - CHAT "Hello &lt;PLAYER&gt; the Builder! Take this shovel!"
        - GIVE WOOD_SPADE
        - WAIT 1       
        - CHAT "If you have any questions, just say 'help'"
        - FINISH 
        #This increments the number of times this script (Joe The Builder) has been completed by this player.
        - DISENGAGE  
        #This sets the NPC Interactable again.
      Chat Trigger: #There can be multiple entries under a Chat Trigger or Location Trigger node. Hence the 1: on the next line.
        1:
          Trigger: I need some /help/
          Script:
           - CHAT "Press 'e' to open your inventory, and drag the shovel to your item bar"
           - CHAT "Press the number 1-9 to select the shovel, then start digging!"
</pre>
</td></tr></tbody></table>
<div class="mw-heading mw-heading2"><h2 id="Basic_Repeatable_Fetch_Quest">Basic Repeatable Fetch Quest</h2></div>
<p>Here is the fastest way to do a repeatable 'fetch' quest. Useful for custom crafting-type NPCs. Once the player agrees to help, he can turn in the items as often as he wants to receive the reward.
</p>
<table class="wikitable collapsible collapsed">
<tbody><tr>
<th>Basic Repeatable Fetch Quest
</th></tr>
<tr>
<td><pre>#--- assignments.yml ----
Denizens:
 John Q QuestGiver:
   Interact Scripts:
     - 0 StartFetch
     - 1 EndFetch

#--- RepeatableFetchQuest.yml ----
     
StartQuest:
  Type: Interact
  Requirements:
    Mode: None
  Steps:
     1:
      Click Trigger:
        Script:
        - CHAT "Hey, you there!"
        - CHAT "I have a special request of you!"
        - CHAT "Will you help me?"
      Chat Trigger:
         1:
          Trigger: /Yes/. I will.
          Script:
          #Tell the player what to do.
          - CHAT "I need you to bring me some thing. For testing!"
          - WAIT 1
          - CHAT "I need: 1 Iron Block, 1 Feather, and 3 Eggs."
          - WAIT 1
          - CHAT "Come back when you have them and I will reward you!"
          #Set this script as finished, so we know they're on the quest
          - FINISH
          #set this script to step 2. So the player gets the hint message.
          - ZAP
         2:
          Trigger: /No/. I will not.
          Script:
          - CHAT "Are you sure? OK. maybe later?"
    2:
      Click Trigger:
        Script:
        - CHAT "Come back you have 1 Iron Block, 1 Feather, and 3 Eggs!"


EndFetch:
  Type: Trigger   
  Requirements:
    Mode: All
    List: #Here we check if they are on the quest and have the items.
    - FINISHED StartQuest
    - ITEM 42 1
    - ITEM 288 1
    - ITEM 344 3
  Steps:
    '1':
      Click Trigger:
        Script:
        #Engage is used to keep the player from clicking twice.
        - ENGAGE
        - TAKE 42 QTY:1
        - TAKE 288 QTY:1
        - TAKE 344 QTY:3
        - CHAT "Thank you so much! Here, take this as a reward!"
        - GIVE 133 QTY:1
        - WAIT 1
        - CHAT "Bring me those items again, and I'll give you another!"       
        #Always disengagae after an Engage
        - DISENGAGE
</pre>
</td></tr></tbody></table>
<div class="mw-heading mw-heading2"><h2 id="Basic_Unrepeatable_Fetch_Quest">Basic Unrepeatable Fetch Quest</h2></div>
<p>By adding 3 lines to the script above, it becomes un-repeatable.
</p>
<table class="wikitable collapsible collapsed">
<tbody><tr>
<th>Basic Repeatable Fetch Quest
</th></tr>
<tr>
<td><pre>#--- assignments.yml ----
Denizens:
 John Q QuestGiver:
   Interact Scripts:
     - 0 StartFetch
     - 1 EndFetch

#--- UnRepeatableFetchQuest.yml ----
     
StartQuest:
  Type: Interact
  Requirements:
    Mode: None
  Steps:
     1:
      Click Trigger:
        Script:
        - CHAT "Hey, you there!"
        - CHAT "I have a special request of you!"
        - CHAT "Will you help me?"
      Chat Trigger:
         1:
          Trigger: /Yes/. I will.
          Script:
          - CHAT "I need you to bring me some thing. For testing!"
          - WAIT 1
          - CHAT "I need: 1 Iron Block, 1 Feather, and 3 Eggs."
          - WAIT 1
          - CHAT "Come back when you have them and I will reward you!"
          - FINISH
          - ZAP
         2:
          Trigger: /No/. I will not.
          Script:
          - CHAT "Are you sure? OK. maybe later?"
    2:
      Click Trigger:
        Script:
        - CHAT "Come back you have 1 Iron Block, 1 Feather, and 3 Eggs!"
    3:
      Click Trigger:
        Script:
        - CHAT "Thanks for the help before!"


EndFetch:
  Type: Interact   
  Requirements:
    Mode: All
    List: #Here we check if they are on the quest and have the items, and haven't completed this yet.
    - FINISHED StartQuest
    - -FINISHED EndFetch
    - ITEM 42 1
    - ITEM 288 1
    - ITEM 344 3
  Steps:
    '1':
      Click Trigger:
        Script:
        - ENGAGE
        - TAKE 42 QTY:1
        - TAKE 288 QTY:1
        - TAKE 344 QTY:3
        - CHAT "Thank you so much! Here, take this as a reward!"
        - GIVE 133 QTY:1
        - WAIT 1
        - CHAT "Tbanks so much! see you around!"  
        #This handy command will move the first script to Step 3.
        - ZAP 3 SCRIPT:StartFetch
        #Mark this script as completed.
        - FINISH
        - DISENGAGE
</pre>
</td></tr></tbody></table>
<div class="mw-heading mw-heading2"><h2 id="The_Race">The Race</h2></div>
<p>Coach wants you to RUN, BOY! This script uses a TASK script and a Location trigger to make a timed race for the player. Good example of ZAP and RUNTASK/CANCELTASK command usage. Be sure and define a Location Bookmark called 'theTree' using the <code> /denizen bookmark location </code> command.  Be sure to turn on the Location Trigger for this NPC! (Use /denizen trigger toggle location)
</p>
<table class="wikitable collapsible collapsed">
<tbody><tr>
<th>Joe the Builder Script and Assignment
</th></tr>
<tr>
<td>
<pre>---- assignments.yml----
Denizens:
  Coach:
    Interact Scripts:
      - 0 Coaches Race
    

---- Scripts.yml -----

'RaceEnd': 
  Type: Task    
  Script:       
  - NARRATE "%%cTimes Up!"
  - ZAP 'SCRIPT:Coaches Race' 3
  
"Coaches Race":
  Type: Interact   
  Requirements:
    Mode: All
    List:
     - -FINISHED Coaches Race
  Steps:
    1:
      Click Trigger:
        Script:
          - CHAT "Think you're fast, sonny-jim?"
          - CHAT "Lets see how fast you are. Run up that hill, around the tree, and back in 15 seconds, if you can!"
          - WAIT 1
          - CHAT "On your mark, get set, go!"
          - RUNTASK SCRIPT:RaceEnd DELAY:15
          - ZAP 2
    2:
      Location Trigger:
         1:
           Trigger: theTree
           Script: 
            - ZAP 4
      Click Trigger:
        Script:
          - CANCELTASK RaceEnd
          - CHAT "Trying to cheat eh?, you have to go around the tree!, try again later, slowpoke!"
          - ZAP 1
    3:
      Click Trigger:
        Script:
          - CHAT "Aww too slow!, go run some laps and try again!"
          - ZAP 1
    4:
      Click Trigger:
        Script:
          - CANCELTASK RaceEnd
          - CHAT "Woo, you are quick! Good job!"
          - GIVE MONEY QTY:1000
          - FINISH
</pre>
</td></tr></tbody></table></s>
