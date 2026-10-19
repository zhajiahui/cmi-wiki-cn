---
title: Togglesitting
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/togglesitting
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Togglesitting {#togglesitting}

## 说明 {#description}

切换猫、狗、狐狸和鹦鹉的坐姿。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| setSitting | state | 设置坐下状态 | false |

## 示例 {#examples}

右键单击时使狼坐下。

```yaml
ExampleDog:
  Type: Wolf
  Skills:
  - sit{state=true} @Self ~onInteract
```

## 别名： {#aliases}

- sit
