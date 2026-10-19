---
title: On Projectile Land
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onProjectileLand
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Projectile Land {#on-projectile-land}

## 说明 {#description}

生物的特殊弹射物（三叉戟、雪球、凋灵之首、羊驼的唾沫等）未击中实体而落地时执行技能。

### 兼容的投射物 {#compatible-projectiles}

[> 参见 onProjectileHit <](onprojectilehit.md#compatible-projectiles)

## 示例 {#examples}

```yaml
YourAverageDrowned:
  Type: DROWNED
  Equipment:
  - TRIDENT HAND
  Skills:
  - message{m="Awww..."} @target ~onProjectileLand
```

## 别名 {#aliases}

- onProjectile_Land
- onTridentLand
