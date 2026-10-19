# Region Flags { #region-flags }

Regions can have flags set upon it. Some uses of flags include:

- Blocking player versus player combat with the `pvp` flag

- Denying entry to a region using the `entry` flag

- Disabling the melting of snow using the `snow-melt` flag

- Blocking players within the region from receiving chat using the `receive-chat` flag

- Halting the growth of vines by using the `vine-growth` flag

A region can have several different flags set at one time, although a certain flag can only have one value at a time. Flags are defined using the `/region flag` (alternatively `/rg flag`) command, as illustrated below for the “spawn” region and “hospital” regions:

```text
/region flag spawn pvp deny
/region flag spawn greeting Welcome to spawn!
/rg flag hospital heal-amount 2
/rg flag hospital heal-delay 1
```

Remove a flag by not specifying a value:

```text
/rg flag spawn pvp
```

List flags by using the “flags” command:

```text
/rg flags spawn
```

The output of this command is interactive in-game. Click flag values to change them, and the arrows at the bottom to navigate through pages.

<a id="contents"></a>

- [Region Groups](https://worldguard.enginehub.org/en/latest/regions/flags/#region-groups)

- [Types of Flags](https://worldguard.enginehub.org/en/latest/regions/flags/#types-of-flags)

- [Conflicting Flags](https://worldguard.enginehub.org/en/latest/regions/flags/#conflicting-flags)

- [Default Values of Flags](https://worldguard.enginehub.org/en/latest/regions/flags/#default-values-of-flags)

- [Flag Listing](https://worldguard.enginehub.org/en/latest/regions/flags/#flag-listing)



  - [Overrides](https://worldguard.enginehub.org/en/latest/regions/flags/#overrides)

  - [Protection-Related](https://worldguard.enginehub.org/en/latest/regions/flags/#protection-related)

  - [Mobs, Fire, and Explosions](https://worldguard.enginehub.org/en/latest/regions/flags/#mobs-fire-and-explosions)

  - [Natural Events](https://worldguard.enginehub.org/en/latest/regions/flags/#natural-events)

  - [Movement](https://worldguard.enginehub.org/en/latest/regions/flags/#movement)

  - [Map Making](https://worldguard.enginehub.org/en/latest/regions/flags/#map-making)

  - [Miscellaneous](https://worldguard.enginehub.org/en/latest/regions/flags/#miscellaneous)

<a id="id1"></a>

## Region Groups { #region-groups }

Sometimes, it may be desired for a flag to only apply to a certain group of players rather than everyone that should enter the region. This can be achieved by specifying an additional “region group” when defining the flag.

Region groups describe the (non-)membership of players to a region. They are handled by WorldGuard internally, and are entirely unrelated to permission groups.

The following region groups exist:

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Region Group</th>
<th markdown="span">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">all</td>
<td markdown="span">Everyone</td>
</tr>
<tr>
<td markdown="span">members</td>
<td markdown="span">Members and owners of the region</td>
</tr>
<tr>
<td markdown="span">owners</td>
<td markdown="span">Owners of the region</td>
</tr>
<tr>
<td markdown="span">nonmembers</td>
<td markdown="span">Everyone who isn’t an owner or member of the region</td>
</tr>
<tr>
<td markdown="span">nonowners</td>
<td markdown="span">Everyone who isn’t an owner of the region</td>
</tr>
</tbody>
</table>

The group can be specified using the `-g` marker as illustrated below:

```text
/region flag spawn -g nonmembers pvp deny
```

It is **not** possible to set the same flag to different values for more than one group on the same region. If you need that functionality, consider making several regions.

!!! note "Note"

    When there are multiple overlapping regions, a player must be a member of the region *on which the flag is set* or *on one of the region’s child regions* (when region inheritance is involved). This is explained further in [Priority and Inheritance](https://worldguard.enginehub.org/en/latest/regions/priorities/).

!!! tip "Tip"

    The `entry` and `exit` flags default to “non-member”, meaning setting them to “deny” will prevent non-members from entering/exiting the region. The `spawn` location flag defaults to “members”, which means that only members can take advantage of it by default. The `nonplayer-protection-domains` flag has no region group. All other flags provided by WorldGuard default to “everyone”.

## Types of Flags { #types-of-flags }

Each flag is of a certain type that determines what kind of values it may take. For example, the `heal-amount` flag is an integer flag, so you can only set integer values for it.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Type</th>
<th markdown="span">Kind of values</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">state</td>
<td markdown="span">Either ‘allow’ or ‘deny’ (explained later)</td>
</tr>
<tr>
<td markdown="span">string</td>
<td markdown="span">Any form of text</td>
</tr>
<tr>
<td markdown="span">integer</td>
<td markdown="span">A number that does not have decimals (5, but not 5.5)</td>
</tr>
<tr>
<td markdown="span">double</td>
<td markdown="span">Numbers that may have decimals (5, 5.5, 2.425)</td>
</tr>
<tr>
<td markdown="span">location</td>
<td markdown="span">A location in a world</td>
</tr>
<tr>
<td markdown="span">boolean</td>
<td markdown="span">True or false</td>
</tr>
<tr>
<td markdown="span">set</td>
<td markdown="span">A list of unique entries</td>
</tr>
</tbody>
</table>

Internally, there are more types, but it should generally not be of concern.

!!! tip "Tip"

    Most string flags will accept `\n` as a newline (for example, to send multiple lines via `greeting`/`farewell`, or a title and subtitle via `greeting-title` and `farewell-title`).

    They may also accept color codes, either in the old style `&[0-9a-f]` or <code>&#96;[RrYyGgCcBbPp012w]</code> for dark-red, red, dark yellow, yellow, etc., and <code>[&amp;&#96;][klmnox]</code> for obfuscated, bold, strikethrough, underline, and italic text.

    They may also accept some replacements, such as `%name%` for the player’s name, `%world%` for world name, `%online%` for player count, `%id%` for the player’s UUID, and `%health%` for the player’s current health.

Example: Using string formatting options

Setting spawn’s `greeting-title` to a fancy welcome message:

```text
/rg flag spawn greeting-title `bWelcome to spawn!\n`YEnjoy your stay in `g`n%world%`x, `C%name%`Y!
```

## Conflicting Flags { #conflicting-flags }

Sometimes, a certain location may have multiple overlapping regions with different values for the same flag. The following rules are used to determine which values are selected:

- Regions will inherit the value of a flag from its parent, **if** the region did not have the flag set. (Note that the `build` flag is set implicitly with membership.)

- Higher priority regions will override lower-priority regions.

- The global region is considered like any other region, except it is at the lowest possible priority.

However, it is still possible for there to be conflicting flag values even after that process. Imagine two different regions at the same priority, for example. At that point, the value of the flag is decided differently depending on the type of flag:

- For state flags, if `deny` is present, the result is `deny`. Otherwise, if `allow` is present, then the final value is `allow`.

- For other flags, the result is not defined. For that reason, do not, for example, set two different greeting messages in the same area with the same priority.

## Default Values of Flags { #default-values-of-flags }

Flags can have default values, which are used if a flag is not set for the subject’s region group on any region that affects the action. The default behavior is whichever is most sensible. For example, if `item-pickup` is not defined, WorldGuard defaults to allowing it. You can view the default values ingame by using the “flags” command as already described above. State flags can either be allowed by default, or have no default value. A rule of thumb is that protection-related flags, as listed below, have no default value, except for the `build` flag. All other state flags are usually allowed by default. The `build` flag is special. Its default value depends on the region membership of the subject and it’s always set implicitely, if it’s not set explicitely on any highest priority region that affects an action. That’s the reason why members and owners can build and non-members can’t by default. All other protection-related flags are always checked in tandem with the build flag. Thus their default behavior is the resulting value of the build flag.

!!! tip "Tip"

    Most of the time you don’t need to set any flags. You should only set flags if you want to deviate from the default values or to overwrite set flags of other regions. Specifically don’t set protection-related flags to completely protect or unprotect a region. Use membership or the `passthrough` flag instead.

## Flag Listing { #flag-listing }

Flags are broken down into categories below.

<a id="flag-overrides"></a>

### Overrides { #overrides }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Flag</th>
<th markdown="span">Type</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">passthrough</td>
<td markdown="span">state</td>
<td markdown="block">

<p markdown="span">This flag is short for ‘passthrough build’. It has nothing to do with movement.</p> <ul markdown="block"> <li markdown="span"><p markdown="span">If not set **(default)**, then the region protects it area.</p> </li> <li markdown="span"><p markdown="span">If set to `deny`, then the region protects its area.</p> </li> <li markdown="span"><p markdown="span">If set to `allow`, then the region **no longer** protects its area.</p> </li> </ul> <p markdown="span">Where does the flag come into use?</p> <ul markdown="block"> <li markdown="span"><p markdown="span">When you are using other flags (PvP, healing, etc.) and you don’t want to prevent building.</p> </li> <li markdown="span"><p markdown="span">Why not set `build` to `allow` (explained later) instead? That would override other regions and let people build!</p> </li> </ul>

</td>
</tr>
<tr>
<td markdown="span">nonplayer-protection-domains</td>
<td markdown="span">set of strings</td>
<td markdown="block">

<p markdown="span">Non-player associables, such as pistons, are usually members of either all regions in which they are in or only of the regions with the highest priorities in which they are in, depending on the `use-max-priority-association` [Configuration](https://worldguard.enginehub.org/en/latest/config/) setting and if it is a [Global Region](https://worldguard.enginehub.org/en/latest/regions/global-region/). Thus there can be borders between regions, such that pistons cannot move blocks from one region into another region.</p> <p markdown="span">The borders between the regions can be removed for non-player associables by setting the `nonplayer-protection-domains` flags of these regions. This flag is a set of strings, describing the domains to which the region belongs. If a non-player associable is a member of a region, then it is also a member of another region, if there is at least one domain to which both regions belong to.</p>

</td>
</tr>
</tbody>
</table>

### Protection-Related { #protection-related }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Flag</th>
<th markdown="span">Type</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">build</td>
<td markdown="span">state</td>
<td markdown="block">

<p markdown="span">Everything:</p> <ul markdown="block"> <li markdown="span"><p markdown="span">Whether blocks can be mined or placed</p> </li> <li markdown="span"><p markdown="span">Whether doors, levers, etc. (but not inventories) can be used</p> </li> <li markdown="span"><p markdown="span">Whether entities and blocks can be interacted with</p> </li> <li markdown="span"><p markdown="span">Whether player versus player combat is permitted</p> </li> <li markdown="span"><p markdown="span">Whether sleeping in a bed is permitted</p> </li> <li markdown="span"><p markdown="span">Whether inventories can be accessed</p> </li> <li markdown="span"><p markdown="span">Whether vehicles (boats, minecarts) can be placed</p> </li> <li markdown="span"><p markdown="span">etc.</p> </li> </ul>

</td>
</tr>
<tr>
<td markdown="span">interact</td>
<td markdown="span">state</td>
<td markdown="block">

<p markdown="span">Everything that involves ‘using’ a block or entity:</p> <ul markdown="block"> <li markdown="span"><p markdown="span">Whether doors, levers, etc. (but not inventories) can be used</p> </li> <li markdown="span"><p markdown="span">Whether vehicles (including animals) can be mounted</p> </li> <li markdown="span"><p markdown="span">etc.</p> </li> </ul>

</td>
</tr>
<tr>
<td markdown="span">block-break</td>
<td markdown="span">state</td>
<td markdown="span">Whether blocks can be broken</td>
</tr>
<tr>
<td markdown="span">block-place</td>
<td markdown="span">state</td>
<td markdown="span">Whether blocks can be placed</td>
</tr>
<tr>
<td markdown="span">use</td>
<td markdown="span">state</td>
<td markdown="span">Whether doors, levers, etc. (but not inventories) can be used</td>
</tr>
<tr>
<td markdown="span">damage-animals</td>
<td markdown="span">state</td>
<td markdown="span">Whether players can harm friendly animals (cows, sheep, etc)</td>
</tr>
<tr>
<td markdown="span">chest-access</td>
<td markdown="span">state</td>
<td markdown="span">Whether inventories can be accessed</td>
</tr>
<tr>
<td markdown="span">ride</td>
<td markdown="span">state</td>
<td markdown="span">Whether vehicles (including animals) can be mounted</td>
</tr>
<tr>
<td markdown="span">pvp</td>
<td markdown="span">state</td>
<td markdown="span">Whether player versus player combat is permitted</td>
</tr>
<tr>
<td markdown="span">sleep</td>
<td markdown="span">state</td>
<td markdown="span">Whether sleeping in a bed is permitted</td>
</tr>
<tr>
<td markdown="span">respawn-anchors</td>
<td markdown="span">state</td>
<td markdown="span">Whether respawn anchors can be activated</td>
</tr>
<tr>
<td markdown="span">tnt</td>
<td markdown="span">state</td>
<td markdown="span">Whether TNT detonation or block damage is permitted</td>
</tr>
<tr>
<td markdown="span">vehicle-place</td>
<td markdown="span">state</td>
<td markdown="span">Whether vehicles (boats, minecarts) can be placed</td>
</tr>
<tr>
<td markdown="span">vehicle-destroy</td>
<td markdown="span">state</td>
<td markdown="span">Whether vehicles can be destroyed</td>
</tr>
<tr>
<td markdown="span">lighter</td>
<td markdown="span">state</td>
<td markdown="span">Whether flint and steel or a fire charge can be used</td>
</tr>
<tr>
<td markdown="span">block-trampling</td>
<td markdown="span">state</td>
<td markdown="span">Whether farmland and turtle or sniffer eggs can be trampled</td>
</tr>
<tr>
<td markdown="span">frosted-ice-form</td>
<td markdown="span">state</td>
<td markdown="span">Whether players with frost walker boots will form ice</td>
</tr>
<tr>
<td markdown="span">item-frame-rotation</td>
<td markdown="span">state</td>
<td markdown="span">Whether items can be rotated within item frames</td>
</tr>
<tr>
<td markdown="span">firework-damage</td>
<td markdown="span">state</td>
<td markdown="span">Whether fireworks can deal damage to entities</td>
</tr>
<tr>
<td markdown="span">use-anvil</td>
<td markdown="span">state</td>
<td markdown="span">Whether anvils can be used</td>
</tr>
<tr>
<td markdown="span">use-dripleaf</td>
<td markdown="span">state</td>
<td markdown="span">Whether dripleaf can be used</td>
</tr>
</tbody>
</table>

!!! warning "Warning"

    None of these flags are player-specific. For example, the `block-break` flag, if set to deny, **prevents pistons from breaking blocks**.

    To understand why, consider the fact that players can fling TNT into a region from outside, or a player can build an inchworm piston machine that moves into another region. While these actions were caused by a player, realistically attempting to figure which player built the TNT cannon or used it is much more difficult. However, you still want to prevent someone from blowing up spawn with a TNT cannon.

    Outright blocking TNT cannons or pistons is the wrong solution. Pistons and TNT cannons should be allowed in *some* cases. For example, a TNT cannon or piston inside should work *within* the region.

    First off, remember who can build in regions: it’s **not** players, it’s **members**. When we consider pistons or TNT, it should be no different. How does WorldGuard figure out whether a piston machine or TNT cannon is a member of a region? **If it’s inside the region,** of course!

    When you create a region, before setting any flags on it:

    - Members may build

    - Non-members may **not** build

    TNT cannons and pistons inside are allowed to work because they are “members.” An imaginary player, “Bobby,” who isn’t a member yet, is unable to place or break blocks. Once you add Bobby to the region, then Bobby can build.

    When you set the protection flags, you override this behavior. If you set `block-break` to `deny`, then even members are unable to break blocks. Bobby cannot break blocks. A TNT cannon inside cannot break blocks. A piston inside cannot break blocks. **You break pistons.**

    That raises two questions:

    - **How do I prevent players from placing or breaking blocks?** Don’t do anything. Don’t change any flags! Remember, only members can build by default.

    - **How do I change a flag to only affect players?** You probably mean: how do you make a flag only affect *non-members*? Well, that’s easy: use [Region Groups](https://worldguard.enginehub.org/en/latest/regions/flags/#region-groups).

!!! tip "Tip"

    Note: If the `build` flag is set to `allow` or `deny`, it can still be overriden with a different flag (`block-break`, `interact`, etc.). The `build` flag is set implicitly with membership.

### Mobs, Fire, and Explosions { #mobs-fire-and-explosions }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Flag</th>
<th markdown="span">Type</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">creeper-explosion</td>
<td markdown="span">state</td>
<td markdown="span">Whether creeper explosions can do damage</td>
</tr>
<tr>
<td markdown="span">enderdragon-block-damage</td>
<td markdown="span">state</td>
<td markdown="span">Whether enderdragons can do block damage (destroy blocks)</td>
</tr>
<tr>
<td markdown="span">ghast-fireball</td>
<td markdown="span">state</td>
<td markdown="span">Whether ghast fireballs and wither skulls can do damage</td>
</tr>
<tr>
<td markdown="span">other-explosion</td>
<td markdown="span">state</td>
<td markdown="span">Whether explosions can do damage</td>
</tr>
<tr>
<td markdown="span">fire-spread</td>
<td markdown="span">state</td>
<td markdown="span">Whether fire can spread</td>
</tr>
<tr>
<td markdown="span">enderman-grief</td>
<td markdown="span">state</td>
<td markdown="span">Whether endermen will break/place blocks</td>
</tr>
<tr>
<td markdown="span">snowman-trails</td>
<td markdown="span">state</td>
<td markdown="span">Whether snow golem will create snow beneath them</td>
</tr>
<tr>
<td markdown="span">ravager-grief</td>
<td markdown="span">state</td>
<td markdown="span">Whether ravagers will break blocks</td>
</tr>
<tr>
<td markdown="span">mob-damage</td>
<td markdown="span">state</td>
<td markdown="span">Whether mobs can hurt players</td>
</tr>
<tr>
<td markdown="span">mob-spawning</td>
<td markdown="span">state</td>
<td markdown="span">Whether mobs can spawn, including ‘manually’ spawning via commands, spawn eggs, or similar methods</td>
</tr>
<tr>
<td markdown="span">deny-spawn</td>
<td markdown="span">set of entity types</td>
<td markdown="span">A list of entity types that cannot spawn, including ‘manually’ spawning via commands, spawn eggs, or similar methods</td>
</tr>
<tr>
<td markdown="span">entity-painting-destroy</td>
<td markdown="span">state</td>
<td markdown="span">Whether non-player entities can destroy paintings</td>
</tr>
<tr>
<td markdown="span">entity-item-frame-destroy</td>
<td markdown="span">state</td>
<td markdown="span">Whether non-player entities can destroy item frames</td>
</tr>
<tr>
<td markdown="span">wither-damage</td>
<td markdown="span">state</td>
<td markdown="span">Whether withers can do damage (with their body explosions - skull projectiles are handled by ghast-fireball as mentioned above)</td>
</tr>
</tbody>
</table>

Example: Preventing sheep and cows from spawning at spawn

The entity types must be specified:

```text
/rg flag spawn deny-spawn cow,pig
```

### Natural Events { #natural-events }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Flag</th>
<th markdown="span">Type</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">lava-fire</td>
<td markdown="span">state</td>
<td markdown="span">Whether lava can start fires</td>
</tr>
<tr>
<td markdown="span">lightning</td>
<td markdown="span">state</td>
<td markdown="span">Whether lightning can strike</td>
</tr>
<tr>
<td markdown="span">water-flow</td>
<td markdown="span">state</td>
<td markdown="span">Whether water can flow</td>
</tr>
<tr>
<td markdown="span">lava-flow</td>
<td markdown="span">state</td>
<td markdown="span">Whether lava can flow</td>
</tr>
<tr>
<td markdown="span">snow-fall</td>
<td markdown="span">state</td>
<td markdown="span">Whether snow will form tiles on the ground</td>
</tr>
<tr>
<td markdown="span">snow-melt</td>
<td markdown="span">state</td>
<td markdown="span">Whether snow will melt</td>
</tr>
<tr>
<td markdown="span">ice-form</td>
<td markdown="span">state</td>
<td markdown="span">Whether ice will form</td>
</tr>
<tr>
<td markdown="span">ice-melt</td>
<td markdown="span">state</td>
<td markdown="span">Whether ice will melt</td>
</tr>
<tr>
<td markdown="span">frosted-ice-melt</td>
<td markdown="span">state</td>
<td markdown="span">Whether frosted ice will melt</td>
</tr>
<tr>
<td markdown="span">mushroom-growth</td>
<td markdown="span">state</td>
<td markdown="span">Whether mushrooms will grow</td>
</tr>
<tr>
<td markdown="span">leaf-decay</td>
<td markdown="span">state</td>
<td markdown="span">Whether leaves will decay</td>
</tr>
<tr>
<td markdown="span">grass-growth</td>
<td markdown="span">state</td>
<td markdown="span">Whether grass will grow</td>
</tr>
<tr>
<td markdown="span">mycelium-spread</td>
<td markdown="span">state</td>
<td markdown="span">Whether mycelium will spread</td>
</tr>
<tr>
<td markdown="span">vine-growth</td>
<td markdown="span">state</td>
<td markdown="span">Whether vines (and kelp) will grow</td>
</tr>
<tr>
<td markdown="span">rock-growth</td>
<td markdown="span">state</td>
<td markdown="span">Whether rocks (dripstone, etc) will grow</td>
</tr>
<tr>
<td markdown="span">sculk-growth</td>
<td markdown="span">state</td>
<td markdown="span">Whether sculk (sculk and sculk vines) will grow</td>
</tr>
<tr>
<td markdown="span">crop-growth</td>
<td markdown="span">state</td>
<td markdown="span">Whether crops (wheat, potatoes, melons, etc) will grow</td>
</tr>
<tr>
<td markdown="span">soil-dry</td>
<td markdown="span">state</td>
<td markdown="span">Whether soil will dry</td>
</tr>
<tr>
<td markdown="span">coral-fade</td>
<td markdown="span">state</td>
<td markdown="span">Whether coral will die when not in water</td>
</tr>
<tr>
<td markdown="span">copper-fade</td>
<td markdown="span">state</td>
<td markdown="span">Whether copper will fade</td>
</tr>
</tbody>
</table>

!!! warning "Warning"

    The `fire-spread`, `water-flow`, `lava-flow` and `lava-fire` flags require that the “high frequency flags” option be enabled in the [configuration](https://worldguard.enginehub.org/en/latest/config/). This is because these events can be very frequent, requiring more region lookups, and potentially slowing down your server (or at least warming the server room a bit more).

### Movement { #movement }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Flag</th>
<th markdown="span">Type</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">entry</td>
<td markdown="span">state</td>
<td markdown="span">Whether players (by default non-members) can enter the region</td>
</tr>
<tr>
<td markdown="span">exit</td>
<td markdown="span">state</td>
<td markdown="span">Whether players (by default non-members) can exit the region</td>
</tr>
<tr>
<td markdown="span">exit-via-teleport</td>
<td markdown="span">state</td>
<td markdown="block">

<p markdown="span">Whether players can exit the region via teleport.</p> <p markdown="span">This only takes effect if the player is otherwise denied exiting the region</p>

</td>
</tr>
<tr>
<td markdown="span">exit-override</td>
<td markdown="span">boolean</td>
<td markdown="span">Whether to always allow a player to exit</td>
</tr>
<tr>
<td markdown="span">entry-deny-message</td>
<td markdown="span">string</td>
<td markdown="span">The message issued to players that are denied entry</td>
</tr>
<tr>
<td markdown="span">exit-deny-message</td>
<td markdown="span">string</td>
<td markdown="span">The message issued to players that are denied exit</td>
</tr>
<tr>
<td markdown="span">notify-enter</td>
<td markdown="span">boolean</td>
<td markdown="span">Whether players with the `worldguard.notify` permission are notified when another player enters the region</td>
</tr>
<tr>
<td markdown="span">notify-leave</td>
<td markdown="span">boolean</td>
<td markdown="span">Whether players with the `worldguard.notify` permission are notified when another player leaves the region</td>
</tr>
<tr>
<td markdown="span">greeting</td>
<td markdown="span">string</td>
<td markdown="span">The message that appears in chat upon entering the region</td>
</tr>
<tr>
<td markdown="span">greeting-title</td>
<td markdown="span">string</td>
<td markdown="span">The title that appears upon entering the region. Including a newline (`\n`) will send a subtitle.</td>
</tr>
<tr>
<td markdown="span">farewell</td>
<td markdown="span">string</td>
<td markdown="span">The message that appears in chat upon leaving the region</td>
</tr>
<tr>
<td markdown="span">farewell-title</td>
<td markdown="span">string</td>
<td markdown="span">The title that appears upon leaving the region. Including a newline (`\n`) will send a subtitle.</td>
</tr>
<tr>
<td markdown="span">enderpearl</td>
<td markdown="span">state</td>
<td markdown="span">Whether enderpearls can be used</td>
</tr>
<tr>
<td markdown="span">chorus-fruit-teleport</td>
<td markdown="span">state</td>
<td markdown="span">Whether chorus fruits can be used to teleport</td>
</tr>
<tr>
<td markdown="span">teleport</td>
<td markdown="span">location</td>
<td markdown="span">The location to teleport to when the `/region teleport` command is used with the region name</td>
</tr>
<tr>
<td markdown="span">spawn</td>
<td markdown="span">location</td>
<td markdown="span">The location to spawn or teleport to when a player (by default member) dies within the region</td>
</tr>
<tr>
<td markdown="span">teleport-message</td>
<td markdown="span">string</td>
<td markdown="span">The message issued to players that are teleported with `/region teleport`</td>
</tr>
</tbody>
</table>

!!! tip "Tip"

    As mentioned above, the `spawn` location flag defaults to “members”, which means that only members can take advantage of it by default. Set the region group for the flag to change this.

!!! tip "Tip"

    If overlapping regions have the same `greeting` or `farewell` flag, no message is sent when moving between these regions, e.g. if you enter one region while being in the other. This is also true, in a more general sense, of any player movement that does *not* result in the flag at the “from” and “to” locations changing.

!!! warning "Warning"

    The `greeting` and `farewell` message flags require that the “use player move event” option **not** be disabled in the [configuration](https://worldguard.enginehub.org/en/latest/config/).

Example: Preventing non-members of a “secret_club” region from entering it

Since entry defaults to “nonmembers”, you don’t need to explicitly set it here:

```text
/rg flag secret_club entry deny
```

### Map Making { #map-making }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Flag</th>
<th markdown="span">Type</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">item-pickup</td>
<td markdown="span">state</td>
<td markdown="span">Whether items can be picked up</td>
</tr>
<tr>
<td markdown="span">item-drop</td>
<td markdown="span">state</td>
<td markdown="span">Whether items can be dropped</td>
</tr>
<tr>
<td markdown="span">exp-drops</td>
<td markdown="span">state</td>
<td markdown="span">Whether XP drops are permitted</td>
</tr>
<tr>
<td markdown="span">deny-message</td>
<td markdown="span">string</td>
<td markdown="span">The message issued to players that are denied an action</td>
</tr>
<tr>
<td markdown="span">invincible</td>
<td markdown="span">state</td>
<td markdown="span">Whether players are invincible</td>
</tr>
<tr>
<td markdown="span">fall-damage</td>
<td markdown="span">state</td>
<td markdown="span">Whether entities receive fall damage</td>
</tr>
<tr>
<td markdown="span">game-mode</td>
<td markdown="span">gamemode</td>
<td markdown="span">The gamemode (survival, creative, adventure) that will be applied to players that enter the region</td>
</tr>
<tr>
<td markdown="span">time-lock</td>
<td markdown="span">string</td>
<td markdown="span">Time of day in ticks (between 0 and 24000) that players will see the world as while in the region. Use + or - for time relative to the world time.</td>
</tr>
<tr>
<td markdown="span">weather-lock</td>
<td markdown="span">weather</td>
<td markdown="span">Type of weather players will see when in the region. This does not affect world mechanics. Valid values are `rain` and `clear`.</td>
</tr>
<tr>
<td markdown="span">natural-health-regen</td>
<td markdown="span">state</td>
<td markdown="span">Whether players should naturally regen health from being satiated or being in peaceful mode.</td>
</tr>
<tr>
<td markdown="span">natural-hunger-drain</td>
<td markdown="span">state</td>
<td markdown="span">Whether players should naturally lose hunger due to saturation/exhaustion levels.</td>
</tr>
<tr>
<td markdown="span">heal-delay</td>
<td markdown="span">integer</td>
<td markdown="span">The number of seconds between heals (if `heal-amount` is set). Set to 0 to disable.</td>
</tr>
<tr>
<td markdown="span">heal-amount</td>
<td markdown="span">integer</td>
<td markdown="span">The amount of half hearts to heal (or hurt if negative) the player at the rate of `heal-delay`</td>
</tr>
<tr>
<td markdown="span">heal-min-health</td>
<td markdown="span">double</td>
<td markdown="span">The minimum number of half hearts that damage (via `heal-amount`) will not exceed</td>
</tr>
<tr>
<td markdown="span">heal-max-health</td>
<td markdown="span">double</td>
<td markdown="span">The maximum number of half hearts that healing (via `heal-amount`) will not exceed</td>
</tr>
<tr>
<td markdown="span">feed-delay</td>
<td markdown="span">integer</td>
<td markdown="span">See equivalent heal flag, except this is for food</td>
</tr>
<tr>
<td markdown="span">feed-amount</td>
<td markdown="span">integer</td>
<td markdown="span">See equivalent heal flag, except this is for food</td>
</tr>
<tr>
<td markdown="span">feed-min-hunger</td>
<td markdown="span">integer</td>
<td markdown="span">See equivalent heal flag, except this is for food</td>
</tr>
<tr>
<td markdown="span">feed-max-hunger</td>
<td markdown="span">integer</td>
<td markdown="span">See equivalent heal flag, except this is for food</td>
</tr>
<tr>
<td markdown="span">blocked-cmds</td>
<td markdown="span">set of strings</td>
<td markdown="span">A list of commands to block</td>
</tr>
<tr>
<td markdown="span">allowed-cmds</td>
<td markdown="span">set of strings</td>
<td markdown="span">A list of commands to whitelist (any unallowed commands will be blocked)</td>
</tr>
</tbody>
</table>

!!! warning "Warning"

    The healing and feeding flags require that the “use player move event” option **not** be disabled in the [configuration](https://worldguard.enginehub.org/en/latest/config/).

Example: Changing the message players receive when an action they try is blocked

Set the `deny-message` flag:

```text
/rg flag spawn deny-message Sorry! You are at spawn. If you want to find a place to call home, use the rail station to leave spawn.
```

Example: Blocking the “/tp” and “/teleport” commands at spawn

The commands in question can be blocked with:

```text
/rg flag spawn blocked-cmds /tp,/teleport
```

Example: In a “hospital” region, heal players one heart every second up to half their health bar

Without any buffs, the player’s maximum health is 20, so 10 is half of that:

```text
/rg flag hospital heal-delay 1
/rg flag hospital heal-amount 2
/rg flag hospital heal-max-health 10
```

### Miscellaneous { #miscellaneous }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Flag</th>
<th markdown="span">Type</th>
<th markdown="span">description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">pistons</td>
<td markdown="span">state</td>
<td markdown="span">Whether pistons can be used</td>
</tr>
<tr>
<td markdown="span">send-chat</td>
<td markdown="span">state</td>
<td markdown="span">Whether players can send chat</td>
</tr>
<tr>
<td markdown="span">receive-chat</td>
<td markdown="span">state</td>
<td markdown="span">Whether players can receive chat</td>
</tr>
<tr>
<td markdown="span">potion-splash</td>
<td markdown="span">state</td>
<td markdown="span">Whether potions can have splash effects</td>
</tr>
</tbody>
</table>

!!! note "Note"

    WorldGuard can only limit chat or commands on the server WorldGuard is running on. If you are using some sort of proxy that handles commands or the chat, WorldGuard won’t be able to affect that.
