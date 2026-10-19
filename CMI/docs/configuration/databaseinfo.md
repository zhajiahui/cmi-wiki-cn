---
title: 数据库连接（DataBaseInfo.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/DataBaseInfo.yml
---

# 数据库连接（DataBaseInfo.yml）

文件：`plugins/CMI/Settings/DataBaseInfo.yml`

连接信息、玩家标识和世界示例已使用占位符，使用时按本地配置填写。

## `storage` { #storage }

```yaml title="DataBaseInfo.yml · storage"
storage:
  # 存储方式：MySQL 或 sqlite
  # 注意！多台服务器不要共用同一组数据库表，否则可能出现非预期问题。每台服务器应使用独立的数据表
  method: sqlite
```

## `mysql` { #mysql }

```yaml title="DataBaseInfo.yml · mysql"
mysql:
  # 需要 MySQL
  username: "USERNAME"
  password: "PASSWORD"
  hostname: "HOST"
  database: "DATABASE"
  # 允许字符为 a-z、0-9 和 _
  tablePrefix: "TABLE_PREFIX"
  # 不了解这些数值的用途时，请保留默认值
  autoReconnect: true
  useSSL: false
  verifyServerCertificate: false
```

## `AutoSaveInterval` { #autosaveinterval }

```yaml title="DataBaseInfo.yml · AutoSaveInterval"
# 自动保存间隔，单位为秒
# 决定多久向数据库写入一次数据
# 没有数据变化时，不执行保存
# 注意！请保持较短间隔，例如约 60 秒
# 最短间隔为 10 秒
AutoSaveInterval: 15
```

## `ForceSaveOnLogOut` { #forcesaveonlogout }

```yaml title="DataBaseInfo.yml · ForceSaveOnLogOut"
# 玩家退出后立即保存数据，不等待下一次自动保存
ForceSaveOnLogOut: false
```

## `ForceLoadOnLogIn` { #forceloadonlogin }

```yaml title="DataBaseInfo.yml · ForceLoadOnLogIn"
# 实验性选项，尚未充分测试，在 BungeeCord 网络中可能出现小问题
# 玩家每次加入时，都从数据库加载数据
# 设为 false，使用预缓存数据，效率更高
ForceLoadOnLogIn: false
```
