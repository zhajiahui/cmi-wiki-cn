---
title: Setname
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/setname
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setname {#setname}

## 说明 {#description}

设置施法者的显示名称。这对玩家不起作用。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| name | n | 要设置的名称 |  |

## 示例 {#examples}

当生物受到损坏时，将生物名称设置为“newmobname”。

```yaml
Skills:
  - setname{name=newmobname} @self ~onDamaged 1
```

##  {#section}

生物受伤时，以及战斗中每隔 10 游戏刻，将名称更新为 Display: 中设置的名称。这可用于更新名称内的占位符，本例更新的是 <caster.hp>。

```yaml
MySkeleton:
  Type: Skeleton
  Display: 'Skeleton <caster.hp>/<caster.mhp><&heart>'
  Skills:
  - setname{name=<caster.name>;delay=2} @self ~onDamaged
  - setname{name=<caster.name>;delay=2} @self ~onTimer:10 ?incombat
```
