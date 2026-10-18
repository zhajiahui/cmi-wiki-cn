---
title: Maven
source: https://docs.phoenixdevt.fr/mmocore/api/maven
source_snapshot: '2026-10-19'
---

# Maven {#📦-maven}

## 存储库 {#repository}

我们为所有 MMO 插件提供了一个Maven存储库，其中包含API版本。将我们的存储库添加到你的存储库列表中：

```xml
<repository>
    <id>phoenix</id>
    <url>https://nexus.phoenixdevt.fr/repository/maven-public/</url>
</repository>
```

## 依赖性 {#dependency}

在你的Maven`pom.xml`中包含以下依赖项

```xml
<dependency>
    <groupId>net.Indyuce</groupId>
    <artifactId>MMOCore-API</artifactId>
    <version>1.13.1-SNAPSHOT</version>
    <scope>provided</scope>
</dependency>
```

---

原文：[📦 Maven](https://docs.phoenixdevt.fr/mmocore/api/maven) · 原文归档：2026-10-19
