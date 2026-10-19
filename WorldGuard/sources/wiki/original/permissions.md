# Permissions { #permissions }

By default, no one can use WorldGuard. In order for yourself, moderators, and players to use WorldGuard, you must provide the proper permissions. One way is to provide op to moderators and administrators (unless disabled in the [configuration](https://worldguard.enginehub.org/en/latest/config/)), but providing the permission nodes on this page (through a permissions plugin) is the more flexible.

You can give the `worldguard.*` permission to give yourself and other administrators full access to WorldGuard.

## Moderator { #moderator }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Permission</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">worldguard.notify</td>
<td markdown="span">Receive notification with the ‘notify’ blacklist action and the ‘notify’ [region flags](https://worldguard.enginehub.org/en/latest/regions/flags/).</td>
</tr>
<tr>
<td markdown="span">worldguard.region.bypass.&lt;world&gt;</td>
<td markdown="span">Bypass region protection for a given world, except for PvP deny flags.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.toggle-bypass</td>
<td markdown="span">Allows using the `/rg bypass` command to toggle the above behavior (still requires the bypass permission).</td>
</tr>
<tr>
<td markdown="span">worldguard.chest-protection.override</td>
<td markdown="span">Bypass [Chest Protection](https://worldguard.enginehub.org/en/latest/chest-protection/) and open protected chests.</td>
</tr>
<tr>
<td markdown="span">worldguard.god.override-regions</td>
<td markdown="span">Allows keeping invincibility when inside regions with `invincibility` set to `DENY`.</td>
</tr>
<tr>
<td markdown="span">worldguard.auto-invincible</td>
<td markdown="span">Automatically receive invincibility when joininng if the config option `auto-invincible` is enabled.</td>
</tr>
<tr>
<td markdown="span">worldguard.override.potions</td>
<td markdown="span">Allows using potions/effects that are blocked with the `blocked-potions` config option.</td>
</tr>
<tr>
<td markdown="span">worldguard.override.lighter</td>
<td markdown="span">Allows using flint and steel or fireballs when `ignition.block-lighter` is enabled in the config.</td>
</tr>
<tr>
<td markdown="span">worldguard.override.infinite-stack</td>
<td markdown="span">Bypasses the `protection.remove-infinite-stacks` config option.</td>
</tr>
</tbody>
</table>

!!! warning "Warning"

    If you are op or have all permissions, you will implicitly have these protection bypass permissions and it will appear that protection does not work.

## Commands { #commands }

See the [Commands](https://worldguard.enginehub.org/en/latest/commands/) page for an explanation of some of these commands.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Permission</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">worldguard.god</td>
<td markdown="span">Be able to use `/god` (and `/ungod`).</td>
</tr>
<tr>
<td markdown="span">worldguard.god.other</td>
<td markdown="span">Be able to use `/god` (and `/ungod`) on others.</td>
</tr>
<tr>
<td markdown="span">worldguard.heal</td>
<td markdown="span">Be able to use `/heal`.</td>
</tr>
<tr>
<td markdown="span">worldguard.heal.other</td>
<td markdown="span">Be able to use `/heal` on others.</td>
</tr>
<tr>
<td markdown="span">worldguard.slay</td>
<td markdown="span">Be able to use `/slay`.</td>
</tr>
<tr>
<td markdown="span">worldguard.slay.other</td>
<td markdown="span">Be able to use `/slay` on others.</td>
</tr>
<tr>
<td markdown="span">worldguard.locate</td>
<td markdown="span">Be able to use `/locate`.</td>
</tr>
<tr>
<td markdown="span">worldguard.stack</td>
<td markdown="span">Be able to use `/stack`.</td>
</tr>
<tr>
<td markdown="span">worldguard.stack.illegitimate</td>
<td markdown="span">Be able to make stack sizes with `/stack` that exceed normal limits (i.e. 64 buckets in one stack).</td>
</tr>
<tr>
<td markdown="span">worldguard.fire-toggle.stop</td>
<td markdown="span">Be able to use `/stopfire` and `/allowfire`.</td>
</tr>
<tr>
<td markdown="span">worldguard.halt-activity</td>
<td markdown="span">Be able to use `/stoplag`.</td>
</tr>
<tr>
<td markdown="span">worldguard.reload</td>
<td markdown="span">Be able to use `/wg reload`.</td>
</tr>
<tr>
<td markdown="span">worldguard.report</td>
<td markdown="span">Be able to use `/wg report`.</td>
</tr>
<tr>
<td markdown="span">worldguard.profile</td>
<td markdown="span">Be able to use `/wg profile`.</td>
</tr>
<tr>
<td markdown="span">worldguard.report.pastebin</td>
<td markdown="span">Be able to have a report or profile submitted to a pastebin service.</td>
</tr>
<tr>
<td markdown="span">worldguard.flushstates</td>
<td markdown="span">Be able to use `/wg flushstates`.</td>
</tr>
<tr>
<td markdown="span">worldguard.running</td>
<td markdown="span">Be able to use `/wg running`.</td>
</tr>
<tr>
<td markdown="span">worldguard.debug.event</td>
<td markdown="span">Be able to use the event testing commands under `/wg debug`. Those commands are used to simulate an action so you can trace down, for example, which plugin is blocking player versus player combat. However, this essentially allows a moderator to impersonate another player.</td>
</tr>
</tbody>
</table>

## Regions { #regions }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Permission</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">worldguard.region.wand</td>
<td markdown="span">Be able to use the [Region Wand](https://worldguard.enginehub.org/en/latest/regions/wand/).</td>
</tr>
<tr>
<td markdown="span">worldguard.region.load</td>
<td markdown="span">Be able to use `/rg load`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.save</td>
<td markdown="span">Be able to use `/rg save`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.migratedb</td>
<td markdown="span">Be able to use `/rg migratedb`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.migrateuuid</td>
<td markdown="span">Be able to use `/rg migrateuuid`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.migrateheights</td>
<td markdown="span">Be able to use `/rg migrateheights`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.define</td>
<td markdown="span">Be able to use `/rg define`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.claim</td>
<td markdown="span">Be able to use `/rg claim`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.unlimited</td>
<td markdown="span">Bypass claiming limits.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.list</td>
<td markdown="span">Be able to use `/rg list`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.list.own</td>
<td markdown="span">Be able to use `/rg list` and have it show one own’s regions.</td>
</tr>
</tbody>
</table>

### Per-Region Permissions { #per-region-permissions }

The following permissions support a base permission (such as `worldguard.region.redefine`), but also allow you to use specific permissions that only apply if a player is an owner or member of a region (note that an owner is also a member):

- `worldguard.region.redefine.own.<region name>`

- `worldguard.region.redefine.member.<region name>`

- `worldguard.region.redefine.<region name>`

Permissions systems that support wildcard permissions can be used to grant permissions to all regions in any given category, e.g.:

- `worldguard.region.redefine.own.*`

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Permission</th>
<th markdown="span">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">worldguard.region.redefine.*</td>
<td markdown="span">Be able to use `/rg redefine`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.remove.*</td>
<td markdown="span">Be able to use `/rg remove`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.setpriority.*</td>
<td markdown="span">Be able to use `/rg setpriority`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.setparent.*</td>
<td markdown="span">Be able to use `/rg setparent`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.select.*</td>
<td markdown="span">Be able to use `/rg select`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.info.*</td>
<td markdown="span">Be able to use `/rg info` and `/rg flags`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.teleport.*</td>
<td markdown="span">Be able to use `/rg teleport`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.teleportcenter.*</td>
<td markdown="span">Be able to use `/rg teleport -c` when in spectator mode.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.addmember.*</td>
<td markdown="span">Be able to use `/rg addmember`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.addowner.*</td>
<td markdown="span">Be able to use `/rg addowner`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.removemember.*</td>
<td markdown="span">Be able to use `/rg removemember`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.removeowner.*</td>
<td markdown="span">Be able to use `/rg removeowner`.</td>
</tr>
<tr>
<td markdown="span">worldguard.region.locationoverride.*</td>
<td markdown="span">Bypasses the `regions.location-flags-only-inside-regions` config option.</td>
</tr>
</tbody>
</table>

Example: Letting players look up information on only regions that they own

Use the own.* form of the permission:

```text
worldguard.region.info.own.*
```

Example: Allowing every player to use `/rg teleport city`

The region name can be specified in the permission:

```text
worldguard.region.teleport.city.*
```

### Flag Command { #flag-command }

The `/rg flag` command has the basic permission:

```text
worldguard.region.flag.*
```

However, rather than providing that encompassing permission, you can provide the combination of the following two:

- To determine *which regions* can have their flag changed by the player, any of the following permissions can be given (and they work like the permissions in the previous section):

  `worldguard.region.flag.regions.own.<region name>` `worldguard.region.flag.regions.member.<region name>` `worldguard.region.flag.regions.<region name>`

- However, to determine *which types of flags* can be set by the player, permissions of the following patterns can be given:

  `worldguard.region.flag.flags.<flag name>.<flag value>.own.<region name>` `worldguard.region.flag.flags.<flag name>.<flag value>.member.<region name>` `worldguard.region.flag.flags.<flag name>.<flag value>.<region name>`

  Examples for `<flag value>` are `allow`, `deny`, `unset` (if no value is specified), etc. More complex values are also checked, however, special characters such as `,`, `.`, whitespaces, etc. are omitted.

Example: Letting players be able to only change flags on regions that they own, and limit the flags that they can change to `use` and `chest-access`

You would need to provide the following permissions:

```text
worldguard.region.flag.regions.own.*
worldguard.region.flag.flags.use.*
worldguard.region.flag.flags.chest-access.*
```

## Subpages { #subpages }

- [Build Permissions](https://worldguard.enginehub.org/en/latest/build-perms/)
