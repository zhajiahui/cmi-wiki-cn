---
title: 基础适配器（Basic Adapter）
source: https://docs.typewritermc.com/adapters/BasicAdapter
source_version: 0.8.0
---

# 基础适配器（Basic Adapter）

Basic Adapter 包含 Typewriter 所需的基础条目。
通常应与 Typewriter 一起安装。
如果还没有安装 Typewriter 或适配器，
请先按[安装指南](../docs/getting-started/installation.md)完成安装，
再继续阅读。

## 条目 {#entries}

### 动作 {#actions}

|名称 |描述 |
| --- | --- |
|[添加药水效果](BasicAdapter/entries/action/add_potion_effect.md)|为玩家添加药水效果 |
|[施加速度](BasicAdapter/entries/action/apply_velocity.md)|对玩家应用速度 |
|[启动过场动画](BasicAdapter/entries/action/cinematic.md)|开始一部新的过场动画 |
|[执行控制台命令](BasicAdapter/entries/action/console_run_command.md)|从控制台运行命令 |
|[延迟动作](BasicAdapter/entries/action/delayed_action.md)|将动作延迟一定时间 |
|[掉落物品](BasicAdapter/entries/action/drop_item.md)|将物品扔到某个位置或玩家身上 |
|[生成烟花](BasicAdapter/entries/action/firework.md)|产生烟花|
|[给予物品](BasicAdapter/entries/action/give_item.md)|给玩家一个物品|
|[组内触发](BasicAdapter/entries/action/group_trigger_action.md)|为与玩家在同一组中的每个人触发下一个条目 |
|[发送消息](BasicAdapter/entries/action/send_message.md)|向玩家发送消息 |
|[播放声音](BasicAdapter/entries/action/play_sound.md)|在玩家或位置播放声音 |
|[执行玩家命令](BasicAdapter/entries/action/player_run_command.md)|让玩家运行命令|
|[随机触发门](BasicAdapter/entries/action/random_trigger.md)|随机选择其连接的触发器 |
|[移除物品](BasicAdapter/entries/action/remove_item.md)|从玩家背包中移除物品 |
|[设置方块](BasicAdapter/entries/action/set_block.md)|在某个位置设置块 |
|[设置物品](BasicAdapter/entries/action/set_item.md)|在特定槽位中设置一个物品 |
|[显示标题](BasicAdapter/entries/action/show_title.md)|向玩家显示头衔 |
|[简单动作](BasicAdapter/entries/action/simple_action.md)|简单动作修改事实|
|[生成粒子](BasicAdapter/entries/action/spawn_particles.md)|在指定位置生成粒子 |
|[停止声音](BasicAdapter/entries/action/stop_sound.md)|停止玩家的一个或所有声音 |
|[切换服务器](BasicAdapter/entries/action/switch_server_action.md)|将玩家切换到另一个服务器 |
|[传送](BasicAdapter/entries/action/teleport.md)|传送一名玩家 |
|[追踪任务](BasicAdapter/entries/action/track_quest.md)|开始追踪玩家的任务 |

### 受众 {#audiences}

|名称 |描述 |
| --- | --- |
|[Boss 栏](BasicAdapter/entries/audience/boss_bar.md)|Boss 栏|
|[过场动画受众](BasicAdapter/entries/audience/cinematic_audience.md)|根据受众是否在过场动画中过滤受众 |
|[最近组员路径流](BasicAdapter/entries/audience/closest_group_member_path_stream.md)|到最近的组成员的路径流 |
|[条件受众](BasicAdapter/entries/audience/criteria_audience.md)|基于条件的受众过滤器 |
|[Cron 受众](BasicAdapter/entries/audience/cron_audience.md)|根据时间是否与 cron 表达式匹配来过滤受众 |
|[直达位置路径流](BasicAdapter/entries/audience/direct_location_path_stream.md)|到直接位置的路径流 |
|[游戏时间受众](BasicAdapter/entries/audience/game_time_audience.md)|根据游戏时间过滤受众|
|[组员路径流](BasicAdapter/entries/audience/group_members_path_stream.md)|团体成员的路径流|
|[手持物品受众](BasicAdapter/entries/audience/holding_item_audience.md)|根据受众是否持有特定物品来过滤受众 |
|[背包物品受众](BasicAdapter/entries/audience/item_in_inventory_audience.md)|根据受众的背包中是否有特定物品来过滤受众 |
| [槽位物品受众](BasicAdapter/entries/audience/item_in_slot_audience.md) | 根据玩家是否在指定槽位中持有指定物品筛选受众 |
|[位置目标路径流](BasicAdapter/entries/audience/location_objectives_path_stream.md)|跟踪位置目标的路径流 |
|[循环过场动画受众](BasicAdapter/entries/audience/looping_cinematic_audience.md)|向受众展示循环播放的过场动画 |
|[简单文本行](BasicAdapter/entries/audience/simple_lines.md)|静态确定的文本行 |
|[简单侧边栏](BasicAdapter/entries/audience/sidebar.md)|为玩家显示侧边栏 |
|[玩家列表页眉与页脚](BasicAdapter/entries/audience/tab_list_header_footer.md)|设置玩家列表的页眉和页脚|
|[计时器受众](BasicAdapter/entries/audience/timer_audience.md)|当玩家在受众中时，每隔指定的持续时间触发一个动作 |
|[触发受众](BasicAdapter/entries/audience/trigger_audience.md)|当玩家进入或离开受众时触发序列 |

