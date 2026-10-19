---
title: config/config-mobs.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config/config-mobs.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# config/config-mobs.yml

文件：`config/config-mobs.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包配置。

## `Configuration` { #configuration }

```yaml title="config/config-mobs.yml · Configuration"
Configuration:
  MobDrops:
    DefaultDropMethod: VANILLA
    DoLootsplosionByDefault: false
    DoHologramNameByDefault: false
    DoItemGlowByDefault: false
    DoItemBeamByDefault: false
    DoItemVFXByDefault: false
    DefaultItemVFX:
      Material: POTION
      Model: 1
    DoPerPlayerDropsByDefault: false
    DoClientsideDropsByDefault: false
    MinimumDamagePercentForDrops: 1%
    DefaultDeathHologram: []
    DefaultLeaderboardTimeout: 6000
    DefaultDeathChatMessage: []
  MobEggs:
    Material: PIG_SPAWN_EGG
    DefaultDisplay: "<mob.name> 刷怪蛋"
    DefaultLore:
    - "<dark_gray>一枚神秘的蛋，</dark_gray>"
    - "<dark_gray>可以用来复活</dark_gray>"
    - <dark_gray><mob.name></dark_gray>
    Model: 0
  
  # ================================================================================
  # 通用生物选项
  # ================================================================================
  Mobs:
    CancelDamageIfZero: false
    KillMessagePrefix: ''
  
  # ================================================================================
  # 生物默认设置：选择生物选项的默认值
  # ================================================================================
  DefaultMobOptions:
    Despawn: true
    
    PreventOtherDrops: false
    PreventVanillaDamage: false
  
  # ================================================================================
  # 全息图相关功能选项
  # ================================================================================
  Holograms:
    GlobalOffset: 0.15
    
    CastBar:
      InfoBackground: 0,0,0,0
      InfoBillboarding: VERTICAL
      CastBackground: 0,0,0,0
      CastBillboarding: VERTICAL
      Offset: 1
    
    HealthBar:
      Background: 0,0,0,0
      Billboarding: VERTICAL
      Offset: -0.05
      Length: 50
      Scale: 0.4,0.4,0.4
    
    Nameplate:
      Background: 0,0,0,60
      Billboarding: VERTICAL
      Offset: 0
    
    Speech:
      Background: 100,100,100,60
      Billboarding: VERTICAL
      LinePrefix: <white>
      Offset: 0.4
  
  # ================================================================================
  # 等级成长：允许生物升级并变强
  # ================================================================================
  MobLeveling:
    
    # 用于按等级提升生物属性
    ScalingEquations:
      Health: V * ((1.05)^(L-1))
      Damage: V * ((1.05)^(L-1))
    
    # 旧版生物属性成长方式
    DefaultLevelModifiers:
      Health: 0.1
      Armor: 0
      Damage: 0
      KnockbackResistance: 0
      Power: 0
    
    # 各世界的成长选项
    WorldScaling:
      Default:
        Enabled: true
        ScaleVanillaMobs: true
        PerBlocksFromSpawn: 250
      world2:
        Enabled: true
        PerBlocksFromSpawn: 250
      world2_nether:
        Enabled: false
        PerBlocksFromSpawn: 100
```
