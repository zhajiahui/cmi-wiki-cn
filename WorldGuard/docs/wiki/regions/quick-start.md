---
title: 快速入门
source_url: https://worldguard.enginehub.org/en/latest/regions/quick-start/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 快速入门 { #quick-start }

## 选择范围 { #selecting-areas }

创建区域前，必须告诉 WorldGuard 实际范围；这需要用到 [WorldEdit](https://www.enginehub.org/worldedit)。

还不会使用 WorldEdit？

可以阅读 [WorldEdit 快速入门](https://worldedit.enginehub.org/en/latest/quickstart/)，学习如何选择范围。

区域支持以下形状：

- 长方体，如立方体或盒状范围

- 带有高度范围的二维多边形

尝试使用圆柱等不支持的形状时，WorldGuard 会提示。

## 基本命令 { #basic-commands }

### 创建区域 { #creating-regions }

每个区域都必须有唯一名称，名称不区分大小写。用 `/region define` 创建区域：

```text
/region define town
```

也可用 `/rg` 代替 `/region`：

```text
/rg define town
```

新建区域会**自动禁止其内部的建造行为**。要允许指定玩家建造，需将其添加为成员或*所有者*。之所以区分所有者与成员，主要是因为可以[分别为两者设置命令使用权限](../permissions.md)。

玩家和权限组都可成为成员或所有者。指定权限组时，在组名前加 `g:`。相关添加与移除命令如下：

```text
/rg addmember town wizjany sk89q g:builders
/rg addowner town sk89q
/rg removemember town g:builders
/rg removeowner town sk89q
```

完整命令说明见[区域命令](commands.md)页面。

创建区域时，也可顺便指定所有者：

```text
/rg define town wizjany sk89q g:builders
```

!!! hint "提示"

    区域修改会在短暂延迟后自动保存，也可使用 `/rg save` 强制保存。所有保存操作都在后台运行，不会暂停服务器。

示例：创建只有建筑团队能建造的出生点区域

1. 使用 WorldEdit 选中出生点范围。

2. 创建名为“spawn”的区域：



   ```text
   /rg define spawn
   ```

3. 将建筑团队添加为成员：



   ```text
   /rg addmember spawn g:builders
   ```

### 其他命令 { #other-commands }

可以删除区域：

```text
/rg remove town
```

可以查看区域信息：

```text
/rg info town
```

可以查看区域列表：

```text
/rg list
```

可以修改现有区域的形状或大小：

```text
/rg redefine town
```

更多命令见[区域命令](commands.md)页面。

## 区域属性 { #properties-of-regions }

### 处理重叠 { #handling-overlap }

WorldGuard 允许区域重叠。这使设置方式更灵活，但也可能增加复杂度。

- 区域重叠时，玩家必须拥有**所有**重叠区域的建造权限。

- 如果希望某个区域覆盖另一个区域，请使用[优先级和区域继承](priorities.md)。

- 如果希望某个区域在是否允许玩家建造方面覆盖所有其他区域，请使用 `build` [区域旗标](flags.md)。

- 如果所建区域不应保护其范围，请使用 `passthrough` [区域旗标](flags.md)。

示例：创建与出生点重叠、允许所有人自由挖掘的采矿区

1. 选中采矿区范围。

2. 创建名为“mine”的区域：



   ```text
   /rg define mine
   ```

3. 将 `build` 设为 `allow`，允许所有玩家建造。由于 spawn 没有显式设置 build 旗标，这会覆盖 spawn 的保护：



   ```text
   /rg flag mine build allow
   ```

!!! warning "警告"

    `build` 还有一些特殊性质，因此通常不建议修改，除非清楚其作用。更多信息见[区域旗标概览](flags.md)。

### 旗标 { #flags }

每个区域都可应用称为旗标的额外设置。例如，可通过“pvp”旗标禁止 PvP：

```text
/rg flag town pvp deny
```

更多信息见[区域旗标](flags.md)指南。

示例：在出生点创建竞技场，让战斗玩家可以交战但不能破坏方块，同时让建筑团队仍能在竞技场内建造

1. 选中竞技场范围。

2. 创建名为“arena”的区域：



   ```text
   /rg define arena
   ```

3. 将 `pvp` 设为 `allow`：



   ```text
   /rg flag arena pvp allow
   ```

4. 建筑团队即使是 spawn 的成员（如果一直按前面的示例操作），也无法在 arena 中建造，因为他们不是 arena 的成员。不过，创建 arena 是为了设置 PvP 旗标，而不是保护范围，因此将 `passthrough` 设为 `allow`，让它不参与建造权限检查：



   ```text
   /rg flag arena passthrough allow
   ```

## 常见场景 { #common-scenarios }

如果想知道如何实现某项需求，如允许使用门、拉杆、压力板等，请参阅[常见场景](common-scenarios.md)。
