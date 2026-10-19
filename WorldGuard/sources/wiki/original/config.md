# Configuration { #configuration }

Many of WorldGuard’s features exist as configuration options (potion blocking, scuba mode with pumpkins, etc.). Every configuration option available is listed on this page.

## Configuration Files { #configuration-files }

Once you have run your server with WorldGuard installed, you will find the main configuration file inside the **plugins/WorldGuard** folder:

- `config.yml`

Then for every world, you will find per-world configuration files:

- `worlds/world/config.yml`

- `worlds/world_nether/config.yml`

- `worlds/mining_world/config.yml`

If you open up the per-world configuration files, they will be nearly empty. When you wish to override a setting, you would copy it into the world’s configuration file.

Example: Making a configuration option per-world

In the main configuration file, you may have set `block-creeper-block-damage` to true:

```text
mobs:
    block-creeper-explosions: false
    block-creeper-block-damage: true
    block-wither-explosions: false
```

But you want to set it to `false` in your nether world. Open up `worlds/world_nether/config.yml` and replace the file with:

```text
mobs:
    block-creeper-block-damage: false
```

Only the relevant line, as well as any parent sections, needs to be copied over.

## Settings { #settings }

!!! note "Note"

    These options are presented here as a reference, but you should change a desired option by first finding it in `config.yml` because some settings may need to be nested under another setting.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">op-permissions</td>
