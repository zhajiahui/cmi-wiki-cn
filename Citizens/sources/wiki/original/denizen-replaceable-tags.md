For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

## Flags

~~{| class="wikitable" width="100%" border="1"
|-
| width="30%" | <flag.g:flag_name>
| Returns the value of a flag attached to the server. NOTE: In 0.9, it's more preferred to use <server.flag[flag_name]>
|-
| <flag.n:flag_name>
| Returns the value of a flag attached to the current NPC. NOTE: In 0.9, it's more preferred to use <npc.flag[flag_name]>
|-
| <flag.p:flag_name>
| Returns the value of a flag attached to the current player. NOTE: In 0.9, it's more preferred to use <player.flag[flag_name]>
|-
|<player[player_name].flag[flag_name]>
|Returns the value of a flag for another player.
|-
|<player.flag[flag_name]>.isexpired>
|Returns true or false if the duration of a flag has expired.
|}~~

<s><div class="mw-heading mw-heading2"><h2 id="Location">Location</h2></div></s>

~~All location tags require coordinates. You can have tags in the brackets [] or you can specify exact locations by yourself. For example, you could use~~

<s><pre>&lt;location[&lt;npc.location&gt;].biome.temperature&gt;</pre></s>

~~to get the temperature at the NPC's location.~~

<s><table border="1" class="wikitable" width="100%">
<tbody><tr>
<td width="30%">&lt;location[x,y,z,world].biome.formatted&gt;
</td>
<td>The formatted name of the biome at coordinates.
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].biome.humidity&gt;
</td>
<td>The current humidity at the coordinates.
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].biome.temperature&gt;
</td>
<td>The current temperature at the coordinates.
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].distance[x,y,z,world]&gt;
</td>
<td>The distance between 2 coordinates.
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].formatted&gt;
</td>
<td>The coordinates in an easier-to-read format.
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].is_liquid&gt;
</td>
<td>Whether or not the block at the coordinates are a liquid. Can be true or false.
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].light&gt;
</td>
<td>The light level at the coordinates.
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading2"><h2 id="NPC">NPC</h2></div></s>

~~NOTE: You can reference an NPC other than the one in the current script by using <npc[npc_id]>... So for example, <npc[2].id> (which would be completely useless) would return '2'.~~

<s><table border="1" class="wikitable" width="100%">
<tbody><tr>
<td width="30%">&lt;npc.flag[flag_name]&gt;
</td>
<td>Returns the value of a flag attached to an NPC.
</td></tr>
<tr>
<td>&lt;npc.id&gt;
</td>
<td>The ID number of the NPC.
</td></tr>
<tr>
<td>&lt;npc.location&gt;
</td>
<td>The coordinates of the NPC. [x,y,z,world]
</td></tr>
<tr>
<td>&lt;npc.location.previous_location&gt;
</td>
<td>The last location the NPC was at.
</td></tr>
<tr>
<td>&lt;npc.location.standing_on&gt;
</td>
<td>The Bukkit block name that the NPC is standing on.
</td></tr>
<tr>
<td>&lt;npc.location.standing_on_display&gt;
</td>
<td>The formatted block name that the NPC is standing on.
</td></tr>
<tr>
<td>&lt;npc.location.world&gt;
</td>
<td>The name of the world the NPC is in.
</td></tr>
<tr>
<td>&lt;npc.location.world_spawn&gt;
</td>
<td>The coordinates of the spawn of the world that the NPC is currently in.
</td></tr>
<tr>
<td>&lt;npc.location.x&gt;
</td>
<td>The x coordinate the NPC is at.
</td></tr>
<tr>
<td>&lt;npc.location.y&gt;
</td>
<td>The y coordinate the NPC is at.
</td></tr>
<tr>
<td>&lt;npc.location.z&gt;
</td>
<td>The z coordinate the NPC is at.
</td></tr>
<tr>
<td>&lt;npc.name&gt;
</td>
<td>The NPC's name.
</td></tr>
<tr>
<td>&lt;npc.name.nickname&gt;
</td>
<td>The NPC's nickname.
</td></tr>
<tr>
<td>&lt;npc.owner&gt;
</td>
<td>The owner of the NPC.
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading2"><h2 id="Player">Player</h2></div></s>

~~NOTE: You can reference a player other than the one in the current script by using <player[player_name]>... So for example, <player[Morphan1].name> (which would be completely useless) would return 'Morphan1'.~~

