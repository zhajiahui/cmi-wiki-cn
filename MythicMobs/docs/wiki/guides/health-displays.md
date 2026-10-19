---
title: 生命值显示
source_url: https://wiki.mythiccraft.io/mythicmobs/Guides/Health-Displays
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 生命值显示

**难度：入门**

你可能想向正在与生物战斗的玩家显示它的生命值。实现方式有几种，本指南将逐一介绍！

# Boss 血条 {#boss-bars}

可以为生物创建 Boss 血条，像末影龙或凋灵一样显示它的生命值，方法很简单。

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  BossBar:
    Enabled: true
    Title: '&cSkeleton King!'
    Range: 50
    Color: GREEN
    Style: SEGMENTED_12
```

# 名称显示 {#nameplate}

可以在生物头顶的名称中显示生命值，具体方式有很多。这里提供 2 个示例：一个用数字显示生物的生命值（15/20），另一个使用随生命值降低而变化的条形显示。

### 数字 {#number}

需要使用 [SetName](../skills/mechanics/setname.md) 机制和 [~onDamaged](../skills/triggers/ondamaged.md) 触发器。我们会通过生物的 display 选项设置信息，并使用 caster.hp 和 caster.mhp 占位符获取当前生命值和最大生命值。

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King &7(<caster.hp>/<caster.mhp>)'
  Skills:
  - setname{n=<caster.name>;delay=2} @self ~onDamaged
```
