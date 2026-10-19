---
title: 保护范围
source_url: https://worldguard.enginehub.org/en/latest/regions/scope/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 保护范围 { #what-s-protected }

保护涵盖的内容非常全面：

- 阻止破坏和放置方块。

- 禁止打开箱子、熔炉等容器。

- 阻止从区域外发射的 TNT 大炮。

- 阻止从区域外发射的砂砾大炮。

- 防止从区域外利用树木生长进行破坏。

- 限制活塞，禁止从保护区域中拉出方块或向其中推入方块。

- 防止利用告示牌修改漏洞进行破坏。

- 防止踩坏作物。

- 保护矿车和船。

- 保护画和物品展示框。

- 保护门、按钮、压力板和拉杆。

- 保护动物，包括牵引、驯服和剪毛操作。

- 阻止未经允许的喷溅药水和投射物。

此外，WorldGuard 也支持模组添加的自定义方块和实体，但存在一些例外，后文会说明。

水流和岩浆流动保护默认关闭，可以在[配置](../config.md)中启用。

!!! tip "提示"

    如果发现绕过保护的方法，请[在问题跟踪器中提交报告](https://github.com/EngineHub/WorldGuard/issues)。

## 例外情况 { #exceptions }

默认会合理地允许非成员进行一些操作：

- 允许丢弃和拾取物品。

- 允许掉落经验。

调整[区域旗标](flags.md)，可以在全局或单个区域内取消这些例外。

也可通过旗标为单个区域添加其他例外，或通过[配置](../config.md)中的 `interaction-whitelist` 在全局添加。

示例：即使在保护区域内，也允许所有人使用门、拉杆、按钮和压力板

`use` 旗标控制这些类型的交互：

```text
/rg flag __global__ use allow
```

关于 `__global__` 的更多信息，见[全局区域](global-region.md)页面。

示例：禁止 spawn 区域的所有非成员在出生点丢弃和拾取物品

拾取和丢弃物品由不同旗标控制：

```text
/rg flag spawn item-pickup -g nonmembers deny
/rg flag spawn item-drop -g nonmembers deny
```

示例：禁止所有地块区域的非成员掉落经验

所有地块区域都必须继承某个模板区域。本例中，模板区域名为 `mall_parent`：

```text
/rg flag mall_parent exp-drops -g nonmembers deny
```

所有地块都会继承该旗标，“nonmembers”会分别针对各地块的非成员。

以下做法**无效**：

```text
DOESN'T WORK: /rg flag __global__ exp-drops -g nonmembers deny
```

因为区域不会继承 `__global__`，所以在 `__global__` 上指定“nonmembers”，指的是**全局区域本身**的非成员。

## 方块与实体 { #blocks-and-entities }

WorldGuard 区域保护的一个重要特点，是处理方块和实体的方式。显然，玩家可以成为保护区域的成员；WorldGuard 也以相同方式看待方块和实体，它们同样可以成为区域成员。

但无法手动将实体或方块加入区域成员列表。只要它们*位于区域内部*，就会被视为成员。因此，区域外的活塞不能向保护区域内推入方块，因为它被视为非成员，而非成员无论是玩家还是其他对象，都不能修改方块。反过来，区域内的活塞可以在区域内部推动方块，因为它属于该区域。

WorldGuard 还会尝试追踪事件的真正*原因*。例如，在保护区域上方放置砂砾，使其落入区域时，WorldGuard 认为最终落地形成的方块由*下落方块实体*放置，而该实体又由*高处最初放置的砂砾方块*产生。不过，最初是谁放置砂砾并不容易确定。由于最初的方块位于区域外，它不是区域成员，因此不能落入保护区域。

!!! warning "警告"

    区域的 `build` 设为 `deny` 后，任何人都不能建造，活塞也会失效，因为该旗标连成员的建造行为都会阻止；如前所述，活塞也可像玩家一样成为普通区域成员。

## 模组和插件支持 { #mod-and-plugin-support }

有些模组会添加新的游戏机制，如新方块、新物品、新实体，或为现有方块、物品、实体添加新行为。这些功能可以由 Bukkit 插件实现，也可由 NeoForge、Fabric 等其他平台上的模组实现。

一般来说，Bukkit 插件通常更愿意遵守其他 Bukkit 插件的保护，但并非始终如此。非 Bukkit 模组的支持往往很差。本节介绍那些未正确遵守 WorldGuard 等区域访问限制插件或模组保护的模组。

### 尽力提供保护 { #best-effort-protection }

需要留意的情况

- 会改变其他方块或实体的方块、实体

- 发射投射物的武器、法术或工具

大多数情况下，WorldGuard 能保护大多数自定义方块和实体。主要做法是阻止玩家在服务器上左键或右键点击未知方块、实体。通常这已足够，因为与大多数方块、实体交互的方式只有这些。

但 WorldGuard 无法保护那些直接在客户端打开界面的方块或实体，因为它们通过 WorldGuard 不知道的独立通道发送数据。在多人服务器中，如果某种界面打开速度明显快于容器界面，通常就可据此判断。

此外，WorldGuard 本身无法有效控制自定义方块或实体代为执行的操作，例如假想的采矿无人机挖掘方块，至少无法做到细致控制。原版 Minecraft 也有能影响世界的方块，如活塞，但 Bukkit 团队或服务器软件维护者会在这些原版方块改变世界时正确通知插件。模组添加的方块和实体很少这样做，因此 WorldGuard 无法处理这些情况。

有些模组会用“假玩家”代表方块或实体执行操作。惯例是将假玩家名称写成 `[ModName]`，但这项信息通常只能说明是哪个模组在修改世界，无法帮助 WorldGuard 判断是否应允许该操作。为了让这些模组能在保护区域工作，假玩家默认会获得通行，绕过全部保护。可以通过[配置](../config.md)中的 `fake-player-build-override` 禁用此行为，但那会让这类模组无法在保护区域内工作。

投射物，以及具有投射效果的魔法模组，是一个主要问题，因为模组很可能不会向插件通知投射物产生的影响。WorldGuard 提供了一种变通方式：在[配置](../config.md)中用 `emit-block-use-at-feet` 指定物品类型列表，*假定*列表中的物品正尝试修改玩家脚下的方块。这样会禁止保护区域*内部*的玩家使用这些物品，从而阻止其发射武器，但无法阻止玩家从*区域外*向区域内射击。

### 解决办法 { #solutions }

如果对应模组实际是 Bukkit 插件，请联系开发者加入对保护插件的支持。可以触发适当的 Bukkit 事件，或使用 [WorldGuard API](https://worldguard.enginehub.org/en/latest/developer/) 实现。

如果模组不是 Bukkit 插件，通常很难说服开发者增加 Bukkit 支持。

除了真正修复保护支持，还可以：

- 如果玩家群体值得信任，就忽略此问题。

- 禁用相关物品或方块。
