---
title: 自定义头颅（CustomHeads.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/CustomHeads.yml
---

# 自定义头颅（CustomHeads.yml）

文件：`plugins/CMI/Settings/CustomHeads.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `LootMobBonus`

启用后，使用带抢夺附魔的工具时，提高生物头颅掉落概率<br>
数值为百分比，按当前掉落概率计算额外增幅<br>
例如基础概率 1%，抢夺 3 提供 30% 加成，最终为 1.3%，这是默认值<br>
仅影响怪物头颅<br>
可复制条目添加任意等级，例如

```text
Lvl33: 35.5
```

## `useDefaultHeadLore`

是否使用默认头颅描述，用于未单独设置描述的头颅

## `defaultHeadLore`

头颅未设置描述时使用的默认描述

## `PlayerHead`

### `PlayerHead.UseLore`

是否使用玩家头颅描述

### `PlayerHead.Lore`

玩家头颅掉落时使用的描述<br>
可用全局变量，便于标识死者与击杀者<br>
也支持占位符；需要玩家对象的占位符会以死者为解析对象

## `HeadHandling`

### `HeadHandling.Maintain.Name`

头颅放置后再破坏时，是否保留自定义名称<br>
原版在放置头颅时会丢弃自定义信息，此项可帮助保留数据

## `Player`

### `Player.Percentage`

头颅掉落概率，范围为 0 到 100，可填 0.2 等小数<br>
100 表示每次玩家击杀其他玩家时都会掉头颅<br>
1 表示玩家被另一名玩家击杀时，有 1% 概率掉头颅

### `Player.LowerChanceAfterDrop`

再次获得同一玩家头颅时，降低掉落概率的百分比，范围为 0 到 100<br>
每次服务器重启后重置

### `Player.LootBonus`

启用后，使用带抢夺附魔的工具时，提高玩家头颅掉落概率<br>
数值为百分比，按当前掉落概率计算额外增幅<br>
例如基础概率 1%，抢夺 3 提供 30% 加成，最终为 1.3%，这是默认值<br>
仅影响玩家头颅<br>
可复制条目添加任意等级，例如

```text
Lvl33: 35.5
```

### `Player.Worlds`

允许掉落玩家头颅的世界，留空包含全部世界

## `Mob`

### `Mob.Drop`

允许生物按指定概率掉落自定义头颅<br>
按实体类型的详细设置见 CustomHeads.yml

### `Mob.Worlds`

允许掉落生物头颅的世界，留空包含全部世界

## `EntityHeads`

各实体的自定义头颅<br>
可添加任意数量的自定义头颅<br>
格式为 \[dropChance\]:\[texture\]<br>
此处概率仅针对这一种头颅<br>
每种实体类型另有独立的全局掉落概率<br>
强烈建议至少有一种头颅的概率为 100%，否则即使触发了实体的掉落，也可能没有头颅产出<br>
可在网上查找自定义贴图<br>
同一实体有多种可用头颅时，随机选择<br>
自定义头颅格式：\[chance\]:\[HeadName\]:c-\[options\]:lore{"\[lore\]"}:\[texture\]<br>
详细说明和示例见 www.zrips.net/cmi/extra/custom-mob-heads/<br>
可省略贴图字符串开头的 eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUv；缺失时会自动补上
