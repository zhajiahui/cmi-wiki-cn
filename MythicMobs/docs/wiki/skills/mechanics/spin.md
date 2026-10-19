---
title: Spin
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Spin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Spin {#spin}

## 说明 {#description}

使目标实体在给定的时间内旋转。   当生物反复施放旋转机制时，它会在旋转的同时向上移动。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| velocity | v | 目标旋转的速度 | 18 |

> 该机制继承了[光环](aura.md)机制的所有属性

### Velocity 属性 {#velocity-attribute}

当你将速度设置为0时，该生物的方向将被锁定。

## 示例 {#examples}

```yaml
SpinningSpider:
  Type: SPIDER
  Skills:
  - spin{duration=100;velocity=20} @self ~onTimer:100
```

## 别名 {#aliases}

- effect:spin
- e:spin
