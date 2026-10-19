---
title: 权限
source_url: https://worldguard.enginehub.org/en/latest/permissions/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 权限 { #permissions }

默认情况下，没有人可以使用 WorldGuard。要让自己、管理人员和玩家使用它，必须授予相应权限。一种方式是给管理人员和管理员 OP 身份，除非[配置](config.md)中禁用了这种行为；也可以通过权限插件授予本页列出的权限节点，后者能更细致地控制权限。

可以为自己和其他管理员授予 `worldguard.*`，以获得 WorldGuard 的全部访问权限。

## 管理人员 { #moderator }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">权限</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">worldguard.notify</td>
<td markdown="span">接收黑名单“notify”动作和“notify”[区域旗标](regions/flags.md)的通知。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.bypass.&lt;world&gt;</td>
<td markdown="span">绕过指定世界中的区域保护，但禁止 PvP 的旗标除外。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.toggle-bypass</td>
<td markdown="span">允许使用 `/rg bypass` 命令切换上述绕过行为，但仍需拥有绕过权限。</td>
</tr>
<tr>
<td markdown="span">worldguard.chest-protection.override</td>
<td markdown="span">绕过[箱子保护](chest-protection.md)，打开受保护的箱子。</td>
</tr>
<tr>
<td markdown="span">worldguard.god.override-regions</td>
<td markdown="span">在 `invincibility` 设为 `DENY` 的区域内仍可保持无敌。</td>
</tr>
<tr>
<td markdown="span">worldguard.auto-invincible</td>
<td markdown="span">配置中的 `auto-invincible` 启用时，加入服务器后自动获得无敌状态。</td>
</tr>
<tr>
<td markdown="span">worldguard.override.potions</td>
<td markdown="span">允许使用 `blocked-potions` 配置选项禁止的药水或效果。</td>
</tr>
<tr>
<td markdown="span">worldguard.override.lighter</td>
<td markdown="span">配置启用 `ignition.block-lighter` 时，仍可使用打火石或火球。</td>
</tr>
<tr>
<td markdown="span">worldguard.override.infinite-stack</td>
<td markdown="span">绕过 `protection.remove-infinite-stacks` 配置选项。</td>
</tr>
</tbody>
</table>

!!! warning "警告"

    如果你拥有 OP 身份或全部权限，就会隐含拥有这些保护绕过权限，从而看起来像保护没有生效。

## 命令 { #commands }

部分命令的说明见[命令](commands.md)页面。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">权限</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">worldguard.god</td>
<td markdown="span">允许使用 `/god` (and `/ungod`)。</td>
</tr>
<tr>
<td markdown="span">worldguard.god.other</td>
<td markdown="span">允许使用 `/god` (and `/ungod`) on others。</td>
</tr>
<tr>
<td markdown="span">worldguard.heal</td>
<td markdown="span">允许使用 `/heal`。</td>
</tr>
<tr>
<td markdown="span">worldguard.heal.other</td>
<td markdown="span">允许使用 `/heal` on others。</td>
</tr>
<tr>
<td markdown="span">worldguard.slay</td>
<td markdown="span">允许使用 `/slay`。</td>
</tr>
<tr>
<td markdown="span">worldguard.slay.other</td>
<td markdown="span">允许使用 `/slay` on others。</td>
</tr>
<tr>
<td markdown="span">worldguard.locate</td>
<td markdown="span">允许使用 `/locate`。</td>
</tr>
<tr>
<td markdown="span">worldguard.stack</td>
<td markdown="span">允许使用 `/stack`。</td>
</tr>
<tr>
<td markdown="span">worldguard.stack.illegitimate</td>
<td markdown="span">允许通过 `/stack` 创建超过正常上限的物品堆叠，例如把 64 个桶堆成一组。</td>
</tr>
<tr>
<td markdown="span">worldguard.fire-toggle.stop</td>
<td markdown="span">允许使用 `/stopfire` and `/allowfire`。</td>
</tr>
<tr>
<td markdown="span">worldguard.halt-activity</td>
<td markdown="span">允许使用 `/stoplag`。</td>
</tr>
<tr>
<td markdown="span">worldguard.reload</td>
<td markdown="span">允许使用 `/wg reload`。</td>
</tr>
<tr>
<td markdown="span">worldguard.report</td>
<td markdown="span">允许使用 `/wg report`。</td>
</tr>
<tr>
<td markdown="span">worldguard.profile</td>
<td markdown="span">允许使用 `/wg profile`。</td>
</tr>
<tr>
<td markdown="span">worldguard.report.pastebin</td>
<td markdown="span">允许将报告或性能分析结果提交到 pastebin 服务。</td>
</tr>
<tr>
<td markdown="span">worldguard.flushstates</td>
<td markdown="span">允许使用 `/wg flushstates`。</td>
</tr>
<tr>
<td markdown="span">worldguard.running</td>
<td markdown="span">允许使用 `/wg running`。</td>
</tr>
<tr>
<td markdown="span">worldguard.debug.event</td>
<td markdown="span">允许使用 the event testing commands under `/wg debug`. Those commands are used to simulate an action so you can trace down, for example, which plugin is blocking player versus player combat. However, this essentially allows a moderator to impersonate another player。</td>
</tr>
</tbody>
</table>

