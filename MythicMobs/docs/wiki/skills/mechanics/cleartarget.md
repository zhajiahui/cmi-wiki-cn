---
title: Clear Target
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ClearTarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Clear Target {#clear-target}

## 说明 {#description}

强制技能机制的目标重置当前目标。

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

```yaml
  Skills:
  - cleartarget @self ~onTimer:20 ?targetalive ?!targetwithin{d=20}
```

## 别名 {#aliases}

- resetTarget
