# Permissions { #permissions }

By default, no one can use WorldEdit. In order for yourself, moderators, and players to use WorldEdit, you must provide the proper permissions. One way is to provide op to moderators and administrators (unless disabled in the [configuration](https://worldedit.enginehub.org/en/latest/config/)), but providing the permission nodes on this page (through a permissions plugin) is the more flexible.

You can give the `worldedit.*` permission to give yourself and other administrators full access to WorldEdit.

## Commands { #commands }

See the [Commands](https://worldedit.enginehub.org/en/latest/commands/) page for an explanation of some of these commands.

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Command</th>
<th markdown="span">Permission</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">`/worldedit`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/worldedit cui`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/worldedit help`</td>
<td markdown="span">`worldedit.help`</td>
</tr>
<tr>
<td markdown="span">`/worldedit reload`</td>
<td markdown="span">`worldedit.reload`</td>
</tr>
<tr>
<td markdown="span">`/worldedit report`</td>
<td markdown="span">`worldedit.report`</td>
</tr>
<tr>
<td markdown="span">`/worldedit trace`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/worldedit tz`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/worldedit version`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/undo`</td>
<td markdown="span">`worldedit.history.undo`, `worldedit.history.undo.self`</td>
</tr>
<tr>
<td markdown="span">`/redo`</td>
<td markdown="span">`worldedit.history.redo`, `worldedit.history.redo.self`</td>
</tr>
<tr>
<td markdown="span">`/clearhistory`</td>
<td markdown="span">`worldedit.history.clear`</td>
</tr>
<tr>
<td markdown="span">`//limit`</td>
<td markdown="span">`worldedit.limit`</td>
</tr>
<tr>
<td markdown="span">`//timeout`</td>
<td markdown="span">`worldedit.timeout`</td>
</tr>
<tr>
<td markdown="span">`//fast`</td>
<td markdown="span">`worldedit.fast`</td>
</tr>
<tr>
<td markdown="span">`//perf`</td>
<td markdown="span">`worldedit.perf`</td>
</tr>
<tr>
<td markdown="span">`//reorder`</td>
<td markdown="span">`worldedit.reorder`</td>
</tr>
<tr>
<td markdown="span">`//drawsel`</td>
<td markdown="span">`worldedit.drawsel`</td>
</tr>
<tr>
<td markdown="span">`//world`</td>
<td markdown="span">`worldedit.world`</td>
</tr>
<tr>
<td markdown="span">`//watchdog`</td>
<td markdown="span">`worldedit.watchdog`</td>
</tr>
<tr>
<td markdown="span">`/gmask`</td>
<td markdown="span">`worldedit.global-mask`</td>
</tr>
<tr>
<td markdown="span">`/toggleplace`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/placement`</td>
<td markdown="span">`worldedit.placement`</td>
</tr>
<tr>
<td markdown="span">`/searchitem`</td>
<td markdown="span">`worldedit.searchitem`</td>
</tr>
<tr>
<td markdown="span">`//registry`</td>
<td markdown="span">`worldedit.registry`</td>
</tr>
<tr>
<td markdown="span">`/unstuck`</td>
<td markdown="span">`worldedit.navigation.unstuck`</td>
</tr>
<tr>
<td markdown="span">`/ascend`</td>
<td markdown="span">`worldedit.navigation.ascend`</td>
</tr>
<tr>
<td markdown="span">`/descend`</td>
<td markdown="span">`worldedit.navigation.descend`</td>
</tr>
<tr>
<td markdown="span">`/ceil`</td>
<td markdown="span">`worldedit.navigation.ceiling`</td>
</tr>
<tr>
<td markdown="span">`/thru`</td>
<td markdown="span">`worldedit.navigation.thru.command`</td>
</tr>
<tr>
<td markdown="span">`/jumpto`</td>
<td markdown="span">`worldedit.navigation.jumpto.command`</td>
</tr>
<tr>
<td markdown="span">`/up`</td>
<td markdown="span">`worldedit.navigation.up`</td>
</tr>
<tr>
<td markdown="span">`//pos`</td>
<td markdown="span">`worldedit.selection.pos`</td>
</tr>
<tr>
<td markdown="span">`//pos1`</td>
<td markdown="span">`worldedit.selection.pos`</td>
</tr>
<tr>
<td markdown="span">`//pos2`</td>
<td markdown="span">`worldedit.selection.pos`</td>
</tr>
<tr>
<td markdown="span">`//hpos1`</td>
<td markdown="span">`worldedit.selection.hpos`</td>
</tr>
<tr>
<td markdown="span">`//hpos2`</td>
<td markdown="span">`worldedit.selection.hpos`</td>
</tr>
<tr>
<td markdown="span">`//chunk`</td>
<td markdown="span">`worldedit.selection.chunk`</td>
</tr>
<tr>
<td markdown="span">`//wand`</td>
<td markdown="span">`worldedit.wand`</td>
</tr>
<tr>
<td markdown="span">`/toggleeditwand`</td>
<td markdown="span">`worldedit.wand.toggle`</td>
</tr>
<tr>
<td markdown="span">`//contract`</td>
<td markdown="span">`worldedit.selection.contract`</td>
</tr>
<tr>
<td markdown="span">`//shift`</td>
<td markdown="span">`worldedit.selection.shift`</td>
</tr>
<tr>
<td markdown="span">`//outset`</td>
<td markdown="span">`worldedit.selection.outset`</td>
</tr>
<tr>
<td markdown="span">`//inset`</td>
<td markdown="span">`worldedit.selection.inset`</td>
</tr>
<tr>
<td markdown="span">`//trim`</td>
<td markdown="span">`worldedit.selection.trim`</td>
</tr>
<tr>
<td markdown="span">`//size`</td>
<td markdown="span">`worldedit.selection.size`</td>
</tr>
<tr>
<td markdown="span">`//count`</td>
<td markdown="span">`worldedit.analysis.count`</td>
</tr>
<tr>
<td markdown="span">`//distr`</td>
<td markdown="span">`worldedit.analysis.distr`</td>
</tr>
<tr>
<td markdown="span">`//sel`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`//expand`</td>
<td markdown="span">`worldedit.selection.expand`</td>
</tr>
<tr>
<td markdown="span">`//expand vert`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`//set`</td>
<td markdown="span">`worldedit.region.set`</td>
</tr>
<tr>
<td markdown="span">`//line`</td>
<td markdown="span">`worldedit.region.line`</td>
</tr>
<tr>
<td markdown="span">`//curve`</td>
<td markdown="span">`worldedit.region.curve`</td>
</tr>
<tr>
<td markdown="span">`//replace`</td>
<td markdown="span">`worldedit.region.replace`</td>
</tr>
<tr>
<td markdown="span">`//overlay`</td>
<td markdown="span">`worldedit.region.overlay`</td>
</tr>
<tr>
<td markdown="span">`//center`</td>
<td markdown="span">`worldedit.region.center`</td>
</tr>
<tr>
<td markdown="span">`//naturalize`</td>
<td markdown="span">`worldedit.region.naturalize`</td>
</tr>
<tr>
<td markdown="span">`//walls`</td>
<td markdown="span">`worldedit.region.walls`</td>
</tr>
<tr>
<td markdown="span">`//faces`</td>
<td markdown="span">`worldedit.region.faces`</td>
</tr>
<tr>
<td markdown="span">`//smooth`</td>
<td markdown="span">`worldedit.region.smooth`</td>
</tr>
<tr>
<td markdown="span">`//snowsmooth`</td>
<td markdown="span">`worldedit.region.snowsmooth`</td>
</tr>
<tr>
<td markdown="span">`//move`</td>
<td markdown="span">`worldedit.region.move`</td>
</tr>
<tr>
<td markdown="span">`//stack`</td>
<td markdown="span">`worldedit.region.stack`</td>
</tr>
<tr>
<td markdown="span">`//regen`</td>
<td markdown="span">`worldedit.regen`</td>
</tr>
<tr>
<td markdown="span">`//deform`</td>
<td markdown="span">`worldedit.region.deform`</td>
</tr>
<tr>
<td markdown="span">`//hollow`</td>
<td markdown="span">`worldedit.region.hollow`</td>
</tr>
<tr>
<td markdown="span">`//forest`</td>
<td markdown="span">`worldedit.region.forest`</td>
</tr>
<tr>
<td markdown="span">`//flora`</td>
<td markdown="span">`worldedit.region.flora`</td>
</tr>
<tr>
<td markdown="span">`//update`</td>
<td markdown="span">`worldedit.update`</td>
</tr>
<tr>
<td markdown="span">`//hcyl`</td>
<td markdown="span">`worldedit.generation.cylinder`</td>
</tr>
<tr>
<td markdown="span">`//cyl`</td>
<td markdown="span">`worldedit.generation.cylinder`</td>
</tr>
<tr>
<td markdown="span">`//cone`</td>
<td markdown="span">`worldedit.generation.cone`</td>
</tr>
<tr>
<td markdown="span">`//hsphere`</td>
<td markdown="span">`worldedit.generation.sphere`</td>
</tr>
<tr>
<td markdown="span">`//sphere`</td>
<td markdown="span">`worldedit.generation.sphere`</td>
</tr>
<tr>
<td markdown="span">`/forestgen`</td>
<td markdown="span">`worldedit.generation.forest`</td>
</tr>
<tr>
<td markdown="span">`/pumpkins`</td>
<td markdown="span">`worldedit.generation.pumpkins`</td>
</tr>
<tr>
<td markdown="span">`//feature`</td>
<td markdown="span">`worldedit.generation.feature`</td>
</tr>
<tr>
<td markdown="span">`//structure`</td>
<td markdown="span">`worldedit.generation.structure`</td>
</tr>
<tr>
<td markdown="span">`//hpyramid`</td>
<td markdown="span">`worldedit.generation.pyramid`</td>
</tr>
<tr>
<td markdown="span">`//pyramid`</td>
<td markdown="span">`worldedit.generation.pyramid`</td>
</tr>
<tr>
<td markdown="span">`//generate`</td>
<td markdown="span">`worldedit.generation.shape`</td>
</tr>
<tr>
<td markdown="span">`//generatebiome`</td>
<td markdown="span">`worldedit.generation.shape.biome`</td>
</tr>
<tr>
<td markdown="span">`/schematic`</td>
<td markdown="span">`worldedit.schematic.delete`, `worldedit.schematic.list`, `worldedit.clipboard.load`, `worldedit.schematic.save`, `worldedit.schematic.formats`, `worldedit.schematic.load`, `worldedit.clipboard.save`, `worldedit.clipboard.share`, `worldedit.schematic.share`</td>
</tr>
<tr>
<td markdown="span">`/schematic delete`</td>
<td markdown="span">`worldedit.schematic.delete`</td>
</tr>
<tr>
<td markdown="span">`/schematic formats`</td>
<td markdown="span">`worldedit.schematic.formats`</td>
</tr>
<tr>
<td markdown="span">`/schematic list`</td>
<td markdown="span">`worldedit.schematic.list`</td>
</tr>
<tr>
<td markdown="span">`/schematic load`</td>
<td markdown="span">`worldedit.clipboard.load`, `worldedit.schematic.load`</td>
</tr>
<tr>
<td markdown="span">`/schematic save`</td>
<td markdown="span">`worldedit.clipboard.save`, `worldedit.schematic.save`</td>
</tr>
<tr>
<td markdown="span">`/schematic share`</td>
<td markdown="span">`worldedit.clipboard.share`, `worldedit.schematic.share`</td>
</tr>
<tr>
<td markdown="span">`//copy`</td>
<td markdown="span">`worldedit.clipboard.copy`</td>
</tr>
<tr>
<td markdown="span">`//cut`</td>
<td markdown="span">`worldedit.clipboard.cut`</td>
</tr>
<tr>
<td markdown="span">`//paste`</td>
<td markdown="span">`worldedit.clipboard.paste`</td>
</tr>
<tr>
<td markdown="span">`//rotate`</td>
<td markdown="span">`worldedit.clipboard.rotate`</td>
</tr>
<tr>
<td markdown="span">`//flip`</td>
<td markdown="span">`worldedit.clipboard.flip`</td>
</tr>
<tr>
<td markdown="span">`/clearclipboard`</td>
<td markdown="span">`worldedit.clipboard.clear`</td>
</tr>
<tr>
<td markdown="span">`//revolve`</td>
<td markdown="span">`worldedit.revolve`</td>
</tr>
<tr>
<td markdown="span">`/tool`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/tool cycler`</td>
<td markdown="span">`worldedit.tool.data-cycler`</td>
</tr>
<tr>
<td markdown="span">`/tool deltree`</td>
<td markdown="span">`worldedit.tool.deltree`</td>
</tr>
<tr>
<td markdown="span">`/tool farwand`</td>
<td markdown="span">`worldedit.tool.farwand`</td>
</tr>
<tr>
<td markdown="span">`/tool floodfill`</td>
<td markdown="span">`worldedit.tool.flood-fill`</td>
</tr>
<tr>
<td markdown="span">`/tool info`</td>
<td markdown="span">`worldedit.tool.info`</td>
</tr>
<tr>
<td markdown="span">`/tool lrbuild`</td>
<td markdown="span">`worldedit.tool.lrbuild`</td>
</tr>
<tr>
<td markdown="span">`/tool navwand`</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">`/tool none`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/tool repl`</td>
<td markdown="span">`worldedit.tool.replacer`</td>
</tr>
<tr>
<td markdown="span">`/tool selwand`</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">`/tool stacker`</td>
<td markdown="span">`worldedit.tool.stack`</td>
</tr>
<tr>
<td markdown="span">`/tool tree`</td>
<td markdown="span">`worldedit.tool.tree`</td>
</tr>
<tr>
<td markdown="span">`/none`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/selwand`</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">`/navwand`</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">`/info`</td>
<td markdown="span">`worldedit.tool.info`</td>
</tr>
<tr>
<td markdown="span">`/tree`</td>
<td markdown="span">`worldedit.tool.tree`</td>
</tr>
<tr>
<td markdown="span">`/repl`</td>
<td markdown="span">`worldedit.tool.replacer`</td>
</tr>
<tr>
<td markdown="span">`/cycler`</td>
<td markdown="span">`worldedit.tool.data-cycler`</td>
</tr>
<tr>
<td markdown="span">`/floodfill`</td>
<td markdown="span">`worldedit.tool.flood-fill`</td>
</tr>
<tr>
<td markdown="span">`/deltree`</td>
<td markdown="span">`worldedit.tool.deltree`</td>
</tr>
<tr>
<td markdown="span">`/farwand`</td>
<td markdown="span">`worldedit.tool.farwand`</td>
</tr>
<tr>
<td markdown="span">`/lrbuild`</td>
<td markdown="span">`worldedit.tool.lrbuild`</td>
</tr>
<tr>
<td markdown="span">`//`</td>
<td markdown="span">`worldedit.superpickaxe`</td>
</tr>
<tr>
<td markdown="span">`/mask`</td>
<td markdown="span">`worldedit.brush.options.mask`</td>
</tr>
<tr>
<td markdown="span">`/material`</td>
<td markdown="span">`worldedit.brush.options.material`</td>
</tr>
<tr>
<td markdown="span">`/range`</td>
<td markdown="span">`worldedit.brush.options.range`</td>
</tr>
<tr>
<td markdown="span">`/size`</td>
<td markdown="span">`worldedit.brush.options.size`</td>
</tr>
<tr>
<td markdown="span">`/tracemask`</td>
<td markdown="span">`worldedit.brush.options.tracemask`</td>
</tr>
<tr>
<td markdown="span">`/superpickaxe`</td>
<td markdown="span">`worldedit.superpickaxe.area`, `worldedit.superpickaxe.recursive`, `worldedit.superpickaxe`</td>
</tr>
<tr>
<td markdown="span">`/superpickaxe area`</td>
<td markdown="span">`worldedit.superpickaxe.area`</td>
</tr>
<tr>
<td markdown="span">`/superpickaxe recursive`</td>
<td markdown="span">`worldedit.superpickaxe.recursive`</td>
</tr>
<tr>
<td markdown="span">`/superpickaxe single`</td>
<td markdown="span">`worldedit.superpickaxe`</td>
</tr>
<tr>
<td markdown="span">`/brush`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/brush apply`</td>
<td markdown="span">`worldedit.brush.apply`</td>
</tr>
<tr>
<td markdown="span">`/brush apply forest`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/brush apply item`</td>
<td markdown="span">`worldedit.brush.item`</td>
</tr>
<tr>
<td markdown="span">`/brush apply set`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/brush biome`</td>
<td markdown="span">`worldedit.brush.biome`</td>
</tr>
<tr>
<td markdown="span">`/brush butcher`</td>
<td markdown="span">`worldedit.brush.butcher`</td>
</tr>
<tr>
<td markdown="span">`/brush clipboard`</td>
<td markdown="span">`worldedit.brush.clipboard`</td>
</tr>
<tr>
<td markdown="span">`/brush cylinder`</td>
<td markdown="span">`worldedit.brush.cylinder`</td>
</tr>
<tr>
<td markdown="span">`/brush deform`</td>
<td markdown="span">`worldedit.brush.deform`</td>
</tr>
<tr>
<td markdown="span">`/brush dilate`</td>
<td markdown="span">`worldedit.brush.morph`</td>
</tr>
<tr>
<td markdown="span">`/brush erode`</td>
<td markdown="span">`worldedit.brush.morph`</td>
</tr>
<tr>
<td markdown="span">`/brush extinguish`</td>
<td markdown="span">`worldedit.brush.ex`</td>
</tr>
<tr>
<td markdown="span">`/brush feature`</td>
<td markdown="span">`worldedit.brush.feature`</td>
</tr>
<tr>
<td markdown="span">`/brush forest`</td>
<td markdown="span">`worldedit.brush.forest`</td>
</tr>
<tr>
<td markdown="span">`/brush gravity`</td>
<td markdown="span">`worldedit.brush.gravity`</td>
</tr>
<tr>
<td markdown="span">`/brush heightmap`</td>
<td markdown="span">`worldedit.brush.heightmap`</td>
</tr>
<tr>
<td markdown="span">`/brush lower`</td>
<td markdown="span">`worldedit.brush.lower`</td>
</tr>
<tr>
<td markdown="span">`/brush morph`</td>
<td markdown="span">`worldedit.brush.morph`</td>
</tr>
<tr>
<td markdown="span">`/brush none`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/brush paint`</td>
<td markdown="span">`worldedit.brush.paint`</td>
</tr>
<tr>
<td markdown="span">`/brush paint forest`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/brush paint item`</td>
<td markdown="span">`worldedit.brush.item`</td>
</tr>
<tr>
<td markdown="span">`/brush paint set`</td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">`/brush raise`</td>
<td markdown="span">`worldedit.brush.raise`</td>
</tr>
<tr>
<td markdown="span">`/brush set`</td>
<td markdown="span">`worldedit.brush.set`</td>
</tr>
<tr>
<td markdown="span">`/brush smooth`</td>
<td markdown="span">`worldedit.brush.smooth`</td>
</tr>
<tr>
<td markdown="span">`/brush snow`</td>
<td markdown="span">`worldedit.brush.snow`</td>
</tr>
<tr>
<td markdown="span">`/brush snowsmooth`</td>
<td markdown="span">`worldedit.brush.snowsmooth`</td>
</tr>
<tr>
<td markdown="span">`/brush sphere`</td>
<td markdown="span">`worldedit.brush.sphere`</td>
</tr>
<tr>
<td markdown="span">`/brush splatter`</td>
<td markdown="span">`worldedit.brush.splatter`</td>
</tr>
<tr>
<td markdown="span">`/biomelist`</td>
<td markdown="span">`worldedit.biome.list`</td>
</tr>
<tr>
<td markdown="span">`/biomeinfo`</td>
<td markdown="span">`worldedit.biome.info`</td>
</tr>
<tr>
<td markdown="span">`//setbiome`</td>
<td markdown="span">`worldedit.biome.set`</td>
</tr>
<tr>
<td markdown="span">`//replacebiome`</td>
<td markdown="span">`worldedit.biome.set`</td>
</tr>
<tr>
<td markdown="span">`/chunkinfo`</td>
<td markdown="span">`worldedit.chunkinfo`</td>
</tr>
<tr>
<td markdown="span">`/listchunks`</td>
<td markdown="span">`worldedit.listchunks`</td>
</tr>
<tr>
<td markdown="span">`/delchunks`</td>
<td markdown="span">`worldedit.delchunks`</td>
</tr>
<tr>
<td markdown="span">`/restore`</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">`/snapshot`</td>
<td markdown="span">`worldedit.snapshots.restore`, `worldedit.snapshots.list`</td>
</tr>
<tr>
<td markdown="span">`/snapshot after`</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">`/snapshot before`</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">`/snapshot list`</td>
<td markdown="span">`worldedit.snapshots.list`</td>
</tr>
<tr>
<td markdown="span">`/snapshot sel`</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">`/snapshot use`</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">`/cs`</td>
<td markdown="span">`worldedit.scripting.execute`</td>
</tr>
<tr>
<td markdown="span">`/.s`</td>
<td markdown="span">`worldedit.scripting.execute`</td>
</tr>
<tr>
<td markdown="span">`//fill`</td>
<td markdown="span">`worldedit.fill`</td>
</tr>
<tr>
<td markdown="span">`//fillr`</td>
<td markdown="span">`worldedit.fill.recursive`</td>
</tr>
<tr>
<td markdown="span">`//drain`</td>
<td markdown="span">`worldedit.drain`</td>
</tr>
<tr>
<td markdown="span">`/fixlava`</td>
<td markdown="span">`worldedit.fixlava`</td>
</tr>
<tr>
<td markdown="span">`/fixwater`</td>
<td markdown="span">`worldedit.fixwater`</td>
</tr>
<tr>
<td markdown="span">`/removeabove`</td>
<td markdown="span">`worldedit.removeabove`</td>
</tr>
<tr>
<td markdown="span">`/removebelow`</td>
<td markdown="span">`worldedit.removebelow`</td>
</tr>
<tr>
<td markdown="span">`/removenear`</td>
<td markdown="span">`worldedit.removenear`</td>
</tr>
<tr>
<td markdown="span">`/replacenear`</td>
<td markdown="span">`worldedit.replacenear`</td>
</tr>
<tr>
<td markdown="span">`/snow`</td>
<td markdown="span">`worldedit.snow`</td>
</tr>
<tr>
<td markdown="span">`/thaw`</td>
<td markdown="span">`worldedit.thaw`</td>
</tr>
<tr>
<td markdown="span">`/green`</td>
<td markdown="span">`worldedit.green`</td>
</tr>
<tr>
<td markdown="span">`/extinguish`</td>
<td markdown="span">`worldedit.extinguish`</td>
</tr>
<tr>
<td markdown="span">`/butcher`</td>
<td markdown="span">`worldedit.butcher`</td>
</tr>
<tr>
<td markdown="span">`/remove`</td>
<td markdown="span">`worldedit.remove`</td>
</tr>
<tr>
<td markdown="span">`//calculate`</td>
<td markdown="span">`worldedit.calc`</td>
</tr>
<tr>
<td markdown="span">`//help`</td>
<td markdown="span">`worldedit.help`</td>
</tr>
</tbody>
</table>

## Other Permissions { #other-permissions }

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
<td markdown="span">`worldedit.navigation.jumpto.tool`</td>
<td markdown="span">Allows usage of the navigation wand’s `/jumpto` shortcut (left click).</td>
</tr>
<tr>
<td markdown="span">`worldedit.navigation.thru.tool`</td>
<td markdown="span">Allows usage of the navigation wand’s `/thru` shortcut (right click).</td>
</tr>
<tr>
<td markdown="span">`worldedit.anyblock`</td>
<td markdown="span">Allows usage of blocks in the [disallowed-blocks](https://worldedit.enginehub.org/en/latest/config/) config option.</td>
</tr>
<tr>
<td markdown="span">`worldedit.limit.unrestricted`</td>
<td markdown="span">Allows setting the limit via the `//limit` [command](https://worldedit.enginehub.org/en/latest/commands/) higher than the maximum in the [configuration](https://worldedit.enginehub.org/en/latest/config/), as well as other limit bypasses.</td>
</tr>
<tr>
<td markdown="span">`worldedit.timeout.unrestricted`</td>
<td markdown="span">Allows setting the calculation timeout via the `//timeout` [command](https://worldedit.enginehub.org/en/latest/commands/) higher than the maximum in the [configuration](https://worldedit.enginehub.org/en/latest/config/).</td>
</tr>
<tr>
<td markdown="span">`worldedit.inventory.unrestricted`</td>
<td markdown="span">Override the `use-inventory` option if enabled in the [configuration](https://worldedit.enginehub.org/en/latest/config/).</td>
</tr>
<tr>
<td markdown="span">`worldedit.override.bedrock`</td>
<td markdown="span">Allows breaking of bedrock with the super-pickaxe tool.</td>
</tr>
<tr>
<td markdown="span">`worldedit.override.data-cycler`</td>
<td markdown="span">Allows cycling non-whitelisted blocks with the data cycler tool.</td>
</tr>
<tr>
<td markdown="span">`worldedit.setnbt`</td>
<td markdown="span">Allows setting [extra data](https://minecraft.wiki/w/Block_entity) on blocks (such as signs, chests, etc).</td>
</tr>
<tr>
<td markdown="span">`worldedit.report.pastebin`</td>
<td markdown="span">Allows uploading report files to pastebin automatically for the `/worldedit report` [command](https://worldedit.enginehub.org/en/latest/commands/).</td>
</tr>
<tr>
<td markdown="span">`worldedit.scripting.execute.<filename>`</td>
<td markdown="span">Allows using the CraftScript with the given filename.</td>
</tr>
</tbody>
</table>

## Fabric Permissions Integration { #fabric-permissions-integration }

Added in version 7.4.5.

WorldEdit integrates into the Fabric Permissions API v1. The API identifies permissions with a namespaced Minecraft `Identifier` rather than a dotted string, so the nodes listed above are converted before they are checked. Depending on which permissions mod you use, you may need to write them differently.

!!! warning "Warning"

    If a node cannot be converted, WorldEdit falls back to the Fabric Permissions API v0, and then to vanilla operator levels. This should not happen in practice as we generally don’t have `worldedit` as its own permission node, but if other mods use our checks this may be an issue.

### Which form do I use? { #which-form-do-i-use }

Due to how permissions have historically worked, you might need to use different forms of the converted permission node. There are two forms of every node, and both come from the same conversion:

**`worldedit:region.set`**

The **identifier form**, for mods that expose the permission API’s identifiers directly.

**`worldedit.region.set`**

The **traditional form**. Some mods, like LuckPerms, rejoin the identifier’s namespace and path with a `.` instead of a `:` to match how permission nodes were traditionally formatted.

!!! warning "Warning"

    The traditional form is *not* always the same as the original node listed above. It is the converted node rejoined with a dot, so any lowercasing or escaping still applies. For example, `worldedit.scripting.execute.my script_v1!` becomes `worldedit.scripting.execute.my_20script_5fv1_21`.

    This only matters in practice for dynamic nodes, such as `worldedit.scripting.execute.<filename>`. Every static node WorldEdit uses is already lowercase and made of safe characters, so the result is identical.

!!! note "Note"

    The lowercasing and escaping are only needed because a Minecraft `Identifier` allows a very limited set of characters, which is a limitation of the Fabric Permissions API that we hope will be fixed in the future. See [this issue](https://github.com/FabricMC/fabric-api/issues/5505).

### Converter { #converter }

To assist with setting permissions, we’ve provided a small tool that converts from a permission node to the forms described above:

!!! note "Converter Tool"

    WorldEdit permission node

    Needs a namespace and a path separated by a dot, such as `worldedit.region.set`. A node without a dot is only matched by the fallback.

    Identifier form

    <a id="perm-converter-identifier"></a>

    Traditional form

    <a id="perm-converter-traditional"></a>

    The interactive converter needs JavaScript. You can apply the rules below by hand instead.

### How the conversion works { #how-the-conversion-works }

1. Split the node at the **first** `.`, into a *namespace* and *path*. If there is no `.`, or it is the first or last character, the node is not usable with the API and only the fallback works.

2. Convert both parts to lowercase using Java’s `toLowerCase(Locale.ROOT)`, then encode it as UTF-8.

3. Keep each byte that is `a` to `z`, `0` to `9`, `.` or `-`. The *path* must also keep `/`. Replace every other byte with `_` followed by its two hex digits. Notably, this includes `_` itself, which is output as `_5f`.

4. Join the two parts with `:` for the identifier form, or with `.` for the traditional form.

### Examples { #examples }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Node</th>
<th markdown="span">Identifier form</th>
<th markdown="span">Traditional form</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">`worldedit.region.set`</td>
<td markdown="span">`worldedit:region.set`</td>
<td markdown="span">`worldedit.region.set`</td>
</tr>
<tr>
<td markdown="span">`WorldEdit.scripting.execute.Build.js`</td>
<td markdown="span">`worldedit:scripting.execute.build.js`</td>
<td markdown="span">`worldedit.scripting.execute.build.js`</td>
</tr>
<tr>
<td markdown="span">`worldedit.scripting.execute.my script_v1!`</td>
<td markdown="span">`worldedit:scripting.execute.my_20script_5fv1_21`</td>
<td markdown="span">`worldedit.scripting.execute.my_20script_5fv1_21`</td>
</tr>
<tr>
<td markdown="span">`worldedit.scripting.execute.café`</td>
<td markdown="span">`worldedit:scripting.execute.caf_c3_a9`</td>
<td markdown="span">`worldedit.scripting.execute.caf_c3_a9`</td>
</tr>
<tr>
<td markdown="span">`worldedit.scripting.execute/tools/build.js`</td>
<td markdown="span">`worldedit:scripting.execute/tools/build.js`</td>
<td markdown="span">`worldedit.scripting.execute/tools/build.js`</td>
</tr>
<tr>
<td markdown="span">`worldedit`</td>
<td markdown="span">Not converted, only uses fallback</td>
<td markdown="span">Not converted, only uses fallback</td>
</tr>
</tbody>
</table>
