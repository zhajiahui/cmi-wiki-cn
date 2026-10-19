---
title: Variable Move
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/VariableMove
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Variable Move {#variable-move}

## 说明 {#description}

在名称和/或注册表之间移动已创建的变量。默认情况下，不会创建新变量，因此这可用于使两个不同的注册表引用完全相同的变量，从而允许对一个注册表的修改反映在另一个注册表中

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| from |  | 要移动的变量，使用 `scope.name` 格式 |  |
| to |  | 变量要移动到的位置，使用 `scope.name` 格式 |  |
| removeOld |  | 是否从旧变量注册表中移除已移动的变量 | false |
| createNew |  | 是否在目标变量注册表中新建变量 | false |
| inheritExpirationTime |  | `createNew` 为 true 时，新变量是否继承旧变量的过期时间 | true |

## 示例 {#examples}

```yaml
  Skills:
  - setVar{name=caster.item;type=ITEM;value=slot:HAND} @self
  - movevariable{from=caster.item;to=skill.item} @self
  - equip{item=itemvariable{variable=skill.item} head} @self
```

## 别名 {#aliases}

- moveVariable
- moveVar
- varMove
