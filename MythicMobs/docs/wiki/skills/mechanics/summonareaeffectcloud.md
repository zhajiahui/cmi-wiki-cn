---
title: Summonareaeffectcloud
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/summonareaeffectcloud
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Summonareaeffectcloud {#summonareaeffectcloud}

## 说明 {#description}

在目标位置周围创建粒子云

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| particle | p | 要使用的粒子效果 | reddust |
| type | effect, t | 粒子云施加的效果类型 | SLOW |
| potionduration | pd | 药水效果的持续时间 | 100 |
| level | lvl, l | 药水效果的等级 | 1 |
| duration | d, cloudduration | 粒子云的持续时间 | 200 |
| durationreudctiononuse | drou | 粒子云每次使用后减少的持续时间 | 0 |
| radius | r | 粒子云的半径 | 2 |
| radiusreductiononuse | rrou | 粒子云每次使用后减少的半径 | 0 |
| radiusreductionontick | rrot | 粒子云每刻减少的半径 | 0 |

### Particle 属性 {#particle-attribute}

可以在 **[此处](particle/particle-types.md)** 找到粒子类型列表。

[Spigot Javadoc 列出的粒子效果也都应可使用。](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html)

## 示例 {#examples}

```yaml
  Skills:
    - summonareaeffectcloud{d=600;r=20;rrot=1} @self
```

## 别名 {#aliases}

- summonCloud
