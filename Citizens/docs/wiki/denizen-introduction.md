---
title: Denizen / 介绍
source_url: https://wiki.citizensnpcs.co/Denizen/Introduction
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5221
---


<a id="top"></a>

# Denizen / 介绍

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<a id="OUTDATED_HISTORICAL_INTRO"></a><h2 id="outdated-historical-intro">过时的历史介绍</h2>
<p>~~Denizen 由 Citizens2 和 Bukkit 提供支持，是一个丰富的附加包，可实现可编写脚本的 Minecraft 体验，包括增强的 NPCs、自定义命令、物品、世界事件和许多其他功能。受 MUD 的启发，由 Denizen 提供支持的功能和 NPCs 具有任何其他仅 Bukkit 解决方案无法比拟的独特 RPG 感觉。想象一下交互式看门人、魔法咒语、魔法巫师、经验训练师、经验和玩家统计系统、有银行家时间的银行家、会说话的城镇居民、魔法任务等等！ Denizen有数千种不同的使用方式，从教程、到游戏、到管理——你的想象力是无限的！~~</p>
<p>~~通过共享您的脚本，您可以启用最令人兴奋的功能。由于支持 Denizen 的语言 dScript 易于阅读，因此用户可以轻松共享和调整脚本以满足自己的需求。很多已经可以在<a href="http://scripts.citizensnpcs.co">Citizens 脚本存储库</a>网上找到了~~</p>
<p>~~虽然我们目前仍处于预发布测试阶段，但基于 YAML 的 dScript 正在成为功能齐全的核心功能集，可以通过数百种方式控制您的服务器。如果这还不够，还有很多方法可以扩展功能，因为 Denizen 在编程时考虑了功能齐全的 Java API。通过一些简单的 Java，您可以轻松制作自己的 dScript 命令、要求、脚本容器、标签、触发器等等。许多插件开发人员已经在使用自定义 Denizen 内容扩展他们的插件，以便于与脚本一起使用，当一点“o”点击时，我们希望您的插件也会注意到！~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Getting_Started">入门</h1></div></s></p>
<p>~~使用 Denizen 时很难找到一个好的“起点”，因为有很多不同的范围，但我们首先看一下使用 CraftBukkit 命令提供的 Denizen 的基本功能和控制。由于Denizen使用C2命令系统，您可能已经熟悉该系统了~~</p>
<p><s><div class="mw-heading mw-heading2"><h2 id="How_to_use_server_commands">如何使用服务器命令</h2></div></s></p>
<p>~~所有命令都有一个“base_command”、一个“command_name”以及字符串值、整数值、值标志（--flag value）或非值标志（-t）。某些命令可能一次使用多个标志。考虑下面的例子。~~</p>
<p><s><pre>/base_command command_name string value --flag value -t
/npc trigger damage --cooldown 5 -t</pre></s></p>
<p><s><pre>Note: Value flags which contain more than one word must be enclosed in quotes. 

/base_command command_name --flag “multi word value” --another_flag another_value  -t -f
/npc constant --name ‘Default Greeting Text’ --value ‘Hello, player!’</pre></s></p>
<p>/base_command command_name --flag “多字值” --another_flag another_value -t -f
/npc 常量 --name ‘默认问候语文本’ --value ‘你好，玩家！’</p>
<p><s><pre>Commands that provide multiple pages of feedback can include an integer number to specify page with some commands. If no number is specified, page 1 is assumed.

/base_command command_name 3
/denizen scripts 3</pre></s></p>
<p>/base_command 命令名 3
/denizen 脚本 3</p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Denizen_console_commands">Denizen 控制台命令</h2></div></s></p>
<p>~~Denizen命令提供了查看和配置Denizen关键组件的方法，例如版本检查和脚本列表。~~</p>
<p><s><pre>/denizen version

Displays the version and build information about the copy of denizen currently loaded. Will also show currently loaded ‘extensibles’.
Usage: 
/denizen version</pre></s></p>
<p>显示有关当前加载的 denizen 副本的版本和构建信息。还将显示当前加载的“可扩展项”。
用途： 
/居民版本</p>
<p><s><pre>/denizen save

