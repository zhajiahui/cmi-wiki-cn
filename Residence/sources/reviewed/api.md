## 开发者 API

Residence 的最新开发版提供 API，可以添加自定义领地标志、处理这些标志，并使用自定义 Bukkit 事件。开发 Residence 附属插件时，可以在论坛主题中寻求帮助。如果插件需要的 API 功能尚未提供，也可以在 Residence 主论坛主题中提出，作者会尝试添加。下载文件见 Download 页面。

## 添加自定义标志

以下说明假定你熟悉 Bukkit，知道如何将 `.jar` 文件作为库加入项目，并了解 Bukkit 的 Listener 类。

这里以向 Residence 添加 `build` 标志为例。

### 第 1 步：添加依赖

将 `Residence.jar` 作为库加入插件项目。

### 第 2 步：注册标志

通过 `FlagPermissions` 类，让 Residence 知道 `build` 是有效标志：

```java
FlagPermissions.addFlag("build");
```

### 第 3 步：处理标志

添加的是 `build` 标志，因此需要在 Bukkit 的 `onBlockPlace()` 事件监听器中加入处理代码。

先判断方块放置的位置是否属于某块领地。尝试取得该位置的 `ClaimedResidence` 对象：

```java
Location loc = event.getBlock().getLocation();
ClaimedResidence res = Residence.getResidenceManager().getByLoc(loc);
```

接着检查返回值是否为 `null`：

```java
if(res!=null)
```

`res` 为 `null` 表示该位置没有领地；否则，需要检查这块领地是否允许 `build`。先取得领地权限：

```java
ResidencePermissions perms = res.getPermisssions();
```

然后检查是否允许建造，不允许时取消事件：

```java
String playerName = event.getPlayer().getName();
```

```java
boolean defaultValue = true;

boolean hasPermission = perms.playerHas(playerName, "build", defaultValue);

if(!hasPermission)
 event.setCancelled(true);
```

### 第 4 步：支持世界权限（可选）

如果这个标志也需要支持世界权限，即在领地外对整个世界设置，就需要在 `res == null` 时另作检查。先取得世界权限列表：

```java
String worldName = event.getBlock().getWorld().getName();
FlagPermissions perms = Residence.getWorldPermisssions(worldName);
```

再使用第 3 步中的 `playerHas()` 检查标志：

```java
boolean hasPermission = perms.playerHas(playerName, "build", defaultValue);

if(!hasPermission)
  event.setCancelled(true);
```

### 第 5 步：合并领地与世界检查

如果不需要区分某个位置是否存在领地，只想判断玩家能否在指定位置执行操作，可以直接取得 `FlagPermissions` 对象：

```java
Location loc = event.getBlock().getLocation();
FlagPermissions = Residence.getPermsByLoc(loc);
```

该位置没有领地时，会自动使用世界权限，相当于将第 3、4 步合并。

## 自定义 Bukkit 事件

可以监听多个自定义 Bukkit 事件。使用时，创建继承 Bukkit `CustomEventListener` 的类，再重写 `onCustomEvent()`：

```java
public class MyListener extends CustomEventListener {
  @Override
  public void onCustomEvent(Event event) {
    //do stuff
  }
}
```

创建这个类的实例，然后在插件主类中向 Bukkit 注册：

`getServer().getPluginManager().registerEvent(Event.Type.CUSTOM_EVENT, myListener, Priority.Normal, this);`

注册后，就可以接收下一节列出的 Residence 事件。

## Residence 的 Bukkit 事件

以下是当前可以监听的 Residence 事件：

