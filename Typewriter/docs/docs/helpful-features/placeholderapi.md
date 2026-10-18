---
title: PlaceholderAPI（PlaceHolderAPI）
source: https://docs.typewritermc.com/docs/helpful-features/placeholderapi
source_version: 0.8.0
---

# PlaceholderAPI（PlaceHolderAPI）

需要**插件**

要学习本教程，你必须安装[PlaceHolderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/)。

## 使用 PlaceholderAPI 占位符 {#use-placeholderapis-placeholders}

如果你想使用 PlaceHolderAPI 的占位符扩展你的故事，你可以通过检查 PlaceHolderAPI 图标是否位于文本框上方来实现（参见图片）：

![PlaceholderAPI图标](../../assets/e5053950a9b4-papi-icon.a3eb2bd.565.avif)

只需使用 PlaceHolderAPI 的格式，你就可以使它们发挥作用。例如，`%player_name%`将给出玩家的名字。

**不工作**

占位符不生效时，检查是否安装了对应扩展。例如，使用 `%player_name%`，需要先从 PlaceholderAPI ecloud 安装 `player`，执行：`/papi ecloud download player`。

## 使用 Typewriter 占位符 {#use-typewriters-placeholders}

Typewriter提供了两个与 PlaceHolderAPI 一起使用的占位符：

- `%typewriter_entryid%`
- `%typewriter_entryname%`

两个占位符提供相同的信息，但你可以选择以不同的方式访问它们。通常建议使用条目 ID 以获得更可靠的结果，但条目名称也是一个选项。

要查找条目 ID，请参阅下图：

![PlaceholderAPI图标](../../assets/3d63c2739603-papi-factid.0f87150.518.avif)

Typewriter的占位符类似于`%typewriter_W2X2ZbG0pzXGsS6%`。
然后，当调用占位符时，它会检查 ID 并：

- 说话者条目：返回显示名称。
- 如果他们的条目是事实，它就会返回事实值。
- 如果条目是声音，则它给出资源包声音的 ID。
- 如果条目是实体，则给出实体的显示名称
- 如果该条目是行条目，则它给出行条目的内容。
- 如果条目是任务，它会给出任务的显示名称。
- 如果条目是目标，则它给出目标的格式化显示名称。
- 如果条目是侧边栏，则它给出侧边栏的标题。

### 占位符参数 {#placeholder-parameters}

有时，你可能想从条目中获取不同的信息。这可以使用占位符参数来完成。你可以在这里找到占位符参数的非详尽列表：

#### 事实条目 {#fact-entries}

- `%typewriter_<entry id>:remaining:<number>%`：返回`<number> - fact value`（当玩家需要收集一定数量的东西并且你想显示他们还需要收集多少东西时很有用）。
- `%typewriter_<entry id>:time:lastUpdated%`：显示事实更新的时间。
- `%typewriter_<entry id>:time:lastUpdated:relative%`：显示事实更新以来的时间，例如`3m 20s`。

#### 会过期的事实 {#expirable-facts}

- `%typewriter_<entry id>:time:expires%`：事实到期的时间。
- `%typewriter_<entry id>:time:expires:relative%`：显示距离事实过期还剩多长时间，例如 `3m 20s`。

## 自定义占位符 {#custom-placeholders}

Typewriter还有 3 个自定义占位符，它们是：

- `%typewriter_tracked_quest%`：显示当前追踪的任务的显示名称。
- `%typewriter_tracked_objectives%`：显示追踪任务的活动目标的目标显示名称。
- `%typewriter_in_cinematic%`：如果不在过场动画模式下，则返回`0`；如果在过场动画模式下，则返回`1`。

---

原文：[PlaceHolderAPI](https://docs.typewritermc.com/docs/helpful-features/placeholderapi) · 文档版本：0.8.0
