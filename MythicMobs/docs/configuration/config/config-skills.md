---
title: config/config-skills.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config/config-skills.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# config/config-skills.yml

文件：`config/config-skills.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包配置。

## `Configuration` { #configuration }

```yaml title="config/config-skills.yml · Configuration"
#
# 技能配置选项
#
# 关于 Mythic 技能功能的更多说明：
# https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/Skills/Skills
#
Configuration:

  #================================================================================
  # 通用技能选项
  #================================================================================

  # 此处暂无内容！

  #================================================================================
  # 目标选择器选项
  #================================================================================
  Targeters:

    # 实体目标过滤器的默认值
    DefaultEntityFilters:
      TargetSelf: false
      TargetPlayers: true
      TargetArmorStands: false
      TargetMarkers: false
      TargetCreativeMode: true
      TargetSpectatorMode: true
      TargetCitizensNPCs: false
      TargetAnimals: true
      TargetCreatures: true
      TargetMonsters: true
      TargetWaterMobs: true
      TargetFlyingMobs: true
      TargetSameFaction: true
      TargetOwner: true
      TargetNonMythic: true
      TargetVillagers: true
```
