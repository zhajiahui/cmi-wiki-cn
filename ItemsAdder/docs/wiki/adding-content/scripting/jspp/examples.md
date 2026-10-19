---
title: "示例"
source_url: "https://wiki.itemsadder.com/adding-content/scripting/jspp/examples"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 示例

## 配置示例

```yaml
info:
  namespace: test
items:
  script_executor:
    name: script_executor
    resource:
      material: PAPER
      generate: false
      model_path: minecraft:item/diamond
    events:
      interact:
        left:
          script:
            name: test:script_test
scripts:
  script_test:
    path: script_test.jspp

```

***

## ⏳ 延迟

使用 `delay(ticks, () -> { ... })` 函数延迟执行。

* **1 秒 = 20 刻**

```java
delay(40, () => {
  msg($player, "This message appears after a 2 seconds delay.");
});
```

***

## 📦 导入 Java 类

使用 `import` 关键字并加上引号，可以导入外部类：

```java
import "org.bukkit.Bukkit";
import "org.bukkit.entity.LivingEntity";
import "net.kyori.adventure.text.Component";
import "com.comphenix.protocol.ProtocolLibrary";
```

***

## ❌ 取消事件

使用以下方式取消当前事件：

```java
cancelEvent();
```

***

## 🔧 实用函数

### 🧱 ItemStack 工具

```java
isCustom(ItemStack itemStack);
newCustomStack(String namespacedId);
newCustomStack(String namespacedId, int amount);
newStack(Material material);
```

### 🧍 玩家手持物品

```java
isHeld(Player player, String namespacedId);
isHeld(Player player, CustomStack customStack);
isHeld(Player player, Material material);
setHeld(Player player, String namespacedId);
```

### 🧱 方块工具

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

### 💬 消息和日志

```java
msg(Player player, String message);
msg(Player player, String message, boolean minimessage);
msg(Player player, Component message);
log(String message);
```

### 数据工具

用于保存持久化数据，并在之后读取。

这些方法支持 `ItemStack`、`CustomItem`、`Entity` 和 `Block`。

```java
hasData(var param, String namespace, String key);
removeData(var param, String namespace, String key);
getDataByte(var param, String namespace, String key, byte def);
setDataByte(var param, String namespace, String key, byte value);
getDataShort(var param, String namespace, String key, short def);
setDataShort(var param, String namespace, String key, short value);
getDataInt(var param, String namespace, String key, int def);
setDataInt(var param, String namespace, String key, int value);
getDataLong(var param, String namespace, String key, long def);
setDataLong(var param, String namespace, String key, long value);
getDataFloat(var param, String namespace, String key, float def);
setDataFloat(var param, String namespace, String key, float value);
getDataDouble(var param, String namespace, String key, double def);
setDataDouble(var param, String namespace, String key, double value);
getDataBool(var param, String namespace, String key, boolean def);
setDataBool(var param, String namespace, String key, boolean value);
getDataString(var param, String namespace, String key, String def);
setDataString(var param, String namespace, String key, String value);
```

#### 示例

<details>

<summary>示例：传送器脚本</summary>

```java
// Test: Save or use player coordinates and orientation in held item, with usage count
let item = $itemStack;
let ns = "myplugin";
let keyX = "coord_x";
let keyY = "coord_y";
let keyZ = "coord_z";
let keyYaw = "coord_yaw";
let keyPitch = "coord_pitch";
let keyUses = "coord_uses";
let maxUses = 3; // Set how many times the item can be used

// Try to read already saved coordinates and orientation
let hasCoords = hasData(item, ns, keyX) && hasData(item, ns, keyY) && hasData(item, ns, keyZ) && hasData(item, ns, keyYaw) && hasData(item, ns, keyPitch);

if (!hasCoords) {
  // Save current coordinates and orientation in the item
  let loc = $player.getLocation();
  setDataDouble(item, ns, keyX, loc.getX());
  setDataDouble(item, ns, keyY, loc.getY());
  setDataDouble(item, ns, keyZ, loc.getZ());
  setDataFloat(item, ns, keyYaw, loc.getYaw());
  setDataFloat(item, ns, keyPitch, loc.getPitch());
  setDataInt(item, ns, keyUses, maxUses);

  // Verify writing
  let savedX = getDataDouble(item, ns, keyX, 0);
  let savedY = getDataDouble(item, ns, keyY, 0);
  let savedZ = getDataDouble(item, ns, keyZ, 0);
  let savedYaw = getDataFloat(item, ns, keyYaw, 0);
  let savedPitch = getDataFloat(item, ns, keyPitch, 0);
  let savedUses = getDataInt(item, ns, keyUses, 0);

  msg($player, "Saved coordinates: " + savedX + ", " + savedY + ", " + savedZ + " (Yaw: " + savedYaw + ", Pitch: " + savedPitch + ")");
  msg($player, "Usages left: " + savedUses);

  if (savedX != loc.getX() || savedY != loc.getY() || savedZ != loc.getZ() || savedYaw != loc.getYaw() || savedPitch != loc.getPitch()) {
    msg($player, "Test FAILED: saving coords/orientation");
  } else {
    msg($player, "Coordinates and orientation saved in the item.");
  }
} else {
  // Read and use the saved coordinates and orientation
  let x = getDataDouble(item, ns, keyX, 0);
  let y = getDataDouble(item, ns, keyY, 0);
  let z = getDataDouble(item, ns, keyZ, 0);
  let yaw = getDataFloat(item, ns, keyYaw, 0);
  let pitch = getDataFloat(item, ns, keyPitch, 0);
  let uses = getDataInt(item, ns, keyUses, 1);

  $player.teleport(new Location($player.getWorld(), x, y, z, yaw, pitch));
  msg($player, "Teleported to saved coordinates: " + x + ", " + y + ", " + z + " (Yaw: " + yaw + ", Pitch: " + pitch + ")");

  // Decrement usage count
  uses -= 1;
  if (uses > 0) {
    setDataInt(item, ns, keyUses, uses);
    msg($player, "Usages left: " + uses);
  } else {
    // Remove data and decrease item amount
    removeData(item, ns, keyX);
    removeData(item, ns, keyY);
    removeData(item, ns, keyZ);
    removeData(item, ns, keyYaw);
    removeData(item, ns, keyPitch);
    removeData(item, ns, keyUses);
    if (hasData(item, ns, keyX) || hasData(item, ns, keyY) || hasData(item, ns, keyZ) || hasData(item, ns, keyYaw) || hasData(item, ns, keyPitch) || hasData(item, ns, keyUses)) {
      msg($player, "Test FAILED: removeData");
    }
    // Decrease item amount
    item.setAmount(item.getAmount() - 1);
    msg($player, "No usages left, item amount decreased.");
  }
}
```

</details>

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

***

## 示例：替换附近的自定义方块

```java
cancelEvent(); // Cancel the event to prevent further processing

var location = $player.getLocation();
var count = 0;

// Iterate through all blocks in a 10x10x10 cube around the player and check isCustom(block) == true
for (var x = -5; x <= 5; x++) {
  for (var y = -5; y <= 5; y++) {
    for (var z = -5; z <= 5; z++) {
      var block = location.getWorld().getBlockAt(location.getBlockX() + x, location.getBlockY() + y, location.getBlockZ() + z);
      if (isCustom(block)) {
        msg($player, "Found a custom block at " + block.getLocation().toString());
        placeBlock(block, "minecraft:stone");
        count++;
      }
    }
  }
}

// Send a message to the player indicating that the script has finished running
msg($player, "Replaced " + count + " custom blocks with stone blocks.");
```
