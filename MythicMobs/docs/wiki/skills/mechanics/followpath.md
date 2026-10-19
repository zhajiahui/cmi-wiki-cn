---
title: Follow Path
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/FollowPath
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Follow Path {#follow-path}

## 说明 {#description}

产生一个[光环](aura.md)，使持有者沿路径移动。此机制也是一种[光环](aura.md)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| path | p | 由 `(x,y,z)` 格式的坐标或[目标选择器](../targeters.md)组成的列表。 |  |
| onGoalSkill | onGoal, og, then | 到达最后一个点时执行的[元技能](../metaskills.md)。 |  |
| tolerance |  | 生物被视为已到达每个点时，与该点之间所需的最小距离。 | 2 |
| speed | s | 移动速度倍率。 | 1 |
| duration | ticks, t, d, time, t | 机制的最长持续时间。未设置时，使用整数可表示的最大值。 |  |
| timeoutdistance | td, maxdistance, md | 设置后，生物与下一个点之间的距离大于此值时，会立即传送到下一个点。 |  |
| timeouttime | tt | 设置后，生物未能在指定时间内到达下一个点时，会传送到该点。 |  |

> 该机制继承了[光环](aura.md)机制的所有属性
>

> > - `auraname` 属性**固定为** `#pathing`。
> > - `duration` 属性**默认为** `2147483647`。
> > - `charges` 属性**固定为** `1`。
> > - `maxStacks` 属性**固定为** `1`。
> > - `mergeAll` 属性**固定为** `true`。

## 示例 {#examples}

```yaml
  Skills:
  - followPath{
    speed=2;
    tolerance=2;
    path=(200,5,520),(200,5,500),@forward{a=5};
    onGoal=[
      - message{m="I DID IT"} @world
    ]} @self ~onInteract
```

## 别名 {#aliases}

- path
