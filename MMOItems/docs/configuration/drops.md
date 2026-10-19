---
title: drops.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: drops.yml
source_version: 6.10.1-SNAPSHOT
---

# drops.yml

文件：`drops.yml`。版本：`6.10.1-SNAPSHOT`。

随包配置。

## `blocks` { #blocks }

```yaml title="drops.yml · blocks"
# 可为每种怪物、方块或 MythicMobs 生物
# 创建任意数量的子表。
# 
# 'coef' 是子表的权重。如果一个子表的 coef=1，
# 另一个子表的 coef=3，那么第一个子表被选中的概率为 1(它的权重)
# 除以 4(所有子表权重之和)。
# 权重越高，子表被选中的概率越高。
#
# 读取掉落表时，会从所有子表中
# 随机选择一个，然后读取该子表的物品。
#
# 子表的名称不影响作用，只需保证同一掉落表中的
# 每个子表名称各不相同。
#
# 子表物品格式：[chance to drop],[min amount]-[max amount],[unidentification chance]
#                    或 [chance to drop],[amount],[unidentification chance]
# '50,1-3,10' 表示：
#       - 50% 的掉落概率
#       - 掉落 1 到 3 个物品
#       - 10% 概率处于未鉴定状态 (每件物品)

# 方块掉落表
# 玩家挖掘或破坏方块时读取。
blocks:
    DIAMOND_ORE:
        rare-diamond:
            coef: 1
            disable-silk-touch: true
            items:
                MATERIAL:
                    RARE_DIAMOND: 100,2-3,0
```

## `customblocks` { #customblocks }

```yaml title="drops.yml · customblocks"
# 自定义方块掉落表
# 玩家挖掘或破坏自定义方块时读取。
customblocks:
    1:
        more-rare-diamond:
            coef: 1
            disable-silk-touch: true
            items:
                MATERIAL:
                    RARE_DIAMOND: 100,2-3,0
```

## `monsters` { #monsters }

```yaml title="drops.yml · monsters"
# 怪物掉落表
# 任何怪物死亡时读取。
monsters:
    BLAZE:
        fire-essence-table:
            coef: 1
            items:
                MATERIAL:
                    fire-essence: 7,1-2,0
    ZOMBIE:
        rock-table:
            coef: 7
            items:
                CONSUMABLE:
                    ROCK: 50,1-3,10
        coin-table:
            coef: 1
            items:
                MISCELLANEOUS:
                    GOLD_COIN: 1,1-10,0
```
