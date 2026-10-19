---
title: 行为
source_url: https://wiki.citizensnpcs.co/Behaviors
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5665
---


<a id="top"></a>

# 行为

<a id="Behaviors"></a><h1 id="behaviors">行为</h1>
<p>行为系统允许 NPCs 运行以 YAML 格式定义的 AI 行为。行为可以是简单的动作，例如行走或等待，也可以是具有条件、循环和并行执行的复杂序列。</p>
<a id="Tree_Structure"></a><h2 id="tree-structure">树结构</h2>
<p>所有行为树都以 <code>tree:</code> 根节点开始：</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - behavior_name arg1 arg2
    - another_behavior
</pre></div></td></tr></tbody></table>
<a id="Built-in_Types"></a><h2 id="built-in-types">内置类型</h2>
<h3 id="sequence">sequence</h3>
<p>按顺序运行子级，直到其中一个失败。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - say "First"
    - wait 1s
    - say "Second"
</pre></div></td></tr></tbody></table>
<a id="selector_/_random"></a><h3 id="selector-random">selector / random</h3>
<p>随机运行一种子行为。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  selector:
    - sequence:
        - if `player_nearby`:
            - say "I see you!"
    - wander radius=15
</pre></div></td></tr></tbody></table>
<h3 id="parallel">parallel</h3>
<p>同时运行多个行为。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  parallel:
    - wander radius=10 pathfind=true
    - sequence:
        - wait 5s
        - say "Still wandering..."
</pre></div></td></tr></tbody></table>
<a id="loop_[condition]"></a><h3 id="loop-condition">loop [condition]</h3>
<p>如果条件为真，则按顺序运行子级。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  loop `memory.get('counter', 0) &lt; 5`:
    - say "Count is {memory.get('counter', 0)}"
    - set counter `memory.get('counter', 0) + 1`
    - wait 1s
</pre></div></td></tr></tbody></table>
<a id="if_[condition]_/_else"></a><h3 id="if-condition-else">if [condition] / else</h3>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - if `memory.has('greeted')`:
        - say "Welcome back!"
      else:
        - say "Nice to meet you!"
        - set greeted true
</pre></div></td></tr></tbody></table>
<h3 id="invert">invert</h3>
<p>反转其子级的成功或失败。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  invert:
    - fail
</pre></div></td></tr></tbody></table>
<a id="timeout_[duration]"></a><h3 id="timeout-duration">timeout [duration]</h3>
<p>如果子进程没有在指定的时间内完成，则失败。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  timeout 5s:
    - walkto 500 64 500
</pre></div></td></tr></tbody></table>
<a id="eval_[language]"></a><h3 id="eval-language">eval [language]</h3>
<p>评估多个表达式。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  eval:
    - memory.set('x', 100)
    - memory.set('y', 64)
    - memory.set('z', 200)
</pre></div></td></tr></tbody></table>
<p>或者使用特定语言（javascript、molang）：</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  eval molang:
    - v.test = 5
    - v.result = v.test * 2
</pre></div></td></tr></tbody></table>
<a id="Movement"></a><h3 id="movement">运动</h3>
<h4 id="walkto">walkto</h4>
<p>步行到指定坐标。</p>
<p><strong>直插式 usage:</strong></p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- walkto 100 64 200 speed=1.5 range=50
</pre></div></td></tr></tbody></table>
<p><strong>命名为parameters:</strong></p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- walkto:
    x: 100
    y: 64
    z: 200
    speed: 1.5
    range: 50
    distance_margin: 2
