---
title: config/config-spawning.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config/config-spawning.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# config/config-spawning.yml

文件：`config/config-spawning.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包配置。

## `Configuration` { #configuration }

```yaml title="config/config-spawning.yml · Configuration"
Configuration:
  Spawners:
    DisableCommandSaving: false
  RandomSpawning:
    DisableVanillaSpawns: false
    GenerateSpawnPoints: false
    SpawnRadiusPerPlayer: 64
    SpawnRadiusPerPlayerMin: 12
    SpawnRadiusPerPlayerY: 16
    PlayerClusterDistance: 24.0
    LimitMultiplier: 1.2
    LocalGroupMultiplier: 0.1
    SpawningLimit: -1
    LocalSpawningLimit: -1
    IgnoreVanillaMobs: false
    IgnoreUnnaturalMobs: false
    ReplaceObeysCap: false
    SharedCooldown: true
    MaxGenerationAttempts: 10
    
    # ADD 方法使用的生成器。可填 NONE、CLUSTER 或 LEGACY
    Generator: NONE
    
    # 每刻用于生成的最长时间，单位为毫秒
    MaxGenerationTime: 5
```
