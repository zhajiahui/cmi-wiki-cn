---
title: Denizen 更新日志
source_url: https://wiki.citizensnpcs.co/Denizen_changelog
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5400
---


<a id="top"></a>

# Denizen 更新日志

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><strong>0.5.3 构建 #60</strong></p>
<ul>
<li>PlayerQue 现在使用 ConcurrentHashMap 来避免 ConcurrentModificationException。 （谢谢你！）</li>
<li><code>/denizen reload</code> 和 <code>/denizen save</code> 现在可以在控制台中使用。</li>
<li>检查interact_delay_in_ticks = 0并将其更改为1。（感谢Sparta！）不过，将其保持在至少10可能是个好主意。</li>
</ul>
<p><strong>0.5.3 构建#56</strong></p>
<ul>
<li>添加了失败命令。将脚本设置为“失败”以检查要求。注意：脚本仍然可以失败和完成，它们是分开的。</li>
<li>添加了“失败”要求。使用 FAILED [脚本名称]。请记住：脚本名称区分大小写！</li>
<li>添加了 RESET 命令。这可用于重置脚本的 FAILED 或 FINISHED 状态。使用 RESET FAILED|FINISHED [脚本名称]。</li>
<li>在 /denizen 帮助中添加了小警告，指出其中列出的许多命令尚未运行 - 这是测试版，朋友们，我正在研究它们：P</li>
<li>记录 /denizen adddata|decdata|getdata。实际上与 Denizens 无关，但可以方便地检查/切换块数据。在树上尝试一下。</li>
<li>修复了 WAIT 命令。现在它实际上按预期工作了。</li>
</ul>
<p><strong>0.5.3 构建 #48</strong></p>
<ul>
<li>LOOK 命令的扩展使用。现在可以指定位置书签来设置 Denizen 的俯仰和偏航。注意：制作位置书签时，您的俯仰和偏航将与您的 XYZ 位置一起记录。使用：查看[位置书签]。现有的参数 CLOSE 和 AWAY 仍然有效。附加 note: LOOK CLOSE 将覆盖设置的俯仰/偏航，因此请确保事先使用 LOOK AWAY，或者确保未启用 LOOK CLOSE。</li>
<li>修复了 RESPAWN 命令的问题。</li>
<li>修复了与彼此亲近的居民交谈的问题。玩家现在只能与最接近的 Denizen 交谈。</li>
<li>添加了 TELEPORT 命令以将玩家传送到 Denizen 的位置书签。使用 TELEPORT [位置书签]。</li>
<li>添加了 REFUSE 命令以获取玩家的许可。使用拒绝[name.of.permission.node]。</li>
</ul>
<p>建议您使用最新版本的 C2。</p>
<p><strong>0.5.3 构建#42</strong></p>
<ul>
<li>SWITCH 现在激活红石。对那些人感到抱歉。</li>
<li>添加了 WAIT 命令。</li>
<li>添加了 SPAWN 命令。</li>
<li>其他代码优化/清理。</li>
</ul>
<p>非常感谢 #citizens 中辛勤工作的 Beta 测试人员！谢谢你！</p>
<p><strong>0.5.3 构建 #25</strong></p>
<ul>
<li>NARRATE 命令现在可以正确替换 &lt;NPC&gt;。</li>
<li>Denizens 不再要求您成为 NPC 的所有者才能使用命令。</li>
<li>调整多行引擎以适应超长名称。</li>
<li>ZAP 现在使用 getName 而不是 getDisplayName（如果这会导致当前进度出现问题，抱歉。）</li>
</ul>
<p><strong>0.5.3 阿尔法</strong></p>
<ul>
<li>添加了 SWITCH 命令。居民现在可以翻转杠杆！</li>
<li>将 Denizen 项目添加到 <a href="http://ci.citizensnpcs.net/job/Denizen/">Citizens 詹金斯</a>！</li>
</ul>
<p><strong>0.5.2 阿尔法：</strong></p>
<ul>
<li>固定要求穿着和时间。注意：PermissionsBukkit 用户仍然遇到 GROUP 问题。</li>
<li>添加了 FOLLOW、TAKE、NARRATE 和 CAST 命令。</li>
</ul>
<p>更新比我计划的要小，敬请期待更多！</p>
<p><strong>0.5.1 阿尔法：</strong></p>
<ul>
<li>固定要求...它们现在应该都可以工作，除了尚未测试可能具有结界的要求。</li>
<li>添加了为居民提供“位置书签”的功能。使用 /denizen 书签位置 [名称]。</li>
<li>添加了 WALKTO、PERMISS、FINISH、RESPAWN、WEATHER 和 EXECUTE 命令。</li>
<li>开始充实 /denizen 帮助</li>
<li>添加了活动调度程序。</li>
</ul>

