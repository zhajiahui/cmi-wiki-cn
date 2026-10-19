---
title: Setgravity
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setgravity
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setgravity {#setgravity}

## 说明 {#description}

设置重力是否影响目标实体。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| gravity | g, b, bool, u, use | 设置实体是否受重力影响 | true |

## 示例 {#examples}

```yaml
  Skills:
  - setgravity{g=false} @self ~onSpawn
  - setusegravity{g=false} @self ~onSpawn
  - ...
```

## 别名 {#aliases}

- setusegravity
