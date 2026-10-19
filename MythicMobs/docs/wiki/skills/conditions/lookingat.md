---
title: Looking At
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/LookingAt
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Looking At {#looking-at}

## 说明 {#description}

检查玩家是否正在查看方块或实体。   仅供玩家使用。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t, block, b, entity, e | 用于检查的对象。 |  |
| distance | d | 生成的射线检测的距离。如果生物查找表现异常，可以尝试更改此值。 | 5 |

## 示例 {#examples}

```yaml
  Conditions:
  - lookingat{b=DIRT} true
```

```yaml
  TargetConditions:
  - isPlayer orElseCast fallbackmechanic
  - lookingat{e=COW} true
```
