---
title: Blocks In Chunk
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/BlocksInChunk
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Blocks In Chunk {#blocks-in-chunk}

## 说明 {#description}

相对于继承目标，选中对应区块中的所有方块

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| noair | na | 是否不以空气为目标。 | true |
| onlyair | oa | 是否仅以空气为目标。 | false |
| nearorigin | no | 目标选择器是否也以原点为目标。 | false |

## 示例 {#examples}

这些元技能会选中技能树触发者所在区块中的每个非空气方块

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @trigger

ExampleSkill2:
  Skills:
  - effect:particles @BlocksInChunk
```

## 别名 {#aliases}

- BIC
