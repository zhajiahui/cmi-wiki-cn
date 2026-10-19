---
title: 切换存储类型
source_url: https://luckperms.net/wiki/Switching-storage-types
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

<a id="how-to"></a>
## 操作方法
切换数据存储很简单。

1. 首先执行 `/luckperms export <file>`
2. 然后完全停止服务器。
3. 编辑配置文件，修改存储类型。
4. 重新启动服务器，让新的数据存储完成初始化。
5. 然后执行 `/luckperms import <file>`
6. 此时，所有数据应已迁移到新的数据存储。

\<file\> 是要保存或读取的文件名。导出的文件会保存在 LuckPerms 数据文件夹中，导入的文件也必须位于该文件夹。导出命令中的文件名可以任意指定（例如 `data`），但重新导入时必须使用同一个名称。

<a id="web-exporting"></a>
## 网页导出

1. 执行 `/luckperms export --upload`
2. 将命令返回的 10 位代码保存到某处。
3. 完全停止服务器
4. 编辑配置文件，修改存储类型。
5. 执行 `/luckperms import <10 digit code> --upload`
6. 此时，所有数据应已迁移到新的数据存储

<a id="backups"></a>
## 备份
此功能也可以用于备份全部 LuckPerms 数据。只需执行导出命令，并将输出文件保存在安全的位置。注意，使用 `--upload` 的网页导出会过期，因此它可能并不是理想的备份存储方式。

