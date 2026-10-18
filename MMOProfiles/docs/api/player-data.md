---
title: 玩家数据
source: https://docs.phoenixdevt.fr/mmoprofiles/api/player-data
source_snapshot: '2026-10-19'
---

# 玩家数据 {#🫅-player-data}

检索到`ProfileProvider`的实例后，你可以使用以下方法访问在线玩家的数据。玩家数据类是`ProfileList`。

```java
UUID playerId = /* TODO */;
ProfileProvider provider = /* see previous page */;

// get player data
ProfileList playerData = provider.getPlayerData(playerId);
```

你还可以使用以下方法访问玩家的档案列表和当前档案。档案类别为`PlayerProfile`。

```java
// get all profiles from player
List<PlayerProfile> profiles = playerData.getProfiles();

// get current profile
@Nullable PlayerProfile currentProfile = playerData.getCurrent();
```

一旦你拥有`PlayerProfile`的实例，你就可以检索有关该档案的信息，包括其运行状况、属性数据、物品栏...大多数方法都非常漂亮straight-forward并且接近其Bukkit等效项。

## 位置图 {#location-maps}

> **信息**
>
> 在代理服务器上使用MMOProfiles会带来一些挑战，包括正确处理玩家位置。玩家可以在具有特定地图的服务器中注销，并在不存在该地图的服务器中重新登录。换句话说，跨后端服务器的地图之间不存在one-to-one对应关系。

在你需要存储Bukkit`Location`的地方，MMOProfiles现在改为存储`LocationMap`。位置映射只是将位置绑定到*服务器组*（参见[下面的](player-data.md#server-groups)）。如果两台服务器位于同一组中，MMOProfiles将为这两台服务器使用相同的位置。管理员有责任正确设置服务器组。

- `PlayerProfile#getLocation()`返回档案在运行服务器的服务器组中的最后位置。请注意，如果服务器组尚未正确设置，并且MMOProfiles发现不存在的世界，则此方法将回退到档案选择位置。
- `PlayerProfile#getLocationMap()`返回`LocationMap`的实例。位置图还用于玩家的最后位置、床生成点和罗盘目标位置。

请注意，MMOProfiles使用自定义对象`WrappedLocation`来存储玩家位置图中的位置。与Bukkit对应的`Location`的唯一区别是`World`对象没有被解析（世界名称保存为字符串），以避免MMOProfiles遇到异常。

### 服务器组 {#server-groups}

通过“服务器组”，我们指的是代理上共享相同**服务器标识符**的所有服务器。服务器标识符是一小段文本，你可以在MMOProfiles`config.yml`中配置它。由于此配置文件是server-specific，因此多个服务器可能具有不同的服务器标识符。

```yml
server-identifier: 'default'
```

具有相同标识符的两台服务器属于同一组。默认情况下，所有服务器都位于标识符为`default`的同一组中。

---

原文：[🫅 Player Data](https://docs.phoenixdevt.fr/mmoprofiles/api/player-data) · 原文归档：2026-10-19
