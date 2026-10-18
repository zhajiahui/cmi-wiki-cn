---
title: 位置目标选择器
source: https://docs.phoenixdevt.fr/mythiclib/scripts/targeters/location
source_snapshot: '2026-10-19'
---

# 位置目标选择器 {#location-targeters}

> **警告**
>
> 建设中

位置目标选择器用于指定要执行机制或脚本的位置。位置目标选择器可能会返回多个位置，在这种情况下，机制/脚本将被执行多次，每个位置一次。

## 脚轮 {#caster}

使用它来定位脚本施法者的位置。可选的`position`参数允许你访问玩家机身上的精确位置，从最低到最高：`FEET`、`BODY`（中间）、`EYES`（眼睛高度）、`TOP`。默认设置为`BODY`。

```yml
location_targeter_caster_1:
  public: true
  mechanics:
  - 'particle{particle=FLAME;target=caster;amount=100;x=0.5;y=1;z=0.5;speed=0.1}'

location_targeter_caster_2:
  public: true
  mechanics:
  - 'particle{particle=FLAME;target={type=caster;position=TOP};amount=100;x=0.1;y=0.1;z=0.1;speed=0.05}'
```

## 圆 {#circle}

使用它可以在距中心位置一定距离的情况下多次运行脚本。`amount`是圆上的样本点数。例如，如果你生成粒子，则越高，圆圈就会显得越“平滑”。`radius`是圆的半径。

将`source`参数设置为`true`将使用脚本源位置作为中心位置。如果设置为`false`，MythicLib将首先尝试使用脚本目标位置作为中心位置。

```yml
location_targeter_circle:
  public: true
  mechanics:
  - 'particle{particle=FLAME;target={type=circle;radius=3;amount=30;source=false}}'
```

## 自定义位置 {#custom-position}

使用此目标选择器，你可以手动输入位置 X、Y 和 Z。将`relative`设置为`true`将**添加**到你输入目标脚本位置的位置，或者如果`source`设置为`false`则施法者位置。例如，以下示例返回脚本源位置上方的一个块。

```yml
location_targeter_custom:
  public: true
  mechanics:
  - 'particle{particle=FLAME;target={type=custom;x=1;y=1;z=1;source=true;relative=true};amount=100;x=0.1;y=0.1;z=0.1;speed=0.05}'
```

## 源位置 {#source-location}

使用它来定位脚本源位置。它通常是最初运行脚本的玩家的位置。

```yml
location_targeter_source:
  public: true
  mechanics:
  - 'particle{particle=LAVA;target=source_location;amount=10;x=0.1;y=0.1;z=0.1}'
```

## 目标实体位置 {#target-entity-location}

脚本目标实体的位置。可选的`position`参数允许你访问玩家机身上的精确位置，从最低到最高：`FEET`、`BODY`（中间）、`EYES`（眼睛高度）、`TOP`。默认设置为`BODY`。

```yml
location_targeter_target:
  public: true
  mechanics:
  - 'particle{particle=LAVA;target={type=target;position=BODY};amount=10;x=0.1;y=0.1;z=0.1;speed=0.05}'
```

## 目标位置 {#target-location}

定位脚本目标位置。

```yml
location_targeter_target_loc:
  public: true
  mechanics:
  - 'particle{particle=LAVA;target=target_location;amount=10;x=0.1;y=0.1;z=0.1}'
```

## 位置变量 {#location-variable}

如果位置/位置恰好存储为脚本中的变量，你可以使用此目标选择器访问它。`name`是要用作目标位置的变量的名称。

```yml
location_targeter_variable:
  public: true
  mechanics:
  - 'copy_vector{value="caster.location";variable=l}' # copy caster location to variable "l"
  - 'set_x{variable=l;x=" <l.x> + 5"}' # add 1 to the X of the location stored in variable "l"
  - 'particle{particle=LAVA;target={type=variable;name=l};amount=10;x=0.1;y=0.1;z=0.1}'
```

---

原文：[Location Targeters](https://docs.phoenixdevt.fr/mythiclib/scripts/targeters/location) · 原文归档：2026-10-19
