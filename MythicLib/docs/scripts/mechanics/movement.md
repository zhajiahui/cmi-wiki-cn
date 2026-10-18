---
title: 移动
source: https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/movement
source_snapshot: '2026-10-19'
---

# 移动 {#🚶-movement}

## 传送一个实体 {#teleport-an-entity}

这会将目标实体传送到目标位置。

|参数|别名 |描述 |默认 |
| --- | --- | --- | --- |
| target_location | - | 需要位置目标选择器。传送到哪里。 | target location |
| target | - | 需要实体目标选择器。要传送的实体。 | caster |
| y_offset | - | 应用于目标位置的 Y 偏移。 | 0 |

```yml
example_mechanic:
  mechanics:
  - 'teleport{y_offset=0;target=caster;target_location={type=custom;world=world;x=-140,y=67,z=10}}'
```

## 设置实体的速度 {#set-the-velocity-of-an-entity}

你需要使用变量来提供位置（<=>向量）。在以下示例中，向量保存在名为`velocity1`的变量中。

| Parameter | Alias | 描述 | Default |
| --- | --- | --- | --- |
| target | - | 需要实体目标选择器。要设置速度的实体。 | caster |
| value | val, v, vector, vec, velocity, vel | 包含要设置速度的矢量（位置）的变量名称。 | none |

```yml
example_mechanic:
  mechanics:
  - 'set_vector{var=velocity1;x=0;y=1;z=0}'
  - 'set_velocity{target=caster;value=velocity1}'
```

---

原文：[🚶 Movement](https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/movement) · 原文归档：2026-10-19
