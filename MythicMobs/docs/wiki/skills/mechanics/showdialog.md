---
title: Show Dialog
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ShowDialog
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Show Dialog {#show-dialog}

## 说明 {#description}

向目标玩家显示 `dialogs` 目录中的[对话框](../../dialogs.md)，可包含文本、物品、输入项和按钮。需要 1.21.6 或更新版本；Folia 上会在玩家所属区域线程打开。

在对话文本中，`<target.*>` 是查看者，`<caster.*>` 是该机制的施法者。如果没有显示 `Buttons` 条目，则不会打开任何内容并记录错误。 `ExitButton`不算数。

> **这是一个[仅支持 Paper](https://papermc.io/downloads/all)机制！**

> **这是[仅限高级版](../../premium-features.md) 机制！**

| [已实现的占位符](../placeholders.md#variable-placeholders) |
| --- |
| `<dialog.button>` |
| `<dialog.[key]>` |
| `<dialog.page>` |
| `<dialog.pages>` |

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| dialog | d, name | 对话框名称，区分大小写，支持占位符 | default |

## 响应变量 {#response-variables}

按钮和可点击文本技能获取以下值：

| 变量 | 值 |
| --- | --- |
| `dialog.button` | 被点击按钮在已显示按钮中的位置，从 0 开始。`ExitButton` 为 `-1`，[可点击文本](../../dialogs.md#clickable-text)为 `-2` |
| `dialog.[key]` | 按 `Key` 获取每个已显示的输入项。可点击文本只发送其 `key=value` 参数 |
| `dialog.page`, `dialog.pages` | 页码（从 1 开始）及总页数，仅由设置了 [`PageSize`](../../dialogs.md#generated-lists) 的对话框提供 |
| 其他 `dialog.*` | 打开对话框时传入的所有值 |

输入值是文本：

- `text`：输入的文本。标签前会添加一个 `\`，包括 `<skill>`。
- `bool`: `true` 或 `false`
- `range`：小数，例如`5.0`
- `option`：选项键

在`var=`属性中，写入`skill.dialog.[key]`。

该技能保留了该技能机制的施法者。没有目标选择器的机制作用于点击玩家。点击在对话框打开后 10 分钟后过期。

## 导航 {#navigation}

对于“后退”或“刷新”按钮，请使用 `showDialog` 与上一个或相同的对话框。 `dialog.*` 值[被保留](../../dialogs.md#passing-values-between-dialogs)，因此条目保持填充状态。

## 示例 {#examples}

向触发玩家显示`WelcomeNotice`。

```yaml
  Skills:
  - showDialog{dialog=WelcomeNotice} @trigger
```

##  {#section}

向 10 格内的每个玩家显示 `CharacterSetup`。

```yaml
  Skills:
  - showDialog{d=CharacterSetup} @PlayersInRadius{r=10}
```

##  {#section-2}

向施法者显示 `PunishMenu`，施法者必须是玩家；触发者名称通过 `<dialog.target>` 取得。

```yaml
  Skills:
  - setvariable{var=skill.dialog.target;type=STRING;value="<trigger.name>"}
  - showDialog{dialog=PunishMenu} @self
```

## 别名 {#aliases}

- openDialog
- dialog
