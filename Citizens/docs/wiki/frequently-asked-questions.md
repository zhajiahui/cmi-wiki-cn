---
title: 常见问题
source_url: https://wiki.citizensnpcs.co/Frequently_Asked_Questions
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5517
---


<a id="top"></a>

# 常见问题

<p>此页面包含有关 Citizens 项目的常见问题。在提交问题、在 Discord 上提问或在论坛帖子上发帖之前，您应该始终检查此处。您的疑问很可能已经在这里得到解答。</p>
<a id="First_of_All"></a><h1 id="first-of-all">首先</h1>
<p>如果此处没有您问题的答案，请在 #citizens 频道中的 <a href="https://discord.gg/Q6pZGSR">不和谐</a> 上提问（为您的问题创建一个话题）。</p>
<a id="Errors"></a><h1 id="errors">错误</h1>
<a id="Why_isn't_Citizens_working_on_my_server?"></a><h2 id="why-isnt-citizens-working-on-my-server">为什么 Citizens 无法在我的服务器上运行？</h2>
<p>Citizens 是一个高级插件，需要当前版本的 Spigot 才能工作。</p>
<p>如果您收到 NoClassDefFound、ClassNotFoundException 或 FieldNotFound 错误，请确保您拥有正确的 Spigot 子版本。 （这是最新版本，在 Minecraft 版本中，例如 1.15.2，而不是 1.15 或 1.15.1）。并且您有 Spigot/Minecraft 的相对较新的主版本（即过去几年内推出的版本）。</p>
<p>否则，请在 <a href="https://discord.gg/Q6pZGSR">这里不和谐</a> 上询问，或提交问题 <a href="http://issues.citizensnpcs.co">这里</a>。</p>
<a id="Why_can't_my_users_hear_my_NPCs?"></a><h2 id="why-cant-my-users-hear-my-npcs">为什么我的用户听不到我的 NPCs？</h2>
<p>确保您授予他们适当的权限。用户需要 <code>citizens.npc.talk</code> 才能通过点击或关闭通话听到 NPCs。参见 <a href="permissions.md" title="Permissions">权限</a>。</p>
<a id="I_can't_right-click_to_select_an_NPC"></a><h2 id="i-cant-right-click-to-select-an-npc">我无法右键点击选择 NPC</h2>
<p>默认情况下，您必须拿着一根棍子才能右键点击选择 NPC。该项目可以在 <a href="configuration.md" title="Configuration">配置</a> 中更改。使用 <code>'*'</code> 不需要任何物品。</p>
<a id="There's_a_&quot;0_health&quot;_line_below_my_NPC's_names"></a><h2 id="theres-a-0-health-line-below-my-npcs-names">我的 NPC 名字下面有一条“0 health”行</h2>
<p>这是一个“below_name”记分板。它不是由 Citizens 创建的。</p>
<p>它很可能是由另一个插件（例如 "TAB"）创建的。请联系该插件的支持人员，了解如何避免此问题的详细信息（如果插件是 "TAB"，则 "belowname"-&gt;"enabled" 下有一个配置选项，您可以将其设置为 "false" 以禁用该插件的此功能，请参阅 <a href="https://github.com/NEZNAMY/TAB/wiki/Feature-guide:-Belowname">这里有关于它的文档</a>）。</p>
<p>这些记分板有时也是由工作人员使用普通 <code>/scoreboard</code> 命令创建的。如果因此，只需使用该命令删除 Below_name 记分板即可。</p>
<a id="Why_are_NPCs_showing_up_in_the_tablist?"></a><h2 id="why-are-npcs-showing-up-in-the-tablist">为什么 NPCs 出现在选项卡中？</h2>
<p>更新：从 1.19.3 开始，这不再是问题（使用混合服务器/客户端版本的 ViaVersion 除外）。</p>
<p>当Minecraft 1.7添加了UUID和新的皮肤系统时，一些服务器使用它来动态定制玩家皮肤。 Mojang对此并不满意，因此在1.7.6中提出了非常严格的玩家实体验证要求。这些要求之一是任何生成的玩家实体在生成时都必须位于选项卡列表中。不幸的是，这意味着 Citizens NPCs 当它们出现在视图中时必须立即出现在选项卡列表中。为了避免不断浪费选项卡列表空间，我们让 NPCs 尽快（不到一秒）再次从选项卡列表中消失。</p>
<p>完全避免这种情况的第一个也是最简单的选择是，course: 没有玩家类型 NPCs。使用村民或盔甲架或任何其他生物类型。这些其他类型根本不会显示在选项卡列表中。</p>
<p>如果您希望避免玩家 NPCs 闪烁，唯一可行的方法是简单地完全填充选项卡列表，以使 NPCs 超出其边缘，从而不可见。一些选项卡列表插件会在真实玩家未使用空间的地方用空白槽和/或信息消息填充屏幕。理论上，任何类似的选项卡列表都应该自动避免闪烁效果。</p>
<p>如果您对运行此类插件不感兴趣，唯一的其他选择就是忽略闪烁。实际上，这对于玩家来说并不是特别明显 - 当然，除了非常短的短暂闪光之外，要看到闪光还需要您在按住 Tab 键的情况下积极地从 NPC 的渲染距离边缘移动，这不是大多数玩家经常做的事情。</p>
<p>注意：故意将 NPCs 持续添加到选项卡列表中是禁止的，因为 Mojang 认为该选项卡列表是“假玩家”的线路，太可信了。 Citizens 和团队不建议以任何方式绕过此系统来假装在您的选项卡列表中包含真实玩家，并且可能会导致 Mojang 对您的服务器采取行动。</p>
<a id="I_have_a_free_server_(Aternos,_Minehut,_...)_but_there's_problems"></a><h2 id="i-have-a-free-server-aternos-minehut-but-theres-problems">我有一个免费服务器（Aternos、Minehut...），但有问题</h2>
<p>免费服务器不会很好地工作。他们通常会严格限制服务器，导致出现错误且无法解决。</p>
<p>请获取合法的服务器（来自信誉良好的服务器公司（如“OVH”）的 VPS 或专用服务器），或者如果您负担不起，则只需使用主主机。</p>
<p>"Homehosting" 是指您在家用 PC（台式机或笔记本电脑）上运行 Spigot 服务器时。这不仅是可能的，实际上是<em>更好</em>比在大多数情况下免费主机，因为它为您提供了运行无问题的 Minecraft 服务器所需的自由和控制权，唯一真正的限制是您必须保持家用 PC 运行才能使 Minecraft 服务器保持正常运行。</p>
<a id="My_PlaceholderAPI_Placeholder_Works_In_Chat,_But_Not_On_An_NPC"></a><h2 id="my-placeholderapi-placeholder-works-in-chat-but-not-on-an-npc">我的 PlaceholderAPI 占位符可以在聊天中使用，但不能在 NPC 上使用</h2>
<p>许多 PAPI 占位符被设计为需要玩家链接 - 例如，显然，<code>%player_name%</code> 需要链接玩家才能知道要显示哪个名字。当您使用命令时，您会被链接，以便占位符会显示您自己的名字。当占位符位于 NPC 上时，它会在全局上下文中进行解析 - 这意味着没有玩家链接。所以 <code>%player_name%</code> 不知道该给哪个玩家起名字，从而失败。</p>
<p>您可以通过输入 <code>/papi parse --null %your_placeholder%</code> 来测试这是否适用于 PAPI 中的占位符...“--null”告诉它在没有玩家上下文的情况下进行解析。 （注意：如果 PAPI 给出“未知玩家”之类的错误，您可能只需要 <a href="https://ci.extendedclip.com/job/PlaceholderAPI/">更新</a> - 此功能已在 PAPI 2.11.2 中添加）。</p>
<p>虽然许多占位符明确表明它们是否需要玩家链接，但某些插件的占位符始终需要玩家链接，即使占位符实际上并未根据解析者的变化而变化。这些情况应该被视为占位符来自的任何插件中的错误，并且您应该要求该插件的开发人员解决问题。</p>
<a id="My_NPCs_Have_Names_Like_CIT-abc_Instead_Of_Their_Actual_Names"></a><h2 id="my-npcs-have-names-like-cit-abc-instead-of-their-actual-names">我的 NPCs 的名字是 CIT-abc，而不是真实姓名</h2>
<p>如果您的 NPC 的名称长度超过 16 个字符，Citizens 会隐藏默认铭牌，然后在其位置生成全息图。隐藏铭牌的工作原理是设置记分板团队，将该团队的铭牌设置为隐藏，并将 NPC 添加到该团队。不幸的是，由于 Minecraft 实现记分板团队的方式，必须根据其名称而不是 UUID 或实际对象添加 NPCs。隐藏的默认铭牌会通过 NPC 的 UUID 获得类似于“CIT-abc”的生成值，以确保它可以唯一地添加到记分板团队中。</p>
<p>如果这个生成的名字是可见的，就意味着记分牌团队隐藏名字的方法被打破了。这通常不应该发生，因为球队是通过直接发送给玩家的数据包生成的。如果它们被阻止，则意味着某些外部插件（甚至是 Bungee/Velocity 等代理上的插件）正在覆盖或阻止团队设置。</p>
<p>如果发生这种情况，主要要做的是检查 <a href="plugin-conflict.md" title="Plugin Conflict">插件冲突</a>。查看该页面，了解如何测试插件以及发现插件有问题后该怎么做。</p>
<a id="How_To"></a><h1 id="how-to">如何做</h1>
<a id="Can_I_change_what_skin_an_NPC_has,_separately_from_its_name?"></a><h2 id="can-i-change-what-skin-an-npc-has-separately-from-its-name">我可以单独更改 NPC 的皮肤吗？</h2>
<p>是的，通过 <code>/npc skin</code>。详细说明请参见<a href="skins.md" title="Skins">皮肤</a>页面。</p>
<a id="How_do_I_make_an_NPC_run_a_command_when_a_player_clicks_it?"></a><h2 id="how-do-i-make-an-npc-run-a-command-when-a-player-clicks-it">如何让 NPC 在玩家点击时运行命令？</h2>
<p>通过 <code>/npc command</code> 详情请参阅 <a href="npc-commands.md" title="NPC Commands">NPC 点击命令</a>。</p>
<a id="My_NPCs_Aren't_Standing_On_Exactly_Their_Path_Destination"></a><h2 id="my-npcs-arent-standing-on-exactly-their-path-destination">我的 NPCs 没有站在他们的路径目的地上</h2>
<p>如果您将 NPC 设置为移动到某个位置，并且它停在几个方块之外……嗯，这很正常。寻路并不完全精确，而且并不总是知道你的意图。例如，当您选择一个块时，它将导航到该块的角落，而不是中心。它还具有何时停止的余量 - 如果余量太小，NPC 可能会超调，并且必须掉头尝试再次找到位置。一般来说，NPC 移动得越快，所需的裕度就越高。</p>
<p>您可以使用 <code>/npc help pathopt</code> 调整 NPC 的边距和其他探路器设置。您会注意到移动行为的差异，具体取决于 <code>new-finder</code> 是 true 还是 false，还取决于每个与边距相关的值。调整一些东西，直到找到你喜欢的东西。</p>
<p>~~如果你真的真的需要它来获得精确的十进制完美坐标，你必须使用 Denizen 或类似的脚本编写一个脚本，在寻路结束后传送 NPC。~~ 在现代 Citizens 中，你可以编辑 <code>config.yml</code> 将 <code>destination-teleport-margin</code> 配置为非零自动启用传送的余量。</p>
<a id="&quot;Hi,_I'm_npc&quot;_keeps_appearing_after_I_removed_text_from_an_NPC"></a><h2 id="hi-im-npc-keeps-appearing-after-i-removed-text-from-an-npc">从 NPC 中删除文本后，不断出现“嗨，我是 npc”</h2>
<p>一旦您使用 <code>/npc text</code>，就会添加 <strong>文本特征</strong>，它将一直保留到您使用 <code>/trait text</code> 将其删除。从 NPC 中清除行列表本身不会删除文本特征，您必须显式删除该特征。</p>
<a id="How_Do_I_Set_Up_An_NPC_As_A_Shop?"></a><h2 id="how-do-i-set-up-an-npc-as-a-shop">如何将NPC设置为商店？</h2>
<p>许多用户希望使用NPCs来提供商店。在弄清楚如何执行此操作时要意识到的关键点是，is: NPC 只是您点击以打开商店的操作，实际上并不需要做更多的事情。因此，对于如何 继续： 有四种不同的选项</p>
<p>答：以后<code>/npc shop</code>会起作用。在撰写本文时，这只是一个占位符实验。</p>
<p>B：您可以使用 <a href="npc-commands.md" title="NPC Commands">NPC 点击命令</a> 将点击命令添加到 NPC，其中该命令是来自任何给定商店插件的商店命令（搜索 Spigot 资源以获取选项）。</p>
<p>C：您可以使用具有本机 Citizens 集成的商店插件，例如 dtlTraders。</p>
<p>D：您可以建立自己的商店系统，并通过编写<a href="https://guide.denizenscript.com/">Denizen 脚本</a>直接与NPCs集成。</p>
<a id="How_Do_I_Make_An_NPC_Wander_Around_Like_A_Mob?"></a><h2 id="how-do-i-make-an-npc-wander-around-like-a-mob">如何让 NPC 像生物一样四处游荡？</h2>
<p>您可以使用 <code>/wp provider wander</code>，它将 NPCs 探路器设置为漫游模式。之后，您可以使用<code>/npc path</code>配置区域限制等漫游设置。</p>
<a id="Questions"></a><h1 id="questions">问题</h1>
<a id="How_Many_NPCs_Can_I_Spawn_Before_My_Server_Lags?"></a><h2 id="how-many-npcs-can-i-spawn-before-my-server-lags">在我的服务器出现延迟之前我可以生成多少个 NPCs？</h2>
<p><strong>简短回答：</strong> 没有答案，只需尝试生成一些，看看效果如何。</p>
<p><strong>详细回答：</strong> 服务器性能取决于 <em>很多</em> 的因素。</p>
<p>首先，显然 - 硬件......更快的 CPU 可以处理更多的处理，更多的 RAM 可以处理更多正在加载的世界，等等。</p>
<p>第二……好吧，实际发生了什么。在世界各地运行的 NPC 将比静止不动的 NPC 使用更多的 CPU 功率。配置为保持块加载的 NPC 将比未配置的 NPC 使用更多的 RAM。主枢纽中的 NPC 将始终被加载、生成并处于活动状态，但森林中央 3000 个方块之外的 NPC 几乎永远不会生成或处理。</p>
<p>虽然您可以遵循这一逻辑来控制事情，但您的实际限制只有通过达到这些限制才能知道。您可以使用 Java 分析器/采样器量化延迟测量（注意：不要在 Spigot/Paper 中使用 "timings" 系统...如果您没有分析器，<a href="https://www.spigotmc.org/resources/spark.57242/">spark</a> 是一个相当基本的采样器，但很容易安装在我的世界服务器上）。</p>
<a id="Why_is_my_NPC_teleporting_when_its_supposed_to_be_walking?"></a><h2 id="why-is-my-npc-teleporting-when-its-supposed-to-be-walking">为什么我的 NPC 应该在行走时却在传送？</h2>
<p>当你在路径上设置 NPC 时，它只是传送到目的地，这意味着它无法找到路径。</p>
<p>当目的地太远时，最常发生这种情况 - 默认路径范围为 25，您可以通过 <code>/npc pathrange 50</code>（或任何其他值）更改此值，最大为 100。如果您需要走得比 100 个方块更远，请考虑沿途在中间设置多个点。</p>
<p>发生这种情况的另一个原因是路径根本不可能——墙壁挡住了路，地板上有洞等等。在这种情况下，当然要添加一条路。</p>
<p>在某些情况下，如果探路者不理解地毯、石板、大门等障碍物，路径可能会意外被阻挡。如果是这种情况，请确保在 Citizens 配置中启用 new-finder 和 new-finder-open-doors。</p>
<p>如果您希望 NPC 在路径不可能时不移动，请使用 <code>/wp disableteleport</code>。</p>
<a id="API"></a><h1 id="api">API</h1>
<a id="How_Do_I_Make_NPCs_Remove_When_The_Server_Shuts_Down?"></a><h2 id="how-do-i-make-npcs-remove-when-the-server-shuts-down">如何让NPCs在服务器关闭时删除？</h2>
<p>简而言之，您可能第一反应不是在关机时删除 NPCs，而是简单地禁用它们保存。</p>
<p>为此，您可以为您的插件创建一个自定义 NPC 注册表来存储临时 NPCs。</p>
<p>实现示例： 的示例代码</p>
<div class="highlight"><pre>    public final NPCRegistry registry = CitizensAPI.createAnonymousNPCRegistry(new MemoryNPCDataStore());

    public void yourMethod() {
        registry.createNPC(EntityType.PLAYER, "Bob");
    }
