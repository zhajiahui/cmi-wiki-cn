# Configuration { #configuration }

Although WorldEdit is primarily command driven, there are some configuration options which may change or limit the behavior of WorldEdit’s commands and tools.

## Configuration Files { #configuration-files }

Once you have run your server with WorldEdit installed, you will find the main configuration file generated in a location which depends on your platform.

### Bukkit Server { #bukkit-server }

Configuration options for the Bukkit version of WorldEdit are found in `plugins/WorldEdit/config.yml`, relative to the server root.

Note that the YAML format which Bukkit uses is very sensitive to errors. You must use 4 spaces for indentation (tabs will break the file!), and adhere to YAML’s syntax. If you are unfamiliar with editing YAML files, you can run your config through an online validator (like [this one](https://yaml-online-parser.appspot.com/)) and ensure that it does not return an error.

### Forge/Fabric { #forge-fabric }

Configuration options in NeoForge/Fabric can be found in the `config/worldedit/worldedit.properties` file. On a server, this is relative to the server root (where the main server .jar is). On a single-player installation, this is in your “.minecraft” folder.

### Sponge Server { #sponge-server }

Configuration options in Sponge servers (either SpongeForge or SpongeVanilla) can be found in the `config/worldedit/worldedit.conf` file.

## Settings { #settings }

!!! note "Note"

    Since the underlying platforms are often in various states of development, not all settings will work on all platforms. Please [notify us](https://worldedit.enginehub.org/en/latest/support/) if you find this to be the case.

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
<td markdown="span">defaultLocale</td>
<td markdown="span">default</td>
<td markdown="span">The default locale to use for translations, defaults to the system locale.</td>
</tr>
<tr>
<td markdown="span">profile</td>
<td markdown="span">false</td>
<td markdown="span">Whether to print out a blocks changed/time info after each operation.</td>
</tr>
<tr>
<td markdown="span">traceUnflushedSessions</td>
<td markdown="span">false</td>
<td markdown="span">Display a debug message when an edit isn’t completed properly.</td>
</tr>
<tr>
<td markdown="span">disallowedBlocks</td>
<td markdown="span">&lt;list of blocks&gt;</td>
<td markdown="span">A list of blocks that cannot be used in patterns (mostly physics blocks that will “pop off” and may severely lag or crash the server if thousands of items are spawned).</td>
</tr>
<tr>
<td markdown="span">defaultChangeLimit</td>
<td markdown="span">-1</td>
<td markdown="span">The default amount of blocks that can be set in one operation.</td>
</tr>
<tr>
<td markdown="span">maxChangeLimit</td>
<td markdown="span">-1</td>
<td markdown="span">The maximum amount of blocks for the change limit (set with `//limit` in-game)</td>
</tr>
<tr>
<td markdown="span">defaultMaxPolygonalPoints</td>
<td markdown="span">-1</td>
<td markdown="span">The default amount of polygonal points that can be used (`//sel poly`), -1 means use maximum</td>
</tr>
<tr>
<td markdown="span">maxPolygonalPoints</td>
<td markdown="span">20</td>
<td markdown="span">The maximum amount of polygonal points that can be used (`//sel poly`, used if you have `worldedit.limit.unrestricted`)</td>
</tr>
<tr>
<td markdown="span">defaultMaxPolyhedronPoints</td>
<td markdown="span">-1</td>
<td markdown="span">The default amount of polyhedron points that can be used (`//sel convex`), -1 means use maximum</td>
</tr>
<tr>
<td markdown="span">maxPolyhedronPoints</td>
<td markdown="span">20</td>
<td markdown="span">The maximum amount of polyhedron points that can be used (`//sel convex`, used if you have `worldedit.limit.unrestricted`)</td>
</tr>
<tr>
<td markdown="span">snapshotRepo</td>
<td markdown="span"></td>
<td markdown="span">If not left empty, the directory name to look for snapshots</td>
</tr>
<tr>
<td markdown="span">snapshotsExperimental</td>
<td markdown="span">false</td>
<td markdown="span">If true, uses the new snapshot code. Try it out and report bugs!</td>
</tr>
<tr>
<td markdown="span">maxRadius</td>
<td markdown="span">-1</td>
<td markdown="span">Maximum radius of commands that take a radius</td>
</tr>
<tr>
<td markdown="span">maxSuperPickaxeSize</td>
<td markdown="span">5</td>
<td markdown="span">Maximum size of super pickaxe tools</td>
</tr>
<tr>
<td markdown="span">maxBrushRadius</td>
<td markdown="span">6</td>
<td markdown="span">Maximum size of brushes</td>
</tr>
<tr>
<td markdown="span">logCommands</td>
<td markdown="span">false</td>
<td markdown="span">Whether to log more informative information on command usage.</td>
</tr>
<tr>
<td markdown="span">logFile</td>
<td markdown="span"></td>
<td markdown="span">If logCommands is true, the file to log to.</td>
</tr>
<tr>
<td markdown="span">logFormat</td>
<td markdown="span">[%1$tY-%1$tm-%1$td %1$tH:%1$tM:%1$tS %4$s]: %5$s%6$s%n</td>
<td markdown="span">The format of command logging</td>
</tr>
<tr>
<td markdown="span">wandItem</td>
<td markdown="span">minecraft:wooden_axe</td>
<td markdown="span">The default item used for selection regions, overriden by existing sessions. Set to -1 for no default.</td>
</tr>
<tr>
<td markdown="span">superPickaxeDrop</td>
<td markdown="span">true</td>
<td markdown="span">Whether the single super pickaxe mode will drop items for blocks it breaks</td>
</tr>
<tr>
<td markdown="span">superPickaxeManyDrop</td>
<td markdown="span">true</td>
<td markdown="span">Whether multi super pickaxe modes will drop items for blocks they break</td>
</tr>
<tr>
<td markdown="span">useInventory</td>
<td markdown="span">false</td>
<td markdown="span">Require players to have items in their inventory to make edits (this option is not well supported and not recommended)</td>
</tr>
<tr>
<td markdown="span">useInventoryOverride</td>
<td markdown="span">false</td>
<td markdown="span">Allow a permission node to override the above setting</td>
</tr>
<tr>
<td markdown="span">useInventoryCreativeOverride</td>
<td markdown="span">false</td>
<td markdown="span">Allow creative mode to override the above setting</td>
</tr>
<tr>
<td markdown="span">navigationUseGlass</td>
<td markdown="span">true</td>
<td markdown="span">Whether the `/up` and `/ceil` commands should place a glass block for the player to stand on if in mid-air</td>
</tr>
<tr>
<td markdown="span">navigationWand</td>
<td markdown="span">minecraft:compass</td>
<td markdown="span">The default item used for the navigation wand which allows `/jumpto` and `/thru` as left-click/right-click, overriden by existing sessions. Set to -1 for no default.</td>
</tr>
<tr>
<td markdown="span">navigationWandMaxDistance</td>
<td markdown="span">50</td>
<td markdown="span">The max distance the navigation wand should trace to find a block to jump to</td>
</tr>
<tr>
<td markdown="span">scriptTimeout</td>
<td markdown="span">3000</td>
<td markdown="span">The maximum time a craftscript can run before it is terminated</td>
</tr>
<tr>
<td markdown="span">calculationTimeout</td>
<td markdown="span">100</td>
<td markdown="span">The default time an expression can run before it is terminated</td>
</tr>
<tr>
<td markdown="span">maxCalculationTimeout</td>
<td markdown="span">300</td>
<td markdown="span">The maximum time an expression can run before termination (changed in game with `//timeout`)</td>
</tr>
<tr>
<td markdown="span">allowedDataCycleBlocks</td>
<td markdown="span"></td>
<td markdown="span">If not empty, a whitelist of blocks which the data cycler tool can be used on</td>
</tr>
<tr>
<td markdown="span">saveDir</td>
<td markdown="span">schematics</td>
<td markdown="span">The directory in which to save schematics (relative to the worldedit folder)</td>
</tr>
<tr>
<td markdown="span">scriptsDir</td>
<td markdown="span">craftscripts</td>
<td markdown="span">The directory in which to look for craftscripts</td>
</tr>
<tr>
<td markdown="span">allowSymlinks</td>
<td markdown="span">false</td>
<td markdown="span">Whether to allow the above to be symlinked locations (useful for sharing between servers)</td>
</tr>
<tr>
<td markdown="span">butcherDefaultRadius</td>
<td markdown="span">-1</td>
<td markdown="span">The default radius of the `/butcher` command (-1 for infinite)</td>
</tr>
<tr>
<td markdown="span">butcherMaxRadius</td>
<td markdown="span">-1</td>
<td markdown="span">The maximum radius of the `/butcher` command</td>
</tr>
<tr>
<td markdown="span">serverSideCUI</td>
<td markdown="span">true</td>
<td markdown="span">Whether to allow the usage of `//drawsel`</td>
</tr>
<tr>
<td markdown="span">defaultVerticalHeight</td>
<td markdown="span">256</td>
<td markdown="span">The height to use for commands that take an optional height.</td>
</tr>
<tr>
<td markdown="span">extendedYLimit</td>
<td markdown="span">false</td>
<td markdown="span">If true, use slower but unbounded positions. This should only be needed with a mod that extends the height limit.</td>
</tr>
</tbody>
</table>
