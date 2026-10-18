---
title: 权限节点
---

# 权限节点

拥有下列权限的玩家，可以使用对应的插件功能。

例如，JohnDoe 登录时拥有 `residence.command.list.others`，就可以执行 `/res listall` 查看所有玩家的领地。

星号 `*` 是通配符。授予 `residence.*`，表示授予所有以 `residence.` 开头的权限。`-residence.admin.*` 表示禁止使用所有管理员命令。

标有 `(OP)` 的权限还要求玩家列在 `ops.json` 中。

| 权限节点 | 作用 |
| --- | --- |
| `residence.chatcolor` | 允许更改领地聊天的文字颜色。 |
| `residence.chatprefix` | 允许更改领地聊天的前缀。 |
| `residence.chatkick` | 允许将玩家踢出领地聊天频道。 |
| `residence.permisiononerror` | 允许在错误消息中查看缺少的权限。 |
| `residence.command.message.enter` | 允许更改进入领地时的消息。 |
| `residence.command.message.leave` | 允许更改离开领地时的消息。 |
| `residence.command.message.enter.remove` | 允许移除进入领地时的消息。 |
| `residence.command.message.leave.remove` | 允许移除离开领地时的消息。 |
| `residence.cleanbypass` | 防止领地被自动清理。 |
| `residence.worldguard.[region]` | 允许在指定区域内创建领地。 |
| `residence.flag.[flagname]` | 允许使用指定的领地标志。 |
| `residence.tpdelaybypass` | 允许绕过传送延迟。 |
| `residence.backup` | 允许使用 backup 标志，将领地保存为 Schematics 文件。 |
| `residence.admin.tp` | 允许传送进入禁止传送的领地。 |
| `residence.topadmin` | 将玩家设为 Residence 最高管理员。 |
| `residence.admin` | 将玩家设为 Residence 管理员。 |
| `residence.admin.move` | 允许在禁止移动的领地内移动。 |
| `residence.newguyresidence` | 首次放置箱子时创建领地。 |
| `residence.bypass.ignorey` | 允许忽略 Y 坐标限制。 |
| `residence.bypass.ignoreyinsubzone` | 允许忽略子领地限制。 |
| `residence.bypass.destroy` | 允许绕过 destroy 标志。 |
| `residence.bypass.build` | 允许绕过 build 标志。 |
| `residence.bypass.container` | 允许绕过 container 标志。 |
| `residence.bypass.use` | 允许绕过 use 标志。 |
| `residence.bypass.fly` | 允许绕过 fly 标志。 |
| `residence.bypass.nofly` | 允许绕过 nofly 标志。 |
| `residence.bypass.tp` | 允许绕过 command 标志。 |
| `residence.bypass.command` | 允许绕过 command 标志。 |
| `residence.bypass.itempickup` | 允许绕过 itempickup 标志。 |
| `residence.buy` | 允许购买领地。 |
| `residence.sell` | 允许出售领地。 |
| `residence.max.res.unlimited` | 不限制领地数量。 |
| `residence.max.res.[number]` | 设置领地数量上限。 |
| `residence.max.subzones.unlimited` | 不限制子领地数量。 |
| `residence.max.subzones.[number]` | 设置子领地数量上限。 |
| `residence.max.subzonedepth.unlimited` | 不限制子领地嵌套层数。 |
| `residence.max.subzonedepth.[number]` | 设置子领地嵌套层数上限。 |
| `residence.max.rents.unlimited` | 不限制租用领地的数量。 |
| `residence.max.rents.[number]` | 设置租用领地的数量上限。 |
| `residence.group.[groupname]` | 设置玩家所属的 Residence 权限组。 |
| `residence.market.evict` | 允许将租客从租用的领地中驱逐。 |
| `residence.rename` | 允许重命名领地。 |
| `residence.select` | 允许选择领地区域。 |
| `residence.select.auto.others` | 允许为其他玩家切换自动选区。 |
| `residence.resize` | 允许调整领地大小。 |
| `residence.create` | 允许创建领地。 |
| `residence.create.subzone` | 允许创建子领地。 |
| `residence.randomtp` | 允许使用 rt 命令。 |
| `residence.randomtp.admin` | 允许对其他玩家使用 rt 命令。 |
| `residence.randomtp.cooldownbypass` | 允许绕过随机传送命令的冷却时间。 |
| `residence.randomtp.delaybypass` | 允许绕过随机传送命令的执行延迟。 |
| `residence.delete` | 允许删除领地。 |
| `residence.delete.subzone` | 允许删除子领地。 |
| `residence.command.kick.bypass` | 允许绕过领地踢出限制。 |
| `residence.command.contract.subzone` | 允许缩小子领地。 |
| `residence.command.expand.subzone` | 允许扩大子领地。 |
| `residence.versioncheck` | 有新版本时显示提示。 |
| `residence.command.[commandname]` | 允许使用指定命令。 |
| `residence.command.[commandname].others` | 允许对其他玩家执行指定命令。 |

---

[查看原文](https://www.zrips.net/residence/permissions/)
