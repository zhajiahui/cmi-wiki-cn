---
title: For Each
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ForEach
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# For Each {#for-each}

## 说明 {#description}

为机制的每个目标*一次且单独*执行指定的元技能。将调用的每个元技能都将有一个实体/位置（来自原始目标）作为其继承目标。

每次迭代时，此机制都会在被调用的元技能中设置技能作用域变量 `<skill.var.index>`，保存当前目标的索引。索引从 0 开始，每处理一个目标就增加 1，实体目标和位置目标分别计数。不要与 forEachValue 的 `<skill.index>` 混淆，它们是不同的标记。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| targettype | targett, tt | 此机制要遍历的目标类型，可以为 `ALL`、`ENTITY` 或 `LOCATION`。 | ALL |

> 该机制继承了[技能](skill.md)机制的所有属性

## 示例 {#examples}

```yaml
# Skills file
ExampleForEach:
  Skills:
  - setvariable{var=skill.listuuid;type=LIST;val=""} @self
  - foreach{skill=ExampleSkill} @PIR{r=10;sort=NEAREST}
  - message{m=<skill.var.listuuid>}

ExampleSkill:
  Skills:
  - variableadd{var=skill.listuuid;value=<target.uuid>}
```

##  {#section}

```yaml
# Skills file
IndexForEach:
  Skills:
  - foreach{skill=IndexSkill} @PIR{r=10;sort=NEAREST}

IndexSkill:
  Skills:
  - message{m="Target number <skill.var.index>"} @self
```

> 为最近的目标打印“目标编号0”，为下一个打印“目标编号1”，依此类推。
