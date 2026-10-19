---
title: Move Pin
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/MovePin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Move Pin {#move-pin}

## 说明 {#description}

将给定的 [pin](../../pins.md) 移动到目标位置。   无法移动MultiPins。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| pin | p | 要移动的定位点。 |  |

## 示例 {#examples}

```yaml
  Skills:
  - movepin{pin=example} @selflocation
```

> 将名为 example 的 pin 移到施法者当前位置。
