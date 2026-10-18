---
title: 实体目标选择器
source: https://docs.phoenixdevt.fr/mythiclib/scripts/targeters/entity
source_snapshot: '2026-10-19'
---

# 实体目标选择器 {#entity-targeters}

> **警告**
>
> 建设中

## 脚轮 {#caster}

使用此目标选择器来瞄准技能脚轮。此目标选择器没有参数，因此你可以仅使用`target=caster`而不是`target={type=caster}`。

```yml
message_script:
  public: true
  mechanics:
  - message{format="Hello world!";target=caster}
```

## 锥体 {#cone}

以圆锥体中的实体为目标，给定圆锥体`angle`和`radius`（它们是数字参数）。你可以对这些参数使用数学公式。角度以度为单位给出。`source`参数是可选的，你可以使用位置目标选择器提供圆锥体的起点。它默认设置为施法者的位置。

`direction`参数也是可选的，你需要使用位置目标选择器提供圆锥体的方向。默认情况下，它设置为施法者眼睛的方向。

```yml
cone_slash_attack:
  public: true
  mechanics:
  - 'damage{amount=10;source=caster;target={type=cone;radius=3;angle=90}}'
```

## 附近的实体 {#nearby-entities}

使用它来定位给定半径和高度的特定位置周围的实体。这基本上将所有实体置于一个高度为`height`且围绕中心位置半径为`radius`的 **圆柱体** 中。

将`source`参数设置为`true`将使用脚本源位置作为中心位置。如果设置为`false`，ML 将首先尝试使用脚本目标位置作为中心位置。

默认情况下，`nearby_entities`目标选择器会忽略施法者/实体技能目标。如果你关闭`ignore_caster`，则目标选择器将考虑技能施法者/实体技能目标。

```yml
aoe_damage_skill:
  public: true
  mechanics:
  - 'damage{amount=10;target={type=nearby_entities;radius=10;height=5;ignore_caster=true}}'
```

## 最近的实体 {#nearest-entity}

获取最接近脚本目标位置的实体，最大范围为`radius`。

将`source`参数设置为true将使用脚本源位置作为中心位置。如果设置为false，ML 将首先尝试使用脚本目标位置作为中心位置。

```yml
damage_to_nearest_entity:
  public: true
  mechanics:
  - 'damage{amount=10;target={type=nearest_entity;radius=10}}'
```

## 目标实体 {#target-entity}

最简单的一种目标选择器，用于定位脚本目标。

```yml
damage_to_target:
  public: true
  mechanics:
  - 'damage{amount=10;target=target}'
```

## 看着 {#looking-at}

瞄准施法者正在查看的实体。有可能没有找到任何实体，在这种情况下，使用此目标选择器的机制将不会被执行。`size`是光线追踪的大小，将其设置为`1`意味着你将击中边界框距离视线最多为1块的实体。`length`是实体可以瞄准的最大距离。`ignore_passable`可用于忽略可通过的方块，例如高草或花朵。

```yml
damage_on_line_of_sight:
  public: true
  mechanics:
  - 'message{format="test"}'
  - 'damage{amount=10;target={type=looking_at;size="0.2 + 0.3";length="50 + 30";ignore_passable=false}}'
```

## 可变目标 {#variable-target}

如果某个实体恰好作为变量存储在脚本中，你可以使用此目标选择器访问它。

```yml
damage_to_self:
  public: true
  mechanics:
  - 'damage{amount=10;target={type=variable;name="caster"}}' # variable name with 'caster' returns the skill caster
```

---

原文：[Entity Targeters](https://docs.phoenixdevt.fr/mythiclib/scripts/targeters/entity) · 原文归档：2026-10-19
