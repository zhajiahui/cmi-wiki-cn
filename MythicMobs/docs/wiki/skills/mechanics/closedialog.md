---
title: Close Dialog
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CloseDialog
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Close Dialog {#close-dialog}

## 说明 {#description}

关闭目标玩家打开的[对话框](../../dialogs.md)，如果有的话，甚至是从另一个插件打开的。

1.21.8之前的服务器将其保留在屏幕上。点击后不运行MythicMobs技能，[hasDialogOpen](../conditions/hasdialogopen.md)变成  false  。

未指定目标选择器时，使用[继承目标](../metaskills.md#inheritance)，否则使用施法者。在按钮技能中，就是点击按钮的玩家。

> **这是一个[仅支持 Paper](https://papermc.io/downloads/all)机制！**

> **这是[仅限高级版](../../premium-features.md) 机制！**

## 属性 {#attributes}

*此技能机制没有属性。*

## 示例 {#examples}

关闭触发玩家的对话框。

```yaml
  Skills:
  - closeDialog @trigger
```

##  {#section}

关闭10块内玩家的对话框。

```yaml
  Skills:
  - closeDialog @PlayersInRadius{r=10}
```

## 别名 {#aliases}

- hideDialog
