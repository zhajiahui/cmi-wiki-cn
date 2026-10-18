![](https://www.zrips.net/wp-content/uploads/2021/07/ctextimage.jpg)

**自定义文本（ctext）功能**可以创建要向玩家显示的任意文本，既可以是简单的带颜色纯文本，也可以包含悬停提示和点击操作。

- 支持 PlaceholderAPI，可自动替换占位符，为每名玩家显示不同的自定义文本。
- 如果你用过 EssentialsX 的 customText 功能，在执行特定命令时显示预设的自定义文本，那么这里的用途相同，但可定制性和功能强上 10 倍。
- 第一，每条命令使用独立文件，便于管理要使用或保留的内容。
- 第二，可以直接在聊天窗口中点击来指定新页面的起点，不必再数 7 行……每页可以有 100 行，也可以只有 1 行，由你决定。
- 第三，支持自动分页。自定义文本超过一页时，会自动出现下一页按钮，点击即可查看下一页。如果不需要，可以为每份自定义文本单独关闭。
- 第四，会自动为新增的自定义文本创建同名命令。例如，默认的 rules 文件会生成 **/rules** 命令，执行后显示规则列表。正式命令为 `/cmi ctext [ctextName] (playerName) (page)`。
- 第五，可以创建原始消息。原始消息支持悬停查看更多信息、点击执行命令，以及点击将文本填入聊天输入框。创建方式很简单：

  ```text
  <T>Your visible Text</T><H>The Hover-over text</H><SC>Suggested Text when you click on it</SC>
  ```

  补充：CMI 的 ctellraw 命令也可以使用这种写法。

```text
<T>Text</T> - 定义要显示的文本
<H>Hover text</H> - 定义鼠标悬停在文本上时显示的内容
<C>cmi heal</C> - 定义点击文本时执行的命令，由玩家执行。
<CC>cmi heal [playerName]</CC> - 定义点击文本时由控制台执行的命令。玩家只能点击执行一次。
<CCI>cmi heal [playerName]</CCI> - 定义点击文本时由控制台执行的命令。玩家可以不限次数地点击执行。
<SC>Suggested text</SC> - 用于替代命令，点击时会将文本填入聊天输入框
<SI>Insertion text</SI> - 与 <SC> 不同，Shift+点击时会向已有文本添加内容，而不会替换原有文本
<URL>www.google.com</URL> - 添加网址链接
同一行中需要包含多条原始消息时，用 <Next> 分隔
原始消息必须以 <T> 开头
```

- 第六，以上内容都可以**在游戏内**通过 `/cmi editctext` 编辑。可以创建新的自定义文本、编辑文本行、添加新页面、删除旧页面，以及开启或关闭别名和自动分页（详见下方标记说明）。点击专用箭头即可调整行的顺序。也就是说，可以完全在游戏内创建和管理自定义文本，无需直接编辑文件。因此，管理员或其他管理人员无需直接访问服务器文件，也能编辑或创建美观的帮助页面。
- 可以用这个功能为自己的服务器创建专用帮助页面，加入可点击的文本行或悬停时显示的补充信息，并通过简单的别名系统访问这些页面。
- 还可以执行 `/cmi getbook [cTextName] (playerName)`，将自定义文本转换成书。所有悬停提示和可点击消息都会自动包含在书中。

例如，要创建一行显示为“Hello there!”的文本，鼠标悬停时显示“Hi!”，点击后为玩家治疗一次，可以这样写：

```text
<T>Hello There!</T><H>Hi!</H><CC>cmi heal [playerName]</CC>
```

如果想在同一行中放置多个带悬停提示的文本片段，只需重复相应写法，并用同一个变量标记下一个片段：

```text
<T>Section One</T><H>Hover for section one<H><SC>Suggested text</SC><Next><T>Second section</T><Next><T>Third section</T><H>With hover message</H>
```

可以使用常规格式的颜色代码。

## 图片

![](https://www.zrips.net/wp-content/uploads/2021/07/ctextimage.jpg)

从 9.0.2.0 版本起，可以使用图片功能，添加玩家头像等图片，并在旁边显示文本。目前仅适用于 1.16+ 服务器。

例如，在自定义文本文件中使用以下配置，就能得到上图所示的效果。

```text
<AutoPage>
------------------------------------------
img:helmet:[playerName] 8
imgtext:
imgtext:
imgtext: {#gray}Welcome %cmi_user_display_name%{#gray}!
imgtext: <T>{#gray}Money balance: &f%cmi_user_balance_formatted%</T><H>{#green}Click</H><C>cmi balance</C>
imgtext: <T>{#gray}Mail: &f%cmi_user_mail_count% </T><H>{#green}Check mail</H><C>cmi mail</C><T>{#gray}Warnings: &f%cmi_user_warning_count%</T>
------------------------------------------
```

可以在图片前后添加文本，也可以同时在图片旁边显示文本。图片旁边的文本必须使用 **imgtext:** 变量，并紧接在 **img:** 后面，否则不会被识别。如果需要，也可以添加多张图片。

使用 **img:head:[playerName]** 可以显示玩家皮肤的头部图像，仅显示皮肤的基础层。  
使用 **img:helmet:[playerName]** 则会同时显示玩家皮肤的头部附加层。  
还可以使用本地文件中的实际图片，例如 **img:diamond.png**。文件必须放在 ~/plugins/CMI/**Images** 文件夹中。  
未指定尺寸时，图片默认高度为 8 像素，这可以基本防止尝试显示 4k 图片。可以提供尺寸来调整图片大小，例如 **img:diamond.png 8 10**，无论原图多大，都会生成 8×10 像素的图片。两个参数均为可选；只提供一个时，会自动按原图比例缩放另一个。第一个参数指定高度，第二个指定宽度。如果只想固定宽度，可以将高度设为 0，例如 **img:diamond.png 0 12**。这样会始终保持 12 像素宽，并根据原图比例缩放高度。

还可以添加悬停提示，甚至点击操作，让显示效果美观、紧凑。

## .txt 分页

创建自定义文本文件时，可以在顶部首行使用 `<AutoPage>`，并在需要的位置设置分页；游戏中会自动显示页码和 **<pref | next >** 按钮。
从 CMI 9.3.2.0 版本起，可以自定义这些按钮的显示内容：在紧接着的下一行添加 `<pageLabel:Something>`，即可将 **Next** 替换为 **Something**。
这里支持颜色代码，包括十六进制颜色代码。
例如：

```text
This is text on page one. 
<NextPage>
<pageLabel:{#gold}Mobs>
This text is about Minecraft animals. 
<NextPage>
<pageLabel:{#gold}Flowers>
You can find flowers in many different biome types.
```

显示效果如下：![](https://www.zrips.net/wp-content/uploads/2023/03/Screen-Shot-2023-03-08-at-19.50.22.png)

![](https://www.zrips.net/wp-content/uploads/2023/03/Screen-Shot-2023-03-08-at-19.50.37.png)

## .txt 标记说明

为避免出错，建议**使用游戏内编辑器：  
`/cmi editctext`**。  
如果确实需要，也可以直接编辑 **CustomText/** 文件夹中的 **.txt** 文件。文件首行或其他位置可能会出现一些特殊标记。这些标记可以通过游戏内编辑器切换，下面会说明它们的作用。

在 CustomText/ 文件夹中添加、删除或编辑 .txt 文件后，必须执行 `/cmi reload`。

如果不想让玩家使用 ctext 命令，可以在权限管理插件中将对应权限设为否定，再创建符合需要的自定义别名，包括以控制台身份为指定玩家打开 ctext 文件的任意页面。  
例如，`asConsole! cmi ctext mobs [playerName] 3` 会为输入该自定义别名命令的玩家打开 mobs.txt 的第 3 页。

**标记说明：**

```text
<AutoAlias> - 如果文件名为 meow，会自动创建 /meow 命令来显示这份文本
<AutoPage> - 自动将 <nextpage> 转换为页码
<Hidden> - 玩家执行 /cmi ctext [tab] 时不显示
<ReqPermission> - 需要拥有权限才能查看或使用

<nextpage> - 将文本分段，指定下一页的起点
<pageLabel:{#hex}text> - 用 Text 替换默认的 Next，支持十六进制颜色

如果想创建自己的欢迎信息 /motd、/help 命令、带分页的 /rules 规则说明，或为 /jobs help、/mcmmo help、/skyblock help 等功能创建自定义信息页面，自定义文本文件很适合这些用途。
```
