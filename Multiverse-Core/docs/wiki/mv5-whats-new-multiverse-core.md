---
title: Multiverse-Core 更新日志
source_url: https://mvplugins.org/mv5/whats-new/multiverse-core/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# Multiverse-Core 更新日志

<a id="Revamped"></a><h3 id="revamped">改造后</h3>
<ol>
<li>
<p>带有 <strong>完整制表符补全</strong> 和标志的 <em>改造后</em> 命令结构（尝试所有命令并查看！）</p>
</li>
<li>
<p><em>改造后</em> 配置文件，带有清晰的注释</p>
</li>
<li>
<p><em>改造后</em> 消息输出，支持本地化</p>
</li>
<li>基于每个玩家客户端的语言设置的语言</li>
<li>
<p>语言的配置选项：<code>per-player-locale</code> 和 <code>default-locale</code></p>
</li>
<li>
<p><em>改造后</em> 生成器插件支持（第 3 方插件可以挂接到 mv 以提供生成器选项选项卡完成）</p>
</li>
<li>
<p><em>改造后</em> <code>mv list</code> 命令具有分页和过滤功能，更好的输出格式</p>
</li>
<li>通过正则表达式匹配改进了过滤器和分页选项（也适用于其他列表相关命令）</li>
<li>
<p>包括使用 <code>/mv list --raw</code> 在世界别名和世界名称之间切换的选项</p>
</li>
<li>
<p><em>改造后</em> 传送处理。现在使用paper的AsyncTeleport API！</p>
</li>
<li>支持在单个命令中传送多个玩家</li>
<li>更新了传送权限，具有更精细的控制（e.g.<code>multiverse.teleport.w.self.worldname</code>）</li>
<li>实施配置选项 <code>use-finer-teleport-permissions</code> 以使用更精细的传送权限。启用后，您将需要 <code>multiverse.teleport.&lt;self|other&gt;.&lt;type&gt;.&lt;finer&gt;</code></li>
<li>
<p>为 <code>/mv tp</code> 命令实现配置选项 <code>concurrent-teleport-limit</code>。 （仅供参考，如果您不知道，您可以使用 <code>/mvtp Player1,Player2 &lt;world&gt;</code> 或 <code>/mvtp @a &lt;world&gt;</code> 传送多个玩家）</p>
</li>
<li>
<p><em>改造后</em> 具有新配置选项的 <code>/mv confirm [otp]</code> 命令</p>
</li>
<li>实施确认OTP以进一步减少意外运行危险命令的机会。示例命令是 <code>/mv confirm 384</code>。可以用config.yml中的<code>use-confirm-otp</code>进行更改。</li>
<li>实施确认模式来控制何时需要 <code>/mv confirm</code>。有关详细信息，请参阅 config.yml 中的 <code>confirm-mode</code>。</li>
<li>
<p>添加 <code>/mv confirm</code> 超时的配置选项，并将其默认超时持续时间增加到 30 秒</p>
</li>
<li>
<p><em>改造后</em>区块安全检查</p>
</li>
<li>大大提高算法逻辑和效率</li>
<li>在搜索之前检查当前位置是否安全（修复了一些边缘情况，例如生成位置位于单个块上的虚空世界）</li>
<li>
<p>添加了 2 个新的配置选项 <code>safe-location-horizontal-search-radius</code> 和 <code>safe-location-vertical-search-radius</code></p>
</li>
<li>
<p><em>改造后</em> 重生世界处理具有更多配置选项</p>
</li>
<li>添加<code>default-respawn-within-same-world</code>选项。默认情况下它基本上会禁用重生处理</li>
<li>
<p>添加<code>enforce-respawn-at-world-spawn</code>配置选项。它将添加对普通 <code>/spawnpoint</code> 命令的支持</p>
</li>
<li>
<p><em>改造后</em> 实体生成配置的处理</p>
<ul>
<li>利用bukkit的<a href="https://jd.papermc.io/paper/1.21.5/org/bukkit/entity/SpawnCategory.html">生成类别</a>确保所有实体都可以配置</li>
<li>配置实体生成的新命令：<code>/mv entity-spawn-config modify [world] &lt;spawn-category&gt; &lt;set|add|reset|remove&gt; &lt;property&gt; [value]</code></li>
<li>查看实体生成配置的新命令：<code>/mv entity-spawn-config info [world]</code></li>
<li>用于清除已禁用实体的新命令：<code>/mv purge-entities [world]</code></li>
<li>用于清除所有实体的新命令，可以选择针对特定的生成类别：<code>/mv purge-all-entities [world] [spawn-categories]</code></li>
<li>添加对控制非生命实体生成的支持（例如您可以使用 MISC SpawnCategory 禁用 ITEM 掉落）</li>
</ul>
</li>
</ol>
<a id="Newly-Added"></a><h3 id="newly-added">新增</h3>
<ol>
<li>
<p><em>新</em> 用于使用生成器字符串创建平坦世界的选项 (<code>mv create flat normal --world-type flat --generator-settings {"layers":[{"block":"stone","height":1},{"block":"grass_block","height":1},{"block":"sea_lantern","height":1}],"biome":"plains"}</code>)</p>
</li>
<li>
<p><em>新</em> 加入位置功能可将玩家传送到每次加入服务器时在固定位置生成</p>
</li>
<li>
<p><em>新</em> 挂钩到 PlaceholderAPI 以获取多元宇宙相关信息（e.g.<code>%multiverse-core_alias_&lt;world&gt;%</code>）</p>
</li>
<li>
<p><em>新</em> 支持单个命令传送多个玩家</p>
</li>
<li>
<p><em>新</em> 配置选项禁用游戏模式强制</p>
</li>
<li>
<p><em>新</em> 克隆/重新生成世界时保留世界属性、游戏规则和世界边界数据的选项</p>
</li>
<li>
<p><em>新</em> 支持创建具有单一生物群系的世界（您现在可以执行 <code>/mv create &lt;worldname&gt; normal --biome &lt;biomename&gt; and  /mv import &lt;worldname&gt; normal --biome @single:&lt;biome&gt;</code>）</p>
</li>
<li>
<p><em>新</em>确认otp进一步减少意外运行危险命令的机会。示例命令是 <code>/mv confirm 384</code>。您可以在config.yml中用<code>use-confirm-otp</code>进行更改。</p>
</li>
</ol>
<a id="Other-Features"></a><h3 id="other-features">其他特点</h3>
<ol>
<li>
<p>添加对删除已卸载世界的支持</p>
</li>
<li>
<p>添加配置选项，以便在 <code>resolve-alias-name</code> 的命令和目标中使用世界别名</p>
</li>
<li>
<p>添加对使用第一个生成位置的目标字符串的支持</p>
</li>
<li>
<p>添加对运行世界相关命令的命令方块的支持（对于 pre-1.21，papermc 已在 1.21.4 内部修复了此问题）</p>
</li>
<li>
<p>World 及其在 <code>worlds.yml</code> 中的属性现在按字母顺序排列</p>
</li>
<li>
<p>实施调试权限的配置选项</p>
</li>
<li>
<p>添加对将多个玩家传送到各自出生点的支持。选择多个玩家同<code>/mvtp</code></p>
</li>
<li>
<p>使用 <code>/mv dumps</code> 命令生成调试链接而不是 <code>/mv version -p</code> 的调试粘贴服务</p>
</li>
<li>
<p>为开发者 API 实现更多 mv 世界事件 -&gt; Load、Unload、Clone、Regen、Remove</p>
</li>
<li>
<p>实施配置选项以禁用旧别名，以减少制表符完成中无用的混乱（i.e。禁用 <code>/mvcreate</code> 的别名，因为您可以轻松使用具有制表符完成支持的 <code>/mv create</code>）</p>
</li>
</ol>
<a id="Other-Fixes"></a><h3 id="other-fixes">其他修复</h3>
<ol>
<li>
<p>修复使用传送门传送时入场费双倍收取 $$$ 的问题</p>
</li>
<li>
<p>使用 PortalCreateEvent 修复已弃用的 EntityCreatePortalEvent（是的，不再有烦人的控制台警告）</p>
</li>
<li>
<p>整个插件中的错误消息更加清晰，从设置配置值到世界管理器操作</p>
</li>
</ol>

