---
title: 对话框
source_url: https://wiki.mythiccraft.io/mythicmobs/Dialogs
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 对话框 {#dialogs}

对话框是由 [Paper Dialog API](https://docs.papermc.io/paper/dev/dialogs) 提供的交互窗口，属于 **[Premium 版功能](premium-features.md)**，需要 **Paper 1.21.6** 或更新版本。使用 [showDialog](skills/mechanics/showdialog.md) 技能机制或 `/mm dialogs show` 打开。

对话框文本支持 [MiniMessage](https://docs.advntr.dev/minimessage/format.html) 和[占位符](skills/placeholders.md)。`&c` 等[旧式颜色代码](skills/placeholders.md#color-codes)会导致对话框无法打开，控制台会记录 `could not be shown`。返回这类颜色代码的占位符也会导致相同问题，例如来自 `Display: '&6Guard'` 的生物名称。

1. [配置](dialogs.md#configuration)
2. [主体元素](dialogs.md#body-elements)
3. [输入项](dialogs.md#inputs)
   1. [输入值](dialogs.md#input-values)
4. [按钮](dialogs.md#buttons)
   1. [点击后的行为](dialogs.md#after-a-click)
   2. [按钮技能中的值](dialogs.md#values-in-button-skills)
   3. [按 Escape 关闭](dialogs.md#closing-with-escape)
   4. [退出按钮](dialogs.md#exit-button)
5. [条件](dialogs.md#conditions)
6. [动态生成的列表](dialogs.md#generated-lists)
   1. [目标选择器生成的行](dialogs.md#targeter-rows)
   2. [数值列表生成的行](dialogs.md#value-rows)
   3. [行条件](dialogs.md#row-conditions)
   4. [分页](dialogs.md#pages)
   5. [玩家列表分页示例](dialogs.md#paged-player-list)
7. [在对话框之间传递值](dialogs.md#passing-values-between-dialogs)
8. [验证输入](dialogs.md#validating-input)
9. [图标、头颅和布局](dialogs.md#icons-heads-and-layout)
   1. [精灵图与头颅](dialogs.md#sprites-and-heads)
   2. [命名图标](dialogs.md#named-icons)
   3. [通过资源包设置布局](dialogs.md#layout-with-a-resource-pack)
   4. [可点击文本](dialogs.md#clickable-text)
10. [使用 MythicCrucible 绘制菜单](dialogs.md#drawing-menus-with-mythiccrucible)
    1. [设置](dialogs.md#setup)
    2. [可点击图片](dialogs.md#clickable-images)
    3. [可变化的图片](dialogs.md#images-that-change)
    4. [放置图片](dialogs.md#placing-images)
    5. [背景面板](dialogs.md#background-panel)
    6. [提示](dialogs.md#tips)
11. [技能机制、条件与命令](dialogs.md#mechanics-conditions-and-commands)
12. [开发者 API](dialogs.md#developer-api)

## 配置 {#configuration}

MythicMobs 会加载 `plugins/MythicMobs` 和[内容包](packs.md)的 `dialogs` 文件夹及其子文件夹中的所有 `.yml` 文件，也会加载内容包 `files` 文件夹中的 `.dialog.yml` 文件。每个对话框都以其名称开头，名称区分大小写：

```yaml
WelcomeNotice:
  Title: "<gold>Welcome!"
  Body:
  - Type: text
    Message: "<gray>Welcome to the server, <target.name>!"
  Buttons:
  - Label: "<green>Got it!"
```

- `Title`：顶部显示的文本
- `ExternalTitle`：从暂停菜单等其他界面打开此对话框时，按钮上显示的名称。通过 MythicMobs 打开时不显示
- `CanClose`：是否允许按 Escape 关闭，默认为 `true`，参见[按 Escape 关闭](dialogs.md#closing-with-escape)
- `Pause`：暂停游戏，仅限单人模式，默认为 `false`
- `AfterAction`：点击后的行为，默认为 `CLOSE`，参见[点击后的行为](dialogs.md#after-a-click)
- `Columns`：多操作对话框中按钮的列数，默认为 `1`

在对话框文本和 `ForEach` 中，`<target.*>` 表示查看对话框的玩家，`<caster.*>` 表示执行 `showDialog` 的施法者，例如某个生物。使用 `/mm dialogs show` 时，两者均为该玩家。

## 正文元素 {#body-elements}

`Body` 用于列出文本和物品元素：

- `Type`：`text` 或 `item`，默认为 `text`
- `Message`：显示的文本
- `Width`：文本最大为 1024 像素，物品最大为 256 像素；默认分别为 256 和 64
- `Item`：见下文，支持占位符
- `Height`：物品高度，最大为 256 像素，默认为 64
- `Decoration`：显示物品数量和耐久条，默认为 `false`
- `ShowTooltip`：鼠标悬停时显示提示信息，默认为 `true`

`Item` 接受以下内容：

- 原版材质或 Mythic 物品
- `mmoitems.TYPE.ID`
- 原版掉落行，例如 `DIAMOND{amount=3}`
- [掉落表](drops/droptables.md)，每次会从中随机取得一个新物品

其他掉落行，例如 `mmoitems{type=...;id=...}`，以及无法识别的物品，会显示为 `STONE` 并记录错误。

## 输入项 {#inputs}

点击按钮时，会将各输入项的值以 `dialog.<key>` 形式传递给按钮技能，其中 `<key>` 是输入项的 `Key`。输入项接受以下设置：

- `Type`：`text`（文本框）、`bool`（复选框）、`range`（滑块）或 `option`（选项）
- `Key`：仅允许字母、数字和 `_`
- `Label`：与输入项一起显示的文本
- `Initial`：初始值。支持占位符，不支持 MiniMessage，参见[输入值](dialogs.md#input-values)
- `Width`：最大 1024 像素，默认为 200。不适用于 `bool`
- `LabelVisible`：是否显示标签，默认为 `true`。仅适用于 `text` 和 `option`

`text` 输入项还接受以下设置：

- `MaxLength`：最大字符数，默认为 256
- `Multiline`：允许输入多行，默认为 `false`
- `MaxLines`、`Height`：配合 `Multiline` 使用，分别设置最大行数和高度；高度最大为 512 像素，默认采用客户端的设置

`range` 输入项还接受以下设置：

- `Start`、`End`：最小值和最大值，默认为 0 和 100
- `Step`：步长，从 `Initial` 开始计算
- `LabelFormat`：用引号括起的滑块文本，不支持占位符或 MiniMessage，默认为 `Label: value`。`"%s: %s"` 显示 `Label` 和数值，`"Volume %2$s"` 只显示数值

未设置 `Initial` 时，会从中点开始计算步长。例如，`Start: 1`、`End: 10` 和 `Step: 1` 会得到 1.5、2.5 ... 9.5。

`option` 输入项还必须设置 `Options`，格式为 `key: "Label"` 键值对。

### 输入值 {#input-values}

输入项在已设置 `dialog.<key>` 时使用该值作为初始值，否则使用 `Initial`。前一个对话框的点击、`setvariable{var=skill.dialog.<key>}` 或 `/mm dialogs show` 都可以设置这个值，参见[传递值](dialogs.md#passing-values-between-dialogs)。

| 类型 | 初始值 | 传入值 |
| --- | --- | --- |
| `text` | 截断至 `MaxLength` | 截断至 `MaxLength` |
| `bool` | 仅在值为 `true` 时勾选 | `true` 或 `false` |
| `range` | 保持在 `Start` 与 `End` 之间 | 例如 `5.0` 的小数，同样限制在指定范围内 |
| `option` | 未知的键会选中第一个选项 | 选项的键 |

玩家输入的标签，例如 `<red>` 和 `<skill>`，前面会加上 `\`，因此不会产生颜色、点击或悬停效果。重新打开输入框时，会看到这个 `\`。输入的 `&` 颜色代码在对话框中保持纯文本，但在 `message` 等技能机制中会转换为颜色。

被 `Conditions` 隐藏的输入项不会发送任何值，而是保留打开对话框时的值。如果修改过的客户端发送了无效值，技能不会执行。

```yaml
CharacterSetup:
  AfterAction: WAIT_FOR_RESPONSE
  Inputs:
  - Type: text
    Key: nickname
    Label: "Display Name"
    Initial: "<target.name>"
  - Type: bool
    Key: pvpEnabled
    Label: "Enable PvP?"
    Initial: true
  - Type: range
    Key: difficulty
    Label: "Difficulty"
    Start: 1
    End: 10
    Initial: 5
    Step: 1
  - Type: option
    Key: classChoice
    Label: "Class"
    Initial: mage
    Options:
      warrior: "<red>Warrior"
      mage: "<blue>Mage"
  Buttons:
  - Label: "<green>Confirm"
    Skills:
    - message{m="<green>Saved <dialog.nickname> as <dialog.classChoice>"}
    - closeDialog
  - Label: "<red>Cancel"
```

## 按钮 {#buttons}

显示出来的 `Buttons` 数量决定对话框类型：1 个按钮为通知，2 个为确认，3 个或更多为采用 `Columns` 的多操作对话框。显示 `ExitButton` 或 `ForEach` 按钮时，也会使用多操作对话框。如果没有任何可见的 `Buttons` 条目，且不将 `ExitButton` 计入其中，对话框就不会打开。

- `Label`：按钮文本
- `Tooltip`：悬停时显示的文本
- `Width`：最大为 1024 像素，默认为 150
- `Skill`：点击时执行的技能，前提是其条件通过
- `Skills`：点击时执行的技能机制，在 `Skill` 之后运行

```yaml
QuestOffer:
  Title: "<gold>New Quest Available"
  Buttons:
  - Label: "<green>Accept"
    Tooltip: "Accept this quest"
    Skills:
    - message{m="<green>Quest accepted!"}
  - Label: "<red>Decline"
```

### 点击后 {#after-a-click}

- `CLOSE`：关闭对话框。
- `NONE`：保持对话框打开。
- `WAIT_FOR_RESPONSE`：显示等待界面，直到技能执行 `showDialog` 或 `closeDialog`，因此技能应以其中一种机制结束。如果没有技能执行，包括未配置技能、条件不满足、输入值无效或点击被取消，对话框会关闭。

1.21.8 之前的服务器无法主动关闭对话框，因此下列情况下对话框会保持打开：

- 执行 `closeDialog` 后
- 在 `NONE` 模式下点击 `ExitButton` 后
- 一次 `WAIT_FOR_RESPONSE` 点击没有执行任何技能时

点击操作会在 10 分钟后过期，关闭或替换对话框时也会过期。

### 按钮技能中的值 {#values-in-button-skills}

按钮技能保留打开对话框的技能所使用的施法者和触发者，并将点击按钮的玩家作为目标，因此未指定目标选择器的技能机制会作用于该玩家。按钮技能会获得以下值：

- `dialog.button`：点击的按钮在已显示按钮中的位置，从 0 开始。`ExitButton` 为 `-1`，[可点击文本](dialogs.md#clickable-text)为 `-2`
- `dialog.<key>`：每个可见输入项的值
- `dialog.page`、`dialog.pages`：参见[分页](dialogs.md#pages)
- 打开对话框时传入的其他所有 `dialog.*` 值

在文本中写作 `<dialog.nickname>`。在 `setvariable` 等机制的 `var=` 选项中，写作 `skill.dialog.nickname`。

### 按 Esc 关闭 {#closing-with-escape}

设置 `CanClose: true` 后，按 Escape 会关闭对话框，并点击通知对话框的按钮、确认对话框的第二个按钮或 `ExitButton`。该点击会发送输入值。

### 退出按钮 {#exit-button}

`ExitButton` 是一个额外按钮，除不支持 `ForEach` 和 `PageSize` 外，使用与其他按钮相同的字段。无论 `AfterAction` 设置为何值，它都会关闭对话框。

## 条件 {#conditions}

`Conditions` 会向不满足条件的玩家隐藏主体元素、输入项、按钮或 `ExitButton`。

```yaml
  Buttons:
  - Label: "<green>VIP Shop"
    Skill: OpenVIPShop
    Conditions:
    - hasTag{tag=vip}
```

条件会将查看对话框的玩家作为施法者，即使对话框由生物打开也是如此：`hasItem`、`holding`、施法者变量及 `<caster.*>` 都会检查该玩家。在对话框文本中，`<caster.*>` 仍表示该生物。条件也可以访问 `dialog.*` 值。

## 生成的列表 {#generated-lists}

带有 `ForEach` 的主体元素或按钮会为列表中的每一行重复一次。`PageSize` 设置每页行数，默认显示所有行。请至少保留一个不带 `ForEach` 的可见 `Buttons` 条目，以便列表为空时对话框仍能打开。

### 目标选择器行 {#targeter-rows}

以 `@` 开头的 `ForEach` 是一个目标选择器，例如 `@PlayersInRadius{r=20}`。每个实体对应一行，可使用 `<skill.value>`（实体名称）、`<skill.uuid>` 和 `<skill.index>`（从 0 开始）。目标选择器以 `showDialog` 的施法者为起点，默认排除施法者，除非添加 `targetself=true`。使用 `/mm dialogs show` 时，可用 `@PlayersOnServer{targetself=true}` 将查看者包含在内。

```yaml
  Body:
  - Type: text
    ForEach: "@PlayersInRadius{r=20}"
    Message: "<skill.value>"
```

### 数值行 {#value-rows}

其他形式的 `ForEach` 会先填入占位符，再按 [forEachValue](skills/mechanics/foreachvalue.md) 的 `values` 格式拆分：

- `key=value;key2=value2`：每个键值对生成一行，可使用 `<skill.key>` 和 `<skill.value>`
- `a,b,c`：每个条目生成一行，可使用 `<skill.value>`
- `a`：生成一行，可使用 `<skill.value>`

每一行还包含 `<skill.index>`。可以使用变量，例如 `ForEach: "<target.var.warps>"`。

```yaml
  Body:
  - Type: item
    ForEach: "DIAMOND,EMERALD,GOLD_INGOT"
    Item: "<skill.value>"
```

### 行条件 {#row-conditions}

占位符和 `Conditions` 会分别应用到每一行，因此可以用 `Conditions` 筛选行。下面的配置只保留大于或等于 100 的值：

```yaml
  Buttons:
  - ForEach: "<global.var.bounties>"
    Label: "<skill.key> <gold><skill.value>"
    Conditions:
    - compareValues{v1=<skill.value>;op=>=;v2=100}
```

### 分页 {#pages}

`dialog.page` 表示当前页，默认为 1，并限制在 1 到最后一页之间；`dialog.pages` 表示总页数。只有设置了 `PageSize` 的对话框才会修改这两个值。因此，返回列表的按钮会回到原来的页码，点击后打开的另一个分页对话框也会从这个页码开始。要从第 1 页开始：

```yaml
    Skills:
    - setvariable{var=skill.dialog.page;type=INTEGER;value=1}
    - showDialog{dialog=WarpList}
```

### 分页玩家列表 {#paged-player-list}

每页显示 6 名在线玩家，并设置上一页和下一页按钮；到达第一页或最后一页时，隐藏相应按钮：

```yaml
OnlinePlayers:
  Title: "<gold>Players <gray>(<dialog.page>/<dialog.pages>)"
  AfterAction: WAIT_FOR_RESPONSE
  Buttons:
  - ForEach: "@PlayersOnServer{targetself=true}"
    PageSize: 6
    Label: "<skill.value>"
    Skills:
    - message{m="<gold>You picked <skill.value>"}
    - closeDialog
  - Label: "<gray>Previous"
    Conditions:
    - compareValues{v1=<dialog.page>;op=>;v2=1}
    Skills:
    - variableSubtract{var=skill.dialog.page;amount=1}
    - showDialog{dialog=OnlinePlayers}
  - Label: "<gray>Next"
    Conditions:
    - compareValues{v1=<dialog.page>;op=<;v2=<dialog.pages>}
    Skills:
    - variableAdd{var=skill.dialog.page;amount=1}
    - showDialog{dialog=OnlinePlayers}
  ExitButton:
    Label: "Close"
```

## 在对话框之间传递值 {#passing-values-between-dialogs}

一次点击产生的 `dialog.*` 值，会传入其技能执行的任何 `showDialog`。返回按钮可使用 `showDialog{dialog=PreviousDialog}`，刷新按钮则再次使用 `showDialog` 打开当前对话框，输入内容会保持填入状态。

从其他技能打开时，应先设置这些值。在生物技能中，用 `@trigger` 等目标选择器选择玩家，不要使用 `@self`。下面的施法者是一名玩家：

```yaml
  Skills:
  - setvariable{var=skill.dialog.target;type=STRING;value="<trigger.name>"}
  - showDialog{dialog=PunishMenu} @self
```

对话框读取 `<dialog.target>`。命令接受不含空格的 `key=value` 键值对，例如 `/mm dialogs show PunishMenu Notch reason=griefing` 会将 `<dialog.reason>` 设为 `griefing`。

## 验证输入 {#validating-input}

在[元技能](skills/metaskills.md)中检查这些值。检查项放在 `Conditions` 中，任一项失败时，执行 `FailedConditionsSkills` 中的技能机制，或 `FailedConditionsSkill` 指定的技能：

- 非空：`stringNotEmpty{s="<dialog.name>"}`
- 至少 3 个字符：`compareValues{v1=<dialog.name.size>;op=>=;v2=3}`
- 仅限数字：`stringEquals{v1=<dialog.code.regex.^\d+$>;v2=true}`
- 数值大于或等于 10：`compareValues{v1=<dialog.amount>;op=>=;v2=10;type=DOUBLE}`

不设置 `type=DOUBLE` 时，非数字值会按文本比较，因此 `abc` 也会通过。

要显示错误信息，先设置 `dialog.error`，再重新打开对话框。第一个主体元素仅在设置了错误时显示：

```yaml
NameForm:
  Title: "<gold>Pick a name"
  AfterAction: WAIT_FOR_RESPONSE
  Body:
  - Type: text
    Message: "<dialog.error>"
    Conditions:
    - variableIsSet{var=skill.dialog.error}
  Inputs:
  - Type: text
    Key: name
    Label: "Name"
  Buttons:
  - Label: "<green>Save"
    Skill: SaveName
  - Label: "<red>Cancel"
```

在 `Skills` 文件夹中：

```yaml
SaveName:
  Conditions:
  - compareValues{v1=<dialog.name.size>;op=>=;v2=3}
  FailedConditionsSkills:
  - setvariable{var=skill.dialog.error;type=STRING;value="<red>Use at least 3 characters"}
  - showDialog{dialog=NameForm}
  Skills:
  - message{m="<green>Saved <dialog.name>"}
  - closeDialog
```

## 图标、头颅与布局 {#icons-heads-and-layout}

### 精灵图与头颅 {#sprites-and-heads}

有两个 MiniMessage 标签可以绘制图片。服务器和客户端都需要 1.21.9 或更新版本：

- `<sprite:[atlas:]sprite>` 用于绘制游戏或资源包纹理，例如 `<sprite:"block/stone">`。atlas 是纹理所属的图集，省略时使用 `minecraft:blocks`。包含 `:` 的名称必须用引号括起。
- `<head:name[:hat]>` 绘制玩家面部，默认包含帽子层，除非 `hat` 为 `false`。

从 1.21.11 起，物品纹理位于 `minecraft:items`，例如 `<sprite:"minecraft:items":"item/diamond">`；此前位于 `minecraft:blocks`，写作 `<sprite:"item/diamond">`。

资源包可以向已有图集添加精灵图，但不能添加新图集。例如，`assets/mypack/textures/gui/sprites/icons/coin.png` 对应 `<sprite:"minecraft:gui":"mypack:icons/coin">`。这两个标签都按 8x8 绘制；如需其他尺寸，请使用 [MythicCrucible 字体图片](dialogs.md#drawing-menus-with-mythiccrucible)。

`<head>` 接受玩家名称，例如 `<head:<target.name>>`，或正版模式 UUID。其他值，例如离线模式 UUID、包含空格或颜色的名称，可能导致对话框无法打开。

```yaml
  Body:
  - Type: text
    Message: '<sprite:"minecraft:gui":"hud/heart/full"> <red>Full health'
```

在所有 MythicMobs 文本中，占位符都可以用于任意 MiniMessage 标签内部，例如 `<head:<skill.value>>` 或 `<click:run_command:/warp <skill.value>>`。

### 命名图标 {#named-icons}

在内容包的 `placeholders.yml` 中，将图标定义为一个[静态占位符](skills/placeholders.md#custom-placeholders)：

```yaml
heart: "<sprite:'minecraft:gui':'hud/heart/full'>"
```

随后可在任意文本中使用，例如 `Message: "<placeholder.heart> Full health"`。静态占位符会在文件加载前直接替换到文件中。如果外层文本使用双引号，占位符值内部的引号必须像上例一样使用单引号，否则文件会加载失败。

### 使用资源包布局 {#layout-with-a-resource-pack}

对话框没有 x/y 坐标。`<font:namespace:name><char.XXXX></font>` 按十六进制编码输出资源包字体字符，例如 `F801` 或 `1F600`。`space` 字体的字符有宽度但没有图像，负宽度会将后续文本向左移动。可以在 `placeholders.yml` 中为常用偏移命名，例如 `back2: '<font:mythic:space><char.F802></font>'`，然后使用 `<placeholder.back2>`。[放置图片](dialogs.md#placing-images)一节提供了空白字体示例。

### 可点击文本 {#clickable-text}

在主体文本中，`<skill:SkillName>...</skill>` 会让标签内的文本变为可点击文本。点击后会像[按钮技能](dialogs.md#values-in-button-skills)一样执行技能。在技能名称后添加 `:key=value` 键值对，可以将值作为 `dialog.<key>` 传入：

```yaml
  Body:
  - Type: text
    Message: "<skill:OpenShop:shop=weapons><gold>[Weapons]</skill> <skill:OpenShop:shop=armor><gold>[Armor]</skill>"
```

在 `OpenShop` 中，`<dialog.shop>` 的值为 `weapons` 或 `armor`。

- 在 `Title` 等其他位置，该标签会显示为纯文本。
- 点击文本不会发送输入值；如需发送，请使用按钮。
- `AfterAction` 同样适用于文本点击。设为 `NONE` 时，技能可以修改某个值，再重新打开对话框。
- 只有标签内的文本和图片可以点击。
- 包含 `:` 的参数必须用引号括起，例如 `<skill:Warp:'to=world:spawn'>`。
- 无法识别的技能会记录错误，且不会提供点击操作。
- 只有[文本输入项](dialogs.md#input-values)会转义标签。聊天等其他由玩家编写的文本不要直接放入主体文本。

下面的开关会切换一个已保存变量的值。标签传入当前值，再由技能条件决定新值：

```yaml
ToggleMenu:
  AfterAction: NONE
  Body:
  - Type: text
    Message: "PvP <skill:TogglePvp:current=<target.var.pvp|false>><yellow>[<target.var.pvp|false>]</skill>"
  Buttons:
  - Label: "Done"
    Skills:
    - closeDialog
```

在 `Skills` 文件夹中：

```yaml
TogglePvp:
  Conditions:
  - stringEquals{v1=<dialog.current>;v2=true}
  Skills:
  - setvariable{var=target.pvp;type=STRING;value=false;save=true}
  - showDialog{dialog=ToggleMenu}
  FailedConditionsSkills:
  - setvariable{var=target.pvp;type=STRING;value=true;save=true}
  - showDialog{dialog=ToggleMenu}
```

## 使用 MythicCrucible 绘制菜单 {#drawing-menus-with-mythiccrucible}

[MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/home) 可以将 PNG 文件转换为字体图片，也就是显示为图像的字符。玩家需要使用 Crucible 生成的资源包。更多选项见 [Crucible 字体文档](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/ResourcePack/ResourcePack-Generator#fonts)。

### 设置 {#setup}

1. 将 PNG 放入[内容包](packs.md)的 `assets/textures/` 下，例如 `plugins/MythicMobs/packs/MyUI/assets/textures/myui/panel.png`。`textures` 及其后的所有路径都使用小写，且不能包含空格。
2. 在内容包文件夹中创建 `font-images.yml`，Crucible 不会自动创建此文件：

   ```yaml
   panel:
     File: myui/panel
     Height: 143
     Ascent: 11
   ```

   - `File`（必填）：`assets/textures/` 下的路径，不包含 `.png`
   - `Height`：绘制高度，单位为像素，默认为 PNG 高度
   - `Ascent`：将图片向上移动，默认值为 `Height` 的一半。如果超过 `Height`，所有字体图片都会显示异常
   - `Char`：用于显示图片的字符，默认由 Crucible 选择

每张图片会在所有位置替换对应字符，包括聊天中。Crucible 从 `plugins/MythicMobs/config/config-generation.yml` 的 `Generation.FontImages.StartingCharacter` 开始递增分配字符，默认值 `"\u5001"` 属于汉字。如果玩家使用中文或日文，应改为不属于任何语言的 `"\uE000"`。必须保留双引号，否则图片会替换普通字符。
3. 在对话框的 `Message` 中使用 `<fontimage.panel>`，其中 `fontimage` 必须小写，并放在所有 `<font>` 标签之外。图片名称不能包含点。在 `Message` 开头添加 `<!shadow>`，可避免图片带有阴影。
4. 执行 `/mm reload`，再执行 `/mm items generate`。启动服务器时也会生成资源包。
5. 默认情况下，Crucible 会将资源包上传至 mcpacks.dev，并在玩家加入及每次生成后发送给玩家。需要在 `config-generation.yml` 中将 `Deployment.Enabled`、`AutoSend.Enabled` 和 `AutoSend.SendOnUpdate` 设为 `true`。如需自行托管，参见[自行托管](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/ResourcePack/ResourcePack-Generator#self-hosting)。`/mmc pack @a` 可以手动发送资源包。

### 可点击图片 {#clickable-images}

`<skill:OpenShop><fontimage.shop></skill>` 会让整张图片的矩形区域都可点击，包括透明像素。可点击图片相互重叠时，`Message` 中靠后的图片会接收点击。没有点击操作的图片不会阻挡点击。

### 可变化的图片 {#images-that-change}

图片名称中的占位符会先被解析。准备好 `toggle_true` 和 `toggle_false` 两张字体图片后，将 [ToggleMenu](dialogs.md#clickable-text) 的 `Message` 改为：

```yaml
    Message: "<!shadow>PvP <skill:TogglePvp:current=<target.var.pvp|false>><fontimage.toggle_<target.var.pvp|false>></skill>"
```

两张图片应使用相同宽度，以免布局移动。静态占位符无法实现这种效果，`<placeholder.toggle_<target.var.pvp|false>>` 不会生效。

### 放置图片 {#placing-images}

每个文本元素是一个宽度为 `Width` 像素的文本框。文本会在 `Width - 8` 处换行。每一行都会单独居中，因此应让各行的总宽度相同。每行高 9 px。

- **上下移动：**`Ascent: 7` 会让图片顶部与当前行顶部对齐。数值越大越靠上，越小越靠下，每增加或减少 1，移动 1 px。
- **左右移动：**使用空白字体。创建 `plugins/MythicCrucible/myui_space/assets/mythic/font/space.json`：

  ```json
  {
    "providers": [
      {"type": "space", "advances": {"\uf801": -1, "\uf802": -2, "\uf821": 1, "\uf822": 2}}
    ]
  }
  ```

将该文件夹加入 `config-generation.yml` 已有的 `FromLocation` 列表中；列表为空时替换 `[]`，以便 Crucible 将其复制到资源包：

  ```yaml
  Generation:
    Import:
      FromLocation:
      - plugins/MythicCrucible/myui_space
  ```

随后，`<font:mythic:space><char.F801></font>` 会将下一个字符向左移动 1 px。在下一张图片前关闭 `</font>`。
- 图片占用的宽度为原宽度乘以缩放比例（`Height` / PNG 高度），再加 1 px。PNG 右侧边缘的空白列不计入宽度。一张宽 20 px 的 PNG 放大 2x 后占用 41 px。每行的第一张图片可以比 `Width - 8` 更宽。

普通字体各字符的宽度如下，已包含每个字符后面的 1 px 间隔：

| 宽度 | 字符 |
| --- | --- |
| 2 | `! ' , . : ; i |` |
| 3 | `` ` `` `l` |
| 4 | 空格、`" ( ) * I [ ] t { }` |
| 5 | `< > f k` |
| 6 | 其他所有 ASCII 字母、数字和符号 |
| 7 | `@ ~` |

### 背景面板 {#background-panel}

满足以下条件时，背景图片可以覆盖整个文本框：

- 单独放在第一行，并用 `<newline>` 结束该行
- 宽度恰好为 `Width` px，且 `Width` 必须是不大于 256 的偶数
- 高度为 `9 x lines + 8` px，其中行数包含该元素的所有行，也包含图片自己所在的行
- 设为 `Ascent: 11`，使用直角，不留透明的角部像素

当 `Width: 256` 且有 15 行时，PNG 尺寸为 256 x 143。它还会遮住 Minecraft 26.3 在点击后的文本框周围绘制的白色轮廓。其他行恰好宽 `Width - 8` 时，起点距离边缘为 4 px。

### 提示 {#tips}

- PNG 最大为 256 x 256 像素，超过后会显示为空框。可以用 `Height` 将其绘制得更大。
- 将 `Height` 设为 PNG 高度的 1、2 或 3 倍，以保持像素清晰。缩小图片会丢失像素。
- 宽度会变化的文本，例如名称和数字，会让整行内容移动。应将这类文本单独放在一行，或放在 `Title` 中。

## 技能机制、条件与命令 {#mechanics-conditions-and-commands}

- 技能机制：[showDialog](skills/mechanics/showdialog.md) 和 [closeDialog](skills/mechanics/closedialog.md)。`closeDialog` 也会关闭其他插件的对话框。
- 条件：[hasDialogOpen](skills/conditions/hasdialogopen.md)。仅统计 MythicMobs 对话框。

| 命令 | 说明 | 权限 |
| --- | --- | --- |
| `/mm dialogs list` (`l`) | 列出已加载的对话框 | `mythicmobs.command.dialogs.list` |
| `/mm dialogs show <dialog> [player] [key=value...]` (`s`, `open`) | 向指定玩家或你自己显示对话框。参见[传递值](dialogs.md#passing-values-between-dialogs) | `mythicmobs.command.dialogs.show` |

玩家还需要 `mythicmobs.command.base` 和 `mythicmobs.command.dialogs`，或者 `mythicmobs.admin` 权限。`/mm dialogs` 也可以写作 `/mm dialog` 或 `/mm dl`。

## 开发者 API {#developer-api}

两个事件都位于 `io.lumine.mythic.bukkit.events`，并提供 `getPlayer()` 和 `getDialog()`，后者返回对话框名称：

- `MythicDialogOpenEvent` 在发送对话框前触发，取消事件可以阻止对话框显示。
- `MythicDialogClickEvent` 在点击按钮或[可点击文本](dialogs.md#clickable-text)时触发。取消事件会跳过技能，效果相当于此次点击未配置技能。`getButton()` 返回 `dialog.button` 的值，`getValues()` 返回技能会接收到的 `dialog.<key>` 值的可修改映射，包括输入值或可点击文本的参数。

`open` 可以从 Java 打开对话框，将映射条目作为 `dialog.<key>` 值传入。未启用 Premium 或无法识别对话框时返回 `false`：

```java
boolean opened = MythicBukkit.inst().getDialogManager().open(player, "DialogName", Map.of("key", "value"));
```

通过 [API](https://wiki.mythiccraft.io/mythicmobs/API) 创建的自定义技能机制、条件、目标选择器和占位符，也可用于对话框。
