---
title: Player By Name
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayerByName
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Player By Name {#player-by-name}

## 说明 {#description}

通过名字来定位特定的玩家。可以是占位符。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| name | n | 玩家名称。 | CarsonJF |

## 示例 {#examples}

下面的生物会记住生成后第一个攻击它的玩家名称，此后每隔 10 秒点燃该玩家一次

```yaml
VengefulMob:
  Type: ZOMBIE
  Skills:
  - setvariable{var=caster.targetedplayer;type=STRING;val=<trigger.name>} @self ~onDamaged =100% ?~isPlayer
  - ignite @PlayerByName{name=<caster.var.targetedplayer>} ~onTimer:200 ?variableisset{var=caster.targetedplayer}
```

## 别名 {#aliases}

- specificplayer
