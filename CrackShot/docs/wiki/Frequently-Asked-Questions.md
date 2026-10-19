---
title: "常见问题"
source_url: "https://github.com/Shampaggon/CrackShot/wiki/Frequently-Asked-Questions"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "Shampaggon/CrackShot Wiki @ d132397f9b52a5274dba87443ad0ebcde369a0a0；2026-10-19 快照；与 0.98.13-x6 的对应关系未确认"
---

<a id="table-of-contents"></a>

## **░ 目录** <a id="table_contents"></a>
<a id="faq"></a>

#### 常见问题
* [如何在其他插件中使用 CrackShot 武器？（套装、竞技场、商店、职业等）](#flexibility)
* [已经配置权限文件，为什么玩家仍能使用所有武器？](#permissions)
* [修改配置后，为什么武器不再显示？](#config)
* [可以添加〈在此填写武器名称〉吗？](#pls)

<a id="using-crackshot-weapons-with-other-plugins"></a>

## **░ 在其他插件中使用 CrackShot 武器** <a id="flexibility"></a>
<a id="method-1---the-skip_name_check-node"></a>

#### 方法 1 - Skip_Name_Check 节点
使用 [Skip_Name_Check](The-Complete-Guide-to-CrackShot.md#skip_name_check) 节点，可以将特定物品 ID 的物品转换成 _CrackShot_ 武器。

用法示例：

    Item_Type: 264~10
    Skip_Name_Check: true

服务器上所有物品 ID 为 `264:10` 的物品，都会自动转换成这把 _CrackShot_ 武器。因此，通过其他插件给予玩家 `264:10` 即可。

<a id="method-2---the-enchantment_to_check-node"></a>

#### 方法 2 - Enchantment_To_Check 节点
使用 [Enchantment_To_Check](The-Complete-Guide-to-CrackShot.md#enchantment_to_check) 节点，可以将拥有指定附魔的物品转换成 _CrackShot_ 武器。

用法示例：

    Item_Type: 264
    Enchantment_To_Check: SILK_TOUCH-2

服务器上所有物品 ID 为 `264`、同时具有_精准采集 II_ 附魔的物品，都会自动转换成这把 _CrackShot_ 武器。因此，通过其他插件给予玩家具有_精准采集 II_ 的_钻石_（ID: 264）即可。

<a id="method-3---the-crackshot-api"></a>

#### 方法 3 - CrackShot API
插件开发者如果想直接支持 _CrackShot_ 武器，可以[接入 _CrackShot_](https://github.com/Shampaggon/CrackShot/wiki/Hooking-into-CrackShot)，通过 _giveWeapon_ 函数直接给予玩家武器。

<a id="method-4---the-crackshot-commands"></a>

#### 方法 4 - CrackShot 命令
如果用于生成 _CrackShot_ 武器的插件支持命令，例如 _BuyCraft_ 或 _CommandSigns_，可以使用 [_CrackShot_ 的 give 和 get 命令](Commands-and-Permissions.md)给予玩家武器。

<a id="setting-up-your-permissions"></a>

## **░ 配置权限** <a id="permissions"></a>
如[命令与权限](Commands-and-Permissions.md)页面所述，以下权限默认授予_所有_用户：

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

<a id="the-configuration-fails-to-load"></a>

## **░ 配置加载失败** <a id="config"></a>
修改配置后，如果 CrackShot 的 _list_ 命令只显示部分武器，或完全不显示武器，就说明武器配置存在错误。

[YAML](http://yaml.org/) 对格式要求非常严格。请检查：
* 没有使用制表符。
* 每个节点或模块的缩进都正确。
* 所有字符串都用引号括起来。

如果武器仍无法正常工作，可以尝试：
* **检查控制台报错** - 控制台输出的错误几乎_总能_指出问题位置。例如，误用了制表符时，错误消息会指出它所在的具体行。
* **将配置粘贴到 YAML 解析器** - 可以使用[在线 YAML 解析器](http://yaml-online-parser.appspot.com/)帮助定位问题。
* **在论坛发布配置求助** - 包括作者在内，论坛上有许多用户愿意提供帮助，前提是你以_正确格式_发布配置，例如使用 [Pastebin](http://pastebin.com/) 或正确的格式标记。

<a id="requesting-generic-default-weapons"></a>

## **░ 请求添加普通默认武器** <a id="pls"></a>
> 示例 1：可以添加 Gold Desert Eagle 和 MP5 吗？  
示例 2：请添加 G36C！  
示例 3：可以添加一把迷你机枪吗？  

提出这些问题的人显然没有理解插件的用途。默认武器只是为了演示 _CrackShot_ 的部分功能，例如双持、附件和枪械动作。插件已经能够制作的普通武器，不会仅因为个人不会配置就被加入默认内容。[阅读指南](The-Complete-Guide-to-CrackShot.md)，学习创建或修改武器。

此类请求几乎肯定不会被采纳。不过，如果想碰碰运气，仍可到[论坛](http://dev.bukkit.org/bukkit-plugins/crackshot/forum/)试试。
