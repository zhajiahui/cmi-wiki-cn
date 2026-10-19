---
title: Addtag
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/addtag
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Addtag {#addtag}

## 说明 {#description}

向目标添加记分板标签。

这与**hastag 条件**结合使用（请参阅[条件](../conditions/hastag.md)）。你还可以使用普通命令 `/tag <targets> add <name>` 来执行相同的操作。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| tag | t | 标签的字符串名称。 | default |

## 示例 {#examples}

此技能会为施法生物添加 Test 标签。

```yaml
TagSkill:
  Skills:
  - addtag{t=Test} @self
```

##  {#section}

此技能仅在生物具有 Test 标签时运行。

```yaml
TagTest:
  Conditions:
  - hastag{t=Test}
  Skills:
  - suicide @self
```

## 别名 {#aliases}

- addscoreboardtag
- tagadd
