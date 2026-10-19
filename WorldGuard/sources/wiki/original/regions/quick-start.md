# Quick Start { #quick-start }

## Selecting Areas { #selecting-areas }

To create a region, you need to tell WorldGuard the physical area. [WorldEdit](https://www.enginehub.org/worldedit) is used for this purpose.

New to WorldEdit?

You can read [WorldEdit’s quick start tutorial](https://worldedit.enginehub.org/en/latest/quickstart/) to learn how to select areas with WorldEdit.

Regions can take the shape of:

- Cuboids (i.e. a cube or a box)

- 2D polygons with heights

If you try to use an unsupported shape such as a cylinder, WorldGuard will inform you of this.

## Basic Commands { #basic-commands }

### Creating Regions { #creating-regions }

All regions must have a name, and names must be unique. Names are case-insensitive. Create a region with `/region define`:

```text
/region define town
```

Rather than using `/region`, you can also use `/rg` as a shortcut:

```text
/rg define town
```

The newly created region **automatically prevents building** within it. To let specific players build, add members or *owners* to the region. The main reason why you’d have separate owners or members is because you can set [permissions to use commands separately for owners and members](https://worldguard.enginehub.org/en/latest/permissions/).

Either players or permission groups can be a member or owner. To specify a permission group, prefix the name of the group with `g:`. The relevant add and remove commands are illustrated below:

```text
/rg addmember town wizjany sk89q g:builders
/rg addowner town sk89q
/rg removemember town g:builders
/rg removeowner town sk89q
```

Full documentation for these commands can be found on the [Region Commands](https://worldguard.enginehub.org/en/latest/regions/commands/) page.

Lastly, when you create a region, you can also conveniently specify the owners:

```text
/rg define town wizjany sk89q g:builders
```

!!! hint "Hint"

    Your changes to regions will automatically be saved after a small delay. However, region data can be force saved using `/rg save`. All saves are done in the background and will not pause the server.

Example: Creating a spawn region where only the build team can build

1. Select the area of spawn using WorldEdit.

2. Create a region named “spawn”:



   ```text
   /rg define spawn
   ```

3. Add the build team as a member:



   ```text
   /rg addmember spawn g:builders
   ```

### Other Commands { #other-commands }

You can remove regions:

```text
/rg remove town
```

You can list information about a region:

```text
/rg info town
```

You can view a list of regions:

```text
/rg list
```

You can change the shape or size of an existing region:

```text
/rg redefine town
```

For more commands, see the [region commands](https://worldguard.enginehub.org/en/latest/regions/commands/) page.

## Properties of Regions { #properties-of-regions }

### Handling Overlap { #handling-overlap }

Regions can overlap in WorldGuard, which provides a lot of flexibility but can be a source of complexity.

- When there are overlapping regions, a player must have permission to build in **all** overlapping regions.

- If you want a region to override another, use [priorities and region inheritance](https://worldguard.enginehub.org/en/latest/regions/priorities/).

- If you want a region to override all others in regards to whether players can build, use the `build` [region flag](https://worldguard.enginehub.org/en/latest/regions/flags/).

- If a region you made isn’t supposed to protect its area, use the `passthrough` [region flag](https://worldguard.enginehub.org/en/latest/regions/flags/).

Example: Creating a free-for-all mining zone that overlaps spawn

1. Select the area of mining zone.

2. Create a region named “mine”:



   ```text
   /rg define mine
   ```

3. Set the `build` flag to `allow`, which permits building for all players and overrides spawn because spawn doesn’t have the build flag explicitly set:



   ```text
   /rg flag mine build allow
   ```

!!! warning "Warning"

    The `build` flag has some additional properties and we generally recommend not to change it, unless you know what you are doing. See the [region flag overview](https://worldguard.enginehub.org/en/latest/regions/flags/) for more information.

### Flags { #flags }

Each region can have extra settings applied to it called flags. For example, PvP can be blocked using the “pvp” flag:

```text
/rg flag town pvp deny
```

Read the [Region Flags](https://worldguard.enginehub.org/en/latest/regions/flags/) guide for more information.

Example: Creating an arena at spawn where fighters can battle but cannot break blocks, while builders can still build within the arena

1. Select the area of arena.

2. Create a region named “arena”:



   ```text
   /rg define arena
   ```

3. Set the `pvp` flag to `allow`:



   ```text
   /rg flag arena pvp allow
   ```

4. Builders cannot build in the arena because they aren’t a member of the arena region, even if they are a member of the spawn region (if you have been following these examples). However, you created the arena region to set the PvP flag, not to protect the area, so set the `passthrough` flag to `allow` to make it transparent to build checks:



   ```text
   /rg flag arena passthrough allow
   ```

## Common Scenarios { #common-scenarios }

If you’re wondering how to do something (like allow the usage of doors, levers, pressure plates, etc.), check out the [Common Scenarios](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/) page.