## 区域 { #regions }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">权限</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">worldguard.region.wand</td>
<td markdown="span">允许使用 the [Region Wand](regions/wand.md)。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.load</td>
<td markdown="span">允许使用 `/rg load`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.save</td>
<td markdown="span">允许使用 `/rg save`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.migratedb</td>
<td markdown="span">允许使用 `/rg migratedb`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.migrateuuid</td>
<td markdown="span">允许使用 `/rg migrateuuid`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.migrateheights</td>
<td markdown="span">允许使用 `/rg migrateheights`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.define</td>
<td markdown="span">允许使用 `/rg define`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.claim</td>
<td markdown="span">允许使用 `/rg claim`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.unlimited</td>
<td markdown="span">绕过认领区域的限制。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.list</td>
<td markdown="span">允许使用 `/rg list`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.list.own</td>
<td markdown="span">允许使用 `/rg list` and have it show one own’s regions。</td>
</tr>
</tbody>
</table>

### 按区域设置权限 { #per-region-permissions }

以下权限支持基本权限形式，例如 `worldguard.region.redefine`；也可以只授予玩家作为区域所有者或成员时才生效的细分权限。注意，所有者同时也是成员：

- `worldguard.region.redefine.own.<region name>`

- `worldguard.region.redefine.member.<region name>`

- `worldguard.region.redefine.<region name>`

支持通配符的权限系统可以用它为某一类别下的所有区域授予权限，例如：

- `worldguard.region.redefine.own.*`

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">权限</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">worldguard.region.redefine.*</td>
<td markdown="span">允许使用 `/rg redefine`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.remove.*</td>
<td markdown="span">允许使用 `/rg remove`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.setpriority.*</td>
<td markdown="span">允许使用 `/rg setpriority`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.setparent.*</td>
<td markdown="span">允许使用 `/rg setparent`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.select.*</td>
<td markdown="span">允许使用 `/rg select`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.info.*</td>
<td markdown="span">允许使用 `/rg info` and `/rg flags`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.teleport.*</td>
<td markdown="span">允许使用 `/rg teleport`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.teleportcenter.*</td>
<td markdown="span">允许使用 `/rg teleport -c` when in spectator mode。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.addmember.*</td>
<td markdown="span">允许使用 `/rg addmember`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.addowner.*</td>
<td markdown="span">允许使用 `/rg addowner`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.removemember.*</td>
<td markdown="span">允许使用 `/rg removemember`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.removeowner.*</td>
<td markdown="span">允许使用 `/rg removeowner`。</td>
</tr>
<tr>
<td markdown="span">worldguard.region.locationoverride.*</td>
<td markdown="span">绕过 `regions.location-flags-only-inside-regions` 配置选项。</td>
</tr>
</tbody>
</table>

示例：只允许玩家查询自己拥有的区域信息

使用权限的 own.* 形式：

```text
worldguard.region.info.own.*
```

示例：允许所有玩家使用 `/rg teleport city`

可以在权限中指定区域名称：

```text
worldguard.region.teleport.city.*
```

### 旗标命令 { #flag-command }

`/rg flag` 命令的基本权限为：

```text
worldguard.region.flag.*
```

也可以不授予这个范围较大的权限，改为组合以下两类权限：

- 要决定玩家可以修改*哪些区域*的旗标，可授予下列任意一种权限，其用法与上一节相同：

  `worldguard.region.flag.regions.own.<region name>` `worldguard.region.flag.regions.member.<region name>` `worldguard.region.flag.regions.<region name>`

- 要决定玩家可以设置*哪些类型的旗标*，可授予以下格式的权限：

  `worldguard.region.flag.flags.<flag name>.<flag value>.own.<region name>` `worldguard.region.flag.flags.<flag name>.<flag value>.member.<region name>` `worldguard.region.flag.flags.<flag name>.<flag value>.<region name>`

  `<flag value>` 的示例有 `allow`、`deny`、`unset`（未指定值时）等。更复杂的值也会进行检查，但其中的 `,`、`.`、空白等特殊字符会被省略。

示例：只允许玩家修改自己拥有的区域，且只能修改 `use` 和 `chest-access` 旗标

需要授予以下权限：

```text
worldguard.region.flag.regions.own.*
worldguard.region.flag.flags.use.*
worldguard.region.flag.flags.chest-access.*
```

## 子页面 { #subpages }

- [建造权限](build-perms.md)
