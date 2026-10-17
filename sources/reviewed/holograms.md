![](https://www.zrips.net/wp-content/uploads/2026/04/2026-04-02_13-02-17.gif)![](https://www.zrips.net/wp-content/uploads/2026/04/2026-04-02_13-22-57.gif)

![](https://www.zrips.net/wp-content/uploads/2026/04/2026-04-02_13-08-23.gif)![](https://www.zrips.net/wp-content/uploads/2026/04/2026-04-02_13-53-36.gif)

![](https://www.zrips.net/wp-content/uploads/2020/05/2020-05-15_13-22-37.gif)![](https://www.zrips.net/wp-content/uploads/2021/07/Nian.gif)

## 简介

**从 9.6.2.0 版本起，1.20+ 服务器上的全息图默认使用改进后的新显示方式。本页大多数示例都采用这一新系统。**

**CMI 的全息图功能**可以在空中显示文字或图标。

还可以创建可点击的全息图，让玩家点击后以玩家或控制台身份执行任意命令。

全息图完全通过数据包实现，其中的物品仅存在于客户端，因此不会被第三方插件清除。

游戏内编辑器可以添加、编辑和删除全息图的行，启用点击交互，将全息图移到你所在的位置，或微调其位置，还能调整激活范围、更新范围等设置。

全息图支持 [PlaceholderAPI](https://www.spigotmc.org/resources/6245/)，可以显示其他插件提供的信息，也可以向不同玩家显示不同内容。添加行时可以使用 `%cmi_user_name%` 等变量。完整变量列表见 [zrips.net/cmi/placeholders](https://www.zrips.net/cmi/placeholders/)。

全息图可以包含多个页面，在需要时切换显示。本页提供了分页设置示例。

可以按需设置全息图各行的更新间隔；无需频繁更新时，这样有助于节省服务器资源。

玩家离全息图太远时，全息图会隐藏，以减轻客户端负担；只有玩家在附近时，全息图才会更新。

全息图的行中也可以使用图标，进一步自定义显示内容。

玩家无法直接看到全息图时，可以将其隐藏。这样，墙后或其他楼层的全息图就不会显示，有助于减轻 Minecraft 处理不佳造成的客户端 TPS 下降。

### 示例

![](https://www.zrips.net/wp-content/uploads/2023/07/HologramExample4.jpg)![](https://www.zrips.net/wp-content/uploads/2023/07/HologramExample3-767x1024.jpg)![](https://www.zrips.net/wp-content/uploads/2023/07/HologramExample2.jpg)

![](https://www.zrips.net/wp-content/uploads/2026/04/HologramPlaytimeTop-677x1024.png)![](https://www.zrips.net/wp-content/uploads/2023/07/HologramExample1.jpg)

###### 主窗口

![](https://www.zrips.net/wp-content/uploads/2026/04/Hologram_MainWindow.png)

###### 动画窗口

![](https://www.zrips.net/wp-content/uploads/2026/04/Hologram_AnimationWindow.png)

###### 位置调整

![](https://www.zrips.net/wp-content/uploads/2026/04/Hlogram_LocationWindow.png)

###### 交互设置

![](https://www.zrips.net/wp-content/uploads/2026/04/Hologram_InteractionsWindow.png)

## 创建全息图

使用 `/cmi hologram new [name]` 创建全息图。例如，要创建名为 **head** 的全息图，执行 `/cmi hologram new head`。也可以直接执行 `/cmi hologram`，再点击 **[+]** 开始创建。

点击绿色的 **[+]**，然后在聊天栏中输入这一行要显示的内容，即可逐行添加文字。也可以看着全息图执行 `/cmi hologram aimlines`，快速打开所看全息图的行编辑器。

点击 **`<Open settings GUI>`** 打开设置界面，可以调整更新频率、更新范围、启用点击交互，或将全息图移到新位置。也可以看着要编辑的全息图执行 `/cmi hologram aimgui`。

![](https://www.zrips.net/wp-content/uploads/2022/10/HologramLinesInterface.png)

执行 **`/cmi hologram`** 可以查看所有全息图，列表会按*与你当前位置的距离*排序，离你最近的排在最前面。点击全息图名称即可开始编辑。

## ICON:[value]

每行只能放置一个图标。

浮动图标仅适用于 1.10+ 服务器。使用新的显示方式（1.20+ 服务器）时，`ICON` 和 `SICON` 都会显示为相同的静态图标。

基本语法：`ICON:[itemName/id]:[data]`

**示例：**  
`ICON:stone` 会显示一个浮动的石头图标，`ICON:stone:3` 则会显示浮动的闪长岩图标。  
`ICON:head:[playerName]` 会显示指定玩家的头颅。  
`ICON:head:%cmi_user_name%` 会显示正在看这个全息图的玩家的头颅。  
`ICON:head:base64` 会显示使用自定义 Base64 皮肤的头颅；皮肤数据可以从 minecraft-heads.com 等网站获取，就是那一长串字符。  
`ICON:Stone%enchanted%` 会显示带附魔效果的图标，在现有语法末尾加上 `%enchanted%` 即可。发光图标的用法相同，只需将 `%enchanted%` 换成 **`%glowing%`**。  
`ICON:Stone-64` 会显示一叠物品；在语法后加上 `-` 和数量即可指定堆叠数量。  
`ICON:%itemInHand%` 可以将玩家手持的物品显示为图标。

要显示带自定义模型数据的图标，在语法末尾加上 **`%customModelData:[id]%`**，例如 **`ICON:bow%customModelData:4%`**。使用这种格式可以实现下图中的效果：

`ICON:materialName%customModelData:[id]%` 会显示带自定义模型数据的图标。在现有语法末尾加上 **`%customModelData:[id]%`** 即可，例如 **`ICON:bow%customModelData:4%`**，效果如下：

![](https://www.zrips.net/wp-content/uploads/2020/04/customdatahologram-134x300.jpg)![](https://www.zrips.net/wp-content/uploads/2022/10/HologramCustomModelDataIcons-84x300.png)

## SICON:[value]

显示一个不会上下浮动的静态图标。

静态图标与浮动图标的语法相同，只需将开头的 **`ICON`** 换成 **`SICON`**。

## 全息图背板

从 9.8.6.0 版本起，可以在全息图后方添加**背板（Board）**。

![](https://www.zrips.net/wp-content/uploads/2026/04/Hologram_Board.png)

背板可以让全息图具有一定厚度。通常可以使用任意方块，并调整其缩放、偏移和旋转。注意，每个坐标轴向两侧的旋转角度均限制在 90 度以内。增加背板厚度会将文字向前移动，交互平面也会随之移动，但仅对正面生效。

## 动画

全息图主要支持两类动画：淡入淡出，以及绕自身轴线自动旋转。  
淡入和淡出的时长以 tick 为单位，决定全息图出现或消失需要多久。默认立即显示或隐藏；设为 5 tick 等数值后，可以得到下图中的效果。

![](https://www.zrips.net/wp-content/uploads/2026/04/2026-04-02_14-48-07.gif)

虽然变化不大，但能让全息图出现在玩家面前时更平滑。

绕自身轴线旋转可以让全息图自动转动，效果如下：

![](https://www.zrips.net/wp-content/uploads/2026/04/2026-04-02_13-02-17.gif)

注意，这个示例并没有使用特殊功能，而是将全息图复制成 3 个，各自的偏航角偏移相差 120 度，从而形成这种视觉效果。旋转以全息图的原点为中心；将整个全息图偏移后，看起来就像是在绕另一个位置旋转。

## 可点击的全息图

全息图默认**不接受点击交互**。需要在每个全息图的设置界面中点击**木棍（Stick）**图标，分别开启。

点击**弓（Bow）**图标可以设置点击后执行的命令，支持[专用命令格式](https://www.zrips.net/cmi/commands/specialized/)。这里设置的是全局命令，点击全息图交互区域的任意位置都会执行。要根据玩家点击的具体文字执行不同命令，需要使用 CText 格式。例如，将某行设为 **`<T>Click Me</T><C>cmi heal [playerName]</C>`**，玩家点击这段文字时就会执行其中的命令。点击 CText 文字时，只执行 CText 中定义的命令，覆盖全局命令；点击其他位置时则执行全局命令。同一行可以放置多段可点击文字，重复添加即可，例如 `<T>Heal Me!</T><C>cmi heal [playerName]</C><T> Feed Me!</T><C>cmi feed [playerName]</C>`。使用 CText 时要注意，文字宽度是估算的。客户端资源包和所用字体会影响文字的实际边界，插件无法准确获知这些边界，因此检测位置可能出现偏差。默认检测以 Minecraft 默认字体为准，也可以在设置界面中调整检测区域。为了让检测尽量准确，标记出的区域（蓝色点）应从一端到另一端覆盖整段文字，包括不可点击的部分。插件会根据文字内容自动估算区域，但使用变量时可能不够准确，需要按实际情况调整。

另外，检测依赖玩家的视线方向和位置，因此转动视角后，全息图的响应可能会有约 0.25 秒延迟。虽然时间很短，看起来仍可能有些卡顿。这是游戏本身的运行方式造成的，目前没有太多调整余地。

![](https://www.zrips.net/wp-content/uploads/2026/04/Hologram_interactionArea.png)

点击**纸（Paper）**图标，可以开关玩家点击全息图时显示的特殊粒子效果。该效果默认开启。

## 悬停效果

从 CMI 9.1.2.x 起，插件可以检测玩家的视线是否停留在全息图上，并显示粒子效果，或改变玩家正在注视的那一行文字。

悬停效果使用与[自定义文本](https://www.zrips.net/cmi/custom-text/)相同的格式，但有一些限制。

支持文字、悬停文字和命令变量，也支持[专用命令格式](https://www.zrips.net/cmi/commands/specialized/)。

支持以下变量：

**`<T>Text</T>`** — 设置要显示的文字。  
**`<H>Hover-over text</H>`** — 设置视线停留在这一行时显示的文字。  
**`<C>cmi heal</C>`** — 设置点击这一行时由控制台执行的命令。

如果 CText 中包含命令，但没有设置悬停部分，插件会自动为普通状态和悬停状态添加不同的文字颜色，颜色可以在设置界面中修改。只有 CText 包含命令时才会自动添加颜色；如果只想改变悬停效果而不执行命令，就需要手动设置。

例如，可以做成下面这样：

```text
<T>{#gray>}Free heal{#edward<}</T><H>{#edward>}&lFree heal{#gray<}</H><C>asConsole! gcooldown:3?! cmi heal [playerName]</C>
```

多条命令之间用 `;;` 分隔。  
可以同时设置点击全息图任意行时执行的命令，以及点击特定行时执行的另一条命令。

在全息图设置界面中点击**绿色地毯（Green Carpet）**图标，可以*关闭*悬停粒子。

点击它下方的图标，可以更换粒子类型。

点击**橡木栅栏（Oak Fence）**图标，可以调整悬停粒子的数量。

点击**红砖墙（Brick Wall）**和**石砖墙（Stone Brick Wall）**图标，可以调整粒子的额外高度、宽度和偏移。

交互区域的大小和相对位置都可以调整。注意，双面全息图启用背板后，背板的厚度可能导致背面的悬停位置检测不准，因为出于效率考虑，插件只检测一个平面。因此，应使用较薄的背板，或避免给较厚的双面全息图添加点击交互。

## **创建分页**

默认情况下，所有文字都在同一页。

要**创建**下一页，新增一行，并将内容设为 `!nextpage!`。

玩家最初只会看到第一页，也就是第一个 **`!nextpage!`** 之前的内容。

执行 `/cmi hologrampages [holoName] (playerName) (next/prev/[pageNumber])` 可以切换玩家正在查看的页面。

每位玩家看到的页面互相独立。

页数没有限制，但游戏内编辑器一次能显示的行数有限，页数多时管理起来可能会比较麻烦。

例如，**创建**一个名为 **Rules** 的全息图，并添加以下各行：

```text
Line 1
Line 2
Line 3
!nextpage!
Line 4
Line 5
```

接着，点击聊天栏中的 **`<Open settings GUI>`** 打开设置界面，点击木棍图标启用交互，再点击**书（Book）**图标，开启自动分页按钮。按钮会显示在全息图底部，玩家点击即可切换页面。也可以自行添加导航按钮：新增一行，输入 **`<T><<<< </T><C>[prevPage]</C><T> >>>></T><C>[nextPage]</C>`**。其中，**`[prevPage]`** 和 **`[nextPage]`** 是特殊变量，点击时会切换当前全息图的页面。

## **点击类型**

可交互的全息图支持以下 5 种点击类型：

`click:left!` — 仅在玩家未潜行并左键点击时执行命令。  
例如：**`click:left! cmi heal [playerName]`**。

`click:leftshift!` — 仅在玩家潜行并左键点击时执行命令。

`click:right!` — 仅在玩家未潜行并右键点击时执行命令。  
例如：**`click:right! cmi feed [playerName]`**。

`click:shiftright!` — 仅在玩家潜行并右键点击时执行命令。

*不指定上述类型* — 任意点击方式都会触发命令。

## 其他设置

###### 适用于 1.20+ 服务器

**显示方式（Display method）** — 1.20+ 服务器默认使用新的显示方式；旧版本服务器只能使用旧方式。1.20+ 服务器可以选择新旧两种方式，但强烈建议使用新方式，因为它对服务器和客户端都更高效。也可以给玩家 **`cmi.hologram.seeold`** 权限，让该玩家看到旧式全息图，适用于有玩家使用旧版客户端、不支持新式全息图的情况。不过，旧式全息图的限制更多，应避免调整缩放、偏移等设置，因为这些设置在旧式全息图上的效果并不相同。默认情况下，新旧两种全息图的尺寸应该一致。

**启用（Enabled）** — 如果不再想向玩家显示某个全息图，可以将其禁用。也可以开启查看权限要求，将它对其他玩家隐藏，同时仍允许工作人员或指定玩家查看和交互。

**跟随方式（Follow type）** — 可选 `Fixed`、`Vertical`、`Horizontal`、`Center`。`Vertical` 模式下，全息图会绕 Y 轴旋转，始终朝向玩家。`Fixed` 模式始终朝向同一方向，可以手动调整方向或通过动画改变。`Horizontal` 模式会沿 X 轴跟随玩家。`Center` 模式始终正对玩家。

**双面显示（Double sided）** — 仅在跟随方式设为 `Fixed` 或 `Horizontal` 时可用。启用后会生成全息图的背面，让正反两面都可见。

**文字对齐（Text alignment）** — 可选 `Center`（居中）、`Left`（左对齐）、`Right`（右对齐）。

**文字阴影（Text shadow）** — 开启或关闭文字阴影。

**文字透明度（Text Alpha）** — 用 0 到 255 之间的值设置文字透明度。

**文字宽度（Text width）** — 设置文字自动换行前的宽度。如果全息图需要交互，应避免一行文字自动折成多行，否则可能影响交互检测。

**文字补齐（Text filler）** — 设置用空格补齐后要达到的行宽，可用于排行榜等需要让两侧文字对齐的内容。在全息图的行中使用 `%filler%`，即可自动填入空格，补足到指定宽度。

**文字穿透显示（Text seethrough）** — 允许隔着方块看到全息图文字，仅对文字部分生效。如果与**背板（Board）**配合使用，可以让文字只在隔着方块看时才可见。

**亮度（Light levels）** — 设置全息图的亮度，可以覆盖世界中的光照亮度。设为 -1 时会自动调整。

**背景颜色（Background color）** — 设置背景的基础颜色。

**背景透明度（Background alpha）** — 设置背景透明度，取值为 0 到 255。

**整体偏移、方向和缩放（Base offset, direction, scale）** — 设置全息图的整体位置、缩放和方向，同时影响背板、文字和图标。

**启用背板（Board enabling）** — 在全息图后方生成类似方块的背板。为了获得更好的显示效果，建议启用背板时将背景透明度设为 0。

**背板缩放、方向和偏移（Board scale, direction and offset）** — 调整背板的位置、缩放和方向，与全息图其他部分的设置相互独立。

**背板材质（Board material）** — 可以使用任意方块类型的材质。

**图标缩放、方向和偏移（Icon scale, direction and offset）** — 统一调整全息图中所有图标。

使用盔甲架的全息图：

**视线检测（Line of sight）** — 设置全息图被方块遮挡时是否隐藏，仅适用于旧式全息图。

## 位置与范围设置页

**更新范围（Update range）** — 玩家进入此范围后，全息图的各行才会更新，单位为方块。范围以全息图原点为中心，按球形计算。

**显示范围（Show range）** — 玩家进入此范围后，全息图的各行才会显示，单位为方块。范围以全息图原点为中心，按球形计算。

**需要权限（Permission required）** — 设置玩家是否必须拥有 **`cmi.hologram.[hologramname]`** 权限才能看到全息图。

提示：使用 `&u` 可以让这一行每次更新时随机更换颜色。

## 交互设置页

全息图的交互默认关闭，只有需要与全息图交互时才应开启。

**显示悬停粒子（Show hover particles）** — 开启或关闭可交互全息图周围的粒子。主要用于在玩家看向可点击全息图时，提供直观提示。

**粒子数量（Particles）** — 设置生成的粒子数量。默认情况下，粒子会沿全息图边缘顺时针移动；数量大于一个时，所有粒子会沿全息图周边等距分布。

**粒子类型（Particle type）** — 可以通过专用的界面编辑器选择任意粒子，并设置其自定义选项。

**粒子间距（Particle spacing）** — 粒子每 tick 生成一次，并沿全息图周边移动设定的距离。可以使用负值，让粒子反向“移动”。

**粒子缩放和偏移（Particle scale and offset）** — 设置显示粒子的平面。它与交互平面相互独立，可以按需更准确地调整粒子的移动路径。

**启用分页按钮（Enable pagination buttons）** — 自动在全息图底部添加分页按钮，点击即可切换页面。仅在全息图有多页时生效。

**命令（Commands）** — 设置点击全息图任意位置时执行的全局命令。

**显示粒子（Show particles）** — 显示或隐藏点击全息图时的粒子，仅影响全局命令。CText 命令使用配置文件中的粒子预设，不受此项影响。

**交互区域大小和偏移（Interaction size and offset）** — 编辑时会显示几个蓝色点，标出交互区域。如果自动检测的区域不准确，可以手动调整，让它贴合现有文字。区域边界应刚好覆盖文字两端，不要超出，这样可以提高悬停检测的准确度，尤其适用于使用 CText 设置了可点击文字片段的情况。

**普通和悬停前缀（Base and Hover prefix）** — 为包含命令的 CText 行设置颜色代码。插件会自动在可点击文字前添加普通状态和悬停状态各自的颜色代码，方便设置悬停时只改变颜色的可点击文字。

## 动画设置页

**翻页间隔（Page change interval）** — 设置全息图自动翻页的间隔，单位为秒。如果玩家手动翻页，会跳过一次自动翻页。

**更新间隔（Update interval）** — 设置全息图各行的更新间隔，单位为秒。文字为静态内容时，将更新间隔设为 **0**。可交互的全息图可以跳过这一间隔，在需要时更新文字，不受实际更新间隔限制。

**自动旋转（Auto rotate）** — 设置每 tick 改变的偏航角度数。可以设为负值，让全息图逆时针旋转。

**淡入（Fade In）** — 设置全息图显示出来需要的 tick 数。数值越大，出现得越慢；设为 0 时立即出现。

**淡出（Fade out）** — 与淡入相同，但用于全息图消失时的效果。

## 图片与动画

![](https://www.zrips.net/wp-content/uploads/2021/07/Nian.gif)![](https://www.zrips.net/wp-content/uploads/2021/07/hologramimage.jpg)

从 CMI 9.0.2.0 起，可以通过全息图添加图片，或制作简单动画。  
注意，透明像素会用 **`_|`** 填充，以保持每行的间距。

添加图片时，使用以下格式之一：

`img:helmet:[playerName]` 会显示包含外层贴图的玩家头部图像，例如 `img:helmet:Zrips`。目前不支持使用动态玩家名。

`img:head:[playerName]` 会显示不含外层贴图的玩家头部图像，例如 `img:head:Zrips`。目前不支持使用动态玩家名。

最后一种方式是指定 **`CMI/Images`** 文件夹中的图片路径，例如 `img:diamond.png`。

图片的原始尺寸不一定符合需求，可以添加 2 个额外参数来调整大小。

使用 `img:diamond.png 12` 可以将图片高度设为 12 像素，宽度则会根据原图尺寸自动按比例缩放。

使用 `img:diamond.png 6 6` 可以同时指定高和宽，无论原图多大，都会显示为 *6×6*。

如果只想设置宽度，让高度自动缩放，可以将高度设为 *0*。例如，`img:diamond.png 0 9` 会将图片*宽度*设为 *9* 像素，*高度*则根据原图尺寸*自动*按比例缩放。

如果没有指定，图片**默认**为 *8* 像素高。

Nyan Cat 的基础示例：

```text
  PageInterval: 0.1
  Range: 46
  RangeExtra: 46
  Spacing: 0.25
  SpacingIcon: 0.5
  Lines:
  - img:nian/0.gif 32
  - '!nextpage!'
  - img:nian/1.gif 32
  - '!nextpage!'
  - img:nian/2.gif 32
  - '!nextpage!'
  - img:nian/3.gif 32
  - '!nextpage!'
  - img:nian/4.gif 32
  - '!nextpage!'
  - img:nian/5.gif 32
```

RAR 压缩包可以从[这里](https://www.zrips.net/wp-content/uploads/2021/07/nian.rar)下载。

**注意！** 使用旧的盔甲架显示方式时，避免创建超过 100 行的全息图。服务器可以处理更大的全息图，甚至可以处理动画，但客户端承受不了。

## 编辑或删除全息图

执行 `/cmi hologram`，即可按*与你的距离*从近到远列出全息图。

点击全息图名称前的红色 `X` 即可**删除**该全息图。*删除后无法撤销。*

要**编辑**全息图，点击其名称打开设置。顶部会显示“*`<Open settings GUI>`*”，点击即可打开设置界面。下方会列出该全息图的各行，点击某一行即可编辑，也可以点击行前的红色 `X` 将其删除。

## 便捷命令

**`/cmi hologram aimgui`** — 打开当前所看全息图的设置界面。

**`/cmi hologram aimlines`** — 打开当前所看全息图的行编辑器。

**`/cmi hologram lastgui`** — 打开上次编辑的全息图的设置界面。

**`/cmi hologram lastlines`** — 打开上次编辑的全息图的行编辑器。

## 保存文件示例

#### 在线时长排行榜

![](https://www.zrips.net/wp-content/uploads/2026/04/HologramPlaytimeTop-198x300.png)

```text
topplaytime:
  Loc: LT_Craft;457.9;156.22;996.6
  Board:
    Enabled: true
    Dimensions: 4;2.8;1.21
    Material: ACACIA_SHELF
    Direction: 180;0;0
    Offset: 0;0;0.98
  Text:
    Shadow: false
    BAlpha: 0
  Settings:
    Interval: 600
  Lines:
  - '{#73C144}&l&nᴛᴏᴘ 10 ᴘʟᴀʏᴛɪᴍᴇ'
  - <head:%cmi_playtimetop_cname_1%:false> {#73C144}1. {#E7E7E7}%cmi_playtimetop_name_1%%filler%&r
    {#E7E7E7}%cmi_playtimetop_time_1%
  - <head:%cmi_playtimetop_cname_2%:false> {#73C144}2. {#E7E7E7}%cmi_playtimetop_name_2%%filler%&r
    {#E7E7E7}%cmi_playtimetop_time_2%
  - <head:%cmi_playtimetop_cname_3%:false> {#73C144}3. {#E7E7E7}%cmi_playtimetop_name_3%%filler%&r
    {#E7E7E7}%cmi_playtimetop_time_3%
  - <head:%cmi_playtimetop_cname_4%:false> {#73C144}4. {#E7E7E7}%cmi_playtimetop_name_4%%filler%&r
    {#E7E7E7}%cmi_playtimetop_time_4%
  - <head:%cmi_playtimetop_cname_5%:false> {#73C144}5. {#E7E7E7}%cmi_playtimetop_name_5%%filler%&r
    {#E7E7E7}%cmi_playtimetop_time_5%
  - <head:%cmi_playtimetop_cname_6%:false> {#73C144}6. {#E7E7E7}%cmi_playtimetop_name_6%%filler%&r
    {#E7E7E7}%cmi_playtimetop_time_6%
  - <head:%cmi_playtimetop_cname_7%:false> {#73C144}7. {#E7E7E7}%cmi_playtimetop_name_7%%filler%&r
    {#E7E7E7}%cmi_playtimetop_time_7%
  - <head:%cmi_playtimetop_cname_8%:false> {#73C144}8. {#E7E7E7}%cmi_playtimetop_name_8%%filler%&r
    {#E7E7E7}%cmi_playtimetop_time_8%
  - <head:%cmi_playtimetop_cname_9%:false> {#73C144}9. {#E7E7E7}%cmi_playtimetop_name_9%%filler%&r
    {#E7E7E7}%cmi_playtimetop_time_9%
  - <head:%cmi_playtimetop_cname_10%:true> {#73C144}10. {#E7E7E7}%cmi_playtimetop_name_10%%filler%&r
    {#E7E7E7}%cmi_playtimetop_time_10%
```

#### 多页示例

![](https://www.zrips.net/wp-content/uploads/2026/04/2026-04-02_13-53-36-300x225.gif)

```text
holopages:
  Loc: LT_Craft;474.34;153.9;989.9
  Board:
    Enabled: true
    Dimensions: 0.82;0.12;0.04
    Direction: 90;0;0
  Interaction:
    Particle:
      Spacing: 0.04
      Effect: Trail;8;{#FFFFFF}
      Count: 6
      Dimension: 0.28;0.02
    HoverPrefix: '&7&n'
    Enabled: true
    Dimension: 0.33;0.01
  Animation:
    In: 5
    Out: 5
  Text:
    Align: LEFT
    BAlpha: 0
    Double: true
  Page:
    Auto: true
  Settings:
    Dir: 0;90;0
    Range:
      Visual: 16
  Lines:
  - '{#f7d486}Ah, a new face.'
  - '{#f7d486}That’s a rare sight around here.'
  - '{#f7d486}Most folks pass through'
  - '{#f7d486}without really seeing the place.'
  - '!nextpage!'
  - '{#f7d486}If you’ve got time, stay a while.'
  - '{#f7d486}There’s more here than it first shows'
  - '{#f7d486}just have to know where to look.'
```

#### 显示物品价值并点击全息图出售

![](https://www.zrips.net/wp-content/uploads/2026/04/2026-04-02_13-22-57-300x225.gif)

```text
Worth:
  Loc: LT_Craft;444.12;154.24;995.73
  Board:
    Enabled: true
    Dimensions: 0.8;0.7;0.01
    Material: BLACKSTONE
    Offset: 0;-0.31;0
  Interaction:
    Particle:
      Effect: Dolphin
    Commands:
    - asConsole! cmi sell hand [playerName]
    Enabled: true
    Dimension: 0.95;1.38
    Offset: 0.95;1.38
  Text:
    Shadow: false
    BAlpha: 0
    Double: true
  Icon:
    Scale: 1.5;1.5;2
    Offset: 0;-0.32;0
  Settings:
    Scale: 1.1;1.1
    Range:
      Update: 16
      Visual: 16
    Interval: 1
  Lines:
  - '&r {#gray} %cmi_iteminhand_displayname% {#white}x %cmi_iteminhand_amount% &r'
  - '{#gray}Worth:{#white} %cmi_iteminhand_worth%'
  - ICON:%iteminhand%
```

#### 悬停检测测试

![](https://www.zrips.net/wp-content/uploads/2026/04/2026-04-02_13-08-23-300x225.gif)

```text
grid:
  Loc: LT_Craft;430.08;153.72;995.43
  Interaction:
    Enabled: true
    Dimension: 0.21;0
  Lines:
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
  - <T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi heal</C><T>⬛</T><C>cmi
    heal</C><T>⬛</T><C>cmi heal</C>
```
