---
title: Denizen / 脚本示例
source_url: https://wiki.citizensnpcs.co/Denizen/Script_Samples
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5226
---


<a id="top"></a>

# Denizen / 脚本示例

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>也许样品会放在这里！</p>
<a id="Checkpoint_NPC"></a><h2 id="checkpoint-npc">检查点 NPC</h2>
<p>~~使用 dScript 突出显示查看脚本：<a href="http://mcmonkey.org/paste/91">http://mcmonkey.org/paste/91</a>~~</p>
<p><s><pre># Simply spawn an NPC and do
# /npc assign --set respawnmaster
# and now you have a checkpoint NPC :D

# NPC Assignment script
respawnmaster:
    # Obligatory type
    type: assignment
    # Actions = script run when NPC-related events occur
    actions:
        # This one is when the NPC is assigned
        on assignment:
        # Enable the trigger 'Proximity' with a radius of 10 blocks
        - trigger name:proximity state:true radius:10
    # interact script list
    interact scripts:
    # The interact below
    - 10 respawnmaster_interact

# The interact script
respawnmaster_interact:
    # Obligatory type
    type: interact
    # List the steps below
    steps:
        # First (Default) step
        1:
            # Triggers that fire when a player moves around near an NPC
            proximity trigger:
                # Specifically, when a player enters the radius of 10 blocks mentioned above
                entry:
                    # Run this script...
                    script:
                    # If the player's last set checkpoint was set by this NPC,
                    # cancel the current script queue (Clear it) (Meaning, the the flag/narrate won't happen)
                    - if &lt;player.flag[respawner]&gt; == &lt;npc.id&gt; queue clear
                    # Add a flag on the player, named respawnpoint, set to the player's current location at the time he entered the radius
                    - flag player respawnpoint:&lt;player.location&gt;
                    # Add a flag on the player, named respawner, set to the ID of the NPC that set this checkpoint.
                    - flag player respawner:&lt;npc.id&gt;
                    # Tell the player that he has reached the checkpoint, in green
                    - narrate "&lt;&amp;2&gt;You reached a checkpoint!"

# World script to handle respawning
respawnhandler:
    # Obligatory type
    type: world
    # List of world events (events not related to an NPC) that we want to run scripts for
    events:
        # The event that fires when a player dies and respawns
        on player respawns:
        # If the player doesn't have a respawn point, clear the scriptqueue, same as above, preventing the determine
        - if &lt;player.flag[respawnpoint]&gt; == null queue clear
        # Run the task script 'respawnnomercy' with a delay of one second
        - run respawnnomercy delay:2s
        # Tell the event that we want to change the outcome to the player's flagged respawn point...
        # in this event, that changes where the player respawns
        # Thus, the player respawns at the checkpoint set in the prox trigger above
        - determine &lt;player.flag[respawnpoint]&gt;

# A task script to prevent errors on Multiverse/whatever servers
respawnnomercy:
    # Obligatory type
    type: task
    # Script below is the only script in a task
    script:
    # Teleport the player to the respawn point, in case the determine above didn't do it
    - teleport &lt;player&gt; &lt;player.flag[respawnpoint]&gt;

# Remember, when whatever quest is completed, to run this command:
# - flag player respawnpoint:!
# To remove the respawnpoint and allow them to respawn normally
</pre></s></p>
<h1 id="npc-assign-set-respawnmaster">/npc assign --set respawnmaster</h1>
<h1 id="and-now-you-have-a-checkpoint-npc-d">现在你有一个检查点 NPC :D</h1>
<h1 id="npc-assignment-script">NPC 赋值脚本</h1>
<p>respawnmaster:
    # 强制类型
    type: 分配
    # Actions = 当 NPC 相关事件发生时运行脚本
    actions:
        # 这是NPC被赋值的时候
        上 assignment:
        # 启用半径为 10 个方块的“接近”触发器
        - 触发 name:proximity state:true radius:10
    # 交互脚本列表
    互动 scripts:
    # 下面的交互
    - 10 个重生大师互动</p>
<h1 id="the-interact-script">交互脚本</h1>
<p>respawnmaster_interact:
    # 强制类型
    type: 互动
    # 列出下面的步骤
    steps:
        # 第一步（默认）
        1：
            # 当玩家在 NPC 附近移动时触发
            接近 trigger:
                # 具体来说，当玩家进入上述10个方块的半径时
                entry:
                    # 运行这个脚本...
                    script:
                    # 如果玩家最后设置的检查点是由这个NPC设置的，
                    # 取消当前脚本队列（清除它）（意思是，标记/叙述不会发生）
                    - 如果 &lt;player.flag[respawner]&gt; == &lt;npc.id&gt; 队列清除
                    # 在玩家上添加一个标志，名为respawnpoint，设置为玩家进入半径时的当前位置
                    - 标记玩家 respawnpoint:&lt;player.location&gt;
                    # 在玩家上添加一个标志，名为respawner，设置为设置此检查点的NPC的ID。
                    - 标记玩家 respawner:&lt;npc.id&gt;
                    # 告诉玩家他已经到达检查站，绿色
                    - 叙述“&lt;&amp;2&gt;您已到达检查站！”</p>
<h1 id="world-script-to-handle-respawning">处理重生的世界脚本</h1>
<p>respawnhandler:
    # 强制类型
    type:世界
    # 我们想要运行脚本的世界事件列表（与 NPC 无关的事件）
    events:
        # 当玩家死亡并重生时触发的事件
        玩家 respawns: 上
        # 如果玩家没有重生点，则清除脚本队列，与上面相同，防止确定
        - 如果 &lt;player.flag[respawnpoint]&gt; == 空队列清除
        # 延迟一秒运行任务脚本“respawnnomercy”
        - 运行respawnnomercy delay:2s
        # 告诉事件我们想要将结果更改为玩家标记的重生点...
        # 在这个事件中，玩家重生的位置会改变
        # 因此，玩家会在上面 prox 触发器中设置的检查点重生
        - 确定&lt;player.flag[respawnpoint]&gt;</p>
<h1 id="a-task-script-to-prevent-errors-on-multiversewhatever-servers">用于防止 Multiverse/任何服务器上错误的任务脚本</h1>
<p>respawnnomercy:
    # 强制类型
    type: 任务
    # 下面的脚本是任务中唯一的脚本
    script:
    # 将玩家传送到重生点，以防上面的确定没有做到这一点
    - 传送 &lt;player&gt; &lt;player.flag[respawnpoint]&gt;</p>
<h1 id="remember-when-whatever-quest-is-completed-to-run-this-command">请记住，当完成任何任务后，运行此 command:</h1>
<h1 id="-flag-player-respawnpoint">- 标记玩家respawnpoint:！</h1>
<h1 id="to-remove-the-respawnpoint-and-allow-them-to-respawn-normally">删除重生点并允许它们正常重生</h1>
<p></p>

