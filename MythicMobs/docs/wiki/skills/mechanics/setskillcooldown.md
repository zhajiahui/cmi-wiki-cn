---
title: Setskillcooldown
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setskillcooldown
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setskillcooldown {#setskillcooldown}

## 说明 {#description}

将给定元技能的冷却时间设置为给定值（以秒为单位）

> 如果用于设置此机制所在元技能的冷却，元技能执行与此机制之间至少要加入 `0` 的延迟。

> 目标元技能首先需要有一个冷却选项。如果你不希望它有冷却时间，但仍想使用此机制动态设置它，请使用`Cooldown: 0`

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| skill | s | 要设置冷却的[元技能](../metaskills.md) |  |
| seconds | sec, time, t | 冷却持续时间 | 0 |

## 示例 {#examples}

```yaml
  Skills:
  - setSkillCooldown{skill=test_skill;seconds=10} @self
```

> 此示例将施法者的元技能 *test_skill* 的冷却时间设置为 10 秒

##  {#section}

```yaml
ExampleSkill:
  Cooldown: 0
  OnCooldownSkill: ExampleSkill-DisplayCooldown
  Skills:
  - delay 0
  - setSkillCooldown{s=ExampleSkill;seconds=<skill.cooldown>/20} @self
```

> 如果你打算设置调用元技能的冷却时间，如何使用该机制

## 别名 {#aliases}

- skillCooldown
- setskillcd
- skillcd
