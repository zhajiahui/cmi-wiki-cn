---
title: Ender Dragon Set Phase
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/EnderDragonSetPhase
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ender Dragon Set Phase {#ender-dragon-set-phase}

## 说明 {#description}

设置目标末影龙实体的战斗阶段。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| phase | p | 要设置的阶段。 | CIRCLING |

### Phase 属性 {#phase-attribute}

下面列出了阶段属性的可能值（在撰写本文时）。   最新的列表可以在 [javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EnderDragon.Phase.html) 中找到。

| 阶段 | 说明 |
| --- | --- |
| BREATH_ATTACK | 龙会在当前位置使用龙息攻击。 |
| CHARGE_PLAYER | 龙会冲向一名玩家。 |
| CIRCLING | 仍有末地水晶时，龙会在柱子围成的环外盘旋；没有水晶时，则在环内盘旋。 |
| DYING | 龙会飞到传送门附近并死亡。 |
| FLY_TO_PORTAL | 龙会飞向空的传送门，适用时会从另一侧接近。 |
| HOVER | 龙会悬停在当前位置，不执行任何动作。 |
| LAND_ON_PORTAL | 龙会降落在传送门上。 |
| LEAVE_PORTAL | 龙会离开传送门。 |
| ROAR_BEFORE_ATTACK | 龙会在使用龙息攻击前咆哮。 |
| SEARCH_FOR_BREATH_ATTACK_TARGET | 龙会寻找玩家并使用龙息攻击。 |
| STRAFING | 龙会飞向目标玩家，并在进入 64 格范围内时发射火球。 |

## 示例 {#examples}

```yaml
  Skills:
  - enderDragonSetPhase{p=CHARGE_PLAYER} @self ~onDamaged 0.2
```

> 龙受到伤害后会向玩家冲锋。请注意，无法确定哪位玩家将成为龙的目标

## 别名 {#aliases}

- setEnderDragonPhase
