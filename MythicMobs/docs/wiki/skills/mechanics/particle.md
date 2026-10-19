---
title: Particle
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle {#particle}

## 说明 {#description}

在目标实体或位置创建粒子效果。

可以在 **[此处](particle/particle-types.md)** 找到粒子类型列表。

[Spigot Javadoc 列出的粒子效果也都应可使用。](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html)

## 属性 {#attributes}

### 常规属性 {#general-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| particle | p | 要使用的[粒子类型](particle/particle-types.md)。 | reddust |
| mob | m, t | 作为粒子生成的实体，不可为原始实体。**仅 Premium 版**支持。 |  |
| amount | count, a | 要创建的粒子数量。 | 10 |
| spread | offset | 粒子的竖直散布。 | 0 |
| hSpread | hs | 粒子的水平散布。 | `spread` |
| vSpread | vs, yspread, ys | 粒子在 y 轴方向的散布，覆盖 `spread`。 | `spread` |
| xSpread | xs | 粒子在 x 轴方向的散布，覆盖该轴上的 `hSpread`。 | hSpread |
| zSpread | zs | 粒子在 z 轴方向的散布，覆盖该轴上的 `hSpread`。 | hSpread |
| speed | s | 粒子的“speed”值。如果粒子具有 [DataType](particle/particle-types.md#datatypes)，此属性的行为会不一致。 | 0 |
| yOffset | y | 粒子相对于目标的 Y 轴偏移。 | 0 |
| viewDistance | vd | 粒子的渲染距离。 | 128 |
| fromorigin | fo | 是否从机制原点生成粒子。 | false |
| directional | d | 粒子是否定向移动。所用的[粒子类型](particle/particle-types.md)必须不带额外数据或额外属性。 | false |
| directionReversed | dr | 反转粒子的方向。 | false |
| direction | dir | 指定粒子移动方向的向量。 | 0,0,0 (x,y,z) |
| fixedyaw | yaw | 设置机制所选位置目标的偏航角。保留为 -1111 时忽略此项。 | -1111 |
| fixedpitch | pitch | 设置机制所选位置目标的俯仰角。保留为 -1111 时忽略此项。 | -1111 |
| audience |  | 粒子效果的[可见对象]。 | nearby |
| color | c | 粒子的颜色，须粒子支持此项。 |  |
| exactoffsets | eo | 更改计算粒子随机生成位置的公式。 | false |

#### 额外属性 {#extra-attributes}

根据所使用的特定[粒子类型](particle/particle-types.md)，额外的属性也将可在粒子相关机制中使用。你可以通过从[粒子类型维基页面](particle/particle-types.md)访问特定粒子的页面来找到更多信息

#### 生物类型粒子 [**仅限 Premium 版**] {#mob-type-particles-premium-only}

这种粒子会用指定实体替代生成的粒子。实体会像普通实体一样行动，可以攻击、受伤、触发技能等，但与施法者之间没有父实体或所有者关系。

### 仅实体可用的属性 {#entity-only-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| useEyeLocation | uel | (true/false) 是否以实体的眼睛位置为粒子基准。 | false |
| forwardOffset | startfoffset, sfo | 相对于目标实体的向前偏移，`directional` 设为 true 时无效。 | 0 |
| sideOffset | soffset, sso | 相对于目标实体的侧向偏移，`directional` 设为 true 时无效。 | 0 |

## 示例 {#examples}

```yaml
  Skills:
  - effect:particles{particle=flame;amount=200;hS=1;vS=1;speed=5} @self
  - ...
```

```yaml
  Skills:
  - effect:particles{particle=block;m=dirt;amount=100;hS=1;vS=1} @self
  - ...
```

```yaml
  Skills:
  - particles{particle=flame;a=10;hs=0.3;vs=0.3;y=0.3;s=0.1125} @self
  - ...
```

## 别名 {#aliases}

- effect:particles
- effect:particle
- particles
- particle
- e:particles
- e:particle
- e:p
