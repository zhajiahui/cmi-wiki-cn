---
title: 权限
source_url: https://worldedit.enginehub.org/en/latest/permissions/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 权限 { #permissions }

默认情况下，没有人可以使用 WorldEdit。要让自己、管理人员和玩家使用它，必须授予相应权限。可以给管理人员和管理员 OP 身份，除非[配置](config.md)中禁用了这种行为；也可以通过权限插件授予本页列出的权限节点，后者能更细致地控制权限。

授予自己或其他管理员 `worldedit.*`，可获得 WorldEdit 的全部访问权限。

## 命令 { #commands }

部分命令的说明见[命令](commands.md)页面。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">命令</th>
<th markdown="span">权限</th>
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

## 其他权限 { #other-permissions }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">权限</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">`worldedit.navigation.jumpto.tool`</td>
<td markdown="span">允许使用导航工具的 `/jumpto` 快捷操作，即左键点击。</td>
</tr>
<tr>
<td markdown="span">`worldedit.navigation.thru.tool`</td>
<td markdown="span">允许使用导航工具的 `/thru` 快捷操作，即右键点击。</td>
</tr>
<tr>
<td markdown="span">`worldedit.anyblock`</td>
<td markdown="span">允许使用 [disallowed-blocks](config.md) 配置中禁止的方块。</td>
</tr>
<tr>
<td markdown="span">`worldedit.limit.unrestricted`</td>
<td markdown="span">允许通过 `//limit` [命令](commands.md)将限制设为高于[配置](config.md)中的最大值，也允许绕过其他限制。</td>
</tr>
<tr>
<td markdown="span">`worldedit.timeout.unrestricted`</td>
<td markdown="span">允许通过 `//timeout` [命令](commands.md)将计算超时时间设为高于[配置](config.md)中的最大值。</td>
</tr>
<tr>
<td markdown="span">`worldedit.inventory.unrestricted`</td>
<td markdown="span">覆盖[配置](config.md)中已启用的 `use-inventory` 选项。</td>
</tr>
<tr>
<td markdown="span">`worldedit.override.bedrock`</td>
<td markdown="span">允许使用超级镐工具破坏基岩。</td>
</tr>
<tr>
<td markdown="span">`worldedit.override.data-cycler`</td>
<td markdown="span">允许使用数据循环工具切换白名单以外方块的数据。</td>
</tr>
<tr>
<td markdown="span">`worldedit.setnbt`</td>
<td markdown="span">允许为方块（例如告示牌、箱子等）设置[额外数据](https://minecraft.wiki/w/Block_entity)。</td>
</tr>
<tr>
<td markdown="span">`worldedit.report.pastebin`</td>
<td markdown="span">允许 `/worldedit report` [命令](commands.md)将报告文件自动上传到 pastebin。</td>
</tr>
<tr>
<td markdown="span">`worldedit.scripting.execute.<filename>`</td>
<td markdown="span">允许使用指定文件名的 CraftScript。</td>
</tr>
</tbody>
</table>

## Fabric 权限集成 { #fabric-permissions-integration }

在 7.4.5 版本中加入。

WorldEdit 集成了 Fabric Permissions API v1。该 API 使用带命名空间的 Minecraft `Identifier` 标识权限，而不是用点分隔的字符串，因此在检查上述权限节点之前会先转换它们。根据所用权限模组的不同，你可能需要采用不同的写法。

!!! warning "警告"

    如果某个节点无法转换，WorldEdit 会回退到 Fabric Permissions API v0，然后再回退到原版管理员等级。实际使用中通常不会遇到这种情况，因为我们一般不会将 `worldedit` 单独用作权限节点；但如果其他模组使用我们的权限检查，就可能遇到此问题。

### 该使用哪种形式？ { #which-form-do-i-use }

由于权限系统以往的工作方式，你可能需要使用转换后的不同形式。每个节点有两种形式，均来自同一次转换：

**`worldedit:region.set`**

**标识符形式**，用于直接公开权限 API 标识符的模组。

**`worldedit.region.set`**

**传统形式**。某些模组（例如 LuckPerms）会用 `.` 而不是 `:` 重新连接标识符的命名空间和路径，以符合传统权限节点的格式。

!!! warning "警告"

    传统形式*并不总是*与上面列出的原始节点相同。它是将转换后的节点用点重新连接，因此小写转换和转义仍然适用。例如，`worldedit.scripting.execute.my script_v1!` 会变成 `worldedit.scripting.execute.my_20script_5fv1_21`。

    实际使用中，这只影响动态节点，例如 `worldedit.scripting.execute.<filename>`。WorldEdit 使用的所有静态节点都已经是小写，且只包含安全字符，因此转换结果与原节点相同。

!!! note "注意"

    之所以需要转为小写并进行转义，是因为 Minecraft `Identifier` 只允许非常有限的字符。这是 Fabric Permissions API 的限制，我们希望未来能解决它。参见[此问题](https://github.com/FabricMC/fabric-api/issues/5505)。

### 转换器 { #converter }

为了方便设置权限，我们提供了一个小工具，可将权限节点转换为上述形式：

!!! note "转换工具"

    WorldEdit 权限节点

    必须包含用点分隔的命名空间和路径，例如 `worldedit.region.set`。不带点的节点只能通过回退机制匹配。

    标识符形式

    <a id="perm-converter-identifier"></a>

    传统形式

    <a id="perm-converter-traditional"></a>

    交互式转换器需要 JavaScript。你也可以按以下规则手动转换。

### 转换规则 { #how-the-conversion-works }

1. 在**第一个** `.` 处分割节点，得到*命名空间*和*路径*。如果没有 `.`，或者它位于第一个或最后一个字符处，则该节点无法用于此 API，只能使用回退机制。

2. 使用 Java 的 `toLowerCase(Locale.ROOT)` 将两部分都转为小写，然后编码为 UTF-8。

3. 保留值为 `a` 到 `z`、`0` 到 `9`、`.` 或 `-` 的每个字节。*路径*还必须保留 `/`。其他字节都替换为 `_` 加上该字节的两位十六进制数。特别注意，`_` 本身也要转换，输出为 `_5f`。

4. 标识符形式使用 `:` 连接这两部分，传统形式则使用 `.`。

### 示例 { #examples }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">节点</th>
<th markdown="span">标识符形式</th>
<th markdown="span">传统形式</th>
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
<td markdown="span">不转换，仅使用回退机制</td>
<td markdown="span">不转换，仅使用回退机制</td>
</tr>
</tbody>
</table>
