---
title: Setcollidable
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setcollidable
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setcollidable {#setcollidable}

## 说明 {#description}

设置技能机制的目标是否应该有可碰撞的碰撞箱。
  
结果相当于 [Collidable](../../mobs/options.md#collidable) 选项。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| collidable | state, value, c | 设置生物是否具有碰撞 | false |

## 示例 {#examples}

在这个例子中，生物一旦受到伤害源就会永久变得不可碰撞。

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - setcollidable{c=false} @self ~onDamaged
```

##  {#section}

在这个例子中，生物将会给自己施加一个光环。在光环持续时间内，生物将不可碰撞。

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - aura{d=100;rd=true;ms=1;
    onStart=[
    - setcollidable{c=false} @self
    ];
    onEnd=[
    - setcollidable{c=true} @self
    ]} @self ~onDamaged
```
