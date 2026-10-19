---
title: "JSpp"
source_url: "https://wiki.itemsadder.com/adding-content/scripting/jspp"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# JSpp

#### 警告

此脚本功能仍在开发中，后续更新可能调整。请持续查阅最新文档，了解更新和兼容性。

## `.jspp`

记得更新 [VSCode 扩展](https://marketplace.visualstudio.com/items?itemName=LoneDev.ia-vscode)，以获得新版预览 `.jspp` 格式的自动补全和常见错误检查。

此脚本模式底层使用 Java，但允许部分借鉴 JavaScript 的语法，便于编写。

优点：

* 代码量较少：常用 import 会自动解析。
* 编写速度更快。

缺点：

* 没有调试器。
* 自动补全不精确，且大部分内容缺失。
* 智能提示对错误的判断不总是可靠。
* 较难定位和修复代码错误。

### ✅ 语法基础

* 与 Java 一样，每条语句结尾都**必须使用分号（`;`）**。
* 可使用 `const`、`let` 或 `var` 声明变量。
* 支持 **lambda 表达式**和 **Java 类导入**。

### 🌟 脚本变量

脚本会从触发它的事件继承若干预定义变量。这些变量自动可用，并带有 `$` 前缀，以避免名称冲突：

* `$plugin`：插件实例。
* `$event`：触发脚本的事件。
* `$player`：事件涉及的玩家（如果适用）。
* `$customStack`：事件涉及的自定义物品堆（如果适用）。
* `$itemStack`：涉及的普通物品堆（如果适用）。
* `$customEntity`：涉及的普通自定义实体（如果适用）。

脚本生成的 Java 类包含 `main` 函数，其签名如下：

```java
public static void main(Plugin $plugin, Event $event, Player $player, CustomStack $customStack, ItemStack $itemStack)
```

自定义实体脚本则使用以下签名：

```java
public static void main(Plugin $plugin, Event $event, Player $player, CustomEntity $customEntity)
```

> 📝 **注意**：此结构目前固定，不可修改。脚本必须在此框架内编写。

### ⏳ 延迟

使用 `delay(ticks, () -> { ... })` 函数延迟执行。

* **1 秒 = 20 刻**

```java
delay(40, () => {
  msg($player, "This message appears after a 2 seconds delay.");
});
```

***

### 📦 导入 Java 类

使用 `import` 关键字并加上引号，可以导入外部类：

```java
import "org.bukkit.Bukkit";
import "org.bukkit.entity.LivingEntity";
import "net.kyori.adventure.text.Component";
import "com.comphenix.protocol.ProtocolLibrary";
```

***

### ❌ 取消事件

使用以下方式取消当前事件：

```java
cancelEvent();
```

***

### 🔧 实用函数

#### 🧱 ItemStack 工具

```java
isCustom(ItemStack itemStack);
newCustomStack(String namespacedId);
newCustomStack(String namespacedId, int amount);
newStack(Material material);
```

#### 🧍 玩家手持物品

```java
isHeld(Player player, String namespacedId);
isHeld(Player player, CustomStack customStack);
isHeld(Player player, Material material);
setHeld(Player player, String namespacedId);
```

#### 🧱 方块工具

```java
isCustom(Block block);
customBlock(Block block);
customBlock(Location location);

block(String worldName, int x, int y, int z);
block(World world, int x, int y, int z);
block(Location location);

location(String worldName, int x, int y, int z);

removeBlock(Block block);
placeBlock(Block block, Material material);
placeBlock(Block block, CustomBlock customBlock);
placeBlock(Block block, String identifier);
```

#### 💬 消息和日志

```java
msg(Player player, String message);
msg(Player player, String message, boolean minimessage);
msg(Player player, Component message);
log(String message);
```

### ↺ 类型转换

用法与 Java 完全相同。

```java
Type1 item = (Type2) item2;
```

***

### 📌 推荐做法

* 使用 `delay()` 实现动画或延迟反馈。
* 修改自定义物品或方块前，始终检查 `isCustom()`。
* 调试时，使用 `log()` 记录动作。
* 处理交互时，使用 `cancelEvent()` 阻止默认行为。
