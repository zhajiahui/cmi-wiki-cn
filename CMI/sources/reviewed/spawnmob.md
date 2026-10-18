## 基础参数

`/cmi spawnmob [type] ([amount]) ([location]) (sp:[range]) (ps:[data]) (ps2:[data])`

**[type]** — 实体类型，可以附加其他参数，具体见下文。

**[amount]** — 要生成的实体数量，也可以使用 **q:[amount]** 格式。

**[location]** — 实体的生成位置。使用常规位置格式，例如 **LT_Craft;46.62;-59.7;-1.7;-67.49;25.49**，这类位置可以通过 **/cmi pos** 命令获取。最后两个数值分别指定俯仰角（pitch）和偏航角（yaw），均为可选。要在特定玩家的位置生成生物，可以使用 **l:** 参数。例如，**l:Zrips** 会在 **Zrips** 在线时，在其所在位置生成生物。

**sp:[range]** — 指定实体分散的范围。生成多个实体时，可以设置分散范围，让它们分布得更均匀，避免全部挤在同一个方块内。例如，**sp:5**。

**ps:[data]** — 指定原实体的乘客，可以包含与基础实体相同类型的数据。

**ps2:[data]** — 与上一项相同，但会在可行时尝试将实体添加到载具的第二个乘客位置，最常见的用途是船。

简单命令示例：**/cmi spawnmob skeleton_horse 5 LT_Craft;46;-59;-1 ps:skeleton sp:10**。这会在指定位置生成 5 匹骷髅马和骑在它们身上的 5 个骷髅，并分散在 10 格范围内。

## 通用实体数据

