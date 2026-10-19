---
title: Entities Near Origin
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesNearOrigin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Entities Near Origin {#entities-near-origin}

## 说明 {#description}

选中元技能原点周围指定半径内的所有实体。此目标选择器扩展自 **[EntitiesInRadius 目标选择器](entitiesinradius.md)**，因此**支持它的全部属性**

## 属性 {#attributes}

> *此目标选择器没有独有属性，但可使用 [EntitiesInRadius](entitiesinradius.md) 的属性*

## 示例 {#examples}

在此示例中，创建的弹射物无论因何结束，都会对其周围半径 2 格内的所有活体实体造成伤害

```yaml
  Skills:
  - projectile{...;
    onTick=[
      - effect:particles @origin
    ];
    onEnd=[
      - damage{a=10} @ENO{r=2}
    ]
    } @target
```

## 别名 {#aliases}

- NearOrigin
- ENO
