---
title: "Vault 官方使用说明"
source_url: "https://dev.bukkit.org/projects/vault"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "Vault 460cb21c6215433da526192720de40b6662f5f99；官方项目页 2026-10-19 快照"
---

# Vault 官方使用说明

Vault 提供权限、聊天与经济 API，让插件可以方便地接入这些系统，而无需分别接入或依赖各个插件。它源于作者对 Register 和当时 Permissions API 运作方式的不满：它们或缺少功能，或实现过于复杂。Vault 希望以直观的方式解决这些问题，为插件可能使用的各类系统提供支持。

**配置：**

- update-check
  - 开启或关闭更新检查器

**权限：**

- vault.admin
  - 允许使用 Vault 信息和转换命令
  - 默认授予 OP
- vault.update
  - Vault 过时时，拥有此权限的人会收到通知
  - 默认授予 OP
  - **在 permissions.yml 中设为 false，也会关闭控制台的版本检查消息**

**此页面列出的 Vault 支持项：**

---

- **权限：** Permissions 3, [bPermissions](http://dev.bukkit.org/server-mods/bpermissions/), [PEX](http://dev.bukkit.org/server-mods/permissionsex), [GroupManager](http://dev.bukkit.org/server-mods/groupmanager), [PermissionsBukkit](http://dev.bukkit.org/server-mods/permbukkit), [zPermission](http://dev.bukkit.org/server-mods/zpermissions), SimplyPerms, [Privileges](http://dev.bukkit.org/server-mods/Privileges), [DroxPerms](http://dev.bukkit.org/server-mods/DroxPerms), xPerms
- **经济：** [iConomy](http://dev.bukkit.org/server-mods/iconomy) 4,5,6, [BOSEconomy](http://dev.bukkit.org/server-mods/boseconomy) 6 & 7, EssentialsEcon, 3Co, [MultiCurrency](http://dev.bukkit.org/server-mods/multicurrency), [MineConomy](http://dev.bukkit.org/server-mods/mineconomy), [eWallet](http://dev.bukkit.org/server-mods/ewallet), [EconXP](http://dev.bukkit.org/server-mods/econxp/), [CurrencyCore](http://dev.bukkit.org/server-mods/currency/), [CraftConomy](http://dev.bukkit.org/server-mods/craftconomy/), AEco, [Gringotts](http://dev.bukkit.org/server-mods/gringotts/)
  - 只有 CraftConomy、CurrencyCore、BOSE 和 iCo6 提供银行支持
  - iCo6/CurrencyCore 将玩家账户与银行账户合并。若需要完整银行功能，建议使用 BOSE。
  - iCo6 的平面文件存储存在严重错误，使用风险自行承担
- **聊天：** [mChat](http://dev.bukkit.org/server-mods/mchat), iChat, [bPermissions](http://dev.bukkit.org/server-mods/bpermissions/), [PEX](http://dev.bukkit.org/server-mods/permissionsex), P3, [DroxPerms](http://dev.bukkit.org/server-mods/DroxPerms)
- 其他经济或权限系统可能内置了 Vault 支持，请向对应项目确认。

---

- JavaDocs: [http://milkbowl.github.io/VaultAPI](http://milkbowl.github.io/VaultAPI)
- GitHub（源码）： <https://github.com/MilkBowl/Vault/>
- GitHub（源码）： <https://github.com/MilkBowl/VaultAPI/>

---

此插件使用 Hidendra 的插件统计系统。除非选择退出，否则会收集以下信息并发送至 bstats.org：

- 唯一标识符
- 服务器使用的 Java 版本
- 服务器为离线模式还是在线模式
- 插件版本
- 服务端版本
- 操作系统版本、名称和架构
- CPU 核心数
- 在线玩家数
- 统计组件版本
- 当前使用的聊天、经济和权限接入项。

要退出此服务，编辑 plugins/bstats/config.yml，将 opt-out 改为 true。

---
