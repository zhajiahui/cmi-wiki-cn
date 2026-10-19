---
title: On Bucket
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onBucket
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Bucket {#on-bucket}

## 说明 {#description}

牛被挤奶，或实体被装入桶中时执行技能，适用于美西螈等可装桶的实体。

> 关联的 [@trigger](../targeters/trigger.md) 是施法者本身

## 示例 {#examples}

```yaml
ANormalCow:
  Type: Cow
  Skills:
  - skill{s=[
    - message{m="HOW DARE YOU?!?"} @trigger
    - sound{s=entity.creeper.primed}
    - explosion{yield=5;delay=30}
    ];cd=2} @self ~onBucket
```

## 别名 {#aliases}

- onUseBucket
- onFillBucket
- onBucketFill
- onMilk
- onMilked
