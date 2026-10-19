---
title: Locations Of Targets
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LocationsOfTargets
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Locations Of Targets {#locations-of-targets}

## 说明 {#description}

定位继承目标的位置

## 属性 {#attributes}

> *此目标选择器没有属性*

## 示例 {#examples}

```yaml
ExampleSkill1:
  Skills:
  - skills{s=ExampleSkill2} @EIR{r=10}

ExampleSkill2:
  Skills:
  - lightning @LocationsOfTargets
```

## 别名 {#aliases}

- locationOfTarget
- LOT
