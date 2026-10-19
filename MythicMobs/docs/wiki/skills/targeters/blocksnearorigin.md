---
title: Blocks Near Origin
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/BlocksNearOrigin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Blocks Near Origin {#blocks-near-origin}

## 说明 {#description}

瞄准元技能原点周围半径内的所有方块

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 2 |
| radiusy | ry, yradius, yr | 半径的 y 分量。 | radius |
| shape | s | 所选方块的形状，可以为 `SPHERE`、`CUBE`。 | SPHERE |
| noise | n | 目标选择器的随机程度。 | 0 |
| noair | na | 是否不以空气为目标。 | true |
| onlyair | oa | 是否仅以空气为目标。 | false |

## 示例 {#examples}

此技能会选中元技能原点周围半径 10 格内的部分方块

```yaml
ExampleSkill:
  Skills:
  - effect:particles @BlocksNearOrigin{r=10;noise=0.5}
```

## 别名 {#aliases}

- BNO
