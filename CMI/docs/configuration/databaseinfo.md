---
title: 数据库连接（DataBaseInfo.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/DataBaseInfo.yml
---

# 数据库连接（DataBaseInfo.yml）

文件：`plugins/CMI/Settings/DataBaseInfo.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `storage`

### `storage.method`

存储方式：MySQL 或 sqlite<br>
注意！多台服务器不要共用同一组数据库表，否则可能出现非预期问题。每台服务器应使用独立的数据表

## `mysql`

### `mysql.username`

需要 MySQL

### `mysql.tablePrefix`

允许字符为 a-z、0-9 和 \_

### `mysql.autoReconnect`

不了解这些数值的用途时，请保留默认值

## `AutoSaveInterval`

自动保存间隔，单位为秒<br>
决定多久向数据库写入一次数据<br>
没有数据变化时，不执行保存<br>
注意！请保持较短间隔，例如约 60 秒<br>
最短间隔为 10 秒

## `ForceSaveOnLogOut`

玩家退出后立即保存数据，不等待下一次自动保存

## `ForceLoadOnLogIn`

实验性选项，尚未充分测试，在 BungeeCord 网络中可能出现小问题<br>
玩家每次加入时，都从数据库加载数据<br>
设为 false，使用预缓存数据，效率更高
