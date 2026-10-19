---
title: "Java"
source_url: "https://wiki.itemsadder.com/adding-content/scripting/java"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# Java

### 警告

此脚本功能仍在开发中，后续更新可能调整。请持续查阅最新文档，了解更新和兼容性。

## `.java`

这些是纯 Java 代码类。

优点：

* 使用纯 Java，开发者无需学习新语言。
* 无需创建插件或配置复杂的 IDE，即可编写 Java 代码。
* 兼容 VSCode 调试器，可以方便地附加调试。
* 支持库方法、字段等内容的自动补全。
* 容易定位和修复代码错误。

缺点：

* 需要掌握 Java。
* 需要手动编写 package、imports 和逻辑方法，否则智能提示和调试器不会正常工作。

### 物品脚本

此脚本由物品事件调用。\
创建物品脚本时，需要继承提供 `handleEvent` 方法的 ItemScript 类。

```java
package iascript;

import org.bukkit.event.Event;
import org.bukkit.plugin.Plugin;
import org.bukkit.entity.Player;
import org.bukkit.inventory.ItemStack;
import dev.lone.itemsadder.api.*;
import dev.lone.itemsadder.api.scriptinginternal.*;

public class example extends ItemScript {
  public void handleEvent(Plugin plugin, Event event, Player player, CustomStack $customStack, ItemStack $itemStack) {
    // Your code...    
  }
}
```

### 实体脚本

此脚本由实体事件调用。\
创建实体脚本时，需要继承提供 `handleEvent` 方法的 ItemScript 类。

```java
package iascript;

import org.bukkit.event.Event;
import org.bukkit.plugin.Plugin;
import org.bukkit.entity.Player;
import dev.lone.itemsadder.api.*;
import dev.lone.itemsadder.api.scriptinginternal.*;

public class example extends EntityScript {
  public void handleEvent(Plugin plugin, Event event, Player player, CustomEntity customEntity) {
    // Your code...    
  }
}
```
