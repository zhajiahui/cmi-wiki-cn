`/cmi panimation {variableExpresion}`  
具体参数说明见下文。

CMI 的部分功能会使用粒子效果，可以在配置文件中更改。每个粒子效果写在同一行中，不能包含空格。需要更复杂的效果时，可以组合多个参数。

## 圆环

参数之间用 `;` 分隔，例如 `circle;effect:heart;dur:0.5`。  
圆环可用的参数如下：

`effect:[particleName]`

可以使用简写 `ef`。

需要指定粒子效果名称，例如 `ef:flying_glyph`。

`fireworks_spark`, `crit`, `magic_crit`, `potion_swirl`, `potion_swirl_transparent`, `spell`, `instant_spell`, `witch_magic`, `note`, `portal`, `flying_glyph`, `flame`, `lava_pop`, `footstep`, `splash`, `particle_smoke`, `explosion_huge`, `explosion_large`, `explosion`, `void_fog`, `small_smoke`, `cloud`, `coloured_dust`, `snowball_break`, `waterdrip`, `lavadrip`, `snow_shovel`, `slime`, `heart`, `villager_thundercloud`, `happy_villager`, `large_smoke`, `water_bubble`, `water_wake`, `suspended`, `barrier`, `mob_appearance`, `end_rod`, `damage_indicator`, `sweep_attack`, `totem`, `spit`, `squid_ink`, `bubble_pop`, `current_down`, `bubble_column_up`, `nautilus`, `dolphin`, `water_splash`, `campfire_signal_smoke`, `campfire_cosy_smoke`, `falling_dust`, `sneeze`, `composter`, `flash`, `falling_lava`, `landing_lava`, `falling_water`, `dripping_honey`, `falling_honey`, `landing_honey`, `falling_nectar`, `soul_fire_flame`, `ash`, `crimson_spore`, `warped_spore`, `soul`, `dripping_obsidian_tear`, `falling_obsidian_tear`, `landing_obsidian_tear`, `reverse_portal`, `white_ash`

`center:[playerName]/[World],[x],[y],[z]`

可以使用简写 `ct`。

需要提供玩家名称或坐标，例如 `ct:Zrips`、`ct:LT_Craft,15,256,21`。

`radius:[distance]`

可以使用简写 `r`。

设置圆环半径。小数使用 `.`，而不是 `,`。例如 `r:1.2`。

`fixed`

当位置来源指定为玩家时，让粒子固定在一处，不再跟随玩家。此参数不需要额外的值，用法为 `circle;effect:heart;center:Zrips;fixed`。

`radiuschange:[distance]`

可以使用简写 `rc`。

每个 tick 改变一次圆环半径。`rc:0.1` 会让半径每个 tick 增加 0.1，`rc:-0.1` 则每个 tick 减少 0.1。半径小于 0 时，粒子效果停止。

`duration:[time]`

可以使用简写 `dur`。

设置粒子效果的显示时间，单位为秒。可以用它防止粒子一直播放，也可以在只需要短暂效果时指定持续时间。默认时间为 **5** 秒。

用法：`dur:1.5`，表示显示粒子 1.5 秒。

`maxradius:[distance]`

可以使用简写 `mr`。

设置圆环的最大半径，达到此值后停止播放。默认值为 2。

用法：`mr:5`。

`offset:[x],[y],[z]`

可以使用简写 `off`。

设置相对于中心位置的偏移量。例如，可以让粒子从玩家头顶开始显示，而不是玩家所在的位置。

用法：`off:0,1.5,0`、`off:0,-1,0`。

`move:[x],[y],[z]/[playerName(,[speed])]`

移动中心点。可以指定移动向量，也可以使用目标玩家的视线方向，并可选填速度。

用法：`move:0,0.1,0` 会让粒子沿 Y 轴每个 tick 向上移动 0.1 格；`move:Zrips` 会让粒子朝 Zrips 的视线方向移动；`move:Zrips,0.1` 会让粒子朝 Zrips 的视线方向移动，速度为每个 tick 0.1 格。

`maxmovedistance:[distance]`

可以使用简写 `maxd` 或 `mmdist`。

设置粒子离开初始位置后可以移动的最大距离，避免粒子沿某个方向无限移动。

用法：`maxd:5.2`。

`rotating`

可以使用简写 `twist`。

让粒子绕自身轴线旋转，可以产生有趣的效果。不需要额外的值。

