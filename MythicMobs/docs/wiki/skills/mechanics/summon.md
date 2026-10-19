---
title: Summon
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/summon
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Summon {#summon}

## 说明 {#description}

在目标周围召唤给定类型的生物。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t, mob, m | 要召唤的生物类型。可以是 Mythic 生物类型或普通实体类型 | SKELETON |
| onSummon | onsummonskill, then | 在召唤出的生物身上执行的[元技能](../metaskills.md) |  |
| amount | a | 要召唤的生物数量。 | 1 |
| level | l | 召唤的生物等级 | 0 |
| yaw |  | 召唤实体的 yaw，未设置时继承施法者的值 |  |
| pitch |  | 召唤实体的 pitch，未设置时继承施法者的值 |  |
| usetargetyaw | uty | 是否使用目标位置或实体的 yaw 设置召唤实体的 yaw；设置了 `yaw` 参数时除外 | false |
| usetargetpitch | utp | 是否使用目标位置或实体的 pitch 设置召唤实体的 pitch；设置了 `pitch` 参数时除外 | false |
| radius | r, noise, n | 以目标为中心、召唤生物的半径 | 0 |
| yRadius | yr, ynoise, yn | 覆盖半径的 Y 分量。 | radius |
| yRadiusUpOnly | yradiusonlyup, yruo, yu | Y 方向的散布范围是否只向上延伸，而不向下延伸。 | false |
| velocity | v, force, f | 生物被召唤后的最大初始速度，使生物向随机方向抛出 | 0 |
| yvelocity | yv, yforce, yf | 与 velocity 相同，但只作用于 y 轴 | velocity |
| onSurface | os, s | （true/false）生物是否只能生成在固体方块上 | false |
| copyThreatTable | ctt | 召唤出的生物是否复制父实体的仇恨表。需要为召唤出的生物启用仇恨表才会生效。 | false |
| inheritThreatTable | itt | 召唤出的生物是否与父实体共享仇恨表。需要为召唤出的生物启用仇恨表才会生效。 | false |
| inheritFaction | if | 召唤出的生物是否与父实体属于同一阵营 | true |
| inheritdespawn | inheritdespawnoption, ido | 召唤出的生物是否继承施法者的[清除选项](../../mobs/options.md#despawn) | false |
| summonerIsOwner | sio | 是否将召唤者设为生物的所有者。 | true |
| summonerIsParent | sip | 是否将召唤者设为生物的父实体。 | true |

## 示例 {#examples}

此示例将在目标玩家周围召唤 5 凋灵骷髅。

```yaml
RaiseSkeletons:
  Skills:
  - summon{type=WITHER_SKELETON;amount=5;radius=4} @PIR{r=20}
```

## 别名 {#aliases}

- spawnmobs
- spawnmob
- piratesummon
