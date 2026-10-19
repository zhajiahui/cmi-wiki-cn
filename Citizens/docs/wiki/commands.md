---
title: 命令
source_url: https://wiki.citizensnpcs.co/Commands
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5677
---


<a id="top"></a>

# 命令

<p>请阅读下面的详细命令文档。有关每种类型的命令和权限的更多信息，请参阅其相应的页面。</p>
<p><strong>[]</strong> - 强制</p>
<p><strong>()</strong> - 可选</p>
<p><strong>Command</strong> - 命令语法</p>
<p><strong>参数 说明</strong> - 命令参数的描述</p>
<p><strong>需要选择</strong> - 该命令是否需要选择 NPC</p>
<p><strong>需要所有权</strong> - 命令是否要求您是 NPC 的所有者</p>
<p><strong>需要生物类型</strong> - 该命令是否要求 NPC 是某种生物类型</p>
<p><strong>Permission</strong> - 命令的权限节点</p>
<p><strong>Description</strong> - 命令的简短描述</p>
<a id="Commands_not_listed_here"></a><h2 id="commands-not-listed-here">此处未列出的命令</h2>
<p><strong>还有相当多的命令没有在这里列出，主要是出于维护顺序的原因（wiki 不经常更新，但实际的命令列表会定期更新。）</strong>
<strong>要查看当前版本的 Citizens 上的命令列表，只需键入 <code>/npc help</code> 游戏中。您可以使用 <code>/npc help 2</code> 查看第 2 页，依此类推（将 2 切换到任意页码）。</strong></p>
<p>要查看特定命令的信息，您可以在游戏中使用 <code>/npc help create</code>。将 "create" 更改为任何其他命令名称（该示例将显示 <code>/npc create</code> 命令的帮助）。</p>
<p>某些命令有文档 其他页面：</p>
<ul>
<li>/NPC皮肤 - <a href="skins.md" title="Skins">皮肤</a></li>
</ul>
<p>还有许多由其他特征添加的命令。见<a href="characters.md" title="Characters">角色类型</a></p>
<a id="Adding_Click_Commands"></a><h2 id="adding-click-commands">添加点击命令</h2>
<p>如果您正在寻找一种在点击 NPC 时添加自动运行命令的方法，请参阅 <a href="npc-commands.md" title="NPC Commands">NPC 点击命令</a> 中的说明。</p>
<a id="Admin_Commands"></a><h2 id="admin-commands">管理命令</h2>
<p>用于管理 Citizens 的命令。</p>
<table>
<thead>
<tr>
<th><strong>管理命令</strong></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Command</td>
<td>权限</td>
<td>描述</td>
</tr>
<tr>
<td>/citizens</td>
<td>citizens.admin</td>
<td>显示基本插件信息</td>
</tr>
<tr>
<td>/citizens reload</td>
<td>citizens.admin</td>
<td>重新加载Citizens</td>
</tr>
<tr>
<td>/citizens save</td>
<td>citizens.admin</td>
<td>保存NPCs和配置</td>
</tr>
</tbody>
</table>
<a id="Help_Commands"></a><h2 id="help-commands">帮助命令</h2>
<p>游戏中用于显示帮助屏幕的命令。</p>
<table>
<thead>
<tr>
<th><strong>帮助命令</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Command</td>
<td>论点</td>
<td>权限</td>
<td>描述</td>
<td></td>
<td></td>
</tr>
<tr>
<td>/citizens help</td>
<td><em>（页码）</em> - 要显示的页码</td>
<td>citizens.help</td>
<td>显示 Citizens 帮助菜单</td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc help</td>
<td><em>（页码）</em> - 要显示的页码</td>
<td>citizens.npc.help</td>
<td>显示 NPC 帮助菜单</td>
<td></td>
<td></td>
</tr>
<tr>
<td>/trait help</td>
<td><em>（页码）</em> - 要显示的页码</td>
<td>citizens.trait.help</td>
<td>显示特征帮助菜单</td>
<td></td>
<td></td>
</tr>
<tr>
<td>/template help</td>
<td><em>（页码）</em> - 要显示的页码</td>
<td>citizens.templates.help</td>
<td>显示模板帮助菜单</td>
<td></td>
<td></td>
</tr>
<tr>
<td>/waypoints help</td>
<td><em>（页码）</em> - 要显示的页码</td>
<td>citizens.waypoints.help</td>
<td>显示航点帮助菜单</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<a id="NPC_Commands"></a><h2 id="npc-commands">NPC 点击命令</h2>
<p>适用于所有 NPCs 的通用命令。</p>
<table>
<thead>
<tr>
<th><strong>NPC 点击命令</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>命令</td>
<td>论点</td>
<td>描述</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc</td>
<td><code>None</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc activationrange</td>
<td><code>[range]</code></td>
<td>设置激活范围</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc age</td>
<td><code>[age] (-l(ock))</code></td>
<td>只能用于可以成为婴儿的实体。使用 <strong>-l</strong> 标志来锁定随时间变化的年龄（注意：可能需要重新登录才能看到这一点）。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc aggressive</td>
<td><code>[true|false] (-t(emporary))</code></td>
<td>设置实体的攻击状态</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc ai</td>
<td><code>(true|false)</code></td>
<td>设置 NPC 是否应使用普通 AI</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc allay</td>
<td><code>(-d(ancing))</code></td>
<td>设置allay修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc anchor</td>
<td><code>(--save [name]|--assume [name]|--remove [name]) (-a) (-c)</code></td>
<td>管理 NPC 的位置锚点</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc areaeffectcloud</td>
<td><code>--color [color] --duration [duration] --radius [radius] --radius_per_tick [radius] --particle [particle]</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc armadillo</td>
<td><code>--state [state]</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc armorstand</td>
<td><code>--visible [visible] --small [small] --marker [marker] --gravity [gravity] --arms [arms] --baseplate [baseplate] --(head|body|leftarm|leftleg|rightarm|rightleg)pose [angle x,y,z]</code></td>
<td>编辑盔甲架属性</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc attribute</td>
<td><code>[attribute] [value]</code></td>
<td>设置各种 NPC 属性</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc axolotl</td>
<td><code>(-d) (--variant variant)</code></td>
<td>设置蝾螈修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc bat</td>
<td><code>--awake [awake]</code></td>
<td>设置蝙蝠修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc bee</td>
<td><code>(-s/-n) --anger anger</code></td>
<td>设置蜜蜂修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc behavior</td>
<td><code>[file.yml]</code></td>
<td>管理行为树</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc boat</td>
<td><code>--type [type]</code></td>
<td>设置船修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc bossbar</td>
<td><code>--style [style] --color [color] --title [title] --visible [visible] --viewpermission [permission] --flags [flags] --track [health | placeholder] --range [range]</code></td>
<td>编辑老板栏属性</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc breakblock</td>
<td><code>--location [x,y,z] --radius [radius]</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc camel</td>
<td><code>(--pose pose)</code></td>
<td>设置驼峰修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc cat</td>
<td><code>(-s/-n/-l) --type type --ccolor collar color</code></td>
<td>设置猫修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc chicken</td>
<td><code>(--variant variant)</code></td>
<td>管理鸡修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc chunkload</td>
<td><code>(-t(emporary))</code></td>
<td>切换 NPC 强制块保持加载状态</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc collidable</td>
<td><code>--fluids [true|false]</code></td>
<td>切换 NPC 的可碰撞性</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc command</td>
<td><code>(add [command] | execute [player UUID] [hand] | remove [id|all] | permissions [permissions] (duration) | sequential | cycle | random | forgetplayer (uuid) | clearerror [type] (name|uuid) | errormsg [type] [msg] | persistsequence [true|false] | cost [cost] (id) | expcost [cost] (id) | itemcost (id)) (-s(hift)) (-l[eft]/-r[ight]) (-p[layer] -o[p]), --cooldown --gcooldown [seconds] --delay [ticks] --permissions [perms] --n [max # of uses] --gn [max # of global uses]</code></td>
<td>使用 <strong>-l</strong> 标志使命令在左键点击时运行，<strong>-r</strong> 在右键点击时运行（默认）。 <strong>执行</strong> 触发分配的命令，就像玩家点击 npc 一样。使用 <strong>--cooldown</strong>（在 <strong>秒</strong> 中）设置每个玩家的冷却时间，然后才能再次使用该命令。使用 <strong>--gcooldown</strong> 设置服务器范围的冷却时间（以秒为单位）。 <strong>--delay</strong> 将在执行命令之前等待 <strong>蜱虫</strong> 中指定的时间。 <strong>--permissions</strong> 会将命令设置为需要特定权限（多个用逗号分隔）。 <strong>--n</strong> 只会让玩家运行该命令的次数。使用 <strong>-o</strong> 作为操作临时执行命令，并使用 <strong>-p</strong> 作为点击玩家而不是服务器运行命令。使用 <strong>-n</strong> 以 NPC 的身份运行命令，而不是点击玩家。玩家类型必须为 NPC。要授予玩家临时权限而不是 op，请使用 <strong>/npc command permissions</strong>。使用 <strong>/npc command cost/expcost/itemcost</strong> 设置每次点击的费用。使用 <strong>/npc command sequential</strong> 或 <strong>/npc command cycle</strong> 可以一条一条地执行命令，而不是一次全部执行。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc configgui</td>
<td><code>None</code></td>
<td>显示 NPC 配置 GUI</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc controllable</td>
<td><code>(-m(ount),-o(wner required)) (--controls [controls]) (--enabled [true|false])</code></td>
<td>切换NPC是否可以骑行和控制</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc copier</td>
<td><code>None</code></td>
<td>切换 NPC 复印机</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc coppergolem</td>
<td><code>(--weatherstate state) (--weatheringtick tick)</code></td>
<td>控制铜傀儡修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc copy</td>
<td><code>(--name newname)</code></td>
<td>复制 NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc cow</td>
<td><code>(--variant variant)</code></td>
<td>管理牛修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc create</td>
<td><code>[name] ((-b(aby),u(nspawned),s(ilent),t(emporary),c(enter),p(acket)) --at [x,y,z,world] --type [type] --item (item) --trait ['trait1, trait2...'] --model [model name] --nameplate [true|false|hover] --temporaryduration [duration] --registry [registry name]</code></td>
<td>创建一个新的NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc debug</td>
<td><code>-p(aths) -n(avigation) -i(tem in hand)</code></td>
<td>显示调试信息</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc deselect</td>
<td><code>None</code></td>
<td>取消选择当前选定的 NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc despawn</td>
<td><code>(id)</code></td>
<td>消灭 NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc disguise</td>
<td><code>--type [type]</code></td>
<td>管理实体伪装</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc display</td>
<td><code>--billboard [billboard] --brightness [blockLight,skyLight] --interpolationdelay [delay] --interpolationduration [duration] --height [height] --width [width] --scale [x,y,z] --viewrange [range] --leftrotation [x,y,z,w] --rightrotation [x,y,z,w] --offset [x,y,z]</code></td>
<td>设置各种显示实体修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc drops</td>
<td><code>None</code></td>
<td>编辑 NPC 的掉落物</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc endercrystal</td>
<td><code>-b(ottom)</code></td>
<td>编辑末影水晶修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc enderdragon</td>
<td><code>--phase [phase] --destroywalls [true|false]</code></td>
<td>设置末影龙修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc enderman</td>
<td><code>-a(ngry)</code></td>
<td>设置末影人修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc entitypose</td>
<td><code>[pose]</code></td>
<td>控制实体姿态</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc equip</td>
<td><code>None</code></td>
<td>切换设备编辑器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc eval</td>
<td><code>[expression]</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc flyable</td>
<td><code>(true|false)</code></td>
<td>切换或设置 NPC 的可飞行状态</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc follow</td>
<td><code>(player name|NPC id) (-p[rotect]) (--margin [margin]) (--enable [boolean])</code></td>
<td>切换 NPC 跟随您</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc forcefield</td>
<td><code>--width [width] --height [height] --strength [strength] --vertical-strength [vertical strength]</code></td>
<td>创建一个力场，将靠近 NPC 的玩家推开</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc fox</td>
<td><code>--type type --sleeping [true|false] --sitting [true|false] --crouching [true|false] --interested [true|false] --pouncing [true|false] --faceplanted [true|false]</code></td>
<td>设置狐狸修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc frog</td>
<td><code>(--variant variant)</code></td>
<td>设置青蛙修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc gamemode</td>
<td><code>[gamemode]</code></td>
<td>改变游戏模式</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc glowing</td>
<td><code>--color [minecraft chat color]</code></td>
<td>切换 NPC 的发光状态</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc goat</td>
<td><code>-l(eft) -r(ight) -n(either) -b(oth) horn</code></td>
<td>设置山羊修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc gravity</td>
<td><code>None</code></td>
<td>切换重力</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc hitbox</td>
<td><code>--scale [scale] --width/height [value] --offset [x,y,z]</code></td>
<td>设置 NPC 碰撞箱</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc hologram</td>
<td><code>add [text] (--duration [duration]) | insert [line #] [text] | set [line #] [text] | remove [line #] | edit_npc [template | name | line #] | clear | lineheight [height] | viewrange [range] | margintop [line #] [margin] | marginbottom [line #] [margin]</code></td>
<td>控制 NPC 全息图文本</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc home</td>
<td><code>--location [loc] --delay [delay] --distance [distance] -h(ere) -p(athfind) -t(eleport)</code></td>
<td>控制家庭位置</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc horse</td>
<td><code>(--color color) (--type type) (--style style) (-cbt)</code></td>
<td>使用 -c 标志使 NPC 拥有箱子，或使用 -b 标志阻止它们拥有箱子。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc hurt</td>
<td><code>[damage]</code></td>
<td>损坏 NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc id</td>
<td><code>None</code></td>
<td>将选定的 NPC 的 ID 发送给发送者</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc inventory</td>
<td><code>(player name/uuid)</code></td>
<td>显示 NPC 的库存</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc item</td>
<td><code>[item] (-h(and))</code></td>
<td>设置NPC的项目</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc itemdisplay</td>
<td><code>--transform [transform]</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc itemframe</td>
<td><code>--visible [true|false] --fixed [true|false] --rotation [rotation] --item [item] --face [face]</code></td>
<td>设置项目框架修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc jump</td>
<td><code>None</code></td>
<td>使 NPC 跳跃</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc knockback</td>
<td><code>(--explicit true|false)</code></td>
<td>切换 NPC 击退</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc leashable</td>
<td><code>None</code></td>
<td>切换可束缚性</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc list</td>
<td><code>(page) ((-a) --owner (owner) --type (type) --char (char) --registry (name))</code></td>
<td>列表 NPCs</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc llama</td>
<td><code>(--color color) (--strength strength)</code></td>
<td>设置美洲驼修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc lookclose</td>
<td><code>--range [range] --filter [filter] -r[ealistic looking] --randomlook [true|false] --perplayer [true|false] --randomswitchtargets [true|false] --randompitchrange [min,max] --randomyawrange [min,max] --disablewhennavigating [true|false] --targetnpcs [true|false]</code></td>
<td>切换当玩家靠近时 NPC 是否会查看</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc mannequin</td>
<td><code>--hide_description [true|false] --immovable [true|false] --description [description] --main_hand [LEFT|RIGHT] --skin_patch_type [type] --skin_patch_body [location] --skin_patch_cape [location] --skin_patch_elytra [location]</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc metadata</td>
<td><code>set|get|remove [key] (value) (-t(emporary))</code></td>
<td>管理 NPC 元数据</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc minecart</td>
<td><code>(--offset offset)</code></td>
<td>设置矿车物品</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc mirror</td>
<td><code>--name [true|false] --equipment [true|false]</code></td>
<td>控制 NPC 皮肤等的镜像</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc model</td>
<td><code>[name]</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc modelanimate</td>
<td><code>[start|stop|clear] (name) (speed)</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc mount</td>
<td><code>(--onnpc &lt;npc id|uuid&gt;) (-d(ismount)) (-c(ancel))</code></td>
<td>安装可控NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc moveto</td>
<td><code>x:y:z:world | x y z world</code></td>
<td>将 NPC 传送到给定位置</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc mushroomcow</td>
<td><code>(--variant [variant])</code></td>
<td>设置蘑菇牛修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc name</td>
<td><code>(-h(over))</code></td>
<td>切换铭牌可见性，或仅在悬停时显示名称</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc ocelot</td>
<td><code>(--type type) (-s(itting), -n(ot sitting))</code></td>
<td>设置NPC的豹猫类型以及是否坐姿</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc owner</td>
<td><code>[uuid|SERVER]</code></td>
<td>设置 NPC 的所有者</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc packet</td>
<td><code>--enabled [true|false]</code></td>
<td>控制数据包 NPC 设置</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc painting</td>
<td><code>(--art art)</code></td>
<td>设置绘画修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc panda</td>
<td><code>--gene (main gene) --hiddengene (hidden gene) -e(ating) -s(itting) -n (sneezing) -r(olling)</code></td>
<td>设置熊猫修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc panimate</td>
<td><code>[animation]</code></td>
<td>播放玩家动画</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc parrot</td>
<td><code>(--variant variant)</code></td>
<td>设置鹦鹉修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc passive</td>
<td><code>(--set [true|false])</code></td>
<td>设置NPC是否损坏其他实体</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc path</td>
<td><code>None</code></td>
<td>切换航点编辑器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc pathopt</td>
<td><code>--avoid-teleporting [true|false] --avoid-water [true|false] --attack-delay-duration [duration] --destination-teleport-margin [margin] --open-doors [true|false] --path-range [range] --stationary-ticks [ticks] --attack-range [range] --distance-margin [margin] --path-distance-margin [margin] --pathfinder-type [CITIZENS|MINECRAFT] --falling-distance [distance]</code></td>
<td>设置 NPC 的寻路选项</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc pathto</td>
<td><code>me | here | cursor | [x] [y] [z] (--margin [distance margin]) (-s[traight line])</code></td>
<td>开始寻路到某个位置</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc pausepathfinding</td>
<td><code>--onrightclick [true|false] --when-player-within [range in blocks] --pauseduration [duration] --lockoutduration [duration]</code></td>
<td>设置寻路暂停</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc phantom</td>
<td><code>(--size size)</code></td>
<td>设置幻影修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc pickupitems</td>
<td><code>(--set [true|false])</code></td>
<td>允许NPC拾取物品</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc pig</td>
<td><code>(--variant variant)</code></td>
<td>管理猪修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc piglin</td>
<td><code>(--dancing [true|false])</code></td>
<td>设置 Piglin 修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc playerfilter</td>
<td><code>-a(llowlist) -e(mpty) -d(enylist) --add [uuid] --remove [uuid] --addpermission [permission] --removepermission [permission] --addgroup [group] --removegroup [group] -c(lear) --applywithin [blocks range]</code></td>
<td>管理 NPC 的玩家过滤器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc playerlist</td>
<td><code>(-a(dd),r(emove))</code></td>
<td>设置NPC是否放入播放列表</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc playsound</td>
<td><code>[sound] (category) (volume) (pitch) (--to [player]) (--at x:y:z:world)</code></td>
<td>在 NPC 的位置播放声音</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc polarbear</td>
<td><code>(-r)</code></td>
<td>设置北极熊修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc pose</td>
<td><code>(--save [name] (-d) | --mirror [name] (-d) | --assume [name] | --remove [name] | --default [name]) (--yaw yaw) (--pitch pitch) (-a)</code></td>
<td>管理 NPC 姿势</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc potioneffect</td>
<td><code>[add|remove|list] (--name [name] or -t for temporary) (--type [type]) (--duration [duration]) (--amplifier [amplifier]) (--icon [icon])</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc powered</td>
<td><code>(--set true|false)</code></td>
<td>将苦力怕 NPC 切换为动力状态</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc pufferfish</td>
<td><code>(--state state)</code></td>
<td>设置河豚修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc rabbittype</td>
<td><code>[type]</code></td>
<td>设置NPC的兔子类型</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc remove</td>
<td><code>(all|id|name| --owner [owner] | --eid [entity uuid] | --world [world])</code></td>
<td>删除 NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc rename</td>
<td><code>[name]</code></td>
<td>重命名 NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc respawn</td>
<td><code>[delay]</code></td>
<td>设置 NPC 的重生延迟</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc rotate</td>
<td><code>(--towards [x,y,z]) (--toentity [name|uuid|me]) (--body [yaw]) (--head [yaw]) (--pitch [pitch]) (-s(mooth))</code></td>
<td>旋转 NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc rotationsettings</td>
<td><code>[linear|immediate] (--link_body) (--head_only) (--max_pitch_per_tick) (--max_yaw_per_tick) (--pitch_range) (--yaw_range)</code></td>
<td>控制 NPC 的各种头部和身体旋转设置。目前 NPCs 使用简单的 Minecraft 式旋转，其中头部/身体每次刻度向目标移动一定的度数 接受以下标志： <strong>--link_body</strong>：头部和身体旋转是否应直接链接 <strong>--head_only</strong>：是否只有头部应该 <strong>--max_yaw_per_tick</strong>：每次改变偏航多少度刻度（默认为 40） <strong>--max_pitch_per_tick</strong>：每刻度改变俯仰角度多少度（默认为 10） <strong>--pitch_range</strong>：可能采取的俯仰范围（默认为 -180,180） <strong>--yaw_range</strong>：可能采取的偏航范围（默认为-180,180)</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc scaledmaxhealth</td>
<td><code>[health]</code></td>
<td>控制 NPC 的最大生命值，可以使用较大的数字。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc select</td>
<td><code>[id|name] (--range range) (--registry [name])</code></td>
<td>选择具有给定 ID 或名称的 NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc setequipment</td>
<td><code>(-c(osmetic)) [slot] [item]</code></td>
<td>通过命令设置设备</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc sheep</td>
<td><code>(--color [color]) (--sheared [sheared])</code></td>
<td>设置羊修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc shop</td>
<td><code>(edit|show|delete|copyfrom) (name) (new_name)</code></td>
<td>NPC 店铺编辑/展示</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc showshop</td>
<td><code>(name)</code></td>
<td>NPC 店铺展示</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc shulker</td>
<td><code>(--peek [peek] --color [color])</code></td>
<td>设置潜影贝修正值</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc sitting</td>
<td><code>(--explicit [true|false]) (--at [at])</code></td>
<td>设置 NPC 坐姿</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc skin</td>
<td><code>(-e(xport) -c(lear) -l(atest) -s(kull) -b(edrock)) [name] (or --url [url] --file [file] (-s(lim)) or -t [uuid/name] [data] [signature])</code></td>
<td>设置 NPC 的皮肤名称。使用 -l 设置皮肤始终更新到最新</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc skinlayers</td>
<td><code>(--cape [true|false]) (--hat [true|false]) (--jacket [true|false]) (--sleeves [true|false]) (--pants [true|false])</code></td>
<td>设置 NPC 的皮肤层可见性</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc slimesize</td>
<td><code>[size]</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc sniffer</td>
<td><code>(--state [state])</code></td>
<td>设置嗅探器修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc snowman</td>
<td><code>(-d[erp]) (-f[orm snow])</code></td>
<td>设置雪人修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc sound</td>
<td><code>(--death [death sound|d]) (--ambient [ambient sound|d]) (--hurt [hurt sound|d]) (-n(one)/-s(ilent)) (-d(efault))</code></td>
<td>设置 NPC 的播放声音</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc spawn</td>
<td><code>(id|name) -l(oad chunks)</code></td>
<td>生成现有的 NPC</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc speak</td>
<td><code>[message] --bubble [duration] --target [npcid|player name] --range (range to look for entities to speak to in blocks)</code></td>
<td>说来自 NPC 的消息</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc spectate</td>
<td><code>(-r(eset))</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc speed</td>
<td><code>[speed]</code></td>
<td>将 NPC 的移动速度设置为百分比</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc spellcaster</td>
<td><code>(--spell spell)</code></td>
<td>设置施法者修正值</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc swim</td>
<td><code>(--set [true|false])</code></td>
<td>设置 NPC 是否游泳</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc target</td>
<td><code>[name|UUID] (-a[ggressive]) (-c[ancel])</code></td>
<td>定位给定实体</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc targetable</td>
<td><code>None</code></td>
<td>切换 NPC 的目标能力</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc text</td>
<td><code>None</code></td>
<td>切换文本编辑器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc textdisplay</td>
<td><code>--shadowed [true|false] --seethrough [true|false] --line_width [width] --text [text]</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc tp</td>
<td><code>(-e(xact))</code></td>
<td>传送到 NPC 前面</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc tphere</td>
<td><code>(cursor) -c(enter) -f(ront)</code></td>
<td>将 NPC 传送到您所在的位置</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc tpto</td>
<td><code>[player name|npc id] [player name|npc id]</code></td>
<td>将一个 NPC 或玩家传送到另一个 NPC 或玩家</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc trackingrange</td>
<td><code>[range]</code></td>
<td>设置跟踪范围</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc tropicalfish</td>
<td><code>(--body color) (--pattern pattern) (--patterncolor color)</code></td>
<td>设置热带鱼修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc type</td>
<td><code>[type]</code></td>
<td>设置 NPC 的实体类型</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc undo</td>
<td><code>(all)</code></td>
<td>撤消上一个操作（当前仅支持创建/删除）</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc useitem</td>
<td><code>(-o(ffhand))</code></td>
<td>设置 NPC 使用其持有的物品</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc vex</td>
<td><code>(--charging [charging])</code></td>
<td>设置 vex 修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc villager</td>
<td><code>(--level level) (--type type) (--profession profession) -s(hake head)</code></td>
<td>设置村民修正值</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc vulnerable</td>
<td><code>(-t(emporary))</code></td>
<td>切换 NPC 的漏洞</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc wander</td>
<td><code>(add x y z world) | (worldguardregion [region]) | (xyrange [xrange] [yrange])</code></td>
<td>设置 NPC 四处徘徊</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc warden</td>
<td><code>dig|emerge|roar|anger [entity uuid/player name] [anger]</code></td>
<td>设置典狱长修改器</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc wither</td>
<td><code>(--invulnerable [true|false]) (--invulnerable-ticks [ticks]) (--arrow-shield [true|false])</code></td>
<td>设置凋零修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc wolf</td>
<td><code>(-s(itting) a(ngry) t(amed) i(nterested)) --collar [hex rgb color|name] --variant [variant]</code></td>
<td>设置狼修饰符</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/trait</td>
<td><code>[trait1] [trait2] ... [traitN]</code> - <a href="characters.md" title="Characters">特征</a> 申请列表</td>
<td>将 <a href="characters.md" title="Characters">特征类型</a> 添加到 NPC。 NPCs 可以具有多个特征。示例：<code>/trait sentinel</code></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<a id="Denizen-added_commands"></a><h2 id="denizen-added-commands">Denizen-添加的命令</h2>
<p>以下 <code>/npc</code> 命令是由 <a href="https://denizenscript.com/">Denizen</a> 添加的（从 <code>/npc help</code> 复制而来）。
<a href="https://guide.denizenscript.com/guides/background/download-denizen.html">Denizen 可以从这里下载。</a></p>
<table>
<thead>
<tr>
<th><strong>Denizen /NPC 命令</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Command</td>
<td>论点</td>
<td>描述</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc mirrorskin</td>
<td>无</td>
<td>使 NPC 镜像看着它的玩家的皮肤。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc mirrorname</td>
<td>无</td>
<td>使 NPC 镜像看着它的玩家的名字。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc mirrorequip</td>
<td>无</td>
<td>使 NPC 镜像看着它的玩家的装备。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc stand</td>
<td>无</td>
<td>制作 NPC 支架。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc pushable</td>
<td><em>-t (-r) (--延迟 #)</em></td>
<td>使 NPC 可推动。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc constant</td>
<td><em>--设置/删除名称 --value 常量值</em></td>
<td>查看/添加/删除 NPC 字符串常量。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc assignment</td>
<td><em>--设置分配名称 (-r)</em></td>
<td>控制 NPC 的分配。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc trigger</td>
<td><em>[触发器名称] [(--冷却时间[秒])/(--半径[半径])/(-t)]</em></td>
<td>控制 NPC 的各种触发器。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc nickname</td>
<td><em>[--设置昵称]</em></td>
<td>为 NPC 提供一个昵称，与 Denizen 兼容的语音引擎一起使用。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc sit</td>
<td><em>(--位置 x,y,z,世界) (--anchor 锚点名称) (-c)</em></td>
<td>让 NPC 坐下。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc sleep</td>
<td><em>(--位置 x,y,z,世界) (--anchor 锚点名称)</em></td>
<td>使 NPC 休眠。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc sneak</td>
<td>无</td>
<td>使 NPC 蹲下。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc wakeup</td>
<td>无</td>
<td>使 NPC 唤醒。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc fish</td>
<td><em>(--位置 x,y,z,世界) (--anchor 锚点名称) (-c)</em></td>
<td>制作 NPC 鱼，在给定位置抛投。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc stopfishing</td>
<td>无</td>
<td>使NPC停止钓鱼。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc invisible</td>
<td>无</td>
<td>将 NPC 隐藏起来。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/npc health</td>
<td><em>--设置#（-r）</em></td>
<td>设置 NPC 的最大运行状况。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<a id="Waypoint_commands"></a><h2 id="waypoint-commands">航点命令</h2>
<p>权限的格式为“citizens.waypoints.xx”，例如“disableteleport”命令的“citizens.waypoints.disableteleport”。</p>
<table>
<thead>
<tr>
<th><strong>航点命令</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Command</td>
<td>论点</td>
<td>描述</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/waypoints add</td>
<td><code>[x] [y] [z] (world) (--index idx)</code></td>
<td>在某个点添加航路点</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/waypoints disableteleport</td>
<td><code>disableteleport</code></td>
<td>卡住时禁用传送</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/waypoints hpa</td>
<td><code>hpa</code></td>
<td>无</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/waypoints provider</td>
<td><code>[provider name]</code></td>
<td>设置当前航路点提供者</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/waypoints remove</td>
<td><code>(x y z world) (--index idx)</code></td>
<td>在某个点添加航路点</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<a id="Template_commands"></a><h2 id="template-commands">模板命令</h2>
<table>
<thead>
<tr>
<th><strong>模板命令</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Command</td>
<td>论点</td>
<td>权限</td>
<td>描述</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/template apply</td>
<td><code>(template namespace:)[template name]</code></td>
<td>citizens.templates.apply</td>
<td>将模板应用于选定的 NPC</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/template generate</td>
<td><code>(template namespace:)[name]</code></td>
<td>citizens.templates.generate</td>
<td>从选定的 NPC 生成模板</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/template list</td>
<td><code>list</code></td>
<td>citizens.templates.list</td>
<td>列出可用模板</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<a id="See_Also"></a><h2 id="see-also">另请参阅</h2>
<p><a href="characters.md" title="Characters">角色类型</a></p>
<p><a href="text-syntax.md" title="Text Syntax">文本语法</a></p>
<p><a href="waypoints.md" title="Waypoints">路径点</a></p>
<table>
<thead>
<tr>
<th>快速导航</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="category-usage.md" title="Category:Usage">用途</a></td>
<td><a href="installation.md" title="Installation">安装</a> · <a href="frequently-asked-questions.md" title="Frequently Asked Questions">常见问题</a> · 命令 · <a href="editors.md" title="Editors">编辑器</a> · <a href="characters.md" title="Characters">角色类型</a> · <a href="https://wiki.citizensnpcs.co/API" title="API">API</a> ·</td>
</tr>
<tr>
<td><a href="category-configuration.md" title="Category:Configuration">配置</a></td>
<td><a href="configuration.md" title="Configuration">配置</a>  · <a href="text-syntax.md" title="Text Syntax">文本语法</a>  · <a href="permissions.md" title="Permissions">权限</a>  · <a href="waypoints.md" title="Waypoints">路径点</a>  · <a href="data-storage.md" title="Data Storage">数据存储</a></td>
</tr>
</tbody>
</table>

