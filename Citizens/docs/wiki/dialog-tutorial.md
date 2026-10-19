---
title: 对话教程
source_url: https://wiki.citizensnpcs.co/Dialog_Tutorial
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4319
---


<a id="top"></a>

# 对话教程

<p>在本教程中，您将学习对话系统语法的基础知识以及所涉及的概念。</p>
<a id="Overview"></a><h2 id="overview">概述</h2>
<p>首先，我们看一下对话框程序的基本流程。 Minecraft的世界可以分解为一系列<em>事件</em>。这些事情包括谈话、战斗、破坏方块等等。一般流程看起来有点像这样：事件 -&gt; 侦听器。这并不容易用文本来表示。我们如何利用这个来创建一个好的系统？</p>
<p>答案非常简单：将事件视为一系列事实，例如参与的玩家、他们的名字等等。每个事实都有一个名称或 <em>钥匙</em> 和一个值，例如。玩家的名字可能有一个键 "name" 和一个值 "fullwall"。事件只是关于所发生事件的大量事实。这使得在文本中推理变得更加容易。</p>
<p>这种方法还可以轻松地将更多事实与事件关联起来；这组事实被称为 <em>查询</em>。查询还可以包含有关世界状态、NPC 拾取的任何内存等信息。</p>
<p>现在我们已经收集了很多事实 - 我们该如何处理它们呢？是时候介绍两个新概念了：<em>规则</em> 和 <em>回应</em>。最终流程如下：事件 -&gt; NPC -&gt; 生成事实 -&gt; 对话系统 -&gt; 规则。</p>
<a id="Rules"></a><h2 id="rules">规则</h2>
<p>规则接受查询并根据条件列表对其进行检查。如果匹配，它就会做某事。例如，在聊天事件中，它可能会检查玩家的名字是否为“fullwall”，然后说“Hello，fullwall！”给玩家。规则很简单，但可以组合起来创建复杂的交互。</p>
<a id="Responses"></a><h2 id="responses">回应</h2>
<p>响应基本上是一个命令列表；它没有标准，但可以从许多不同类型的规则中调用。</p>
<a id="Writing_a_Rule"></a><h2 id="writing-a-rule">编写规则</h2>
<p>让我们来看看语法。在继续之前，请确保您已下载并安装 Adventures。任何使用对话系统的 NPC 都需要具有对话特征，因此在尝试任何这些示例之前请使用 /traitdialog。</p>
<p>这是一个示例规则；一点也不过分。</p>
<div class="highlight"><pre>rule example {
    criteria events=any;
}
</pre></div>
<p>这是编写规则所需的绝对最低限度。我们有关键字“rule”，后跟规则名称和 { 字符。 { 和 } 字符标记冒险的开始和结束。
接下来，我们有一个“标准”声明。这告诉 Adventures 规则正在侦听哪些事件以及它检查的标准。</p>
<div class="highlight"><pre>criteria events="any";
                ^ matches any kind of event, as a demonstration
</pre></div>
<p>请注意条件语句后面的分号 (';') - 规则中的每一行都应以其中之一结尾。
您还可以有多个事件，以 commas: 分隔</p>
<div class="highlight"><pre>criteria events=onchat, ondamage;
</pre></div>
<p>在我们继续讨论更高级的条件示例之前，让我们回顾一下对话框中不同类型的值。请注意，“any”用引号引起来 - 这意味着该值应被视为文本块。</p>
<div class="highlight"><pre>100 - a number
"100" - text containing the characters 100
"text" - text
true/false - yes or no value
$sender.location.x - value is taken from the query fact "sender.location.x"
"${sender.name}" - value is text containing the fact under sender.name
</pre></div>
<p>现在，仅仅匹配事件的标准是毫无意义的。您还可以从查询中检查事实。假设我们只想在 NPC 位于 x=100 时匹配规则。</p>
<div class="highlight"><pre>criteria events="any" $npc.location.x=100;
</pre></div>
<p>当 y 低于 50 时怎么办？</p>
<div class="highlight"><pre>criteria events="any" $npc.location.x=100, $npc.location.y&lt;50;
</pre></div>
<p>匹配一个以h开头的聊天规则怎么样？ （note: 这使用正则表达式）</p>
<div class="highlight"><pre>criteria events="onchat" $message~=/h[a-zA-Z]+/
</pre></div>
<a id="Writing_a_Response"></a><h2 id="writing-a-response">写回应</h2>
<p>请注意，本节中使用的许多语句都可以在规则中使用，但将逻辑分离为响应可能会有所帮助。</p>
<p>响应的编写方式很像没有标准声明的规则。</p>
<div class="highlight"><pre>response example {
}
</pre></div>
<p>我们将这个响应称为规则。</p>
<div class="highlight"><pre>rule example {
    criteria events="any";
    response example;
}
</pre></div>
<a id="Writing_a_full_Dialog"></a><h2 id="writing-a-full-dialog">编写完整的对话框</h2>
<p>让我们看一个经典的“Hello”示例。当玩家说“嗨！”时我们想回复“你好，（名字）！”。</p>
<p>将以下文本复制并粘贴到plugins/Adventures/dialog 文件夹内的新文件“Hello.txt”中。</p>
<div class="highlight"><pre>rule saidHi {
    criteria events=onchat $message="Hi!";
    response sayHi;
}
response sayHi {
    say message:"Hello, ${sender.name}!", target:$sender;
}
</pre></div>

