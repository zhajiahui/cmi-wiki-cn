---
title: Blackscreen
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Blackscreen
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Blackscreen {#blackscreen}

## 说明 {#description}

使玩家屏幕变黑。

## 属性 {#attributes}

> 该机制继承了[光环](aura.md)机制的所有属性
>

> > - `auraname` 属性**固定为** `#blackScreen`。
> > - `maxStacks` 属性**固定为** `1`。
> > - `refreshDuration` 属性**固定为** `true`。
> > - `interval` 属性**固定为** `10`。

## 示例 {#examples}

当生物传送时使玩家致盲

```yaml
BlackScreen:
  Skills:
  - blackscreen{d=2} @PlayersInRadius{r=100} ~onTeleport
```

## 别名 {#aliases}

- effect:blackScreen
- e:blackScreen
