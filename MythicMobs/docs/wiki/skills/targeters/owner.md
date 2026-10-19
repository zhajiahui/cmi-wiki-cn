---
title: Owner
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Owner
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Owner {#owner}

## 说明 {#description}

以施法生物的拥有者为目标。   所有者可以通过 [SetOwner](../mechanics/setowner.md) 机制设置。

## 属性 {#attributes}

> *此目标选择器没有属性*

## 示例 {#examples}

此元技能将向施法生物的所有者发送一条消息

```yaml
ExampleSkill:
  Skills:
  - message{m="Hello there!"} @Owner
```
