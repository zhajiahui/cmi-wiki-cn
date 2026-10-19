---
title: Template Type
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/TemplateType
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Template Type {#template-type}

## 说明 {#description}

检查目标生物是否扩展指定的[模板](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Mobs/Templates)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| templates | template, t | 要匹配的模板。可以指定模板列表，此时存在任意一个指定模板，条件即成立。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - templatetype{template=NetherMob,EndMob}
```

## 别名 {#aliases}

- template
- instanceOf
