---
title: Shieldpercent
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shieldpercent
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Shieldpercent {#shieldpercent}

## 说明 {#description}

对目标实体应用吸收护盾，以达到其最大生命值的一定百分比。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| multiplier | m | 倍率。护盾值为 `maxhealth*multiplier` | 0.1 |
| maxabsorb | maxshield, ma, ms | 护盾的最大值不得超过生物最大生命值乘以此值 | `Multiplier's value` |

## 示例 {#examples}

按倍率为施法者添加伤害吸收生命值。

```yaml
  Skills:
  - shieldPercent{multiplier=2;mS=2.5} @self ~onTimer:2000
  - ...
```