- `ResidenceCommandEvent`：玩家执行 Residence 注册的命令时触发。
- `ResidenceFlagChangeEvent`：领地标志发生变化时触发，可以取消。
- `ResidenceFlagCheckEvent`：检查领地标志时触发，可以覆盖返回值。
- `ResidenceOwnerChangeEvent`：领地主人发生变化时触发。
- `ResidenceCreationEvent`：创建领地时触发，可以取消。
- `ResidenceSubzoneCreationEvent`：创建子领地时触发，可以取消。
- `ResidenceRenameEvent`：重命名领地时触发。
- `ResidenceSizeChangeEvent`：调整领地大小时触发。
- `ResidenceChatEvent`：玩家发送领地聊天消息时触发。
- `ResidenceTPEvent`：玩家传送到领地时触发。
- `ResidenceAreaAddEvent`：向领地添加区域时触发。
- `ResidenceAreaDeleteEvent`：从领地移除区域时触发。
- `ResidenceDeleteEvent`：删除领地时触发，可以查询删除原因，也可以取消。
- `ResidenceRentEvent`：租赁相关操作发生时触发，可以查询原因，也可以取消。之后还会继续增加事件。
- `ResidenceChangedEvent`：玩家所在领地变化时触发，包括子领地切换。
- `ResidenceRaidEndEvent`：领地战争结束时触发。
- `ResidenceRaidPreStartEvent`：正式交战前触发。
- `ResidenceRaidStartEvent`：领地战争开始时触发。

在 `CustomEventListener` 中，可以用 Java 的 `instanceof` 判断具体事件，再转换成相应类型：

```java
if(event instanceof ResidenceCommandEvent)
{
  ResidenceCommandEvent e = (ResidenceCommandEvent) event;
  //do stuff
}
else if(event instanceof ResidenceFlagChangeEvent)
{
  ResidenceFlagChangeEvent e = (ResidenceFlagChangeEvent) event;
  //do stuff
}
```

其他事件的判断方式相同。所有 Residence 事件都可以通过 `getResidence()` 取得对应的 `ClaimedResidence` 对象。

## 其他常用 API

Residence 的各个子系统都有对应的管理器，可以通过 `Residence` 主类的静态方法取得。

`ResidenceManager`：放置和管理所有领地。

```java
ResidenceManager rmanager = Residence.getResidenceManager();
```

`SelectionManager`：管理创建领地时使用的选区点。

```java
SelectionManager smanager = Residence.getSelectionManager();
```

`EconomyManager`：取得 Residence 所连接的经济插件接口。

```java
EconomyInterface econ = Residence.getEconomyManager();
```

`ConfigManager`：保存配置文件中的设置。

```java
ConfigManager cmanager = Residence.getConfigManager();
```

`PermissionManager`：保存配置中的权限组，并连接服务器使用的权限插件。

```java
PermissionManager pmanager = Residence.getPermissionManager();
```

`WorldFlagManager`：保存应用于整个世界的标志。

```java
WorldFlagManager wmanager = Residence.getWorldFlags();
```

还有其他管理器，这里列出的是较常用的几个。

## 手动启用 Residence

如果你的插件名称在字母顺序上排在 R 之前，它可能会先于 Residence 启用。如果需要立即调用 Residence 的功能，而 Residence 还没有完成初始化，就可能出现问题。可以先检查 Residence 是否存在、是否已启用：

```java
PluginManager pm = getServer().getPluginManager();
Plugin p = pm.getPlugin("Residence");
if(p!=null)
{
  if(!p.isEnabled())
  {
    System.out.println(" - Manually Enabling Residence!");
    pm.enablePlugin(p);
  }
}
else
{
  System.out.println(" - Residence NOT Installed, DISABLED!");
  this.setEnabled(false);
}
```

## 检查玩家能否放置方块

```java
ResidencePlayer rPlayer = Residence.getInstance().getPlayerManager().getResidencePlayer(attacker); 
boolean canPlace = rPlayer.canPlaceBlock(Block block, boolean inform);
```

## 检查玩家能否破坏方块

```java
ResidencePlayer rPlayer = Residence.getInstance().getPlayerManager().getResidencePlayer(attacker); 
boolean canBreak = rPlayer.canBreakBlock(Block block, boolean inform);
```

## 检查玩家能否伤害实体

```java
ResidencePlayer rPlayer = Residence.getInstance().getPlayerManager().getResidencePlayer(attacker); 
boolean canDamage = rPlayer.canDamageEntity(Entity entity, boolean inform);
```
