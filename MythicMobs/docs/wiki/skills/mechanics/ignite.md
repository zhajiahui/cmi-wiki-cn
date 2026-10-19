---
title: Ignite
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ignite
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ignite {#ignite}

## 说明 {#description}

使目标实体着火。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| ticks | t,d,duration | 目标应燃烧的刻数。 | 60 |

## 示例 {#examples}

点燃使用该技能的生物正在攻击的实体，持续100游戏刻（5秒）

```yaml
  Skills:
  - ignite{ticks=100} @trigger ~onAttack
```
