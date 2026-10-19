---
title: Players Near Origin
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersNearOrigin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Players Near Origin {#players-near-origin}

## 说明 {#description}

以元技能原点周围给定半径内的所有玩家为目标。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |

## 示例 {#examples}

在此示例中，创建的弹射物无论因何结束，都会对其周围半径 2 格内的每位玩家造成伤害

```yaml
  Skills:
  - projectile{...;
    onTick=[
      - effect:particles @origin
    ];
    onEnd=[
      - damage{a=10} @PlayersNearOrigin{r=2}
    ]
    } @target
```

## 别名 {#aliases}

- playersnearsource
- PNO
