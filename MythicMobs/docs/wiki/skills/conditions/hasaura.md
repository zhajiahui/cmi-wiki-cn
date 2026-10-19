---
title: Hasaura
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasaura
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Hasaura {#hasaura}

## 说明 {#description}

检查目标实体是否具有给定的光环

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| aura | auraname, b, buff, buffname, debuff, debuffname, n, name | 要检查的光环名称。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - hasaura{aura=firedebuff} true
```

## 别名 {#aliases}

- hasbuff
- hasdebuff
