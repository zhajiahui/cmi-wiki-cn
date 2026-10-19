---
title: "Space"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/space"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# Space

## [此处下载](https://www.spigotmc.org/resources/space.59572/)

## 添加兼容性

创建新文件夹：`ItemsAdder/contents/space/resourcepack/`

将 Space 插件资源包解压到上述文件夹中，结构类似如下：\
`ItemsAdder/contents/space/resourcepack/assets/...`

然后运行 `/iazip`，并按照[托管教程](../../plugin-usage/plugin-configuration/resourcepack-hosting.md)操作。

## 已知问题

### 粒子问题

合并资源包后，你会注意到方块有了双倍粒子。\
这是正常现象，目前无法修复，原因是 Space 插件处理方块模型的方式不正确。
