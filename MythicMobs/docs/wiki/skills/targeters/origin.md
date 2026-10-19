---
title: Origin
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Origin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Origin {#origin}

## 说明 {#description}

选中元技能的“原点”或“来源”位置。这个位置通常是施法生物的位置，但这一说法并非总是成立（  true  ），例如 Projectile 技能的“原点”就是弹射物所在位置

## 属性 {#attributes}

> *此目标选择器没有属性*

## 示例 {#examples}

origin 目标选择器的用法很多。以下面的元技能为例：

```yaml
ExampleSkill:
  Skills:
  - effect:particles @origin
```

如果由生物正常执行此技能，粒子会出现在生物所在位置，因为此时技能原点就是生物本身。在这种情况下，`origin` 与 `self` 目标选择器的行为相同。

但如果在元机制内部执行元技能，或通过 [Origin 通用属性](../mechanics.md#universal-attributes)手动更改技能原点，技能原点通常就会改变，粒子也会显示在其他位置。

`origin` 的具体位置取决于上下文。有关此行为的更多信息，可查看实际使用原点的各个技能机制的 Wiki 页面。

## 别名 {#aliases}

- source
