## **░ 目录** <A NAME="table_contents">
#### 常见问题
* <A HREF="#flexibility">如何在其他插件中使用 CrackShot 武器？（套装、竞技场、商店、职业等）</A>
* <A HREF="#permissions">已经配置权限文件，为什么玩家仍能使用所有武器？</A>
* <A HREF="#config">修改配置后，为什么武器不再显示？</A>
* <A HREF="#pls">可以添加〈在此填写武器名称〉吗？</A>

## **░ 在其他插件中使用 CrackShot 武器** <A NAME="flexibility">
#### 方法 1 - Skip_Name_Check 节点
使用 <a href="https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#skip_name_check" target="_blank">Skip_Name_Check</a> 节点，可以将特定物品 ID 的物品转换成 _CrackShot_ 武器。

用法示例：

    Item_Type: 264~10
    Skip_Name_Check: true

服务器上所有物品 ID 为 `264:10` 的物品，都会自动转换成这把 _CrackShot_ 武器。因此，通过其他插件给予玩家 `264:10` 即可。

#### 方法 2 - Enchantment_To_Check 节点
使用 <a href="https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#enchantment_to_check" target="_blank">Enchantment_To_Check</a> 节点，可以将拥有指定附魔的物品转换成 _CrackShot_ 武器。

用法示例：

    Item_Type: 264
    Enchantment_To_Check: SILK_TOUCH-2

服务器上所有物品 ID 为 `264`、同时具有_精准采集 II_ 附魔的物品，都会自动转换成这把 _CrackShot_ 武器。因此，通过其他插件给予玩家具有_精准采集 II_ 的_钻石_（ID: 264）即可。

#### 方法 3 - CrackShot API
插件开发者如果想直接支持 _CrackShot_ 武器，可以[接入 _CrackShot_](https://github.com/Shampaggon/CrackShot/wiki/Hooking-into-CrackShot)，通过 _giveWeapon_ 函数直接给予玩家武器。

#### 方法 4 - CrackShot 命令
如果用于生成 _CrackShot_ 武器的插件支持命令，例如 _BuyCraft_ 或 _CommandSigns_，可以使用 [_CrackShot_ 的 give 和 get 命令](https://github.com/Shampaggon/CrackShot/wiki/Commands-and-Permissions)给予玩家武器。

## **░ 配置权限** <A NAME="permissions">
如[命令与权限](https://github.com/Shampaggon/CrackShot/wiki/Commands-and-Permissions)页面所述，以下权限默认授予_所有_用户：

* crackshot.use.all
* crackshot.craft.all
* crackshot.buy.all

因此，如果想指定玩家可以使用、合成或购买哪些武器，必须先_撤销_这些节点。大多数权限插件可以使用短横线 `-` 表示否定权限。

权限配置示例：

    permissions:
    - -crackshot.use.all
    - crackshot.use.deagle
    - crackshot.use.python

以上配置只允许用户使用默认武器 _Desert Eagle_ 和 _Python_。如果没有撤销所有玩家默认拥有的 `crackshot.use.all` 权限，玩家就仍然可以使用全部 _CrackShot_ 武器。

## **░ 配置加载失败** <A NAME="config">
修改配置后，如果 CrackShot 的 _list_ 命令只显示部分武器，或完全不显示武器，就说明武器配置存在错误。

[YAML](http://yaml.org/) 对格式要求非常严格。请检查：
* 没有使用制表符。
* 每个节点或模块的缩进都正确。
* 所有字符串都用引号括起来。

如果武器仍无法正常工作，可以尝试：
* **检查控制台报错** - 控制台输出的错误几乎_总能_指出问题位置。例如，误用了制表符时，错误消息会指出它所在的具体行。
* **将配置粘贴到 YAML 解析器** - 可以使用[在线 YAML 解析器](http://yaml-online-parser.appspot.com/)帮助定位问题。
* **在论坛发布配置求助** - 包括作者在内，论坛上有许多用户愿意提供帮助，前提是你以_正确格式_发布配置，例如使用 [Pastebin](http://pastebin.com/) 或正确的格式标记。

## **░ 请求添加普通默认武器** <A NAME="pls">
> 示例 1：可以添加 Gold Desert Eagle 和 MP5 吗？  
示例 2：请添加 G36C！  
示例 3：可以添加一把迷你机枪吗？  

提出这些问题的人显然没有理解插件的用途。默认武器只是为了演示 _CrackShot_ 的部分功能，例如双持、附件和枪械动作。插件已经能够制作的普通武器，不会仅因为个人不会配置就被加入默认内容。[阅读指南](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot)，学习创建或修改武器。

此类请求几乎肯定不会被采纳。不过，如果想碰碰运气，仍可到[论坛](http://dev.bukkit.org/bukkit-plugins/crackshot/forum/)试试。
