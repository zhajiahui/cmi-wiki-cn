---
title: For Each Pin
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ForEachPin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# For Each Pin {#for-each-pin}

## 说明 {#description}

为 MultiPin 中的每个 pin 运行指定元技能。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| name | n, pin, p, key, k | 定位点名称。 |  |

> 该机制继承了[技能](skill.md)机制的所有属性

## 示例 {#examples}

```yaml
  Skills:
  - foreachpin{name=YourCoolPin;skill=[
    - particle{p=flame;a=20}
    ]} @self
```
