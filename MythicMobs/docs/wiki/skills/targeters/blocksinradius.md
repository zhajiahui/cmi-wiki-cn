---
title: Blocks In Radius
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/BlocksInRadius
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Blocks In Radius {#blocks-in-radius}

## 说明 {#description}

以继承目标半径内的所有方块为目标。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 2 |
| radiusy | ry, yradius, yr | 半径的 y 分量。 | radius |
| shape | s | 所选方块的形状，可以为 `SPHERE`、`CUBE`。 | SPHERE |
| noise | n | 目标选择器的随机程度。 | 0 |
| noair | na | 是否不以空气为目标。 | true |
| onlyair | oa | 是否仅以空气为目标。 | false |
| nearorigin | no | 目标选择器是否以原点为目标。 | false |

## 示例 {#examples}

这些元技能可选中技能树触发者周围半径 10 格内的每个非空气方块

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @trigger

ExampleSkill2:
  Skills:
  - effect:particles @BlocksInRadius{r=10}
```

## 别名 {#aliases}

- BIR
