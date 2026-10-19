---
title: 消耗品技能
source_url: https://wiki.mythiccraft.io/mythicmobs/examples/Consumable-Skills
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 消耗品技能 {#consumable-skills}

这些技能通常由玩家使用物品时触发，并使用 [Mythic Crucible](https://git.lumine.io/mythiccraft/mythiccrucible)。

### Eat Food 技能 {#eat-food-skill}

---

- 一个食物食用技能示例。使用后会恢复饱和度，并短暂给予饱和药水效果，同时稍作延迟后播放三种声音和粒子效果。

```yaml
eatmeal:
  Skills:
  - feed{amount=10;overfeed=true} @self
  - effect:particles{p=happy_villager;amount=5;speed=.5;y=1} @self
  - effect:sound{s=minecraft:entity.experience_orb.pickup;v=0.8;p=0.6} @self
  - Delay 2
  - effect:sound{s=minecraft:entity.experience_orb.pickup;v=0.8;p=0.7} @self
  - Delay 2
  - effect:sound{s=minecraft:entity.experience_orb.pickup;v=0.8;p=0.8} @self
  - potion{t=SATURATION;d=100;l=2;force=true} @self
```

---

### Drink Flight Potion 技能 {#drink-flight-potion-skill}

---

- 一个饮用药水的法术。使用后会给予饮用者 1 分钟的飞行能力，通过 Boss 血条倒计时显示剩余持续时间，并用粒子表示效果正在生效。

```yaml
basicflypot:
  Conditions:
  Skills:
  - effect:sound{s=entity.generic.drink;v=1;p=1} @self
  - effect:particles{p=fireworks_spark;amount=20;speed=.5;y=1} @self
  - effect:sound{s=block.end_portal_frame.fill;v=0.3;p=2} @self
  - effect:sound{s=item.bottle.fill_dragonbreath;v=0.3;p=0.8} @self
  - effect:sound{s=minecraft:block.beacon.power_select;v=1;p=1.4} @self
  - effect:particles{p=ELECTRIC_SPARK;amount=10;speed=.8;y=1} @self
  - fly{duration=1200;ot=flightaura;i=20;bt=true;auraName=Flight Remaining:} @self
flightaura:
  Skills:
  - effect:particles{p=fireworks_spark;amount=5;speed=.1;y=1} @self
```
