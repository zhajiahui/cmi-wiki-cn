---
title: 占位符
source: https://docs.phoenixdevt.fr/mmocore/general/placeholders
source_snapshot: '2026-10-19'
---

# 占位符 {#🏷️-placeholders}

所有占位符在插件加载时自动注册，并需要 **PlaceholderAPI** 才能工作。你不需要运行任何命令来初始化占位符。请记住，你可以使用`{placeholderapi_mmocore_...}`从 MVdWPlaceholderAPI 访问 PAPI占位符。

如果你正在寻找占位符并且在这里看不到它，请记住MythicLib还附带其自己的一组 [PAPI占位符](../../mythiclib/general/placeholders.md)。

### 主机占位符 {#main-placeholders}

| **占位符** | **描述** |
| --- | --- |
| `%mmocore_attribute_<attribute>%` | [玩家基础属性](../features/attributes.md)的当前值。 |
| `%mmocore_<health/mana/stamina/stellium>%` | 格式良好的当前资源值 |
| `%mmocore_<health/mana/stamina/stellium>_bar%` | 将当前资源值格式化为 BAR！ |
| `%mmocore_max_health%` | `%mythiclib_stat_max_mana%`格式良好的简写 |
| `%mmocore_stat_<stat_name>%` | 返回格式化的玩家[属性](../features/stats.md)值 |

### 积分 {#points}

| **占位符** | **描述** |
| --- | --- |
| `%mmocore_skill_points%` | 更多信息请参阅[技能点](../skills/intro.md#upgrading-a-skill)。 |
| `%mmocore_class_points%` | 更多信息请参阅[职业点](../features/classes.md#class-points)。 |
| `%mmocore_attribute_points%` | 更多信息请参阅[基础属性点](../features/attributes.md)。 |
| `%mmocore_attribute_reallocation_points%` | 更多信息请参阅[基础属性点](../features/attributes.md)。 |
| `%mmocore_attribute_points_spent_<attribute_id>%` | 花在特定基础属性上的积分。 |
| `%mmocore_skill_tree_points_<tree>%` | 未使用的技能树点，用于特定的树。使用`global`获取全球技能树积分。 |

### 职业&副职业 {#class-professions}

| **占位符** | **描述** |
| --- | --- |
| `%mmocore_level%` | 主打RPG玩家等级。 |
| `%mmocore_level_percent%` | 进展到下一个等级（%）。 |
| `%mmocore_experience%` | 返回玩家经验。 |
| `%mmocore_next_level%` | 返回下一等级所需的玩家经验。与%mmocore_experience%一起使用效果很好。 |
| `%mmocore_profession_<profession>%` | [副职业](../profession/intro.md)玩家等级。 |
| `%mmocore_profession_experience_<profession>%` | 返回特定副职业的玩家经验。 |
| `%mmocore_profession_next_level_<profession>%` | 返回特定副职业的下一个等级所需的玩家经验。 |
| `%mmocore_profession_percent_<profession>%` | 当前进展到下一个副职业等级（百分比）。 |
| `%mmocore_class%` | 玩家职业名称，或默认名称职业。 |
| `%mmocore_class_id%` | 当前玩家职业的内部名称/ID |
| `%mmocore_mana_icon%` | 魔力图标为玩家当前职业 |
| `%mmocore_mana_name%` | 魔力名称为玩家当前职业 |
| `%mmocore_exp_multiplier_<profession>%` | 返回特定副职业的经验乘数（“main”可以替换副职业名称） |
| `%mmocore_exp_boost_<profession>%` | 返回助推器为特定副职业提供了多少经验乘数（“main”可以替换副职业名称） |

### 任务与目标 {#quests-objectives}

| **占位符** | **描述** |
| --- | --- |
| `%mmocore_quest%` | 正在进行中 [任务](../features/quests.md)，或“无”。 |
| `%mmocore_quest_progress%` | 当前任务的进度，如果没有任务则显示“0”。 |
| `%mmocore_quest_objective%` | 当前的任务目标，如果没有任务则为“无”。 |

### 社交 {#social}

| **占位符** | **描述** |
| --- | --- |
| `%mmocore_guild_name%` | 返回公会名称，如果没有则返回 '' |
| `%mmocore_guild_tag%` | 返回公会标签，如果没有则返回 '' |
| `%mmocore_guild_leader%` | 返回公会领导者或 '' 如果没有 |
| `%mmocore_guild_members%` | 返回公会成员，如果没有则返回 '' |
| `%mmocore_guild_online_members%` | 返回公会在线成员，如果没有则返回 '' |
| `%mmocore_party_count%` | 统计党员人数。 |
| `%mmocore_party_member_<n>%` | n-th党员姓名，若无效则为`None` |
| `%mmocore_online_friends%` | 目前在线好友数 |
| `%mmocore_online_friend_<n>%` | n-th网友姓名，如果无效则为`None` |

### 技能 {#skills}

| **占位符** | **描述** |
| --- | --- |
| `%mmocore_skill_level_<skill_name>%` | 返回玩家对于特定技能的等级。 |
| `%mmocore_skill_parameter_<param_id>:<skill_id>%` | 返回技能参数的值，例如你可以使用`mana`或`cooldown`作为参数。 |
| `%mmocore_bound_skill_parameter_<param_id>:<slot_number>%` | 返回绑定到给定编号插槽的技能参数的技能参数值。 |
| `%mmocore_bound_<slot_idx>%` | 绑定到给定技能插槽的技能的名称。 |
| `%mmocore_id_bound_<slot_idx>%` | 技能的UPPERCASE_ID绑定到给定的技能插槽。 |
| `%mmocore_cooldown_bound_<slot_idx>%` | 返回特定技能槽位中技能的剩余冷却时间时间。 |
| `%mmocore_is_casting%` | 如果玩家处于强制转换模式，则返回`true`，否则返回`false` |
| `%mmocore_passive_bound_<slot_idx>%` | (true/false) 被动技能是否绑定到给定插槽？ |
| `%mmocore_cast_slot_offset_<slot_idx>%` | 仅当使用 *技能杆 *技能铸件时。返回玩家需要按下的按键绑定，以便将技能投射到n-th插槽上 |

### 战斗 {#combat}

| **占位符** | **描述** |
| --- | --- |
| `%mmocore_in_combat%` | 如果玩家处于战斗状态，则返回`true`，否则返回`false` |
| `%mmocore_pvp_mode%` | 如果玩家已启用 PVP 模式，则为 True，否则为false |
| `%mmocore_since_last_hit%` | 返回自上次战斗命中以来的时间（以秒为单位）（如果不在战斗中，则返回-1）。自MMOCore1.11.2快照起 |
| `%mmocore_since_enter_combat%` | 返回自第一次战斗命中以来的时间（以秒为单位）（如果不在战斗中，则返回-1）。自MMOCore1.11.2快照起 |
| `%mmocore_invulnerability_left%` | 受到攻击之前剩余的时间（更改区域/使用 PvpMode 命令时） |
| `%mmocore_combat_left%` | 如果玩家不战斗，离开战斗前还剩时间 |
| `%mythiclib_cooldown_pvpmode%` | `/pvpmode` 的冷却时间 |

---

原文：[🏷️ Placeholders](https://docs.phoenixdevt.fr/mmocore/general/placeholders) · 原文归档：2026-10-19
