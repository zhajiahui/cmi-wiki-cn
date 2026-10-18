---
title: 使用 MythicMobs
source: https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic
source_snapshot: '2026-10-19'
---

# 使用 MythicMobs {#using-mythicmobs}

此页面将帮助你使用 Mythic/MythicMobs脚本语言在MythicLib/MMOItems/MMOCore中注册自定义技能。主要步骤如下：

1. 编写神话脚本
2. 将该脚本注册为自定义MythicLib技能，
3. 重新加载插件。

## 1/ 代码MythicMobs技能 {#_1-code-a-mythicmobs-skill}

第一步是使用MythicMobs脚本语言对技能执行的操作进行编码。在本教程中，我们将考虑在MythicMobs手册中找到的技能示例。它是一种简单的火焰射弹，可造成10伤害并使其击中的第一个敌人减速2秒。

```yml
FireBolt: # The main skill
  Skills:
  - 'projectile{onTick=FireBolt-Tick;onHit=FireBolt-Hit;v=8;i=1;hR=1;vR=1;hnp=true} @targetLocation'
FireBolt-Tick:
  Skills:
  - 'effect:particles{p=flame;amount=20;speed=0;hS=0.2;vS=0.2} @origin'
FireBolt-Hit:
  Skills:
  - 'damage{a=10}'
  - 'potion{type=SLOW;duration=40;lvl=2}'
```

## 2/ 将其声明为MythicLib技能 {#_2-declare-it-as-a-mythiclib-skill}

转到`MythicLib/skill`文件夹并创建一个YAML配置文件，其名称可以是你想要的任何名称 - 假设你将其命名为`tutorial.yml`。就像在MythicMobs中一样，你可以：

- 同一配置文件中有多个技能
- 将文件组织到子文件夹中
- 文件和文件夹名称可以是你想要的任何名称

你将在下面找到模板MythicLib技能定义，你可以将其复制并粘贴到配置文件中。我们将在以下部分中详细介绍每个配置选项。

```yml
FIRE_BOLT:
  source: mythicmobs:FireBolt
  # trigger: RIGHT_CLICK # Not needed here as we are making an active skill

  name: Firebolt
  lore:
    - 'You conjure a flaming ball and'
    - 'ball and hurl it at your target.'
    - ''
    - '&e{cooldown}s Cooldown'
    - '&9Costs {mana} {mana_name}'
  icon: BLAZE_POWDER

  # Edit default values of the ability parameters
  parameters:
    damage:
      name: Damage
      player:
        base: 2
        per-level: 1
      item: 5.0
    duration:
      name: Duration
      player: '2 + {level} * 1'
      item: 5.0
  
  extra-skills:
    FireBolt: # The main skill
      Skills:
      - 'projectile{onTick=FireBolt-Tick;onHit=FireBolt-Hit;v=8;i=1;hR=1;vR=1;hnp=true} @targetLocation'
    FireBolt-Tick:
      Skills:
      - 'effect:particles{p=flame;amount=20;speed=0;hS=0.2;vS=0.2} @origin'
    FireBolt-Hit:
      Skills:
      - 'damage{a=10}'
      - 'potion{type=SLOW;duration=40;lvl=2}'

# You can have multiple skills in one config file
#ANOTHER_SKILL:
  #source: ...
  #....
```

### 配置选项 {#config-options}

#### 技能标识符 {#skill-identifier}

让我们看一下`FIRE_BOLT`配置部分。首先，很好地格式化配置节名称，使其与`UPPERCASE_ID_FORMAT`匹配，因为它是MMOItems/MMOCore中用于技能的名称。

#### 技能源码 {#skill-source}

然后，提供技能的“来源”。由于我们使用MythicMobs实现MythicLib技能，因此源必须是`mythicmobs:FireBolt`，其中`FireBolt`是我们之前定义的MythicMobs技能的名称。下表列出了你可以实际与MythicLib一起使用的所有技能源：

