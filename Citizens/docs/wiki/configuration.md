---
title: 配置
source_url: https://wiki.citizensnpcs.co/Configuration
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5511
---


<a id="top"></a>

# 配置

<p>Citizens 配置在文件 <em>/plugins/Citizens/config.yml</em> 中处理。有关每个设置的详细信息，请参阅下文。有关 &lt;npc&gt; 等文本节点的更多信息，请参阅 <a href="text-syntax.md" title="Text Syntax">文本语法</a> 页面。</p>
<a id="Default_Configuration"></a><h2 id="default-configuration">默认配置</h2>
<div class="highlight"><pre># Citizens Configuration

general:
  authlib:
    profile-url: https://sessionserver.mojang.com/session/minecraft/profile/ # generally shouldn't be touched, but allows you to configure a custom GameProfile server for advanced users
  debug-chunk-loads: false # for advanced debugging of when chunks are loaded and why
  debug-file: '' # whether to log debug output to a file instead of to console
  debug-mode: false # enables debugging mode with extra information on spawning, skin fetching, etc.
  debug-pathfinding: false # enables pathfinding debugging which shows a visual display (yellow flowers) of where NPCs are pathfinding to
  color-scheme:
    message-error: &lt;red&gt; # the error message colour, default red
    message-highlight: &lt;yelloe&gt; # the highlight colour, default yellow
    message: &lt;green&gt; # the default message colour, default green
  translation:
    locale: '' # if you want to use a specific language translation such as fr_FR etc.
  reload-warning-enabled: true # whether to require /citizens reload entered twice
