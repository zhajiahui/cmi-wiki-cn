---
title: Form Line
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/FormLine
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Form Line {#form-line}

## 说明 {#description}

使施法生物沿着线性路径到达某个位置

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| path | p | 由 `(x,y,z)` 格式的坐标或[目标选择器]组成的列表。 |  |
| onGoalSkill | onGoal, og, then | 到达最后一个点时执行的[元技能]。 |  |
| tolerance |  | 生物被视为已到达每个点时，与该点之间所需的最小距离。 | 2 |
| speed | s | 移动速度倍率。 | 1 |
| duration | ticks, t, d, time, t | 机制的最长持续时间。未设置时，使用整数可表示的最大值。 |  |

> 该机制继承了[光环](aura.md)机制的所有属性

## 示例 {#examples}

```yaml
  Skills:
  - formline{
    speed=2;
    tolerance=2;
    path=(200,5,520),(200,5,500),@forward{a=5};
    onGoal=[
      - message{m="I DID IT"} @world
    ]} @self ~onInteract
```

## 别名 {#aliases}

- lineup
