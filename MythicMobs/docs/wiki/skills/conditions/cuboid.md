---
title: Cuboid
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/cuboid
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Cuboid {#cuboid}

## 说明 {#description}

目标是否位于具有 `location1` 和 `location2` 作为相反顶点的长方体内

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| location1 | loc1, l1, a | 第 1 个点的 x,y,z 坐标。 |  |
| location2 | loc2, l2, b | 第 2 个点的 x,y,z 坐标。 |  |
| relative | r | 坐标是否相对于施法者。 | false |

## 示例 {#examples}

```yaml
  TargetConditions:
  - cuboid{location1=x,y,z;location2=x,y,z;relative=true}
```

## 别名 {#aliases}

- incuboid
