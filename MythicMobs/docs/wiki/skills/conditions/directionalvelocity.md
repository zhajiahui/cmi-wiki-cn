---
title: Directionalvelocity
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/directionalvelocity
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Directionalvelocity {#directionalvelocity}

## 说明 {#description}

检查目标的速度是否与给定参数匹配的条件。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| x | s, side | X 轴速度，可以是范围。未设置时，此条件不检查该项。 |  |
| absx | ax, abss, as | 是否仅使用 X 轴速度的绝对值。 | `relative`'s value |
| y | up, down, vertical, v | Y 轴速度，可以是范围。未设置时，此条件不检查该项。 |  |
| absy | ay | 是否仅使用 Y 轴速度的绝对值。 | false |
| z | f, forward | Z 轴速度，可以是范围。未设置时，此条件不检查该项。 |  |
| absz | az, absf, af | 是否仅使用 Z 轴速度的绝对值。 | false |
| relative | rel | 检查是否相对于实体的朝向，而不是世界坐标轴。为 true 时，X 表示前后方向，Z 表示左右方向。 | false |

### X、Y 和 Z 属性 {#x-y-and-z-attributes}

他们检查实体沿这些轴的速度。但这也意味着速度本身可以是正值或负值，具体取决于方向本身。

> - 如果你**朝 `positive` X 值**移动，你将拥有 **`positive` X 速度**。
> - 如果你**朝 `negative` X 值**移动，你将拥有 **`negative` X 速度**
> - 如果你**跳跃`up`**，你将拥有**`positive` Y 速度**
> - 如果你**下落`down`**，你将拥有**`negative` Y 速度**

### Absx、Absy 和 Absz 属性 {#absx-absy-and-absz-attributes}

有时只想检查移动的大小，而非方向。为此，可启用对应属性；启用 X、Y 或 Z 轴的属性后，就只检查绝对值，不再考虑实际方向。

> - 如果你**跳跃`up`**，你将拥有**`positive` Y 速度**
> - 如果你**下落`down`**，你将拥有**`positive` Y 速度**

## 示例 {#examples}

在此示例中，我们检查玩家 y 速度的绝对值是否低于5。

```yaml
  Conditions:
  - directionalVelocity{y=<0;absx=true} true
```

## 别名 {#aliases}

- dvelocity
