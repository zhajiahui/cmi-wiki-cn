---
title: Removetag
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/removetag
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Removetag {#removetag}

## 说明 {#description}

从目标上删除记分板标签。

这与 **hastag 条件** 结合使用（请参阅[条件](https://wiki.mythiccraft.io/mythicmobs/conditions/start)）。你还可以使用普通命令 `/scoreboard players tag <player name> remove [Tag Name]` 来执行相同的操作。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| tag | t | 标签的字符串名称。 | default |

## 示例 {#examples}

此技能会为施法生物添加 Test 标签。

```yaml
UntagSkill:
  Skills:
  - removetag{t=Test} @self
```

## 别名 {#aliases}

- removescoreboardtag
- tagremove
