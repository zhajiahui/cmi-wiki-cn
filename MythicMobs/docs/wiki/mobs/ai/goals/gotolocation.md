---
title: Go To Location
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/GoToLocation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Go To Location

# 前往指定位置 {#go-to-location}

## 说明 {#description}

让生物前往指定位置。注意：Followrange 必须大于生物与该位置之间的距离。

## 属性 {#attributes}

> *此 AI 行为目标没有属性。*

## 示例 {#examples}

```yaml
  AIGoalSelectors:
  - clear
  - goto 10,20,30
```

## 别名 {#aliases}

- goto
