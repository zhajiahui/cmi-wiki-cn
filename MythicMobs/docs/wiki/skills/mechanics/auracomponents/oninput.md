---
title: On Input
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/OnInput
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Input {#on-input}

## 说明 {#description}

根据玩家输入触发技能。该组件可能需要定向移动、跳跃/潜行/冲刺状态或任何移动。匹配的状态导出为整型变量

| [已实现的占位符](../../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.input-forward>` |
| `<skill.var.input-backward>` |
| `<skill.var.input-right>` |
| `<skill.var.input-left>` |
| `<skill.var.input-jump>` |
| `<skill.var.input-sneak>` |
| `<skill.var.input-sprint>` |

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v6"></path><path d="M12 17h.01"></path></svg>Variable's values

未进行对应输入时，变量值为 `0`；正在输入时为 `1`。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| oninputskill | oninput, oi | 输入状态匹配时执行的技能。 |  |
| forward |  | 是否要求向前输入。 | false |
| backward |  | 是否要求向后输入。 | false |
| left |  | 是否要求向左输入。 | false |
| right |  | 是否要求向右输入。 | false |
| requireanymovement | anymovement, move | 是否要求任意方向输入。 | false |
| requirejump | jump | 是否要求跳跃输入。 | false |
| requiresneak | sneak | 是否要求潜行输入。 | false |
| requiresprint | sprint | 是否要求疾跑输入。 | false |

## 别名 {#aliases}

- playerinput
