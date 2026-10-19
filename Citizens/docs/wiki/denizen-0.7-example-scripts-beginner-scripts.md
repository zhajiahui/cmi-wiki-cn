---
title: Denizen / 0.7 / 脚本示例 / 入门脚本
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Beginner_Scripts
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5382
---


<a id="top"></a>

# Denizen / 0.7 / 脚本示例 / 入门脚本

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><s></s></p>
<div style="float:right;margin-left:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
</div>
<div style="margin-right:2.0em; margin-top:35px; padding:10px; font-family:camingodos-web; font-size:110%;">
<p><span style="font-family:natalya-alternate-one; font-size:650%; margin-right:-7px; margin-left:-10px;">S</span>有时最好的学习方法是看一些例子。以下初学者脚本使用基本的 denizen 命令和要求，为您提供一些不错的基本功能居民们。
<br/><br/></p>
<div style="padding:20px; font-family:camingodos-web; font-size:110%; background-color:#EEDDEE; border-style:dotted; border-width:1px; width:55%; font-weight:500;">示例脚本与作业和脚本放在同一个框中。确保将文本放入插件文件夹中的正确文件中。
<ul><li>作业应始终附加到plugins\Denizen\assignments.yml</li>
<li>脚本可以放置在plugins\Denizen\scripts\ 目录中的任何.yml 文件中。请记住：每个文件可以有多个脚本！</li></ul>
</div>
<p><br/><br/>
现在...脚本！</p>
</div>
<div class="mw-heading mw-heading2"><h2 id="Denizen_Basics">Denizen 基础知识</h2></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
<p>尽管 Denizen 可能非常先进，但它也可以执行非常简单的任务。大多数基础知识都可以通过快速脚本来涵盖。查看这些示例。
</p>
<div class="mw-heading mw-heading4"><h4 id="The_Click_and_Damage_Triggers">点击和损坏触发器</h4></div>
<p>点击 Denizen NPC 可以激活点击触发器或损坏触发器，具体取决于按下了哪个按钮。这可能是最简单且与 NPC 交互的最直接方式。请务必打开伤害触发器！ （使用/denizen触发切换伤害）
</p><p><br/>
</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> 右键点击说话，左键点击好痛！</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="The_Chat_and_Proximity_Triggers">聊天和接近触发器</h4></div>
<p>剩下的两个快速脚本触发器是聊天触发器和邻近触发器。聊天将捕获 Denizen NPC 附近所说的任何文本并拦截它。玩家的文字指向NPC 和 NPC 可以响应。当玩家进入指定范围时会触发接近。 （注意：默认情况下未启用接近功能，因此请选择您想要具有接近功能的 NPC。触发器并输入 /denizen 触发切换接近功能）
</p><p><br/>
</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> 有史以来最糟糕的治疗师。</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading2"><h2 id="Simple,_random_conversations"><span id="Simple.2C_random_conversations"></span>简单、随意的对话</h2></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
<p>让您沉浸在自己的世界中的一个好方法就是与 Denizen NPC 进行基本交互并输出随机响应。有几种不同的方法可以完成此操作，如下面的示例所示。由于这个概念很简单，因此可以使用快速脚本和交互脚本来完成。
</p>
<div class="mw-heading mw-heading4"><h4 id="A_conversation_with_RANDOM">与随机的对话</h4></div>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> 与 RANDOM 命令的快速脚本对话。</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="A_conversation_with_ZAP_RANDOM">与 ZAP RANDOM 的对话</h4></div>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> 与 ZAP 命令交互脚本对话。</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="Notch's_Cookies"><span id="Notch.27s_Cookies"></span>Notch 的饼干</h4></div>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> Notch 喜欢饼干和随机聊天。</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading2"><h2 id="Multiple_Scripts_&amp;_Requirements"><span id="Multiple_Scripts_.26_Requirements"></span>多个脚本和要求</h2></div>
<p></p>
<p><s></s></p>
<p>Random chat is nice, but controlling the flow of conversation and events is just as important. One of the best features of Denizen's Interact Scripts is the requirements system, which can be used to control multiple scripts. Imagine NPCs greeting players based on weather, or having conversations only when on a quest. For further understanding, you should check out [Denizen/Script Assignments#Multiple Scripts], but take these examples below to get a basic understanding.
</p>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="A_Simple_Multiple_Requirement_Script">一个简单的多需求脚本</h4></div>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> 两个脚本比一个更好。</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="Script_sequencing_with_the_SCRIPT_requirement">具有 SCRIPT 要求的脚本排序</h4></div>
<p>Another good way to control the flow of multiple scripts is by using the SCRIPT requirement, which can check if the player has completed or failed scripts.由于“任务，第 2 部分”需要完成“任务，第 1 部分”，因此玩家将被迫按照要求中的参数规定的顺序完成脚本。
</p>
<p><br/>
</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> 你必须按顺序做！</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="Script_sequencing_with_FLAGS">使用 FLAGS 进行脚本排序</h4></div>
<p>该脚本更像是一个中间脚本，但显示了如何使用标志来控制脚本的顺序。在此示例中，多个 NPCs 是此业力示例的一部分。注意：斯科蒂的脚本/杰森的脚本/等等。未显示，并且对于此示例不一定重要，但假设玩家以某种方式从这些角色收集业力，<b>一次一个</b>。</p>
<p><br/>
</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> “Karma”奖励系统示例。</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:250px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
<p><br/>
</p>
<p><br/>
</p>
<p><br/>
</p>
<table class="wikitable collapsible collapsed">
<tbody><tr>
<th>Joe Builder 脚本和作业
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
<div class="mw-heading mw-heading2"><h2 id="Basic_Repeatable_Fetch_Quest">基本可重复获取任务</h2></div>
<p>这是执行可重复“获取”任务的最快方法。适用于定制制作类型 NPCs。一旦玩家同意提供帮助，他就可以多次上交物品以获得奖励。
</p>
<table class="wikitable collapsible collapsed">
<tbody><tr>
<th>基本可重复获取任务
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
<div class="mw-heading mw-heading2"><h2 id="Basic_Unrepeatable_Fetch_Quest">基本的不可重复的获取任务</h2></div>
<p>通过在上面的脚本中添加 3 行，它就变得不可重复。
</p>
<table class="wikitable collapsible collapsed">
<tbody><tr>
<th>基本可重复获取任务
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
<div class="mw-heading mw-heading2"><h2 id="The_Race">比赛</h2></div>
<p>教练要你跑，孩子！该脚本使用任务脚本和位置触发器为玩家进行计时竞赛。 ZAP 和 RUNTASK/CANCELTASK 命令用法的好示例。确保使用 <code> /denizen bookmark location </code> 命令定义一个名为 'theTree' 的位置书签。  请务必打开此 NPC 的位置触发器！ （使用 /denizen 触发切换位置）</p>
<table class="wikitable collapsible collapsed">
<tbody><tr>
<th>Joe Builder 脚本和作业
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
</td></tr></tbody></table>
<p></p>