</pre></div>
<a id="How_Do_I_Track_My_Custom_NPC?"></a><h2 id="how-do-i-track-my-custom-npc">如何追踪我的定制 NPC？</h2>
<p>我们从 API 新用户那里收到了很多关于分配 NPC ids、跟踪 NPC ids、是否应该使用 ids 或 uuid 等问题。</p>
<p>基本上所有此类问题的答案都是：呃，好吧，不要！您与 NPC 相关的自定义数据或行为应通过特征分配！查看 <a href="https://wiki.citizensnpcs.co/API#Creating_a_Trait" title="API">API#Creating_a_Trait</a> 了解更多信息。</p>
<a id="More_API_Topics"></a><h2 id="more-api-topics">更多 API 主题</h2>
<p>大多数与 API 相关的问题都可以通过 <a href="https://wiki.citizensnpcs.co/API" title="API">API</a> 页面得到解答。</p>
<a id="Historical"></a><h1 id="historical">历史</h1>
<a id="How_Do_I_Add_Multiple_Lines_To_An_NPC's_Name?"></a><h3 id="how-do-i-add-multiple-lines-to-an-npcs-name">如何为NPC的名称添加多行？</h3>
<p>~~我的世界中的实体名称只有一行。但是，您可以仅生成多个实体来形成名称。~~</p>
<p>~~最简单的方法就是下载任何全息图插件，并将全息图放置在 NPC 上方以制作这些“附加线”。~~</p>
<p>~~如果你不想为此下载新插件，只需生成重力= false、标记= true、可见= false的盔甲盔甲架实体，并将名称设置为附加行即可。~~</p>
<p>在现代版本中，您现在可以使用 <code>/npc hologram</code> 来实现此目的。</p>
<a id="NPC_names_are_capped_at_only_16_characters!_Or,_'/npc_name'_won't_work!"></a><h3 id="npc-names-are-capped-at-only-16-characters-or-npc-name-wont-work">NPC 名称最多只能包含 16 个字符！或者，“/npc name”将不起作用！</h3>
<p>~~最常见的与 Citizens 的插件冲突是由记分板插件引起的。~~</p>
<p>~~这可能会导致以下问题：NPC 名称上限为 16 个字符（而不是正常的 48 个字符）、<code>/npc name</code> 无法正确切换铭牌可见性，或其他与记分板相关的功能失败。~~</p>
<p>~~这可能是由任何形式的记分板相关插件引起的，例如添加侧边栏的插件（如 Featherboard 所做的）、编辑玩家姓名标签、添加自定义的 Below_name 行或类似插件。~~</p>
<p>~~这不是一个不可避免的问题，而是许多记分板插件犯的错误造成的。有兴趣的话可以在<a href="plugin-conflict.md" title="Plugin Conflict">插件冲突</a>阅读这个错误的技术细节~~</p>
<p>~~但是，对用户的修复很简单：要么向记分板插件的开发人员报告问题，要么切换到未损坏的记分板插件（如果您想要侧边栏，请考虑 <a href="https://forum.denizenscript.com/viewtopic.php?f=13&amp;t=147">Magic Sidebar 脚本</a>）。~~</p>
<p>这在最近的版本中得到了修复。</p>
<a id="How_do_I_upgrade_from_old_versions_to_Citizens_2.0?"></a><h3 id="how-do-i-upgrade-from-old-versions-to-citizens-20">如何从旧版本升级到Citizens 2.0？</h3>
<p>请参阅 <a href="installation.md" title="Installation">安装</a> 页面。</p>
<a id="How_do_I_get_more_NPC_types?"></a><h3 id="how-do-i-get-more-npc-types">如何获得更多 NPC 类型？</h3>
<p>NPC 类型现在称为 "traits"。这些不再是您放置在 <em>/plugins/Citizens/types</em> 目录中的内置 JAR。您必须下载每个单独的角色并将其放置在 <em>/plugins</em> 文件夹中。</p>
<p>您可以在 <a href="characters.md" title="Characters">角色类型</a> 页面上找到有关特征的更多信息，或者在 <a href="https://wiki.citizensnpcs.co/API" title="API">API</a> 页面上学习如何创建自己的特征。</p>
<a id="See_Also"></a><h2 id="see-also">另请参阅</h2>
<p><a href="configuration.md" title="Configuration">配置</a></p>
<p><a href="commands.md" title="Commands">命令</a></p>
<p><a href="permissions.md" title="Permissions">权限</a></p>
<table>
<thead>
<tr>
<th>快速导航</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="category-usage.md" title="Category:Usage">用途</a></td>
<td><a href="installation.md" title="Installation">安装</a>  · 常见问题  · <a href="commands.md" title="Commands">命令</a>  · <a href="editors.md" title="Editors">编辑器</a>  · <a href="characters.md" title="Characters">角色类型</a>  · <a href="https://wiki.citizensnpcs.co/API" title="API">API</a>  ·</td>
</tr>
<tr>
<td><a href="category-configuration.md" title="Category:Configuration">配置</a></td>
<td><a href="configuration.md" title="Configuration">配置</a>  · <a href="text-syntax.md" title="Text Syntax">文本语法</a>  · <a href="permissions.md" title="Permissions">权限</a>  · <a href="waypoints.md" title="Waypoints">路径点</a>  · <a href="data-storage.md" title="Data Storage">数据存储</a></td>
</tr>
</tbody>
</table>

