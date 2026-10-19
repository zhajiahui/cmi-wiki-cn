---
title: Add Trade
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/AddTrade
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Add Trade {#add-trade}

## 说明 {#description}

更改村民交易。如果使用时村民没有职业，会变成傻子村民。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| action | mode, m | 要执行的操作，可以为 `ADD`、`REMOVE`、`REPLACE`。 | ADD |
| slot | s , index | 执行操作时选择的槽位。槽位从 0 开始，因此村民有 3 项交易时，中间一项交易的槽位是 1。 | 0 |
| ingredient | item, ingredient1, item1, i, i1 | 第一种材料。 | STONE |
| ingredient2 | item2, i2 | 第二种材料。 |  |
| result | r | 交易产出的物品。 | STONE |
| maxUses | uses, u | 交易的使用次数。 | <Max Int> |
| experienceReward | expReward, exp, dropExp | 交易是否掉落经验。 | false |
| villagerExp | villExp, vexp | 成功交易后给予村民的经验值。 | 0 |
| priceMultiplier | multiplier | 玩家激怒村民时使用的价格倍率。 | 0 |
| demand | d | 交易的需求值。 | 1 |
| specialPrice | special | 村民对玩家友好时使用的特殊价格，例如因玩家声望或村庄英雄效果而获得的价格。 | 1 |
| ignoreDiscounts | discounts | 是否忽略折扣。 | false |

## 示例 {#examples}

```yaml
TestVillager:
  Type: Villager
  Display: 'OwO'
  Skills:
  - addTrade{item=DIAMOND 1;item2=EMERALD 2;result=IRON_INGOT 3;expReward=True;villExp=999;multiplier=0} @self ~onDamaged
  - addTrade{action=REPLACE;slot=1;item=DIRT 1;item2=COAL 2;result=DIAMOND_BLOCK 3;expReward=True;villExp=999;multiplier=0} @self ~onSignal:rev
```

## 别名 {#aliases}

- setTrade
- removeTrade
- replaceTrade
