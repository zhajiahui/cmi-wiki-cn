---
title: Spawn Reason
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/SpawnReason
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Spawn Reason {#spawn-reason}

## 说明 {#description}

检查目标的生成原因

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| reason | r | 要检查的原因，可以是任意一种 [Bukkit](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/event/entity/CreatureSpawnEvent.SpawnReason.html) 原因。 |  |

## 示例 {#examples}

在此示例中，如果目标实体因袭击而生成，则该技能将对目标实体应用发光效果

```yaml
ExampleSkill:
  TargetConditions:
  - spawnReason{reason=RAID} true
  Skills:
  - potion{t=GLOWING;d=100;l=0}
```
