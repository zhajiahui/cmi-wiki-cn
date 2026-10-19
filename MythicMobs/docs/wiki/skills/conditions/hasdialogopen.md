---
title: Has Dialog Open
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/HasDialogOpen
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Has Dialog Open {#has-dialog-open}

## 说明 {#description}

检查目标玩家是否打开了 MythicMobs [对话框](../../dialogs.md)。 [showDialog](../mechanics/showdialog.md) 使其  true   直到：

- 按钮或[可点击文本](../../dialogs.md#clickable-text) 单击，使用 `AfterAction: CLOSE`
- 点击了不运行任何技能、且设置为 `AfterAction: WAIT_FOR_RESPONSE` 的选项。
- `ExitButton` 点击
- [closeDialog](../mechanics/closedialog.md) 运行
- 玩家离开服务器

除非`CanClose: false`，否则 Escape 会关闭屏幕上的对话框并[单击按钮](../../dialogs.md#closing-with-escape)。 Escape 在没有 `ExitButton` 的[多操作对话框](../../dialogs.md#buttons) 上不单击任何内容。如果没有发生上面列表中的点击，则条件将保持  true  ，直到`closeDialog`运行、玩家离开服务器或稍后的对话框关闭。

> **此条件[仅支持 Paper](https://papermc.io/downloads/all)！**

> **这是[仅限高级版](../../premium-features.md) 条件！**

## 属性 {#attributes}

*此条件没有属性*

## 示例 {#examples}

```yaml
  Conditions:
  - hasDialogOpen true
```

## 别名 {#aliases}

- dialogOpen
