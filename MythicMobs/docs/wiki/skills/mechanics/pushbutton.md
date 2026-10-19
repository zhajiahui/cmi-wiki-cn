---
title: Pushbutton
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/pushbutton
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Pushbutton {#pushbutton}

## 说明 {#description}

在提供的坐标处按下按钮。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| x |  | 按钮的 X 坐标 | 0 |
| y |  | 按钮的 Y 坐标 | 0 |
| z |  | 按钮的 Z 坐标 | 0 |
| location | loc, l | 操作的位置，使用 `x,y,z` 格式。设置后会忽略其他参数 |  |

## 示例 {#examples}

```yaml
HitSecretButton:
  Skills:
  - pushbutton{x=15;y=67;z=-213}
```

## 别名 {#aliases}

- buttonpush
