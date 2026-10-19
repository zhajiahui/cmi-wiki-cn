---
title: Health Percent
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HealthPercent
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Health Percent {#health-percent}

## 说明 {#description}

匹配目标的生命值百分比或乘数

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| percent | p, healthpercent, hp | 要检查的生命值百分比或倍率，例如 50% 或 0.5。 | 0 |
| includeabsorption | ia | 是否将伤害吸收提供的生命值纳入计算。 | false |

## 示例 {#examples}

```yaml
# Exactly at 50% health
Conditions:
- healthpercent{p=50%} true
```

```yaml
# Below 50% health
Conditions:
- healthpercent{p=<50%} true
```

```yaml
# Above 10% health
Conditions:
- healthpercent{p=>0.1} true
```

## 别名 {#aliases}

- hppercent
