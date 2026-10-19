---
title: Target
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Target
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Target {#target}

## 说明 {#description}

瞄准施法者的目标。

- 如果施法者是生物，则瞄准其目标
- 如果施法者是玩家，则选中玩家视线中距离足够近的实体

请注意，恶魂等部分实体的 AI 是硬编码的，永远不会设置目标，因此此目标选择器对它们无效

## 属性 {#attributes}

> *此目标选择器没有属性*

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - ignite @Target
```

## 别名 {#aliases}

- T