<s><table border="1" class="wikitable" width="100%">
<tbody><tr>
<td width="30%">&lt;player.chat_history&gt;
</td>
<td>Last message the player sent.
</td></tr>
<tr>
<td>&lt;player.chat_history[X]&gt;
</td>
<td>Message the player sent X times ago.
</td></tr>
<tr>
<td>&lt;player.equipment.boots&gt;
</td>
<td>The Bukkit name for the boots the player is wearing. Can also be used for chestplate, leggings, and helmet.
</td></tr>
<tr>
<td>&lt;player.equipment.boots.formatted&gt;
</td>
<td>The formatted name for the boots the player is wearing. Can also be used for chestplate, leggings, and helmet.
</td></tr>
<tr>
<td>&lt;player.flag[flag_name]&gt;
</td>
<td>Returns the value of a flag attached to a player.
</td></tr>
<tr>
<td>&lt;player.health&gt;
</td>
<td>The player's health, 1-20. Each number is half of a heart.
</td></tr>
<tr>
<td>&lt;player.health.formatted&gt;
</td>
<td>The player's formatted health. Can be healthy, scraped, injured, seriously wounded, and dying.
</td></tr>
<tr>
<td>&lt;player.health.percentage&gt;
</td>
<td>The player's health as a percentage.
</td></tr>
<tr>
<td>&lt;player.inventory.contains.display[display_name]&gt;
</td>
<td>Checks if the player's inventory contains an item with a name chosen on an anvil. You can also add .qty[X] to check if the player has an X amount of the item. Can be true or false.
</td></tr>
<tr>
<td>&lt;player.inventory.contains[item_id]&gt;
</td>
<td>Checks if the player's inventory contains an item. You can also add .qty[X] to check if the player has an X amount of the item. Can be true or false.
</td></tr>
<tr>
<td>&lt;player.food_level&gt;
</td>
<td>The player's food level, 1-20. Each number is half of a thing-on-the-hunger-bar.
</td></tr>
<tr>
<td>&lt;player.food_level.formatted&gt;
</td>
<td>The player's formatted food level. Can be healthy, parched, hungry, and famished.
</td></tr>
<tr>
<td>&lt;player.food_level.percentage&gt;
</td>
<td>The player's food level as a percentage.
</td></tr>
<tr>
<td>&lt;player.group[group_name]&gt;
</td>
<td>Checks if the player is in a group via Vault. Can be true or false.
</td></tr>
<tr>
<td>&lt;player.group[group_name].global&gt;&gt;
</td>
<td>Checks if the player is in a global group via Vault. Can be true or false.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.enchantments&gt;
</td>
<td>List of enchantments on item in player's hand.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.enchantments_with_level&gt;
</td>
<td>List of enchantments and their levels on item in player's hand.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.enchantments_with_level_only&gt;
</td>
<td>List of levels of enchantments on item in player's hand.
</td></tr>
<tr>
<td>&lt;player.item_in_hand&gt;
</td>
<td>Contains all details of the item in the player's hand.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.data&gt;
</td>
<td>The material data of the item the player is holding.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.display&gt;
</td>
<td>The name chosen on an anvil for the item the player is holding.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.durability&gt;
</td>
<td>The durability of the item the player is holding.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.id&gt;
</td>
<td>The ID of the block or item the player is holding. All block and item IDs are found <a class="external text" href="http://www.minecraftwiki.net/wiki/Data_values" rel="nofollow">here</a>.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.lore&gt;
</td>
<td>List of lore on item in the player's hand.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.max_stack&gt;
</td>
<td>The maximum amount you can have in one inventory slot of the item the player is holding.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.material&gt;
</td>
<td>Bukkit material name of the item in the player's hand.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.material.formatted&gt;
</td>
<td>Formatted material name of the item in the player's hand.
</td></tr>
<tr>
<td>&lt;player.item_in_hand.qty&gt;
</td>
<td>The current amount of the inventory slot of the item the player is holding.
</td></tr>
<tr>
<td>&lt;player.is_banned&gt;
</td>
<td>Whether the player is banned. Can be true or false.
</td></tr>
<tr>
<td>&lt;player.is_online&gt;
</td>
<td>Whether the player is online. Can be true or false.
</td></tr>
<tr>
<td>&lt;player.is_op&gt;
</td>
<td>Whether the player is an operator. Can be true or false.
</td></tr>
<tr>
<td>&lt;player.location&gt;
</td>
<td>The coordinates of the player. [x,y,z,world]
</td></tr>
<tr>
<td>&lt;player.location.bed_spawn&gt;
</td>
<td>The coordinates of the last bed the player slept in, if any.
</td></tr>
<tr>
<td>&lt;player.location.cursor_on[X]&gt;
</td>
<td>The location of the block the player's cursor is on, within X range.
</td></tr>
<tr>
<td>&lt;player.location.standing_on&gt;
</td>
<td>The Bukkit block name that the player is standing on.
</td></tr>
<tr>
<td>&lt;player.location.standing_on.formatted&gt;
</td>
<td>The formatted block name that the player is standing on.
</td></tr>
<tr>
<td>&lt;player.location.world&gt;
</td>
<td>The name of the world the player is in.
</td></tr>
<tr>
<td>&lt;player.location.world_spawn&gt;
</td>
<td>The coordinates of the spawn of the world that the player is currently in.
</td></tr>
<tr>
<td>&lt;player.location.x&gt;
</td>
<td>The x coordinate the player is at.
</td></tr>
<tr>
<td>&lt;player.location.y&gt;
</td>
<td>The y coordinate the player is at.
</td></tr>
<tr>
<td>&lt;player.location.z&gt;
</td>
<td>The z coordinate the player is at.
</td></tr>
<tr>
<td>&lt;player.money&gt;
</td>
<td>The amount of money in this player's account. Requires Vault and an economy plugin.
</td></tr>
<tr>
<td>&lt;player.name&gt;
</td>
<td>The player's name.
</td></tr>
<tr>
<td>&lt;player.name.display&gt;
</td>
<td>The player's display name. (The one that shows in chat.)
</td></tr>
<tr>
<td>&lt;player.mcmmo.level[skill_name]&gt;
</td>
<td>The player's current level for an McMMO skill.
</td></tr>
<tr>
<td>&lt;player.money&gt;
</td>
<td>How much money the player has, as a number. (0.0, 1.5, 2.25, etc.)
</td></tr>
<tr>
<td>&lt;player.money.asint&gt;
</td>
<td>How much money the player has, as an integer. (0, 1, 2, etc.)
</td></tr>
<tr>
<td>&lt;player.money.currency&gt;
</td>
<td>The currency set in this server's economy plugin.
</td></tr>
<tr>
<td>&lt;player.money.currency.plural&gt;
</td>
<td>The currency set in this server's economy plugin, in its plural form.
<p>Examples: Dollars, pounds, coins
</p>
</td></tr>
<tr>
<td>&lt;player.money.currency.singular&gt;
</td>
<td>The currency set in this server's economy plugin, in its singular form.
<p>Examples: Dollar, pound, coin
</p>
</td></tr>
<tr>
<td>&lt;player.script[script_name].failed&gt;
</td>
<td>Checks if the player has failed a script. Can be true or false.
</td></tr>
<tr>
<td>&lt;player.script[script_name].finished&gt;
</td>
<td>Checks if the player has finished a script. Can be true or false.
</td></tr>
<tr>
<td>&lt;player.time&gt;
</td>
<td>The player's time in ticks, from 0 to 23999. For a quick view of what different tick values mean in real life hours, look <a class="external text" href="http://media-mcw.cursecdn.com/b/bc/Day_Night_Clock_24h.png" rel="nofollow">here</a>.
</td></tr>
<tr>
<td>&lt;player.time.period&gt;
</td>
<td>The time period for this player. Can be "day" or "night".
</td></tr>
<tr>
<td>&lt;player.xp&gt;
</td>
<td>The total experience of a player.
</td></tr>
<tr>
<td>&lt;player.xp.level&gt;
</td>
<td>The current experience level of a player.
</td></tr>
<tr>
<td>&lt;player.weather&gt;
</td>
<td>The current weather in this player's world. Is "storming" if there's a storm, "sunny" if the weather is clear and it's daytime, and "clear" if the weather is clear and it's nighttime.
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading2"><h2 id="Util">Util</h2></div></s>

