---
title: 对话参考
source_url: https://wiki.citizensnpcs.co/Dialog_Reference
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5005
---


<a id="top"></a>

# 对话参考

<a id="Syntax"></a><h2 id="syntax">语法</h2>
<a id="Values"></a><h3 id="values">价值观</h3>
<div class="highlight"><pre>10, 1.02, 123 - number
"test" - text
"${message}" - text with query value inside
$message - query value
[10, 12, 12...] - list of values
{"key" : value, "key2" : value...} - dictionary
</pre></div>
<a id="Rule_syntax"></a><h3 id="rule-syntax">规则语法</h3>
<div class="highlight"><pre>rule rulename {
   criteria events="any"...;
   // statements here
}
</pre></div>
<a id="Statement_syntax"></a><h3 id="statement-syntax">语句语法</h3>
<div class="highlight"><pre>rule example {
    // criteria
    say "example", $sender; // arguments can be without names
    say message:"example", target:$sender; // or all named to prevent ambiguity
    say "example", target:$sender; // or only some named
}
</pre></div>
<a id="Random_syntax"></a><h3 id="random-syntax">随机语法</h3>
<div class="highlight"><pre>response example {
    random {
        say "Hi", "p:fullwall" : 0.5;
        say "Hi2", "p:fullwall" : 0.3;
    }
}
</pre></div>
<p>检查每个语句的给定概率；如果检查失败，则继续进行下一项检查。一旦成功检查，该语句就会被执行，并且不再检查。</p>
<a id="Events"></a><h2 id="events">活动</h2>
<a id="Standard_variables_available"></a><h5 id="standard-variables-available">可用的标准变量</h5>
<ul>
<li><em>某个根名称下的实体</em></li>
</ul>
<div class="highlight"><pre>root.health : entity's current health
root.maxhealth : entity's max health
root.type : entity type
root.location.x : x 
root.location.y : y 
root.location.z : z 
root.location.pitch : pitch 
root.location.yaw : yaw 
root.location.world : world
</pre></div>
<ul>
<li><em>某个根名称下的玩家</em></li>
</ul>
<div class="highlight"><pre>root.name : name
</pre></div>
<h5 id="onchat">聊天</h5>
<div class="highlight"><pre>message : the message involved in the event
sender : the sender
</pre></div>
<a id="Statements"></a><h2 id="statements">声明</h2>
<ul>
<li>[] - 必需参数</li>
<li>() - 可选参数</li>
<li>... - 重复论证</li>
<li>可以在没有显式键的情况下给出参数，并将按照必需参数和可选参数的顺序进行解析。</li>
</ul>
<a id="Remember"></a><h5 id="remember">记住</h5>
<div class="highlight"><pre>remember [$fact:value (10ns|ms|s|m|h|d (expiration time)) (-p (persistent)), ($fact2:value ...)];
</pre></div>
<a id="Forget"></a><h5 id="forget">忘记</h5>
<div class="highlight"><pre>forget [memory:"factname" | ["factname1", "factname2"...]];
</pre></div>
<a id="Say"></a><h5 id="say">说</h5>
<div class="highlight"><pre>say [message:"message"], [target:"p:playername"|"n:npcid"|"broadcast"|"log"|fact of type 'Player'];
</pre></div>
<a id="Code"></a><h5 id="code">代码</h5>
<div class="highlight"><pre>java|js|py|lua|rb|clj|scala [code:"code"]
</pre></div>
<p>根据输入评估原始代码。注意：JS 内置于 Java 中，但所有其他都需要额外的程序。例如。 rb需要安装JRuby，scala需要安装scala等。
Java 评估是在匿名可运行类的 run() 方法中完成的。仅 org.bukkit 导入可以不加前缀；如果您希望自动导入更多内容，请发送消息 fullwall。</p>
<a id="Denizen_Script"></a><h5 id="denizen-script">Denizen 脚本</h5>
<div class="highlight"><pre>dtask [name:"script name"], [player:query player | "playername"], (denizen:query NPC or Denizen | "denizen ID" | denizen ID as number)
dtask [name:"script name"], [denizen:query NPC or Denizen | "denizen ID" | denizen ID as number], (player:query player | "playername")
</pre></div>
<p>需要安装 <a href="denizen.md" title="Denizen">Denizen</a> 0.8。</p>

