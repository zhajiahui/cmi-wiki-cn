---
title: 物品分解（Scavenge.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/Scavenge.yml
---

# 物品分解（Scavenge.yml）

文件：`plugins/CMI/Settings/Scavenge.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `Scavenge`

### `Scavenge.ItemBreak.Base`

分解时物品损坏的概率<br>
取值为 0 到 100，100 表示每次提取附魔都会损坏物品<br>
可让玩家提取附魔时不破坏物品本身<br>
设为 100，每次都损坏物品<br>
物品损坏后，仍会进入材料返还流程<br>
注意！没有附魔的物品，损坏概率为 100%

### `Scavenge.ItemBreak.ForEachEnchant`

根据附魔数量，额外增加物品损坏概率<br>
例如基础概率 8%，此项为 2，物品有 3 个附魔，则损坏概率为 8+(2\*3)=14%

### `Scavenge.ItemBreak.ForEachEnchantLevel`

根据附魔等级，额外增加物品损坏概率<br>
按附魔当前等级与最高等级的比例计算<br>
例如设为 7.5，满级附魔额外增加 7.5% 损坏概率<br>
锋利 2 的最高等级为 5，此时只增加 3% 失败概率

### `Scavenge.ItemBreak.MaxBreakChance`

提取附魔时，物品损坏概率的百分比上限<br>
避免总概率达到 100% 后，每次都损坏物品

### `Scavenge.ItemBreak.BreakDurabilityCheck`

物品未满耐久度时，额外增加的失败概率，范围为 0 到 100<br>
设为 50，物品只剩 1 点耐久度时，失败概率增加 50%<br>
未损坏的物品不会增加失败概率

### `Scavenge.ItemBreak.DurabilityCheck`

设为 true，提取材料时考虑物品耐久度<br>
例如最大耐久度 100、当前 50，只将一半材料纳入提取<br>
不代表一定返还 50% 材料，而是只有一半材料会进入 IngredientReturn 返还流程

### `Scavenge.ItemBreak.IngredientReturn.Base`

提取失败时，返还物品材料的最大概率，单位为百分比<br>
分别对每一份材料进行判断<br>
数据库中必须存在对应合成配方，否则不返还材料

### `Scavenge.EnchantExtractionFail.Base`

提取附魔失败的基础概率<br>
失败时，玩家不会获得对应附魔书

### `Scavenge.EnchantExtractionFail.ForEachLevel`

根据附魔等级，额外增加提取失败概率<br>
按附魔当前等级与最高等级的比例计算<br>
例如设为 75，满级附魔有 75% 概率提取失败<br>
锋利 2 的最高等级为 5，此时只应用 30% 失败概率<br>
水下速掘等只有 1 级的附魔，始终使用最高失败概率

### `Scavenge.EnchantExtractionFail.MaxFailChance`

提取附魔失败的最大概率，单位为百分比<br>
避免总概率达到 100% 后，每次都失败

### `Scavenge.EnchantExtractionFail.LevelLower.Base`

提取失败后降低附魔等级的概率<br>
这是提取失败后的第二步，仅在失败时发生<br>
附魔已经为 1 级时，不会获得附魔书<br>
若想避免提取失败时降低附魔等级，设为 100<br>
若想每次提取都降低附魔等级，将 EnchantExtractionFail.Base 和此项都设为 100

### `Scavenge.EnchantExtractionFail.LevelLower.ForEachLevel`

按附魔等级调整降级概率，满级时达到指定最大值<br>
附魔等级越高，被降级的概率越高

### `Scavenge.EnchantExtractionFail.LevelLower.MaxChance`

按附魔等级调整降级概率，满级时达到指定最大值

### `Scavenge.Cost.Base`

提取基础费用，设为 0 免费

### `Scavenge.Cost.Extra`

根据附魔价值追加费用，价值可通过 /cmi setenchantworth 设置<br>
此值为各项附魔及物品价值的百分比<br>
例如基础费用为 100、附加费用为 5%，提取价值 1000 的锋利 5，物品 sell hand 价值为 100，则总费用为 155

### `Scavenge.WithoutIngredients`

启用后，允许分解没有有效材料返还配方的物品<br>
仅在还能返还附魔时允许，否则仍禁止分解

### `Scavenge.BlackList`

禁止分解的材质列表

### `Scavenge.BlackToWhiteList`

设为 true，黑名单改为白名单，只允许分解列表中的物品

### `Scavenge.AllowItemPickups`

设为 false，玩家打开分解界面时不能拾取地面物品

### `Scavenge.ResetRepairCost`

启用后，剑等物品在分解后未损坏时，重置其铁砧修复费用，使其可像新物品一样继续附魔，避免费用过高
