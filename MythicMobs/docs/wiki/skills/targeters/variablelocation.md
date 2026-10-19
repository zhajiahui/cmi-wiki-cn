---
title: Variable Location
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/VariableLocation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Variable Location {#variable-location}

## 说明 {#description}

定位指定变量中存储的位置。可以通过 [SetVariableLocation](../mechanics/setvariablelocation.md) 机制设置这样一个变量。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| variable | name, n, var, key, k | 变量名称。 |  |
| scope | s | 变量的作用域，也可通过 scope.name 语法在名称中设置。 |  |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - setvarloc{var=caster.1;v=@targetlocation} @self
  - particle{y=2} @VariableLocation{var=caster.1}
```

## 别名 {#aliases}

- varLocation