</pre></div></td></tr></tbody></table>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>x</code>、<code>y</code>、<code>z</code> - 目标坐标（必填）</li>
<li><code>speed</code> - 移动速度倍增器（可选）</li>
<li><code>range</code> - 最大寻路范围（可选）</li>
<li><code>distance_margin</code> / <code>margin</code> - 距离目标有多近（可选）</li>
</ul>
<h4 id="wander">wander</h4>
<p>在半径范围内随机徘徊。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- wander radius=10 pathfind=true
</pre></div></td></tr></tbody></table>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>radius</code> - 以方块为单位的徘徊半径（默认值：10）</li>
<li><code>pathfind</code> - 是否使用寻路（默认：true）</li>
</ul>
<h4 id="look">look</h4>
<p>使 NPC 查看特定坐标。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- look 100 64 200
</pre></div></td></tr></tbody></table>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>x</code>、<code>y</code>、<code>z</code> - 目标坐标（必填）</li>
</ul>
<h4 id="teleport">teleport</h4>
<p>将 NPC 传送到坐标。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- teleport 100 64 200
- teleport 100 64 200 world_name
</pre></div></td></tr></tbody></table>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>x</code>、<code>y</code>、<code>z</code> - 目标坐标（必填）</li>
<li><code>world</code> - 世界名称（可选，默认为当前世界）</li>
</ul>
<a id="Timing"></a><h3 id="timing">时机</h3>
<h4 id="wait">wait</h4>
<p>等待指定的持续时间。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- wait 3s      # 3 seconds
- wait 100t    # 100 ticks
- wait 2m      # 2 minutes
</pre></div></td></tr></tbody></table>
<p><strong>持续时间 formats:</strong></p>
<ul>
<li><code>s</code>-秒</li>
<li><code>t</code> - 刻度</li>
<li><code>m</code>-分钟</li>
<li>还可以使用表达式：<code>wait `some_expression`</code></li>
</ul>
<h4 id="wait_until">wait_until</h4>
<p>等待直到条件成立。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- wait_until `player.distance &lt; 10`
</pre></div></td></tr></tbody></table>
<h4 id="cooldown">cooldown</h4>
<p>速率限制行为。仅当自上次运行以来已经过去了足够的时间时才会成功。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- cooldown greeting 30s
- say "Hello there!"
</pre></div></td></tr></tbody></table>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>key</code> - 冷却标识符（必需）</li>
<li><code>duration</code> - 冷却时间（默认：1秒）</li>
</ul>
<a id="Memory_Management"></a><h3 id="memory-management">内存管理</h3>
<h4 id="set">set</h4>
<p>设置内存变量。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- set counter 5
- set name "Bob"
- set calculated `10 * 5`
</pre></div></td></tr></tbody></table>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>key</code> - 变量名称（必填）</li>
<li><code>value</code> - 要设置的值（必需，可以是表达式）</li>
</ul>
<h4 id="forget">forget</h4>
<p>删除内存变量。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- forget counter
</pre></div></td></tr></tbody></table>
<h4 id="clear_memory">clear_memory</h4>
<p>清除所有内存变量。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- clear_memory
</pre></div></td></tr></tbody></table>
<a id="Communication"></a><h3 id="communication">通讯</h3>
<h4 id="say">say</h4>
<p>Makes the NPC say a message to nearby players.</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- say "Hello, world!"
- say `"Player count: " + player.count`
</pre></div></td></tr></tbody></table>
<h4 id="emit_signal">emit_signal</h4>
<p>发出信号。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- emit_signal "start_patrol"
</pre></div></td></tr></tbody></table>
<h4 id="emit_signal_to">emit_signal_to</h4>
<p>Emits a signal to a specific NPC by ID or UUID.</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- emit_signal_to 123 "alert"
- emit_signal_to "uuid-string" "alert"
</pre></div></td></tr></tbody></table>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>npc</code> - NPC ID 或 UUID（必填）</li>
<li><code>signal</code> - 信号名称（必填）</li>
</ul>
<h4 id="emit_global_signal">emit_global_signal</h4>
<p>发出所有 NPCs 接收到的信号。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- emit_global_signal "server_restart_warning"
</pre></div></td></tr></tbody></table>
<h4 id="wait_for_signal">wait_for_signal</h4>
<p>等待直到收到信号。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- wait_for_signal "start_patrol"
- say "Signal received!"
</pre></div></td></tr></tbody></table>
<a id="World_Interaction"></a><h3 id="world-interaction">世界互动</h3>
<h4 id="break_block">break_block</h4>
<p>Breaks a block realistically using the NPC's held item at the specified coordinates.</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- break_block 100 64 200 radius=3
</pre></div></td></tr></tbody></table>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>x</code>、<code>y</code>、<code>z</code> - 块坐标（必填）</li>
<li><code>radius</code> - 打破方块的最大距离（默认值：3）</li>
</ul>
<a id="Control_Flow"></a><h3 id="control-flow">控制流程</h3>
<h4 id="succeed">succeed</h4>
<p>始终返回成功。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- succeed
</pre></div></td></tr></tbody></table>
<h4 id="fail">fail</h4>
<p>总是返回失败。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- fail
</pre></div></td></tr></tbody></table>
<h4 id="repeat">repeat</h4>
<p>重复指定的次数。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- repeat 5:
    - say "Counting..."
    - wait 1s
