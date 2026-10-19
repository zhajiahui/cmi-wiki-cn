---
title: Haspotioneffect
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/haspotioneffect
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Haspotioneffect {#haspotioneffect}

## 说明 {#description}

测试目标实体是否具有药水效果

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t | 药水效果类型。 | ANY |
| level | lvl, l | 要匹配的等级范围，可选。 |  |
| duration | d | 要匹配的持续时间范围，可选。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - haspotioneffect{t=SLOW;l=0-2;d=0-9999} true
```

```yaml
  TargetConditions:
  - haspotioneffect{t=Speed;l=0-9} true
```

## 别名 {#aliases}

- hasPotion
