完整的命令列表及用法说明。以管理员身份执行时，用 `/resadmin` 代替 `/res`。

## 通用命令

### `/res ? [pagenumber]`

显示帮助。末尾的页码用于切换页面，默认为第 1 页。

### `/resadmin`

需要以管理员身份执行命令时，用它代替 /res。

## 选区命令

### `/res select [x y z]`

选择要保护的长方体区域。可以使用选区工具，默认是木斧；也可以指定 X、Y、Z，表示从当前位置这个中心点，沿各轴向两侧延伸的距离。例如 10 5 10 会选中宽 21、高 11、长 21 的区域。

### `/res select chunk`

选择整个区块作为保护范围。

### `/res select auto [playername]`

开启自动选区工具。

### `/res select expand [amount]`

沿视线方向扩大选区。

### `/res select size`

显示选区大小。

### `/res select shift [amount]`

沿视线方向平移选区。

### `/res select vert`

将选区从天空延伸到基岩。

### `/res select worldedit`

使用 WorldEdit 定义的选区。

## 创建与删除

### `/res area [add/remove/replace] [areaID]`

向领地添加区域，或移除区域。同一块领地的多个区域可以相互重叠。

### `/res create [ResidenceName]`

创建领地。

### `/res remove [ResidenceName]`

删除领地。

### `/res removeall`

删除自己的所有领地。

### `/res subzone [SubZoneName]`

在领地内创建子领地。必须是领地主人才可使用。

### `/res auto (residence name) (radius)`

在自己周围创建允许范围内最大的领地。

### `/res confirm`

确认删除领地。

## 信息查询

### `/res area list [residence]`

列出领地包含的区域。

### `/res show`

显示当前所在领地的边界。

### `/res area listall [residence]`

列出领地包含的区域及其坐标。

### `/res current`

显示当前所在的领地。

### `/res info`

查看领地信息；省略领地名时，查看当前所在领地。

### `/res list [player]`

列出自己或指定玩家拥有的领地。

### `/res listall`

列出所有领地。

### `/res listallhidden`

列出所有隐藏领地。

### `/res listhidden`

列出隐藏领地。

### `/res limits`

列出主要限制。

### `/res sublist [residence] [page]`

列出当前领地内的所有子领地。要查看其他页，需要填写领地名和页码。

### `/res version`

显示插件版本信息。

## 领地标志

### `/res gset [GroupName] [flag] [true/false/remove]`

为不同权限组设置领地标志。

### `/res lset [blacklist/ignorelist] [material]`

在领地的黑名单或忽略列表中添加、移除一种材料。

### `/res lset info`

列出领地的黑名单和忽略列表设置。

### `/res pset [PlayerName] [flag] [true/false/remove]`

为不同玩家设置领地标志。

### `/res set [flag] [true/false/remove]`

设置领地标志。

### `/res setall [flag] [true/false/remove]`

为所有世界中的所有领地设置标志。

### `/res setallfor [playerName] [flag] [true/false/remove]`

为指定玩家拥有的所有领地设置通用标志。

### `/res clearflags`

移除领地的全部标志。

### `/res check [residence] [flag] (playername)`

查看某个标志对自己是否生效。

### `/res flags`

列出所有标志。

### `/resadmin flags`

列出所有管理员标志。

### `/res padd [player]`

将玩家加入领地。

### `/res pdel [player]`

将玩家从领地中移除。

## 实用命令

### `/res expand [amount]`

将当前所在领地沿视线方向扩大指定数量的方块。

### `/res contract [amount]`

将当前所在领地沿视线方向缩小指定数量的方块。

### `/res default [residence]`

将领地恢复为默认标志设置。

### `/res give [residence] [player]`

将领地转让给另一位玩家。对方必须在线，自己必须是领地主人。

### `/res lists`

管理预设的领地权限列表，执行 /res lists 查看详情。

### `/res message [residence] [enter/leave] [message]`

设置进入或离开领地时的消息。省略领地名时，使用当前所在领地。

### `/res message [residence] remove [enter/leave]`

移除进入或离开领地时的消息。

### `/res mirror [source] [target]`

将一块领地的权限复制到另一块领地。必须同时拥有这两块领地。

