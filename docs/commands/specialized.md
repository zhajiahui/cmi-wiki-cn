---
title: 特殊指令
---

# 特殊指令

## 特殊指令用法

**适用于：等级、计划任务、传送门、EventCommands、交互指令、礼包和自定义别名。**

###### 动作

只使用**一个**动作变量，否则只会采用最后一个。

支持 PlaceHolderAPI 变量。

- **[playerName]**：在能够确定目标玩家时，替换为目标玩家的名称。计划任务无法确定应使用哪位玩家，因此不适用。
- **msg!**：后面指定玩家名称；如果该玩家在线，就向其发送一条普通消息。例如：**msg! Zrips Hello!**
- **broadcast!**：向服务器中的所有玩家发送普通消息，不添加任何额外前缀。
- **actionbar!**：向所有玩家发送此变量后指定的动作栏消息。
- **title!**：向所有玩家发送此变量后指定的主标题消息。
- **subtitle!**：向所有玩家发送此变量后指定的副标题消息。
- **kickall!**：将所有玩家踢出服务器，并显示指定的消息。可用于关闭服务器之前。
- **asPlayer!**：以最初触发这条命令的玩家身份执行命令。
- **asConsole!**：从控制台执行命令。可用于 customAlias 等功能；这些功能若未明确指定从控制台执行，默认会以玩家身份执行命令。
- **asFakeOp!**：以拥有 OP 权限的玩家身份执行命令。它与 asConsole! 略有不同：不会收到任何反馈消息，服务器也会按真实玩家执行的方式处理命令。请注意，执行者并非触发命令的玩家，而是另一位虚拟 OP 玩家。
- **allPlayers!**：对所有在线玩家执行命令。需要插入玩家名称的位置应使用 [allPlayers]。例如：**allPlayers! cmi heal [allPlayers]** 会治疗所有在线玩家。

###### 条件

