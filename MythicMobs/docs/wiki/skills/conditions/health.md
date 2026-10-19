---
title: Health
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/health
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Health {#health}

## 说明 {#description}

匹配目标的生命值

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| health | h, amount, a | 要检查的生命值范围。 | 0 |
| includeabsorption | ia | 是否将伤害吸收提供的生命值纳入计算。 | false |

## 示例 {#examples}

```yaml
Conditions:
- health{h=50} true
```

```yaml
# Below 50 health
Conditions:
- health{h=<50} true
```

```yaml
# Above 10 health
Conditions:
- health{h=>10} true
```

## 别名 {#aliases}

- hp
