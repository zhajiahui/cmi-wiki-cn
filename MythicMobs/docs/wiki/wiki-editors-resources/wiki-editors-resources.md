---
title: Wiki 编辑资料
source_url: https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/Wiki-Editors-Resources
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Wiki 编辑资料

# Wiki 编辑者资源 {#wiki-editors-resources}

本页较完整地汇总了编写各个 Wiki 页面时使用的当前语法。如果某种情况尚未记录，请询问应该采用什么语法。

每个页面的 Markdown 源码中还有以注释形式写下的进一步说明，可以通过“编辑”页面查看。

## 通用规则 {#general-rules}

- 各个“章节”（以 `## title` 定义）之间应始终保留两个换行符，即按两次 Enter。
- 使用超链接时，请注意相对路径以 `/wiki/` 为起点。例如，可以写成 `[ExampleMechanic](Wiki-Editors-Resources/ExampleMechanic)`。如果引用的资源就在 Wiki 内，请使用这种写法。

## 嵌入数据 {#embedded-data}

Wiki 中有一些以 HTML 注释形式嵌入的数据，用于生成 Wiki 数据集。编辑这些数据时务必谨慎

### 属性数据 {#attribute-data}

这些数据添加在各个属性的默认值字段中。可嵌入两类数据，二者可以同时使用，顺序不限，只要在该字段中存在即可

这也适用于不在任何特定机制内的通用属性

`| type | types, t | A list of entity types to match |<!--type:EntityType--><!--list--> |`

#### 类型 {#type}

使用此项表示属性值只能来自指定枚举，例如 Material、BarStyle 等

[有效类型列表见此处](https://github.com/Lxlp38/MythicScribe/blob/master/generated/enumList/enumList.md)，填写类型时大小写不限

#### 列表 {#list}

使用此项表示属性值可以是逗号分隔的元素列表。若与 `type` 一起使用，列表中的每个元素都必须来自同一枚举

### 触发器数据 {#trigger-data}

触发器页面可在任意位置放置其中一种注释，建议放在 `## Description` 前

- `MobTrigger` 用于仅供生物使用的触发器
- `PlayerTrigger` 用于所有玩家均可激活的触发器
- `ItemTrigger` 用于专门从物品上触发的触发器
- `ArchetypeTrigger` 用于配合使用的触发器

`<!--type:PlayerTrigger-->`

如果未指定类型，触发器会被视为“通用”，可用于多个位置。不确定时，保持不指定即可。

### 目标选择器通用属性数据 {#targeter-universal-attribute-data}

用于说明目标选择器通用属性列表适用于实体还是位置。

实际上，你通常不需要修改此项。

在属性表的 Attribute 表头中加入注释，即可设置此项

`| Attribute <!-- ETA --> | Aliases | Description | Default |`

实体使用 ETA，位置使用 LTA

## 示例页面 {#example-pages}

- [技能机制 Wiki 页面](examplemechanic.md)
- [目标选择器 Wiki 页面](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/ExampleMechanic "使用与技能机制页面相同的语法")
- [条件 Wiki 页面](https://wiki.mythiccraft.io/mythicmobs/Wiki-Editors-Resources/ExampleMechanic "使用与技能机制页面相同的语法")

## [测试页面](test-page.md) {#test-page}

## 可直接复制使用的片段 {#quick-copy-pastes}

```
## Attributes
| Attribute | Aliases   | Description                                                          | Default |
|-----------|-----------|----------------------------------------------------------------------|---------|
```

```
## Aliases
- [x] alias1
- [x] alias2
```

```
> **This is a [Paper-Only] mechanic!**

> **This is a [Premium-Only] mechanic!**

**<[Premium-Only]>**
```

```
<!-- LINKS -->
[metaskill]: /Skills/Metaskills
[mechanic]: /Skills/Mechanics
[targeter]: /Skills/Targeters
[trigger]: /Skills/Triggers
[condition]: /Skills/Conditions
[origin]: /Skills/Targeters/Origin
[audience]: /Skills/Audience

[Paper-Only]: https://papermc.io/downloads/all
[Premium-Only]: Premium-Features

[material]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html

[Implemented Placeholders]: /Skills/Placeholders#variable-placeholders
```
