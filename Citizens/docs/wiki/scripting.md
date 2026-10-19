---
title: 脚本
source_url: https://wiki.citizensnpcs.co/Scripting
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5404
---


<a id="top"></a>

# 脚本

<a id="NOTICE"></a><h2 id="notice">通知</h2>
<p>此页面指的是不再完全支持的旧版 Javascript 脚本。现代 Citizens 中提供的主要脚本支持是通过 <a href="https://denizenscript.com/">Denizen</a> 实现的。</p>
<a id="Scripting_Support_in_Citizens2"></a><h2 id="scripting-support-in-citizens2">Citizens2 中的脚本支持</h2>
<p>Citizens2 支持各种脚本语言，包括 Lua、Javascript 和 Python。</p>
<p>Java 内置 Javascript 支持；可以通过安装 JRuby (<a href="http://jruby.org/">http://jruby.org/</a>)、Jython (<a href="http://www.jython.org/">http://www.jython.org/</a>)、Kahlua (<a href="https://github.com/krka/kahlua2">https://github.com/krka/kahlua2</a>) 等来添加其他语言。</p>
<p>脚本 API 在全局命名空间中包含一些内置对象，这些对象有助于执行某些任务。目前，“事件”对象允许注册 Bukkit 事件的事件侦听器，并且在“插件”下提供了对 Citizens 插件对象的引用。</p>
<a id="Behaviours"></a><h2 id="behaviours">行为</h2>
<p>让我们看一个如何使用脚本的示例。可以通过/npc script --add [scripts]命令将脚本添加到NPC，其中scripts是plugins/Citizens/scripts文件夹中要使用的文件列表。脚本通过其扩展名来区分——确保它是正确的！</p>
<p>当Citizens加载脚本文件时，它将调用方法'onLoad(NPC)' - 此时可以执行任何操作，尽管NPC不一定会被生成。如果方法“run(NPC)”存在，它也会被 Citizens 在每个时钟周期调用。</p>
<div class="highlight"><pre>   function leftClick(event) {
       event.getClicker().sendMessage("hello from Javascript scripting!");
   }
</pre></div>
<div class="highlight"><pre>   function onLoad(npc) {
       events.on(Java.type('net.citizensnpcs.api.event.NPCLeftClickEvent').class, leftClick);
   }
</pre></div>
<a id="Scripting_Gotchas_and_Tips"></a><h2 id="scripting-gotchas-and-tips">脚本编写陷阱和技巧</h2>
<a id="Javascript_(Nashorn)"></a><h3 id="javascript-nashorn">JavaScript (Nashorn)</h3>
<ul>
<li>Nashorn 是一个更快的 Javascript 引擎，仅包含在 Java 7 及更高版本中。建议在较旧的 Rhino 引擎上运行它。</li>
<li>有关 Java-Javascript 连接的更多信息，请阅读 <a href="https://docs.oracle.com/javase/8/docs/technotes/guides/scripting/nashorn/api.html">https://docs.oracle.com/javase/8/docs/technotes/guides/scripting/nashorn/api.html</a>。</li>
</ul>
<a id="Javascript_(Rhino)"></a><h3 id="javascript-rhino">JavaScript（犀牛）</h3>
<ul>
<li>一些代码期望实现 equals 和 hashcode 方法 - 应经常使用简单的 equals 函数。</li>
<li>for..in 循环不适用于 Java 集合。</li>
<li>Rhino 不能使用抽象类。</li>
<li>您可以使用新的 <code>[interfacename](object)</code> 来实现 Java 接口，其中对象包含实现该接口的方法。</li>
<li>使用 importPackage(Packages.name.space) 或 importClass(Packages.name.space.YourClass) 导入其他类/包。包裹。如果该类位于 java.util 包中，则不需要前缀。</li>
</ul>