</pre></div></td></tr></tbody></table>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>count</code> - 重复次数（默认值：1）</li>
</ul>
<a id="Special_Syntax"></a><h2 id="special-syntax">特殊语法</h2>
<a id="Command_Execution"></a><h3 id="command-execution">命令执行</h3>
<p>以 <code>/</code> 开头的行作为命令执行：</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - /npc speak "Hello from command!"
    - /say This is a server command
</pre></div></td></tr></tbody></table>
<a id="Expression_Evaluation"></a><h3 id="expression-evaluation">表达评估</h3>
<p>以反引号 (<code>`</code>) 开头的行被计算为表达式：</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - `inv.add(item.json('{"material":"DIAMOND","amount":64}'))`
    - `memory.set('flag', true)`
</pre></div></td></tr></tbody></table>
<a id="Expression_System"></a><h2 id="expression-system">表达系统</h2>
<p>行为树系统与动态值的表达式注册表集成。</p>
<a id="Expression_Syntax"></a><h3 id="expression-syntax">表达式语法</h3>
<p>表达式可以使用多个 ways:</p>
<p><strong>内联于 conditions:</strong></p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- if `memory.get('counter') &lt; 10`:
    - say "Counter is low"
</pre></div></td></tr></tbody></table>
<p><strong>参数values:中</strong></p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- walkto `npc.location.x + 10` `npc.location.y` `npc.location.z`
</pre></div></td></tr></tbody></table>
<p><strong>在text:</strong></p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- say "Counter value: {memory.get('counter')}"
</pre></div></td></tr></tbody></table>
<p><strong>独立式 evaluation:</strong></p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- `memory.set('result', 10 * 5)`
</pre></div></td></tr></tbody></table>
<a id="Memory_System"></a><h2 id="memory-system">记忆系统</h2>
<p>内存系统提供跨行为执行的持久存储。</p>
<a id="Usage"></a><h3 id="usage">用途</h3>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - set visited_waypoint_1 true
    - set visit_count `memory.get('visit_count', 0) + 1`
    - if `memory.has('greeted')`:
        - say "Welcome back! Visit #{memory.get('visit_count')}"
      else:
        - say "First visit!"
        - set greeted true
    - forget temporary_flag
</pre></div></td></tr></tbody></table>
<a id="Memory_Methods"></a><h3 id="memory-methods">记忆方法</h3>
<ul>
<li><code>memory.set(key, value)</code> - 设置一个值</li>
<li><code>memory.get(key, default)</code> - 获取具有可选默认值的值</li>
<li><code>memory.has(key)</code> - 检查键是否存在</li>
<li><code>memory.remove(key)</code> - 删除钥匙</li>
<li><code>memory.clear()</code> - 清除所有内存</li>
</ul>
<p>Memory is automatically saved and loaded with the NPC.</p>
<a id="Complete_Examples"></a><h2 id="complete-examples">完整的例子</h2>
<a id="Basic_Patrol"></a><h3 id="basic-patrol">基本巡逻</h3>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - set patrol_started true
    - loop `memory.get('patrol_count', 0) &lt; 3`:
        - walkto `npc.location.x + 10` `npc.location.y` `npc.location.z`
        - wait 2s
        - cooldown speak 10s
        - say "Patrolling area {memory.get('patrol_count', 0)}"
        - walkto `npc.location.x - 10` `npc.location.y` `npc.location.z`
        - set patrol_count `memory.get('patrol_count', 0) + 1`
    - say "Patrol complete!"
    - forget patrol_count
</pre></div></td></tr></tbody></table>
<a id="Signal_Coordination"></a><h3 id="signal-coordination">信号协调</h3>
<p><strong>Guard NPC:</strong></p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - wait_for_signal "intruder_alert"
    - say "Intruder detected! Responding!"
    - walkto `signal.data.x` `signal.data.y` `signal.data.z`
    - emit_global_signal "area_secured"
</pre></div></td></tr></tbody></table>
<p><strong>了望 NPC：</strong></p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - if `player.distance &lt; 10`:
        - cooldown alert 60s
        - emit_global_signal "intruder_alert"
        - say "Alert! Intruder spotted!"
</pre></div></td></tr></tbody></table>
<a id="Conditional_Greeter"></a><h3 id="conditional-greeter">有条件的问候语</h3>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - if `memory.has('greeted')`:
        - say "Welcome back!"
      else:
        - sequence:
            - say "Nice to meet you!"
            - set greeted true
    - cooldown greet 10s
    - wait 2s
    - say "Have a nice day!"
</pre></div></td></tr></tbody></table>
<a id="Resource_Gathering"></a><h3 id="resource-gathering">资源收集</h3>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">tree:
  sequence:
    - set gathered 0
    - loop `memory.get('gathered', 0) &lt; 5`:
        - wander radius=20 pathfind=true
        - wait 5s
        - break_block `npc.location.x` `npc.location.y - 1` `npc.location.z`
        - set gathered `memory.get('gathered', 0) + 1`
        - say "Gathered {memory.get('gathered')} resources"
    - say "Resource gathering complete!"
    - teleport 0 64 0
</pre></div></td></tr></tbody></table>
<a id="Loading_Behavior_Trees"></a><h2 id="loading-behavior-trees">加载行为树</h2>
<a id="External_File"></a><h3 id="external-file">External File</h3>
<p>您可以从 <code>behaviors/</code> 目录中的外部文件加载树。</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">traits:
  - name: behavior
    tree: patrol_behavior.yml
</pre></div></td></tr></tbody></table>
<p>行为将从 <code>plugins/Citizens/behaviors/patrol_behavior.yml</code> 加载</p>
<a id="Template_System"></a><h3 id="template-system">模板系统</h3>
<p>行为树可以包含在templates:中</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">greeter:
  traits:
    - name: behavior
      tree:
        sequence:
          - cooldown greet 10s
          - say "Hello there, traveler!"
          - wait 2s
</pre></div></td></tr></tbody></table>
<a id="API"></a><h2 id="api">API</h2>
<a id="Registering_Custom_Behaviors"></a><h3 id="registering-custom-behaviors">注册自定义行为</h3>
<p>使用BehaviorRegistry注册自定义行为：</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="java">registry.registerBehavior("my_behavior", (params, context) -&gt; {
    String arg = context.getArgOrParam(0, "param_name", params, "default");
    ExpressionValue argHolder = registry.getExpressionRegistry().parseValue(arg);

    return new InstantBehavior() {
        @Override
        public void reset() {
        }

        @Override
        public BehaviorStatus run() {
            NPC npc = context.getNPC();
            // Your behavior logic here
            return BehaviorStatus.SUCCESS;
        }

        @Override
        public boolean shouldExecute() {
            return true;
        }
    };
});
</pre></div></td></tr></tbody></table>
<a id="Custom_Expression_Languages"></a><h3 id="custom-expression-languages">自定义表达语言</h3>
<p>使用 ExpressionRegistry 为特定于域的语言注册自定义表达式引擎。</p>

