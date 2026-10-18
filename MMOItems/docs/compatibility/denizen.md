---
title: Denizen
source: https://docs.phoenixdevt.fr/mmoitems/compatibility/denizen
source_snapshot: '2026-10-19'
---

# Denizen {#📝-denizen}

> **警告**
>
> 此功能是实验性的，不再可用。

## 获取 MI物品 {#getting-a-mi-item}

首先，你必须使用`<mmoitem_template[type=SWORD>;id=KATANA]>`检索物品模板，该模板返回 MMOItemTemplateTag。然后，你必须使用`<templateTag.generate[]>`子标签生成物品。

以下示例将生成具有随机等级和层的物品。如果你没有指定任何层，它将根据你在设置层时选择的机会随机选择[物品生成器选项](../features/tiers.md#modifier-capacity-item-generation)。

`<mmoitemTemplateTag.generate[]>`

以下示例将生成具有特定等级和层的物品。

`<mmoitemTemplateTag.generate[level=10;tier=RARE]>`

以下示例将生成物品，其等级将随目标玩家的等级缩放。目标玩家是一个 PlayerTag，必须在标签上下文中传递。如果你不指定物品等级，则MMOItems将采用完全随机的等级，除非你启用`match-level`选项。

`<mmoitemTemplateTag.generate[player=SomePlayerTag;match-level=TRUE]>`

## ItemTags 的新属性 {#new-properties-for-itemtags}

使用以下标签，你可以检查物品是否是 MMOItem

`<itemTag.is_mmoitem>`

使用以下标签，你可以检查物品是否未识别

`<itemTag.is_unidentified>`

使用以下标签，你可以在确保其未识别后生成物品的已识别版本

`<itemTag.identify>`

在下面的示例中，我们检查基本铁剑是否是 MMOItem，因此将始终返回false。

`<item[DIAMOND_SWORD].is_mmoitem>`

---

原文：[📝 Denizen](https://docs.phoenixdevt.fr/mmoitems/compatibility/denizen) · 原文归档：2026-10-19
