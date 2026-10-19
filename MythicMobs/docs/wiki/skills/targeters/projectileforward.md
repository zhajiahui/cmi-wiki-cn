---
title: Projectile Forward
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ProjectileForward
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Projectile Forward {#projectile-forward}

## 说明 {#description}

根据施放技能的弹射物的方向，选中其前方的位置

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| forward | f, amount, a | 目标点应位于前方多远处。 | 1 |
| rotate | rot | 目标位置绕弹射物的旋转角度。 | 0 |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onTick=[
      - effect:particles{p=flame} @ProjectileForward{f=2}
      - effect:particles @Origin
    ]}
```
