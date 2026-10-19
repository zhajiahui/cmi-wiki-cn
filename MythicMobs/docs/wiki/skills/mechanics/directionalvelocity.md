---
title: Directional Velocity
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/DirectionalVelocity
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Directional Velocity {#directional-velocity}

## 说明 {#description}

更改特定矢量上目标实体的速度

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| yaw |  | 速度变化向量的偏航角。 |  |
| pitch |  | 速度变化向量的俯仰角。 |  |
| velocity | v | 速度变化量的大小。 |  |
| mode | m | 要使用的模式。 | SET |

### Mode 属性 {#mode-attribute}

接受的值为

- `SET`
- `ADD`
- `MULTIPLY`
- `REMOVE`
- `DIVIDE`
- `MINIMUM`

## 示例 {#examples}

```yaml
  Skills:
  - directionalvelocity{yaw=180;v=1;mode=MINIMUM} @self
```

## 别名 {#aliases}

- dvelocity