<s><table border="1" class="wikitable" width="100%">
<tbody><tr>
<td width="30%">&lt;util.random.int[1].to[50]&gt;
</td>
<td>Returns a random number between the lower bound (first number) and upper bound (second number).
</td></tr>
<tr>
<td width="30%">&lt;util.random.uuid&gt;
</td>
<td>Returns a random "uuid" useful for starting new queues.
</td></tr>
<tr>
<td width="30%">&lt;util.substr[string]&gt;
</td>
<td>Returns a substring of a string.
</td></tr>
</tbody></table></s>

<s><div class="mw-heading mw-heading2"><h2 id="Math_Tags">Math Tags</h2></div></s>

~~Math tags are a useful part of Denizen that, as the name implies, allows you to perform mathematical operations internally.

Here's the general syntax, with spaces for readability. (You shouldn't include spaces in your actual script. If you must, put it in "quotes")~~

<s><pre>&lt;m: firstThing + secondThing&gt; 
//Now, all together,
&lt;m:firstThing+secondThing&gt;
</pre></s>

~~Of course, + isn't the only mathematical operator that can be used. You can also use:

Minus and Modulus: (- and %)

Divide and Multiply: (/ and *)~~

<s><div class="mw-heading mw-heading2"><h2 id="Text">Text</h2></div></s>