npc:
  always-use-name-holograms: false # whether to always use name holograms (armor stands) for nameplates rather than custom names
  chat:
    options:
      bystanders-hear-targeted-chat: true 
      max-number-of-targets-to-show: 2
      multiple-targets-format: &lt;target&gt;|, &lt;target&gt;| &amp; &lt;target&gt;| &amp; others
      range: 5
      max-text-range: 500
      talk-to-npcs: true # whether to include NPCs in chat
    format:
      no-targets: '[&lt;npc&gt;]: &lt;text&gt;'
      with-target-to-bystanders: '[&lt;npc&gt;] -&gt; [&lt;target&gt;]: &lt;text&gt;'
      to-target: '[&lt;npc&gt;] -&gt; You: &lt;text&gt;'
      with-targets-to-bystanders: '[&lt;npc&gt;] -&gt; [&lt;targets&gt;]: &lt;text&gt;'
  pathfinding:
    new-finder:
      iterations-per-tick: 5000 # how many steps to run of the new pathfinder every tick. Useful when you want to spread pathfinding over multiple ticks
      check-bounding-boxes: false # whether to check bounding boxes of entities can fit e.g. through single block gaps or fences etc
      open-doors: false # whether to open/close doors while pathfinding
    defaults:
      destination-teleport-margin: -1 # teleport to the destination when below this threshold. e.g. you may want to teleport to the exact destination if &lt;2 blocks away
    default-distance-margin: 2 # the distance from the goal to stop early while moving along a path measured in blocks squared
    default-path-distance-margin: 1 # the distance from the goal to stop early while finding a path measured in blocks
    update-path-rate: 20 # how often to update the path in ticks, typically for entity targeting
    maximum-new-pathfinder-iterations: 10000 # the maximum number of blocks to search while pathfinding using the new pathfinder 
    minecraft:
      max-fall-distance: 3 # the maximum fall distance to check while pathfinding (old pathfinder)
    attack-range: 3.0625
    use-new-finder: false # whether to use the built in Citizens A* pathfinder instead of Minecraft's 
    disable-mc-fallback-navigation: true # minecraft by default will try to use 'fallback' pathfinding where it returns the closest reachable block to the destination. by default try to reach the destination only.
  default:
    bossbar-view-range: 64 # the bossbar view range, blocks
    look-close:
      enabled: false
      range: 5 # range in blocks
      random-look-enabled: false
      random-look-delay: 60 # delay in ticks
      disable-while-navigating: true
    pathfinding:
      range: 75.0 # the maximum pathfinding range to destination in blocks
    random-talker: true 
    realistic-looking: false # whether to check line of sight when looking close
    stationary-ticks: -1 # how many ticks can an NPC be stuck in the same block before teleporting to the goal / performing the 'stuck action'
    block-breaker-radius: -1 # the default radius in blocks for the NPC to pathfind to when breaking blocks
    talk-close:
      enabled: false
      range: 5
    text: # default text
      '0': Hi, I'm &lt;npc&gt;!
    waypoints:
      cache-paths: false # whether to cache paths found for /npc path. eliminates pathfinding when used
  limits:
    default-limit: 10
    max-permission-checks: 100 # number of permission nodes to check when using NPC limits
    max-packet-entries: 15 
    max-speed: 100
  tablist:
    disable: true # whether to keep NPCs on the tab list
  chunks:
    always-keep-loaded: false
  controllable:
    max-ground-speed: 0.5 # maximum speed while on the ground
    use-boat-controls: true # using WASD type controls
    ground-direction-modifier: 1.0 # % speed modifier to turning while on the ground
  skins:
    max-retries: -1 # maximum time to try from Mojang
    retry-delay: 120 # delay in ticks between retries
    rotation-update-degrees: 90.0 
    use-latest-by-default: false # whether to always fetch new skin updates
    view-distance: 100.0 
    placeholder-update-frequency-ticks: 6000 # how often to update skin placeholders, in ticks
  packets:
    update-delay: 30 # performance option, lower = faster updates to equipment, higher = slower updates but more performance
  selection:
    quick-select: false 
    item: stick # selection item
    message: &lt;b&gt;You selected &lt;a&gt;&lt;npc&gt;&lt;b&gt;!
  player:
    remove-from-list: true
  server-ownership: false
  text:
    max-talk-cooldown: 5
    min-talk-cooldown: 10
    talk-item: book
  teleport-delay: -1
  player-scoreboard-teams:
    enable: true
  follow:
    teleport-across-worlds: true # whether to teleport cross-world when /npc follow is enabled
  commands:
    global-delay-seconds: 1 # the global delay between click commands in seconds. set to 0 for no delay between commands
    error-messages:
      maximum-times-used: You have reached the maximum number of uses ({0}).
      missing-item: Missing {1} {0}
      no-permission: You don't have permission to do that.
      not-enough-experience: You need at least {0} experience.
      not-enough-money: You need at least ${0}.
      on-cooldown: Please wait for {minutes} minutes and {seconds_over} seconds.
      on-global-cooldown: Please wait for {minutes} minutes and {seconds_over} seconds.
advanced:
  check-minecraft-version: true
economy:
  npc:
    cost: 100.0 # the cost of /npc create if using economy integration
storage:
  save-task:
    delay: 72000
  file: saves.yml
  type: yaml
subplugins:
  folder: plugins

</pre></div>
<p>旧配置</p>
<p>将鼠标悬停在每个字段上可查看每个字段的用途。</p>
<div class="highlight"><pre># Citizens Configuration
npc:
 chat:
   prefix: '[&lt;npc&gt;]: '
 selection:
   quick-select: false
   item: 280
   message: &lt;b&gt;You selected &lt;a&gt;&lt;npc&gt;&lt;b&gt;!
 default:
   look-close: false
   random-talker: true
   talk-close: false
 talk:
   max-cooldown: 60
   min-cooldown: 30
   talk-item: 340
 server-ownership: false

general:
 debug-mode: false
subplugins:
 folder: 'plugins'
</pre></div>
<p>{{#if:|}}</p>
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
<td>配置·<a href="text-syntax.md" title="Text Syntax">文本语法</a>·<a href="permissions.md" title="Permissions">权限</a>·<a href="waypoints.md" title="Waypoints">路径点</a>·<a href="data-storage.md" title="Data Storage">数据存储</a></td>
</tr>
</tbody>
</table>

