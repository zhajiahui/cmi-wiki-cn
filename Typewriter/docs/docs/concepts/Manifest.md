---
title: 呈现条目（Manifest Entries）
source: https://docs.typewritermc.com/docs/concepts/Manifest
source_version: 0.8.0
---

# 呈现条目（Manifest Entries）

Typewriter 有多种条目。主要的一类是 `Sequence Entries`，包括 `Dialogue Entries`、`Event Entries` 和 `Action Entries`；另一类是 `Manifest Entry`。`Sequence Entries` 使用命令式逻辑，`Manifest Entries` 使用声明式逻辑。下面说明两者的区别和工作方式。

## “然后”与“当……时” {#then-vs-when}

### “然后”（`Sequence entries`） {#then-sequence-entries}

`Sequence Entries` 使用“然后”的逻辑，像一组按顺序执行的指令：“先做这件事，然后做那件事，再做另一件事。”可以把它看成横向的有向图，每一步依次连接到下一步。

例如，玩家在村庄中移动时，需要显示并更新一个 Minecraft Boss 栏。

通过“然后”逻辑，你将：

1. 当玩家进入村庄时显示boss栏
2. 将Boss 栏文本更新为“欢迎来到村庄！”
3. 玩家进入铁匠铺时，将 Boss 栏文字改为“去看看铁匠铺！”
4. 玩家离开铁匠铺时，将 Boss 栏文字恢复为“欢迎来到村庄！”
5. 当玩家离开村庄时隐藏Boss 栏

### “当……时”（`Manifest Entries`） {#when-manifest-entries}

`Manifest Entries` 使用“当……时”的逻辑，定义条件，以及满足条件时应发生的行为。它像一棵树，不同分支对应不同的条件和动作。

还是同一个村庄的例子，使用“当……时”的逻辑：

- 当玩家在村庄里时
  - 显示带有文字“欢迎来到村庄！”的 Boss 栏。
- 当玩家在铁匠大楼内时
  - 将 Boss 栏文字改为“去看看铁匠铺！”

在此方法中，你定义应发生操作的条件，而不是指定步骤的线性序列。
假设你想向村庄添加更多建筑物，并在玩家进入每个建筑物时显示不同的消息。
用“然后”的逻辑，会产生许多重复条目；用“当……时”的逻辑，只需增加条件和动作，Typewriter 就会根据玩家的位置决定显示内容。

## 交互图示 {#interactive-visualization}

下面的交互图示展示了“然后”和“当……时”逻辑的区别。
将光标移到村庄和铁匠铺上，观察 Boss 栏如何随玩家位置变化。

下方分别用有向图和树形结构展示这两种逻辑。

[查看原文交互图](https://docs.typewritermc.com/docs/concepts/Manifest#interactive-visualization)

[manifest.riv](../../assets/e5923f7c53e1-manifest.riv)

---

原文：[Manifest Entries](https://docs.typewritermc.com/docs/concepts/Manifest) · 文档版本：0.8.0
