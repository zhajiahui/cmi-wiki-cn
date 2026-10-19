---
title: Denizen / 0.7 / 可替换标签 .8
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Replaceables.8
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5393
---


<a id="top"></a>

# Denizen / 0.7 / 可替换标签 .8

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>可替换的数据标签可用于动态地将标志和值放入文本和命令中。</p>
<a id="Flag_Replaceables"></a><h3 id="flag-replaceables">标记可更换件</h3>
<table>
<thead>
<tr>
<th><player.name></player.name></th>
<th>获取 bukkit 玩家名称</th>
</tr>
</thead>
<tbody>
<tr>
<td><player.name.display></player.name.display></td>
<td>获取带有前缀和颜色的玩家名称（如果指定）</td>
</tr>
<tr>
<td><player.name.plist></player.name.plist></td>
<td>获取玩家列表中列出的玩家名称</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th><player.location></player.location></th>
<th>获取玩家的当前位置，格式为 dscript。</th>
</tr>
</thead>
<tbody>
<tr>
<td><player.location.formatted></player.location.formatted></td>
<td>获取玩家当前位置的文本友好格式版本</td>
</tr>
<tr>
<td><player.location.standing_on></player.location.standing_on></td>
<td>获取玩家当前站立的方块的名称</td>
</tr>
<tr>
<td><player.location.world></player.location.world></td>
<td>获取玩家当前所在世界的名称。</td>
</tr>
<tr>
<td><player.location.world_spawn></player.location.world_spawn></td>
<td>获取玩家当前世界的生成位置，格式为 dscript</td>
</tr>
<tr>
<td><player.location.bed_spawn></player.location.bed_spawn></td>
<td>获取玩家当前的床生成位置，格式为 dscript。</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th><player.health></player.health></th>
<th>获取玩家当前的健康状况。</th>
</tr>
</thead>
<tbody>
<tr>
<td><player.health.formatted></player.health.formatted></td>
<td>通过将最大生命值除以当前生命值，获取玩家生命值的文本友好表示。</td>
</tr>
<tr>
<td><player.health.formatted.#></player.health.formatted.#></td>
<td>相同，只是指定 max-health 而不是依赖 bukkit 的 p.getMaxHealth()。</td>
</tr>
<tr>
<td><player.health.percentage></player.health.percentage></td>
<td>获取玩家生命值的百分比。</td>
</tr>
<tr>
<td><player.health.percentage.#></player.health.percentage.#></td>
<td>相同，只是指定 max-health 而不是依赖 bukkit 的 p.getMaxHealth()。</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th><player.food_level></player.food_level></th>
<th>获取玩家当前的食物等级。</th>
</tr>
</thead>
<tbody>
<tr>
<td><player.food_level.formatted></player.food_level.formatted></td>
<td>获取玩家食物水平的文本友好表示。</td>
</tr>
<tr>
<td><player.food_level.formatted.#></player.food_level.formatted.#></td>
<td>相同，除了指定最大食物水平。</td>
</tr>
<tr>
<td><player.food_level.percentage></player.food_level.percentage></td>
<td>获取玩家食物水平的百分比。</td>
</tr>
<tr>
<td><player.food_level.percentage.#></player.food_level.percentage.#></td>
<td>相同，除了指定最大食物水平。</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th><player.xp></player.xp></th>
<th>获取下一级别的进度百分比。</th>
</tr>
</thead>
<tbody>
<tr>
<td><player.xp.to_level></player.xp.to_level></td>
<td>获取玩家升级到下一级别之前的 XP 数量。</td>
</tr>
<tr>
<td><player.xp.total></player.xp.total></td>
<td>获取玩家当前拥有的 XP 总量。</td>
</tr>
<tr>
<td><player.xp.level></player.xp.level></td>
<td>获取玩家当前的 XP 等级。</td>
</tr>
</tbody>
</table>

