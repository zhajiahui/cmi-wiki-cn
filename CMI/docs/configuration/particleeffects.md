---
title: 粒子效果（ParticleEffects.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/ParticleEffects.yml
---

# 粒子效果（ParticleEffects.yml）

文件：`plugins/CMI/Settings/ParticleEffects.yml`

## `Particles` { #particles }

```yaml title="ParticleEffects.yml · Particles"
# 若要完全关闭某种粒子，设为 ""
# 设置方法见 https://www.zrips.net/cmi/extra/particles/
Particles:
  Enabled: true
  TotemHalo: circle;effect:reddust;c:255,255,10;twist;part:3;offset:0,2,0;pitch:90;radius:0.3;interval:2
  Healing: circle;effect:heart;dur:0.1;part:1;offset:0,1.7,0;radius:0.3
  GlyphHead: circle;effect:flying_glyph;dur:5;pitchc:15;part:10;offset:0,1.7,0;radius:0.5;yawc:12;color:rs;pitch:90
  tpaWarmup: circle;effect:flying_glyph;dur:5;pitchc:15;part:10;offset:0,1.7,0;radius:0.5;yawc:12;color:rs;pitch:90
  GColumn: circle;c:0,255,0;twist;part:5;r:0.75;pitch:90;move:0,0.1,0;rc:-0.02
  SmallBoop: circle;effect:flying_glyph;yaw:[playerName];pitch:[playerName];r:0.1;part:3;rc:0.03;mr:0.3;twist
  HologramInteraction: circle;effect:flying_glyph;yaw:[playerName];pitch:[playerName];r:0.1;part:3;rc:0.03;mr:0.3;twist
  HologramNewInteraction: circle;effect:reddust;r:0;part:2;rc:0.2;mr:1;color:rs;yaw:[playerName];a:90
  HologramHover: circle;effect:crit;r:0;part:1;
  TpUp: circle;c:200,50,210;twist;part:5;r:0.5;pitch:90;move:0,0.33,0;offset:0,-0.2,0
  TpDown: circle;c:150,50,10;part:5;r:0.5;pitch:90;move:0,-0.33,0;offset:0,2.2,0
  # custom1 到 custom30 是可自由使用的粒子预设，可用于命令预热等功能
  custom1: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom2: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom3: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom4: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom5: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom6: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom7: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom8: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom9: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom10: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom11: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom12: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom13: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom14: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom15: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom16: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom17: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom18: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom19: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom20: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom21: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom22: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom23: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom24: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom25: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom26: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom27: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom28: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom29: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
  custom30: circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:4
```

## `TeleportEffects` { #teleporteffects }

```yaml title="ParticleEffects.yml · TeleportEffects"
# 玩家进行指定类型的传送时，在出发位置和目标位置显示设置的粒子动画
# 不想显示时，设为空文本
# 动画名称使用上方 Particles 中的名称，例如 TpUp
TeleportEffects:
  Unknown:
    From: ''
    To: ''
  Elevator:
    From: ''
    To: ''
  SafeLogin:
    From: ''
    To: ''
  Spawn:
    From: ''
    To: ''
  NetherRoof:
    From: ''
    To: ''
  BelowBedrock:
    From: ''
    To: ''
  Back:
    From: ''
    To: ''
  DBack:
    From: ''
    To: ''
  Home:
    From: ''
    To: ''
  Jump:
    From: ''
    To: ''
  Patrol:
    From: ''
    To: ''
  Portal:
    From: ''
    To: ''
  WarmUp:
    From: ''
    To: ''
  Biome:
    From: ''
    To: ''
  FlightCharge:
    From: ''
    To: ''
  InvEdit:
    From: ''
    To: ''
  TimedCommand:
    From: ''
    To: ''
  TpaAll:
    From: ''
    To: ''
  Tp:
    From: ''
    To: ''
  Bungee:
    From: ''
    To: ''
  Top:
    From: ''
    To: ''
  Down:
    From: ''
    To: ''
  TpAll:
    From: ''
    To: ''
  TpHere:
    From: ''
    To: ''
  TpPos:
    From: ''
    To: ''
  TpoPos:
    From: ''
    To: ''
  Warp:
    From: ''
    To: ''
  JoinSpawn:
    From: ''
    To: ''
  Totem:
    From: ''
    To: ''
  randomTp:
    From: ''
    To: ''
  World:
    From: ''
    To: ''
  HoloEdit:
    From: ''
    To: ''
```
