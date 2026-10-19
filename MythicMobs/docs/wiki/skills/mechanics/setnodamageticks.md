---
title: Setnodamageticks
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setnodamageticks
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setnodamageticks {#setnodamageticks}

## 说明 {#description}

设置目标的无敌游戏刻数。攻击过程中立即使用时应加上延迟，因为无敌时间在事件完成后才会应用。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| ticks | d, duration, t | 要设置的 NoDamageTicks（正常情况下生物无敌的刻数） | 0 |

## 示例 {#examples}

攻击后使施法者无敌。

```yaml
  Skills:
  - setNoDamageTicks{ticks=0;delay=1} @self ~onAttack
```

## 别名 {#aliases}

- setimmunityticks
