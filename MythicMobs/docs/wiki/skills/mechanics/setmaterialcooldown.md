---
title: Setmaterialcooldown
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setmaterialcooldown
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setmaterialcooldown {#setmaterialcooldown}

## 说明 {#description}

设置目标玩家身上指定材质物品的冷却时间

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | mat, m | 要设置冷却的材质 | ENDER_PEARL |
| duration | d | 冷却持续时间，以刻为单位 | 100 |

## 示例 {#examples}

```yaml
  Skills:
  - setmaterialcooldown{m=CHORUS_FRUIT;d=150} @PIR{r=10}
```
