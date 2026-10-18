---
title: 占位符
source: https://docs.phoenixdevt.fr/mmoitems/general/placeholders
source_snapshot: '2026-10-19'
---

# 占位符 {#🏷️-placeholders}

所有占位符在插件加载时自动注册，并需要 **PlaceholderAPI** 才能工作。你不需要运行任何命令来初始化占位符。请记住，你可以使用`{placeholderapi_mmoitems_...}`从 MVdWPlaceholderAPI 访问 PAPI占位符。

如果你正在寻找占位符但在这里找不到它，请检查 [**MYTHICLIB占位符**](../../mythiclib/general/placeholders.md)！

### 属性 {#stats}

| **占位符** | **描述** |
| --- | --- |
| `%mmoitems_stat_<stat name>%` | 返回格式化的玩家[属性](../features/stats/stats.md)值 |
| `%mmoitems_stat_<element name>_<damage/damage_percent/weakness/defense/defense-percent>%` | 返回元素属性 |

### 类型 {#types}

| **占位符** | **描述** |
| --- | --- |
| `%mmoitems_type_<item type>_name%` | 返回指定的 [物品类型](../features/types.md)的名称。 |
| `%mmoitems_type_<item type>_total%` | 返回指定 [物品类型](../features/types.md)中物品的总金额。 |

### 耐久度 {#durability}

| **占位符** | **描述** |
| --- | --- |
| `%mmoitems_durability%` | 返回当前物品左侧的耐久度 |
| `%mmoitems_durability_max%` | 返回当前物品的最大值耐久度 |
| `%mmoitems_durability_ratio%` | 以百分比形式返回当前物品的耐久度 |
| `%mmoitems_durability_bar_square%` | 以条形（方块）形式返回当前物品的耐久度 |
| `%mmoitems_durability_bar_diamond%` | 返回当前物品的耐久度作为条形（钻石） |
| `%mmoitems_durability_bar_thin%` | 返回当前物品的耐久度作为条形（细） |

有关自定义耐久度的更多信息，请访问 [此 wiki 页面](../features/custom-durability.md)。

### 杂项 {#misc}

| **占位符** | **描述** |
| --- | --- |
| `%mmoitems_tier_<item tier>%` | 返回给定层的名称 |
| `%mmoitems_ability_cd_<ability name>%` | 返回给定能力的当前冷却时间 |

---

原文：[🏷️ Placeholders](https://docs.phoenixdevt.fr/mmoitems/general/placeholders) · 原文归档：2026-10-19
