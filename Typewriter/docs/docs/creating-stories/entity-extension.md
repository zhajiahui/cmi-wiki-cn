---
title: 实体与 NPC（Entities & NPC's）
source: https://docs.typewritermc.com/docs/creating-stories/entity-extension
source_version: 0.8.0
---

# 实体与 NPC（Entities & NPC's）

**扩展**

在开始本教程之前，你必须安装 Entity、RoadNetwork 和 Quest Extensions。

任何好的故事讲述都需要其他角色出现在世界上。
Typewriter有自己的实体扩展，允许你创建和控制 NPC 等实体。

## Entity Extension 是什么？ {#what-is-the-entity-extension}

实体扩展是一项功能，可以轻松生成、管理和控制服务器上的 NPC 等实体。

以下是一些功能：

- **定义实体**：使用自定义数据创建一个新实体并在世界中生成它，该实体可以在多个服务器上重复使用
- **有条件地显示实体**：只有当玩家处于某个任务阶段时才会出现 NPC
- **活动**：向实体添加自定义操作，例如晚上步行到小酒馆或在城市巡逻

## 创建 NPC {#creating-an-npc}

Typewriter中的实体必须定义在`Manifest`页面中。
这是通过创建你要使用的实体类型的新定义来完成的。
该定义可以使用实体实例多次生成。

**NPC**是一种特殊类型的实体，它是玩家，头顶上有一个名牌和指示器。
这使得它易于使用，并且可能是你将使用的最常见的实体类型。

### 新建 NPC 定义 {#creating-a-new-npc-definition}

要创建 NPC 定义，你必须创建呈现页面并在其中定义 NPC。以下是如何定义 NPC 的示例：

首先单击**添加页面**。
在这里，在下拉菜单中选择**呈现**类型，并将页面命名为你想要的名称。
在此示例中，我们将其命名为`Characters`。

如果你需要有关如何创建页面的更多信息，请参阅[界面布局](../getting-started/layout.md)部分。

接下来，你必须定义 NPC。点击`Add Entry`按钮或右上角的`+`，
然后搜索`Add NPC Definition`，并将其添加到页面中。你现在应该在屏幕上看到该条目。

添加NPC定义

简化的预制 npc

+

# 自定义实体

现在你已经定义了实体，你可以根据自己的喜好对其进行自定义。

## 设置实体名称 {#setting-the-entitys-name}

我们将该条目重命名为`Oliver Definition`。

要更改头部上方的显示名称，我们可以将`Display Name`字段更改为`<red><b>Oliver</b></red>`。

![重命名条目和实体](../../assets/2317b98c5b8f-entity_name_change.e412283.432.avif)

## 设置 NPC 皮肤 {#setting-the-npcs-skin}

要改变NPC的皮肤，我们可以改变`Skin`字段。
这些具有纹理和签名。
这些需要由Minecraft生成，并且不易编辑。
幸运的是，Typewriter提供了一种从玩家 uuid 或 url 生成这些内容的方法。

将 Oliver 的皮肤换成 [NameMC](../../assets/c9c214f0f86a-b2319359e305d7a2.png) 上的这一款。
点击 `Skin` 字段右侧的链条图标，选择 `Fetch from url`。

然后，我们可以输入 url`https://s.namemc.com/i/b2319359e305d7a2.png`并单击`Fetch`。

<video controls preload="metadata" src="../../assets/65e606d1fbb7-fetch_skin.webm"></video>

## 创建 NPC 实例 {#creating-an-npc-instance}

我们现在已经定义了 NPC，但它还没有在世界中生成。
要生成实体，我们必须添加`Entity Instance`条目。
每种类型的实体都有不同的`Entity Instance`定义。
对于 NPC，我们可以使用`NPC Instance`定义。

添加 Npc 实例

简化的预制 npc 实例

+

首先，从`Definition`下拉列表中选择要生成的 NPC 定义。
在本例中，我们将选择我们刚刚创建的`Oliver Definition`。
这将作为我们的 NPC 实例的基础

![定义 选择](../../assets/a1aa0c062e1a-definition_select.d48ad0b.431.avif)

最后，我们需要设置 NPC 的生成位置。
第一位玩家开始看到 NPC 时，NPC 总会出现在这个位置。

我们可以使用内容模式选择器来执行此操作，并获取你登录的Minecraft客户端的位置。

<video controls preload="metadata" src="../../assets/e090ae60fe6d-entity_location.webm"></video>

就是这样！
你现在已经创建了一个实体定义并在世界中生成了它的一个实例。
你现在可以在游戏中看到带有你提供的自定义名称、皮肤和数据的 NPC！

同样的原则适用于所有其他实体，例如**奶牛**或**村民**。
你可以使用实体扩展来定义和生成任何你想要的实体；只需确保你的定义类型与你想要生成的实例类型相匹配。

**说明**

由于并非所有实体都有定义或实例，因此当你需要创建没有定义或实例的类型的实体时，请从[Discord](https://discord.gg/HtbKyuDDBw)请求它。

---

原文：[Entities & NPC's](https://docs.typewritermc.com/docs/creating-stories/entity-extension) · 文档版本：0.8.0
