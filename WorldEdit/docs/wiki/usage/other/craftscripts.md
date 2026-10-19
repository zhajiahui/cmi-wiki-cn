---
title: CraftScripts
source_url: https://worldedit.enginehub.org/en/latest/usage/other/craftscripts/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# CraftScripts { #craftscripts }

脚本让你可以编写小任务，无需学习 Java、弄清如何编译 WorldEdit，或重复实现已有功能。CraftScript 使用 JavaScript 编写。

## 前置要求 { #requirements }

使用 CraftScript 前，需要安装 [Rhino JavaScript 引擎](https://github.com/mozilla/rhino/releases)。[这里](https://github.com/mozilla/rhino/releases/download/Rhino1_7_13_Release/rhino-runtime-1.7.13.jar)提供直接下载链接。将下载的文件重命名为 `js.jar`。在 Bukkit 上，将 `js.jar` 移到 `plugins/` 或 `plugins/WorldEdit` 文件夹；其他平台则放入 `mods` 文件夹。

## 使用 CraftScript { #using-craftscripts }

安装 JS 引擎后，将 CraftScript `.js` 文件放入 `craftscripts` 文件夹中（位于 WorldEdit 配置文件夹内，根据平台不同为 `plugins/WorldEdit` 或 `config/WorldEdit`）。

运行 CraftScript

```text
/cs <filename> <args>
/.s <args>
```

`/cs` 命令会运行指定文件名的 CraftScript（可省略 `.js`）。每个 CraftScript 都可以有自己的参数。`/.s` 命令会重新运行上次使用的 CraftScript。

## 编写 CraftScript { #writing-craftscripts }

WorldEdit 的脚本功能让你无需学习 Java 或编译代码，就能编写修改世界的代码。WorldEdit 中的脚本称为 CraftScript，使用 JavaScript 编写，放在 craftscripts/ 目录中。使用 WorldEdit 编写脚本的好处包括：

- 直接接入 WorldEdit 的撤销／重做系统

- 使用 WorldEdit 的方块放置优先顺序

- 支持 WorldEdit 的方块类型语法（`//set sign[facing=north]`）

- 获取用户选中的区域

!!! note "注意"

    建议在开始编写 CraftScript 前，先掌握 JavaScript 或 Java 的基础知识。

!!! tip "提示"

    虽然这里会介绍如何将 CraftScript 与 WorldEdit API 配合使用，但实际上并不限制脚本能做什么。高级用户甚至可以调用底层平台（Bukkit、NeoForge 等）的 API。

### 简介 { #introduction }

脚本的全局命名空间中有以下三个变量：

- `context` 是 [CraftScriptContext](https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/scripting/CraftScriptContext.java) 的实例。

- `player` 是调用脚本的玩家，为 [Player](https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/entity/Player.java) 的实例。

- `argv` 是一个 Java 字符串数组，包含调用脚本时传入的参数。

### 操作方块 { #working-with-blocks }

WorldEdit 中的所有方块编辑都通过 EditSession 完成。此对象会自动处理历史记录和方块放置顺序。要为自己的脚本获取编辑会话，使用：

```text
var sess = context.remember();
```

每次调用该方法都会得到一个新的 `EditSession`，因此应保留一个供后续使用。设置方块时，需要提供 `BlockState` 或 `BaseBlock`。前者是方块类型与一个或多个状态的组合，后者则是在 `BlockState` 基础上还可以包含 NBT 数据的方块。

示例：将方块设为白色羊毛

```text
importPackage(Packages.com.sk89q.worldedit.world.block);

var sess = context.remember();
sess.setBlock(player.getBlockOn().toVector().toBlockPoint(), BlockTypes.WHITE_WOOL.getDefaultState());
```

由于 `BlockTypes` 位于 `com.sk89q.worldedit.world.block` 命名空间中，必须先导入。`setBlock()` 的第一个参数是表示世界位置的 `BlockVector3`。

要获取方块，在 `EditSession` 上调用 `getBlock()`，返回的同样是 `BaseBlock`。

### 处理参数 { #processing-arguments }

参数通过 `argv` 变量传入。如果需要检查用户是否提供了正确数量的参数，可以使用 `CraftScriptContext#checkArgs()`。

`CraftScriptContext` 可以通过 `CraftScriptContext#getBlock()` 进行一些基本的参数解析。也可以通过 `WorldEdit.getInstance().getPatternFactory()` 和 `.getMaskFactory()` 直接调用 WorldEdit 的解析器。

示例：检查参数

```text
context.checkArgs(1, 3, "<block> [width] [height]");
var block = context.getBlock(argv[1]);
```

如果用户输入无效方块，会发生什么？程序会抛出异常。如果没有捕获它，用户会收到错误提示，脚本也会停止。

### 使用 Java 包 { #working-with-java-packages }

可以使用以下语法导入 Java 包：

```text
importPackage(Packages.package.name.here);
```

可以导入 Java 类路径中的任何包，不限于 WorldEdit。

### 示例脚本 { #example-scripts }

可以在 [WorldEdit 的 GitHub 仓库](https://github.com/EngineHub/WorldEdit/tree/master/contrib/craftscripts)中找到一些示例脚本。注意，它们不一定都已更新以适配当前 WorldEdit API。有关 WorldEdit API 的更多信息见 [API 章节](https://worldedit.enginehub.org/en/latest/api/)。
