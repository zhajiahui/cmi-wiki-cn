---
title: Owner
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/owner
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Owner {#owner}

## 说明 {#description}

检查目标实体是否是施法者的所有者。

- 如果施法者是可驯服的生物，则将检查目标实体是否是该生物的“普通”所有者
- 如果施法者不是可驯服的生物，则为了匹配目标实体，必须通过 [SetOwner](../mechanics/setowner.md) 机制将其设置为所有者

## 属性 {#attributes}

> *此条件没有属性*

## 示例： {#examples}

```yaml
  TargetConditions:
  - owner true
```

## 别名 {#aliases}

- isOwner
