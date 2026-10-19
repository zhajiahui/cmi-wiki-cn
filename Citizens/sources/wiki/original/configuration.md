Citizens configuration is handled in the file */plugins/Citizens/config.yml*. See below for detailed information on each setting. For more information on text nodes such as <npc>, see the [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax") page.

## Default Configuration

```
# Citizens Configuration

general:
  authlib:
    profile-url: https://sessionserver.mojang.com/session/minecraft/profile/ # generally shouldn't be touched, but allows you to configure a custom GameProfile server for advanced users
  debug-chunk-loads: false # for advanced debugging of when chunks are loaded and why
  debug-file: '' # whether to log debug output to a file instead of to console
  debug-mode: false # enables debugging mode with extra information on spawning, skin fetching, etc.
  debug-pathfinding: false # enables pathfinding debugging which shows a visual display (yellow flowers) of where NPCs are pathfinding to
  color-scheme:
    message-error: <red> # the error message colour, default red
    message-highlight: <yelloe> # the highlight colour, default yellow
    message: <green> # the default message colour, default green
  translation:
    locale: '' # if you want to use a specific language translation such as fr_FR etc.
  reload-warning-enabled: true # whether to require /citizens reload entered twice
npc:
  always-use-name-holograms: false # whether to always use name holograms (armor stands) for nameplates rather than custom names
  chat:
    options:
      bystanders-hear-targeted-chat: true 
      max-number-of-targets-to-show: 2
      multiple-targets-format: <target>|, <target>| & <target>| & others
      range: 5
      max-text-range: 500
      talk-to-npcs: true # whether to include NPCs in chat
    format:
      no-targets: '[<npc>]: <text>'
      with-target-to-bystanders: '[<npc>] -> [<target>]: <text>'
      to-target: '[<npc>] -> You: <text>'
      with-targets-to-bystanders: '[<npc>] -> [<targets>]: <text>'
  pathfinding:
    new-finder:
      iterations-per-tick: 5000 # how many steps to run of the new pathfinder every tick. Useful when you want to spread pathfinding over multiple ticks
      check-bounding-boxes: false # whether to check bounding boxes of entities can fit e.g. through single block gaps or fences etc
      open-doors: false # whether to open/close doors while pathfinding
    defaults:
      destination-teleport-margin: -1 # teleport to the destination when below this threshold. e.g. you may want to teleport to the exact destination if <2 blocks away
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
      '0': Hi, I'm <npc>!
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
    message: <b>You selected <a><npc><b>!
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
```

old config

Mouse over each field to see what each one is used for.

```
# Citizens Configuration
npc:
 chat:
   prefix: '[<npc>]: '
 selection:
   quick-select: false
   item: 280
   message: <b>You selected <a><npc><b>!
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
```

{{#if:|}}

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | Configuration  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
