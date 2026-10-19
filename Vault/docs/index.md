---
title: "Vault"
source_kind: plugin-overview
translation_review: reviewed
---

# Vault

Vault 为其他插件提供经济、权限和聊天相关服务的统一接口与桥接。账户余额等经济功能由注册到 Vault 的经济服务提供方实现。

随包版本为 **`1.7.3-b131`**。Vault 自身未声明必需插件或软依赖。本批 Citizens、ItemsAdder、MMOItems、Multiverse-Core、MythicMobs、NeigeItems、WorldEdit 将 Vault 列为软依赖（`softdepend`），没有插件将其列为 `depend`。

## 查看服务与转换经济数据

| 命令 | 用途 | 权限 |
| --- | --- | --- |
| `/vault-info` | 查看 Vault 及已注册服务的信息 | `vault.admin` |
| `/vault-convert [economy1] [economy2]` | 将 economy1 的数据转换到 economy2 | `vault.admin` |

`vault.admin` 的默认值为 `op`。更新检查等随包选项见[配置说明](configuration/index.md)。

## 官方资料

- [Vault 官方 README](https://github.com/MilkBowl/Vault/blob/460cb21c6215433da526192720de40b6662f5f99/README.md)
- [命令与权限声明](https://github.com/MilkBowl/Vault/blob/460cb21c6215433da526192720de40b6662f5f99/plugin.yml)
- [服务查询与配置初始化源码](https://github.com/MilkBowl/Vault/blob/460cb21c6215433da526192720de40b6662f5f99/src/net/milkbowl/vault/Vault.java)