### 过场动画 {#cinematics}

|名称 |描述 |
| --- | --- |
|[动作栏对话过场动画](BasicAdapter/entries/cinematic/actionbar_dialogue_cinematic.md)|显示动作栏键入的对话 |
|[致盲过场动画](BasicAdapter/entries/cinematic/blinding_cinematic.md)|使玩家失明，使屏幕看起来是黑色的 |
|[镜头过场动画](BasicAdapter/entries/cinematic/camera_cinematic.md)|创建过场动画摄影机路径 |
|[过场动画控制台命令](BasicAdapter/entries/cinematic/cinematic_console_command.md)|在特定帧作为控制台运行命令。 |
|[过场动画玩家命令](BasicAdapter/entries/cinematic/cinematic_player_command.md)|在特定帧以玩家身份运行命令。 |
|[粒子过场动画](BasicAdapter/entries/cinematic/particle_cinematic.md)|为过场动画生成粒子 |
|[药水效果过场动画](BasicAdapter/entries/cinematic/potion_effect_cinematic.md)|在过场动画期间对玩家应用不同的药水效果 |
|[南瓜头盔过场动画](BasicAdapter/entries/cinematic/pumpkin_hat_cinematic.md)|在过场动画中展示南瓜帽 |
|[随机动作栏对话过场动画](BasicAdapter/entries/cinematic/random_actionbar_dialogue_cinematic.md)|显示随机动作栏键入的对话 |
|[随机逐字对话过场动画](BasicAdapter/entries/cinematic/random_spoken_dialogue_cinematic.md)|播放随机逐字对话对话过场动画 |
|[随机副标题对话过场动画](BasicAdapter/entries/cinematic/random_subtitle_dialogue_cinematic.md)|显示随机动作栏消息 |
|[屏幕震动过场动画](BasicAdapter/entries/cinematic/screen_shake_cinematic.md)|摇动屏幕|
|[虚拟方块过场动画](BasicAdapter/entries/cinematic/set_fake_block_cinematic.md)|设置一个假块 |
|[声音过场动画](BasicAdapter/entries/cinematic/sound_cinematic.md)|播放过场动画时播放声音 |
|[逐字对话过场动画](BasicAdapter/entries/cinematic/spoken_dialogue_cinematic.md)|播放一段逐字对话对话影片 |
|[副标题对话过场动画](BasicAdapter/entries/cinematic/subtitle_dialogue_cinematic.md)|显示字幕消息 |
|[标题过场动画](BasicAdapter/entries/cinematic/title_cinematic.md)|在过场动画放映期间显示标题 |
|[触发序列过场动画](BasicAdapter/entries/cinematic/trigger_sequence_cinematic.md)|要运行的触发器序列 |

### 对话 {#dialogues}

|名称 |描述 |
| --- | --- |
|[消息对话](BasicAdapter/entries/dialogue/message.md)|向玩家显示一条消息 |
|[选项对话](BasicAdapter/entries/dialogue/option.md)|向玩家显示选项列表 |
|[随机消息对话](BasicAdapter/entries/dialogue/random_message.md)|从列表中向玩家显示随机消息 |
|[随机逐字对话](BasicAdapter/entries/dialogue/random_spoken.md)|向玩家显示随机选择的动画消息 |
|[逐字对话](BasicAdapter/entries/dialogue/spoken.md)|向玩家显示动画消息 |

### 事件 {#events}

|名称 |描述 |
| --- | --- |
|[破坏方块事件](BasicAdapter/entries/event/on_block_break.md)|当玩家打破方块时|
|[放置方块事件](BasicAdapter/entries/event/on_place_block.md)|当玩家放置方块时 |
|[聊天包含文本事件](BasicAdapter/entries/event/on_message_contains_text.md)|当玩家发送包含特定文字的聊天消息时 |
|[合成物品事件](BasicAdapter/entries/event/craft_item_event.md)|当玩家制作物品时调用 |
|[检测命令执行事件](BasicAdapter/entries/event/on_detect_command_ran.md)|当玩家运行现有命令时 |
|[手动触发事件](BasicAdapter/entries/event/fire_trigger_event.md)|当玩家运行`/tw fire <entry id/name> [player]`时触发事件 |
|[钓鱼事件](BasicAdapter/entries/event/on_fish.md)|当玩家钓到鱼或物品时 |
|[方块交互事件](BasicAdapter/entries/event/on_interact_with_block.md)|当玩家与方块交互时 |
|[拾取物品事件](BasicAdapter/entries/event/on_item_pickup.md)|当玩家拿起物品时 |
|[玩家死亡事件](BasicAdapter/entries/event/on_player_death.md)|当玩家死亡时 |
|[玩家攻击实体事件](BasicAdapter/entries/event/on_player_hit_entity.md)|当玩家击中实体时 |
|[玩家加入事件](BasicAdapter/entries/event/on_player_join.md)|当玩家加入服务器时 |
|[玩家击杀实体事件](BasicAdapter/entries/event/on_player_kill_entity.md)|当玩家杀死一个实体时 |
|[玩家击杀玩家事件](BasicAdapter/entries/event/on_player_kill_player.md)|当一名玩家杀死一名玩家时 |
|[玩家接近位置事件](BasicAdapter/entries/event/on_player_near_location.md)|当玩家靠近某个位置时 |
|[玩家退出事件](BasicAdapter/entries/event/on_player_quit.md)|当玩家退出服务器时 |
|[运行命令事件](BasicAdapter/entries/event/on_run_command.md)|当玩家运行自定义命令时 |

