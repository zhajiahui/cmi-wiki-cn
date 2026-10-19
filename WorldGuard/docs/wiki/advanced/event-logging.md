---
title: 事件日志
source_url: https://worldguard.enginehub.org/en/latest/advanced/event-logging/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 事件日志 { #event-logging }

## 事件归并 { #event-funneling }

Bukkit 通过“事件”将游戏中发生的事情通知插件。事件种类很多，例如：

- 装满桶

- 倒空桶

- 玩家右键点击实体

- 玩家放置方块

- 玩家挖掘方块

- 实体改变方块

- 活塞推出

- 活塞收回

不过，归根结底，这些事件围绕 Minecraft 中的三种基本对象展开：

- 物品

- 方块

- 实体

可以对这些对象执行某些操作：

- 放置

- 破坏

- 与之交互

- 对其造成伤害

为简化处理，WorldGuard 将 Bukkit 事件归并为一组更基础的事件：

- 装满桶 → 与方块交互、与物品交互

- 倒空桶 → 与方块交互、与物品交互

- 玩家右键点击实体 → 与实体交互

- 玩家放置方块 → 与方块交互

- 玩家挖掘方块 → 与方块交互

- 实体改变方块 → 与方块交互

- 活塞推出 → 与方块交互

- 活塞收回 → 与方块交互

这样，区域保护等 WorldGuard 功能只需处理“与方块交互”“与实体交互”等基础事件，就能判断是否允许放置、破坏某个方块或实体，或与其交互。

## 追踪原因 { #tracking-cause }

判断某项操作是否应当允许时，另一个重要环节是确定*是谁*在执行操作。

原因有时是间接的，这会让追踪变得复杂。例如，玩家向另一名玩家射箭时，直接原因是箭，但真正的原因是射箭的玩家。再如，玩家放置砂砾，使其向下掉落：最终落在地上的方块来自 (1) 下落中的砂砾方块实体；该实体来自 (2) 最初放置的砂砾方块；最初的方块又来自 (3) 玩家。

原因既可能是玩家，也可能是方块（如活塞）或实体（如末影人或苦力怕）。

但并非总能追踪到事件的真正原因。有时，WorldGuard 必须处理无法追溯来源的事件链。

## 显示内部事件 { #displaying-internal-events }

WorldGuard 只使用少量内部事件来归并 Bukkit 事件。可以在这些事件产生时将其输出到服务器日志中，用于：

- 查明某项操作触发了哪个黑名单事件

- 确认 WorldGuard 是否处理了某项操作

- 协助开发 WorldGuard，了解它如何处理某些事件

要启用此模式，请在启动命令行中指定 `-Dworldguard.debug.listener=true`。

!!! tip "提示"

    应在私有测试服务器上启用此功能，因为在繁忙的服务器上，它会产生大量日志。

示例：在 Windows 批处理文件中启用此模式

如果批处理文件的内容如下：

```text
@echo off
java -Xmx4096M -Xms4096M -jar server.jar nogui
pause
```

请像这样添加 `-Dworldguard.debug.listener=true`：

```text
@echo off
java -Xmx4096M -Xms4096M -Dworldguard.debug.listener=true -jar server.jar nogui
pause
```

此选项可以放在“java”之后、“-jar”之前的任意位置。本示例将其放在 -jar 的正前方。

## 理解输出内容 { #interpreting-the-output }

以在保护区域上方放置砂砾为例。服务器日志或控制台中会显示以下输出：

```text
* USE   GRAVEL         [Player{sk89q}] @world :BlockPlaceEvent
* PLACE GRAVEL @0,99,0 [Player{sk89q}] :BlockPlaceEvent
* SPAWN FALLING_BLOCK  [Block{0,99,0}] @-0,99,0 :EntityChangeBlockEvent
* PLACE GRAVEL @       [Block{0,99,0} | FallingSand] :EntityChangeBlockEvent [CANCELLED]
* SPAWN DROPPED_ITEM   [Block{0,99,0} | FallingSand] @-0,0,0 :EntityChangeBlockEvent
```

!!! note "注意"

    为便于说明，以下输出经过了精简和排版。

每一行的一般格式如下：

```text
ACTION TYPE/LOCATION [CAUSES] @LOOCATION :BUKKIT-EVENT [CANCELLED?]
```

事件被取消，表示该事件对应的操作已被阻止。

### 追踪砂砾的放置过程 { #tracing-gravel-placement }

首先，使用砂砾方块时，会产生使用方块事件：

```text
* USE   GRAVEL         [Player{sk89q}] @world :BlockPlaceEvent
```

原因自然是玩家。如果使用方块事件没有因为黑名单或 WorldGuard 的某项功能而被取消，就会继续实际放置方块：

```text
* PLACE GRAVEL @0,99,0 [Player{sk89q}] :BlockPlaceEvent
```

由于砂砾放在空中，它必须下落。下落的方块会变成实体（与骷髅、画等对象一样属于实体），因此会触发实体生成事件，原因是刚放置的砂砾方块。注意，WorldGuard 不会尝试追踪最初是谁放置了该方块。

```text
* SPAWN FALLING_BLOCK  [Block{0,99,0}] @-0,99,0 :EntityChangeBlockEvent
```

下落中的砂砾接触地面时，会尝试在地面上放置一个新的砂砾方块，再移除自身这个下落方块实体。直接原因是下落方块实体，但整个事件链始于先前放置的方块，日志条目会体现这一点：

```text
* PLACE GRAVEL @       [Block{0,99,0} | FallingSand] :EntityChangeBlockEvent [CANCELLED]
```

可以看到，砂砾放置事件被阻止了。这是因为砂砾落进了保护区域，而且来自区域外。WorldGuard 不希望生存模式下的玩家因此意外损失方块，所以会改为生成掉落物，从而触发另一个内部事件：

```text
* SPAWN DROPPED_ITEM   [Block{0,99,0} | FallingSand] @-0,0,0 :EntityChangeBlockEvent
```

可以看到，原因仍然一路追溯到最初放置的方块。区域没有禁用非成员产生的物品掉落（最初的砂砾来自区域外，因此视为非成员），所以物品事件不会被取消，掉落物得以生成。
