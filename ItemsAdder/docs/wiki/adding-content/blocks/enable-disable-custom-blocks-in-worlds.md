---
title: "在世界中启用/禁用自定义方块"
source_url: "https://wiki.itemsadder.com/adding-content/blocks/enable-disable-custom-blocks-in-worlds"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 在世界中启用/禁用自定义方块

你可以在某些世界中禁用自定义方块，这将阻止插件生成自定义区域文件。

默认情况下，自定义方块在所有世界中启用。

## 所有规则

```yaml
blocks:
  worlds:
    - "*" # Enable in all worlds
    - "world_*" # Enable in worlds starting by `world_`
    - "*_nether" # Enable in worlds ending by `_nether`
    - "!my_custom_world" # Disable in world named `my_custom_world`
```

## 示例

### 在所有世界中启用

```yaml
blocks:
  worlds:
    - "*"
```

### 在除下界以外的所有世界中启用

```yaml
blocks:
  worlds:
    - "*"
    - "!*_nether"
```
