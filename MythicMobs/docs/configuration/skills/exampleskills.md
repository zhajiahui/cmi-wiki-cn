---
title: skills/ExampleSkills.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: skills/ExampleSkills.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# skills/ExampleSkills.yml

文件：`skills/ExampleSkills.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包示例配置。

## `SmashAttack` { #smashattack }

```yaml title="skills/ExampleSkills.yml · SmashAttack"
# 更多信息请查看插件手册，或加入 Discord：
# http://www.mythicmobs.net
#  

#
# 传送到目标身边，造成伤害，并击退
# 附近的所有玩家
#
# 冷却时间以秒为单位
SmashAttack:
  Cooldown: 8
  Conditions:
  - targetwithin{d=25}
  Skills:
  - "message{cooldown=30;m=\"<mob.name><&co> 哈哈哈！我要碾碎你，蠢货！\"} @PlayersInRadius{r=40}"
  - teleport @target
  - effect:sound{s=mob.endermen.portal;volume=1.0;pitch=0.5}
  - delay 10
  - damage{amount=5;ignorearmor=true} @PlayersInRadius{r=5}
  - throw{velocity=10;velocityY=5} @PlayersInRadius{r=5}
  - effect:explosion @Self
```

## `SummonSkeletons` { #summonskeletons }

```yaml title="skills/ExampleSkills.yml · SummonSkeletons"
#
# 每秒召唤 2 只骷髅，持续 3 秒。
#
SummonSkeletons:
  Cooldown: 15
  Skills:
  - "message{m=\"<caster.name><&co> 起来吧，我的随从们！\"} @PlayersInRadius{r=40}"
  - delay 20
  - summon{mob=SkeletalMinion;amount=2;noise=5} @Self
  - delay 20
  - summon{mob=SkeletalMinion;amount=2;noise=5} @Self
  - delay 20
  - summon{mob=SkeletalMinion;amount=2;noise=5} @Self
```

## `AngrySludgePoison` { #angrysludgepoison }

```yaml title="skills/ExampleSkills.yml · AngrySludgePoison"
#
# 使 15 格内的所有玩家中毒
#
AngrySludgePoison:
  Cooldown: 10
  Skills:
  - potion{type=POISON;lvl=2;duration=100} @PlayersInRadius{r=15}
  - effect:particles{p=happyVillager;amount=1000;hSpread=15;ySpread=1;speed=0;yOffset=0.5} @Self
```
