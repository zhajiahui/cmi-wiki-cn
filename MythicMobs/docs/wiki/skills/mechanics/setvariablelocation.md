---
title: Setvariablelocation
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setvariablelocation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setvariablelocation {#setvariablelocation}

## 说明 {#description}

设置字符串值，其内容取决于传入 value 参数的位置，包含目标位置的坐标与世界信息。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| value | val, v, a, amount | 目标位置 | @self |

> 该机制继承了 [SetVariable](setvariable.md) 机制的所有*可继承*属性

## 示例 {#examples}

```yaml
TestSkill:
 Skills:
 - setvarloc{var=caster.1;v=@self} @self
 - m{m=<caster.var.1>} @self
```

## 别名 {#aliases}

- variableSetLocation
- setVarLoc
