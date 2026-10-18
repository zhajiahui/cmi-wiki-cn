## 欢迎使用 CMI 插件

CMI 适用于 1.7.x 及以上版本的 Spigot 和 Paper 服务器，提供多种功能，方便服主管理服务器。它的命令、权限和占位符系统灵活多变，为玩家提供现代、统一的使用体验。

本页介绍 BungeeCord、经济系统、聊天管理器等多项功能。从顶部菜单可以进入各项功能的详细说明。面对 300 条命令和众多功能，如果一时不知从何入手，可以加入我们的 Discord 服务器，社区成员可以帮助解答问题。

这是一个付费插件，运行时需要免费的 CMILib 库。购买前如有疑问，可以查看右上角菜单中的 FAQ，看看其中是否有相应解答。

**在运行群组服？** 如果在 BungeeCord 网络中使用 CMI，建议安装免费的 **[CMI Bungee](https://www.zrips.net/cmib/)** 或 [**CMI Velocity**](https://www.zrips.net/cmiv/) 插件，以使用 CMI 支持的全部功能。未安装时，部分功能会受限。下载后，将其放入 BungeeCord/Velocity 服务器的插件目录，再重新加载。

**经济系统**：要让 CMI 经济系统正常工作，需要从以下两种方案中选择一种：  
1. 使用[**这里**](https://www.zrips.net/cmivault/)提供的重新编译版 Vault。它直接支持 CMI 经济系统，与其他插件的兼容性最好。  
2. 使用[**这里**](https://zrips.net/cmii/)提供的经济注入器，为任意 Vault 构建版本添加 CMI 经济支持。  
  
两种方案都可用，但第二种方案可能会与一些插件出现小问题：这些插件在 Vault 加载后立即加载，而此时注入器还没有加载。  
另外，记得在配置文件中启用 `Economy`。

遇到问题，或想建议新功能？请在 [**GitHub**](https://github.com/Zrips/CMI/issues) 提交 issue，方便我和其他关注插件发展的用户跟进。![:)](https://www.spigotmc.org/styles/default/xenforo/clear.png "微笑 :)")

[![](https://www.zrips.net/wp-content/uploads/2019/02/discordiconlong-1.png)](https://discord.gg/dDMamN4)

**使用地理位置查询功能，需要将[此文件](https://www.zrips.net/wp-content/uploads/2019/02/GeoIP.dat)放入 CMI 文件夹。要查看玩家所在城市，请使用[此文件](https://www.zrips.net/wp-content/uploads/2019/02/GeoLiteCity.dat)。也可以在配置文件中开启自动下载。**

## 关于 CMI

![](https://www.zrips.net/wp-content/uploads/2019/02/about.jpg)

这个插件的目标是提供**一体化**服务器管理，替代多个过时的插件。它可以**完全替代** Essentials/EssentialsX，并提供简单的数据转换命令，将旧的玩家数据迁移到新系统。它提供的功能比你预想的更多，也包含打造独特服务器、加入新游戏机制所需的大多数工具。  
功能既包括治疗（`heal`）等基础操作，也包括游戏内礼包编辑器、跨各类容器查找物品、传送门系统、自动更新的告示牌、可点击的全息图等较复杂的功能。  
为什么定价 15 欧元？因为它值 150 欧元，但要价这么高就过头了。![:)](https://www.spigotmc.org/styles/default/xenforo/clear.png "微笑 :)")  
如果对这个插件还有疑问，可以看看评价区。

## 视频

![](https://www.zrips.net/wp-content/uploads/2019/02/videos.jpg)

[Haganite Plays 提供的视频](https://www.youtube.com/watch?v=mV4HCUtJ6HA)

[Hagenite Plays 的功能简览](https://www.youtube.com/watch?v=6ZDpZjJU0BY)

[Hagenite Plays 的插件评测](https://www.youtube.com/watch?v=1ecnZ1z-PFg)

## 功能

![](https://www.zrips.net/wp-content/uploads/2019/02/features.jpg)

- **接近 300 条命令，还不包括各项独立功能。**
- **MySQL/SQLite** 数据库系统。
- 带余额排行榜的**经济系统**。
- **聊天管理器**，提供现代化的游戏内聊天体验，完整支持十六进制颜色等功能。
- **支票系统**，可以制作存有金钱的物品。
- **高级监狱系统**。
- **全息图系统**，支持点击交互，并完整支持 **PlaceHolderAPI**。
- **模块化设置**，可以关闭不需要的功能，按需节省服务器资源。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-12-31_16-18-56.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-12-31_16-18-56.gif) [![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-27_17-07-48.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-27_17-07-48.gif)

- 支持 PlaceHolderAPI 的**自动更新告示牌**。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_13-57-38.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_13-57-38.gif)

- **物品分解**系统。

![](https://www.zrips.net/wp-content/uploads/2019/07/Scavanger2.gif)

- **粒子动画**创建系统。

[![](https://www.zrips.net/wp-content/uploads/2019/03/2019-03-02_16-54-23.gif)](https://www.zrips.net/wp-content/uploads/2019/03/2019-03-02_16-54-23.gif) ![](https://www.zrips.net/wp-content/uploads/2019/03/2019-03-02_16-30-01.gif)

- **传送门系统**，支持自定义粒子、自定义命令和 **bungeecord**。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_12-42-21.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_12-42-21.gif)

- **镜像建造**，提供 11 种不同的设置方式。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_13-01-05.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_13-01-05.gif)

- 带图形界面的**盔甲架编辑器**。

[![](https://www.zrips.net/wp-content/uploads/2019/02/armorstands4.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/armorstands4.jpg)

- 内置**自动晋级系统**，可以根据玩家统计、McMMO、Jobs 等数据晋级。

[![](https://www.zrips.net/wp-content/uploads/2019/02/rank.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/rank.jpg)

- **Boss 栏（BossBar）**系统，可以显示自定义消息，并提供多种自定义设置。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_13-20-48-1.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_13-20-48-1.gif)

- 通过 **Bungee 网络发送私聊或公开消息**。
- 支持 **Toast（进度通知）消息**，可用于自定义消息或语言文件。

[![](https://www.zrips.net/wp-content/uploads/2019/02/toast4.png)](https://www.zrips.net/wp-content/uploads/2019/02/toast4.png) [![](https://www.zrips.net/wp-content/uploads/2019/02/toast3.png)](https://www.zrips.net/wp-content/uploads/2019/02/toast3.png) [![](https://www.zrips.net/wp-content/uploads/2019/02/toast2.png)](https://www.zrips.net/wp-content/uploads/2019/02/toast2.png) [![](https://www.zrips.net/wp-content/uploads/2019/02/toast1.png)](https://www.zrips.net/wp-content/uploads/2019/02/toast1.png)

- 创建**自定义占位符**，供插件自身或 PlaceHolderAPI 使用。
- 将**盔甲染成**任意颜色，甚至让颜色自动变化。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-10-05_15-11-21.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-10-05_15-11-21.gif)

- 为任意物品**绑定命令**，使用物品时执行，也可以限制物品的使用次数。
- 完整支持 **PlaceholderAPI** 插件。
- **命令别名系统**，可以简化长命令，并在配置文件中为每条命令单独开启或关闭。
- 可自定义、支持动画，并可按组设置的**玩家列表（TabList）系统**。

[![](https://www.zrips.net/wp-content/uploads/2019/02/tablist2.png)](https://www.zrips.net/wp-content/uploads/2019/02/tablist2.png) [![](https://www.zrips.net/wp-content/uploads/2019/02/tablist1.png)](https://www.zrips.net/wp-content/uploads/2019/02/tablist1.png)

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-04-26_18-07-34.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-04-26_18-07-34.gif)

- **飞行能量**，可以用金钱或经验支付飞行费用。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-02-35.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-02-35.gif)

- 游戏内的**自定义别名编辑器**，可以按需调整命令。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-24-00.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-24-00.gif)

- 全局**占位符系统**。
- 详细的**玩家统计**。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-27-54.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-27-54.gif)

- 可以按需**编辑玩家统计数据**。
- **出售手持物品（Sell hand）**，可直接出售背包中的物品。设置价格时，内置的**漏洞利用检测**会检查潜在问题。

[![](https://www.zrips.net/wp-content/uploads/2019/02/worth.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/worth.jpg)

- 创建**可点击的方块或实体**，执行数量**不限**的命令。可以向玩家收取金钱或经验，也可以要求玩家拥有指定权限，并提供游戏内编辑器。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-50-24.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-50-24.gif)

- 按指定的生成原因，**阻止怪物在指定世界生成**。
- **禁用附魔**，玩家将无法通过附魔台获得被禁用的附魔，并提供图形界面。

[![](https://www.zrips.net/wp-content/uploads/2019/02/enchantdisabler.png)](https://www.zrips.net/wp-content/uploads/2019/02/enchantdisabler.png)

- **调整不死图腾的行为**，例如允许直接使用背包内的图腾，而不必拿在手上。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-50-25.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-50-25.gif)

- **自定义文本系统**，执行你设定的命令即可显示预设文字。
- **礼包系统**，内置礼包创建界面。
- **在线时长奖励**。

[![](https://www.zrips.net/wp-content/uploads/2019/02/playtimerewards.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/playtimerewards.jpg)

- **搜索功能**，可以按多种条件搜索所有玩家，包括离线玩家和 PlayerVaults 中的数据。
- **扫描功能**，可以扫描整张地图，在各类容器中查找指定物品，包括盔甲架和马携带的箱子。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_11-01-45.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_11-01-45.gif)

- 用鼠标滚轮切换画作。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_11-30-11.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_11-30-11.gif)

- **修复世界中的损坏区块**。
- 内置**定时任务系统**，可以在指定时间或按固定间隔自动执行命令。
- 可以在指定区块范围内或整个世界中**替换方块**。例如，要移除世界中的刷怪笼时，这个功能就很有用。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_11-41-25.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_11-41-25.gif)

- 内置基于**正则表达式的聊天过滤**。
- 用一条命令**导入 Essentials 玩家数据**。
- **弹射板**功能，可以自定义力度、角度或方向。与传送门系统配合，就能实现下图中的效果。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_11-55-36.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_11-55-36.gif)

- 普通聊天和私聊消息都支持**悬停提示**，可以显示 PlaceHolderAPI 插件提供的额外信息。
- 点击聊天消息即可快捷回复。
- **创建书本**，内容支持悬停提示或可点击的命令。
- 将**物品压缩**成更紧凑的形式。
- **拆分物品**，将方块拆成粒状材料（nuggets）。
- 服务器的区块**视距（ViewRange）**可按玩家权限设置，最高可达 32 个区块。
- **自定义配方**创建器。

[![](https://www.zrips.net/wp-content/uploads/2019/02/customrecipe.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/customrecipe.jpg) [![自定义无序合成配方](https://www.zrips.net/wp-content/uploads/elementor/thumbs/customrecipeshapeless-o3jwuvkblzosje9ztr4niryhqlpqmex2ej7lp9sglc.jpg "自定义无序合成配方")](https://www.zrips.net/wp-content/uploads/2019/02/customrecipeshapeless.jpg)

- 将服务器设为**维护模式**。
- 解除物品的**修复费用上限**，允许修复费用达到 2147483647 级。
- 在聊天中 **@玩家**，自动改变其名称的显示并向其播放声音提示。每位玩家都可以单独关闭此功能。
- **防止代修物品**，避免 VIP 玩家为普通玩家修理物品。
- 用一条命令**跳转到目标位置**。
- **阻止铁傀儡掉落玫瑰**。
- 防止 MultiCraft 用 `/list` 命令刷屏控制台。
- **防止利用下界传送门复制经验**。
- **解除书本锁定**，以便编辑。
- **完整控制玩家重生**。
- **带着坐骑传送到任意位置**。

[![](https://www.zrips.net/wp-content/uploads/2019/02/84038fe4091e8a91965073d8c094aa5641c78baa.gif)](https://www.zrips.net/wp-content/uploads/2019/02/84038fe4091e8a91965073d8c094aa5641c78baa.gif)

- 用一条命令查看实体信息。
- 用一条命令骑乘任意实体。
- 通过命令或直接点击，坐在楼梯、台阶或地毯上。

[![](https://www.zrips.net/wp-content/uploads/2019/02/sitting.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/sitting.jpg)

- 隐藏物品标志。
- 修复地图中的光照错误。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_16-24-04.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_16-24-04.gif) [![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_16-26-09.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_16-26-09.gif)

- **自动挂机（AFK）检测**，防止玩家利用跳跃或防挂机装置规避检测。
- **BossBar 指南针**。
- **`Ban/UnBan/ TempBan/checkBan/ IpBan/TempIpBan/ IpBanList`** 封禁管理功能，支持封禁原因，并可通过专用权限设置临时封禁的最长时限。
- 按组列出当前在线的所有玩家。
- **背包功能**，在背包中按住 Shift 并右键点击潜影盒即可使用。
- **睡觉加快夜晚流逝**，不要求所有玩家同时入睡，每位入睡的玩家都能加速。睡觉时会通过 BossBar 显示相关信息。
- 按需**调整白天和夜晚的时长**。
- **给玩家上铐**，在调查期间限制其操作。
- **锁定玩家 IP**，防止其他用户从另一台电脑尝试登录该玩家的账号。
- **通过正则表达式阻止物品重命名**。
- 用一条命令**清理服务器**中的多余对象，包括掉落物（不包括武器、盔甲和工具）、经验球、箭、投射物、已点燃的 TNT 和下落的方块。
- 在特定事件发生时执行命令：**`firstJoinServer, joinServer, quitServer, playerDeath, playerRespawn, playerTeleport, bedLeave, bedEnter, playerWorldChange, playerGameModeChange, playerKick, playerLevelChange, voidFall, elytraStartGlide, elytraEndGlide`** 等。
- 根据权限**全面控制玩家伤害**。
- 无需重启服务器即可**修改最大玩家数**。
- **BossBar 血量显示**，可以查看实体的总生命值、剩余生命值和你造成的伤害，也兼容箭矢。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_12-04-39.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_12-04-39.gif)

- 无需重启服务器即可修改 motd，支持颜色代码和双行文字。

[![](https://www.zrips.net/wp-content/uploads/2019/02/motd.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/motd.jpg)

- 卸载区块以释放服务器内存。
- 通过一个权限节点，让玩家死亡后自动重生。
- 消耗经验或指定物品为鞘翅加速，获得更畅快的飞行体验，并提供速度显示和速度上限。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_12-10-39.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_12-10-39.gif)

- 使用 `[item]` 变量即可在聊天中展示物品。此功能要求开启聊天处理和悬停消息，并由 CMI 接管。
- 加载最远 32 个区块范围内的地图，用于区域预览。
- 根据玩家离线天数，清理 playerdata 文件夹中的旧玩家数据文件。
- 让刷怪笼掉落为保留指定类型的物品，之后放置时仍是同一种刷怪笼。
- 用一条命令查看物品 NBT 标签。
- 发送私聊消息。
- 通过 social spy 监听私聊。
- 通过 commandspy 监听玩家执行的命令。
- 直接向玩家发送标题消息。
- 直接向玩家发送动作栏消息。
- 刷怪笼被 TNT 或苦力怕炸毁时，按指定概率掉落。
- 限制刷怪笼的放置密度，避免玩家在同一处堆放数十个刷怪笼，搭建巨型刷怪场。
- PvP 战斗后，按指定概率掉落玩家头颅。
- 击杀实体后掉落自定义实体头颅。
- 为每位玩家设置刷怪笼挖掘次数，限制玩家在一定时间内可挖掘的数量。
- 按 IP 查看关联账号。
- 玩家可以设置自己的家。
- 设置供玩家使用的传送点。
- 控制服务器时间。
- 控制玩家的个人时间。
- 控制服务器天气。
- 内置隐身系统，可以隐藏玩家。
- 生成任意实体，并自定义其各项参数，例如会飞的猪。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_12-16-06.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-23_12-16-06.gif)

- 根据玩家离线天数，清理 stats 文件夹中的旧玩家数据文件。
- 根据玩家离线天数，清理旧的 Essentials 玩家数据文件。
- 根据玩家离线天数，清理旧的 LWC 保护。
- 阻止玩家在下界“屋顶”上活动。
- 仅在指定玩家在线时执行自定义命令。
- 仅在指定玩家离线时执行自定义命令。
- 显示玩家的详细信息，包括曾用名（仅限正版服务器）和所在国家。要显示国家，需要将相应文件放入 CMI 文件夹。
- 显示玩家曾用昵称的详细列表，以及每次改名的日期（仅限正版服务器）。

[![](https://www.zrips.net/wp-content/uploads/2019/02/whowas.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/whowas.jpg)

- 编辑在线或离线玩家的背包。
- 编辑在线或离线玩家的末影箱。
- 将手中物品补满至最大堆叠数量。
- 在视线所指的位置生成树。
- 为自己或其他玩家打开工作台。
- 为自己或其他玩家打开村民交易界面。
- 静默打开箱子进行查看，不播放开箱动画。
- 通过权限节点允许玩家加入已满员的服务器。
- 设置出生点，供玩家直接传送，或在死亡后重生。
- 电梯系统。
- 阻止名称相同、仅大小写不同的多个账号加入服务器。
- 内置命令冷却机制，防止命令被立即重复使用。冷却时间在服务器重启后仍会保留。
- 内置命令等待机制，避免 `/tp` 等命令立即执行，防止玩家借此逃离 PvP 战斗。
- 显示玩家在服务器上的总在线时长和首次加入日期。
- 显示按玩家在线时长排序的完整列表。
- 无需重启服务器，即可让玩家槽位数的修改生效。
- 内置倒计时，可以从指定数值开始，适合 PvP 决斗或撒物品活动。
- 特定玩家登录时通知管理员。
- 通过权限节点阻止紫颂果传送。
- 向在线或离线玩家发放带自定义名称、物品描述或附魔的物品。支持特定生物的刷怪笼，也支持官方物品标签。

- 修改在线或离线玩家的游戏模式。
- 修改在线或离线玩家的无敌模式。
- 给玩家临时无敌模式，重新登录后失效。
- 修改在线或离线玩家的飞行模式。
- 给玩家临时飞行模式，重新登录后失效。
- 修改在线或离线玩家的飞行速度。
- 修改在线或离线玩家的行走速度。
- 修改在线或离线玩家的重生位置。
- 修改在线或离线玩家的药水效果。
- 修改昵称，支持颜色代码、黑名单及其他可选限制。
- 玩家切换世界时，自动将其游戏模式改为指定模式。
- 玩家切换世界时，自动将其飞行模式改为指定状态。
- 玩家切换世界时，自动将其无敌模式改为指定状态。
- 查看服务器状态。

[![](https://www.zrips.net/wp-content/uploads/2019/02/status.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/status.jpg)

- 传送指定世界中的所有在线或离线玩家。
- 传送到在线或离线玩家的位置。
- 传送回自己的死亡位置。
- 修改在线或离线玩家的最大生命值（maxhealth）。
- 看着刷怪笼执行一条命令，即可进行设置。
- 治疗在线或离线玩家。
- 为在线或离线玩家补充饱食度。
- 清空在线或离线玩家的背包。
- 清空在线或离线玩家的末影箱。
- 为玩家关闭公共聊天，保持聊天栏整洁，也能在录制视频时避免消息刷屏。
- 按住 Shift 并右键点击告示牌即可编辑。
- 用一条命令修改告示牌文字，也可以同时修改多行。会检查玩家在该位置是否有建造权限；没有权限时，告示牌文字也无法修改。
- 用一条命令，将一块告示牌上的文字复制到其他多块告示牌。

- 修理在线或离线玩家的物品。
- 为在线或离线玩家的物品附魔。
- 修改在线或离线玩家的物品名称。
- 修改在线或离线玩家的物品描述。
- 修改在线或离线玩家的经验。
- 修改在线或离线玩家的饱食度。
- 修改在线或离线玩家的指南针指向。
- 将任意方块设为在线或离线玩家的头饰。
- 生成任意玩家的头颅，并发给在线或离线玩家。
- 传送到世界中的任意位置。
- 列出拥有 OP 的玩家。
- 通过 Mojang 页面查看玩家的昵称变更记录。
- 清空聊天栏。
- 显示所有可用的颜色代码。
- 实时编辑玩家背包。
- 随时保存背包。
- 从已保存的数据加载背包。
- 在玩家死亡时保存背包，以便之后恢复。
- 查看玩家在世界中的位置，鼠标悬停在消息上时可查看额外信息。

[![](https://www.zrips.net/wp-content/uploads/2019/02/pos.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/pos.jpg)

- 显示包含死亡位置的消息。

[![](https://www.zrips.net/wp-content/uploads/2019/02/deathloc.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/deathloc.jpg)

- 还有更多功能……

## 依赖

![](https://www.zrips.net/wp-content/uploads/2019/02/dependencies.jpg)

**Java 8 及以上版本**  
[Paper](https://papermc.io/) / [Spigot](https://www.spigotmc.org/) / Bukkit — **1.7.10 / 1.8.8 / 1.9.x / 1.10.x / 1.11.x / 1.12.x / 1.13.x / 1.14.x / 1.15.x / 1.16.x / 1.17.x / 1.18.x / 1.19.x / 1.20.x**  
**CMI 运行时需要 [CMILib](https://www.zrips.net/cmilib/) 库。**

对于每个大版本分支，请使用该分支中最新的小版本及其最新构建。例如，不支持 1.16.1，支持 1.16.5。运行某个大版本的服务器时，尽量保持该分支内的更新最稳妥。

### 可选插件

- [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/)
- MVdWPlaceholderAPI
- Vault
- ProtocolLib
- [PlayerVaults](https://www.spigotmc.org/resources/playervaults.9228/)
- [PlayerVaultsNBT](https://www.spigotmc.org/resources/playervaults-w-nbt-format-no-dupe-bugs.32833/)
- PermissionsEx
- [DiscordSRV](https://www.spigotmc.org/resources/discordsrv.18494/)
- PowerfulPerms
- bPermissions
- GroupManagerX
- zPermissions
- [LuckPerms](https://www.spigotmc.org/resources/luckperms.28140/)
- [Jobs](https://www.spigotmc.org/resources/jobs-reborn.4216/)
- [McMMO](https://www.spigotmc.org/resources/official-mcmmo-original-author-returns.64348/)
- [Votifier](https://dev.bukkit.org/projects/votifier)
- [nuVotifier](https://www.spigotmc.org/resources/nuvotifier.13449/)
- [Multiverse-Core](https://www.spigotmc.org/resources/multiverse-core.390/)
- MultiWorld
- My Worlds
- TheWorld
- dynmap
- [LWC](https://www.spigotmc.org/resources/lwc-extended.69551/)

## API

![](https://www.zrips.net/wp-content/uploads/2019/02/api-1.jpg)

供希望将 **CMI** 作为依赖、通过 API 使用特定功能的开发者使用。可以从[**这里**](https://www.zrips.net/wp-content/uploads/2021/09/CMI9.0.0.0API.jar)下载插件的精简版本。这个版本保留了原插件的所有方法，但去除了实际实现代码，因此无法作为插件在服务器上运行；它可以帮助你基于 CMI 引擎开发自己的插件。GitHub 仓库见[**这里**](https://github.com/Zrips/CMI-API)。**[CMI 自定义事件](https://www.zrips.net/cmi/api/)**

## 语言文件

![](https://www.zrips.net/wp-content/uploads/2019/02/localeFiles.jpg)

所有消息都可以翻译，也可以创建独立的语言文件，方便使用。插件默认使用英语（EN）。

另外还附带了一些语言文件，翻译尚不完整，欢迎补充翻译 ^.^：

- **西班牙语**
- **中文**
- **德语**
- **意大利语**
- **俄语**
- **还有更多！[完整列表见 GitHub](https://github.com/Zrips/CMI/tree/master/Translations)。**

**设置：**

1. 将 jar 文件拖入 plugins 文件夹。
2. 启动服务器，生成默认文件。
3. 按需修改配置，然后开始使用。![:)](https://www.spigotmc.org/styles/default/xenforo/clear.png "微笑 :)")
