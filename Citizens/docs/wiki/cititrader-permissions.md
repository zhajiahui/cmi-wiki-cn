---
title: Cititrader / 权限
source_url: https://wiki.citizensnpcs.co/Cititrader/Permissions
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=3367
---


<a id="top"></a>

# Cititrader / 权限

<p>Cititrader会自动给ops授予权限，下面我会解释一下每个权限的作用。</p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.*</a></td>
<td>授予对所有商人命令的访问权限 [<strong>默认</strong>: op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.create</a></td>
<td>可以使用 /trader create [<strong>默认</strong>: op] 创建商人</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.sellprice</a></td>
<td>可以设置商人的销售价格[<strong>默认</strong>：op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.buyprice</a></td>
<td>可设置采购订单[<strong>默认</strong>：op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.setwallet</a></td>
<td>设置npc的钱包类型[<strong>默认</strong>: op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.wallet</a></td>
<td>从 NPC 钱包中给予/索取。 [<strong>默认</strong>：op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.disable</a></td>
<td>允许玩家禁用 NPC（关闭商店）[<strong>默认</strong>：op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.enable</a></td>
<td>允许玩家启用 NPC（打开商店）[<strong>默认</strong>：op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.cancel</a></td>
<td>允许玩家取消商人 NPC 的任何交易或状态 [<strong>默认</strong>: true]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.link</a></td>
<td>允许玩家链接 NPC 以使用其价目表。 [<strong>默认</strong>：op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.unlink</a></td>
<td>允许玩家取消链接 NPC[<strong>默认</strong>: op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.linkchest</a></td>
<td>允许玩家将箱子链接到 NPC [<strong>默认</strong>：op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.command.unlinkchest</a></td>
<td>允许玩家取消箱子与 NPC 的链接 [<strong>默认</strong>：op]</td>
</tr>
</tbody>
</table>
<a id="Individual_Wallet_Permissions"></a><h3 id="individual-wallet-permissions">个人钱包权限</h3>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.wallet.private</a></td>
<td>允许用户设置商人使用自己的私人钱包。 [<strong>默认</strong>：用户]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.wallet.owner</a></td>
<td>允许用户设置商人使用其所有者的银行钱包。 [<strong>默认</strong>：用户]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.wallet.bank</a></td>
<td>允许用户设置商人使用银行账户（经济插件必须支持银行，用户必须拥有银行账户）。 [<strong>默认</strong>：用户]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.wallet.admin</a></td>
<td>允许用户将商人设置为管理员，无限金钱和物品。 [<strong>默认</strong>：op]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">traders.wallet.town_bank</a></td>
<td>允许用户设置商人使用城镇银行（需要城镇插件，您需要拥有 NPC 并成为城镇市长或助理）。 [<strong>默认</strong>：op]</td>
</tr>
</tbody>
</table>

