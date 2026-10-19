---
title: Togglelever
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/togglelever
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Togglelever {#togglelever}

## 说明 {#description}

在给定坐标处切换拉杆开关。

经过设定时间后，拉杆恢复初始状态，默认 20 游戏刻，即 1 秒。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| location | loc, l | 操作的位置，使用 `x,y,z` 格式。设置后会忽略其他位置参数 |  |
| duration | d | 拉杆保持开启的持续时间，以刻为单位。 | 20 |
| x |  | 按钮的 X 坐标。 | 0 |
| y |  | 按钮的 Y 坐标。 | 0 |
| z |  | 按钮的 Z 坐标。 | 0 |

## 示例 {#examples}

切换给定坐标处放置的拉杆。

```yaml
OpenSecretDoor:
  Skills:
    - togglelever{duration=600;x=15;y=67;z=-213}
```

## 别名 {#aliases}

- lever
