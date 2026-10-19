---
title: 黑名单
source_url: https://worldguard.enginehub.org/en/latest/blacklist/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 黑名单 { #blacklist }

黑名单可以在玩家进行某项操作（如放置方块、使用物品等）时执行一个或多个动作。用途示例包括：

- 阻止玩家挖掘金矿石

- 发现钻石块时通知所有管理员

- 玩家放置附魔台时向其发送消息

黑名单文件示例：

```text
# Deny lava buckets
[lava_bucket]
ignore-groups=admins,mods
on-use=deny,tell
message=Sorry, you can't use lava buckets!

# Deny some ore
[gold_ore,iron_ore]
ignore-groups=admins
on-break=deny,tell,notify

# No TNT!
[tnt]
ignore-groups=admins
on-place=deny,notify,kick
```

## 黑名单文件 { #blacklist-files }

每个世界都有自己的配置文件：

- `worlds/world/blacklist.txt`

- `worlds/world_nether/blacklist.txt`

- `worlds/mining_world/blacklist.txt`

!!! hint "提示"

    WorldGuard 本身不支持让多个世界共用一个黑名单文件。不过，可以尝试在操作系统中创建“符号链接”，让两个文件路径指向同一个文件。

## 文件格式 { #the-format }

黑名单文件由多个部分组成，格式如下：

```text
[a list of items/blocks to match]
event to watch=what to do
event to watch=what to do
event to watch=what to do
option=value
```

WorldGuard 会忽略以 `#` 开头的行，可以用这些行给自己写备注。

### 匹配语法 { #matching-syntax }

可以通过 [Bukkit 材质列表](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)中的条目匹配物品和方块。用逗号分隔多个条目，即可匹配多种物品和方块：

```text
[oak_wood,brick,glass]
```

## 事件 { #events }

指定要监控的物品或方块后，还必须指定要拦截的情形，以及要执行的动作。

可用事件如下。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">事件</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">on-break</td>
<td markdown="span">匹配的方块被挖掘时</td>
</tr>
<tr>
<td markdown="span">on-destroy-with</td>
<td markdown="span">玩家挖掘时手持匹配的物品或方块</td>
</tr>
<tr>
<td markdown="span">on-place</td>
<td markdown="span">放置匹配的方块时</td>
</tr>
<tr>
<td markdown="span">on-use</td>
<td markdown="span">使用玩家背包中的物品时</td>
</tr>
<tr>
<td markdown="span">on-interact</td>
<td markdown="span">玩家与匹配的方块（门、拉杆等）交互（即右键点击）时</td>
</tr>
<tr>
<td markdown="span">on-drop</td>
<td markdown="span">玩家丢弃匹配的物品时</td>
</tr>
<tr>
<td markdown="span">on-acquire</td>
<td markdown="span">玩家获得匹配的物品时</td>
</tr>
<tr>
<td markdown="span">on-dispense</td>
<td markdown="span">发射器发射匹配的物品时</td>
</tr>
<tr>
<td markdown="span">on-equip</td>
<td markdown="span">玩家装备匹配的物品时</td>
</tr>
</tbody>
</table>

指定事件后，还必须在后面提供一组“动作”，如下所示：

```text
[enchantment_table]
on-place=deny,tell
on-drop=notify
```

### 可用动作 { #available-actions }

每个事件都可以指定多个动作。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">动作</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">deny</td>
<td markdown="span">拒绝该操作（仅在黑名单**未**处于“白名单模式”时生效，后文会解释）</td>
</tr>
<tr>
<td markdown="span">allow</td>
<td markdown="span">允许该操作（仅在黑名单处于“白名单模式”时生效）</td>
</tr>
<tr>
<td markdown="span">notify</td>
<td markdown="span">通知拥有 `worldguard.notify` 权限的管理员</td>
</tr>
<tr>
<td markdown="span">log</td>
<td markdown="span">记录到控制台、文件或数据库</td>
</tr>
<tr>
<td markdown="span">tell</td>
<td markdown="span">告知玩家该操作未获允许</td>
</tr>
<tr>
<td markdown="span">kick</td>
<td markdown="span">踢出玩家</td>
</tr>
<tr>
<td markdown="span">ban</td>
<td markdown="span">封禁玩家</td>
</tr>
</tbody>
</table>

