---
title: Variableunset
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/variableunset
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Variableunset {#variableunset}

## 说明 {#description}

取消设置[变量](../variables.md)。

## 属性 {#attributes}

> 该机制继承了 [SetVariable](setvariable.md) 机制的所有*可继承*属性

## 示例 {#examples}

从施法者身上取消设置名为 test 的施法者作用域变量。

```yaml
RemoveVariable:
  Skills:
  - variableUnset{var=caster.testing} @self
```

这种写法也会从施法者身上取消设置名为 test 的施法者作用域变量。

```yaml
RemoveVariable:
  Skills:
  - variableUnset{var=testing;scope=caster} @self
```

## 别名 {#aliases}

- unsetvariable
- unsetvar
- varunset
