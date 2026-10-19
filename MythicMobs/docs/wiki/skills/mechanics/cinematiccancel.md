---
title: Cinematic Cancel
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CinematicCancel
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Cinematic Cancel {#cinematic-cancel}

## 说明 {#description}

中断目标玩家的活动 [cinematicCamera](cinematiccamera.md)，立即返回他们的摄像机和控制权。机制必须以玩家为目标。

取消会触发 [onCinematicEnd](../triggers/oncinematicend.md) 触发器（以及原始机制的 `onEnd` 技能），结束原因为 `CANCELLED`。如果目标玩家当前不在过场动画中，则机制不会执行任何操作。

## 属性 {#attributes}

*此技能机制没有属性。*

## 示例 {#examples}

取消触发玩家当前播放的过场动画。

```yaml
  Skills:
  - cinematicCancel @trigger
```

##  {#section}

生物受伤时，结束 30 格内所有玩家的过场动画。

```yaml
  Skills:
  - cinematicCancel @PlayersInRadius{r=30} ~onDamaged
```

## 别名 {#aliases}

- cinecancel
- stopcinematic