Saves the contents of the ‘dScript saves’ in memory to disk as saves.yml. Useful for editing the contents while the server is running, using /denizen reload. 
When using Denizen on a production server, there are key events that auto-save the saves.yml, so it’s encouraged that saves.yml be edited only while the server is off.  When using on a development server, server action should be brought to a minimum while editing saves.yml.
Usage:
/denizen save</pre></s></p>
<p>将内存中“dScript saves”的内容保存到磁盘，格式为 saves.yml。对于在服务器运行时使用 /denizen reload 编辑内容很有用。 
在生产服务器上使用 Denizen 时，有些关键事件会自动保存 saves.yml，因此建议仅在服务器关闭时编辑 saves.yml。  在开发服务器上使用时，编辑 saves.yml 时应尽量减少服务器操作。
用途：
/居民保存</p>
<p><s><pre>/denizen reload

Reloads key disk files into memory, overwriting the copy currently in memory. Must specify which file to reload, or -a for all. Valid values are: scripts, saves, config or the -a flag.

Note: When reloading the config, some values require a server-reboot to take effect.
Usage: 
/denizen reload scripts|saves|config|-a

Example Usages:
/denizen reload -a
/denizen reload scripts</pre></s></p>
<p>将关键磁盘文件重新加载到内存中，覆盖当前内存中的副本。必须指定要重新加载的文件，或者为所有文件指定 -a。有效值 are: 脚本、保存、配置或 -a 标志。</p>
<p>注意：重新加载配置时，某些值需要重新启动服务器才能生效。
用途： 
/denizen 重新加载脚本|保存|配置|-a</p>
<p>用法示例：
/denizen 重新加载 -a
/denizen 重新加载脚本</p>
<p><s><pre>/denizen debug

Enables or disables the dBugger which can be very useful when writing and troublshooting script flow and any problems that may occur. 
Using the -s flag will toggle stacktraces, allowing some nitty-gritty error messages to slip through for when something seriously goes on. If getting help, it’s likely that we’ll ask you to enable this and provide us with the feedback. Using the -c flag will toggle color.
Usage: 
/denizen debug (-c) (-s)

Example Usages:
/denizen debug
/denizen debug -c</pre></s></p>
<p>启用或禁用 dBugger，这在编写和排除脚本流程以及可能发生的任何问题时非常有用。 
使用 -s 标志将切换堆栈跟踪，从而允许在发生严重情况时漏掉一些具体的错误消息。如果需要帮助，我们可能会要求您启用此功能并向我们提供反馈。使用 -c 标志将切换颜色。
用途： 
/denizen 调试 (-c) (-s)</p>
<p>用法示例：
/denizen 调试
/denizen 调试 -c</p>
<p><s><pre>/denizen scripts

Shows a list of scripts currently loaded into Denizen. Used alone, it lists all scripts, identified by type and name. Use an integer to specify which page to view. 

