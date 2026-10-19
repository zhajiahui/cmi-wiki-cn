---
title: Setscore
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setscore
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setscore {#setscore}

## 说明 {#description}

修改假玩家姓名的记分板目标值。与[修改分数](modifyscore.md)机制类似，但只能执行**设置**操作。

## 属性 {#attributes}

> 该机制继承了 [ModifyScore](modifyscore.md) 机制的每个*可继承*属性
>

> > - `action`属性在`SET`**设置**并且无法修改

## 示例 {#examples}

此示例将为目标“TestScore”设置名为“Bob”的玩家的分数，即使该玩家在服务器上不存在。如果目标当前不存在，它将创建该目标。

```yaml
  Skills:
  - setscore{o=TestScore;e=Bob;v=1} ~onInteract 
```

![](https://i.imgur.com/0HKvAUM.png)
