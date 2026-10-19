---
title: "移除默认内容"
source_url: "https://wiki.itemsadder.com/faq/removing-default-content"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 移除默认内容

如果未执行[首次安装](../plugin-usage/first-install.md)教程中的可选步骤，你应该不会有任何默认资源。

按照本教程操作，只保留自己的物品、方块和其他内容，移除所有 ItemsAdder 自带内容。

## 如何移除默认资源

打开 `plugins/ItemsAdder/contents/` 文件夹，删除不需要的文件夹/文件

执行此命令：`/iacleancache items`。

然后运行 `/iazip`。

## 移除内部资源（不推荐）

如果要完全移除所有已提供的资源，必须禁用此设置。

```yaml
extract_internal_utility_assets: true
```

打开 `plugins/ItemsAdder/contents/` 文件夹，删除不需要的文件夹/文件。

然后运行 `/iazip`。

如果删除 ItemsAdder 内部资源，请勿报告显示问题，其中某些资源供插件显示 GUI 和其他内容使用。
