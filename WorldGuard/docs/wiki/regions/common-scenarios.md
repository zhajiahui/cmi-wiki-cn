---
title: 常见场景
source_url: https://worldguard.enginehub.org/en/latest/regions/common-scenarios/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 常见场景 { #common-scenarios }

以下是可能遇到的常见场景，其中部分内容也在其他页面中介绍过。

<a id="contents"></a>

- [常规](#general)



  - [如何允许使用门、拉杆等方块？](#how-do-i-allow-the-usage-of-doors-levers-etc)

  - [如何允许玩家骑马和乘坐矿车？](#how-do-i-let-people-ride-horses-and-minecarts)

  - [如何禁止在野外建造？](#how-do-i-prevent-building-in-the-wilderness)

  - [如何只禁止非成员离开区域？](#how-can-i-only-deny-exit-for-non-members)

  - [如何允许玩家从 exit=deny 区域的某一侧离开？](#how-can-i-let-players-exit-one-side-of-an-exit-deny-region)

  - [如何取消所有附魔台的保护？](#how-do-i-unprotect-all-enchantment-tables)

  - [如何允许挖掘，但禁止放置方块？](#how-do-i-allow-mining-but-prevent-block-placing)

  - [如何允许玩家阅读讲台上的书，但不取走它？](#how-do-i-allow-players-to-read-lectern-books-but-not-take-them)

  - [如何只允许破坏指定类型的方块？](#how-do-i-allow-breaking-of-only-certain-block-types)

- [地块设置](#plot-setups)



  - [如何创建一套地块？](#how-can-i-create-a-setup-with-plots)

  - [如何禁止使用商场公共区域内的门等方块？](#how-do-i-prevent-door-etc-usage-in-public-areas-of-the-mall)

- [问题排查](#problems)



  - [为什么活塞不工作？](#why-don-t-pistons-work)

!!! tip "提示"

    更多常见问题的解决方法，也请参阅[常见问题](../faq.md)页面。

## 常规 { #general }

### 如何允许使用门、拉杆等方块？ { #how-do-i-allow-the-usage-of-doors-levers-etc }

如果希望所有人都能使用门、拉杆、按钮、压力板等方块，请设置 `use` 旗标：

```text
/rg flag REGION_NAME use allow
```

如果希望对**所有**区域应用此设置，请在[全局区域](global-region.md)中设置：

```text
/rg flag __global__ use allow
```

### 如何允许玩家骑马和乘坐矿车？ { #how-do-i-let-people-ride-horses-and-minecarts }

如果希望所有人都能使用全部载具，请设置 `ride` 旗标：

```text
/rg flag REGION_NAME ride allow
```

如果希望对**所有**区域应用此设置，请在[全局区域](global-region.md)中设置：

```text
/rg flag __global__ ride allow
```

!!! warning "警告"

    这样也会允许玩家骑走其他人区域中的马！只有确实希望如此，或有其他防盗马措施时才使用。

### 如何禁止在野外建造？ { #how-do-i-prevent-building-in-the-wilderness }

如[全局区域](global-region.md)页面所述，可以将 `passthrough` 旗标设为 `deny`：

```text
/rg flag __global__ passthrough deny
```

**不要**设置 `build` 旗标。

### 如何只禁止非成员离开区域？ { #how-can-i-only-deny-exit-for-non-members }

`entry` 和 `exit` 默认针对非成员，因此无需设置区域组：

```text
/rg addmember example_region sk89q
/rg flag example_region exit deny
```

### 如何允许玩家从 exit=deny 区域的某一侧离开？ { #how-can-i-let-players-exit-one-side-of-an-exit-deny-region }

创建两个区域：

- 其中一个区域设置 `exit=deny`。

- 另一个区域位于禁止离开区域的边缘，在希望允许离开的那一侧向外延伸一小段，并设置 `exit-overide=true`。

### 如何取消所有附魔台的保护？ { #how-do-i-unprotect-all-enchantment-tables }

在[配置](../config.md)中调整 `interaction-whitelist`，将附魔台加入列表。可用的准确名称见 [Bukkit Material](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)。

### 如何允许挖掘，但禁止放置方块？ { #how-do-i-allow-mining-but-prevent-block-placing }

将 `block-break` 旗标设为 `allow`：

```text
/rg flag mining_area block-break allow
```

### 如何允许玩家阅读讲台上的书，但不取走它？ { #how-do-i-allow-players-to-read-lectern-books-but-not-take-them }

首先确认使用 WorldGuard 7.0.1+。更早的版本发布于 1.14 之前，当时还没有讲台。

- 将 `use` 旗标设为 `allow`：`/rg flag <region> use allow`

### 如何只允许破坏指定类型的方块？ { #how-do-i-allow-breaking-of-only-certain-block-types }

目前尚不支持按区域这样设置。不过，可以按[黑名单](../blacklist.md)所述，通过白名单模式在世界范围内实现，或使用[建造权限](../build-perms.md)。

## 地块设置 { #plot-setups }

### 如何创建一套地块？ { #how-can-i-create-a-setup-with-plots }

要创建地块，需要利用[优先级与继承](priorities.md)中介绍的区域继承。先创建两个区域，再创建各个地块区域。

最终会有以下区域：

- 外层区域（`mall`）

- 可选的“模板”区域，供所有地块区域继承（`shop_template`）

- 各个地块

创建商场区域：

```text
/rg define mall
```

创建商店模板。这里使用 `-g` 创建没有实际空间范围的区域，因为它本身不用于保护任何区域。

```text
/rg define shop_template -g
```

创建一些地块：

```text
/rg define shop1
/rg define shop2
/rg define shop3
```

接下来设置父区域：

```text
/rg setparent shop_template mall
/rg setparent shop1 shop_template
/rg setparent shop2 shop_template
/rg setparent shop3 shop_template
```

!!! hint "提示"

    另一种做法是把商场区域的优先级调低（`/rg setpriority mall -1`）。

### 如何禁止使用商场公共区域内的门等方块？ { #how-do-i-prevent-door-etc-usage-in-public-areas-of-the-mall }

目标如下：

- 在商场中将 `use` 设为 `deny`：`/rg flag mall use deny`

- 由于这也会禁止地块内的使用操作，需要只修改地块内的 `use`

- 有了先前创建的模板区域，就很容易处理：`/rg flag shop_template use allow`

借助继承，地块会继承模板的 `use` 旗标，并覆盖商场中的 `use` 旗标。

## 问题排查 { #problems }

### 为什么活塞不工作？ { #why-don-t-pistons-work }

是否设置了 `build` 旗标？**不应**这样做，请取消它：

```text
/rg flag __global__ build
```

- 如果只是想禁止建造，实际上什么也不用设置！区域创建后，默认就受到保护。

- 如果想禁止在野外建造，可以将 `passthrough` 设为 `deny`：



  ```text
  /rg flag __global__ passthrough deny
  ```

!!! warning "警告"

    如果希望活塞将方块从一个区域推入另一个区域，请确认两个区域属于同一个 [nonplayer-protection-domain](flags.md#flag-overrides)。
