Read below for detailed command documentation. For more info on per-type commands and permissions, see its corresponding page.

**[]** - Mandatory
  
**()** - Optional

**Command** - command's syntax
  
**Args Description** - description of the command's arguments
  
**Require Selected** - whether the command requires an NPC to be selected
  
**Require Ownership** - whether the commands requires you to be the owner of the NPC
  
**Require Mob Types** - whether the command requires an NPC to be a certain mob type(s)
  
**Permission** - command's permission node
  
**Description** - short description of the command

## Commands not listed here

**There are quite a few commands that are not listed here, mainly for reasons of maintenance order (the wiki isn't updated all that often, but the actual commands list is updated regularly.)**
 **To see the list of commands on your current version of Citizens, simply type `/npc help` in-game. You can use `/npc help 2` to view page 2, and so on (switch 2 to any page number).**
  
To see information on a specific command, you can use `/npc help create` in-game. Change the "create" to any other command name (the example will show help for the `/npc create` command).
  
  
Some commands have documentation elsewhere:

- /npc skin - [Skins](https://wiki.citizensnpcs.co/Skins "Skins")

There are also many commands that are added by other traits. see [Characters](https://wiki.citizensnpcs.co/Characters "Characters")

## Adding Click Commands

If you're looking for a way to add automatically ran commands when you click an NPC, that's explained at [NPC_Commands](https://wiki.citizensnpcs.co/NPC_Commands "NPC Commands").

## Admin Commands

Commands used for administration of Citizens.

| **Admin Commands** | | |
| --- | --- | --- |
| Command | Permission | Description |
| /citizens | citizens.admin | Show basic plugin information |
| /citizens reload | citizens.admin | Reload Citizens |
| /citizens save | citizens.admin | Save NPCs and configuration |

## Help Commands

Commands used in-game to show the help screen.

| **Help Commands** | | | | | |
| --- | --- | --- | --- | --- | --- |
| Command | Arguments | Permission | Description |
| /citizens help | *(Page)* - Page number to display | citizens.help | Show Citizens help menu |
| /npc help | *(Page)* - Page number to display | citizens.npc.help | Show NPC help menu |
| /trait help | *(Page)* - Page number to display | citizens.trait.help | Show trait help menu |
| /template help | *(Page)* - Page number to display | citizens.templates.help | Show template help menu |
| /waypoints help | *(Page)* - Page number to display | citizens.waypoints.help | Show waypoints help menu |

## NPC Commands

General commands used for all NPCs.

| **NPC Commands** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Command | Arguments | Description |
| /npc | `None` | None |
| /npc activationrange | `[range]` | Sets the activation range |
| /npc age | `[age] (-l(ock))` | Can only be used on entities that can become babies. Use the **-l** flag to lock age over time (note: relogs may be required to see this). |
| /npc aggressive | `[true|false] (-t(emporary))` | Sets the aggressive status of the entity |
| /npc ai | `(true|false)` | Sets whether the NPC should use vanilla AI |
| /npc allay | `(-d(ancing))` | Sets allay modifiers |
| /npc anchor | `(--save [name]|--assume [name]|--remove [name]) (-a) (-c)` | Manages the NPC's location anchor(s) |
| /npc areaeffectcloud | `--color [color] --duration [duration] --radius [radius] --radius_per_tick [radius] --particle [particle]` | None |
| /npc armadillo | `--state [state]` | None |
| /npc armorstand | `--visible [visible] --small [small] --marker [marker] --gravity [gravity] --arms [arms] --baseplate [baseplate] --(head|body|leftarm|leftleg|rightarm|rightleg)pose [angle x,y,z]` | Edit armorstand properties |
| /npc attribute | `[attribute] [value]` | Set various NPC attributes |
| /npc axolotl | `(-d) (--variant variant)` | Sets axolotl modifiers |
| /npc bat | `--awake [awake]` | Set bat modifiers |
| /npc bee | `(-s/-n) --anger anger` | Sets bee modifiers |
| /npc behavior | `[file.yml]` | Manages behavior trees |
| /npc boat | `--type [type]` | Sets boat modifiers |
| /npc bossbar | `--style [style] --color [color] --title [title] --visible [visible] --viewpermission [permission] --flags [flags] --track [health | placeholder] --range [range]` | Edit bossbar properties |
| /npc breakblock | `--location [x,y,z] --radius [radius]` | None |
| /npc camel | `(--pose pose)` | Sets camel modifiers |
| /npc cat | `(-s/-n/-l) --type type --ccolor collar color` | Sets cat modifiers |
| /npc chicken | `(--variant variant)` | Manage chicken modifiers |
| /npc chunkload | `(-t(emporary))` | Toggle the NPC forcing chunks to stay loaded |
| /npc collidable | `--fluids [true|false]` | Toggles an NPC's collidability |
| /npc command | `(add [command] | execute [player UUID] [hand] | remove [id|all] | permissions [permissions] (duration) | sequential | cycle | random | forgetplayer (uuid) | clearerror [type] (name|uuid) | errormsg [type] [msg] | persistsequence [true|false] | cost [cost] (id) | expcost [cost] (id) | itemcost (id)) (-s(hift)) (-l[eft]/-r[ight]) (-p[layer] -o[p]), --cooldown --gcooldown [seconds] --delay [ticks] --permissions [perms] --n [max # of uses] --gn [max # of global uses]` | Use the **-l** flag to make the command run on left click, **-r** on right click (default). **execute** triggers assigned commands as if a player clicked the npc. Set the per-player cooldown before the command can be used again using **--cooldown** (in **seconds**). Set the server-wide cooldown in seconds using **--gcooldown**. **--delay** will wait the specified amount in **ticks** before executing the command. **--permissions** will set the command to require specific permissions (separate multiple with commas). **--n** will only let the player run the command that number of times. Use **-o** to temporarily execute the command as an op and **-p** to run the command as the clicking player instead of the server. Use **-n** to run the command as the NPC instead of the clicking player. Must be a player type NPC. To give the player temporary permissions instead of op, use **/npc command permissions**. Set the cost of each click with **/npc command cost/expcost/itemcost**. Commands can be executed one by one instead of all at once by using **/npc command sequential** or **/npc command cycle**. |
| /npc configgui | `None` | Display NPC configuration GUI |
| /npc controllable | `(-m(ount),-o(wner required)) (--controls [controls]) (--enabled [true|false])` | Toggles whether the NPC can be ridden and controlled |
| /npc copier | `None` | Toggle the NPC copier |
| /npc coppergolem | `(--weatherstate state) (--weatheringtick tick)` | Controls copper golem modifiers |
| /npc copy | `(--name newname)` | Copies an NPC |
| /npc cow | `(--variant variant)` | Manage cow modifiers |
| /npc create | `[name] ((-b(aby),u(nspawned),s(ilent),t(emporary),c(enter),p(acket)) --at [x,y,z,world] --type [type] --item (item) --trait ['trait1, trait2...'] --model [model name] --nameplate [true|false|hover] --temporaryduration [duration] --registry [registry name]` | Create a new NPC |
| /npc debug | `-p(aths) -n(avigation) -i(tem in hand)` | Display debugging information |
| /npc deselect | `None` | Deselect currently selected NPC |
| /npc despawn | `(id)` | Despawn a NPC |
| /npc disguise | `--type [type]` | Manages entity disguises |
| /npc display | `--billboard [billboard] --brightness [blockLight,skyLight] --interpolationdelay [delay] --interpolationduration [duration] --height [height] --width [width] --scale [x,y,z] --viewrange [range] --leftrotation [x,y,z,w] --rightrotation [x,y,z,w] --offset [x,y,z]` | Set various display entity modifiers |
| /npc drops | `None` | Edit an NPC's drops |
| /npc endercrystal | `-b(ottom)` | Edit endercrystal modifiers |
| /npc enderdragon | `--phase [phase] --destroywalls [true|false]` | Sets enderdragon modifiers |
| /npc enderman | `-a(ngry)` | Set enderman modifiers |
| /npc entitypose | `[pose]` | Control entity pose |
| /npc equip | `None` | Toggle the equipment editor |
| /npc eval | `[expression]` | None |
| /npc flyable | `(true|false)` | Toggles or sets an NPC's flyable status |
| /npc follow | `(player name|NPC id) (-p[rotect]) (--margin [margin]) (--enable [boolean])` | Toggles NPC following you |
| /npc forcefield | `--width [width] --height [height] --strength [strength] --vertical-strength [vertical strength]` | Creates a forcefield which pushes players close to the NPC away |
| /npc fox | `--type type --sleeping [true|false] --sitting [true|false] --crouching [true|false] --interested [true|false] --pouncing [true|false] --faceplanted [true|false]` | Sets fox modifiers |
| /npc frog | `(--variant variant)` | Sets frog modifiers |
| /npc gamemode | `[gamemode]` | Changes the gamemode |
| /npc glowing | `--color [minecraft chat color]` | Toggles an NPC's glowing status |
| /npc goat | `-l(eft) -r(ight) -n(either) -b(oth) horn` | Sets goat modifiers |
| /npc gravity | `None` | Toggles gravity |
| /npc hitbox | `--scale [scale] --width/height [value] --offset [x,y,z]` | Sets the NPC hitbox |
| /npc hologram | `add [text] (--duration [duration]) | insert [line #] [text] | set [line #] [text] | remove [line #] | edit_npc [template | name | line #] | clear | lineheight [height] | viewrange [range] | margintop [line #] [margin] | marginbottom [line #] [margin]` | Controls NPC hologram text |
| /npc home | `--location [loc] --delay [delay] --distance [distance] -h(ere) -p(athfind) -t(eleport)` | Controls home location |
| /npc horse | `(--color color) (--type type) (--style style) (-cbt)` | Use the -c flag to make the NPC have a chest, or the -b flag to stop them from having a chest. |
| /npc hurt | `[damage]` | Damages the NPC |
| /npc id | `None` | Sends the selected NPC's ID to the sender |
| /npc inventory | `(player name/uuid)` | Show's an NPC's inventory |
| /npc item | `[item] (-h(and))` | Sets the NPC's item |
| /npc itemdisplay | `--transform [transform]` | None |
| /npc itemframe | `--visible [true|false] --fixed [true|false] --rotation [rotation] --item [item] --face [face]` | Sets itemframe modifiers |
| /npc jump | `None` | Makes the NPC jump |
| /npc knockback | `(--explicit true|false)` | Toggle NPC knockback |
| /npc leashable | `None` | Toggles leashability |
| /npc list | `(page) ((-a) --owner (owner) --type (type) --char (char) --registry (name))` | List NPCs |
| /npc llama | `(--color color) (--strength strength)` | Sets llama modifiers |
| /npc lookclose | `--range [range] --filter [filter] -r[ealistic looking] --randomlook [true|false] --perplayer [true|false] --randomswitchtargets [true|false] --randompitchrange [min,max] --randomyawrange [min,max] --disablewhennavigating [true|false] --targetnpcs [true|false]` | Toggle whether a NPC will look when a player is near |
| /npc mannequin | `--hide_description [true|false] --immovable [true|false] --description [description] --main_hand [LEFT|RIGHT] --skin_patch_type [type] --skin_patch_body [location] --skin_patch_cape [location] --skin_patch_elytra [location]` | None |
| /npc metadata | `set|get|remove [key] (value) (-t(emporary))` | Manages NPC metadata |
| /npc minecart | `(--offset offset)` | Sets minecart item |
| /npc mirror | `--name [true|false] --equipment [true|false]` | Controls mirroring of NPC skins and more |
| /npc model | `[name]` | None |
| /npc modelanimate | `[start|stop|clear] (name) (speed)` | None |
| /npc mount | `(--onnpc <npc id|uuid>) (-d(ismount)) (-c(ancel))` | Mounts a controllable NPC |
| /npc moveto | `x:y:z:world | x y z world` | Teleports a NPC to a given location |
| /npc mushroomcow | `(--variant [variant])` | Sets mushroom cow modifiers |
| /npc name | `(-h(over))` | Toggle nameplate visibility, or only show names on hover |
| /npc ocelot | `(--type type) (-s(itting), -n(ot sitting))` | Set the ocelot type of an NPC and whether it is sitting |
| /npc owner | `[uuid|SERVER]` | Set the owner of an NPC |
| /npc packet | `--enabled [true|false]` | Controls packet NPC settings |
| /npc painting | `(--art art)` | Set painting modifiers |
| /npc panda | `--gene (main gene) --hiddengene (hidden gene) -e(ating) -s(itting) -n (sneezing) -r(olling)` | Sets panda modifiers |
| /npc panimate | `[animation]` | Plays a player animation |
| /npc parrot | `(--variant variant)` | Sets parrot modifiers |
| /npc passive | `(--set [true|false])` | Sets whether an NPC damages other entities or not |
| /npc path | `None` | Toggle the waypoint editor |
| /npc pathopt | `--avoid-teleporting [true|false] --avoid-water [true|false] --attack-delay-duration [duration] --destination-teleport-margin [margin] --open-doors [true|false] --path-range [range] --stationary-ticks [ticks] --attack-range [range] --distance-margin [margin] --path-distance-margin [margin] --pathfinder-type [CITIZENS|MINECRAFT] --falling-distance [distance]` | Sets an NPC's pathfinding options |
| /npc pathto | `me | here | cursor | [x] [y] [z] (--margin [distance margin]) (-s[traight line])` | Starts pathfinding to a certain location |
| /npc pausepathfinding | `--onrightclick [true|false] --when-player-within [range in blocks] --pauseduration [duration] --lockoutduration [duration]` | Sets pathfinding pause |
| /npc phantom | `(--size size)` | Sets phantom modifiers |
| /npc pickupitems | `(--set [true|false])` | Allow NPC to pick up items |
| /npc pig | `(--variant variant)` | Manage pig modifiers |
| /npc piglin | `(--dancing [true|false])` | Sets piglin modifiers |
| /npc playerfilter | `-a(llowlist) -e(mpty) -d(enylist) --add [uuid] --remove [uuid] --addpermission [permission] --removepermission [permission] --addgroup [group] --removegroup [group] -c(lear) --applywithin [blocks range]` | Manages the NPC's player filter |
| /npc playerlist | `(-a(dd),r(emove))` | Sets whether the NPC is put in the playerlist |
| /npc playsound | `[sound] (category) (volume) (pitch) (--to [player]) (--at x:y:z:world)` | Plays a sound at the NPC's location |
| /npc polarbear | `(-r)` | Sets polarbear modifiers |
| /npc pose | `(--save [name] (-d) | --mirror [name] (-d) | --assume [name] | --remove [name] | --default [name]) (--yaw yaw) (--pitch pitch) (-a)` | Manage NPC poses |
| /npc potioneffect | `[add|remove|list] (--name [name] or -t for temporary) (--type [type]) (--duration [duration]) (--amplifier [amplifier]) (--icon [icon])` | None |
| /npc powered | `(--set true|false)` | Toggle a creeper NPC as powered |
| /npc pufferfish | `(--state state)` | Sets pufferfish modifiers |
| /npc rabbittype | `[type]` | Set the NPC's rabbit type |
| /npc remove | `(all|id|name| --owner [owner] | --eid [entity uuid] | --world [world])` | Remove a NPC |
| /npc rename | `[name]` | Rename a NPC |
| /npc respawn | `[delay]` | Sets an NPC's respawn delay |
| /npc rotate | `(--towards [x,y,z]) (--toentity [name|uuid|me]) (--body [yaw]) (--head [yaw]) (--pitch [pitch]) (-s(mooth))` | Rotate NPC |
| /npc rotationsettings | `[linear|immediate] (--link_body) (--head_only) (--max_pitch_per_tick) (--max_yaw_per_tick) (--pitch_range) (--yaw_range)` | Controls various head and body rotation settings for the NPC. Currently NPCs look using simple Minecraft-style rotation where the head/body move a certain amount of degrees per tick towards the target Accepts the following flags: **--link_body**: whether the head and body rotation should be linked directly **--head_only**: whether only the head should **--max_yaw_per_tick**: how many degrees to change yaw per tick (defaults to 40) **--max_pitch_per_tick**: how many degrees to change pitch per tick (defaults to 10) **--pitch_range**: the range of possible pitches to take (defaults to -180,180) **--yaw_range**: the range of possible yaws to take (defaults to -180,180) |
| /npc scaledmaxhealth | `[health]` | Controls the max health of an NPC, can use large numbers. |
| /npc select | `[id|name] (--range range) (--registry [name])` | Select a NPC with the given ID or name |
| /npc setequipment | `(-c(osmetic)) [slot] [item]` | Sets equipment via commands |
| /npc sheep | `(--color [color]) (--sheared [sheared])` | Sets sheep modifiers |
| /npc shop | `(edit|show|delete|copyfrom) (name) (new_name)` | NPC shop edit/show |
| /npc showshop | `(name)` | NPC shop show |
| /npc shulker | `(--peek [peek] --color [color])` | Sets shulker modifiers |
| /npc sitting | `(--explicit [true|false]) (--at [at])` | Sets the NPC sitting |
| /npc skin | `(-e(xport) -c(lear) -l(atest) -s(kull) -b(edrock)) [name] (or --url [url] --file [file] (-s(lim)) or -t [uuid/name] [data] [signature])` | Sets an NPC's skin name. Use -l to set the skin to always update to the latest |
| /npc skinlayers | `(--cape [true|false]) (--hat [true|false]) (--jacket [true|false]) (--sleeves [true|false]) (--pants [true|false])` | Sets an NPC's skin layers visibility |
| /npc slimesize | `[size]` | None |
| /npc sniffer | `(--state [state])` | Sets sniffer modifiers |
| /npc snowman | `(-d[erp]) (-f[orm snow])` | Sets snowman modifiers |
| /npc sound | `(--death [death sound|d]) (--ambient [ambient sound|d]) (--hurt [hurt sound|d]) (-n(one)/-s(ilent)) (-d(efault))` | Sets an NPC's played sounds |
| /npc spawn | `(id|name) -l(oad chunks)` | Spawn an existing NPC |
| /npc speak | `[message] --bubble [duration] --target [npcid|player name] --range (range to look for entities to speak to in blocks)` | Says a message from the NPC |
| /npc spectate | `(-r(eset))` | None |
| /npc speed | `[speed]` | Sets the movement speed of an NPC as a percentage |
| /npc spellcaster | `(--spell spell)` | Sets spellcaster modifiers |
| /npc swim | `(--set [true|false])` | Sets an NPC to swim or not |
| /npc target | `[name|UUID] (-a[ggressive]) (-c[ancel])` | Target a given entity |
| /npc targetable | `None` | Toggles an NPC's targetability |
| /npc text | `None` | Toggle the text editor |
| /npc textdisplay | `--shadowed [true|false] --seethrough [true|false] --line_width [width] --text [text]` | None |
| /npc tp | `(-e(xact))` | Teleport in front of an NPC |
| /npc tphere | `(cursor) -c(enter) -f(ront)` | Teleport a NPC to your location |
| /npc tpto | `[player name|npc id] [player name|npc id]` | Teleport an NPC or player to another NPC or player |
| /npc trackingrange | `[range]` | Sets the tracking range |
| /npc tropicalfish | `(--body color) (--pattern pattern) (--patterncolor color)` | Sets tropical fish modifiers |
| /npc type | `[type]` | Sets an NPC's entity type |
| /npc undo | `(all)` | Undoes the last action (currently only create/remove supported) |
| /npc useitem | `(-o(ffhand))` | Sets an NPC to be using their held items |
| /npc vex | `(--charging [charging])` | Set vex modifiers |
| /npc villager | `(--level level) (--type type) (--profession profession) -s(hake head)` | Sets villager modifiers |
| /npc vulnerable | `(-t(emporary))` | Toggles an NPC's vulnerability |
| /npc wander | `(add x y z world) | (worldguardregion [region]) | (xyrange [xrange] [yrange])` | Sets the NPC to wander around |
| /npc warden | `dig|emerge|roar|anger [entity uuid/player name] [anger]` | Sets warden modifiers |
| /npc wither | `(--invulnerable [true|false]) (--invulnerable-ticks [ticks]) (--arrow-shield [true|false])` | Sets wither modifiers |
| /npc wolf | `(-s(itting) a(ngry) t(amed) i(nterested)) --collar [hex rgb color|name] --variant [variant]` | Sets wolf modifiers |
| /trait | `[trait1] [trait2] ... [traitN]` - A list of [Traits](https://wiki.citizensnpcs.co/Characters "Characters") to apply | Adds the [trait type](https://wiki.citizensnpcs.co/Characters "Characters") to the NPC. NPCs can have multiple traits. Example:  `/trait sentinel` |

## Denizen-added commands

The following `/npc` commands are added by [Denizen](https://denizenscript.com/) (as copied from `/npc help`).
[Denizen can be downloaded from here.](https://guide.denizenscript.com/guides/background/download-denizen.html)

| **Denizen /NPC Commands** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Command | Arguments | Description |
| /npc mirrorskin | None | Makes the NPC mirror the skin of the player looking at it. |
| /npc mirrorname | None | Makes the NPC mirror the name of the player looking at it. |
| /npc mirrorequip | None | Makes the NPC mirror the equipment of the player looking at it. |
| /npc stand | None | Makes the NPC stand. |
| /npc pushable | *-t (-r) (--delay #)* | Makes an NPC pushable. |
| /npc constant | *--set/remove name --value constant value* | Views/adds/removes NPC string constants. |
| /npc assignment | *--set assignment_name (-r)* | Controls the assignment for an NPC. |
| /npc trigger | *[trigger name] [(--cooldown [seconds])/(--radius [radius])/(-t)]* | Controls the various triggers for an NPC. |
| /npc nickname | *[--set nickname]* | Gives the NPC a nickname, used with a Denizen-compatible Speech Engine. |
| /npc sit | *(--location x,y,z,world) (--anchor anchor_name) (-c)* | Makes the NPC sit. |
| /npc sleep | *(--location x,y,z,world) (--anchor anchor_name)* | Makes the NPC sleep. |
| /npc sneak | None | Makes the NPC crouch. |
| /npc wakeup | None | Makes the NPC wake up. |
| /npc fish | *(--location x,y,z,world) (--anchor anchor_name) (-c)* | Makes the NPC fish, casting at the given location. |
| /npc stopfishing | None | Makes the NPC stop fishing. |
| /npc invisible | None | Turns the NPC invisible. |
| /npc health | *--set # (-r)* | Sets the max health for an NPC. |

## Waypoint commands

Permissions are of the format "citizens.waypoints.xx", like "citizens.waypoints.disableteleport" for the "disableteleport" command.

| **Waypoint Commands** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Command | Arguments | Description |
| /waypoints add | `[x] [y] [z] (world) (--index idx)` | Adds a waypoint at a point |
| /waypoints disableteleport | `disableteleport` | Disables teleportation when stuck |
| /waypoints hpa | `hpa` | None |
| /waypoints provider | `[provider name]` | Sets the current waypoint provider |
| /waypoints remove | `(x y z world) (--index idx)` | Adds a waypoint at a point |

## Template commands

| **Template Commands** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Command | Arguments | Permission | Description |
| /template apply | `(template namespace:)[template name]` | citizens.templates.apply | Applies a template to the selected NPC |
| /template generate | `(template namespace:)[name]` | citizens.templates.generate | Generate a template from the selected NPC |
| /template list | `list` | citizens.templates.list | Lists available templates |

## See Also

[Characters](https://wiki.citizensnpcs.co/Characters "Characters")
  
[Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")
  
[Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · Commands  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
