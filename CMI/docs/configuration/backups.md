---
title: 数据备份（BackUps.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/BackUps.yml
---

# 数据备份（BackUps.yml）

文件：`plugins/CMI/Settings/BackUps.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `AutoBackup`

### `AutoBackup.Enabled`

启用后，现有备份超过指定间隔时，自动备份数据库

### `AutoBackup.Max`

保留的自动备份文件数量<br>
自动备份文件使用特定命名格式，例如 2025-09-04\_13-20-42\_cmi.sqlite.db

### `AutoBackup.Zip`

是否将数据库文件压缩为 ZIP，以减少体积

### `AutoBackup.TablesToSave`

自动备份时保存的数据表<br>
建议跳过较大的表，只保存最重要的数据表<br>
可用值：usertable inventories playtime playtimereward<br>
始终保存 UserTable，便于从备份提取数据时查找玩家 ID

### `AutoBackup.Interval`

备份间隔，单位为小时<br>
服务器启动后不久会执行备份检查，之后每小时检查一次

## `ManualBackup`

### `ManualBackup.TablesToSave`

手动发起备份时保存的数据表<br>
可用值：usertable inventories playtime playtimereward<br>
始终保存 UserTable，便于从备份提取数据时查找玩家 ID
