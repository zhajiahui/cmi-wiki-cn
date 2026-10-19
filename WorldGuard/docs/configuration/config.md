---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 7.0.17+2370-e42d8bc
---

# config.yml

文件：`config.yml`。版本：`7.0.17+2370-e42d8bc`。

主配置。

连接信息或服务器标识已替换为示例值，使用时填写自己的信息。

## `regions` { #regions }

```yaml title="config.yml · regions"
regions:
    uuid-migration:
        perform-on-next-start: false
        keep-names-that-lack-uuids: true
    use-creature-spawn-event: true
    disable-bypass-by-default: false
    announce-bypass-status: false
    use-paper-entity-origin: false
    enable: true
    invincibility-removes-mobs: false
    cancel-chat-without-recipients: true
    nether-portal-protection: true
    fake-player-build-override: true
    explosion-flags-block-entity-damage: true
    high-frequency-flags: false
    protect-against-liquid-flow: false
    wand: minecraft:leather
    max-claim-volume: 30000
    claim-only-inside-existing-regions: false
    set-parent-on-claim: ''
    location-flags-only-inside-regions: false
    max-region-count-per-player:
        default: 7
```

## `auto-invincible` { #auto-invincible }

```yaml title="config.yml · auto-invincible"
auto-invincible: false
```

## `auto-invincible-group` { #auto-invincible-group }

```yaml title="config.yml · auto-invincible-group"
auto-invincible-group: false
```

## `auto-no-drowning-group` { #auto-no-drowning-group }

```yaml title="config.yml · auto-no-drowning-group"
auto-no-drowning-group: false
```

## `use-player-move-event` { #use-player-move-event }

```yaml title="config.yml · use-player-move-event"
use-player-move-event: true
```

## `use-player-teleports` { #use-player-teleports }

```yaml title="config.yml · use-player-teleports"
use-player-teleports: true
```

## `use-particle-effects` { #use-particle-effects }

```yaml title="config.yml · use-particle-effects"
use-particle-effects: true
```

## `disable-permission-cache` { #disable-permission-cache }

```yaml title="config.yml · disable-permission-cache"
disable-permission-cache: false
```

## `security` { #security }

```yaml title="config.yml · security"
security:
    deop-everyone-on-join: false
    block-in-game-op-command: false
    host-keys-allow-forge-clients: false
```

## `host-keys` { #host-keys }

```yaml title="config.yml · host-keys"
host-keys: {}
```

## `summary-on-start` { #summary-on-start }

```yaml title="config.yml · summary-on-start"
summary-on-start: true
```

## `op-permissions` { #op-permissions }

```yaml title="config.yml · op-permissions"
op-permissions: true
```

## `build-permission-nodes` { #build-permission-nodes }

```yaml title="config.yml · build-permission-nodes"
build-permission-nodes:
    enable: false
    deny-message: "&e你没有在这里执行此操作的权限。"
```

## `event-handling` { #event-handling }

```yaml title="config.yml · event-handling"
event-handling:
    block-entity-spawns-with-untraceable-cause: false
    interaction-whitelist: []
    emit-block-use-at-feet: []
    ignore-hopper-item-move-events: false
    break-hoppers-on-denied-move: true
```

## `protection` { #protection }

```yaml title="config.yml · protection"
protection:
    item-durability: true
    remove-infinite-stacks: false
    disable-xp-orb-drops: false
    use-max-priority-association: false
```

## `gameplay` { #gameplay }

```yaml title="config.yml · gameplay"
gameplay:
    block-potions: []
    block-potions-overly-reliably: false
    disable-conduit-effects: false
```

## `default` { #default }

```yaml title="config.yml · default"
default:
    pumpkin-scuba: false
    disable-health-regain: false
```

## `physics` { #physics }

```yaml title="config.yml · physics"
physics:
    no-physics-gravel: false
    no-physics-sand: false
    vine-like-rope-ladders: false
    allow-portal-anywhere: false
    disable-water-damage-blocks: []
```

## `ignition` { #ignition }