`particles:[amount]`

可以使用简写 `part`。

设置一个圆环中的粒子数量。

用法：`part:3`。

`pitch:[degrees/playerName]`

设置圆环的俯仰角，可用于将圆环朝一侧或另一侧倾斜。取值范围为 0 到 180。也可以使用玩家名称，以该玩家的俯仰角作为参数值。

用法：`pitch:152 pitch:Zrips`。

`yaw:[degrees/playerName]`

设置圆环的偏航角，可用于将圆环转向一侧或另一侧。取值范围为 0 到 180。也可以使用玩家名称，以该玩家的偏航角作为参数值。

用法：`yaw:152 yaw:Zrips`。

`pitchchange:[degrees]`

可以使用简写 `pitchc`。

按指定幅度改变俯仰角，用于制作旋转圆环效果。

用法：`pitchc:5`。

`yawchange:[degrees]`

可以使用简写 `yawc`。

按指定幅度改变偏航角，用于制作旋转圆环效果。

用法：`yawc:5`。

`followdirection`

可以使用简写 `fdir`。

如果指定了玩家，俯仰角（Pitch）和偏航角（yaw）会根据目标玩家的偏航角与俯仰角更新。不需要额外参数。

`color`

可以使用简写 `c`。

如果粒子支持着色，此参数用于设置粒子颜色。  
可以使用以下几种形式：  
`[r],[g],[b]`：通过红、绿、蓝三个数值设置颜色，取值范围为 0 到 255。  
支持十六进制颜色代码，例如 `{#6600cc}` 或 `{#red}`。  
`r`：让颜色持续变化，循环遍历所有颜色。  
`rs`：根据中心位置的俯仰角和偏航角显示彩虹色。  
`rfs`：根据与初始位置的距离为粒子着色。

用法：`c:100,250,10 c:r c:rs c:rfs`。

`target:[playerName]`

可以使用简写 `tr`。

指定要跟随的玩家。

用法：`tr:Zrips`。

`hidewhenvanished`

可以使用简写 `hwv`。

设置后，如果某位玩家看不见粒子所附着的来源玩家，也会对其隐藏这些粒子。

## 预设

常用的粒子效果可以通过预设简化设置。预设来自 `config.yml` 中的 `Particles` 部分。使用 `preset:[name]` 指定预设；额外参数如果在预设中已有定义，就会覆盖预设值，否则会为本次使用添加该参数。

例如，`/cmi panimation preset:TotemHalo;target:Zrips` 会让粒子效果附着在 Zrips 身上。因此，也可以用动态变量替代玩家名称，例如：`/cmi panimation preset:TotemHalo;target:[playerName]`。

## 示例

[![](https://www.zrips.net/wp-content/uploads/2019/03/2019-03-02_16-37-04.gif)](https://www.zrips.net/wp-content/uploads/2019/03/2019-03-02_16-37-04.gif) 

`circle;effect:flying_glyph;yaw:[playerName];pitch:[playerName];r:0.1;part:3;rc:0.03;mr:1;twist;off:0,2.5,0;target:[playerName]`

![](https://www.zrips.net/wp-content/uploads/2019/03/2019-03-02_16-28-11.gif)

`circle;effect:heart;dur:0.1;part:1;offset:0,1.7,0;radius:0.3;target:[playerName]`

![](https://www.zrips.net/wp-content/uploads/2019/03/2019-03-02_16-30-01.gif)

`circle;effect:flying_glyph;dur:5;pitchc:15;part:10;offset:0,1.7,0;radius:0.5;yawc:12;color:rs;pitch:90;target:[playerName]`

![](https://www.zrips.net/wp-content/uploads/2019/03/2019-03-02_16-31-22.gif)

`circle;c:0,255,0;twist;part:5;r:0.75;pitch:90;move:0,0.1,0;rc:-0.02;target:[playerName]`

![](https://www.zrips.net/wp-content/uploads/2019/03/2019-03-02_16-25-28.gif)

`circle;c:200,50,210;twist;part:5;r:0.5;pitch:90;move:0,0.33,0;offset:0,-0.2,0;target:[playerName]`

![](https://www.zrips.net/wp-content/uploads/2019/03/2019-03-02_16-54-23.gif)

`circle;effect:reddust;dur:5;pitchc:5;part:10;offset:0,1,0;radius:1;yawc:5;color:rs;target:[playerName]`
