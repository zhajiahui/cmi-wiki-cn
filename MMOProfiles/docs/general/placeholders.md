---
title: 占位符
source: https://docs.phoenixdevt.fr/mmoprofiles/general/placeholders
source_snapshot: '2026-10-19'
---

# 占位符 {#🏷️-placeholders}

全部占位符会在插件加载时自动注册，并依赖 **PlaceholderAPI**。无需额外执行命令或下载其他内容来初始化占位符。

注意：可以通过 MVdWPlaceholderAPI 的 `{placeholderapi_mmoprofiles_...}` 调用这些 PAPI 占位符。

## 主机占位符 {#main-placeholders}

| **占位符** | **描述** |
| --- | --- |
| `%mmoprofiles_real_uuid%` | 玩家的原始 UUID，仅在启用代理端档案时有意义。 |
| `%mmoprofiles_current_profile_uuid%` | 玩家当前档案的 UUID。 |
| `%mmoprofiles_current_profile_name%` | 玩家当前档案的名称。 |
| `%mmoprofiles_current_profile_slot%` | 当前档案对应的栏位编号，为整数。 |
| `%mmoprofiles_amount_profiles%` | 玩家已创建的档案数量。 |
| `%mmoprofiles_profile_slots%` | 玩家最多可创建的档案数量。 |
| `%mmoprofiles_remaining_profile_slots%` | 玩家还可以创建的档案数量。 |
| `%mmoprofiles_profile_name_{slot}%` | 第 {slot} 个栏位中的档案名称。 |

---

原文：[🏷️ Placeholders](https://docs.phoenixdevt.fr/mmoprofiles/general/placeholders) · 原文归档：2026-10-19
