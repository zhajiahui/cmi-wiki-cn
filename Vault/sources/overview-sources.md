---
title: "Vault 官方资料摘录"
source_kind: plugin-overview
translation_review: reviewed
---

# Vault 官方资料摘录

核对日期：2026-10-19。随包版本为 `1.7.3-b131`。

## 插件之间的服务桥接

来源：[官方 README](https://github.com/MilkBowl/Vault/blob/460cb21c6215433da526192720de40b6662f5f99/README.md)。

> Because Vault provides a bridge to other plugins, their binaries will be required to build from.

来源：[Vault.java](https://github.com/MilkBowl/Vault/blob/460cb21c6215433da526192720de40b6662f5f99/src/net/milkbowl/vault/Vault.java)。源码通过 Bukkit 的 `ServicesManager` 查询 `Economy.class`、`Permission.class` 和 `Chat.class` 的服务提供方，分别用于经济、权限和聊天服务。此处的桥接身份没有改写为完整经济系统。

## 命令与权限

来源：[官方 plugin.yml](https://github.com/MilkBowl/Vault/blob/460cb21c6215433da526192720de40b6662f5f99/plugin.yml)。

> Displays information about Vault

> Converts all data in economy1 and dumps it into economy2

两段说明分别对应 `vault-info` 和 `vault-convert`。官方用法为 `/vault-convert [economy1] [economy2]`，两条命令均声明 `permission: vault.admin`；`vault.admin` 的 `default` 为 `op`。

## 配置资料

来源：[官方 README](https://github.com/MilkBowl/Vault/blob/460cb21c6215433da526192720de40b6662f5f99/README.md)。

> If you wish to perform configuration changes, this can be done via a configuration file but should not be necessary in most cases.

来源：[初始化源码](https://github.com/MilkBowl/Vault/blob/460cb21c6215433da526192720de40b6662f5f99/src/net/milkbowl/vault/Vault.java)。

```java
getConfig().addDefault("update-check", true);
```

所取 README 提到 “Advanced Configuration”，但未包含完整的同名章节，因此没有补写未经确认的配置手册地址。

## 随包依赖声明

随包 JAR 的 `plugin.yml` 中，Vault 的 `depend` 与 `softdepend` 均为空。Citizens、ItemsAdder、MMOItems、Multiverse-Core、MythicMobs、NeigeItems、WorldEdit 的 `softdepend` 包含 Vault；本批没有插件在 `depend` 中声明 Vault。