命令示例：**/cmi spawnmob skeleton_horse;baby;hp{50};n{{#brown}Death_Bringer};s{3}**

**glow** — 让实体发光。

**n{[name]}** — 指定实体显示的名称，例如 **n{{#pink}My_Little_Ponny}**。名称中需要空格时，使用单个 `_`；需要实际的下划线时，使用双下划线 __。

**hidename** — 隐藏实体名称。必须在设置名称之后使用，否则名称仍会显示。如果想为实体命名，方便在清理生物的命令和插件中排除它，可以使用这个参数。

**effect{[data]}** — 应用于实体的药水效果，格式为 **[name]/[InSeconds]/[level]**，例如 **effect{speed/6666/2}**。多个效果可以写作 **effect{speed/6666/2,fire_resistance/6669/1}**。

**scale{number}** — 指定实体的缩放比例，也可以提供范围，在范围内随机选择。例如，**sheep;scale{0.5-2.5}** 会生成大小随机的绵羊。

**s{[amount]}** — 实体速度。如果想用更简单的方式提高实体速度，可以用它代替 effect 命令。

**hp{[amount]}** — 实体生命值，范围为 1 至 2048。未指定时，使用该实体的默认生命值。

**pickup** — 允许实体拾取地上的物品。

**nopickup** — 禁止实体拾取地上的物品。

**immortal** — 使实体不会死亡。

**invisible** — 使实体隐身。

**nograv** — 关闭实体的重力。这会让实体悬浮，同时无法移动。对能够飞行的实体无效。

**baby** — 在可行时生成实体的幼年形态。这会将实体保持在幼年阶段，实际上不会再长大。

**adult** — 在可行时生成实体的成年形态。请注意，不指定 **adult** 或 **baby** 时，结果可能随机。

**dumb** — 生成没有 AI 的实体。这会使实体无法移动，也无法与其他实体或玩家互动。

**expire{[time]}** — 指定实体自动移除前的时间，单位为秒，最长为 20 分钟（1200 秒）。使用此命令生成的实体，即使计时尚未结束，也会在服务器重启时移除。

**notpersistent** — 生成的实体会在服务器重启或区块卸载时移除。

**t{[playerName]}** — 将实体的目标设为指定的在线玩家，使实体在生成时就攻击该玩家。

**upwards** — 生成上下颠倒的实体。此选项与实体自定义名称不兼容。

onfire — 适用于 1.17+ 服务器。生成带有着火效果的实体。{{

## 盔甲和手持物品

**helmet{[material]}** — 头盔槽位中的物品。可以是任意材质，也可以使用 **head:[name]** 指定玩家头颅，例如 **helmet{head:Zrips}**。

**chest{[material]}** — 胸甲槽位中的物品。

**legs{[material]}** — 护腿槽位中的物品。

**boots{[material]}** — 靴子槽位中的物品。

**mhand{[material]}** — 主手中的物品。

**ohand{[material]}** — 副手中的物品。{

## 按实体类别区分的数据

**tamed** — 如果实体可以被驯服，则生成已驯服的实体。

**saddle** — 如果实体可以装备鞍，就为它添加鞍，例如马、猪、羊驼等。

**chest** — 如果实体可以携带箱子，就为它添加箱子。适用于骡和驴这类实体。

**angry** — 生成被激怒的实体，主要用于狼和蜜蜂。

**bounce** — 指定投射物击中物体时是否反弹。

## 按实体类型区分的数据

**山羊（Goat）**

**screaming** — 将山羊设为尖叫状态。

**已激活的 TNT（Primed TNT）**

incendiary — 将已激活的 TNT 设为可引燃的类型。

**苦力怕（Creeper）**

**charge** — 将苦力怕设为充能状态。

**盔甲架（Armor stand）**

**noplate** — 移除盔甲架的底板。  
**arms** — 显示盔甲架的手臂。  
**noarms** — 隐藏盔甲架的手臂。  
**small** — 将盔甲架设为小型。

**哞菇（Mushroom cow）**

**brown** — 将哞菇设为棕色。

**村民（Villagers）**

**职业**: armorer,  butcher, cartographer, cleric, farmer, fisherman, fletcher, leatherworker, librarian, mason, nitwit, shepherd, toolsmith, weaponsmith.  
**类型**: desert, jungle, plains, savanna, snow, swamp, taiga  
示例：**villager;butcher;jungle;3**，生成一名丛林类型、等级为 3 的屠夫村民。

**经验球（Experience orbs）**

填写整数，指定玩家拾取经验球时获得的经验值。例如，**experience_orb;50**。

**已激活的 TNT（TNTPrimed）**

填写整数，设置 TNT 爆炸前的计时。时间单位为秒，也可以使用小数。例如，**primed_tnt;5** 会生成在 5 秒后爆炸的 TNT。

**豹猫（Ocelot）**

**类型**: red, siamese, wild, 或 black.

**绵羊（Sheep）**

**类型**：可选值为 black, blue, brown, cyan, gray, green, light_blue, light_gray, lime, magenta, orange, pink, purple, red, white, yellow, 或 rainbow.

**马（Horse）**

**类型**: white, black, chestnut, creamy, darkbrown, 或 gray.

**史莱姆（Slime）**

填写数值，指定史莱姆的大小。默认值为 3。例如，**slime;5**。

**岩浆怪（Magma cube）**

填写数值，指定岩浆怪的大小。默认值为 3。例如，**magma_cube;5**。

**羊驼（Llama）**

**类型**: brown, creamy, gray, 或 white.

**鹦鹉（Parrot）**

**类型**: blue, cyan, gray, green, 或 red.

**雪傀儡（Snowgolem）**

**类型**: derp

**熊猫（Panda）**

**类型**: aggressive, brown, lazy, normal, playful, weak, 或 worried.

此实体可以同时接受两个参数。例如，**panda;lazy,worried** 分别指定主基因和隐藏基因。

**猫（Cat）**

**类型**: all_black, black, british_shorthair, calico, jellie, persian, ragdoll, red, siamese, tabby, 或 white.

**狐狸（Fox）**

**类型**: snow.

**美西螈（Axolotl）**

**类型**: blue, cyan, gold, lucy, 或 wild.

**狼（Wolf）**

**类型**: ashen, black, chestnut, pale, rusty, snowy, spotted, striped, woods

**鲑鱼（Salmon）**

**类型**: small, medium, large

**船（Boat）**

在 1.21.2+ 服务器中，船的各个类型都有独立的类型名称。

**类型**: acacia, bamboo, birch, cherry, dark_oak, jungle, mangrove, oak, 或 spruce.

竹子没有对应的船类型，生成的是竹筏。

**乐魂（Happy Ghast）**

**类型**: white, orange, magenta, lightblue, yellow, lime, pink, gray, lightgray, cyan, purple, blue, brown, green, red, black

**区域效果云（Area Effect Cloud）**

**color**：任意颜色，可以使用颜色名称，也可以使用 **#662266** 这样的十六进制颜色代码。请注意，自定义粒子可能会覆盖或忽略此颜色。  
**potion:** 用作此效果云效果的药水名称。  
**particle**：要使用的效果。  
**radius**：初始效果半径，单位为格，最大为 32。  
**radiustick**：每 tick 的半径变化量，可以为负值。效果半径达到 0 时，会自动移除。  
**duration**：效果的持续时间。默认会一直显示。  
**示例**：  
**/spawnmob area_effect_cloud;radius{32};potion{healing};radiustick{-0.1};particle{dust:green}** 会显示初始半径为 32、具有治疗效果的效果云。半径每 tick 缩小 0.1 格，即每秒缩小 2 格，直到降为 0 后消失。效果显示为绿色尘埃。

## 命令：

`/cmi spawnmob [type] ([amount]) ([location]) (sp:[range]) (ps:[data]) (ps2:[data])`

## 权限：

**cmi.command.spawnmob** — 在你所在的位置生成实体。

## 占位符：

此功能没有占位符。
