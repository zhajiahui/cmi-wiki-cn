---
title: NPC 点击命令
source_url: https://wiki.citizensnpcs.co/NPC_Commands
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5546
---


<a id="top"></a>

# NPC 点击命令

<h2 id="npc">NPC 点击命令</h2>
<p>要在玩家点击 Citizens NPC 时执行命令，使用 /npc command（<code>/npc help command</code>）。</p>
<h2 id="_1">添加命令</h2>
<p>默认情况下，"/npc command" 以<strong>服务器</strong>身份执行命令。添加 "-p" 参数后，改为以<strong>点击 NPC 的玩家</strong>身份执行。</p>
<p>例如，执行 <code>/npc command add -p help</code> 后，玩家点击 NPC 时，NPC 会自动以该玩家身份执行 "/help"。填写命令名称时不要加上开头的 "/"。</p>
<p>使用 "&lt;p&gt;" 自动填入玩家名称，使用 "&lt;npc&gt;" 自动填入 NPC ID。</p>
<p>例如，<code>/npc command add kick &lt;p&gt;</code> 会在玩家点击 NPC 时自动踢出该玩家。</p>
<p>另一个常见例子是 <code>/npc command add tp &lt;p&gt; 0 64 0</code>，它会将点击 NPC 的玩家传送到指定坐标。这里假定使用原版 'tp' 命令；如果使用 Essentials，应改用 'tppos'。</p>
<p>这里可以填写 Minecraft 或任意插件提供的命令。例如，安装 Multiverse 后，<code>/npc command add mvtp &lt;p&gt; myworldname</code> 会使用 Multiverse 的世界传送命令。</p>
<h3 id="_2">其他占位符</h3>
<p>安装 PlaceholderAPI 后，可以在命令中使用 PAPI 占位符，例如 <code>/npc command add msg &lt;p&gt; The current TPS is %server_tps%</code>。</p>
<p>可用的占位符及其格式见 <a href="https://github.com/PlaceholderAPI/PlaceholderAPI/wiki">PlaceholderAPI 文档</a>。</p>
<h3 id="_3">权限</h3>
<p>默认情况下，任何人都能点击 NPC 来执行命令，不要求权限。</p>
<p>使用 <code>-p</code> 时，<strong>命令本身</strong>的权限检查会针对该玩家进行。</p>
<p>使用 <code>-o</code> 时，命令以 OP 身份执行，即<strong>临时</strong>将该玩家视为服务器 OP。若某个插件不认可 OP，或保护插件禁用了 OP，则可能例外。请注意，<code>-o</code> 可能产生副作用或性能问题。</p>
<p>通常最好以服务器身份执行，也就是不填写 <code>-p</code> 或 <code>-o</code>，使用默认的 as-server。这样不需要玩家拥有权限。命令中需要玩家名称的位置，应使用 <code>&lt;p&gt;</code> 填入。</p>
<p>如果还要自行添加权限<strong>要求</strong>，在添加命令时填写 <code>--permission my.perm.here</code>。</p>
<h3 id="npc_1">让 NPC 对玩家说话</h3>
<p>要通过 NPC 命令让 NPC 对玩家说话，可以使用下面的命令；如果不需要点击命令功能的完整选项，直接使用 <code>/npc text</code> 即可。</p>
<p><code>/npc command add say MESSAGE HERE</code></p>
<p>Citizens 会自动重定向 "say" 命令，让 NPC 说话，而不是让服务器控制台说话。</p>
<p>内部实现是将 <code>/say MESSAGE HERE</code> 替换为 <code>/npc speak MESSAGE HERE --target &lt;p&gt; --id &lt;id&gt;</code>。</p>
<p>要使用原版 "say" 命令，可以执行 <code>/npc command add minecraft:say ...</code>。</p>
<a id="Bungee"></a><h3 id="bungee">Bungee</h3>
<p>在 Bungee 服务器上，支持 Bungee 的 <code>server</code> 命令，例如 <code>/npc command add -p server MyServerName</code>。这是 Citizens 内置的特殊处理，会自动绕过通常的权限要求。</p>
<p>Velocity 或其他代理端只有在实现了 Bungee 协议时，才可能同样可用；许多代理端都实现了该协议。</p>
<p>其他 Bungee 代理命令，以及 Velocity 或其他代理端上的其他命令，都无法直接执行。只有能在 Spigot 服务器实例内运行的命令才有效。如果要执行 Bungee 插件的命令，该插件需要提供带接口命令的 Spigot 插件，或者使用 <a href="https://github.com/DenizenScript/Depenizen/blob/master/Docs/Bungee.md">DepenizenBungee</a> 之类的通用 Bungee 控制中转工具。</p>
<h2 id="_4">删除命令</h2>
<p>输入 <code>/npc command</code>，查看当前已绑定命令及其 ID。点击删除按钮 "-"，或手动执行 <code>/npc command remove ID#</code>，即可删除命令。</p>
<h2 id="_5">执行顺序</h2>
<p>默认情况下，使用 <code>/npc command</code> 添加多条命令后，每次点击会按顺序在同一次操作中执行所有命令。</p>
<p>也可以设置为每次点击只执行一条，按固定顺序或随机顺序执行。</p>
<p>使用 <code>/npc command sequential</code>，让每次点击依次执行一条命令。</p>
<p>使用 <code>/npc command random</code>，让每次点击随机执行一条命令。</p>
<p>要恢复为一次执行全部命令，再次执行之前切换模式的命令即可。例如，之前设置了顺序模式，就再次执行 <code>/npc command sequential</code> 将其关闭，恢复默认行为。</p>
<h2 id="_6">其他选项</h2>
<p><code>/npc command</code> 还支持以下设置：</p>
<ul>
<li><code>/npc command permissions x.y.z</code>：给玩家附加临时权限。通常不建议使用，应改用 <code>-o</code>，或者直接以服务器身份执行。</li>
<li><code>/npc command add -l somethinghere</code>：响应左键点击，也就是拳击或攻击。禁用 PvP 时可能无效。</li>
<li><code>/npc command add -r somethinghere</code>：响应右键点击，即通常的交互操作。</li>
<li><code>/npc command add --n 5 somethinghere</code>：限制每名玩家的使用次数，本例为 5 次。</li>
<li><code>/npc command add --cooldown 10s somethinghere</code>：为每名玩家分别设置冷却时间，本例为 10 秒内只能使用一次。</li>
<li><code>/npc command add --gcooldown 10s somethinghere</code>：设置全局冷却，本例为 10 秒；冷却结束前，任何人都无法再次使用此 NPC。</li>
<li><code>/npc command add --delay 40t somethinghere</code>：延迟执行命令，本例为 40 刻，也就是 2 秒。</li>
<li><code>/npc command cost 50</code>：通过兼容 Vault 的经济插件收取费用，本例为 $50。余额不足的玩家无法执行；余额足够时，会先扣费再执行命令。</li>
<li><code>/npc command expcost 50</code>：收取经验等级，行为类似 'cost'，但消耗的是经验等级。</li>
<li><code>/npc command itemcost</code>：打开 GUI，设置物品费用。玩家必须支付相应物品后，命令才会执行。</li>
<li><code>/npc command hideErrors</code>：向玩家隐藏所有错误消息，例如权限不足、余额不足等。</li>
</ul>
<p><code>/npc command</code> 还有其他选项，可以在游戏中输入 <code>/npc help command</code> 查看。</p>
<h2 id="_7">常见问题与故障</h2>
<h3 id="_8">左键点击命令没有反应！</h3>
<p>在 Minecraft 中，左键“点击”实体实际上是<strong>拳击</strong>或攻击。对于玩家类型的 NPC，左键点击 NPC 就相当于_攻击一名玩家_。因此，如果在 server.properties 或通过插件禁用了 PvP，也会阻止这种“左键点击”。</p>
<p>可以采用以下任一种方式解决：</p>
<ul>
<li>A：改用右键点击。Minecraft 将其称为“实体交互”，除了限制非常严格的插件外，通常都会允许。</li>
<li>B：在配置中启用 PvP，再使用兼容 Citizens 的插件禁用<strong>真正的</strong>玩家 PvP。例如，使用 [Denizen] 时，可以采用以下脚本：</li>
</ul>
<div class="highlight"><pre>no_pvp:
    type: world
    events:
        on player damages player:
        - determine cancelled
</pre></div>
<h2 id="_9">获取更多帮助</h2>
<p>有疑问时，可以加入 <a href="https://discord.gg/Q6pZGSR">Citizens 与 Denizen 共用的 Discord</a> 寻求帮助。</p>

