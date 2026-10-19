---
title: Yaw
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/yaw
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Yaw {#yaw}

## 说明 {#description}

检查目标实体的偏航角是否在范围内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| yaw | y | 要检查的偏航角。 | 0 |
| clamp | c | 是否将偏航角限制在 0-360 范围内。 | true |

## 示例 {#examples}

```yaml
  Conditions:
  - yaw{y=90to180} true
```

```yaml
  Conditions:
  - yaw{y=>0} true
```