Using the type flag will cut down the search results to a specific type.
Using the filter flag will limit results to a specific search string.
Usage: 
/denizen scripts (--filter key_word) (--type script_container_type) (#)

Example Usages:
/denizen scripts --filter ‘bob quest’ 2
/denizen scripts --type task</pre></s></p>
<p>显示当前加载到 Denizen 中的脚本列表。单独使用时，它会列出所有脚本，并按类型和名称进行标识。使用整数指定要查看的页面。 </p>
<p>使用类型标志会将搜索结果缩减为特定类型。
使用过滤器标志会将结果限制为特定的搜索字符串。
用途： 
/denizen 脚本 (--filter key_word) (--type script_container_type) (#)</p>
<p>用法示例：
/denizen 脚本 --filter 'bob quest' 2
/denizen 脚本 --类型任务</p>
<p><s><pre>/denizen listener

Shows a list of active listeners for a player. Use the player flag to specify a different player. Use an integer to specify a page.

Using the finish flag will force-finish the listener, running the script the was specified in the original listen script command.
Using the cancel flag will cancel the listener, effectively removing it.
Using the report flag will output the status of the listener.
Usage: 
/denizen listener (--player player_name) (--finish|report|cancel listener_id)

Example Usages:
/denizen listener --report apple_quest_1
/denizen listener --player aufdemrand 2</pre></s></p>
<p>显示玩家的活跃侦听器列表。使用玩家标志来指定不同的玩家。使用整数指定页。</p>
<p>使用完成标志将强制结束侦听器，运行原始侦听脚本命令中指定的脚本。
使用取消标志将取消侦听器，从而有效地将其删除。
使用报告标志将输出侦听器的状态。
用途： 
/denizen 监听器 (--playerplayer_name) (--完成|报告|取消listener_id)</p>
<p>用法示例：
/denizen 监听器 --report apple_quest_1
/denizen 监听器 --player aufdemrand 2</p>
<p><s><div class="mw-heading mw-heading2"><h2 id="NPC_console_commands">NPC 控制台命令</h2></div></s></p>
<p>~~为了向 Citizens 无缝提供附加功能，Denizen 扩展了 /npc bukkit 命令以提供添加了附加特征的接口。此处列出的一些命令是核心 Citizens 命令，此处提供是因为它们通常与 Denizen 功能一起使用。 （DENIZEN！表示仅适用于 Denizen 的新 NPC 命令。）~~</p>
<p><s><pre>/npc create

The command to create a new NPC. Must provide a string name. Can also specify a type flag which will change the EntityType of the NPC.
 
Examples:
/npc create Jack
/npc create Henry the Great --type enderman
/npc create Susan --type cow</pre></s></p>
<p>该命令创建一个新的NPC。必须提供字符串名称。还可以指定类型标志，该标志将更改 NPC 的 EntityType。</p>
<p>示例：
/npc 创建杰克
/npc 创建亨利大帝 --type 末影人
/npc create Susan --型牛</p>
<p><s><pre>/npc select

Selects a NPC to work with. Used alone, it will select the nearest NPC in range. A npcid may also be specified to select a specific NPC.
 
Examples:
/npc select
/npc select 10</pre></s></p>
<p>选择要使用的 NPC。单独使用时，它将选择范围内最接近的 NPC。还可以指定 npcid 以选择特定的 NPC。</p>
<p>示例：
/npc 选择
/npc 选择 10</p>
<p><s><pre>/npc vulnerable

Allows a NPC to be damaged, and killed. Also required (in most cases) when using the ‘health trait’ that is provided with Denizen. Use the -t flag to indicate the vulnerability to be temporary. When temporary, vulnerability will not persist through a restart.
 
Examples:
/npc vulnerable
/npc vulnerable -t</pre></s></p>
<p>允许 NPC 被损坏并杀死。使用 Denizen 提供的“健康特征”时也需要（在大多数情况下）。使用 -t 标志指示该漏洞是暂时的。如果是暂时的，漏洞不会在重新启动后持续存在。</p>
<p>示例：
/npc 易受攻击
/npc 易受攻击 -t</p>
<p><s><pre>DENIZEN! /npc assignment

Used to specify and view the current assignment of an NPC. Also adds the trigger and constants trait to the NPC. To set an assignment, use the set flag with the name of the script as a value. Remember: Only assignment-type scripts can be assigned. To view information on the current assignment, use /npc assignment. Using the -r flag will remove the current assignment.
 
Examples:
/npc assignment
/npc assignment --set ‘town sheriff’</pre></s></p>
<p>用于指定和查看 NPC 的当前分配。还向 NPC 添加了触发器和常量特征。要设置分配，请使用 set 标志并将脚本名称作为值。请记住：只能分配分配类型的脚本。要查看有关当前分配的信息，请使用 /npc 分配。使用 -r 标志将删除当前分配。</p>
<p>示例：
/npc 任务
/npc 分配 --set ‘镇警长’</p>
<p><s><pre>DENIZEN! /npc trigger

Controls the various settings of interact-script triggers. To specify a trigger, use a string of the name. Use in combination of the -t  flag to toggle the trigger on or off. Using the cooldown flag allows the default cooldown for a trigger to be overridden on a NPC level. Changing the cooldown in this manner only affects the selected NPC. Triggers with range settings can also be modified using the radius flag. Using /npc trigger alone displays an overview of all available triggers for the selected NPC.

Examples:
/npc trigger
/npc trigger chat -t
/npc trigger proximity --radius 15
/npc trigger damage --cooldown 0.5</pre></s></p>
<p>控制交互脚本触发器的各种设置。要指定触发器，请使用名称字符串。与 -t 标志结合使用来打开或关闭触发器。使用冷却标志允许在 NPC 级别覆盖触发器的默认冷却时间。以这种方式更改冷却时间只会影响选定的 NPC。具有范围设置的触发器也可以使用半径标志进行修改。单独使用 /npc 触发器可显示所选 NPC 的所有可用触发器的概述。</p>
<p>示例：
/NPC触发器
/npc 触发聊天 -t
/npc触发接近--半径15
/npc 触发伤害 --cooldown 0.5</p>
<p><s><pre>DENIZEN! /npc constant

Constants are saved strings, or ‘pre-set variables’ that can be set in either an assignment script, or specified at the NPC-level. Constants set to a NPC will override any values also found set in an assignment. With the use of the /npc constant server command, dScripts can be ‘configurable’ in-game.
To set a constant, use the set flag with a value of the constant name, along with a value flag along with the new value of the constant. Constants can also be removed using the remove flag. Using /npc constant will show any constants currently known to the specified NPC.

Examples:
/npc constant --remove allowed_items
/npc constant --set ‘welcome message’ --value ‘Welcome to my village!’

Note: Constants are available for use within dScripts with use of a constant replaceable tag.  </pre></s></p>
<p>常量是保存的字符串或“预设变量”，可以在赋值脚本中设置，或在 NPC 级别指定。设置为 NPC 的常量将覆盖在赋值中设置的任何值。通过使用 /npc 常量服务器命令，dScript 可以在游戏中“配置”。
要设置常量，请使用带有常量名称值的设置标志，以及值标志和常量的新值。也可以使用删除标志删除常量。使用/npc常量将显示指定NPC当前已知的任何常量。</p>
<p>示例：
/npc 常量 --remove allowed_items
/npc Constant --set ‘欢迎消息’ --value ‘欢迎来到我的村庄！’</p>
<p>注意：常量可通过常量可替换标签在 dScript 中使用。  </p>
<p><s><pre>DENIZEN! /npc health

Modifies the current and maximum health of a NPC. While being vulnerable is not required, NPCs cannot lose any health without being vulnerable. By default, NPCs are invulnerable, unable to be damaged. Using the set flag will specify a new max-health. Using the -r flag will reset the NPCs current health to max. Using /npc health with no additional arguments will provide current status.
 
Examples:
/npc health
/npc health --set 100
/npc health -r</pre></s></p>
<p>修改 NPC 的当前和最大运行状况。虽然脆弱性不是必需的，但 NPCs 不会在不脆弱的情况下失去任何生命值。默认情况下，NPCs是无敌的，无法被损坏。使用设置标志将指定新的最大健康状况。使用 -r 标志会将 NPCs 当前运行状况重置为最大值。使用 /npc health 且不带任何其他参数将提供当前状态。</p>
<p>示例：
/NPC 生命值
/npc 生命值 --set 100
/npc 生命值 -r</p>
<p><s><pre>/npc playerlist

In order for vulnerable NPCs to be attacked by Minecraft Monsters, the NPC must be added back into the Bukkit Playerlist. This treats a NPC like a Player, and should be noted that it could conflict with some external plugins. When using this feature, there may also be slightly increased overhead, so it should only be used when necessary.
 
Examples:
/npc playerlist

Note: /npc playerlist only works on Player-Type NPCs.</pre></s></p>
<p>为了使易受攻击的 NPCs 受到 Minecraft 怪物的攻击，必须将 NPC 添加回 Bukkit 玩家列表中。这将 NPC 视为玩家，并且应该注意它可能与某些外部插件发生冲突。使用此功能时，也可能会稍微增加开销，因此应该仅在必要时使用。</p>
<p>示例：
/npc 玩家列表</p>
<p>注意：/npc玩家列表仅适用于玩家类型NPCs。</p>
<p><s><pre>DENIZEN! /npc nickname

Nicknames are NPC names on steroids. They are similar to Player display names, but also allow for a level of dynamic content to be used, since they allow the use of replaceable tags. Use the set flag to change a NPCs nickname. When used without any flags, the current nickname is shown. To remove a nickname, use the -r flag.

Examples:
/npc nickname
/npc nickname -r
/npc nickname --set ‘&lt;magic&gt;&lt;npc.name&gt;&lt;gold&gt;, 
     the friendly Wizard’
/npc nickname --set ‘&lt;npc.name&gt;, of Clan
     &lt;flag.n:clan_name&gt;’

Note: Nicknames, at this time, do not affect the ‘nameplate’ above player-type NPCs. This feature request may become possible in the future. To reference a NPCs nickname use the &lt;npc.name.nickname&gt; tag.</pre></s></p>
<p>昵称是 NPC 类固醇名称。它们与玩家显示名称类似，但也允许使用一定程度的动态内容，因为它们允许使用可替换的标签。使用 set 标志更改 NPCs 昵称。当不带任何标志使用时，将显示当前昵称。要删除昵称，请使用 -r 标志。</p>
<p>示例：
/npc昵称
/npc 昵称 -r
/npc 昵称 --set ‘&lt;magic&gt;&lt;npc.name&gt;&lt;gold&gt;, 
     友好的巫师’
/npc 昵称 --set ‘&lt;npc.name&gt;, 氏族
     &lt;flag.n:clan_name&gt;’</p>
<p>注意：此时昵称不会影响玩家类型NPCs上方的“铭牌”。此功能请求将来可能成为可能。要引用 NPCs 昵称，请使用 &lt;npc.name.nickname&gt; 标签。</p>
<p><s><pre>DENIZEN! /npc pushable

Moves NPCs out of the way when colliding with a Player. Default Citizens behavior is to allow clipping on NPC objects, allowing Players and NPCs to occupy the same space. Can also specify that the NPC be returnable using the -r flag. After being pushed, a returnable NPC will return to its previous location after a delay, which can be specified with the delay flag. Once the pushable trait is enabled, the actual push behavior can be toggled with the -t flag.
 
Examples:
/npc pushable
/npc pushable -r --delay 6
/npc pushable -t</pre></s></p>
<p>与玩家碰撞时将 NPCs 移开。默认的 Citizens 行为是允许剪切 NPC 对象，从而允许玩家和 NPCs 占据相同的空间。还可以使用 -r 标志指定 NPC 可返回。可返回的NPC被推送后，会在一段延迟后返回到之前的位置，这可以通过延迟标志来指定。一旦启用了可推送特征，就可以使用 -t 标志切换实际的推送行为。</p>
<p>示例：
/npc 可推动
/npc 可推 -r --delay 6
/npc 可推 -t</p>
<p><s><pre>DENIZEN! /npc FISH/STOPFISHING

Makes the NPC cast a fishing line to a position specified with the location flag, using the location format x,y,z,world_name, or alternatively, an anchor by using the anchor flag with the name of the anchor as the value. If you wish to make the NPC cast to the location of your cursor, use the -c flag. Using the /npc stopfishing command, the NPC will reel in its line.

Examples:
/npc fish --location 128,64,64,world
/npc fish -c
/npc fish --anchor chair_location
/npc stopfishing</pre></s></p>
<p>使 NPC 使用位置格式 x,y,z,world_name 将钓鱼线投射到由位置标志指定的位置，或者使用以锚点名称作为值的锚点标志来投射到锚点。如果您希望将 NPC 转换到光标位置，请使用 -c 标志。使用 /npc stopfishing 命令，NPC 将收线。</p>
<p>示例：
/npc 鱼 --location 128,64,64,world
/npc 鱼 -c
/npc 鱼 --锚椅位置
/npc 停止捕鱼</p>
<p><s><pre>DENIZEN! /npc SIT/STAND

Puts the NPC in the sitting position. If a specific location is desired, it can be specified with the location flag, using the location format x,y,z,world_name, or alternatively, an anchor can be specified by using the anchor flag with the name of the anchor as the value. If you wish to make the NPC sit on the location of your cursor, use the -c flag. Using the /npc stand command, or initiating navigation on a NPC will make the NPC assume a standing postion.

Examples:
/npc sit --location 128,64,64,world
/npc sit
/npc sit --anchor chair_location
/npc sit -c
/npc stand</pre></s></p>
<p>将 NPC 置于坐姿。如果需要特定位置，则可以使用位置格式 x,y,z,world_name 通过位置标志来指定，或者也可以使用锚点标志并将锚点名称作为值来指定锚点。如果您希望使 NPC 位于光标位置，请使用 -c 标志。使用 /npc Stand 命令，或在 NPC 上启动导航将使 NPC 处于站立位置。</p>
<p>示例：
/npc sat --位置 128,64,64,世界
/npc 坐
/npc sat --锚椅位置
/npc 坐 -c
/npc 站</p>
<p><s><pre>DENIZEN! /npc SLEEP/WAKEUP

Makes the NPC sleep on a position specified with the location flag, using the location format x,y,z,world_name, or alternatively, an anchor by using the anchor flag with the name of the anchor as the value.  When using the /npc wakeup command, the NPC will stop sleeping.

Examples:
/npc sleep --location 128,64,64,world
/npc sleep --anchor chair_location
/npc wakeup</pre></s></p>
<p>使用位置格式 x,y,z,world_name 使 NPC 休眠在位置标志指定的位置上，或者使用以锚点名称作为值的锚点标志来休眠锚点。  当使用/npc唤醒命令时，NPC将停止休眠。</p>
<p>示例：
/npc sleep --位置 128,64,64,世界
/npc sleep --anchor chair_location
/NPC唤醒</p>
<p><s><pre>DENIZEN! /npc NAMEPLATE

Changes the color of a NPCs nameplate. 

Examples:
/npc nameplate red</pre></s></p>
<p>更改 NPCs 铭牌的颜色。 </p>
<p>示例：
/npc铭牌红色</p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Experimental_commands">实验命令</h2></div></s></p>
<p>~~这些是当前 Denizen 中被视为“实验性”的一些命令。预计这些命令的语法和用法会在最终发布之前发生更改。~~</p>
<p><s><pre>/dtime #

To be used with the World Script ‘On Time’ event. Minecraft time 0 = 6:00 in dTime. dTime is based on a 24 hour clock.

Examples:
/dtime 6
/dtime 23</pre></s></p>
<p>与世界脚本“准时”事件一起使用。 Minecraft 时间 0 = 6:00（以 dTime 为单位）。 dTime 基于 24 小时制。</p>
<p>示例：
/d时间 6
/d时间 23</p>
<p><s><pre>/notable add

Adds a ‘notable location’ which is used throughout Denizen asa ‘location bookmark’ of sorts. Used in the World Script event ‘on walk over...’. Use the name flag to name the location.

Examples:
/notable add ‘secret spot 1’
/notable add treasure</pre></s></p>
<p>添加一个“显着位置”，在 Denizen 中用作某种“位置书签”。用于世界脚本事件“on walk over...”。使用名称标志来命名该位置。</p>
<p>示例：
/值得注意的是添加“秘密地点 1”
/值得注意的添加宝藏</p>

