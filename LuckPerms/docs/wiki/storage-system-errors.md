---
title: 存储系统排错
source_url: https://luckperms.net/wiki/Storage-system-errors
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

本页是通用[常见问题列表](faq.md)的补充，专门讨论与存储有关的问题和错误。

这里列出了存储后端的一些常见错误及修复方法（主要是 MySQL！）。

___

首先，说明一下 LuckPerms 的权限存储是如何工作的。我们经常收到用户的抱怨（有时相当生气！），指责我们导致功能异常，但 95% 的情况下，这些问题与 LuckPerms 并无关系。:cry:

为了将权限数据写入存储后端，LuckPerms 会使用一种称为“驱动”的组件，与底层存储系统交互。

这些驱动由第 3 方开发，经过广泛测试，而且大多出自数据库软件背后的组织。

需要特别说明：

* **如果错误源于驱动，就*不是* LuckPerms 导致的。**
* 你*可能*遇到了驱动本身的缺陷，但这种情况并不常见
* 最可能的原因是某些环境或配置设置有误。


下方列出了一些常见错误。如果你的问题不在其中，欢迎在这里的 GitHub 上提交错误报告，我们会指出排查方向（如果最终确认是 LuckPerms 的缺陷，也会修复！）。

___

<a id="common-errors"></a>
# 常见错误

<a id="luckperms-cannot-connect-to-my-mysql-server"></a>
### LuckPerms 无法连接到 MySQL 服务器

例如以下错误：

> Caused by: java.util.concurrent.CompletionException: java.sql.SQLTransientConnectionException: luckperms - Connection is not available, request timed out after 5000ms.   
> ...   
> Caused by: java.sql.SQLTransientConnectionException: luckperms - Connection is not available, request timed out after 5000ms.


> luckperms - Failed to validate connection com.mysql.jdbc.JDBC4Connection@xxxxxxxxx (Communications link failure)   
> The last packet successfully received from the server was xxxxxxx milliseconds ago.  The last packet sent successfully to the server was xx milliseconds ago.)

检查以下各项是否正确：

* 使用了正确的地址和端口
* 使用了正确的用户名和密码
* 数据库存在，且该用户可以访问
* 服务器在线，并且正在接受连接
* 没有防火墙规则阻止连接
* MySQL 绑定到了正确的端口，并且安装 LuckPerms 的服务器可以访问它
* 检查是否超出了 MySQL 的最大连接数限制。默认情况下，LuckPerms 在每个服务器上会使用 10 个连接。如果许多插件都连接到同一个服务器，就需要提高此限制。

如果出现 `Communications link failure` 或与超时有关的错误，就说明上方列表中的某一项不正确。

要让该用户能够访问 LuckPerms 的数据表，请执行：
```sql
GRANT ALL PRIVILEGES ON [databasename].* TO '[username]'@'[ipaddress]';
```
请将 [ ] 中的内容替换为实际值。

例如：
```sql
GRANT ALL PRIVILEGES ON luckperms.* TO 'luck'@'%';
```

完成更改后，再执行：
```sql
FLUSH PRIVILEGES;
```

___

<a id="mysql-ssl-errors"></a>
### MySQL SSL 错误
如果出现类似以下内容的错误：
> Establishing SSL connection without server's identity verification is not recommended. According to MySQL requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.

……就需要为 MySQL 连接禁用 SSL。

可以编辑 LuckPerms 配置文件中的连接属性。在 "Storage" 部分找到：
```yaml
data:
  pool-settings:
    # This setting allows you to define extra properties for connections.
    properties:
      useUnicode: true
      characterEncoding: utf8
      useSSL: false
      verifyServerCertificate: false
```

然后添加最后两个选项。

___

<a id="mysql-no-operations-allowed-after-connection-closed-error"></a>
### MySQL “No operations allowed after connection closed” 错误
如果出现类似以下内容的错误：
> me.lucko.luckperms.lib.hikari.pool.PoolBase - luckperms-hikari - Failed to validate connection me.lucko.luckperms.lib.mysql.jdbc.JDBC4Connection@xxxxxxx (No operations allowed after connection closed.)

