For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>Replaceable data tags can be used to dynamically put flags and values inside texts and commands.
</p>
</div></s>

<s><div class="mw-heading mw-heading3"><h3 id="Flag_Replaceables">Flag Replaceables</h3></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:ghostwhite; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;FLAG.PLAYER:Name:fallback&gt; or &lt;FLAG.P:Name:fallback&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The value of a FLAG set on the Player, with the optional 'fallback' being the value used if the FLAG isn't found.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:ghostwhite; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;FLAG.DENIZEN:Name:fallback&gt; or &lt;FLAG.D:Name:fallback&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The value of a FLAG set on the Denizen, with the optional 'fallback' being the value used if the FLAG isn't found.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:ghostwhite; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;FLAG.GLOBAL:Name:fallback&gt; or &lt;FLAG.G:Name:fallback&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The value of a FLAG set globally, with the optional 'fallback' being the value used if the FLAG isn't found.
 </div>
</td></tr></tbody></table>
</div>
</div></s>

<s><div class="mw-heading mw-heading3"><h3 id="Chat_Input_Replaceable">Chat Input Replaceable</h3></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lightcyan; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;*&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  Contains the value of the Chat Trigger used by the Player in the Current Step. Unlike other replaceables, it can currently only be used in Speech commands and the FLAG command.
 </div>
</td></tr></tbody></table>
</div>
</div></s>

<s><div class="mw-heading mw-heading3"><h3 id="Player_Replaceables">Player Replaceables</h3></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;DISPLAYNAME&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The display name of the Player interacting with the Denizen, i.e. the name including colors.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;HEALTH&gt; or &lt;PLAYER.HEALTH&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The Player's health, from 0 to 20.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER&gt; or &lt;PLAYER.NAME&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The name of the Player.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.BOOTS&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The MATERIAL of the boots that the Player is wearing. Is 'FALSE' if the Player is not wearing any.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.CHESTPLATE&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The MATERIAL of the chestplate that the Player is wearing. Is 'FALSE' if the Player is not wearing any.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.EXP&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The Player's total experience.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.EXP_TO_NEXT_LEVEL&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The experience the Player must gain to reach the next level.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.FOOD_LEVEL&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The Player's food level, from 0 to 20.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.HELM&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The MATERIAL of the helm that the Player is wearing. Is 'FALSE' if the Player is not wearing any.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.ITEM_IN_HAND.ID&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The ID of the item in the Player's hand. Is '0' if the Player's hand is empty.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.ITEM_IN_HAND.MATERIAL&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The MATERIAL of the item in the Player's hand. Is 'AIR' if the Player's hand is empty.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.ITEM_IN_HAND.NAME&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The name of the item in the Player's hand. Doesn't work at the moment.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.ITEM_IN_HAND.QTY&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The quantity of the item in the Player's hand.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.KILLER&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The name of the last killer of this Player. Doesn't work at the moment.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.LEGGINGS&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The MATERIAL of the leggings that the Player is wearing. Is 'FALSE' if the Player is not wearing any.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.MONEY&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The amount of money that the Player has. This replaceable will only work if you have Vault installed and a compatible permissions/economy plugin.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.WORLD&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The name of the world the Player is in.
 </div>
</td></tr></tbody></table>
</div>
</div></s>

<s><div class="mw-heading mw-heading3"><h3 id="Denizen_Replaceables">Denizen Replaceables</h3></div></s>

<s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:papayawhip; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;NPC&gt; or &lt;DENIZEN.NAME&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The name of the Denizen.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:papayawhip; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;NPCID&gt; or &lt;DENIZEN.NPCID&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The ID of the Denizen.
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:papayawhip; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;WORLD&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  The name of the world the Denizen is in.
 </div>
</td></tr></tbody></table>
</div>
</div></s>
