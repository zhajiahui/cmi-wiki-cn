---
title: Shieldbreak
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shieldbreak
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Shieldbreak {#shieldbreak}

## 说明 {#description}

如果目标玩家正在用盾牌格挡，则使其停止格挡。仅对玩家有效。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| duration | d | 格挡被击破后，盾牌被禁用的持续时间，以刻为单位 | 100 |

## 示例 {#examples}

如果玩家正在阻挡，这将打破阻挡并使护盾处于冷却状态200游戏刻（或10秒）。

```yaml
  Skills:
  - shieldbreak{duration=200} @target
```

## 别名 {#aliases}

- disableshield
