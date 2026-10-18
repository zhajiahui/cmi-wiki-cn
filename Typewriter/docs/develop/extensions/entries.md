---
title: 创建条目（Create Entries）
source: https://docs.typewritermc.com/develop/extensions/entries
source_version: 0.8.0
---

# 创建条目（Create Entries）

为Typewriter插件创建扩展涉及使用各种条目类型，每种条目类型都有一个特定的目的，即打造身临其境的玩家体验。
本文档解释了这些条目类型的作用和功能，为开发人员如何有效使用它们提供了明确的指导。

## 基础条目接口 {#base-entry-interfaces}

有四个基本接口，所有条目都扩展其中之一。这些都是：

1. **StaticEntry**：代表静态页面。这些用于不会动态更改或触发任何操作的内容。示例包括静态文本或图像。
2. **TriggerEntry**：专为启动其他操作或事件的条目而设计。这些条目可以触发一个或多个附加条目，这使得它们对于交互序列至关重要。
3. **CinematicEntry**：用​​于过场动画体验。这些条目非常适合创建沉浸式故事驱动序列，以更具视觉动态的方式吸引玩家。
4. **ManifestEntry**：用于创建呈现页面，向玩家显示有状态的内容。

### 1. 静态入口 {#1-staticentry}

- **AssetEntry**：处理外部资源，例如图像或文件。
- **ArtifactEntry**：管理插件生成的资源，例如 JSON 文件。
- **EntityEntry**：用作游戏中静态实体的基础。
  - **SpeakerEntry**：扩展 EntityEntry 为能够说话的实体，并具有定义的显示名称和声音。
- **FactEntry**：表示静态事实或数据点。
- **SoundIdEntry**：保存特定声音的标识符。
- **SoundSourceEntry**：处理声音发射源。

### 2. 触发入口 {#2-triggerentry}

- **EventEntry**：事件驱动条目的基础。
  - **CustomCommandEntry**：扩展 EventEntry 以允许创建自定义游戏内命令。

#### 2a. TriggerableEntry（TriggerEntry 的扩展） {#2a-triggerableentry-an-extension-of-triggerentry}

这些是可以由其他条目触发的条目。它们是最常见的条目类型，用于创建交互式序列。

- **DialogueEntry**：专门用于与特定说话人的对话，增强NPC互动。
- **ActionEntry**：根据玩家交互执行操作，能够修改事实或触发事件。
  - **CustomTriggeringActionEntry**：ActionEntry 的变体，允许自定义触发机制和手动触发操作。

### 3. 过场动画入口 {#3-cinematicentry}

- 该基本接口主要用于在游戏中打造过场动画体验，没有列出专门的接口，但它对于创建故事驱动的视觉动态序列至关重要。

### 4. 呈现条目 {#4-manifestentry}

最大的`ManifestEntry`是`AudienceEntry`。
它用于定义可用于向玩家显示有状态内容的受众。
几乎所有其他`ManifestEntry`都是`AudienceEntry`的子类型。
虽然这不是必需的。
不是`AudienceEntry`子类型的条目的示例是`EntityDefinitionEntry`。

以下是`AudienceEntry`的子类型：

- **AudienceFilterEntry**：AudienceEntry 的变体，用于过滤传递给条目子项的受众。
- **QuestEntry**：指定任务类型。
- **ObjectiveEntry**：任务中目标的基础。
- **LinesEntry**：在侧边栏或玩家列表中显示文本行。

`ManifestEntry`的另一个类别适用于**实体**。
这在文档中有单独的页面。

## 实现与使用 {#implementation-and-usage}

每个接口都设计有特定的标签和方法，以促进Typewriter插件内的独特交互。
实现这些接口使开发人员能够打造各种玩家体验，从简单的静态显示到复杂的多步骤交互式任务和对话。

例如，TriggerableEntry 可用于设置仅在特定条件下激活的任务，而 DialogueEntry 可以通过个性化对话使 NPC 栩栩如生。
类似地，ActionEntry 可用于创建根据玩家操作而变化的动态效果，而 CinematicEntry 可用于创建视觉上动态的故事序列。

### 定义条目 {#defining-a-entry}

Typewriter负责创建和使用条目时的繁重工作。
开发人员只需要定义条目的类及其字段（有时还需要定义其他方法）。
其余的由Typewriter处理。
从扫描扩展 jar 文件中所有不同的条目类到触发它们。

定义一个条目需要满足以下要求：

1. 必须是实现某个基础条目接口的类。
2. 它必须有一个无参数构造函数。
3. 它必须具有包含所有必填字段的`@Entry`注解。

`@Entry`注解用于定义条目的类型、名称和其他属性。它有以下字段：

- **name**：条目的名称。这用于识别条目。
- **description**（描述）：条目的简短描述。
- **color**（颜色）：编辑器中条目的颜色。它可以是`Colors`类中的一个，也可以是十六进制颜色代码字符串。
- **icon**（图标）：编辑器中条目的图标。所有可用的图标都可以在[Iconify](https://icones.js.org/)上找到。它必须是图标的名称。

要了解每个条目类型的具体要求，请查看条目接口的文档。

**注意**

条目中不允许保存状态，因此所有字段都必须是 final 字段。
如果你需要状态，请使用`AudienceEntry`。

---

总之，这些条目接口构成了Typewriter插件功能的支柱，为在Minecraft中创建沉浸式和交互式内容提供了强大的框架。
通过理解和利用这些接口，开发人员可以极大地增强玩家体验，使其更具吸引力和活力。

---

原文：[Create Entries](https://docs.typewritermc.com/develop/extensions/entries) · 文档版本：0.8.0
