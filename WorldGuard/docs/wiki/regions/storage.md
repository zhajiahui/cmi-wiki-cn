---
title: 存储驱动
source_url: https://worldguard.enginehub.org/en/latest/regions/storage/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 存储驱动 { #storage-drivers }

区域数据支持以下存储方式：

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">存储驱动</th>
<th markdown="span">优点</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">YAML</td>
<td markdown="block">

<ul markdown="block"> <li markdown="span"><p markdown="span">无需数据库服务器。</p> </li> <li markdown="span"><p markdown="span">直接修改文件即可手动编辑区域数据。</p> </li> <li markdown="span"><p markdown="span">便于随世界一起备份。</p> </li> <li markdown="span"><p markdown="span">完整加载和保存的速度快。</p> </li> </ul>

</td>
</tr>
<tr>
<td markdown="span">MySQL</td>
<td markdown="block">

<ul markdown="block"> <li markdown="span"><p markdown="span">便于其他系统访问数据。</p> </li> <li markdown="span"><p markdown="span">保存时仅写入发生变化的数据。</p> </li> </ul>

</td>
</tr>
</tbody>
</table>

!!! note "注意"

    目前不支持 PostgreSQL、SQL Server、SQLite 等其他支持 SQL 的数据库。

!!! warning "警告"

    区域存储的 SQL 支持由第三方开发者贡献，尽管经过多次大幅重写，使用时仍存在严重问题。强烈建议不要使用 SQL 保存 WorldGuard 区域。

    **如果已经使用 SQL 存储区域，请通过下方介绍的迁移命令转回 YAML。WorldGuard 将在未来版本移除区域存储的 SQL 支持。**

## 切换驱动 { #switching-drivers }

默认使用 YAML 文件。

可以在[配置](../config.md)中启用 `regions.sql.use`，切换到 MySQL，并同时停止使用 YAML。切换后会自动创建数据库表，但请先为数据库用户授予必要的 SQL 权限。

!!! warning "警告"

    强烈建议在切换驱动前备份。

### 迁移数据 { #migrating-data }

如果只是切换存储驱动，新存储中没有数据，就会发现区域全部不见。可以使用专门的迁移命令在两种存储之间转移数据；既可在切换新驱动**之前**迁移，也可在切换**之后**迁移。

使用 `/rg migratedb from to`，指定来源和目标驱动。例如，从 YAML 迁移到 MySQL：

```text
/rg migratedb yaml mysql
```

请确认目标数据库为空。

## 存储驱动 { #id1 }

!!! warning "警告"

    如果在 WorldGuard 之外手动修改数据，记得先备份。

### YAML { #yaml }

YAML 区域数据位于 WorldGuard 配置目录中各世界文件夹内的“region.yml”。可在服务器运行时修改，再用 `/rg load` 重新加载。

区域文件的结构如下例所示：

```text
regions:
    test:
        min: {x: 1730.0, y: 0.0, z: -169.0}
        max: {x: 1742.0, y: 255.0, z: -158.0}
        members:
            players: [bobby]
            unique-ids: [0ea8eca3-dbf6-47cc-9d1a-c64551ca975c]
        flags: {use: allow, greeting: Welcome!, pvp: allow, pvp-group: MEMBERS}
        owners:
            groups: [admins]
        type: cuboid
        priority: 4
    __global__:
        members: {}
        flags: {}
        owners: {}
        type: global
        priority: 0
```

通常存储 UUID，但部分命令也可通过 `-n` 添加玩家名称。

### MySQL { #mysql }

- 同一组数据表只能由一个服务器实例使用。

- 可以设置表前缀，让同一个数据库用于不同的数据集或安装实例。

- 修改在事务中执行，出错时会回滚。

- 默认情况下，WorldGuard 只保存区域数据的变化，不会重新保存整个区域数据集。

所用数据表如下：

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">数据表</th>
<th markdown="span">用途</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">region</td>
<td markdown="span">区域数据，包括形状、优先级和父区域信息。</td>
</tr>
<tr>
<td markdown="span">region_cuboid</td>
<td markdown="span">长方体区域数据，包含边界。</td>
</tr>
<tr>
<td markdown="span">region_poly2d</td>
<td markdown="span">多边形区域数据，包含最小和最大 Y 值。</td>
</tr>
<tr>
<td markdown="span">region_poly2d_point</td>
<td markdown="span">多边形区域的每个顶点各占一行。</td>
</tr>
<tr>
<td markdown="span">region_flag</td>
<td markdown="span">各区域的旗标数据。</td>
</tr>
<tr>
<td markdown="span">region_players</td>
<td markdown="span">区域上的玩家列表。</td>
</tr>
<tr>
<td markdown="span">region_groups</td>
<td markdown="span">区域上的组列表。</td>
</tr>
<tr>
<td markdown="span">world</td>
<td markdown="span">将世界规范化为世界 ID。</td>
</tr>
<tr>
<td markdown="span">user</td>
<td markdown="span">将用户规范化为用户 ID。</td>
</tr>
<tr>
<td markdown="span">group</td>
<td markdown="span">将组规范化为组 ID。</td>
</tr>
</tbody>
</table>

每行用户记录会设置 UUID 或名称中的一项。

!!! warning "警告"

    不建议在服务器运行 WorldGuard 时，修改 MySQL 中存储的数据。WorldGuard 只保存区域数据的变化，外部修改若导致区域数据进入它无法预料的状态，可能引发问题。

## 高延迟环境 { #high-latency-environment }

数据会在后台整体加载和保存，因此较慢的硬盘或远程 MySQL 服务器通常不会造成太大问题。
