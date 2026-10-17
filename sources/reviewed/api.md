CMI-API 的源码和 JAR 文件可在 [github.com/Zrips/CMI-API](https://github.com/Zrips/CMI-API) 获取。

在 `pom.yml` 中添加：

```text
<dependency>  <groupId>com.github.Zrips</groupId>  <artifactId>CMI-API</artifactId>  <version>9.8.6.4</version>  <scope>provided</scope></dependency>
```

```text
<repository>  <id>jitpack.io</id>  <url>https://jitpack.io</url></repository>
```


## 玩家与用户对象

大部分玩家相关功能可以通过用户对象访问：

```java
CMIUser user = CMIUser.getUser(player);
```

少数情况下可能返回 `NULL`，使用前需要判空。

可以从用户对象取得离线玩家对象：

```java
Player player = user.getPlayer();
```

即使玩家离线，也能通过该对象访问部分玩家数据。不过，这会实际加载玩家信息，**不建议用这种方式批量加载数百甚至数千名玩家**，否则会给服务器带来负担。

修改玩家数据后，**仅在玩家离线时**，可以调用：

```java
 player.saveData();
```

也可以使用：

```java
CMI.getInstance().save(player);
```

后一种方式会先检查玩家对象是否适合保存。

## 管理器

不少功能通过对应的管理器访问，基本格式为：

```java
CMI.getInstance().get[managerName]();
```

例如，获取传送门管理器：

```java
CMI.getInstance().getPortalManager();
```

## 物品价格

获取物品价格：

```text
// Item stack used to get worthItemStack item;WorthItem worth = CMI.getInstance().getWorthManager().getWorth(item);if (worth == null){  // Worthless item so we can return null or 0D, whatever is needed in your case  return null;}// Buy price used in exploit detectionDouble buyPrice  = worth.getBuyPrice();// Sell price defines actual worth of the fileDouble sellPrice = worth.getSellPrice();
```


设置物品价格：

```text
// Item of which worth value we are gettingItemStack item;// Worth objectWorthItem worth = CMI.getInstance().getWorthManager().getWorth(item);if (worth == null){  // If its null then lets create new one  worth = new WorthItem(item);  // Adding worth to cache  CMI.getInstance().getWorthManager().addWorth(worth);}// Changing pricesworth.setBuyPrice(2D);worth.setSellPrice(1D);// Lets update values in save file CMI.getInstance().getWorthManager().updatePriceInFile(worth);
```


## 自定义事件

- `CMIAfkEnterEvent`：玩家进入 AFK 状态时触发。
- `CMIAfkKickEvent`：玩家因 AFK 即将被踢出服务器时触发。
- `CMIAfkLeaveEvent`：玩家离开 AFK 状态时触发。
- `CMIAnvilItemRenameEvent`：在铁砧中重命名物品时触发。
- `CMIAnvilItemRepairEvent`：使用铁砧修复物品时触发。
- `CMIArmorChangeEvent`：玩家更换盔甲栏物品时触发。
- `CMIAsyncPlayerTeleportEvent`：异步传送玩家时触发，可以取消。
- `CMIBackpackOpenEvent`：打开背包时触发。
- `CMIChequeCreationEvent`：创建支票前触发。
- `CMIChequeUsageEvent`：使用支票时触发。
- `CMIChunkChangeEvent`：玩家切换区块时触发。
- `CMIConfigReloadEvent`：重载配置时触发。
- `CMIEventCommandEvent`：执行事件指令时触发。
- `CMIIpBanEvent`：封禁 IP 时触发。
- `CMIIpUnBanEvent`：解除 IP 封禁时触发。
- `CMIHologramClickEvent`：与可交互的全息图交互时触发。
- `CMIPlayerBanEvent`：玩家被封禁时触发。
- `CMIPlayerFakeEntityInteractEvent`：玩家与虚拟实体交互时触发，通常对应全息图按钮交互。
- `CMIPlayerItemsSellEvent`：通过指令出售物品，或关闭出售界面时触发。
- `CMIPlayerItemsSellEvent`：玩家使用 worth 指令出售物品时触发。
- `CMIPlayerJailEvent`：玩家被关入监狱时触发。
- `CMIPlayerKickEvent`：玩家被踢出时触发。
- `CMIPlayerNickNameChangeEvent`：玩家昵称变更时触发。
- `CMIPlayerOpenArmorStandEditorEvent`：玩家打开盔甲架编辑器时触发。
- `CMIPlayerSitEvent`：玩家坐下时触发。
- `CMIPlayerTeleportRequestEvent`：玩家传送后触发。
- `CMIPlayerUnBanEvent`：解除玩家封禁时触发。
- `CMIPlayerUnjailEvent`：玩家出狱时触发。
- `CMIPlayerUnVanishEvent`：玩家退出隐身状态时触发。
- `CMIPlayerVanishEvent`：玩家进入隐身状态时触发。
- `CMIPlayerWarnEvent`：玩家收到警告时触发。
- `CMIPlayerWarpEvent`：将玩家传送到目标位置前触发。
- `CMIPortalCreateEvent`：创建下界传送门时触发。
- `CMIPortalUseEvent`：使用 CMI 传送门时触发。
- `CMIPvEStartEventAsync`：PvE 开始时触发。
- `CMIPvEEndEventAsync`：PvE 结束时触发。
- `CMIPvPStartEventAsync`：PvP 开始时触发。
- `CMIPvPEndEventAsync`：PvP 结束时触发。
- `CMISelectionEvent`：选择区域时触发。
- `CMISelectionVisualizationEvent`：开始显示选区可视化效果前触发，可以取消。
- `CMIStaffMessageEvent`：发送管理组消息时触发。
- `CMIUserBalanceChangeEvent`：使用 CMI 经济系统时，在玩家余额变化时触发。变更类型包括 setBalance、Withdraw、Deposit。
