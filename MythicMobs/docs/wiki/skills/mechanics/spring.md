---
title: Spring
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/spring
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Spring {#spring}

## 说明 {#description}

在目标实体或位置创建临时液体“泉”。

> 泉水向外扩散的液体能够破坏、也确实会破坏那些
> 通常会被液体破坏的方块。请谨慎使用。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t | 流体源的类型，可设为 `water` 或 `lava` | water |
| duration | d | 流体源的持续时间，以刻为单位 | 40 |

## 示例 {#examples}

在目标下方产生一股水泉，持续 5 秒。

```yaml
Flood:
  Skills:
  - spring{d=100} @target
```

## 别名 {#aliases}

- water
