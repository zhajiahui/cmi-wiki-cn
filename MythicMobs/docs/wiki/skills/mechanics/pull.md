---
title: Pull
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/pull
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Pull {#pull}

## 说明 {#description}

以基本速度将所有目标实体拉向施法者，该速度根据目标与施法者的距离而增加。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| velocity | v | 拉拽的基础速度 | 1 |
| toOrigin | to | 是否朝技能原点拉拽目标 | false |

### Velocity 属性 {#velocity-attribute}

根据目标与施法者的距离，目标被拉得更快。定义的速度是“基本”速度，并且技能根据距离缩放速度，以尝试将实体直接拉向生物（如果可能的话）基于基本速度。

## 示例 {#examples}

将目标和 10 范围内的所有玩家拉向施法生物。

```yaml
DeathGrip:
  Skills:
  - pull{velocity=10} @target
  - delay 60
  - pull{v=6;to=true} @PIR{r=10}
```
