---
title: triggers.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: triggers.yml
source_version: 1.7.1-SNAPSHOT
---

# triggers.yml

文件：`triggers.yml`。版本：`1.7.1-SNAPSHOT`。

随包配置。

## `WEAPON_CRIT` { #weapon_crit }

```yaml title="triggers.yml · WEAPON_CRIT"
######################################
#
# 自定义触发器
#
# 可以在 MythicLib 中实现自定义技能触发器，
# 不过此功能较为复杂。在此文件中注册后，
# 需要使用一个技能机制手动调用此触发器。
#
# 之后即可在 MMOLib 脚本中调用自定义触发器，
# 进一步自定义技能和脚本。
#
# 更多信息见此 Wiki 页面：
# https://docs.phoenixdevt.fr/mythiclib/skills/triggers.html#custom-triggers
#
######################################


# 武器暴击时触发
# 对应的命中效果：on_hit_effects/weapon_crits
# 在脚本中调用：              script/on_hit_effects.yml>weapon_crit_script
WEAPON_CRIT:

  # 设为 false 时，如果技能因冷却中、
  # 魔力或耐力不足等原因
  # 无法施放，会向玩家发送消息。
  silent: true
```
