# Behaviors

The Behaviors system allows NPCs to run AI behaviors defined in YAML format. Behaviors can be simple actions like walking or waiting, or complex sequences with conditions, loops, and parallel execution.

## Tree Structure

All behavior trees start with a `tree:` root node:

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

## Built-in Types

### sequence

Runs children in order until one fails.

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

### selector / random

Runs one sub-behavior at random.

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

### parallel

Runs multiple behaviors at the same time.

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

### loop [condition]

Runs the children in sequence if the condition is true.

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

### if [condition] / else

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

### invert

Inverts the success or failure of its child.

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

### timeout [duration]

If the child doesn't complete within the specified duration, it fails.

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

### eval [language]

Evaluates multiple expressions.

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

Or with a specific language (javascript, molang):

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

### Movement

#### walkto

Walks to specified coordinates.

**Inline usage:**

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- walkto 100 64 200 speed=1.5 range=50
</pre></div></td></tr></tbody></table>

**Named parameters:**

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

**Parameters:**

- `x`, `y`, `z` - Target coordinates (required)
- `speed` - Movement speed multiplier (optional)
- `range` - Maximum pathfinding range (optional)
- `distance_margin` / `margin` - How close in blocks to get to target (optional)

#### wander

Random wandering within a radius.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- wander radius=10 pathfind=true
</pre></div></td></tr></tbody></table>

**Parameters:**

- `radius` - Wander radius in blocks (default: 10)
- `pathfind` - Whether to use pathfinding (default: true)

#### look

Makes the NPC look at specific coordinates.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- look 100 64 200
</pre></div></td></tr></tbody></table>

**Parameters:**

- `x`, `y`, `z` - Target coordinates (required)

#### teleport

Teleports the NPC to coordinates.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- teleport 100 64 200
- teleport 100 64 200 world_name
</pre></div></td></tr></tbody></table>

**Parameters:**

- `x`, `y`, `z` - Target coordinates (required)
- `world` - World name (optional, defaults to current world)

### Timing

#### wait

Waits for a specified duration.

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

**Duration formats:**

- `s` - seconds
- `t` - ticks
- `m` - minutes
- Can also use expressions: `` wait `some_expression` ``

#### wait_until

Waits until a condition becomes true.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- wait_until `player.distance &lt; 10`
</pre></div></td></tr></tbody></table>

#### cooldown

Rate limits behaviors. Only succeeds if enough time has passed since the last time it was run.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- cooldown greeting 30s
- say "Hello there!"
</pre></div></td></tr></tbody></table>

**Parameters:**

- `key` - Cooldown identifier (required)
- `duration` - Cooldown duration (default: 1s)

### Memory Management

#### set

Sets a memory variable.

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

**Parameters:**

- `key` - Variable name (required)
- `value` - Value to set (required, can be expression)

#### forget

Removes a memory variable.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- forget counter
</pre></div></td></tr></tbody></table>

#### clear_memory

Clears all memory variables.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- clear_memory
</pre></div></td></tr></tbody></table>

### Communication

#### say

Makes the NPC say a message to nearby players.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- say "Hello, world!"
- say `"Player count: " + player.count`
</pre></div></td></tr></tbody></table>

#### emit_signal

Emits a signal.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- emit_signal "start_patrol"
</pre></div></td></tr></tbody></table>

#### emit_signal_to

Emits a signal to a specific NPC by ID or UUID.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- emit_signal_to 123 "alert"
- emit_signal_to "uuid-string" "alert"
</pre></div></td></tr></tbody></table>

**Parameters:**

- `npc` - NPC ID or UUID (required)
- `signal` - Signal name (required)

#### emit_global_signal

Emits a signal that all NPCs receive.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- emit_global_signal "server_restart_warning"
</pre></div></td></tr></tbody></table>

#### wait_for_signal

Waits until a signal is received.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- wait_for_signal "start_patrol"
- say "Signal received!"
</pre></div></td></tr></tbody></table>

### World Interaction

#### break_block

Breaks a block realistically using the NPC's held item at the specified coordinates.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- break_block 100 64 200 radius=3
</pre></div></td></tr></tbody></table>

**Parameters:**

- `x`, `y`, `z` - Block coordinates (required)
- `radius` - Maximum distance in blocks to break from (default: 3)

### Control Flow

#### succeed

Always returns SUCCESS.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- succeed
</pre></div></td></tr></tbody></table>

#### fail

Always returns FAILURE.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- fail
</pre></div></td></tr></tbody></table>

#### repeat

Repeats a specified number of times.

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

**Parameters:**

- `count` - Number of repetitions (default: 1)

## Special Syntax

### Command Execution

Lines starting with `/` are executed as commands:

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

### Expression Evaluation

Lines starting with backtick (`` ` ``) are evaluated as expressions:

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

## Expression System

The behavior tree system integrates with the Expression Registry for dynamic values.

### Expression Syntax

Expressions can be used in several ways:

**Inline in conditions:**

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- if `memory.get('counter') &lt; 10`:
    - say "Counter is low"
</pre></div></td></tr></tbody></table>

**In parameter values:**

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- walkto `npc.location.x + 10` `npc.location.y` `npc.location.z`
</pre></div></td></tr></tbody></table>

**In text:**

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- say "Counter value: {memory.get('counter')}"
</pre></div></td></tr></tbody></table>

**Standalone evaluation:**

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">- `memory.set('result', 10 * 5)`
</pre></div></td></tr></tbody></table>

## Memory System

The memory system provides persistent storage across behavior executions.

### Usage

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

### Memory Methods

- `memory.set(key, value)` - Set a value
- `memory.get(key, default)` - Get a value with optional default
- `memory.has(key)` - Check if key exists
- `memory.remove(key)` - Remove a key
- `memory.clear()` - Clear all memory

Memory is automatically saved and loaded with the NPC.

## Complete Examples

### Basic Patrol

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

### Signal Coordination

**Guard NPC:**

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

**Lookout NPC:**

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

### Conditional Greeter

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

### Resource Gathering

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

## Loading Behavior Trees

### External File

You can load trees from external files in the `behaviors/` directory.

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

The behaviors will be loaded from `plugins/Citizens/behaviors/patrol_behavior.yml`

### Template System

Behavior trees can be included in templates:

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

## API

### Registering Custom Behaviors

Register custom behaviors with the BehaviorRegistry:

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

### Custom Expression Languages

Register custom expression engines with the ExpressionRegistry for domain-specific languages.