### `/res rename [OldName] [NewName]`

重命名领地。重命名子领地时，OldName 必须填写完整名称 parent.subzone，NewName 只填写新的子领地名称。

### `/res renamearea [residence] [OldName] [NewName]`

重命名属于某块领地的实际区域。

### `/res tp [residence]`

传送到指定位置。

### `/res tpconfirm`

忽略不安全传送的警告。

### `/res tpset`

设置自己领地的传送落点。

### `/res unstuck`

将自己移到当前保护区域外。

### `/res command <allow/block/list>`

管理领地中允许或禁止使用的命令。

### `/res compass`

将指南针指向领地位置。

### `/res kick`

将玩家踢出领地。

### `/res material [material]`

根据材料 ID 检查该材料是否存在。

### `/res reset <residence/all>`

将领地恢复为默认标志设置。

### `/res rt (worldname) (playerName)`

传送到世界中的随机位置。

### `/res setmain`

设置主领地，使其作为聊天前缀显示。

### `/res tool`

显示领地选区工具和信息查看工具的名称。

## 领地聊天

### `/res rc (residence)`

加入当前或指定领地的聊天频道。

### `/res rc leave`

离开当前领地聊天频道。

### `/res rc setcolor [colorCode]`

设置领地聊天频道的文字颜色。

### `/res rc setprefix [newName]`

设置领地聊天频道的前缀。

### `/res rc kick [player]`

将玩家踢出频道。

## 领地商店

设有 `shop` 标志的领地可以使用商店命令。

### `/res shop list`

显示领地商店列表。

### `/res shop vote [amount]`

为领地商店投票。

### `/res shop like`

为领地商店点赞。

### `/res shop votes`

显示领地商店的投票数。

### `/res shop likes`

显示领地商店的点赞数。

### `/res shop setdesc [text]`

设置领地商店的介绍。

### `/res shop createboard [place]`

创建领地商店展示牌。

### `/res shop deleteboard`

删除领地商店展示牌。

## 市场与经济

### `/res lease [renew/cost] [residence]`

为领地续期，或查看续期费用。只有使用 iConomy 时才会收取费用。

### `/res market list`

查看待出售的领地列表。

### `/res market info [residence]`

查看待出售领地的信息。

### `/res market sell [residence] [amount]`

将领地挂牌出售。

### `/res market unsell [residence]`

取消出售领地。

### `/res market buy [residence]`

购买领地。

### `/res market rentable [residence] [cost] [days] repeat:t/f`

将领地设为可出租，租期为 [days] 天，每期租金为 [cost]。设置 repeat:t 时，当前租客的租期结束后，领地会自动恢复为可出租状态。

### `/res market rent [residence] repeat:t/f`

租用领地。repeat 为 true，且领地主人也为出租设置了 repeat:t 时，租期结束后会自动续租。

### `/res market release [residence]`

取消领地的已出租或可出租状态。

### `/res bank [deposit/withdraw] [amount]`

管理领地银行中的存款。

## 管理员命令

### `/res resadmin [on/off]`

开启或关闭领地管理员模式。

### `/res signconvert`

转换 ResidenceSign 插件的告示牌。

### `/res signupdate`

更新领地告示牌。

### `/resadmin lease set [residence] [#days/infinite]`

设置领地在 # 天后到期，或永不过期。

### `/resadmin removeall [player]`

删除指定玩家拥有的所有领地。

### `/resadmin removeworld [worldName]`

删除指定世界内的所有领地。**注意：该世界中保存的领地会全部删除，操作不可撤销。**

### `/resadmin setowner [residence] [player]`

更改领地主人。

### `/resadmin server [residence]`

将领地设为服务器所有。

### `/resload`

加载 Residence 插件。**注意：此命令不会覆盖 res.yml 中的修改。手动添加或修改 res.yml 后，使用它将更改加载到服务器。**

### `/resreload`

重新加载 Residence 插件。**注意：它会用插件或服务器启动时加载的设置覆盖 res.yml 中的修改。手动添加或修改 res.yml 后，应使用 /resload。**

**这份列表并非始终保持最新，实际可用的命令可能更多。**