<td markdown="span">TRUE</td>
<td markdown="span">Whether players with op should be given all permissions for WorldGuard, even if the permissions plugin in use does not provide permission for ops.</td>
</tr>
<tr>
<td markdown="span">summary-on-start</td>
<td markdown="span">TRUE</td>
<td markdown="span">Show summary information about WG’s settings for each world on server start. This is pretty noisy and it should be disabled if you have many worlds.</td>
</tr>
<tr>
<td markdown="span">auto-invincible</td>
<td markdown="span">FALSE</td>
<td markdown="span">Give players with the `worldguard.auto-invincible` permission invincibility mode on join.</td>
</tr>
<tr>
<td markdown="span">auto-invincible-group</td>
<td markdown="span">FALSE</td>
<td markdown="span">Give players in the `wg-invincible` permission group invincibility mode on join.</td>
</tr>
<tr>
<td markdown="span">auto-no-drowning-group</td>
<td markdown="span">FALSE</td>
<td markdown="span">Give players in the `wg-amphibious` permission group water breathing mode on join.</td>
</tr>
<tr>
<td markdown="span">use-player-move-event</td>
<td markdown="span">TRUE</td>
<td markdown="span">Whether WorldGuard should use (a little) more CPU to handle features that require tracking player movement. This must be on to use healing, feeding, greeting, and some other [Region Flags](https://worldguard.enginehub.org/en/latest/regions/flags/).</td>
</tr>
<tr>
<td markdown="span">use-player-teleports</td>
<td markdown="span">TRUE</td>
<td markdown="span">Whether teleport events should be considered when tracking player movement. This should always be on if you are using the player move event and any of the flags that require that.</td>
</tr>
<tr>
<td markdown="span">use-particle-effects</td>
<td markdown="span">TRUE</td>
<td markdown="span">Whether WorldGuard should display particle effects when an action is cancelled.</td>
</tr>
<tr>
<td markdown="span">disable-permission-cache</td>
<td markdown="span">FALSE</td>
<td markdown="span">WorldGuard caches certain permission checks to improve performance with slower permission plugins. If you encounter issues with slow permission updates when using a modern permissions plugin, try setting this option to `TRUE`.</td>
</tr>
<tr>
<td markdown="span">custom-metrics-charts</td>
<td markdown="span">TRUE</td>
<td markdown="span">Reports some additional statistics to [bStats](https://bstats.org/plugin/bukkit/WorldGuard/3283).</td>
</tr>
<tr>
<td markdown="span">host-keys</td>
<td markdown="span"></td>
<td markdown="span">A list of hostnames that players must connect from. See [Host Keys](https://worldguard.enginehub.org/en/latest/host-keys/).</td>
</tr>
</tbody>
</table>

### security.* { #security }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">deop-everyone-on-join</td>
<td markdown="span">FALSE</td>
<td markdown="span">Clear op status from all players that join.</td>
</tr>
<tr>
<td markdown="span">block-in-game-op-command</td>
<td markdown="span">FALSE</td>
<td markdown="span">Block the /op command from being used in-game.</td>
</tr>
<tr>
<td markdown="span">host-keys-allow-forge-clients</td>
<td markdown="span">FALSE</td>
<td markdown="span">Allow players using Forge to join when using [Host Keys](https://worldguard.enginehub.org/en/latest/host-keys/).</td>
</tr>
</tbody>
</table>

### build-permission-nodes.* { #build-permission-nodes }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">enable</td>
<td markdown="span">FALSE</td>
<td markdown="span">A feature that lets you block building based on giving players the proper permissions. See [Build Permissions](https://worldguard.enginehub.org/en/latest/build-perms/).</td>
</tr>
<tr>
<td markdown="span">deny-message</td>
<td markdown="span">&eSorry, but you are not permitted to do that here.</td>
<td markdown="span">Concerning build permissions, this is the message that is sent when permission is denied. If a message is not set, a default one is used.</td>
</tr>
</tbody>
</table>

### event-handling.* { #event-handling }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">block-entity-spawns-with-untraceable-cause</td>
<td markdown="span">FALSE</td>
<td markdown="span">As Bukkit does not always tell plugins the exact reason that an entity was spawned, it may be possible for a player to bypass protection to spawn an entity (such as with a spawn egg). This option blocks cases where the true cause cannot be determined. It is recommended that this option is left off because the number of cases where the cause is not known is quite large.</td>
</tr>
<tr>
<td markdown="span">interaction-whitelist</td>
<td markdown="span">[]</td>
<td markdown="span">A list of block types that should not be protected. For example, if chests were added to this list, then they would never be protected with [region protection](https://worldguard.enginehub.org/en/latest/regions/). This setting is useful primarily when non-vanilla functionality is present (game features added by other plugins or mods) and you don’t want it blocked.</td>
</tr>
<tr>
<td markdown="span">emit-block-use-at-feet</td>
<td markdown="span">[]</td>
<td markdown="span">A list of items that, if used, will also require that the player have the permission to *theoretically* modify the block at his or her feet. This setting is useful primarily when there is some item from some plugin or mod that uses a projectile (that affects the world) but does not test permission with WorldGuard. However, this is not a proper solution because the player can still stand in an area where they have permission and shoot *into* the desired area.</td>
</tr>
<tr>
<td markdown="span">ignore-hopper-item-move-events</td>
<td markdown="span">FALSE</td>
<td markdown="span">Disable protections relating to hoppers moving items to and from containers. This can be set to true to slightly improve performance if your server has many hoppers, but be warned that it will allow hoppers outside regions to pull items from inside regions if they are close enough to the border.</td>
</tr>
<tr>
<td markdown="span">break-hoppers-on-denied-move</td>
<td markdown="span">TRUE</td>
<td markdown="span">If a hopper attempts to pull an item and is denied (as long as the previous config setting is false), WorldGuard will break the hopper block to prevent it from continuously attempting to pull items.</td>
</tr>
</tbody>
</table>

Example: Disabling protection on workbenches

The `interaction-whitelist` option can be used:

```text
interaction-whitelist: [workbench]
```

### protection.* { #protection }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">item-durability</td>
<td markdown="span">TRUE</td>
<td markdown="span">Set to `false` to have items never break.</td>
</tr>
<tr>
<td markdown="span">remove-infinite-stacks</td>
<td markdown="span">FALSE</td>
<td markdown="span">Remove items with ‘infinite’ stack sizes, which is essentially any stack size less than 0 (which is the result of a number overflowing the maximum and wrapping into the negatives).</td>
</tr>
<tr>
<td markdown="span">disable-xp-orb-drops</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether to disable XP orb drops.</td>
</tr>
<tr>
<td markdown="span">use-max-priority-association</td>
<td markdown="span">FALSE</td>
<td markdown="span">Wheter or not non-player associables, such as pistons, are only members of the regions with the highest priorities in which they are in. If set to `false`, non-player associables are members of all regions in which they are in, which means that pistons, for example, can push blocks from inside a region outwards into a surrounding region (unless there is only a protected [Global Region](https://worldguard.enginehub.org/en/latest/regions/global-region/) outside). If set to `true`, pistons, for example, cannot push blocks from inside a region outwards into a surrounding protected region with a lower priority.</td>
</tr>
</tbody>
</table>

### gameplay.* { #gameplay }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">block-potions</td>
<td markdown="span">[]</td>
<td markdown="span">A list of potion types that cannot be used. The list of possible potion types can be [found in Bukkit](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html).</td>
</tr>
<tr>
<td markdown="span">block-potions-overly-reliably</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether WorldGuard should try extra hard to block the list of potions mentioned in block-potions. This is generally not needed and enabling this may block more than you want.</td>
</tr>
<tr>
<td markdown="span">disable-conduit-effects</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether WorldGuard should disable effects from conduits.</td>
</tr>
</tbody>
</table>

Example: Blocking the use of night vision and speed potions

The names [found in Bukkit](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html) are used:

```text
block-potions: [night_vision, speed]
```

### simulation.sponge.* { #simulation-sponge }

!!! warning "Warning"

    These settings are not included in the config by default. This feature is deprecated and marked for removal in a future version.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">enable</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether to simulate sponge blocks similar to the way they worked in Minecraft Classic. Between the introduction of survival Minecraft and Minecraft 1.8 (several years), sponges did not work, but this setting is now obsolete and its use is no longer recommended.</td>
</tr>
<tr>
<td markdown="span">radius</td>
<td markdown="span">3</td>
<td markdown="span">The radius of the sponge’s action.</td>
</tr>
<tr>
<td markdown="span">redstone</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether Redstone can control the simulated Sponge blocks.</td>
</tr>
</tbody>
</table>

### default.* { #default }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">pumpkin-scuba</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether players with pumpkins (but not Jack o’ Lanterns) in their helmet slot will have water breathing.</td>
</tr>
<tr>
<td markdown="span">disable-health-regain</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether automatic health regeneration should be disabled.</td>
</tr>
</tbody>
</table>

### physics.* { #physics }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">no-physics-gravel</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether gravel should not fall.</td>
</tr>
<tr>
<td markdown="span">no-physics-sand</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether sand should not fall.</td>
</tr>
<tr>
<td markdown="span">vine-like-rope-ladders</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether ladders will work like vines in that they won’t break as long as the top most ladder block is in a valid location (it’s on a wall).</td>
</tr>
<tr>
<td markdown="span">allow-portal-anywhere</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether portal blocks can be placed in invalid locations.</td>
</tr>
<tr>
<td markdown="span">disable-water-damage-blocks</td>
<td markdown="span">[]</td>
<td markdown="span">A list of block types that will not be broken by water.</td>
</tr>
</tbody>
</table>

Example: Preventing Redstone and Redstone torches from being damanged by water

Material names are from [Bukkit’s Material list](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html):

```text
physics:
    disable-water-damage-blocks: [redstone_wire, redstone_torch]
```

### ignition.* { #ignition }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">block-tnt</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the detonation of TNT should be blocked.</td>
</tr>
<tr>
<td markdown="span">block-tnt-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether TNT should do no block damage.</td>
</tr>
<tr>
<td markdown="span">block-lighter</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the use of flint and steel should be disabled.</td>
</tr>
</tbody>
</table>

### fire.* { #fire }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">disable-lava-fire-spread</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether lava should be able to create fires.</td>
</tr>
<tr>
<td markdown="span">disable-all-fire-spread</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether fire can spread.</td>
</tr>
<tr>
<td markdown="span">disable-fire-spread-blocks</td>
<td markdown="span">[]</td>
<td markdown="span">A list of block types that fire cannot spread to, or at least damage.</td>
</tr>
<tr>
<td markdown="span">lava-spread-blocks</td>
<td markdown="span">[]</td>
<td markdown="span">If set (as a list of block types), the only blocks on which lava could flow on (other than air) would be the ones in the list.</td>
</tr>
</tbody>
</table>

### mobs.* { #mobs }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">block-creeper-explosions</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the effects of Creeper explosions should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-creeper-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether block damage caused by Creeper explosions should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-wither-explosions</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the effects of Wither explosions should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-wither-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether block damage caused by Wither explosions should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-wither-skull-explosions</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the effects of Wither skulls should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-wither-skull-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether block damage caused by Wither skulls should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-enderdragon-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether block damage caused by Enderdragons should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-enderdragon-portal-creation</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the ability of the Enderdragon to create a portal should be disabed.</td>
</tr>
<tr>
<td markdown="span">block-fireball-explosions</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the effects of fireball explosions should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-fireball-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether block damage caused by fireball block damage should be disabled.</td>
</tr>
<tr>
<td markdown="span">anti-wolf-dumbness</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the wolf should be invincible in a number of situations, including, but not limited to, walking into lava and getting stuck. When wolves were first introduced into the game, Minecraft had very poor path finding and so wolves would frequently walk into lava or fire. However, as the AI of helper mobs in Minecraft have still much to improve, this setting may still prove to be useful.</td>
</tr>
<tr>
<td markdown="span">allow-tamed-spawns</td>
<td markdown="span">TRUE</td>
<td markdown="span">Whether tamable mobs (wolves, horses, cats, etc.) should be spawnable.</td>
</tr>
<tr>
<td markdown="span">disable-enderman-griefing</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the ability of Endermen to pick up and place blocks should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-snowman-trails</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the feature of snowmen placing snow trails should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-painting-destroy</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the ability of mobs to break paintings should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-item-frame-destroy</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the ability of mobs to break item frames should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-armor-stand-destroy</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the ability of mobs to break armor stands should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-plugin-spawning</td>
<td markdown="span">TRUE</td>
<td markdown="span">Whether mobs spawned by plugins should be blocked when needed to apply some of these configuration options or to protect areas of the world.</td>
</tr>
<tr>
<td markdown="span">block-above-ground-slimes</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether slimes spawning above ground should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-other-explosions</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether miscellaneous explosions should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-zombie-door-destruction</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the ability for zombies to break doors should be disabled.</td>
</tr>
<tr>
<td markdown="span">block-vehicle-entry</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether mobs should be blocked from entering vehicles.</td>
</tr>
<tr>
<td markdown="span">block-creature-spawn</td>
<td markdown="span">[]</td>
<td markdown="span">A list of entity types that should not spawn.</td>
</tr>
</tbody>
</table>

### player-damage.* { #player-damage }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">disable-fall-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether fall damage should be disabled for players.</td>
</tr>
<tr>
<td markdown="span">disable-lava-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether lava damage should be disabled for players.</td>
</tr>
<tr>
<td markdown="span">disable-fire-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether fire damage should be disabled for players.</td>
</tr>
<tr>
<td markdown="span">disable-lightning-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether lightning damage should be disabled for players.</td>
</tr>
<tr>
<td markdown="span">disable-drowning-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether drowning damage should be disabled for players.</td>
</tr>
<tr>
<td markdown="span">disable-suffocation-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether suffocation damage should be disabled for players.</td>
</tr>
<tr>
<td markdown="span">disable-contact-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether contact damage (cacti, etc.) should be disabled for players.</td>
</tr>
<tr>
<td markdown="span">teleport-on-suffocation</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether players should be teleported to a safe location (if found, and which is usually up) when they are suffocating. This feature potentially allows players to cross vertical barriers.</td>
</tr>
<tr>
<td markdown="span">disable-void-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether void damage (falling into the bottom of the world) should be disabled for players.</td>
</tr>
<tr>
<td markdown="span">teleport-on-void-falling</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether players should be teleported to a safe location (if found) when they are falling into the void. This feature potentially allows players to enter areas that they normally may not be able to go.</td>
</tr>
<tr>
<td markdown="span">reset-fall-on-void-teleport</td>
<td markdown="span">FALSE</td>
<td markdown="span">Resets fall distance on void teleporting. Leaving this off will likely let the player die of fall damage (though their items will not be in the void, at least).</td>
</tr>
<tr>
<td markdown="span">disable-explosion-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether explosion damage should be disabled for players.</td>
</tr>
<tr>
<td markdown="span">disable-mob-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether damage from mobs should be disabled for players.</td>
</tr>
<tr>
<td markdown="span">disable-death-messages</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether death messages for players should be disabled.</td>
</tr>
</tbody>
</table>

### crops.* { #crops }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">disable-creature-trampling</td>
<td markdown="span">FALSE</td>
<td markdown="span">Disable the trampling of farmland by creatures.</td>
</tr>
<tr>
<td markdown="span">disable-player-trampling</td>
<td markdown="span">FALSE</td>
<td markdown="span">Disable the trampling of farmland by players.</td>
</tr>
</tbody>
</table>

### turtle-egg.* { #turtle-egg }

Same options as the crops section, but for turtle eggs.

### sniffer-egg.* { #sniffer-egg }

Same options as the crops section, but for sniffer eggs.

### weather.* { #weather }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">prevent-lightning-strike-blocks</td>
<td markdown="span">[]</td>
<td markdown="span">A list of block types where lightning should not be able to strike.</td>
</tr>
<tr>
<td markdown="span">disable-lightning-strike-fire</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether fire caused by lightning should be blocked.</td>
</tr>
<tr>
<td markdown="span">disable-thunderstorm</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether thunderstorms should never start.</td>
</tr>
<tr>
<td markdown="span">disable-weather</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether weather events (including thunderstorms) should never start.</td>
</tr>
<tr>
<td markdown="span">disable-pig-zombification</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the “zombification” of pigs when they are struck by lightning should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-villager-witchification</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the “witchification” of villagers when they are struck by lightning should be disabed.</td>
</tr>
<tr>
<td markdown="span">disable-powered-creepers</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the possibility of creepers becoming powered when they are struck by lightning should be disabled.</td>
</tr>
<tr>
<td markdown="span">always-raining</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether it should always be raining or snowing.</td>
</tr>
<tr>
<td markdown="span">always-thundering</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether it should always be thundering.</td>
</tr>
</tbody>
</table>

### dynamics.* { #dynamics }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">disable-mushroom-spread</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the spread of mushrooms should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-ice-melting</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the melting of ice should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-snow-melting</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the melting of snow should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-snow-formation</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the formation of snow should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-ice-formation</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the formation of ice should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-leaf-decay</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the decay of leaves should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-grass-growth</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the growth of grass should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-mycelium-spread</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the spread of mycelium should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-vine-growth</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the growth of vines and kelp should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-rock-growth</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the growth of rocks such as dripstones should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-sculk-growth</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the growth of sculk should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-crop-growth</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the growth of wheat, carrots, melons, etc should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-soil-dehydration</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the dehydration of soil should be disabled.</td>
</tr>
<tr>
<td markdown="span">disable-coral-block-fade</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether coral should remain alive when not in water.</td>
</tr>
<tr>
<td markdown="span">disable-copper-block-fade</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the oxidation of copper blocks should be disabled.</td>
</tr>
<tr>
<td markdown="span">snow-fall-blocks</td>
<td markdown="span">[]</td>
<td markdown="span">If set (as a list of block types), the only blocks on which snow can fall on would be the ones in the list.</td>
</tr>
</tbody>
</table>

### chest-protection.* { #chest-protection }

!!! warning "Warning"

    These settings are not included in the config by default. Sign-based chest protection is deprecated and marked for removal in a future version. See [Chest Protection](https://worldguard.enginehub.org/en/latest/chest-protection/) for details.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">enable</td>
<td markdown="span">FALSE</td>
<td markdown="span">Enables [Chest Protection](https://worldguard.enginehub.org/en/latest/chest-protection/).</td>
</tr>
<tr>
<td markdown="span">disable-off-check</td>
<td markdown="span">TRUE</td>
<td markdown="span">Even if chest protection is off, WorldGuard will block the creation of signs with `[Lock]` on them so that if chest protection is later enabled, players cannot have preemptively lock chests that they did not own to begin with. This option, if set to `true`, disables this check when chest protection is off.</td>
</tr>
</tbody>
</table>

### blacklist.* { #blacklist }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">use-as-whitelist</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether the purpose of the blacklist should be inverted, where the only things that can be done are the ones that are denied on the blacklist.</td>
</tr>
</tbody>
</table>

### blacklist.logging.* { #blacklist-logging }

These settings determine what the “log” action in the [Blacklist](https://worldguard.enginehub.org/en/latest/blacklist/) does. Several logging targets can be enabled simultaneously.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">console:</td>
<td markdown="span"></td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">enable</td>
<td markdown="span">TRUE</td>
<td markdown="span">Whether logging to the console should be enabled.</td>
</tr>
<tr>
<td markdown="span">database:</td>
<td markdown="span"></td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">enable</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether logging to a database should be enabled.</td>
</tr>
<tr>
<td markdown="span">dsn</td>
<td markdown="span">`jdbc:mysql://localhost:3306/minecraft`</td>
<td markdown="span">The connection string for the database. `minecraft` in the default is the name of the database.</td>
</tr>
<tr>
<td markdown="span">user</td>
<td markdown="span">root</td>
<td markdown="span">The username to connect to the database with.</td>
</tr>
<tr>
<td markdown="span">pass</td>
<td markdown="span"></td>
<td markdown="span">The password to connect to the database with.</td>
</tr>
<tr>
<td markdown="span">table</td>
<td markdown="span">blacklist_events</td>
<td markdown="span">The table to use.</td>
</tr>
<tr>
<td markdown="span">file:</td>
<td markdown="span"></td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">enable</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether logging to files should be enabled.</td>
</tr>
<tr>
<td markdown="span">path</td>
<td markdown="span">worldguard/logs/%Y-%m-%d.log</td>
<td markdown="span">The pattern for the log files.</td>
</tr>
<tr>
<td markdown="span">open-files</td>
<td markdown="span">10</td>
<td markdown="span">The maximum number of file handles to have open at once (file handles with the operating system).</td>
</tr>
</tbody>
</table>

### regions.* { #regions }

!!! hint "Hint"

    You cannot override `use-creature-spawn-event` per-world.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">wand</td>
<td markdown="span">minecraft:leather</td>
<td markdown="span">The ID of the item that is used to right click a block to inspect the regions affecting it. By default, this item is cow leather. Before, it was string but Minecraft added a use for string.</td>
</tr>
<tr>
<td markdown="span">disable-bypass-by-default</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether bypass permissions are disabled by default.</td>
</tr>
<tr>
<td markdown="span">announce-bypass-status</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether a hint for `/region bypass` should be displayed at login.</td>
</tr>
<tr>
<td markdown="span">invincibility-removes-mobs</td>
<td markdown="span">FALSE</td>
<td markdown="span">If enabled, if a player is attacked while they are invincible due to the invincibility [region flag](https://worldguard.enginehub.org/en/latest/regions/flags/), then the attacking mob is removed from the world.</td>
</tr>
<tr>
<td markdown="span">fake-player-build-override</td>
<td markdown="span">TRUE</td>
<td markdown="span">Whether players with a name that start with `[` and end with `]` should bypass all protection. This is only the case with third-party plugins and mods that use ‘fake players’ in lieu of firing the proper events.</td>
</tr>
<tr>
<td markdown="span">explosion-flags-block-entity-damage</td>
<td markdown="span">TRUE</td>
<td markdown="span">Whether the various `-explosion` [region flags](https://worldguard.enginehub.org/en/latest/regions/flags/) should also disable entity damage when enabled.</td>
</tr>
<tr>
<td markdown="span">high-frequency-flags</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether to handle frequently occurring events such as fire spread or fluid flow in regards to [region flags](https://worldguard.enginehub.org/en/latest/regions/flags/) (such as `fire-spread`, `water-flow`, and `lava-flow`). This is disabled by default because those mentioned flags are rarely used and this setting may result in a performance impact in certain scenarios (many, many players and many, many regions).</td>
</tr>
<tr>
<td markdown="span">protect-against-liquid-flow</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether fluid flows between regions should be blocked. This prevents one player from griefing another by having lava or water flow into the other player’s region. This setting must be enabled in tandem with `high-frequency-flags` for it to take effect.</td>
</tr>
<tr>
<td markdown="span">use-paper-entity-origin</td>
<td markdown="span">FALSE</td>
<td markdown="span">When on a [Paper server](https://papermc.io), this option will treat entities as members of the region where they spawned, not where they currently are. This will automatically prevent mobs that wander into regions from accidentally destroying it. (Note that this is separate from mobs that are targetting players in regions - that is still dependent on the player’s permission, not the mob’s.)</td>
</tr>
<tr>
<td markdown="span">max-claim-volume</td>
<td markdown="span">30000</td>
<td markdown="span">The maximum number of blocks in a region that can be claimed with [self-serve region claiming](https://worldguard.enginehub.org/en/latest/regions/claiming/).</td>
</tr>
<tr>
<td markdown="span">claim-only-inside-existing-regions</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether players can only claim within existing regions.</td>
</tr>
<tr>
<td markdown="span">cancel-chat-without-recipients</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether chat messages without recipients (for example when all online players are in regions where `receive-chat` is set to `deny`) should be cancelled. Turning this on may prevent external chat sinks (e.g. a Discord bridge plugin) from showing these messages.</td>
</tr>
<tr>
<td markdown="span">nether-portal-protection</td>
<td markdown="span">TRUE</td>
<td markdown="span">Whether any portal travel that might lead to portal creation in a protected area should be blocked.</td>
</tr>
<tr>
<td markdown="span">set-parent-on-claim</td>
<td markdown="span"></td>
<td markdown="span">A region ID that newly created regions with [self-serve region claiming](https://worldguard.enginehub.org/en/latest/regions/claiming/) automatically get assigned as [parent](https://worldguard.enginehub.org/en/latest/regions/priorities/#inheritance).</td>
</tr>
<tr>
<td markdown="span">location-flags-only-inside-regions</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether locations for location-type [Region Flags](https://worldguard.enginehub.org/en/latest/regions/flags/) have to be whithin the corresponding region.</td>
</tr>
<tr>
<td markdown="span">titles-always-use-default-times</td>
<td markdown="span">TRUE</td>
<td markdown="span">Set this to true if you use greeting/farewell titles and another plugin makes the titles disappear too quickly.</td>
</tr>
<tr>
<td markdown="span">max-region-count-per-player:</td>
<td markdown="span"></td>
<td markdown="span">The maximum number of regions that can be claimed by a player (via [self-serve region claiming](https://worldguard.enginehub.org/en/latest/regions/claiming/)). This setting can differ per permission-group if new entries are added below (like for ‘default’). ‘default’ is the default limit. If a player is a member of several groups that are listed, then the player receives the highest limit.</td>
</tr>
<tr>
<td markdown="span">default</td>
<td markdown="span">7</td>
<td markdown="span">(See above.)</td>
</tr>
</tbody>
</table>

Example: Setting different region count limits per group

Each permission group is given its own entry:

```text
max-region-count-per-player:
    default: 7
    builders: 20
    moderators: 40
```

!!! warning "Warning"

    There are also some additional settings in this category, but we do not recommend changing them:

    <table>
    <colgroup>
    </colgroup>
    <thead>
    <tr>
    <th markdown="span">Setting</th>
    <th markdown="span">Default</th>
    <th markdown="span">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td markdown="span">enable</td>
    <td markdown="span">TRUE</td>
    <td markdown="span">Whether support for defining regions should be enabled.</td>
    </tr>
    <tr>
    <td markdown="span">use-creature-spawn-event</td>
    <td markdown="span">TRUE</td>
    <td markdown="span">Whether the creature move event should be handled for applying some mob-related [region flags](https://worldguard.enginehub.org/en/latest/regions/flags/).</td>
    </tr>
    </tbody>
    </table>

### regions.uuid-migration.* { #regions-uuid-migration }

These settings are used to migrate from old versions of WorldGuard and Minecraft. In the past, Minecraft accounts were identified purely by their name, but around the end of Minecraft 1.7, Minecraft moved to a system where players were (internally) identified by “UUIDs” and players *could change their names*. However, all older configuration files still referred to players by their name, so the following settings enable the conversion to UUID on server start for one time (the setting is automatically disabled).

UUID migration can be run repeatedly (with repeated changing of the setting) and it will only convert names that have not yet been converted to UUIDs. If there are no names to convert, then nothing will happen.

!!! hint "Hint"

    You cannot override these settings per-world.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">perform-on-next-start</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether UUID migration should be performed on next server start (once). If the configuration file does not yet have this setting, WorldGuard will assume its value is `true`, perform the conversion, then set the setting to `false`.</td>
</tr>
<tr>
<td markdown="span">keep-names-that-lack-uuids</td>
<td markdown="span">TRUE</td>
<td markdown="span">Sometimes, a name that was added to a region does not actually exist. This option keeps names that can’t be converted in the region data so that they can later be removed or re-converted (by adjusting the settings in this section to re-run the conversion).</td>
</tr>
</tbody>
</table>

### regions.sql.* { #regions-sql }

!!! warning "Warning"

    These settings are not included in the config by default. SQL support for WorldGuard region storage is deprecated and marked for removal in a future version. Please migrate to YAML storage. See [Storage Drivers](https://worldguard.enginehub.org/en/latest/regions/storage/) for more information.

!!! hint "Hint"

    You cannot override these settings per-world.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Setting</th>
<th markdown="span">Default</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">use</td>
<td markdown="span">FALSE</td>
<td markdown="span">Whether MySQL should be used to store data (see [Storage Drivers](https://worldguard.enginehub.org/en/latest/regions/storage/)).</td>
</tr>
<tr>
<td markdown="span">dsn</td>
<td markdown="span">`jdbc:mysql://localhost/worldguard`</td>
<td markdown="span">The connection string for the database. `worldguard` in the default is the name of the database.</td>
</tr>
<tr>
<td markdown="span">username</td>
<td markdown="span">worldguard</td>
<td markdown="span">The username to connect to the database with.</td>
</tr>
<tr>
<td markdown="span">password</td>
<td markdown="span">worldguard</td>
<td markdown="span">The password to connect to the database with.</td>
</tr>
<tr>
<td markdown="span">table-prefix</td>
<td markdown="span"></td>
<td markdown="span">The table prefix.</td>
</tr>
</tbody>
</table>

## Subpages { #subpages }

- [Host Keys](https://worldguard.enginehub.org/en/latest/host-keys/)
