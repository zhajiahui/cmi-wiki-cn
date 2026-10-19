---
title: Items/lottery_box.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: Items/lottery_box.yml
source_version: 1.22.0
---

# Items/lottery_box.yml

文件：`Items/lottery_box.yml`。版本：`1.22.0`。

随包物品或内容配置。

## `TARGET` { #target }

```yaml title="Items/lottery_box.yml · TARGET"
# 物品 ID 为 TARGET；修改 ID 时请同步修改 ItemActions 文件的顶级键。
TARGET:
  material: ENDER_CHEST
  name: '&6&l矿物抽奖箱'
  lore:
    - '&7每箱随机获得以下奖励之一：'
    - '&b钻石 &7/ &6金锭 &7/ &f铁锭'
    - '&7三种奖励等概率，每次获得 &e1 &7个。'
    - ''
    - '&e背包内右键 &7开启 &a1 &7个'
    - '&eShift + 右键 &7开启 &a16 &7个'
    - '&7批量开启需要同一格内至少有 &e16 &7个。'
```