<s><div class="mw-heading mw-heading3"><h3 id="Colors">Colors</h3></div></s>

<s><table border="1" class="wikitable" width="25%">
<tbody><tr>
<td width="60%">&lt;aqua&gt;
</td>
<td style="background-color:#55FFFF">
</td></tr>
<tr>
<td>&lt;black&gt;
</td>
<td style="background-color:black">
</td></tr>
<tr>
<td>&lt;blue&gt;
</td>
<td style="background-color:#5555FF">
</td></tr>
<tr>
<td>&lt;dark_aqua&gt;
</td>
<td style="background-color:#00AAAA">
</td></tr>
<tr>
<td>&lt;dark_blue&gt;
</td>
<td style="background-color:#0000AA">
</td></tr>
<tr>
<td>&lt;dark_gray&gt;
</td>
<td style="background-color:#555555">
</td></tr>
<tr>
<td>&lt;dark_green&gt;
</td>
<td style="background-color:#00AA00">
</td></tr>
<tr>
<td>&lt;dark_purple&gt;
</td>
<td style="background-color:#AA00AA">
</td></tr>
<tr>
<td>&lt;dark_red&gt;
</td>
<td style="background-color:#AA0000">
</td></tr>
<tr>
<td>&lt;gold&gt;
</td>
<td style="background-color:#FFAA00">
</td></tr>
<tr>
<td>&lt;gray&gt;
</td>
<td style="background-color:#AAAAAA">
</td></tr>
<tr>
<td>&lt;green&gt;
</td>
<td style="background-color:#55FF55">
</td></tr>
<tr>
<td>&lt;light_purple&gt;
</td>
<td style="background-color:#FF55FF">
</td></tr>
<tr>
<td>&lt;red&gt;
</td>
<td style="background-color:#FF5555">
</td></tr>
<tr>
<td>&lt;white&gt;
</td>
<td style="background-color:white">
</td></tr>
<tr>
<td>&lt;yellow&gt;
</td>
<td style="background-color:#FFFF55">
</td></tr></tbody></table></s>

<s><div class="mw-heading mw-heading3"><h3 id="Special_Characters">Special Characters</h3></div></s>

<s><table border="1" class="wikitable" width="25%">
<tbody><tr>
<td width="60%">&lt;&amp;nl&gt;
</td>
<td>NewLine
</td></tr>
<tr>
<td>&lt;&amp;cm&gt;
</td>
<td>,
</td></tr>
<tr>
<td>&lt;&amp;ss&gt;
</td>
<td>§
</td></tr>
<tr>
<td>&lt;&amp;sq&gt;
</td>
<td>'
</td></tr>
<tr>
<td>&lt;&amp;dq&gt;
</td>
<td>"
</td></tr>
<tr>
<td>&lt;&amp;co&gt;
</td>
<td>:
</td></tr>
<tr>
<td>&lt;&amp;rb&gt;
</td>
<td>]
</td></tr>
<tr>
<td>&lt;&amp;lb&gt;
</td>
<td>[
</td></tr>
<tr>
<td>&lt;&amp;rc&gt;
</td>
<td>}
</td></tr>
<tr>
<td>&lt;&amp;lc&gt;
</td>
<td>{
</td></tr>
<tr>
<td>&lt;&amp;ns&gt;
</td>
<td>#
</td></tr>
</tbody></table></s>

<s><div class="mw-heading mw-heading2"><h2 id="Pssst...">Pssst...</h2></div></s>

~~<http://pastebin.com/KBADLinZ>  
Here is a summary of them :)  
-Jeebs~~
