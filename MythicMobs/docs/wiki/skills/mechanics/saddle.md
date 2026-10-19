---
title: Saddle
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/saddle
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Saddle {#saddle}

## 说明 {#description}

允许在目标实体上装备或移除马鞍。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| take | t, remove, r | 是否改为移除鞍 | false |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - saddle{r=true} @self
```

下面的例子有点微妙：它展示了如何制作一匹可以给自己配备临时马鞍的马

```yaml
ExampleMob:
  Type: HORSE
  Options:
    Tamed: true
  Skills:
  - aura{d=1200;auraName=TemporarySaddle;cd=600;sync=true;i=1;
    onStart=[
    - saddle @self
    ];
    onTick=[
    - particle{p=crit;hs=0.3;vs=0.2;y=1;a=2} @self
    - closeinventory @Passenger
    ];
    onEnd=[
    - saddle{r=true} @self
    ]
    } @self ~onInteract
```

## 别名 {#aliases}

- setsaddle
- givesaddle
