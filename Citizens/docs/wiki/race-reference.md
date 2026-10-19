---
title: 种族参考
source_url: https://wiki.citizensnpcs.co/Race_Reference
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4679
---


<a id="top"></a>

# 种族参考

<a id="Creating_a_Race"></a><h2 id="creating-a-race">创造一场比赛</h2>
<p>比赛文件夹需要进入[服务器文件夹]/plugins/Adventures/races/YourRaceHere。
每场比赛都需要一个描述符或一个文件来告诉 Adventures 为您的比赛加载什么。这将是 info.yml OR info.js OR info.extension，其中扩展是嵌入式 Java 脚本语言，例如 Jython 或 JRuby。</p>
<p>如果信息文件使用脚本语言，则根命名空间中需要有一个 getDescriptor() 方法，该方法返回 net.citizensnpcs.adventures.race.RaceDescriptor 的实例。</p>
<a id="YAML_Info_File_Structure"></a><h2 id="yaml-info-file-structure">YAML 信息文件结构</h2>
<p>示例 YAML 文件显示所有当前可用的 keys:</p>
<div class="highlight"><pre>name: Name # required
tribe:
     max-size: 10 # required
     behavior: # optional, a behavior root node (explained later)
members:
     names: # required, a list of possible names for new members to have, picked at random
         0: Bob
         1: SirBob
         2: Bob2
     types: # required, a list of possible entity types for new members to have, picked at random
         0: CREEPER
     behavior: # optional, a behavior root node (explained later)
dialog:
     allowed-rules: rule1, filename1 # comma-separated list of rules to allow (can be per-rule or per-file). Leave empty for all rules allowed.
</pre></div>
<p>行为根节点对于部落来说很重要。它们被定义为 <em>决策树</em> 行为，是 NPC 的单个工作单元。树是一种组织数据的方式，看起来类似于倒置的树。如需简单说明，请查看 <a href="https://monk.library.illinois.edu/cic/public/analytics/decision_tree.png">这里</a>。 NPC 的 AI 将从顶部开始，逐步形成一种行为。</p>
<p>共有三种流结构有助于行为流：序列、选择器和装饰器。序列只是逐一执行列表中的每个行为，直到它们全部完成。选择器根据某种策略从列表中选择一个或多个行为，例如随机选择或基于优先级的选择。装饰器 <em>包裹</em> 不知道它做什么的另一种行为，例如在一段时间后停止它，或者反转它的响应，或者在它完成之前/之后做一些事情。</p>
<p>最后，我们有边缘节点，它们是用户定义的，并与 NPC 一起实际工作。这是一个非常强大的构造，允许出现复杂的行为。</p>
<p>我们在 YAML 中定义它，就像 so: 一样</p>
<div class="highlight"><pre>behavior:
    sequence: # builds a sequence
        sub: # omitted
    sequence -r: # builds a sequence which retries children if they fail until the sequence is complete
    selector: # builds a random selector
        sub: # omitted
        sub2: # omitted
    selector -r: # retries children if they fail until a successful behavior completes
    selector -p: # prioritises children
    js filename: "" # loads a javascript goal at the file location under your race folder and invokes the getBehavior(Tribe, DataKey) function on it to get a Behavior instance.
    your.package.name.ClassName: # loads the class at the given package and instantiates it to get a Behavior instance. Must have a 0-argument constructor (note that @Persist annotations from CitizensAPI will work for loading extra data).
</pre></div>

