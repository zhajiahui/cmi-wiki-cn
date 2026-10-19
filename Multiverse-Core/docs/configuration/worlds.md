---
title: worlds.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: worlds.yml
source_version: 5.8.1
---

# worlds.yml

文件：`worlds.yml`。版本：`5.8.1`。

随包配置。

连接信息或服务器标识已替换为示例值，使用时填写自己的信息。

## `minecraft:overworld` { #minecraftoverworld }

```yaml title="worlds.yml · minecraft:overworld"
minecraft:overworld:
  adjust-spawn: true
  alias: ''
  allow-advancement-grant: true
  allow-flight: false
  allow-weather: true
  anchor-respawn: true
  auto-heal: true
  auto-load: true
  bed-respawn: true
  biome: ''
  difficulty: easy
  entry-fee:
    enabled: false
    amount: 0.0
    currency: '@vault-economy'
  gamemode: survival
  generator: ''
  hidden: false
  hunger: true
  keep-spawn-in-memory: false
  meta: {}
  player-limit: -1
  portal-form: all
  pvp: true
  respawn-world: ''
  scale: 1.0
  spawn-location:
    ==: MVSpawnLocation
    x: 0.0
    y: 74.0
    z: 0.0
    pitch: 0.0
    yaw: 0.0
  spawning:
    monster:
      spawn: true
      tick-rate: '@unset'
      spawn-limit: '@unset'
      exceptions: []
    animal:
      spawn: true
      tick-rate: '@unset'
      spawn-limit: '@unset'
      exceptions: []
    water_animal:
      spawn: true
      tick-rate: '@unset'
      spawn-limit: '@unset'
      exceptions: []
    water_ambient:
      spawn: true
      tick-rate: '@unset'
      spawn-limit: '@unset'
      exceptions: []
    water_underground_creature:
      spawn: true
      tick-rate: '@unset'
      spawn-limit: '@unset'
      exceptions: []
    ambient:
      spawn: true
      tick-rate: '@unset'
      spawn-limit: '@unset'
      exceptions: []
    axolotl:
      spawn: true
      tick-rate: '@unset'
      spawn-limit: '@unset'
      exceptions: []
    misc:
      spawn: true
      tick-rate: '@unset'
      spawn-limit: '@unset'
      exceptions: []
  world-blacklist: []
  read-only:
    environment: normal
    generator-settings: ''
    legacy-world-name: rpgworld
    seed: 0
  version: 1.3
```
