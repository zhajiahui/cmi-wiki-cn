---
title: 作用域占位符表
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders/Scoped-Placeholder-Table
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 作用域占位符表

# 带作用域的占位符表 {#scoped-placeholder-table}

| 作用域 | 目标实体 |
| --- | --- |
| `caster` | 技能机制的施法者 |
| `target` | 技能机制的目标。例如，`- message{m=<target.name>} @NearestPlayer` 会向最近的玩家发送该玩家自己的名称 |
| `trigger` | 技能机制的触发者，即导致技能触发的实体。例如，`<trigger.name>` 配合 `~onDeath` 触发器会返回击杀该生物的实体名称 |
| `owner` | 施法实体的主人 |
| `parent` | 施法实体的父实体 |