|来源 |格式|
| --- | --- |
| [MythicMobs](https://www.spigotmc.org/resources/5702/) | `mythicmobs:<MythicMobsSkillname>` |
| [MythicLib](https://www.spigotmc.org/resources/90306/) | `mythiclib:<mythiclib_script_name>` |
| [Fabled](https://www.spigotmc.org/resources/91913/) | `fabled:<FabledAbilityName>` |
| [CoreTools](https://www.spigotmc.org/resources/125126/) | `coretools:<CoreToolsScriptName>` |

#### 技能图标、名称和描述 {#skill-icon-name-and-lore}

`icon`选项允许你修改MMOCore将在技能UI 中使用的物品来显示技能。你可以使用任何有效的Minecraft材料名称。

为了添加自定义模型数据，物品模型...使用以下语法。请注意，所有这些参数都是可选的。

```yml
FIRE_BOLT:
  #...
  icon:
    item: DIAMOND_SWORD
    custom_model_data: 1234
    item_model: 'minecraft:dirt'
    item_flags: [HIDE_ATTRIBUTES, HIDE_ENCHANTS]
```

`lore`选项允许你自定义技能描述，玩家将在MMOCore技能UI 中看到。请注意占位符的使用，例如`{cooldown}`、`{mana}`、`{mana_name}`，当显示技能时，它们将被动态替换。

```yml
FIRE_BOLT:
  #...
  lore:
    - 'You conjure a flaming ball and'
    - 'ball and hurl it at your target.'
    - ''
    - '&e{cooldown}s Cooldown'
    - '&9Costs {mana} {mana_name}'
```

`name`选项允许你自定义技能名称。请注意，这是MMOItems使用的唯一字段，因为图标和描述仅由MMOCore使用。

```yml
FIRE_BOLT:
  #...
  name: Firebolt
```

#### 触发 {#trigger}

`trigger`选项定义该技能的默认触发类型/转换方法。可用触发器类型的列表可在 [此 wiki 页面](../triggers.md)上找到。

具有触发器的技能称为*被动技能*，因为它们会自动触发。使用以下语法创建被动技能，当玩家右移时触发：

```yml
FIRE_BOLT:
  # ...
  trigger: SHIFT_RIGHT_CLICK # Triggers when the player shift right clicks
```

没有触发器的技能被称为*主动技能*，需要手动[由玩家](../../../mmocore/skills/casting.md)施放。如果你想要激活技能，请不要提供触发器。

> **信息**
>
> 请注意，如果你在MMOCore职业技能配置中指定触发器，它可以修改技能的触发器，或将主动技能变为被动技能。

#### 技能类别 {#skill-categories}

每个技能都可以通过字段`categories`分配到类别列表。默认情况下，每个技能与两个类别相关联：其技能、ID（例如`FIREBALL`，不要与技能名称混淆），以及`ACTIVE`或`PASSIVE`，具体取决于它是主动还是被动技能。这些类别可以在 [技能插槽公式](../../../mmocore/skills/binding.md#skill-slots)中使用。

```yml
FIREBOLT:
  # ...
  categories: [ fire, projectile ]
```

#### 技能参数 {#skill-parameters}

`parameters`部分允许你定义技能将使用的技能修饰符。在我们的示例中，我们定义了两个技能修饰符：`damage`和`duration`。每个修改器都有一个`name`（显示在技能UI 中）、一个`player`部分（定义修改器如何随玩家等级缩放）和`item`部分（定义修改器如何随物品等级缩放）。

`player`部分规定当技能通过MMOCore职业投射时技能修改器的缩放比例。`item`部分规定了将技能放置到MMOItems物品上时的默认技能参数值。`name`字段由MMOCoreUI 和MMOItems用于物品描述。

请注意，你可以通过两种方式提供`player`部分。你可以提供`base`和`per-level`值，这将导致线性缩放：

```yml
FIRE_BOLT:
  #...
  parameters:
    #...
    damage:
      name: Damage
      player:
        base: 2
        per-level: 1
      item: 5.0
```

你还可以使用`{level}`占位符提供完全自定义的公式，它代表玩家技能等级：

```yml
FIRE_BOLT:
  #...
  parameters:
    #...
    duration:
      name: Duration
      player: '2 + {level} * 1'
      item: 5.0
```

然而，`item`字段始终是平面十进制数。

### `extra-skills` {#extra-skills}

如你所见，你可以将 Mythic 脚本放入MythicLib配置文件中。这就是`extra-skills`配置部分的全部内容 - 你放置在此配置部分中的任何 Mythic 脚本都将传递给 Mythic。为了注册MythicLib自定义技能，你可以将 Mythic 脚本放入 ML 配置文件中，或者简单地将引用（脚本名称i.e`FireBolt`）传递给现有的 Mythic 脚本。无论哪种方式，Mythic 脚本名称都必须匹配：

```yml
FIRE_BOLT:
  #...

  extra-skills:
    FireBolt: # These two must match
      #...
```

## 3/ 重新加载插件 {#_3-reload-the-plugins}

1. 使用`/mm reload`重新加载MythicMobs。现在，你应该能够使用`/mm debug cast FireBolt`来测试你的MythicMobs技能。
2. 使用`/ml reload`重新加载MythicLib。现在，你的技能应该已在MythicLib中注册，并且你应该能够使用`/ml debug cast FIRE_BOLT`来测试你的 MMO技能。

就是这样！你不需要MMOItems或MMOCore的额外配置文件，因为这两个插件都直接使用MythicLib技能注册表。

## 技能条件 {#skill-conditions}

定制MM技能也支持技能条件。如果不满足任何技能条件，则技能将不会施放，并且不会消耗魔力。

## 检索MythicMobs技能内的 MMO技能修改器 {#retrieving-mmo-skill-modifiers-inside-mythicmobs-skills}

> **警告**
>
> 下面描述的一些功能在MythicMobs免费版本中不可用。

我们再考虑一下`Fire-Bolt`技能。

如前所述，以下技能目前造成的伤害与10持平。我们希望该值与MMOCore技能等级或MMOItems物品功率成比例。

```yml
SomeSkill:
  Mechanics:
  - damage{a=10}
```

以下技能造成的伤害相当于`damage`MythicLib技能修正值。`<modifier.xxx>`允许将MythicLib技能参数值转发到机械、条件内部使用的MythicMobs数学公式...

```yml
SomeSkill:
  Mechanics:
  - damage{a="<modifier.damage>"}
```

这些占位符可以与数学公式组合。在以下示例中，`duration`修饰符乘以20以将秒转换为刻。

```yml
SomeSkill:
  Mechanics:
  - potion{type=SLOW;duration="<modifier.duration> * 20";lvl=2}
```

以下是MythicLib实现的占位符的完整列表，可在MythicMobs技能中找到。

| 占位符 | 描述 |
| --- | --- |
| `<modifier.(mod_name)>` | 技能修饰符，十进制数 |
| `<modifier.int.(mod_name)>` | 技能修饰符，作为整数 |
| `<cooldown.skill_(name)>` | 剩余冷却时间为技能 |
| `<mmostat.(stat_name)>` | 玩家属性值，十进制数。例如：`<mmostat.attack_damage>` |
| `<mana>` | 玩家的当前魔力(MMOCore) |
| `<stamina>` | 玩家的当前耐力(MMOCore) |
| `<stellium>` | 玩家当前的群星(MMOCore) |

## 造成伤害 {#dealing-damage}

> **信息**
>
> 为了将来更好地支持MythicLib伤害系统，此内容可能会发生变化。

使用`mmodamage`机制而不是原生`damage`机制来处理 MMO 伤害类型的伤害。

```yml
SomeSkill:
  Mechanics:
  - mmodamage{amount="<modifier.damage> + 10";types=SKILL,MAGIC,PROJECTILE;element=FIRE}
```

你可以使用`amount`或`a`指定能力伤害，以及使用`types`或`t`指定伤害类型。可用损坏类型的列表可以在[此处](../../features/damage.md)找到。

它的工作原理就像默认的`damage`MythicMobs技能机制，不同之处在于它完全支持MythicLib伤害系统，这意味着它将应用伤害增益属性（额外的技能伤害等），伤害减免属性，on-hit效果（使用武器伤害类型时来自MMOItems的on-hit能力），来自MMOCore的技能对实体造成伤害时触发......

例如，以下生物每2秒对所有附近的实体造成10*物理*-*武器* 伤害。

```yml
ZombieWarrior:
  Type: ZOMBIE
  Damage: 10
  Skills:
    - 'mmodamage{amount=10;type=PHYSICAL,WEAPON} @NearbyEntities{r=5} ~onTimer:40'
```

### 暴击 {#critical-strikes}

默认情况下，武器和技能暴击分别适用于损坏类型`WEAPON`和`SKILL`。如果造成的伤害实例至少具有 *武器* 类型，它将能够造成 *武器* 伤害。如果它至少具有 *技能* 类型，它将能够造成 *技能* 伤害。

如果伤害实例造成的伤害既不是 *武器* 也不是 *技能* 类型，则它将无法造成暴击。这对于 DoT（*随时间变化的伤害*）、流血或中毒伤害很有用。

请注意，这是暴击的默认行为，并且可以通过使用自定义 [on-hit效果](../../features/on-hit-effects.md)来完全修改它。

## 增加/减少造成的伤害 {#increase-decrease-damage-dealt}

你可能还想使用以下技能机制：

```yml
SomeSkill:
  Mechanics:
  - multiplydamage{type=SKILL;amount="1 + <modifier.extra> / 100"}
```

这具有将 *技能* 伤害乘以特定系数的效果。目前该系数为`1 + <modifier.extra> / 100`，因此如果`extra`技能修改器设置为50，*技能* 伤害将增加50%。你可以使用此机制将实体或玩家造成的传入伤害增加一定的系数（e.g在生命值较低时增加伤害）。

如果你想增加任何来源的伤害（无伤害类型），请使用：

```yml
SomeSkill:
  Mechanics:
  - multiplydamage{amount="1 + <modifier.extra> / 100"}
```

## 检查技能施法者是否可以瞄准另一个实体 {#checking-if-the-skill-caster-can-target-another-entity}

使用`mmoCanTarget{..}`MythicMobs条件，你可以检查是否有任何玩家可以定位另一个实体。格式如下：

```yml
SomeSkill:
  Conditions:
  - mmoCanTarget{interaction=OFFENSE_ACTION}
```

有两种不同的交互类型：`OFFENSE_ACTION`、`SUPPORT_ACTION`。例如，当使用增益技能（如治疗或速度提升）时，玩家将能够瞄准另一个玩家，但如果技能变得具有攻击性（造成伤害或造成减益），则同一目标将无效。因此，指定你所讨论的交互类型非常重要。PvP/PvE交互规则用户指南可在 [此处](../../../mmocore/features/combat.md)。

以下是一些示例：

```yml
COMBAT_ONE:
  mythicmobs-skill-id: combat_one_run
  modifiers:
  - damage
  - duration
  extra-skills:
    combat_one_run:
      TargetConditions:
      - mmoCanTarget{interaction=SUPPORT_ACTION} true
      Skills:
      - jsonmessage{m="[{'text':'SUPPORT_ACTION','color':'red'}]"} @self

COMBAT_TWO:
  mythicmobs-skill-id: combat_two_run
  modifiers:
  - damage
  - duration
  extra-skills:
    combat_two_run:
      TargetConditions:
      - mmoCanTarget{interaction=OFFENSE_ACTION} true
      Skills:
      - jsonmessage{m="[{'text':'OFFENSE_ACTION','color':'red'}]"} @self

COMBAT_THREE:
  mythicmobs-skill-id: combat_three_run
  modifiers:
  - damage
  - duration
  extra-skills:
    combat_three_run:
      Skills:
      - mmodamage{amount=10;types=SKILL,MAGIC,PROJECTILE} @Target{conditions=[ - mmoCanTarget{interaction=OFFENSE_ACTION} true ]}
```

---

原文：[Using MythicMobs](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic) · 原文归档：2026-10-19