- **perm:[permissionNode]!**：玩家拥有指定权限节点时才执行命令。无法确定目标玩家时不适用。例如：**perm:cmi.announce.vip! broadcast! Hello vip guys**
- **moneycost:[amount]!**：玩家有足够的金钱时才执行命令。继续执行前，会从玩家余额中扣除指定金额。
- **hasmoney:[amount]!**：检查玩家是否有足够的金钱；足够则继续执行命令，不足则停止。此条件只检查余额，不会扣钱。
- **expcost:[amount]!**：玩家有足够的经验时才执行命令。
- **hasexp:[amount]!**：检查玩家是否有足够的经验；足够则继续执行命令，不足则停止。
- **item:[itemData]!**：玩家有足够数量的指定物品时才执行命令。**请注意**，此条件除了检查物品数量，还会在命令成功时实际扣除这些物品。例如：**item:coal;12!** 要求玩家拥有 12 个煤炭才能执行命令。物品采用单行格式定义，详见[**这里**](icwol.md)。
- **exactitem:[itemData]!**：玩家有足够数量、完全匹配的指定物品时才执行命令。例如：**exact****item:coal;12!** 要求玩家拥有 12 个煤炭才能执行命令。与前一种物品定义不同，此条件要求完全匹配；本例只会选取普通煤炭，带有自定义名称或物品描述的煤炭都会被忽略。
- **hasitem:[itemData]!**：玩家有足够数量的指定物品时才执行命令，执行时不会扣除物品。例如，**hasitem:coal;5** 会检查玩家背包中是否有 5 个煤炭。物品采用单行格式定义，详见[**这里**](icwol.md)。物品定义越详细，匹配结果越准确：只指定物品类型时，会选取所有类型匹配的物品；若还指定了名称，则只选取类型和名称都匹配的物品。
- **hasexactitem:[itemData]!**：玩家有足够数量、完全匹配的物品时才执行命令。与 **hasitem** 不同，此条件只检查完全符合条件的物品。例如，**hasitem:coal;5** 会检查玩家背包中是否有 5 个煤炭，同时排除带有自定义名称或自定义物品描述的煤炭，只识别普通煤炭堆叠。
- **ifonline:[playerName]!**：玩家在线时才执行命令。可按需要使用固定名称或 [playerName]。
- **ifoffline:[playerName]!**：玩家离线时才执行命令。可按需要使用固定名称或 [playerName]。
- **ifempty:[hand/offhand/quickbar/armor/inv/subinv/ender]!**：玩家背包的指定区域为空时才执行命令。**Subinv** 指打开背包后看到的 27 个格子，即 3 行格子。类型为 **inv** 时，会检查玩家背包中的所有物品。**quickbar/maininv/subinv** 类型还可指定额外数值。例如，**maininv-5** 要求主背包有 5 个空格，**subinv-10** 要求背包子区域有 10 个空格，**quickbar-3** 要求快捷栏有 3 个空格。用法示例：**ifempty:maininv-3?!**
- **check:[value1][==|>|>=|<|<=|!=][value2][?][#]!**：只有条件成立时才继续执行。例如，**check:%cmi_user_balance%>1000!** 只在玩家余额大于 1000 时执行命令；**check:%cmi_user_name%==Zrips!** 只在玩家名称为 Zrips 时执行命令。  
  如需与空值比较，可使用“null”或“[empty]”，例如 **check:$1==null!**。  
  **==** 和 **!=** 检查还可使用多个值。例如，**check:$1==join|leave!** 会检查第一个输入的参数是否等于 **join** 或 **leave**；**!=** 的用法相同，但只在参数不等于其中任何一个值时，才执行后续命令。
- **contains:[value1][=>][value2][@][#]!**：只有 value1 包含 value2 时才继续执行。例如，**contains:$1=>stone!** 会检查第一个输入的参数是否包含文本 **stone**；它可以是 stonebricks 等较长单词的一部分。
- **votes:[amount]!**：玩家有足够的投票数时才执行命令（**Votifier**）。

###### 特殊用法

- **cooldown:[timeInSec]!**：为该行及其后的命令（如有）设置再次使用前的冷却时间。例如：**cooldown:5! cmi heal [playerName]** 会治疗玩家，但最多每 5 秒治疗一次。
- **ucooldown:[timeInSec]!**：与前一种冷却不同，此冷却按来源分别计算。因此，不同的 InteractiveCommands 或自定义别名可以有各自的冷却时间。
- **gcooldown:[timeInSec]!**：冷却在全服生效；触发后，任何人都要等到冷却结束才能再次触发。
- **delay! 5**：触发后等待 5 秒，再执行其余命令。例如，可用于在关闭服务器前创建倒计时。也可使用小数，例如：

  ```text
  delay! 0.5
  ```

  将玩家发射 2 次、间隔 2 秒的示例：

  ```text
  - cmi launch [playerName]
  - delay! 2
  - cmi launch [playerName]
  ```

  请注意，玩家将无法运行命令。  
  从 9.1.3.2 版本起，可以为延迟指定一个标识名称，例如：

  ```text
  - cmi launch [playerName]
  - delay! 2 playerlaunch
  - cmi launch [playerName]
  ```

  此名称可用于 **stopdelay:[name]!** 变量。
- **stopdelay:[name]!**：通过上述标识名称取消延迟，例如 **stopdelay:playerlaunch!**。
- **[randomPlayer]**：此占位符可获取一名没有 **cmi.scheduler.exclude** 权限节点的随机在线玩家的名称。可用于在特定时间向随机玩家发放奖励。例如：**cmi give [randomPlayer] diamond %rand/1-5%** 会向一名随机在线玩家发放 1 到 5 个钻石。

## 条件语句

**statement:[value]!**

**if:[value][@][#]!**

这 2 个特殊变量需要搭配使用。

可以用在哪里？用法很简单。  
以下面的配置为例：

```text
    - statement:check1! hasexp:50! hasmoney:100! perm:cmi.command.fly!
    - if:check1! msg! [playerName] PASS
    - if:check1@! msg! [playerName] FAIL
```

第一行有 3 项检查，检查结果会关联到一个自定义名称，本例为“check1”，也可以换成其他名称。后面 2 行使用该检查结果：第一行返回 true 时执行“**if:check1!**”这一行，返回 false 时才执行“**if:check1@!**”这一行。这样只需检查一次，之后直接使用结果，无需重复相同检查，让命令处理更简洁、更快。在此基础上，可以写出更简洁、高效的配置，例如：

```text
    - statement:check1! hasexp:50! hasmoney:100! perm:cmi.command.fly!
    - if:check1! command 1  
    - if:check1! command 2
    - if:check1! command 3
    - if:check1! command 4
    - if:check1@! command 5
    - if:check1@! command 6
    - if:check1@! command 7
```

## 附加用法

- perm:[value][@][?][#]!
- bperm:[value][@][?][#]!
- moneycost:[value][?][#]!
- expcost:[value][?][#]!
- hasmoney:[value][@][?][#]!
- hasitem:[value][@][?][#]!
- item:[value][?][#]!
- hasexp:[value][@][?][#]!
- votes:[value][@][?][#]!
- cooldown:[value][?][#]!
- ucooldown:[value][?][#]!
- gcooldown:[value][?][#]!
- ifonline:[value][?][#]!
- ifoffline:[value][?][#]!
- ifempty:[value][?][#]!
- click:[value][#]!
- ifinworld:[value][@][?][#]!
- ifingamemode:[value][@][#]!
- ifhashealth:[value][@][#]!
- ifhashunger:[value][@][#]!
- ifhasair:[value][@][#]!

以上都是条件检查。也就是说，玩家没有指定权限节点，或金钱、经验不足时，不会执行其后的命令。例如：**perm:cmi.testperm! cmi heal [playerName]**

- 若要在玩家缺少命令所需的权限节点，或金钱、经验不足时向其发送提示，在检查变量中使用 **?**。例如：**perm:cmi.testperm?! cmi heal [playerName]**。玩家没有 **cmi.testperm** 权限节点时，就会收到相关提示，命令也不会执行。
- 若要在玩家不满足要求时取消全部命令，在检查变量中使用 **#**。例如：`- moneycost:150#! cmi heal [playerName]``- cmi feed [playerName]`

  此时，如果玩家账户中没有 150 金钱来支付费用，就既不会被治疗，也不会恢复饥饿值。
- 若要执行当前命令，并取消这一行之后的所有命令，可以使用 **~** 变量。例如：

  ```text
  - check:$1==null~! asConsole! cmi feed [playerName]
  - check:$1==join~! asConsole! cmi heal [playerName]
  - asConsole! cmi msg [playerName] !&4Wrong command!
  ```

  未提供参数时，会执行恢复饥饿值的命令。第一个参数等于“join”时，会治疗玩家，后续命令均不再检查。如果提供了非空且不是“join”的参数，则执行最后一行，输出错误消息。
- 若要检查相反条件，使用 **@**。例如：**perm:cmi.testperm@! cmi heal [playerName]** 只会在玩家**没有** **cmi.testperm** 权限节点时执行命令。
- 若要只在玩家位于特定世界时执行命令，使用 **ifinworld:[value][@][?][#]!** 条件。只有给定世界名称与玩家当前所在世界一致时才执行命令。可以指定多个世界名称，例如 **ifinworld:LT_Craft|LT_Craft_nether!**。使用 **@** 时，则只在给定世界名称与玩家当前所在世界不一致时执行命令。
- 这些附加条件可以按需要用于检查相反条件、向玩家发送提示，以及停止执行后续命令。完整变量可以写成：**perm:cmi.testperm@?#! cmi heal [playerName]**

**bperm:[value][@][?][#]!** 会尝试绕过 CMI 命令的基础权限检查。此功能**仅**适用于 CMI 命令。例如：

```text
bperm:cmi.someCustom! cmi heal
```

这会允许玩家在没有所需的 **cmi.command.heal** 权限节点时执行 **/cmi heal**。可用于限制使用次数的物品等场景：玩家平时没有权限执行某些命令，但使用这些物品时可以执行。

**ptarget:[name]!** 是只能从控制台使用的特殊变量。替换占位符或检查条件时，会以指定玩家为目标。例如，有一个 **/givehomes** 自定义别名，命令如下：

```text
asConsole! ptarget:$1! lp user $1 permission set cmi.command.sethome.%cmi_equationint_{cmi_user_maxperm_cmi.command.sethome_1}+1%
```

之后，就可以从控制台使用 **/givehomes Zrips** 执行命令，利用这些占位符为 **Zrips** 添加新的权限节点。本例会将家数量上限增加一个。

**click:[value]!** 仅适用于交互指令功能中点击方块的情况。**value** 可以是**四个**选项之一：**left, right, leftshift, rightshift**。它规定只有玩家以指定方式点击方块时才执行命令。例如，**click:leftshift!** 只在玩家潜行时按鼠标左键才执行命令。

## 辅助动作

- closeinv!

需要关闭玩家背包时，可以使用此动作。

- ph!

使用此变量时，不会解析已有的占位符，而是将其原样传给命令。可用于执行带有占位符的目标命令，例如：**ph! cmi bossbarmsg all -sec:3 %cmi_server_time_mm:ss%** 会基于此占位符创建动态 Boss 栏消息；如果没有 **ph!**，Boss 栏命令接收到的将是已经解析的占位符值，只会显示静态信息。

- ch!

使用此变量时，不会解析已有的颜色代码，而是将其原样传给命令。可用于执行带有原始十六进制颜色代码的目标命令，例如：**ch! somePlugin coolCommand #000001****Welcome back!** 会按原始格式触发命令，不修改十六进制颜色。如果没有 **ch!**，命令接收到的将是已经解析过的内容，格式可能不符合目标插件的要求。

## 示例

/cmi attachcommand !limiteduse:1!;;asConsole! check:%cmi_random_1_100%<=20! cmi money give [playerName] 100

使用次数为一次的物品，使用时有 20% 的概率获得 100 金钱。

/cmi attachcommand !limiteduse:1!;;asConsole! cmi money give [playerName] %cmi_random_10_50%

一次性物品，使用时随机获得 10 到 50 金钱。

exactitem:coal;160?! asConsole! give [playerName] coal;n{&2Enchanted_Coal} -s

检查是否有 160 个普通煤炭。如果玩家拥有这些物品，就会获得带有自定义名称的新煤炭，同时扣除 160 个普通煤炭。物品数量不足时，会显示反馈消息。

---

[查看原文](https://www.zrips.net/cmi/commands/specialized/)
