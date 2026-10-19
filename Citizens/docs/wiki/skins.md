---
title: 皮肤
source_url: https://wiki.citizensnpcs.co/Skins
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5467
---


<a id="top"></a>

# 皮肤

<a id="NPC_Skins"></a><h2 id="npc-skins">NPC 皮肤</h2>
<p>自 Citizens 首次发布以来，许多服务器管理员都要求定制 NPC 皮肤。在最近的 Minecraft 版本中，可以通过新的玩家数据包系统控制 NPC 的皮肤。默认情况下，NPC 将具有默认的 Steve 或 Alex 皮肤。您可以使用<code>/npc skin [NAME]</code>命令设置NPC的皮肤。例如，<code>/npc skin mcmonkey4eva</code></p>
<a id="What's_the_best_way_to_set_a_custom_skin?"></a><h2 id="whats-the-best-way-to-set-a-custom-skin">设置自定义皮肤的最佳方法是什么？</h2>
<p>如果您想设置自定义皮肤（玩家上还没有的皮肤），请使用 <code>/npc skin --url [image]</code>。 “[image]”部分必须填写有效的公共图像直接链接。 "public" 意味着它位于网络主机上（您可以使用 Discord 或 <a href="https://imgur.com">伊姆古尔</a> 或其他任何东西），而 "direct" 意味着它是一个以包含原始图像的“.png”结尾的链接（不是指向相册或类似内容的链接。默认情况下，Imgur 会为您提供一个相册链接，您必须右键点击 -&gt; 复制图像URL）。</p>
<p>例如：<code>/npc skin --url https://gamepedia.cursecdn.com/minecraft_gamepedia/3/37/Steve_skin.png</code></p>
<p>请注意，<code>--url</code> 功能由 <a href="https://mineskin.org/">矿皮</a> 内部支持，在某些情况下，直接使用他们的网站可能会有所帮助。</p>
<p>如果您想要 URL 中的 <strong>苗条模型</strong>（又名“Alex 模型”）（3 像素宽臂而不是 4 像素），将皮肤图像直接上传到 <a href="https://mineskin.org/">矿皮</a> 并使用页面上的模型选择选项可能会有所帮助。</p>
<a id="Other_Options"></a><h2 id="other-options">其他选项</h2>
<p>您可以使用 <code>/npc skin [NAME] -l</code>（小写 L）始终为玩家使用最新的皮肤（如果玩家更改皮肤则更新）。如果未设置，将保留当前皮肤（使用该命令时）。</p>
<p>您可以从控制台（或任何大输入命令发送器）使用 <code>/npc skin -t [uuid] [data] [signature]</code> 从 Mojang 设置非常具体的完整皮肤 blob。如果您不确切知道那是什么，请不要使用它。它是一个开发者工具。</p>
<p>请注意，某些站点（例如 <a href="https://mineskin.org/">https://mineskin.org/</a>）允许您生成 <code>-t</code> 选项的值。</p>
<a id="Mirroring_A_Player's_Current_Skin"></a><h2 id="mirroring-a-players-current-skin">镜像玩家当前的皮肤</h2>
<p>如果您希望每个玩家都能看到自己当前应用于 NPC 的皮肤，请安装 <a href="https://denizenscript.com/">Denizen</a>，然后使用命令 <code>/npc mirrorskin</code>。您还可以通过 <code>/npc mirrorname</code> 镜像名称，或使用 <code>/npc mirrorequip</code> 镜像配备的物品。</p>
<a id="For_API_Users"></a><h2 id="for-api-users">对于API用户</h2>
<p>如果您使用Java Citizens API，您可以通过<code>npc.getOrAddTrait(SkinTrait.class)</code>并调用<code>setSkinName</code>等方法来控制NPCs上的皮肤。请参阅 <a href="https://jd.citizensnpcs.co/net/citizensnpcs/trait/SkinTrait.html">皮肤特征 JavaDoc</a> 了解更多信息。</p>
<p><strong>Note:</strong> 您不能（也不应该）从图像或 URL 直接通过 Java API 设置。相反，将图像上传到 <a href="https://mineskin.org/">矿皮</a> 并保存纹理+签名数据（将它们存储在字符串或配置文件中），然后使用 <code>setSkinPersistent(uniqueId, signature, texture)</code> 进行设置。</p>
<p><strong>还有note:</strong> 如果您要创建一个新的 NPC 并给它一个皮肤，最好在调用 <code>spawn()</code> 之前给它一个皮肤，因为第一次生成将触发默认皮肤加载，这可能会很慢，甚至会覆盖您的自定义皮肤。如果您在生成调用之前设置了皮肤，则它不会尝试加载默认皮肤。</p>
<a id="Common_Issues"></a><h2 id="common-issues">常见问题</h2>
<p>许多问题都会导致皮肤系统出现故障。如果您遇到问题，请确保 following:</p>
<ul>
<li>您正在运行从 <a href="https://www.spigotmc.org/wiki/buildtools/">https://www.spigotmc.org/wiki/buildtools/</a> 获取的完全最新的 Spigot 服务器，该服务器运行受支持的最新版本的 Minecraft。 （Paper 通常也有效）。您可以使用<code>/version</code>来检查您的服务器的版本。</li>
<li>您正在运行 Citizens2 的最新开发版本 <a href="http://ci.citizensnpcs.co/job/Citizens2/">http://ci.citizensnpcs.co/job/Citizens2/</a> 请验证具体的内部版本号（不是文件版本名称） 您可以使用 <code>/version citizens</code> 来检查此内部版本号。</li>
<li>您有一个专用服务器（不是共享托管服务！）</li>
<li>您完全拥有服务器的 IP（服务器上没有其他端口被其他 Minecraft 服务器使用！（除非它们也是您自己的服务器。））</li>
<li>您正在在线模式下运行服务器（离线模式服务器无法工作！）（请注意，如果您在 Bungee 网络上，则必须启用“bungeecord: true”以确保游戏知道它仍然可以连接到 Mojang 的服务器来下载皮肤）。</li>
<li>当前日志文件 (<code>logs/latest.log</code>) 中没有任何错误。任何错误，即使看似无关，也必须修复！</li>
<li>您不受 Mojang 的费率限制。如果您最近加载了太多皮肤（来自玩家头部头骨物品或来自 npc 皮肤命令），则可能会发生这种情况。这个问题可以通过等待一段时间而不加载更多皮肤来解决，以允许 Mojang 降低速率限制。</li>
<li>Mojang 的服务器已上线。检查 <a href="https://status.mojang.com/check">Mojang 状态页面</a> 是否显示绿色。如果皮肤通常可以使用，但突然有一段时间无法使用，则可能只是官方服务器已关闭。</li>
</ul>
<p>如果您确认满足所有这些要求，但仍然遇到问题，请随时向 <a href="https://github.com/CitizensDev/Citizens2/issues">GitHub</a> 发布问题或在 <a href="https://discord.gg/Q6pZGSR">不和谐</a> 上询问并提供尽可能多的信息（至少粘贴您当前的日志文件和 Citizens saves.yml 文件）</p>
<p>请 <strong>不要</strong> 在请求帮助时对上述任何一项撒谎。它们并不是为了“抓住你”或类似的东西：列出这些要求是因为如果不满足这些要求 <strong>WILL</strong> 就会导致问题，如果你说你满足了它们但实际上没有，你只会浪费每个人的时间（包括你自己的时间！）。</p>
<a id="Technical_Info"></a><h2 id="technical-info">技术信息</h2>
<p>如果您对皮肤系统内部工作原理（纹理/签名系统）感兴趣，可以查看皮肤斑点系统 <a href="https://one.denizenscript.com/denizen/lngs/player%20entity%20skins">在 Denizen 文档网站上</a> 的说明。</p>
<a id="Additional_Resources"></a><h2 id="additional-resources">其他资源</h2>
<ul>
<li>如果您经常重复使用皮肤，这里有一个 Denizen 脚本，用于在 NPCs 上保存/加载皮肤：<a href="https://forum.denizenscript.com/resources/npc-skin-save-load.8/">NPC 皮肤保存/加载</a></li>
<li>Mineskin 有一个皮肤库，您可以查看：<a href="https://mineskin.org/gallery">Mineskin Gallery</a></li>
<li>这里还有一些皮肤列表网站：<a href="https://www.minecraftskins.com/">MinecraftSkins.com</a>、<a href="https://www.minecraftskins.net/">MinecraftSkins.net</a>、<a href="https://www.planetminecraft.com/skins/">PlanetMinecraft Skins</a></li>
<li>Minecraft 关于皮肤的 Wiki 页面：<a href="https://minecraft.fandom.com/wiki/Skin">Minecraft Wiki: Skins</a></li>
<li>这是一个 Denizen 脚本，可以像编辑 NPC 皮肤一样轻松地编辑玩家皮肤：<a href="https://forum.denizenscript.com/resources/player-skin-command.54/">Player Skin Command</a></li>
</ul>
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
<td><a href="installation.md" title="Installation">安装</a>  · <a href="frequently-asked-questions.md" title="Frequently Asked Questions">常见问题</a>  · <a href="commands.md" title="Commands">命令</a>  · <a href="editors.md" title="Editors">编辑器</a>  · <a href="characters.md" title="Characters">角色类型</a>  · <a href="https://wiki.citizensnpcs.co/API" title="API">API</a>  ·</td>
</tr>
<tr>
<td><a href="category-configuration.md" title="Category:Configuration">配置</a></td>
<td><a href="configuration.md" title="Configuration">配置</a>  · <a href="text-syntax.md" title="Text Syntax">文本语法</a>  · <a href="permissions.md" title="Permissions">权限</a>  · <a href="waypoints.md" title="Waypoints">路径点</a>  · <a href="data-storage.md" title="Data Storage">数据存储</a></td>
</tr>
</tbody>
</table>

