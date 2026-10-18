---
title: 插件 API
source: https://docs.phoenixdevt.fr/mmocore/api/api
source_snapshot: '2026-10-19'
---

# 插件 API {#🔧-plugin-api}

## 玩家数据 {#player-data}

玩家数据存储在`PlayerData`实例内，可以使用该类中的静态`get`方法来操作和访问这些实例：

```java
PlayerData playerData = PlayerData.get(/* player UUID or Player instance */);
playerData.setLevel(10); // Sets player level to 10
playerData.giveExperience(500); // Gives 500 experience to the player
```

你可以修改玩家职业、等级、队伍、技能数据、任务数据和其他任何内容。  当玩家加入时，玩家数据同步加载，事件优先级为 NORMAL。

## 添加额外的任务条件/触发器/掉落表物品/条件 {#adding-extra-quest-conditions-triggers-drop-table-items-conditions}

为了提高与其他掉落表或任务插件的兼容性，你可能需要注册额外的选项，例如掉落表物品、条件或任务条件/触发器。

使用`MMOLoader`的实例加载这些选项。MMOCore拥有的加载器越多，它可以识别的选项就越多（就像技能机制或MythicMobs中的掉落表物品一样）。首先，你需要设置`MMOLoader`，以便它加载任何额外选项。例如，这是默认的`MMOLoader`：

```java
    @Override
    public Trigger loadTrigger(MMOLineConfig config) {
        if (config.getKey().equals("message"))
            return new MessageTrigger(config);

        if (config.getKey().equals("sound"))
            return new SoundTrigger(config);

        if (config.getKey().equals("command"))
            return new CommandTrigger(config);

        if (config.getKey().equals("item"))
            return new ItemTrigger(config);

        if (config.getKey().equals("exp"))
            return new ExperienceTrigger(config);

        return null;
    }

    @Override
    public DropItem loadDropItem(MMOLineConfig config, DropTableManager tables) {
        if (config.getKey().equals("droptable"))
            return new DropTableDropItem(tables, config);

        if (config.getKey().equals("vanilla"))
            return new VanillaDropItem(config);

        if (config.getKey().equals("note"))
            return new NoteDropItem(config);

        if (config.getKey().equals("gold"))
            return new GoldDropItem(config);

        return null;
    }

    @Override
    public Objective loadObjective(MMOLineConfig config, ConfigurationSection section) {
        if (config.getKey().equals("goto"))
            return new GoToObjective(section, config);

        if (config.getKey().equals("mine"))
            return new MineBlockObjective(section, config);

        if (config.getKey().equals("kill"))
            return new KillMobObjective(section, config);

        if (config.getKey().equals("getitem"))
            return new GetItemObjective(section, config);

        if (config.getKey().equals("clickon"))
            return new ClickonObjective(section, config);

        return null;
    }

    @Override
    public Condition loadCondition(MMOLineConfig config) {
        // TODO Auto-generated method stub
        return null;
    }
```

正如你所看到的，你必须为每种选项类型（触发/条件/删除物品...）重写 MMOLoader 超类中的一个方法。`config`返回一个对象，可让你获取有关线路配置的信息，如`vanilla{type=DIAMOND} 0.5 1-3`（类似于MythicMobsAPI）。

设置 MMOLoader 后，你必须使用`MMOCore.plugin.loadManager.registerLoader(yourMMOLoader)`将其注册到MMOCore中。确保在**MMOCore启用**之前注册它。要么让你的插件在MMOCore之前加载并在启用时注册它，要么不要冒任何加载顺序问题的风险，并在MMOCore加载后**加载**时注册它。

> **信息**
>
> 将来，掉落表和物品将移至MythicLib，以统一MMOItems和MMOCore掉落表。MMOCore中的任务触发器/条件也将合并到MythicLib脚本系统中。

---

原文：[🔧 Plugin API](https://docs.phoenixdevt.fr/mmocore/api/api) · 原文归档：2026-10-19
