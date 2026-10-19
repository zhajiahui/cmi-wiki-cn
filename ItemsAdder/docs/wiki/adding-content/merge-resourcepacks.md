---
title: "合并资源包"
source_url: "https://wiki.itemsadder.com/adding-content/merge-resourcepacks"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 合并资源包

**Minecraft 1.20.3 之前的版本仅支持 1 个服务器资源包**。

**Minecraft 1.20.4** 及更新版本支持多个资源包，但此功能仍有缺陷，因为**自定义模型数据不会合并**。\
**如果**使用多个资源包，需要将其合并。

## 如何合并？

### 步骤 1

复制资源包的 `assets` 文件夹。

### 步骤 2

将资源包的 `assets` 文件夹粘贴到新建的 `contents` 子文件夹中。\
例如 `merged_pack_1`：`ItemsAdder/contents/merged_pack_1/resourcepack/`

### 步骤 3

使用命令 `/iazip` 压缩 ItemsAdder 资源包。\
（根据所选托管方式，按对应的[托管教程](../plugin-usage/plugin-configuration/resourcepack-hosting.md)操作。）

### 步骤 4（进阶用户）

合并超过 1 个资源包时，可能需要指定合并优先级。\
打开 config.yml，填写 `contents` 各子文件夹的加载优先顺序。

```yaml
    contents-folders-priorities:
      - vanilla
      - _iainternal
      - merged_pack_1
      - merged_pack_2
      - merged_pack_3
      # ... other packs here of which you want to change load order.
```

## 示例

[modelengine.md](../compatibility-with-other-plugins/compatible/modelengine.md)

[nova.md](../compatibility-with-other-plugins/compatible/nova.md)

[space.md](../compatibility-with-other-plugins/compatible/space.md)
