---
title: Trigger
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Trigger {#trigger}

## 说明 {#description}

定位触发技能树的实体

## 属性 {#attributes}

> *此目标选择器没有属性*

## 示例 {#examples}

```yaml
TomTheMurderous:
  Type: COW
  Skills:
  - damage{a=20} @trigger ~onInteract
```
