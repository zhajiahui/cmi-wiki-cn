---
title: Ender Dragon Set Respawn Phase
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/EnderDragonSetRespawnPhase
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ender Dragon Set Respawn Phase {#ender-dragon-set-respawn-phase}

## 说明 {#description}

若目标位置所在维度正在进行末影龙战斗，则设置其重生阶段。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| phase | p | 要设置的阶段。 | NONE |

### Phase 属性 {#phase-attribute}

下面列出了阶段属性的可能值（在撰写本文时）。   最新的列表可以在 [javadoc](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/boss/DragonBattle.RespawnPhase.html) 中找到。

| 阶段 | 说明 |
| --- | --- |
| END | 重生流程结束。 |
| NONE | 当前没有正在进行的重生流程。 |
| PREPARING_TO_SUMMON_PILLARS | 水晶光束保持朝上。 |
| START | 水晶光束朝向上方的天空。 |
| SUMMONING_DRAGON | 所有水晶，包括柱子上的水晶，都指向天空。 |
| SUMMONING_PILLARS | 水晶光束从一根柱子指向另一根柱子，必要时重新生成柱子上的水晶。 |

## 示例 {#examples}

```yaml
  Skills:
  - enderDragonSetRespawnPhase{p=SUMMONING_DRAGON} @selflocation
```

## 别名 {#aliases}

- setEnderDragonRespawnPhase
