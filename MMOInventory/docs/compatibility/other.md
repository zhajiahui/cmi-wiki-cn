---
title: 其他插件
source: https://docs.phoenixdevt.fr/mmoinventory/compatibility/other
source_snapshot: '2026-10-19'
---

# 其他插件 {#🔌-other-plugins}

MMOInventory具有对其他物品插件的本机支持。它可以从其他插件（如 *LoreAttributesRecoded*、*Oraxen* 或 *Nexo*）检测特定的物品，但**仅通过检测其中的特定模式来使用物品描述**。例如，如果你的 Sword物品的物品描述中都有`&cSword`，则MMOInventory能够检测到它，从而对这些物品应用插槽限制。

这具有创建“虚构的物品类型”的效果，这些类型不是像MMOItems那样的真实物品类型，但仍然是共享一个属性（特定的描述模式）的物品类别。

`loretag{tag="&cRing"}`将仅接受物品，其描述行与`&cRing`完全匹配。此插槽限制完全支持基本颜色代码。`loretag{tag="&cSword";check=EQUALS}`将具有完全相同的行为。以下物品匹配槽限制，因为它有一个描述行与`&cRing`完全匹配。

![图片](../assets/de4cc07b8683-item1.D7tECfWH.png)

`loretag{tag="&cRing";check=CONTAINS}`将接受物品，其描述行包含`&cRing`。以下物品匹配插槽限制，即使`&cRing`出现的行还包含其他文本。

![图片](../assets/aab2dca7bd87-item2.CyapwR1H.png)

其他可能的检查是`STARTS_WITH`和`ENDS_WITH`，它们检查物品描述行中是否有任何以给定字符串开头/结尾。

---

原文：[🔌 Other Plugins](https://docs.phoenixdevt.fr/mmoinventory/compatibility/other) · 原文归档：2026-10-19
