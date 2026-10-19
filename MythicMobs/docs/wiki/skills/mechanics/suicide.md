---
title: Suicide
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/suicide
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Suicide {#suicide}

## 说明 {#description}

立即杀死生物。此机制没有目标选择器，只影响施法生物。它不适用于船、盔甲架等部分非活体实体，这些实体建议使用 [remove](remove.md)。

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

10% 受伤时有几率杀死施法生物。

```yaml
  Skills:
  - suicide ~onDamaged 0.1
```
