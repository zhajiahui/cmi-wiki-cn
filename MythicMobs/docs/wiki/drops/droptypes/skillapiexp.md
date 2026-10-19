---
title: SkillAPI 经验
source_url: https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/SkillAPIExp
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# SkillAPI 经验

# Skill A P I 经验 {#skill-a-p-i-exp}

## 说明 {#description}

掉落时，如果触发者是玩家，就会获得指定数量的 SkillAPI 经验。奖励消息中可以使用 `<drop.amount>` [占位符](../../skills/placeholders.md#misc-placeholders)获取发放的经验数量。这条消息可以在 `config-general.yml` 文件中配置。

## 属性 {#attributes}

> *此掉落类型没有属性。*

## 示例 {#examples}

```yaml
  Drops:
  - skillapi-exp 20
```

## 别名 {#aliases}

- skillapiexp
