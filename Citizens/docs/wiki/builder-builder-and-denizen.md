---
title: Builder / Builder 与 Denizen
source_url: https://wiki.citizensnpcs.co/Builder/Builder_and_Denizen
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4764
---


<a id="top"></a>

# Builder / Builder 与 Denizen

<p>结合 Denizen 和 Builder 执行的操作示例</p>
<a id="Continuous_Rebuilding"></a><h2 id="continuous-rebuilding">持续重建</h2>
<p>如果您希望构建器看起来很忙碌并不断重建和销毁结构文件，您可以使用这样的设置。</p>
<p>在 denizen 脚本文件夹中的任何 yml 文件中创建一个任务脚本，如下所示。</p>
<div class="highlight"><pre>---- script.yml ----
Rebuild:
  Type: Task
  Script:
    - execute as_npc "builder &lt;npc.id&gt; build excavate oncomplete:Rebuild"
</pre></div>
<p>现在创建一个构建器，加载所需的结构文件，设置原点，然后调用 <em>/builder build oncomplete:Rebuild</em></p>
<p>构建器将构建结构文件，然后运行任务，该任务将使用 <em>挖掘</em> 选项再次构建它，该选项将首先将其拆除，并且循环将永远持续下去。</p>
<p>您可以将此脚本用于任意数量的构建器/结构文件，而无需进行任何更改。</p>

