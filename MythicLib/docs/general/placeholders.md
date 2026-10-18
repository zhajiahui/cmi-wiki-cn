---
title: 占位符
source: https://docs.phoenixdevt.fr/mythiclib/general/placeholders
source_snapshot: '2026-10-19'
---

# 占位符 {#🏷️-placeholders}

这些是占位符，你可以在MMOItems和MMOCore中使用。

| **占位符** | **描述** |
| --- | --- |
| `%mythiclib_stat_<stat_name>%` | 玩家属性的当前值。 |
| `%mythiclib_raw_stat_<stat_name>%` | 玩家属性的当前值（不进行舍入）。 |
| `%mythiclib_cooldown_<cooldown_key>%` | 这个占位符处理冷却时间的许多事情，包括来自MMOCore/MMOItems的技能、 MI物品、缓解机制等。请参阅可用的冷却时间密钥列表[此处为](../scripts/variables.md#cooldownmap)。 |
| `%mythiclib_defense_damage_reduction%` | 当造成100伤害时，防御会减轻伤害。 |
| `%mythiclib_space_<number>%` | 使用[负空间字体资源包](https://www.spigotmc.org/threads/negative-space-font-resource-pack.440952/)]的正(`10`)/负(`-10`)空间。 |

仅当使用 [built-in魔力/耐力模块](../misc/mana-stamina.md#placeholders)时，一些附加的占位符才可用。

---

原文：[🏷️ Placeholders](https://docs.phoenixdevt.fr/mythiclib/general/placeholders) · 原文归档：2026-10-19
