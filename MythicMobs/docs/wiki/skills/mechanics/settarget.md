---
title: Settarget
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/settarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Settarget {#settarget}

## 说明 {#description}

将生物的目标设为目标实体。
如果使用仇恨表，则会提高该实体的仇恨值，直到达到切换目标所需的阈值。

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

右键交互时，将施法者的目标设为触发实体。

```yaml
  Skills:
  - setTarget @trigger ~onInteract
```

## 别名 {#aliases}

- target
