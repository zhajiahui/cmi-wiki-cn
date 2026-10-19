---
title: Has Aura Type
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HasAuraType
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Has Aura Type {#has-aura-type}

## 说明 {#description}

检查目标实体是否具有给定的光环类型

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| auragroup | auratype, group, type, t, g | 要检查的光环类型。 |  |

## 示例 {#examples}

此示例将应用 `Example` 类型的光环。然后第二个示例将检查它是否存在

```yaml
  Skills:
  - aura{auraName=NotMeThisTime;auratype=Example;d=100} @self
```

```yaml
  Conditions:
  - hasAuraType{type=Example} true
```

## 别名 {#aliases}

- hasbufftype
- hasdebufftype
