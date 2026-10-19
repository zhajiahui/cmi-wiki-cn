---
title: Display Transformation
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/DisplayTransformation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Display Transformation {#display-transformation}

## 说明 {#description}

设置目标展示实体的变换。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| action | a | 要使用的操作，可以为 `SET`、`ADD`、`MULTIPLY`、`DIVIDE`。 | SET |
| transformationtype | transformation, type, tt | 变换类型，可以为 `TRANSLATION`、`SCALE`、`RIGHT_ROTATION`、`LEFT_ROTATION`。 | TRANSLATION |
| value | val | 变换的值。 | 0,0,0 |

## 示例 {#examples}

```yaml
ExampleDisplayEntity:
  Type: block_display
  Skills:
  # sets the translation transform to `0,0,1` after 10 seconds the entity spawns
  - displaytransformation{action=set;transformation=translation;value=0,0,1;delay=200} @self ~onSpawn

  # rotates the item display along the y-axis (similar to a dropped item)
  - displaytransformation{action=MULTIPLY;transformation=LEFT_ROTATION;val=0,0.707,0,0.707} @self ~onTimer:10
```

## 别名 {#aliases}

- settransformation
- transformation
