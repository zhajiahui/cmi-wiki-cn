# Claiming { #claiming }

A rudimentary player-oriented claiming system is available for use in WorldGuard. It creates regions like `/rg define` would, but players must use a special command with separate permissions. WorldEdit selections are still required for selecting the physical area of the region, although only the `worldedit.selection` permission is necessary for that.

Player can claim selected regions using the `/rg claim` command:

```text
/rg claim region_name
```

The player running the command will automatically be added as a region owner. Access to the command is provided by the `worldguard.region.claim` permission.

## Rules { #rules }

- **Maximum region count:** Unless the player has the `worldguard.region.unlimited` permission, the player cannot exceed the maximum number of regions that is permitted in the [Configuration](https://worldguard.enginehub.org/en/latest/config/) for the player.

- **Maximum region volume:** Unless the player has the `worldguard.region.unlimited` permission, the volume of a claim must not exceed the `regions.max-claim-volume` configuration.

- **Overwrite prevention:** The region to be claimed cannot replace an existing one with the same name.

- **Overlap prevention:** The region to be claimed cannot overlap another region that the player is not an owner of.

- **Overlap only owned:** If `regions.claim-only-inside-existing-regions` is enabled, the region must overlap another region that the player is an owner of. Note that the region to be claimed does *not* need to be fully contained within another region (see [Issue #753](https://github.com/EngineHub/WorldGuard/issues/753)).

!!! note "Note"

    At this time, polygonal regions are not fully supported. See [Issue #1537](https://github.com/EngineHub/WorldGuard/issues/1537).

## Other Commands { #other-commands }

You can give players the ability to use other commands (like setting flags and adding members) by setting the appropriate [Permissions](https://worldguard.enginehub.org/en/latest/permissions/).
