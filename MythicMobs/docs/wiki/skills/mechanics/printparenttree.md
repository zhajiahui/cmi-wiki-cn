---
title: Print Parent Tree
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PrintParentTree
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Print Parent Tree {#print-parent-tree}

## 说明 {#description}

打印有关执行机制的 Metaskill 及其 SkillTree 的调试信息

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

```yaml
Example1:
  Skills:
  - skill{s=Example2}

Example2:
  Skills:
  - skill{s=Example3}

Example3:
  Skills:
  - printParentTree
```
