---
title: 实体适配器（Entity Adapter）
source: https://docs.typewritermc.com/adapters/EntityAdapter
source_version: 0.8.0
---

# 实体适配器（Entity Adapter）

实体适配器包含与实体一起使用的所有基本条目。
它允许你创建动态实体，例如 NPC 或全息图。

通常应与 Typewriter 一起安装。
如果还没有安装 Typewriter 或适配器，
请先按[安装指南](../docs/getting-started/installation.md)完成安装，
再继续阅读。

## 条目 {#entries}

### 活动 {#activitys}

|名称 |描述 |
| --- | --- |
|[受众活动](EntityAdapter/entries/activity/audience_activity.md)|根据玩家所在的受众群体选择活动 |
|[游戏时间活动](EntityAdapter/entries/activity/game_time_activity.md)|游戏时间活动|
|[对话中活动](EntityAdapter/entries/activity/in_dialogue_activity.md)|对话活动 |
|[近距离注视活动](EntityAdapter/entries/activity/look_close_activity.md)|近距离看活动|
|[路径活动](EntityAdapter/entries/activity/path_activity.md)|沿着预定的路径移动 |
|[巡逻活动](EntityAdapter/entries/activity/patrol_activity.md)|在一组地点移动 |
|[玩家在附近活动](EntityAdapter/entries/activity/player_close_by_activity.md)|附近活动的玩家 |
|[随机环顾活动](EntityAdapter/entries/activity/random_look_activity.md)|随机看看活动 |
|[目标位置活动](EntityAdapter/entries/activity/target_location_activity.md)|地点活动|
|[定时活动](EntityAdapter/entries/activity/timed_activity.md)|允许子活动在有限的时间内进行活动 |
|[触发活动](EntityAdapter/entries/activity/trigger_activity.md)|当活动处于活动或非活动状态时触发序列 |

### 受众 {#audiences}

|名称 |描述 |
| --- | --- |
|[直达实体实例路径流](EntityAdapter/entries/audience/direct_entity_instance_path_stream.md)|直接实体实例的路径流 |

### 过场动画 {#cinematics}

|名称 |描述 |
| --- | --- |
|[实体过场动画](EntityAdapter/entries/cinematic/entity_cinematic.md)|在过场动画中使用动画实体 |

### 数据 {#datas}

|名称 |描述 |
| --- | --- |
|[年龄数据](EntityAdapter/entries/data/ageable_data.md)|老化数据 |
|[身上箭矢数量数据](EntityAdapter/entries/data/arrow_count_data.md)|实体中箭头的数量 |
|[猫变种数据](EntityAdapter/entries/data/cat_variant_data.md)|猫的变种。 |
|[驮箱马类箱子数据](EntityAdapter/entries/data/chested_horse_chest_meta.md)|如果马有胸部。 |
|[项圈颜色数据](EntityAdapter/entries/data/collar_color_data.md)|猫项圈或狼项圈的颜色 |
|[自定义名称数据](EntityAdapter/entries/data/custom_name_data.md)|实体的自定义名称 |
|[跳舞数据](EntityAdapter/entries/data/dancing_data.md)|实体是否在跳舞|
|[发光效果数据](EntityAdapter/entries/data/glowing_effect_data.md)|如果实体发光 |
|[马变种数据](EntityAdapter/entries/data/horse_variant_dat.md)|马的变种。 |
|[羊驼地毯颜色数据](EntityAdapter/entries/data/llama_carpet_color_data.md)|美洲驼地毯的颜色。 |
|[羊驼变种数据](EntityAdapter/entries/data/llama_variant_data.md)|美洲驼的变种。 |
|[标记数据](EntityAdapter/entries/data/marker_data.md)|实体是否为标记 |
|[着火数据](EntityAdapter/entries/data/on_fire_data.md)|如果实体着火|
|[鹦鹉颜色数据](EntityAdapter/entries/data/parrot_color_data.md)|鹦鹉的颜色|
|[姿势数据](EntityAdapter/entries/data/pose_data.md)|实体的姿态 |
|[药水效果颜色数据](EntityAdapter/entries/data/potion_effect_color_data.md)|药水效果粒子的颜色|
|[河豚膨胀状态数据](EntityAdapter/entries/data/puff_state_data.md)| Puf 实体的状态 |
|[兔子类型数据](EntityAdapter/entries/data/rabbit_type_data.md)|兔子的种类 |
|[鞍具数据](EntityAdapter/entries/data/saddled_data.md)|如果该实体有一个马鞍。 |
|[大小数据](EntityAdapter/entries/data/size_data.md)|实体规模|
|[皮肤数据](EntityAdapter/entries/data/skin_data.md)|玩家皮肤数据|
|[小型数据](EntityAdapter/entries/data/small_data.md)|实体是否小 |
|[村民数据](EntityAdapter/entries/data/villager_data.md)|村民资料|

