---
title: Runaigoalselector
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/runaigoalselector
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Runaigoalselector {#runaigoalselector}

## 说明 {#description}

更改寻路 AI 行为。并非所有实体都支持所有行为。要重新设置 AI，先使用 clear，再通过 runaigoalselector 添加所需行为。与生物配置不同，这个机制每次只能指定一个行为；只要不使用 clear，新行为就会追加到已有行为末尾。

AI 目标列表可以在[此处](../../mobs/custom-ai.md#ai-goal-selectors)找到。更复杂的目标，例如具有位置的巡逻，可能需要以字符串形式输入，例如下面的示例。

> **这是一个无目标机制，受影响的实体将始终是施法者**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| goal | aigoalselector, g, goalselector, s, string, t, target | 要追加的 AI 行为选择器 |  |

## 示例 {#examples}

```yaml
ChangePathfinderGoalExample:
  Skills:
  - runaigoalselector{goal=clear} # wipes previous pathfinding objectives
  - runaigoalselector{goal=fleesun} # prioritizes avoiding sunlight exposure
  - runaigoalselector{goal=randomstroll} # randomly wanders
  - runaigoalselector{goal="patrol 1494,38,10;1494,38,-10;1514,38,-10;1514,38,10"} # passively wanders between various coordinates
```

## 别名 {#aliases}

- aigoal
- aigoals
