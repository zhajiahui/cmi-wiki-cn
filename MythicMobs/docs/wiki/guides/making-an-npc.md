---
title: 制作 NPC
source_url: https://wiki.mythiccraft.io/mythicmobs/Guides/Making-An-NPC
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 制作 NPC

**难度：入门**

使用几个基本技巧，就能通过 MythicMobs 创建用途丰富的 NPC。基本思路是创建一个没有 AI、不移动、不会消失的生物，再为这个 NPC 生物添加各种机制和技能，例如消息、命令，或你能想到的任何技能。

# 步骤 1 - 基础 NPC {#step-1-basic-npc}

第一步是创建生物文件，可以放在任意位置。本例会创建一个 NPC 子文件夹。

以下面的生物作为基础，可以创建一个只会站在原地的简单 NPC。我们使用 [LibsDisguises](https://www.spigotmc.org/resources/libs-disguises-free.81/)，让它看起来像玩家。

`plugins/MythicMobs/Mobs/NPC/Steve.yml`

```yaml
NPC_Steve:
  Type: INTERACTION
  Display: 'Steve the Guide'
  Disguise: Player <Inherit> setSkin Steve setDynamicName true
  Options:
    AlwaysShowName: true
    Despawn: persistent
```

- `NPC_Steve`：生成 NPC 时会用到这个名称。/mm m spawn NPC_Steve
- `Type: INTERACTION`：你可以使用喜欢的任何类型，但我们会使用交互实体，因为它没有 AI，也不会发出声音等。
- `Display: 'Steve the Guide'`：显示在 NPC 头顶的名称。
- `Disguise: Player <Inherit> setSkin Steve setDynamicName true`：让 NPC 看起来像玩家。可以将 "Steve" 替换为你想使用其皮肤的任意玩家名称。必须让 setDynamicName 保持为 true，NPC 才能使用 Display 设置。`<Inherit>` 占位符（区分大小写）会让 NPC 显示其 `Display:` 名称。关于使用自定义皮肤的更多信息，请[阅读这里](../mobs/disguises.md)。
- `AlwaysShowName: true`：在 NPC 头顶显示名称。
- `Despawn: persistent`：让 NPC 在重载、重启和区块卸载时保持生成状态。

# 步骤 2 - 添加消息与命令 {#step-2-adding-messages-and-commands}

可以使用 [Message](../skills/mechanics/message.md) 和 [Command](../skills/mechanics/command.md) 机制，为 NPC 添加消息或命令。本指南使用 @trigger 和 onInteract，向右键点击 NPC 的用户显示消息或为其运行命令。测试时请使用 SURVIVAL 模式，因为创造模式玩家无法被选为目标。

### Message {#message}

这个示例会在玩家右键点击 NPC 时向其发送消息。我们添加了[通用属性](../skills/mechanics.md#universal-attributes) `cd=3`，让两次点击之间有 3 秒冷却。

```yaml
  Skills:
  - message{m=&bWelcome to Hypixel &a<trigger.name>&b!;cd=3} @trigger ~onInteract
```

### 命令 {#commands}

这个示例会为右键点击 NPC 的玩家打开一个 DeluxeMenus 菜单。

```yaml
  Skills:
  - command{c="dm open shops-blocks <trigger.name>"} @trigger ~onInteract
```

可以为 NPC 添加任意数量的技能或机制，除了消息和命令，还可以运行任何机制和元技能。

# 步骤 3 - ModelEngine（可选） {#step-3-modelengine-optional}

如果希望 NPC 使用 ModelEngine 模型，可以移除伪装那一行，改用 2 个技能应用模型。我们会使用 onSpawn 和 onLoad，确保即使重启后，模型也始终应用在生物上。

还需要给模型添加一个名称标签骨骼，才能在模型上方显示名称。在 Blockbench 中打开模型，创建一个名为 `tag_name` 的空骨骼，再将修改后的模型上传到 Blueprints 文件夹，并执行 `/meg reload`。

`plugins/MythicMobs/Mobs/NPC/Steve.yml`

```yaml
NPC_Steve:
  Type: INTERACTION
  Display: 'Steve'
  Options:
    AlwaysShowName: true
    Collidable: false
    Despawn: persistent
  Skills:
  - model{m=SteveModel;n=name;save=true} @self ~onSpawn
```

model 机制使用的属性如下：

- `m=SteveModel`：填写模型名称，例如我们这里的模型为 `plugins/ModelEngine/Blueprints/SteveModel.bbmodel`。
- `n=name`：我们创建的[名称标签骨骼](https://git.mythiccraft.io/mythiccraft/model-engine-4/-/wikis/Modeling/Bone-Behaviors#nametag)的名称。
- `save=true`：告诉 ModelEngine 保留模型，即使重启也一样。

# 步骤 4 - 生成 NPC {#step-4-spawning-the-npc}

现在可以使用 `/mm reload` 重载修改后的文件，将 NPC 添加到服务器。站在希望 NPC 出现的位置，使用 `/mm m spawn NPC_Steve` 即可。

你现在已经创建了一个 MythicMobs NPC。
