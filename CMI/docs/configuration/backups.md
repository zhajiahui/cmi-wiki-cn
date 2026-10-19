---
title: 数据备份（BackUps.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/BackUps.yml
---

# 数据备份（BackUps.yml）

文件：`plugins/CMI/Settings/BackUps.yml`

## `AutoBackup` { #autobackup }

```yaml title="BackUps.yml · AutoBackup"
AutoBackup:
  # 启用后，现有备份超过指定间隔时，自动备份数据库
  Enabled: true
  # 保留的自动备份文件数量
  # 自动备份文件使用特定命名格式，例如 2025-09-04_13-20-42_cmi.sqlite.db
  Max: 10
  # 是否将数据库文件压缩为 ZIP，以减少体积
  Zip: true
  # 自动备份时保存的数据表
  # 建议跳过较大的表，只保存最重要的数据表
  # 可用值：usertable inventories playtime playtimereward
  # 始终保存 UserTable，便于从备份提取数据时查找玩家 ID
  TablesToSave:
  - usertable
  - playtimereward
  # 备份间隔，单位为小时
  # 服务器启动后不久会执行备份检查，之后每小时检查一次
  Interval: 24
```

## `ManualBackup` { #manualbackup }

```yaml title="BackUps.yml · ManualBackup"
ManualBackup:
  # 手动发起备份时保存的数据表
  # 可用值：usertable inventories playtime playtimereward
  # 始终保存 UserTable，便于从备份提取数据时查找玩家 ID
  TablesToSave:
  - usertable
  - playtimereward
```