### 实体 {#entitys}

|名称 |描述 |
| --- | --- |
|[悦灵实例](EntityAdapter/entries/entity/allay_instance.md)|一个 allay 实体的实例 |
|[猫实例](EntityAdapter/entries/entity/cat_instance.md)|猫实体的实例 |
|[鸡实例](EntityAdapter/entries/entity/chicken_instance.md)|鸡实体的实例 |
|[牛实例](EntityAdapter/entries/entity/cow_instance.md)|牛实体的实例 |
|[末影人实例](EntityAdapter/entries/entity/enderman_instance.md)|末影人实体的实例 |
|[青蛙实例](EntityAdapter/entries/entity/frog_instance.md)|青蛙实体的实例 |
|[碰撞箱定义](EntityAdapter/entries/entity/hit_box_definition.md)|实体的点击框允许与不同实体进行交互|
|[疣猪兽实例](EntityAdapter/entries/entity/hoglin_instance.md)| hoglin 实体的实例 |
|[尸壳实例](EntityAdapter/entries/entity/husk_instance.md)|外壳实体的实例 |
|[交互指示器定义](EntityAdapter/entries/entity/interaction_indicator_definition.md)|互动指标|
|[铁傀儡实例](EntityAdapter/entries/entity/iron_golem_instance.md)|铁傀儡实体的一个实例 |
|[物品展示实体实例](EntityAdapter/entries/entity/item_display_instance.md)|物品显示实体的实例 |
|[岩浆怪实例](EntityAdapter/entries/entity/magma_cube_instance.md)|岩浆立方体实体的实例 |
|[具名实体定义](EntityAdapter/entries/entity/named_entity_definition.md)|头部上方有名称和指示器的实体 |
|[NPC 实例](EntityAdapter/entries/entity/npc_instance.md)|简化的预制 npc 实例 |
|[猪灵蛮兵实例](EntityAdapter/entries/entity/piglin_brute_instance.md)|猪灵野蛮实体的一个实例 |
|[猪灵实例](EntityAdapter/entries/entity/piglin_instance.md)|一个 Piglin 实体的实例 |
|[玩家实例](EntityAdapter/entries/entity/player_instance.md)|玩家实体的实例 |
|[玩家自身 NPC 定义](EntityAdapter/entries/entity/self_npc_definition.md)|自我NPC的定义|
|[骷髅实例](EntityAdapter/entries/entity/skeleton_instance.md)|骨架实体的实例 |
|[史莱姆实例](EntityAdapter/entries/entity/slime_instance.md)|史莱姆实体的一个实例 |
|[堆叠实体定义](EntityAdapter/entries/entity/stacked_entity_definition.md)|实体的堆叠 |
|[文本展示实体实例](EntityAdapter/entries/entity/text_display_instance.md)|文本显示实体的实例 |
|[村民实例](EntityAdapter/entries/entity/villager_instance.md)|村民实体的实例 |
|[监守者实例](EntityAdapter/entries/entity/warden_instance.md)|典狱长实体的实例 |
|[女巫实例](EntityAdapter/entries/entity/witch_instance.md)|女巫实体实例|
|[僵尸实例](EntityAdapter/entries/entity/zombie_instance.md)|僵尸实体的实例|

### 事件 {#events}

|名称 |描述 |
| --- | --- |
|[实体交互事件](EntityAdapter/entries/event/entity_interact_event.md)|当玩家点击一个实体时 |

### 实例 {#instances}

|名称 |描述 |
| --- | --- |
|[分组高级实体实例](EntityAdapter/entries/instance/group_advanced_entity_instance.md)|实体的高级实例 |
|[个人高级实体实例](EntityAdapter/entries/instance/individual_advanced_entity_instance.md)|实体的高级实例 |
|[共享高级实体实例](EntityAdapter/entries/instance/shared_advanced_entity_instance.md)|实体的高级实例 |

### 任务 {#quests}

|名称 |描述 |
| --- | --- |
|[实体交互目标](EntityAdapter/entries/quest/interact_entity_objective.md)|与实体交互 |
|[实体交互目标路径流](EntityAdapter/entries/quest/interact_entity_objectives_path_stream.md)|交互实体目标的路径流 |

---

原文：[Entity Adapter](https://docs.typewritermc.com/adapters/EntityAdapter) · 文档版本：0.8.0
