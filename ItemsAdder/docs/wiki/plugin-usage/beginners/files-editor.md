---
title: "文件编辑器"
source_url: "https://wiki.itemsadder.com/plugin-usage/beginners/files-editor"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 文件编辑器

## 如何安装

* [下载 Visual Studio Code (vs-code)](https://code.visualstudio.com/download)
* [下载扩展](https://marketplace.visualstudio.com/items?itemName=LoneDev.ia-vscode)

### 预览

<div align="left"><figure><img src="../../assets/47b4c631c891b9ea05db.png" alt="" width="397"><figcaption></figcaption></figure></div>

### 启用字段和补全提示的说明

<figure><img src="../../assets/f2befc44d8bc104c67c4.png" alt=""><figcaption></figcaption></figure>

## FTP

[从此处](https://marketplace.visualstudio.com/items?itemName=Natizyskunk.sftp)下载 VSCode 的 FTP 扩展。

在电脑的任意位置创建空文件夹，例如 `Downloads` 文件夹中。\
此文件夹将存放服务器文件的副本，每次保存时都会同步。\
例如 `remote_itemsadder_contents`。

按 `CTRL+SHIFT+P` 并运行 **Config**。

<figure><img src="../../assets/cc5029fe12f473958101.png" alt=""><figcaption></figcaption></figure>

更改 `host`、`port`、`username` 和 `password`（如有需要，还要更改 `protocol`）。\
`uploadOnSave` 允许保存时自动上传文件。

```json
{
    "name": "My Server",
    "host": "eux1.humbleservers.com",
    "protocol": "sftp",
    "port": 2022,
    "username": "username",
    "password": "password",
    "remotePath": "/plugins/ItemsAdder/",
    "uploadOnSave": true,
    "useTempFile": false,
    "openSsh": false
}
```

按 `CTRL+SHIFT+P` 并运行 **Download Project**。

<figure><img src="../../assets/e1942988cdb4d4d97792.png" alt=""><figcaption></figcaption></figure>