## 选项 { #options }

选项与事件写在同一位置，如下所示：

```text
[enchantment_table]
on-place=deny,tell
message=Sorry, you can't use enchantment tables!
```

这里的 `message` 是一个选项，用于覆盖“tell”动作使用的消息。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">选项</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">ignore-groups</td>
<td markdown="span">不受影响的权限组列表，以逗号分隔</td>
</tr>
<tr>
<td markdown="span">ignore-perms</td>
<td markdown="span">拥有这些权限的玩家不受影响，以逗号分隔；可以自行定义权限！</td>
</tr>
<tr>
<td markdown="span">comment</td>
<td markdown="span">写给自己的消息，执行 `log` 和 `notify` 动作时会输出，用于覆盖默认消息</td>
</tr>
<tr>
<td markdown="span">message</td>
<td markdown="span">显示给玩家的消息，用于覆盖默认消息。在消息中使用 %s，会被替换为物品的英文名称</td>
</tr>
</tbody>
</table>

## 白名单模式 { #whitelist-mode }

通过[配置](config.md)将黑名单切换为白名单模式后，行为将反转。只有带有 `allow` 动作的条目才会被允许。

!!! tip "提示"

    白名单模式的限制可能显得很严格。要放置一个方块，必须允许使用该方块（玩家手中的物品）、与现有方块交互（世界中被点击、用来放置新方块的那个方块），以及放置新方块。根据具体需求，使用[建造权限](build-perms.md)可能更方便，因为它支持在权限节点中使用通配符。

## 示例 { #examples }

示例：阻止某些桶的使用

```text
[lava_bucket,water_bucket,bucket]
on-use=deny,tell
```

示例：踢出使用 TNT 的玩家，并通知管理员

```text
[tnt]
ignore-groups=admins
on-place=deny,notify,kick
```

示例：只允许“obsidian”组的玩家和管理员使用黑曜石

```text
[obsidian]
ignore-groups=admins,obsidian
on-place=deny,tell
on-break=deny,tell
```

## 日志记录 { #logging }

使用 `log` 动作，可以将消息记录到以下几个位置：

- 控制台

- 文件

- 数据库

可以在[配置](config.md)中启用或禁用这些日志输出目标，也可以同时启用多个目标。默认仅启用控制台日志。

### 控制台日志 { #console-logging }

控制台日志只会将日志条目输出到服务器控制台。

### 文件日志 { #file-logging }

文件日志会将日志条目写入文件。在[配置](config.md)中，可以在日志文件路径里使用特殊变量（如当天日期），让日志每天自动轮换。

可使用以下变量：

- %Y 年份（YYYY）

- %m 月份（MM）

- %d 日期（DD）

- %W 一年中的第几周（00-52）

- %H 24 小时制时间（HH）

- %h 12 小时制时间（HH）

- %i 分钟（mm）

- %s 秒（ss）

- %u 用户名

- %% 会转换为单个百分号“%”

### 数据库日志 { #database-logging }

WorldGuard 可以将日志条目写入 MySQL 数据库，但必须先自行创建数据库和数据表。建表所需的 SQL 如下：

```text
CREATE TABLE IF NOT EXISTS `blacklist_events` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `world` varchar(10) NOT NULL,
 `event` varchar(25) NOT NULL,
 `player` varchar(16) NOT NULL,
 `x` int(11) NOT NULL,
 `y` int(11) NOT NULL,
 `z` int(11) NOT NULL,
 `item` int(11) NOT NULL,
 `time` int(11) NOT NULL,
 `comment` varchar(255) DEFAULT NULL,
 PRIMARY KEY (`id`)
);
```
