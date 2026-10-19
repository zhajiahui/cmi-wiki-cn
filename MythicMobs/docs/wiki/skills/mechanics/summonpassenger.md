---
title: Summonpassenger
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/summonpassenger
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Summonpassenger {#summonpassenger}

## 说明 {#description}

召唤生物骑乘施法者；如果当前有乘客，会先将其移下。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| passenger | p, rider, r, type, t | 要设为乘客的生物类型 |  |
| stack | s | 是否让召唤出的实体骑乘施法者当前的乘客 | false |

## 示例 {#examples}

```yaml
  Skills:
  - summonPassenger{type=MyZombie}
```

会召唤生物“MyZombie”来骑乘技能机制的施法者。

## 别名 {#aliases}

- passenger
- summonRider
- rider
