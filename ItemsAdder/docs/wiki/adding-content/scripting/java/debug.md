---
title: "调试"
source_url: "https://wiki.itemsadder.com/adding-content/scripting/java/debug"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 调试

需要 ItemsAdder 4.0.13 或更高版本。

仅兼容 `.java` 脚本类型。

#### 步骤 1

继续之前，请先按[自动补全设置教程](autocompletion.md)操作。

#### 步骤 2

安装 [Debugger for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug)。

如果已安装 [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)，就已经包含此扩展。

#### 步骤 3

在与 Java 包名匹配的文件夹中创建脚本文件。

例如，此文件：

`ItemsAdder/contents/test/iascript/example.java`

必须使用：

```java
package iascript;
```

文件夹必须与包名一致，否则 Java 断点可能无法正常工作。

```java
package iascript;

import org.bukkit.Material;
import org.bukkit.event.Event;
import org.bukkit.plugin.Plugin;
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
    }
}
```

创建引用该脚本的 `.yml` 文件：

```yaml
info:
  namespace: test

items:
  example_execute_script:
    name: Example Execute Script
    resource:
      material: DIAMOND
      generate: false
      model_path: minecraft:item/diamond
    script:
      enabled: true
      path: iascript/example
```

#### 步骤 4

更改服务器启动参数，加入 JDWP 调试选项。

使用空闲端口，并与 Minecraft 服务器端口区分。

```bash
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:55213 -jar server.jar nogui
```

如果希望服务器启动前等待调试器连接，使用 `suspend=y`。

#### 步骤 5

新建文件 `.vscode/launch.json`（不要遗漏开头的点！）。

将端口 `55213` 改为你自己的调试端口。

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "java",
      "name": "Attach to Minecraft Server",
      "request": "attach",
      "hostName": "localhost",
      "port": 55213
    }
  ]
}
```

#### 步骤 6

启动服务器，再从 VSCode 启动 `Attach to Minecraft Server` 调试配置。

现在可以在 Java 脚本文件中设置断点。
