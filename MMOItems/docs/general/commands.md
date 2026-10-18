---
title: 命令
source: https://docs.phoenixdevt.fr/mmoitems/general/commands
source_snapshot: '2026-10-19'
---

# 命令 {#💾-commands}

## 物品命令 {#item-commands}

|命令 |用途 |
| --- | --- |
| `/mmoitems create <type> <id>` | 使用指定的物品类型和物品ID创建新的物品。ID不是显示名称。 |
| `/mi copy <type> <current-id> <new-id>` | 将你持有的物品复制到具有不同ID的新物品中。如果批量生产很有用。 |
| `/mi delete <type> <id>` | 删除指定的物品。 |
| `/mi edit <type> <id>` | 打开物品编辑器。 |
| `/updateitem` | 更新你持有的物品。 |
| `/updateitem <type> <id>` | 打开特定物品的自动 [物品更新程序](../items/revision-id.md)。不完全建议始终保持此状态，因为如果你有足够的更新，则始终更新物品最终可能会导致延迟。 |
| `/mi drop <type> <item-id> <world> <x> <y> <x>` | 生成并掉落（本质上是在物品中生成，而不将其放入玩家物品栏中）。 |
| `/mi item identify` | 手动识别你所持有的物品。 |
| `/mi item repair` | 手动修复你持有的物品。 |
| `/mi item unidentify` | 手动取消识别你所持有的物品。 |
| `/mi item deconstruct` | 手动解构你持有的物品。 |
| `/mi give <type> <item> (player) (min-max) (unident-chance) (drop-chance) (soulbound-chance) (silent)` | 将物品赋予玩家 |

## 物品管理 {#item-management}

| Command | 用途 |
| --- | --- |
| `/mi browse` | 提取我们创建的所有物品的可交互库，按物品类型排序。 （推荐用于大多数物品创作！） |
| `/mi itemlist <type>` | 列出特定物品类型的所有物品。 |
| `/mi allitems` | 列出所有已创建物品，但不如 /mi browse 方便。 |
| `/mi giveall <type> <item> <min-max> <unident-chance>` | 为所有在线玩家提供物品。 |

## 合成站 {#crafting-stations}

| Command | 用途 |
| --- | --- |
| `/mi stations list` | 列出所有当前的合成站。 |
| `/mi stations open <station> (player)` | 这将为指定的玩家打开指定的站。这是将站绑定到块的命令。 |

## 其他功能 {#miscellaneous}

| Command | 用途 |
| --- | --- |
| `/mi ability <ability> (player) (mod1) (val1) (mod2) (val2)` | 施放MMOItems能力（也可与 MM技能配合使用）。存在选择该能力、施放该能力的玩家以及修改伤害和冷却时间等值的参数。 |
| `/mi heal` | 与精华/CMI 治疗类似，这可以治愈你并消除所有负面影响。 |
| `/mi debug info (player)` | 打开一个有用的聊天菜单，其中包含有关玩家的信息。这包括属性，如职业和魔力（如果适用）。 |
| `/mi list (type/spirit/ability)` | 显示武器、员工精神、实体等的所有可用类型。 |

## 基本设置 {#general}

| Command | 用途 |
| --- | --- |
| `/mmoitems reload` | 编辑配置文件后重新加载整个插件。无需重新启动服务器！ |
| `/mi reload (adv-recipes/stations)` | 重新加载插件或重新加载高级配方/合成站（如果适用）。 |

## 物品一代 {#item-generation}

| Command | 用途 |
| --- | --- |
| `/mi generate <player> (extra-args)` | 检查[获取物品](../items/obtain-item.md)了解更多信息 |

---

原文：[💾 Commands](https://docs.phoenixdevt.fr/mmoitems/general/commands) · 原文归档：2026-10-19
