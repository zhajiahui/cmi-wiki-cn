---
title: API 用法
source: https://docs.phoenixdevt.fr/mmoprofiles/api/usage
source_snapshot: '2026-10-19'
---

# API 用法 {#🪣-api-usage}

主要的API类是`ProfileProvider`。你可以使用Bukkit的服务提供者访问此接口的MMOProfiles实现。

```java
ProfileProvider provider = Bukkit.getServicesManager().getRegistration(ProfileProvider.class).getProvider();
```

当插件启用时，该服务由MMOProfiles提供。如果你想从插件的`onEnable`内部访问此服务，你需要在插件`plugin.yml`中将MMOProfiles声明为软（或硬）依赖项。

```yml
softdepend: [ ..., MMOProfiles ]
```

## 检查Proxy-mode档案是否打开 {#check-if-proxy-mode-profiles-is-on}

以下代码片段可用于检查MMOProfiles当前是否正在运行proxy-mode档案。

```java
// possible values: PROXY, LEGACY, NONE
// are proxy-mode profiles enabled?
boolean proxyMode = MythicLib.plugin.getProfileMode() == ProfileMode.PROXY;
```

---

原文：[🪣 API Usage](https://docs.phoenixdevt.fr/mmoprofiles/api/usage) · 原文归档：2026-10-19
