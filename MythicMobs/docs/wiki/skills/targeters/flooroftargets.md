---
title: Floor Of Targets
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/FloorOfTargets
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Floor Of Targets {#floor-of-targets}

## 说明 {#description}

选中继承目标下方的第一个固体方块

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| tries | t, max, m | 目标选择器尝试获取目标的最大次数。 | 3 |

## 示例 {#examples}

此机制会将半径 10 格内每位玩家脚下的方块伪装为冰

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @PIR{r=10}

ExampleSkill2:
  Skills:
  - blockmask{r=1;m=ICE} @FloorOfTargets
```

## 别名 {#aliases}

- floorsOfTarget
- FOT
