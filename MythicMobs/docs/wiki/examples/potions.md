---
title: 药水
source_url: https://wiki.mythiccraft.io/mythicmobs/examples/Potions
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 药水 {#potions}

## 基础飞行药水 {#basic-potion-of-flight}

- 一瓶带有附魔光效的简单药水，饮用后会给予饮用者 1 分钟的飞行能力。

关于 "basicflypot" 技能的使用方式，请查看[这里](consumable-skills.md#drink-flight-potion-skill)。

```yaml
basicflypot:
  Id: potion
  Display: '&f&lBasic&6 Potion of &b&lFlight&r'
  Options:
    Color: 89,255,230
  Lore:
  - '&9Flight (1:00)'
  Enchantments:
  - MENDING
  Hide:
  - ENCHANTS
  Skills:
  - skill{s=basicflypot} ~onConsume
```
