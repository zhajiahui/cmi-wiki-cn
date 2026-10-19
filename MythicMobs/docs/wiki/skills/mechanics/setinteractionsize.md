---
title: Set Interaction Size
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetInteractionSize
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Set Interaction Size {#set-interaction-size}

## 说明 {#description}

设置目标 `INTERACTION` [类型](../../mobs/mobs.md#type) 实体的大小。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| height | h | 要设置的高度值 | 1 |
| width | w | 要设置的宽度值 | 1 |

## 示例 {#examples}

下面的配置在右键交互时，将施法的交互实体大小设为 2x3。

```yaml
ExampleInteractionEntity:
  Type: INTERACTION
  Skills:
  - setInteractionSize{height=2;width=3} @self ~onInteract
```

## 别名 {#aliases}

- interactionSize
