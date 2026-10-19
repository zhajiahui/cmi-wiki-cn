---
title: Mythic 生物
source_url: https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/MythicMob
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mythic 生物 {#mythic-mob}

## 说明 {#description}

掉落时，生成指定的 MythicMobs 生物。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t, mob, m | 要召唤的生物类型。可以是 Mythic 生物类型或普通实体类型 | SKELETON |
| amount | a | 要召唤的生物数量。 | 1 |
| level | lvl, l | 召唤的生物等级 | 0 |
| radius | r, noise, n | 以目标为中心、召唤生物的半径 | 0 |
| yRadius | yr, ynoise, yn | 覆盖半径的 Y 分量。 | radius |
| yRadiusUpOnly | yradiusonlyup, yruo, yu | Y 方向的散布范围是否只向上延伸，而不向下延伸。 | false |
| velocity | v, force, f | 生物被召唤后的最大初始速度，使生物向随机方向抛出 | 0 |
| yvelocity | yv, yforce, yf | 与 velocity 相同，但只作用于 y 轴 | velocity |
| onSurface | os, s | （true/false）生物是否只能生成在固体方块上 | false |

## 示例 {#examples}

```yaml
  Drops:
  - mythicmob{type=IncredibleLootchest;velocity=1;os=true} 1 1
```

## 别名 {#aliases}

- mythicmobs
- mm