```yaml title="config.yml · ignition"
ignition:
    block-tnt: false
    block-tnt-block-damage: false
    block-lighter: false
```

## `fire` { #fire }

```yaml title="config.yml · fire"
fire:
    disable-lava-fire-spread: false
    disable-all-fire-spread: false
    disable-fire-spread-blocks: []
    lava-spread-blocks: []
```

## `mobs` { #mobs }

```yaml title="config.yml · mobs"
mobs:
    block-creeper-explosions: false
    block-creeper-block-damage: false
    block-wither-explosions: false
    block-wither-block-damage: false
    block-wither-skull-explosions: false
    block-wither-skull-block-damage: false
    block-enderdragon-block-damage: false
    block-enderdragon-portal-creation: false
    block-fireball-explosions: false
    block-fireball-block-damage: false
    block-windcharge-explosions: false
    anti-wolf-dumbness: false
    allow-tamed-spawns: true
    disable-enderman-griefing: false
    disable-snowman-trails: false
    block-painting-destroy: false
    block-item-frame-destroy: false
    block-armor-stand-destroy: false
    block-plugin-spawning: true
    block-above-ground-slimes: false
    block-other-explosions: false
    block-zombie-door-destruction: false
    block-vehicle-entry: false
    block-creature-spawn: []
```

## `player-damage` { #player-damage }

```yaml title="config.yml · player-damage"
player-damage:
    disable-fall-damage: false
    disable-lava-damage: false
    disable-fire-damage: false
    disable-lightning-damage: false
    disable-drowning-damage: false
    disable-suffocation-damage: false
    disable-contact-damage: false
    teleport-on-suffocation: false
    disable-void-damage: false
    teleport-on-void-falling: false
    reset-fall-on-void-teleport: false
    disable-explosion-damage: false
    disable-mob-damage: false
    disable-death-messages: false
```

## `crops` { #crops }

```yaml title="config.yml · crops"
crops:
    disable-creature-trampling: false
    disable-player-trampling: false
```

## `turtle-egg` { #turtle-egg }

```yaml title="config.yml · turtle-egg"
turtle-egg:
    disable-creature-trampling: false
    disable-player-trampling: false
```

## `sniffer-egg` { #sniffer-egg }

```yaml title="config.yml · sniffer-egg"
sniffer-egg:
    disable-creature-trampling: false
    disable-player-trampling: false
```

## `weather` { #weather }

```yaml title="config.yml · weather"
weather:
    prevent-lightning-strike-blocks: []
    disable-lightning-strike-fire: false
    disable-thunderstorm: false
    disable-weather: false
    disable-pig-zombification: false
    disable-villager-witchification: false
    disable-powered-creepers: false
    always-raining: false
    always-thundering: false
```

## `dynamics` { #dynamics }

```yaml title="config.yml · dynamics"
dynamics:
    disable-mushroom-spread: false
    disable-ice-melting: false
    disable-snow-melting: false
    disable-snow-formation: false
    disable-ice-formation: false
    disable-leaf-decay: false
    disable-grass-growth: false
    disable-mycelium-spread: false
    disable-vine-growth: false
    disable-rock-growth: false
    disable-sculk-growth: false
    disable-crop-growth: false
    disable-soil-dehydration: false
    disable-soil-moisture-change: false
    disable-coral-block-fade: false
    disable-copper-block-fade: false
    snow-fall-blocks: []
```

## `blacklist` { #blacklist }

```yaml title="config.yml · blacklist"
blacklist:
    use-as-whitelist: false
    logging:
        console:
            enable: true
        database:
            enable: false
            dsn: "jdbc:mysql://HOST/DATABASE"
            user: "USERNAME"
            pass: ''
            table: "TABLE_NAME"
        file:
            enable: false
            path: worldguard/logs/%Y-%m-%d.log
            open-files: 10
```

## `custom-metrics-charts` { #custom-metrics-charts }

```yaml title="config.yml · custom-metrics-charts"
custom-metrics-charts: true
```
