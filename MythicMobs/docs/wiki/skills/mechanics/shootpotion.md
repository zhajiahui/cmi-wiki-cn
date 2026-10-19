---
title: Shootpotion
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shootpotion
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Shootpotion {#shootpotion}

## 说明 {#description}

向目标实体或位置投掷药水，对所有命中的实体造成指定类型的喷溅药水效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| velocity | v | 投掷药水的速度 | 1 |

> 该机制继承了[药水](potion.md)机制的所有*可继承*属性

## 示例 {#examples}

向目标投掷药水，使其减速。

```yaml
ThrownCripplingPotion:
  Skills:
  - shootpotion{type=SLOW;duration=200;level=4;velocity=5} @target
```
