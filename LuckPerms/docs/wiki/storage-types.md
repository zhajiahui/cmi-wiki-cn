---
title: "存储类型"
source_url: https://luckperms.net/wiki/Storage-types
source_kind: official-wiki
translation_review: reviewed
source_version: "fc2919c3d5e6bfba82af31f9930273b00f08ddbf"
---

LuckPerms 可以通过多种方式存储数据。这些选项可以在配置文件的“Storage Settings”（存储设置）部分修改。

<a id="possible-options"></a>
### 可选类型

* **远程数据库** - 需要连接到单独托管的数据库服务器
  * MySQL
  * MariaDB（相比 MySQL 更推荐使用）
  * PostgreSQL
  * MongoDB
* **文件型/本地数据库** - 无需额外设置，开箱即用。这种格式不方便编辑。
  * H2（相比 SQLite 更推荐使用）
  * SQLite
* **可读、可编辑的文本文件**
  * YAML（.yml 文件）
  * JSON（.json 文件）
  * HOCON（.conf 文件）
  * TOML（.toml 文件）

默认选项为 `H2`。

<a id="remote-databases"></a>
#### 远程数据库
| 优点 | 缺点 |
|----------------------------------------------------------------------|-----------------------------------------------|
| 允许多台服务器共享数据。                                             | 设置较复杂？？                                |
| 通常更加可靠                                                         | 需要额外的资源来托管数据库                     |
| 通常可以处理更多数据，并支持并发读写                                 |                                               |
| 具有索引，批量查询和更新时效率更高                                   |                                               |

<a id="flatfile-databases"></a>
#### 文件型数据库
| 优点                                                             | 缺点                                            |
|------------------------------------------------------------------|-------------------------------------------------|
| 通常比可编辑文件更加可靠，效率也更高                              | 难以直接编辑数据                                |
| 具有索引，批量查询和更新时效率更高                               | 有时容易出现数据损坏问题                        |
|                                                                  | 数据无法在服务器之间共享                        |

<a id="text-config-files"></a>
#### 文本（配置）文件
| 优点 | 缺点 |
|----------|-----------|
| 内容可直接阅读！                                 | 与文件型数据库相比，磁盘空间利用率较低                                              |
| 可以直接编辑或查看文件                           | 难以执行批量查询和更新                                                              |
|                                                  | 数据无法在服务器之间共享                                                            |
|                                                  | 更容易因人为失误（手动编辑数据时出错）而损坏                                        |

___

<a id="more-details"></a>
### 详细说明

<a id="flatfilelocal-databases-h2--sqlite"></a>
#### 文件型/本地数据库（H2 和 SQLite）
* 所有数据都存储在 LuckPerms 文件夹内的一个文件中。
* 与 YAML 或 JSON 不同，这些数据不方便使用文本编辑器编辑。
* 必须使用插件命令来编辑或查看数据。

使用 `H2` 时，所有数据都存储在 `luckperms-h2.mv.db` 文件中。   
使用 `SQLite` 时，所有数据都存储在 `luckperms-sqlite.db` 文件中。

要使用其中一种类型，请设置：
```yaml
storage-method: h2
storage-method: sqlite
```

<a id="readable--editable-text-files-yaml--json--hocon--toml"></a>
#### 可读、可编辑的文本文件（YAML / JSON / HOCON / TOML）
* 数据存储在 LuckPerms 文件夹内的多个文件中。
* 服务器运行时也可以读取或编辑这些文件，修改会自动生效。

使用 `YAML` 时，数据以 `.yml` 为扩展名存储在 `yaml-storage` 目录中。   
使用 `JSON` 时，数据以 `.json` 为扩展名存储在 `json-storage` 目录中。   
使用 `HOCON` 时，数据以 `.conf` 为扩展名存储在 `hocon-storage` 目录中。  
使用 `TOML` 时，数据以 `.toml` 为扩展名存储在 `toml-storage` 目录中。
   
这些类型的内部布局非常相似，区别仅在于语法。

[本页末尾](storage-types.md#example-files)展示了一些示例文件。

要使用其中一种类型，请设置：
```yaml
storage-method: yaml
storage-method: json
storage-method: hocon
storage-method: toml
```

<a id="remote-databases-mysql--mariadb--postgresql--mongodb"></a>
#### 远程数据库（MySQL / MariaDB / PostgreSQL / MongoDB）
需要在配置文件中填写数据库服务器的地址、端口、数据库名称、用户名和密码。   
   
如果预计要存储大量数据，或考虑扩展为群组服，建议使用这种类型。如果已经运行多台服务器，并希望在它们之间同步数据，就必须使用远程数据库类型。   
   
数据表结构见[此处](https://github.com/LuckPerms/LuckPerms/tree/master/common/src/main/resources/me/lucko/luckperms/schema)。

要使用其中一种类型，请设置：
```yaml
storage-method: mysql
storage-method: mariadb
storage-method: postgresql
storage-method: mongodb
```

___

<a id="example-files"></a>
### 示例文件
<a id="example-yaml-file"></a>
##### YAML 文件示例
```yml
uuid: c1d60c50-70b5-4722-8057-87767557e50d
name: Luck
primary-group: default
permissions:
- test.permission:
    value: true
    context:
      server: factions
- negated.permission.example:
    value: false
- special.test.perm
- special.test.permission
parents:
- default
prefixes:
- '&c[Admin] ':
    priority: 10
meta:
- homes:
    value: '10'
```

<a id="example-json-file"></a>
##### JSON 文件示例
```json
{
  "uuid": "c1d60c50-70b5-4722-8057-87767557e50d",
  "name": "Luck",
  "primaryGroup": "default",
  "permissions": [
    {
      "permission": "test.permission",
      "value": true,
      "context": {
        "server": "factions"
      }
    },
    {
      "permission": "negated.permission.example",
      "value": false
    },
    {
      "permission": "special.test.perm",
      "value": true
    },
    {
      "permission": "special.test.permission",
      "value": true
    }
  ],
  "parents": [
    {
      "group": "default"
    }
  ],
  "prefixes": [
    {
      "prefix": "&c[Admin] ",
      "priority": 10
    }
  ],
  "meta": [
    {
      "key": "homes",
      "value": "10"
    }
  ]
}
```

<a id="example-hocon-file"></a>
##### HOCON 文件示例
```conf
uuid=c1d60c50-70b5-4722-8057-87767557e50d
name=Luck
primary-group=default
permissions=[
    {
        permission="test.permission"
        value=true
        context {
            server=factions
        }
    },
    {
        permission="negated.permission.example"
        value=false
    },
    {
        permission="special.test.perm"
        value=true
    },
    {
        permission="special.test.permission"
        value=true
    }
]
parents=[
    {
        group=default
    }
]
prefixes=[
    {
        prefix="&c[Admin] "
        priority=10
    }
]
meta=[
    {
        key=homes
        value="10"
    }
]
```

<a id="example-toml-file"></a>
##### TOML 文件示例
```toml
uuid = "c1d60c50-70b5-4722-8057-87767557e50d"
name = "Luck"
primary-group = "default"

[[permissions]]
  permission = "test.permission"
  value = true

  [permissions.context]
    server = "factions"

[[permissions]]
  permission = "negated.permission.example"
  value = false

[[permissions]]
  permission = "special.test.perm"
  value = true

[[permissions]]
  permission = "special.test.permission"
  value = true

[[parents]]
  group = "default"

[[prefixes]]
  prefix = "&c[Admin] "
  priority = 10

[[meta]]
  key = "homes"
  value = "10"
```
