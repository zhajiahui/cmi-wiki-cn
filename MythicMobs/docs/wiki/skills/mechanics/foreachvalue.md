---
title: For Each Value
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ForEachValue
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# For Each Value {#for-each-value}

## 说明 {#description}

对指定列表/映射格式值的每个值执行一次指定的元技能*一次且单独*。将调用的每个元技能都将根据迭代值设置特殊技能参数：

- 对于列表格式的输入
  - `<skill.value>` 为迭代值
  - `<skill.index>` 为值的索引
- 对于映射格式输入：
  - `<skill.key>` 为迭代键
  - `<skill.value>` 为迭代值
  - `<skill.index>` 为键值对的索引

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| values | val, v | 要遍历的列表或映射格式的字符串。 |  |

> 该机制继承了[技能](skill.md)机制的所有属性

## 示例 {#examples}

```yaml
# Skills file
ExampleForEachValue:
  Skills:
  - setvariable{var=skill.listnames;type=LIST;val="Steve,Alex"} @self
  - foreachvalue{skill=ExampleSkill;values=<skill.var.listnames>} @self # Can also directly use the entry1,entry2,entry3... syntax

ExampleSkill:
  Skills:
  - message{m="Found you :D"} @PlayerByName{name=<skill.value>}
```

```yaml
# Skills file
ExampleForEachValueForMap:
  Skills:
  - setvariable{var=skill.mapnames;type=MAP;val="Steve=hello;Alex=1,2,3"} @self
  - foreachvalue{skill=ExampleSkill;values=<skill.var.mapnames>} @self # Can also directly use the key=value;key2=value2... syntax

ExampleSkill:
  Skills:
  - message{m="You have a value of <skill.value>"} @PlayerByName{name=<skill.key>}
```
