---
title: datasource.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: datasource.yml
source_version: 3.3.3.6
---

# datasource.yml

文件：`datasource.yml`。版本：`3.3.3.6`。

随包配置。

## `DefaultSettings` { #defaultsettings }

```yaml title="datasource.yml · DefaultSettings"
# HikariCP 的默认设置适用于大多数部署环境，通常无需额外调整。
# https://github.com/brettwooldridge/HikariCP#gear-configuration-knobs-baby
DefaultSettings:
  # HikariCP 会尝试让 DriverManager 根据 jdbcUrl 识别驱动，
  # 但部分旧驱动还需要指定 driverClassName。
  # 除非出现明确提示“找不到驱动”的错误，否则省略此项。默认值：none
  DriverClassName: 'com.mysql.cj.jdbc.Driver'
  # 从连接池取出的连接默认是否自动提交事务。
  # 此项为布尔值。默认值：true
  AutoCommit: true
  # HikariCP 尝试在连接池中保留的最少空闲连接数。
  # 空闲连接数低于此值，且总连接数低于 maximumPoolSize 时，
  # HikariCP 会尽可能快速补充连接。
  # 不过，为获得更好的性能并及时应对突发请求，建议不设置此值，让 HikariCP 使用固定大小的连接池。
  # 默认值：与 maximumPoolSize 相同
  MinimumIdle: 10
  # 连接池允许的最大连接数，包括空闲连接和正在使用的连接。
  # 此值基本决定了与后端数据库建立的实际连接数上限。
  # 应根据实际运行环境选择合理的值。
  # 连接池达到此大小且没有空闲连接时，getConnection() 最多阻塞 connectionTimeout 毫秒，随后超时。
  # 请查阅连接池大小的相关说明。默认值：10
  MaximumPoolSize: 10
  # 检测连接是否仍然可用时允许等待的最长时间。
  # 必须小于 connectionTimeout。最小允许值为 250 ms。默认值：5000
  ValidationTimeout: 5000
  # 客户端从连接池获取连接时，最多等待多少毫秒。
  # 超过此时长仍无可用连接时，抛出 SQLException。
  # 最小允许值为 250 ms。默认值：30000（30 秒）
  ConnectionTimeout: 30000
  # 连接在池中最多可保持空闲多久。
  # 仅当 minimumIdle 小于 maximumPoolSize 时生效。
  # 连接数已降至 minimumIdle 时，不再移除空闲连接。
  # 实际移除时间可能比此值晚，最大偏差为 +30 秒，平均偏差为 +15 秒。
  # 不会在达到此空闲时长前移除连接。
  # 设为 0，永不因空闲而移除连接。
  # 最小允许值为 10000ms（10 秒）。默认值：600000（10 分钟）
  IdleTimeout: 600000
  # 池中连接的最长存活时间。
  # 正在使用的连接不会被移除；归还并关闭后才会移出连接池。
  # 各连接的存活时间会略微错开，避免大量连接同时失效。
  # 强烈建议设置此值，且应比数据库或基础设施施加的连接时限短几秒。
  # 设为 0 表示不限制存活时间，但仍受 idleTimeout 影响。
  # 最小允许值为 30000ms（30 秒）。默认值：1800000（30 分钟）
  MaxLifetime: 1800000
  # 池中连接的保活检查间隔。正在使用的连接不会
  # 由保活线程检测，只有空闲连接才会接受检测。
  # keepaliveTimeMs：通过定期检查连接是否可用来维持连接。单位为毫秒，默认值为 0（关闭）。
  KeepaliveTime: 300000
  # 驱动支持 JDBC4 时，强烈建议不设置此项。
  # 此项用于不支持 JDBC4 Connection.isValid() API 的旧驱动。
  # 从池中交出连接前执行的查询，用于确认与数据库的连接仍然有效。
  # 建议先不设置此项运行连接池；驱动不兼容 JDBC4 时，HikariCP 会记录错误。默认值：~
  ConnectionTestQuery: ~
  # MySQL 配置
  # 以下是为提高 MySQL 性能而推荐的一些设置。
  # MySQL 还有许多性能选项，建议一并查阅，根据应用需求调整。
  # http://dev.mysql.com/doc/connector-j/en/connector-j-reference-configuration-properties.html
  DataSourceProperty:
    # MySQL 驱动为每条连接缓存的预处理语句数量。
    # 默认值 25 较为保守。建议设置为 250-500。
    prepStmtCacheSize: 250
    # 驱动允许缓存的预处理 SQL 语句的最大长度。MySQL 默认值为 256。
    # 根据原作者的经验，尤其是使用 Hibernate 等 ORM 框架时，生成的语句往往远长于此默认值。
    # 建议值为 2048。
    prepStmtCacheSqlLimit: 2048
    # 缓存默认关闭；未启用缓存时，上面的两项参数均不生效。
    # 必须将此项设为 true。
    cachePrepStmts: true
    # 较新版本的 MySQL 支持服务端预处理语句，可显著提高性能。
    # 将此项设为 true。
    useServerPrepStmts: true
```
