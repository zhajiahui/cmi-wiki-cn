# On Projectile Land

## Description {#description}

Executes a skill when the mob's special projectile type (trident, snowball, wither skull, llama's spit etc) lands on the ground without hitting an entity.

### Compatible Projectiles {#compatible-projectiles}

[> Reference onProjectileHit's <](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onProjectileHit#compatible-projectiles)

## Examples {#examples}

```yaml
YourAverageDrowned:
  Type: DROWNED
  Equipment:
  - TRIDENT HAND
  Skills:
  - message{m="Awww..."} @target ~onProjectileLand
```

## Aliases {#aliases}

- onProjectile_Land
- onTridentLand
