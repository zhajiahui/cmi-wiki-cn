---
title: Targeted Target
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetedTarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Targeted Target {#targeted-target}

## 说明 {#description}

选中继承的目标实体。可配合[目标选择器选项](../targeters.md#targeter-options)进行[目标过滤](../metaskills.md#targets-filtering)。

## 属性 {#attributes}

> *此目标选择器没有属性*

## 示例 {#examples}

```yaml
ExampleSkill1:
  Skills:
  - skills{s=ExampleSkill2} @PIR{r=10}
```

##  {#section}

```yaml
ExampleSkill2:
  Skills:
  - lightning @TargetedTarget
```

## 别名 {#aliases}

- targeted
