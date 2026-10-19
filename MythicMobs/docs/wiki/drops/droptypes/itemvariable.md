---
title: 物品变量
source_url: https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/ItemVariable
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 物品变量 {#item-variable}

## 说明 {#description}

掉落指定物品变量中定义的物品。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| variable | var, name, n | 要获取的物品变量的作用域和名称，格式为 scope.name |  |

## 示例 {#examples}

```yaml
  Drops:
  - itemvariable{variable=caster.stolenitem} 1 1
```

## 别名 {#aliases}

- itemvar
