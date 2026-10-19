---
title: Denizen / 0.7 / 交互脚本 / 自定义命令
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scritps/Custom_Commands
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5392
---


<a id="top"></a>

# Denizen / 0.7 / 交互脚本 / 自定义命令

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<a id="Custom_Commands"></a><h2 id="custom-commands">自定义命令</h2>
<p>Denizen是可扩展的！除了触发器、活动和即将推出的要求之外，还提供了 API 来帮助您在项目中制作自定义脚本命令！对命令有一个好主意吗？有更好的方法来打击玩家吗？ （MEGASTRIKE 命令，有人吗？）</p>
<p>继续阅读！</p>
<a id="YourCommand_extends_AbstractCommand"></a><h2 id="yourcommand-extends-abstractcommand">YourCommand 扩展 AbstractCommand</h2>
<p>您需要的第一件事是扩展 Denizen AbstractCommand 的自定义命令类。这包含在执行命令时调用的方法。这称为每次脚本包含您的命令时。</p>
<a id="Example_Command"></a><h4 id="example-command">命令示例</h4>
<p>有时，最简单的工作方法就是查看实际示例。 <a href="http://pastie.org/4369453">在 Pastie.org 上查看 STRIKE 命令的副本</a> 是一个非常简单的命令，或者查看下面的代码。如需更多示例，您可以随时查看 <a href="https://github.com/aufdemrand/Denizen/tree/master/src/main/java/net/aufdemrand/denizen/commands/core">核心 Denizen 命令</a>。</p>
<table>
<thead>
<tr>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Code:</strong> 罢工 Denizen 命令</td>
</tr>
<tr>
<td>[位置书签]</td>
</tr>
</tbody>
</table>
<a id="Command_Template"></a><h4 id="command-template">命令模板</h4>
<p>下面是一个命令模板副本，用于复制/粘贴自定义 denizen 命令的骨架。</p>
<table>
<thead>
<tr>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Code:</strong> Denizen 命令模板</td>
</tr>
<tr>
<td>{{{2}}}</td>
</tr>
</tbody>
</table>
<a id="The_ScriptEntry_object"></a><h3 id="the-scriptentry-object">ScriptEntry 对象</h3>
<p>当 Denizen 读取脚本时，每一行都会变成一个 SciptEntry 对象，其中包含命令、参数以及各种其他数据和对象，如下所述。您的命令是此 AbstractCommand 类的扩展，每次调用您的命令来执行时，都会执行该类并处理 ScriptEntry。当然，您的 Command 如何使用 ScriptEntry 信息取决于您。</p>
<p>Denizen ScriptEngine 和执行器构造 ScriptEntry 并使用可在命令中使用的信息填充 ScriptEntry。下面是您可以针对发送到命令执行方法的 scriptEntry 使用的方法列表。</p>
<p><a href="https://wiki.citizensnpcs.co/index.php?title=Template:DenizenCommand&amp;action=edit&amp;redlink=1" title="Template:DenizenCommand (page does not exist)">Template:DenizenCommand</a></p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>参数()</td>
<td>脚本中使用的参数的 String[] 值</td>
</tr>
<tr>
<td>这是 Denizen 的 argBuilder 方法的输出。它将命令参数用空格和引号分开。例如：<code>arg1 arg2 'this is argument 3' "and that's argument 4"</code> 将返回一个大小为 4 的字符串数组。注意参数 4，它使用单引号处理参数。提示：参数用双引号括起来，反之亦然。</td>
<td></td>
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
<td>发送队列()</td>
<td>QueueType 为 QueueType.TRIGGER、QueueType.TASK 或 QueueType.ACTIVITY</td>
</tr>
<tr>
<td>Denizen 的脚本引擎包含一个名为 runQeues 的方法，该方法将 ScriptEntries 发送到执行器。在此过程中，它存储从哪个队列调用命令。可用于高级情况。通常，如果由交互脚本调用，则包含 QueueType.TRIGGER。</td>
<td></td>
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
<td>获取脚本()</td>
<td>脚本名称的字符串值</td>
</tr>
<tr>
<td>如果存储有关脚本的信息可能很有用。例如，如果参数中没有另外指示脚本，Denizen 的 FINISH 命令会认为此信息是理所当然的。</td>
<td></td>
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
<td>获取步骤()</td>
<td>脚本步骤的整数值</td>
</tr>
<tr>
<td>可以与 getScript() 类似地使用。 ZAP 命令使用此信息来了解要继续执行哪个步骤。</td>
<td></td>
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
<td>获取玩家()</td>
<td>脚本触发器的玩家对象</td>
</tr>
<tr>
<td>非常简单。 bukkit Player 对象可以获取有关玩家的各种信息。</td>
<td></td>
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
<td>getDenizen()</td>
<td>脚本触发者的 DenizenNPC 对象</td>
</tr>
<tr>
<td>DenizenNPC 可以轻松地与已交互的 Denizen 进行合作。好的 例如： LOOK 命令。</td>
<td></td>
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
<td>获取启动时间()</td>
<td>System.currentTimeMillis() 的长值</td>
</tr>
<tr>
<td>包含系统时间的 <code>Long System.currentTimeMillis()</code>，该时间被发送到您的命令进行处理，您可以使用它进行检查。</td>
<td></td>
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
<td>设置延迟时间()</td>
<td>应为 System.currentTimeMillis() 格式的 Long 值</td>
</tr>
<tr>
<td>高级用法。有关示例，请参阅 DELAY 命令。</td>
<td></td>
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
<td>获取延迟时间()</td>
<td>使用 setDelayedTime() 设置的长值</td>
</tr>
<tr>
<td>高级用法。再次参见 DELAY 命令的示例。如果没有使用 setDelayedTime() 设置，则默认为 null。</td>
<td></td>
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
<td>获取文本()</td>
<td>触发器发送的文本的 String[2]</td>
</tr>
<tr>
<td>Vanilla Denizen 将使用它来存储发送到聊天触发器或从聊天触发器发送的信息。元素 [0] 包含触发脚本时玩家输入的文本，元素 [1] 包含脚本的 Trigger: 节点中设置的文本。</td>
<td></td>
</tr>
</tbody>
</table>
<a id="Registering_your_command"></a><h2 id="registering-your-command">注册您的命令</h2>
<p>为了让 Denizen 使用您的命令，需要注册它。这可能可以在插件的 onEnable() 方法中完成。</p>
<a id="Example_code"></a><h4 id="example-code">示例代码</h4>
<table>
<thead>
<tr>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Code:</strong> 用于注册 Denizen 命令的示例代码</td>
</tr>
<tr>
<td>{{{2}}}</td>
</tr>
</tbody>
</table>

