---
title: Set Text Display
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetTextDisplay
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Set Text Display {#set-text-display}

## 说明 {#description}

设置目标文本显示实体的文本组件

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| text | t | 要使用的文本。未设置时，此机制会改为移除实体上的文本 |  |

## 示例 {#examples}

```yaml
ExampleTextDisplayEntity:
  Type: TEXT_DISPLAY
  DisplayOptions:
    Text: I am but a humble example, nothing to see here
  Skills:
  - settextdisplay{text="MUHAHAHA! YOU FELL FOR MY TRICKERY!";delay=100} @self ~onSpawn
```

## 别名 {#aliases}

- setText
