---
title: "从 GroupManager 或 PermissionsEx 迁移"
source_url: https://luckperms.net/wiki/Migrating-from-GroupManager-or-PermissionsEx
source_kind: official-wiki
translation_review: reviewed
source_version: "fc2919c3d5e6bfba82af31f9930273b00f08ddbf"
---

本页是[迁移指南](migration.md)的补充。 

按指南将数据从 GroupManager 或 PermissionsEx 迁移到 LuckPerms 后，本页的资料可以帮助你尽快上手。

首先，下方表格将 GroupManager 和 PermissionsEx 的命令与 LuckPerms 中的**对应命令**进行了对照。如果你知道如何在 GM 或 PEX 中完成某项操作，这些表格可以帮助你快速找到 LuckPerms 中的相应做法。

当然，也可以查阅 [LuckPerms 的完整命令文档](command-usage.md)；直接熟悉这份文档或许更好！

其次，你还可以在服务器上安装一个兼容组件，继续使用*部分* PermissionsEx 和 GroupManager 命令，并让它们自动转交给 LuckPerms 执行。有关详情见[此处](https://github.com/LuckPerms/LuckPermsCompat)。不过，我们通常建议你直接迈出这一步，尽早习惯*正式的* LuckPerms 命令——花一点时间，它们就会像你之前熟悉的 GM 或 PEX 命令一样，用起来得心应手。

祝你迁移顺利，也希望你用 LuckPerms 用得愉快！

<a id="groupmanager-command-equivalents"></a>
#### GroupManager 命令对照
| GroupManager                               | LuckPerms                                                |
| ------------------------------------------ | -------------------------------------------------------- |
| manuadd \<player\> \<group\>               | lp user \<player\> parent set \<group\>                  |
| manudel \<player\>                         | lp user \<player\> clear                                 |
| manuaddsub \<player\> \<group\>            | lp user \<player\> parent add \<group\>                  |
| manudelsub \<player\> \<group\>            | lp user \<player\> parent remove \<group\>               |
| manpromote \<player\> \<group\>            | lp user \<player\> promote \<track\>                     |
| mandemote \<player\> \<group\>             | lp user \<player\> demote \<track\>                      |
| manwhois \<player\>                        | lp user \<player\> info                                  |
| manuaddp \<player\> \<permission\>         | lp user \<player\> permission set \<permission\> true    |
| manudelp \<player\> \<permission\>         | lp user \<player\> permission unset \<permission\>       |
| manulistp \<player\>                       | lp user \<player\> permission info                       |
| manucheckp \<player\> \<permission\>       | lp user \<player\> haspermission \<permission\>          |
| manuaddv \<player\> prefix \<value\>       | lp user \<player\> meta addprefix \<priority\> \<value\> |
| manuaddv \<player\> suffix \<value\>       | lp user \<player\> meta addsuffix \<priority\> \<value\> |
| manuaddv \<player\> \<variable\> \<value\> | lp user \<player\> meta set \<variable\> \<value\>       |
| manudelv \<player\> \<variable\>           | lp user \<player\> meta unset \<variable\>               |
| manulistv \<player\>                       | lp user \<player\> meta info                             |
|                                            |                                                          |
| mangadd \<group\>                          | lp creategroup \<group\>                                 |
| mangdel \<group\>                          | lp deletegroup \<group\>                                 |
| mangaddi \<group1\> \<group2\>             | lp group \<group1\> parent add \<group2\>                |
| mangdeli \<group1\> \<group2\>             | lp group \<group1\> parent remove \<group2\>             |
| listgroups                                 | lp listgroups                                            |
| mangaddp \<group\> \<permission\>          | lp group \<group\> permission set \<permission\> true    |
| mangdelp \<group\> \<permission\>          | lp group \<group\> permission unset \<permission\>       |
| manglistp \<group\>                        | lp group \<group\> permission info                       |
| mangcheckp \<group\> \<permission\>        | lp group \<group\> haspermission \<permission\>          |
| mangaddv \<player\> prefix \<value\>       | lp group \<group\> meta addprefix \<priority\> \<value\> |
| mangaddv \<player\> suffix \<value\>       | lp group \<group\> meta addsuffix \<priority\> \<value\> |
| mangaddv \<player\> \<variable\> \<value\> | lp group \<group\> meta set \<variable\> \<value\>       |
| mangdelv \<player\> \<variable\>           | lp group \<group\> meta unset \<variable\>               |
| manglistv \<player\>                       | lp group \<group\> meta info                             |
|                                            |                                                          |
| mansave                                    | lp sync                                                  |
| manload                                    | lp sync                                                  |


<a id="permissionsex-command-equivalents"></a>
#### PermissionsEx 命令对照
| PermissionsEx                                                | LuckPerms                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| pex                                                          | lp                                                           |
| pex reload                                                   | lp sync                                                      |
| pex toggle debug                                             | [lp verbose \<option>](verbose.md)                              |
| pex user \<user\> check \<permission\>                       | lp user \<user\> haspermission \<permission\>                |
| pex backend                                                  | lp info                                                      |
| pex import \<backend\>                                       | lp export \<file\> / lp import \<file\>                      |
|                                                              |                                                              |
| pex user \<user\> list                                       | lp user \<user\> permission info                             |
| pex user \<user\> prefix                                     | lp user \<user\> meta info                                   |
| pex user \<user\> prefix \<prefix\>                          | lp user \<user\> meta addprefix \<priority\> \<prefix\>      |
| pex user \<user\> suffix                                     | lp user \<user\> meta info                                   |
| pex user \<user\> suffix \<suffix\>                          | lp user \<user\> meta addsuffix \<priority\> \<suffix\>      |
| pex user \<user\> delete                                     | lp user \<user\> clear                                       |
| pex user \<user\> add \<permission\> \<world\>               | lp user \<user\> permission set \<permission\> \<true/false\> world=\<world\> |
| pex user \<user\> remove \<permission\> \<world\>            | lp user \<user\> permission unset \<permission\> world=\<world\> |
| pex user \<user\> timed add \<permission\> \<time\> \<world\> | lp user \<user\> permission settemp \<permission\> \<true/false\> \<time\> world=\<world\> |
| pex user \<user\> timed remove \<permission\> \<time\> \<world\> | lp user \<user\> permission unsettemp \<permission\> world=\<world\> |
| pex user \<user\> set \<option\> \<value\> \<world\>         | lp user \<user\> meta set \<option\> \<value\> world=\<world\> |
|                                                              |                                                              |
| pex user \<user\> group list                                 | lp user \<user\> parent info                                 |
| pex user \<user\> group add \<group\> \<world\>              | lp user \<user\> parent add \<group\> world=\<world\>        |
| pex user \<user\> group add \<group\> \<world\> \<time\>     | lp user \<user\> parent addtemp \<group\> \<time\> world=\<world\> |
| pex user \<user\> group set \<group\>                        | lp user \<user\> parent set \<group\>                        |
| pex user \<user\> group remove \<group\> \<world\>           | lp user \<user\> parent remove \<group\> world=\<world\>     |
| pex groups list                                              | lp listgroups                                                |
| pex group \<group\> list                                     | lp group \<group\> permission info                           |
| pex group \<group\> prefix                                   | lp group \<group\> meta info                                 |
| pex group \<group\> prefix \<prefix\>                        | lp group \<group\> meta addprefix \<priority\> \<prefix\>    |
| pex group \<group\> suffix                                   | lp group \<group\> meta info                                 |
| pex group \<group\> suffix \<suffix\>                        | lp group \<group\> meta addsuffix \<priority\> \<suffix\>    |
| pex group \<group\> create                                   | lp creategroup \<group\>                                     |
| pex group \<group\> delete                                   | lp deletegroup \<group\>                                     |
| pex group \<group\> parents list                             | lp group \<group\> parent info                               |
| pex group \<group\> users                                    | lp group \<group\> listmembers                               |
| pex group \<group\> parents set \<parents\>                  | lp group \<group\> parent add \<parent\>                     |
| pex group \<group\> add \<permission\> \<world\>             | lp group \<group\> permission set \<permission\> \<true/false\> world=\<world\> |
| pex group \<group\> remove \<permission\> \<world\>          | lp group \<group\> permission unset \<permission\> world=\<world\> |
| pex group \<group\> timed add \<permission\> \<time\> \<world\> | lp group \<group\> permission settemp \<permission\> \<true/false\> \<time\> world=\<world\> |
| pex group \<group\> timed remove \<permission\> \<time\> \<world\> | lp group \<group\> permission unsettemp \<permission\> world=\<world\> |
| pex group \<group\> set \<option\> \<value\> \<world\>       | lp group \<group\> meta set \<option\> \<value\> world=\<world\> |
|                                                              |                                                              |
| pex group \<group\> user add \<user\>                        | lp user \<user\> parent add \<group\>                        |
| pex group \<group\> user remove \<user\>                     | lp user \<user\> parent remove \<group\>                     |
| pex promote \<user\> \<ladder\>                              | lp user \<user\> promote \<ladder\>                          |
| pex demote \<user\> \<ladder\>                               | lp user \<user\> demote \<ladder\>                           |



