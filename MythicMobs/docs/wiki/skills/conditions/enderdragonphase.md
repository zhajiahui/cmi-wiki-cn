---
title: Ender Dragon Phase
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EnderDragonPhase
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ender Dragon Phase {#ender-dragon-phase}

## 说明 {#description}

检查目标末影龙实体的阶段。   有效阶段的列表可以在 [Spigot Phase javadoc](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EnderDragon.Phase.html) 中找到。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| phase | p | 要匹配的阶段列表。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - enderdragonphase{phase=CIRCLING} true
```

```yaml
Conditions:
- enderdragonphase{phases=FLY_TO_PORTAL,LEAVE_PORTAL} true
```

## 别名 {#aliases}

- edragonPhase
