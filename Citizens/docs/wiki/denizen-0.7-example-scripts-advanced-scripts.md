---
title: Denizen / 0.7 / 脚本示例 / 高级脚本
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Example_Scripts/Advanced_Scripts
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5390
---


<a id="top"></a>

# Denizen / 0.7 / 脚本示例 / 高级脚本

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>这些脚本使用 Denizen 的所有强大功能来完成一些非常酷的事情。</p>
<a id="Maggie's_Magic_Shop"></a><h4 id="maggies-magic-shop">玛吉的魔法店</h4>
<p>玛吉出售魔法零碎物品。这组脚本模拟供应商。她会向玩家打招呼，提供她的商品，并检查是否有适当的金额。这是如何使用标志的一个很好的例子。</p>
<p><a href="https://wiki.citizensnpcs.co/File:Maggie_Choice_Debug.png"><img alt="" src="assets/4cc05749f803-Maggie_Choice_Debug.png"/></a></p>
<p>玛吉的剧本：你想买什么？</p>
<p><a href="https://wiki.citizensnpcs.co/File:Maggie_Buying_Feathers.png"><img alt="" src="assets/6625867c1488-Maggie_Buying_Feathers.png"/></a></p>
<p>玛吉的剧本：买羽毛游戏画面</p>
<p><a href="https://wiki.citizensnpcs.co/File:Maggie_Feather_Debug.png"><img alt="" src="assets/e10648a2853b-Maggie_Feather_Debug.png"/></a></p>
<p>玛吉的脚本：购买羽毛调试屏幕</p>
<div class="highlight"><pre># Maggie sells some magic items for money.
# Version 1.1

# ASSIGNMENTS
#
#  Maggie:
#    Interact Scripts:
#    - 0 Magic Shop
#    - 10 ^Magic Shop Not Enough Money
#    - 20 ^Magic Shop Feathers
#    - 20 ^Magic Shop Dust
    
# MAGGIES MAGIC SHOP.YML ----

'Magic Shop':
  Type: Interact
  Requirements:
    Mode: None
  Steps:
    1:
      Proximity Trigger:
        Script:
        - CHAT 'Welcome to my shop! Have a look around!'
      Click Trigger:
        Script:
        - CHAT 'What would you like to buy?'
        - HINT
      Chat Trigger:
        1:
          Trigger: I would like to buy some /feathers/
          Script:
          - CHAT 'Great! Feathers are 20 coins.'
          - ^NARRATE 'Right click to purchase some feathers.'
          - FLAG 'MAGICSHOPITEM:FEATHER' 'DURATION:15'
        2:
          Trigger: I would like to buy some /glowstone dust/
          Script:
          - CHAT 'Great! Glowstone dust is 50 coins.'
          - ^NARRATE 'Right click to purchase some glowstone dust.'
          - FLAG 'MAGICSHOPITEM:DUST' 'DURATION:15'
        3:
          Trigger: I would like to buy some /*/
          Script:
          - CHAT "Ah! Sorry, I don't sell any of that!"

          
'Magic Shop Not Enough Money':
  Type: Interact
  Requirements:
    Mode: All
    List:
    - FLAGGED 'MAGICSHOPITEM'
  Steps:
    1:
      Click Trigger:
        Script:
        - ^NARRATE "Erm... seems you don't have enough money."
        - RESET 'FLAG:MAGICSHOPITEM'

        
'Magic Shop Feathers':
  Type: Interact
  Requirements:
    Mode: All
    List:
    - FLAGGED 'MAGICSHOPITEM:FEATHER'
    - MONEY 20
  Steps:
    1:
      Click Trigger:
        Script:
        - ^TAKE MONEY QTY:20
        - ^GIVE FEATHER QTY:10
        - CHAT 'Thanks! Here are your feathers.'  
        - NARRATE 'You bought 10 Feathers for 20 coins! Sweet!'
        - NARRATE 'Right click again to buy some more.'

        
'Magic Shop Dust':
  Type: Interact
  Requirements:
    Mode: All
    List:
    - FLAGGED 'MAGICSHOPITEM:DUST'
    - MONEY 50
  Steps:
    1:
      Click Trigger:
        Script:
        - ^TAKE MONEY QTY:50
        - ^GIVE GLOWSTONE_DUST QTY:10
        - CHAT "Thanks! Here's your dust."
        - NARRATE 'You bought 10 Glowstone Dust for 50 coins! Sweet!'
        - NARRATE 'Right click again to buy some more.'
</pre></div>
<a id="To_Do"></a><h2 id="to-do">待办事项</h2>

