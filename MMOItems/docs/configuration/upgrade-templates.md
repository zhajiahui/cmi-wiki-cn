---
title: upgrade-templates.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: upgrade-templates.yml
source_version: 6.10.1-SNAPSHOT
---

# upgrade-templates.yml

文件：`upgrade-templates.yml`。版本：`6.10.1-SNAPSHOT`。

随包配置。

## `weapon-default` { #weapon-default }

```yaml title="upgrade-templates.yml · weapon-default"
# 模板 ID，仅用作引用。要为特定物品
# 设置升级功能，需要在
# 编辑界面中输入此文本。
weapon-default:

    # 物品每次升级，攻击伤害
    # 提高 3%(相对于当前值)
    attack-damage: 3%
    
    # 每次升级都会增加绝对值 +2% 的
    # 暴击几率(与当前值无关)。
    critical-strike-chance: 2
    
    pve-damage: 1%
```

## `armor-template-example` { #armor-template-example }

```yaml title="upgrade-templates.yml · armor-template-example"
armor-template-example:
    armor: 3%
    armor-toughness: 2%
    block-rating: 5%
    dodge-rating: 5%
    parry-rating: 5%
```
