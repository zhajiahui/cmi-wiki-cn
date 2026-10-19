---
title: "示例"
source_url: "https://wiki.itemsadder.com/adding-content/scripting/java/examples"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 示例

需要 ItemsAdder 4.0.13 或更高版本。

仅兼容 `.java` 脚本类型。

此示例脚本会：

* 向控制台输出当前使用的自定义物品 ID
* 向玩家发送问候消息
* 给予玩家钻石，并发送相关消息
* 如果可用，给予玩家 `iasurvival` 内容包中的红宝石，并发送相关消息

```java
package iascript;

import org.bukkit.event.Event;
import org.bukkit.plugin.Plugin;
import org.bukkit.Material;
import org.bukkit.entity.Player;
import org.bukkit.inventory.ItemStack;
import dev.lone.itemsadder.api.*;
import dev.lone.itemsadder.api.scriptinginternal.*;
import static dev.lone.itemsadder.api.scriptinginternal.ScriptingUtils.*;

public class example extends ItemScript {
  public void handleEvent(Plugin plugin, Event event, Player player, CustomStack $customStack, ItemStack $itemStack) {
    log("Player " + player.getName() + " interacted with item: " + $customStack.getNamespacedID());
    
    player.sendMessage("Hello from example script!");

    player.getInventory().addItem(new ItemStack(Material.DIAMOND, 1));
    player.sendMessage("You have been given a diamond!");

    var customStack = CustomStack.getInstance("iasurvival:ruby");
    if(customStack != null) {
      log("Custom stack found: " + customStack.getNamespacedID());
      player.getInventory().addItem(customStack.getItemStack());
      player.sendMessage("You have been given a ruby!");
    } else {
      log("Custom stack not installed on the server: iasurvival:ruby");
      player.sendMessage("Ruby item not found.");
    }
    
  }
}
```