### 事实 {#facts}

|名称 |描述 |
| --- | --- |
|[倒计时事实](BasicAdapter/entries/fact/countdown_fact.md)|从设定值开始倒计时的事实 |
|[Cron 事实](BasicAdapter/entries/fact/cron_fact.md)|保存到指定日期，例如 (0 0 * * 1 |
|[处于受众中事实](BasicAdapter/entries/fact/in_audience_fact.md)|玩家在受众中的事实|
|[处于过场动画中事实](BasicAdapter/entries/fact/in_cinematic_fact.md)|如果玩家处于过场动画 |
|[背包物品数量事实](BasicAdapter/entries/fact/inventory_item_count_fact.md)|玩家背包中特定物品的数量 |
|[手持物品事实](BasicAdapter/entries/fact/item_holding_fact.md)|玩家当前持有的特定物品的数量 |
|[槽位物品事实](BasicAdapter/entries/fact/item_in_slot_fact.md)|检查特定物品是否位于玩家的特定槽位中 |
|[数字占位符事实](BasicAdapter/entries/fact/number_placeholder.md)|占位符数字的计算事实 |
|[永久事实](BasicAdapter/entries/fact/permanent_fact.md)|永久保存，永远不会被删除 |
|[任务状态事实](BasicAdapter/entries/fact/quest_status_fact.md)|特定任务的状态 |
|[会话事实](BasicAdapter/entries/fact/session_fact.md)|保存到玩家退出服务器为止 |
|[限时事实](BasicAdapter/entries/fact/timed_fact.md)|保存指定的持续时间，例如 20 分钟 |
|[数值占位符事实](BasicAdapter/entries/fact/value_placeholder.md)|占位符值的事实 |

### 组 {#groups}

|名称 |描述 |
| --- | --- |
|[全局组](BasicAdapter/entries/group/global_group.md)|所有在线玩家一组|
|[玩家组](BasicAdapter/entries/group/player_group.md)|每个玩家的分组|
|[世界组](BasicAdapter/entries/group/world_group.md)|面向全世界的集团|

### 任务 {#quests}

|名称 |描述 |
| --- | --- |
|[可完成目标](BasicAdapter/entries/quest/completable_objective.md)|可以显示已完成阶段的目标 |
|[位置目标](BasicAdapter/entries/quest/location_objective.md)|位置目标定义|
|[目标文本行](BasicAdapter/entries/quest/objective_lines.md)|显示当前所有目标 |
|[任务完成事件](BasicAdapter/entries/quest/quest_complete_event.md)|当玩家完成任务时触发 |
|[任务开始事件](BasicAdapter/entries/quest/quest_start_event.md)|当玩家开始任务时触发 |
|[任务状态更新事件](BasicAdapter/entries/quest/quest_status_update_event.md)|当玩家的任务状态更新时触发 |
|[简单目标](BasicAdapter/entries/quest/objective.md)|客观的定义|
|[简单任务](BasicAdapter/entries/quest.md)|任务定义|
|[已追踪目标受众](BasicAdapter/entries/quest/tracked_objective_audience.md)|根据受众是否有跟踪目标来过滤受众 |
|[已追踪任务受众](BasicAdapter/entries/quest/tracked_quest_audience.md)|根据受众是否有跟踪任务来过滤受众 |

### 声音 {#sounds}

|名称 |描述 |
| --- | --- |
|[自定义声音](BasicAdapter/entries/sound/custom_sound.md)|自定义声音 |

### 静态条目 {#statics}

|名称 |描述 |
| --- | --- |
|[基础道路网络](BasicAdapter/entries/static/base_road_network.md)|道路网络一词的定义|
|[玩家自身说话者](BasicAdapter/entries/static/self_speaker.md)|玩家本人|
|[简单说话者](BasicAdapter/entries/static/simple_speaker.md)|最基本的音箱|

---

原文：[Basic Adapter](https://docs.typewritermc.com/adapters/BasicAdapter) · 文档版本：0.8.0