> me.lucko.luckperms.lib.hikari.pool.PoolBase - luckperms-hikari- Failed to validate connection me.lucko.luckperms.lib.mariadb.MariaDbConnection@xxxxxxx (xxx cannot be called on a closed connection)

……就需要修改 `maximum-lifetime`（LP 配置）和 `wait_timeout`（MySQL 配置）设置。

关键在于，LP 配置中的 `maximum-lifetime` 值必须**小于** MySQL 配置中的 `wait_timeout` 值。

| `maximum-lifetime` |
|--------------------|
| 位置：[LuckPerms 配置](https://github.com/LuckPerms/LuckPerms/blob/be92a6754404b387dead24ebc1dd3ca8af8e6456/bukkit/src/main/resources/config.yml#L125-L128) |
| 单位：毫秒 |
| 默认值：`1800000`（30 分钟） |


| `wait_timeout` |
|----------------|
| 位置：[MySQL 服务器配置](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_wait_timeout) |
| 单位：秒 |
| 默认值：`28800`（8 小时） |

修改哪一个值都可以，只要 `maximum-lifetime` 小于 `wait_timeout`。请记住，这两个值的单位不同！

默认的 `maximum-lifetime` 值为 30 分钟，对**绝大多数**用户都没有问题。只有你或主机服务商将等待超时设置从默认的 8 小时改成其他值时，才会产生问题。

如果 MySQL 服务器由第 3 方提供，请向他们询问该值的设置。

___

<a id="mysql-exceeded-max-connections"></a>
### MySQL 超出最大连接数

类似以下内容的错误：

> Caused by: com.mysql.jdbc.exceptions.jdbc4.MySQLSyntaxErrorException: User 'xxxxxxxxx' has exceeded the 'max_user_connections' resource (current value: xxx)

你的 MySQL 用户超出了最大连接数限制。默认情况下，LuckPerms 在每个服务器上会使用 10 个连接。如果许多插件都连接到同一个 MySQL 服务器，就需要提高此限制。

如果自行托管 MySQL 服务器，可以参考下方链接了解如何提高限制。

* https://dev.mysql.com/doc/refman/5.5/en/too-many-connections.html
* https://www.electrictoolbox.com/update-max-connections-mysql/

如果 MySQL 服务器由主机服务商提供，需要请他们为你提高限制。

___

<a id="mysql-public-key-retrieval-is-not-allowed"></a>
### MySQL 公钥检索受限（Public Key Retrieval is not allowed）

类似以下内容的错误：

> Caused by: me.lucko.luckperms.lib.mysql.jdbc.exceptions.jdbc4.MySQLNonTransientConnectionException: Public Key Retrieval is not allowed

这是一个可以修复的 MySQL 错误。

可以编辑 LuckPerms 配置文件中的连接属性。在 "Storage" 部分找到：

```yaml
data:
  pool-settings:
    # This setting allows you to define extra properties for connections.
    properties:
      useUnicode: true
      characterEncoding: utf8
      useSSL: false
      verifyServerCertificate: false
      allowPublicKeyRetrieval: true
```
然后添加最后一个选项 `allowPublicKeyRetrieval`，并设为 true。

___

<a id="mysql-failed-to-set-port"></a>
### MySQL 端口设置失败

类似以下内容的错误：

> Failed to set property port on target class me.lucko.luckperms.lib.mysql.jdbc.jdbc2.optional.MysqlDataSource
java.lang.NumberFormatException: For input string: xxxx

LuckPerms 配置中的 `address` 设置未能正确设置端口，可能是地址和端口拼写或格式有误。如果使用默认端口 3306，就完全无需指定端口。`address` 一行的正确格式为 `"address:port"`。

___

<a id="luckperms-cannot-connect-to-my-redis-server"></a>
### LuckPerms 无法连接到 Redis 服务器
检查以下各项是否正确：

* 使用了正确的地址和端口
* 密码正确
* 没有防火墙规则阻止连接
* Redis 服务器确实正在运行
