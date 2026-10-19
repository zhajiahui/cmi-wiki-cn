---
title: Setrotation
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setrotation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setrotation {#setrotation}

## 说明 {#description}

更改目标的旋转（仅适用于非玩家实体）。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| relative | r, rel | 变化是否相对于目标，布尔值 | false |
| yaw | y | 新的 yaw（偏航角） | 0 |
| pitch | p | 新的 pitch（俯仰角） | 0 |

## 示例 {#examples}

```yaml
  Skills:
  - setrotation{relative=true;pitch=-45}
  - ...
```

## 别名 {#aliases}

- setrot
