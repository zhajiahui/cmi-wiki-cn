---
title: Go To Parent
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/GoToParent
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Go To Parent

# 前往父实体身边 {#go-to-parent}

## 说明 {#description}

超过一定距离时，让生物向其[父实体](../../../skills/targeters/parent.md)移动。[Followrange](../../options.md#followrange) 必须大于主人与生物之间的距离。）

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| followrange | fr, r, maxrange | 生物与父实体的距离超过此值后，开始跟随父实体。 | 4 |
| minrange | mr | 生物与父实体的距离进入此范围后，停止跟随父实体。 | 4 |
| speed | s | 移动的速度。 | 1.0 |
| droptarget | dt | 生物开始跟随父实体时，是否放弃当前目标。 | true |
| teleportToWorld | ttw, tow | 父实体位于不同世界时，生物是否传送。 | true |

## 示例 {#examples}

```yaml
  AIGoalSelectors:
  - clear
  - gotoparent{fr=10;mr=3}
```
