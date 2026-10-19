---
title: Set Projectile Direction
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetProjectileDirection
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Set Projectile Direction {#set-projectile-direction}

## 说明 {#description}

将调用的弹射物的移动方向设置为给定目标

## 属性 {#attributes}

## 属性 {#attributes-2}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| magnitude | m | 变化的幅度。值为 1 时，投射物会完全转向指定方向；较小的值会在 0 到 100% 之间插值调整方向 | 1 |

## 支持的目标选择器 {#supported-targeters}

该机制接受位置目标选择器和实体目标选择器。当给定实体目标时，弹射物将瞄准该实体的当前位置。

## 示例 {#examples}

一旦被弹射物调用，该机制将根据弹射物当前的方向改变弹射物的方向

```yaml
  Skills:
  - setprojectiledirection @ProjectileForward{f=10;rot=45}
```

##  {#section}

使用实体瞄准器将弹射物瞄准10块内最近的玩家

```yaml
  Skills:
  - setprojectiledirection @NearestPlayer{r=10}
```
