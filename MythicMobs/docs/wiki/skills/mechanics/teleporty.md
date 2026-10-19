---
title: Teleporty
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/teleporty
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Teleporty {#teleporty}

## 说明 {#description}

将施法者传送到指定的 Y 坐标。   该机制不需要目标，因为施法者始终是被传送的人。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| y |  | 在 Y 轴上要传送到的位置 | 0 |

## 示例 {#examples}

此示例会将施法者传送到其坐标，但 Y 的值为 5。

```yaml
WarpY:
  Skills:
  - teleportY{y=5}
```

## 别名 {#aliases}

- tpy
