---
title: Is In Cinematic
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/IsInCinematic
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Is In Cinematic {#is-in-cinematic}

## 说明 {#description}

检查目标玩家当前是否位于活动的电影摄像机路径中。

当玩家被 [cinematicCamera](../mechanics/cinematiccamera.md) 机制移动时返回   true  ，并且在过场动画结束或取消时返回   false  。

## 属性 {#attributes}

*此条件没有属性*

## 示例 {#examples}

```yaml
  Conditions:
  - isInCinematic true
```

## 别名 {#aliases}

- incinematic
- incine
- cinematicactive
