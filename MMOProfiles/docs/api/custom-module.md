---
title: 自定义数据模块
source: https://docs.phoenixdevt.fr/mmoprofiles/api/custom-module
source_snapshot: '2026-10-19'
---

# 自定义数据模块 {#📦-custom-data-modules}

档案数据模块对应于拥有profile-dependant数据的插件。所有 MMO 插件都有自己的档案数据模块。当玩家选择档案时，MMOProfiles要求所有档案数据模块加载所选玩家档案的档案数据，对于给定的玩家。  在所有档案数据模块成功加载其profile-dependant数据之前，MMOProfiles不会让用户玩（也不会退出档案选择区域）。

如果你有一个拥有profile-dependant数据的插件（任务进度、自定义物品栏、玩家升级、职业等...），你将必须实现自己的`ProfileDataModule`并将其注册到MMOProfiles中。

## 实施`ProfileDataModule` {#implement-profiledatamodule}

`ProfileDataModule`接口有两种方法：

- `#getOwningPlugin()`应该返回插件的主实例
- `#getId()`应该返回唯一的name-spaced密钥。MMOProfiles将使用它来解析档案占位符（见下文）。

### 值得聆听的活动 {#events-to-listen-to}

MMOProfiles期望每个档案数据模块侦听以下事件。你将在[以下 Wiki 页面](events.md)中找到有关这些事件的更多信息。

- `ProfileSelectEvent`在玩家选择档案时调用。
- 当玩家取消选择档案时调用`ProfileUnloadEvent`。
- `ProfileCreateEvent`在玩家创建新档案时调用。
- `ProfileRemoveEvent`在玩家删除档案时调用。

这些事件有一个名为`#validate(ProfileDataModule)`的方法，当你的插件完成加载/卸载profile-specific数据时需要调用该方法（将你的档案数据模块实例作为参数传递）。

> **提示**
>
>`ProfileDataModule`接口的参考实现可以在`DefaultProfileDataModule`类的MythicLib中找到。

以下代码片段为`ProfileSelectEvent`和`ProfileUnloadEvent`上应该发生的情况提供了pseudo-code。选择档案后，将异步加载档案数据，然后调用`#validate`方法。  当所有已注册的档案数据模块都调用此方法时，MMOProfiles仅允许玩家加入服务器。取消选择档案时，将异步卸载并保存档案数据，然后调用`#validate`方法。

```java
Plugin myPlugin;
ProfileDataModule dataModule; // MMOProfiles API
PlayerDataManager manager; // MMO plugin API

@EventHandler
public void onProfileSelection(ProfileSelectEvent event) {
    PlayerData playerData = manager.get(event.getPlayer());
    manager.loadData(playerData).thenAccept(Tasks.sync(plugin, v -> {
        // ...
        event.validate(dataModule);
    }));
}

@EventHandler
public void onProfileUnload(ProfileUnloadEvent event) {
    manager.unregister(event.getPlayer()).thenAccept(Tasks.sync(plugin, v -> {
        // ...
        event.validate(dataModule);
    }));
}
```

### 为何以及何时验证玩家会话 {#why-and-when-to-validate-player-sessions}

当玩家加入服务器并选择档案时，MMOProfiles会等待所有插件加载其玩家数据，然后再传送玩家。同时，它们通常被留在“档案选择黑匣子”中，以避免在不一致的玩家数据状态期间发生不必要的交互。

你实际上不需要立即调用`#validate`方法。事实上，我们建议你推迟调用它，直到从数据库加载玩家数据为止。

> **警告**
>
>`#validate`方法必须从主服务器线程调用，否则会引发异常。

未能调用`#validate`（例如，由于之前未处理的异常）将导致玩家的会话冻结，并且玩家陷入档案选择困境。会话不活动几秒钟后，MythicLib将开始在控制台中引发“幽灵会话”警告。

## 注册你的`ProfileDataModule`实例 {#register-your-instance-of-profiledatamodule}

在插件的`#onEnable`中使用以下方法来注册`ProfileDataModule`的实例。如果你的模块是`Listener`的实例，则MMOProfiles将为你注册其事件。

```java
ProfileProvider provider = /* profile provider */;
ProfileDataModule yourProfileDataModule = /* TODO */;
provider.registerModule(yourProfileDataModule);
```

---

原文：[📦 Custom Data Modules](https://docs.phoenixdevt.fr/mmoprofiles/api/custom-module) · 原文归档：2026-10-19
