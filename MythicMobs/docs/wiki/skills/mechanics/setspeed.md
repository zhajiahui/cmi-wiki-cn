---
title: Setspeed
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setspeed
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setspeed {#setspeed}

## 说明 {#description}

导致目标改变其速度属性

> 必须显式设置 [MovementSpeed](../../mobs/options.md#movementspeed) 选项才能正常工作！

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | a, amount, m, multiplier, s, v, value | 应用于实体基础速度的倍率 | 1 |
| type | t | 速度类型，可设为 `FLY` 或其他字符串。不完全等于 `FLY` 时，会修改行走速度 | WALK |

## 示例 {#examples}

这会将生物生成时的行走速度设置为2

```yaml
  Skills:
  - setspeed{speed=2;type=walking} ~onSpawn
```
