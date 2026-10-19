---
title: "无法在聊天中输入和无法移动"
source_url: "https://wiki.itemsadder.com/faq/cant-write-in-chat-and-cant-move"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 无法在聊天中输入和无法移动

## Worldguard

如果你遇到车辆卡住（被卡在地下等奇怪的 bug），请打开 WorldGuard 的 config.yml 文件并设置以下内容：

```yaml
block-plugin-spawning: false
```

## Towny

如果载具出现问题，并且你使用 Towny 插件，请打开 Towny 的 `config.yml`，并从此处移除 Slime：

```yaml
town_mob_removal_entities: Monster,Flying,Shulker,SkeletonHorse,ZombieHorse
```

## Mob Farm Manager

如果你拥有[Mob Farm Manager](https://www.spigotmc.org/resources/mob-farm-manager-supports-1-7-10-up-to-1-16-hopper-support.15127/)插件，请确保检查是否设置了任何实体类型**`SLIME`**规则，这可能会移除作为车辆一部分的史莱姆并导致此 bug。

## Residence

在**Residence**中使用命令`/res set monsters t/r`。\
我已经联系了 Residence 开发者，希望[他们会修复这个问题](https://github.com/Zrips/Residence/issues/469#issuecomment-801425643)

## 其他生物移除/分组/合并插件

请移除任何关于实体类型**`SLIME`**的分组/合并/移除功能。
