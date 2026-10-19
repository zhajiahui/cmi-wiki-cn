---
title: Shield
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shield
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Shield {#shield}

## 说明 {#description}

添加伤害吸收生命值。建议将 maxShield 设为大于 amount 的值。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要给予的护盾量 | 1 |
| maxabsorb | maxshield, ma, ms | 实体护盾的最大值 | 1 |

## 示例 {#examples}

为施法者添加伤害吸收生命值。

```yaml
  Skills:
  - shield{amount=50;maxShield=100} @self ~onSpawn
  - ...
```
