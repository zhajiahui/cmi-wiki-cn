---
title: Hide
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/hide
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Hide {#hide}

## 说明 {#description}

在设定的时间内对目标玩家隐藏施法者。

> 然后可以通过使用 [showentity](showentity.md) 机制来显示隐藏的实体。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| auraname | buffname, debuffname | 光环名称。 | #hiding |
| ignoreAuraOptions | iao, permanent, perma | 使此机制忽略所有与[光环](aura.md)相关的选项及 `duration` 属性。 | false |

> 该机制继承了[光环](aura.md)机制的所有属性
>

> > - `auraname` 属性**默认为** `#hiding`。
> > - `charges` 属性**固定为** `1`。
> > - `maxStacks` 属性**固定为** `1`。
> > - `mergeAll` 属性**固定为** `true`。

## 示例 {#examples}

```yml
DUMMY:
  Type: ZOMBIE
  Skills:
  - hide{d=100} @Server ~onInteract
```

##  {#section}

```yml
CUSTOM_ITEM:
  Id: STICK
  Skills:
  - hide{d=100} @Server ~onUse #User is now invisible from all online players, no armor is shown
```

## 别名 {#aliases}

- hideFromPlayers
- hideFromPlayer
