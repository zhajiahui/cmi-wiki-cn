---
title: 自定义命令（Custom Commands）
source: https://docs.typewritermc.com/docs/creating-stories/advanced-interactions/custom-commands
source_version: 0.8.0
---

# 自定义命令（Custom Commands）

**开始前**

本教程假定你已按[安装指南](../../getting-started/installation.md#basic-extension)安装 Basic Extension。

本教程介绍自定义命令的创建方式。示例命令接收昵称（pseudo）和年龄，然后向玩家显示消息。

## 创建自定义命令 {#creating-a-custom-command}

示例命令接收昵称（pseudo）和年龄，再向玩家显示消息。首先用 Custom Command 条目定义命令。
要添加自定义命令条目，请转到面板的右上角并单击 + 图标。搜索`Add Custom Command`，将其添加到你的呈现中并为其命名。

添加自定义命令

创建带有参数的自定义命令

+

## 创建参数 {#creating-the-arguments}

这里需要两种参数：`Word Argument` 接收单词，在示例中用于昵称；`Number Argument` 接收数字，在示例中用于年龄。
要添加参数，请单击`Custom Command`条目，然后单击`Arguments`，然后选择`Add Word Argument`。接下来，单击最后一个参数并添加一个子项：`Add Number Argument`。

![自定义命令参数](../../../assets/a3549dbd8813-custom-command-arguments.e8e529a.528.avif)

![争论子活动](../../../assets/db8388a835e5-arguments-children.5d45883.528.avif)

**编号参数**

重命名你的参数，以便玩家在执行命令时更容易理解。

## 为命令添加行为 {#do-something-with-your-command}

要让命令执行动作，把触发项添加到最后一个参数中。这里在 `Number Argument` 中点击 `Trigger`，选择动作条目。示例使用 `Send Message` 条目。
用 `Interaction Context Text Variable` 读取玩家输入的参数，并为变量设置键。最后用读取到的参数值拼出消息。

![交互上下文文本变量](../../../assets/18708cff90a3-context-text-variable.aa02770.528.avif)

## 结果 {#result}

### 序列结果 {#sequence-result}

现在你的页面应该如下所示：

[sequence.json](../../../assets/814d9dcd77ee-sequence.json)

[manifest.json](../../../assets/059f8b0f9f49-manifest.json)

**变量**

我们的文档渲染器当前不支持显示动态变量，因此你只会看到简化的静态消息，而不是实际的变量。

### 游戏内结果 {#in-game-result}

在游戏中，命令应该如下所示：

<video controls preload="metadata" src="../../../assets/243f6f7fc444-result.webm"></video>

---

原文：[Custom Commands](https://docs.typewritermc.com/docs/creating-stories/advanced-interactions/custom-commands) · 文档版本：0.8.0
