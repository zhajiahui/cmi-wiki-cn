---
title: Aura
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/aura
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Aura {#aura}

## 说明 {#description}

光环机制对目标实体起到状态效果的作用，并且可以在其持续时间内触发其他技能。光环允许你创建自定义状态效果（即增益和减益），并跟踪其持续时间，也可以在其他机制和条件中使用。

1. [属性](aura.md#attributes)
2. [成分](aura.md#components)
3. [附件类型](aura.md#attachment-types)
   1. [ModelEngine附件](aura.md#modelengine-attachment)
4. [ShowBarTimer属性](aura.md#showbartimer-attribute)
5. [示例](aura.md#examples)
6. [别名](aura.md#aliases)

| [已实现的占位符](../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.aura-name>` |
| `<skill.var.aura-type>` |
| `<skill.var.aura-charges>` |
| `<skill.var.aura-duration>` |
| `<skill.var.aura-duration-millis>` |
| `<skill.var.aura-stacks>` |

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| auraName | aura, b, buff, buffname, debuff, debuffname, n, name | 可选名称。若要使用引用特定光环的相关机制和条件，则必须填写。未定义时会分配随机 UUID。 |  |
| components | component, comp | 要应用的光环组件。本页后文会进一步说明。 |  |
| auratype | auragroup, group, type, g | 光环类型，与其名称类似。 |  |
| tags | tag | 光环具有的标签列表，以逗号分隔。标签本身没有作用，但可以用来标记光环，便于后续检查。 |  |
| attachmenttype | attachment, attach | 应用到光环所附加实体上的[附着物](aura.md#attachment-types)。 | NONE |
| onStartSkill | onStart, os | 光环首次开始时执行的元技能。 |  |
| onTickSkill | onTick, ot | 每隔 [interval] 刻在受影响实体上执行的元技能。 |  |
| onEndSkill | onEnd, oe | 光环结束时执行的元技能。 |  |
| ShowBarTimer | bartimer, bt | 设置后，会在光环持续期间为施法者显示状态条。 | false |
| Charges | c | 设置后，光环会在充能次数降至零时消失。此值可由其他机制修改。 | 0 |
| Duration | ticks, t, d, time, t | 光环存在的最长时间，单位为刻。 | 200 |
| Interval | i | 光环触发 onTick 技能的间隔，单位为刻。 | 1 |
| maxStacks | ms | 对同一个目标实体多次施加光环时，可以叠加的次数。 | 1 |
| refreshDuration | rd | 实体再次被施加同一光环时，将光环的持续时间刷新为机制中定义的时长。 | true |
| mergeSameCaster | msc, mc | 将同一实体施加给另一实体的所有同名光环合并为一个光环，防止一个生物在同一实体上多次叠加同一光环。 | `mergeAll`、`overwriteAll` 或 `overwriteSameCaster` 中任意一项为 `true` 时，此项为 `false`。 |
| mergeAll | ma | 将任意实体施加给另一实体的所有同名光环合并为一个光环，防止多个生物在同一实体上多次叠加同一光环。 | false |
| overwriteSameCaster | osc, oc | 施加时，停止同一施法者已施加在目标上的所有相同光环，并用新光环替换，不能与合并选项同时使用。 | false |
| overwriteAll | overwrite, ow | 施加时，停止目标上的所有相同光环，并用新光环替换，不能与合并选项同时使用。 | false |
| CancelOnGiveDamage | cogd | 具有此光环的实体对其他实体造成任何伤害时，取消光环。 | false |
| CancelOnTakeDamage | cotd | 具有此光环的实体受到任何伤害时，取消光环。 | false |
| CancelOnDeath | cod | 具有此光环的实体死亡时，取消光环。 | true |
| CancelOnCasterDeath | cocd | 光环的施法者死亡时，取消光环。 | false |
| CancelOnTeleport | cot | 具有此光环的实体发生任何传送时，取消光环，无论传送由其他机制还是服务器命令触发。 | false |
| CancelOnChangeWorld | cocw | 具有此光环的实体切换世界时，取消光环，通常适用于玩家。 | false |
| CancelOnSkillUse | cosu | 光环生效期间，具有此光环的实体使用其他技能时，取消光环。 | false |
| CancelOnQuit | coq | 具有此光环的实体退出服务器时，取消光环，实际只适用于玩家。 | true |
| DoEndSkillOnTerminate | desot, alwaysrunendskill, ares | 光环被 auraremove 机制移除时，是否执行 onEndSkill。 | true |

## 组件 {#components}

一个光环可以定义多个要使用的组件。每个定义的组件都可以触发额外的元技能并应用特定的功能。

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M15.09 14c.18-.63.66-1.15 1.12-1.62A6 6 0 1 0 7.79 12.38c.45.46.93.98 1.12 1.62"></path></svg>Tip

如果你熟悉 [onDamaged](ondamaged.md) 或 [onAttack](onattack.md) 等机制，那么这对你来说可能听起来很熟悉。事实上，这些机制只是应用了单个特定组件的光环。但是通过使用适当的光环组件，你将能够创建一个同时具有多种此类效果的光环！

组件具有相同的机制语法，并且每个组件都有自己可以定义的特定属性

```yaml
  - aura{auraname=MultiAura;duration=200;interval=10;
      components=[
        - onattack{onattack=[ - particles{p=flame;a=50;s=1} @self ]}
        - ondamaged{ondamaged=[ - particles{p=soulflame;a=50;s=1} @self ]}
        - stat{stat=HEALTH;type=ADDITIVE;value=20}
      ]}
```

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 8h.01"></path></svg>Skill Execution, Charges and Event Modification

事件触发型组件，例如 [OnDamaged](auracomponents/ondamaged.md)、[OnAttack](auracomponents/onattack.md)、[OnShoot](auracomponents/onshoot.md)，只有在**配置的技能成功执行时**，才消耗一次[次数](aura.md#attributes)，并应用 `cancelEvent`、`damageMultiplier` 等事件修改属性。成功执行表示概率判定通过、未在冷却且所有条件满足。技能失败时，触发事件保持原样，不消耗次数。未配置技能时，始终视为执行成功。

| 组件 | 说明 |
| --- | --- |
| [ChunkLoad](auracomponents/chunkload.md) | 在光环持续期间，保持目标所在区块加载。 |
| [Fear](auracomponents/fear.md) | 使目标因恐惧而四处奔跑。 |
| [Fly](auracomponents/fly.md) | 使目标玩家拥有创造模式的飞行能力。 |
| [Glow](auracomponents/glow.md) | 使目标发光。 |
| [OnAttack](auracomponents/onattack.md) | 为目标施加一个光环组件，在其对其他对象造成伤害时触发技能，也可以修改伤害事件本身。 |
| [OnBlockBreak](auracomponents/onblockbreak.md) | 为目标施加一个在其破坏方块时触发技能的光环组件。 |
| [OnBlockPlace](auracomponents/onblockplace.md) | 为目标施加一个在其放置方块时触发技能的光环组件。 |
| [OnChat](auracomponents/onchat.md) | 为目标玩家施加一个在其发送聊天消息时触发元技能的光环组件。 |
| [OnDamaged](auracomponents/ondamaged.md) | 为目标施加一个光环组件，在其受到其他对象的伤害时触发技能，也可以修改伤害事件本身。 |
| [OnDeath](auracomponents/ondeath.md) | 为目标施加一个在其死亡时触发技能的光环组件。 |
| [OnInteract](auracomponents/oninteract.md) | 为目标施加一个光环组件，在其右键点击实体或被玩家右键点击时触发技能。 |
| [OnInput](auracomponents/oninput.md) | 为目标玩家施加一个光环组件，根据其输入触发技能并设置变量。 |
| [OnSwing](auracomponents/onswing.md) | 为目标玩家施加一个在其挥动手臂（左键点击）时触发技能的光环组件。 |
| [OnShoot](auracomponents/onshoot.md) | 为目标施加一个在其发射弹射物时触发技能的光环组件。 |
| [ProjectileRebound](auracomponents/projectilerebound.md) | 将飞向目标的弹射物反弹开，也可以选择将其反弹给发射者。 |
| [Stat](auracomponents/stat.md) | 为目标施加一个向其提供指定属性的光环组件。 |
| [Stun](auracomponents/stun.md) | 暂时将目标固定在原地。 |

## 附着类型 {#attachment-types}

附件是可选的“对象”，应用于（附加）到光环所应用的实体

| 挂接对象 | 别名 | 说明 |
| --- | --- | --- |
| [MODELENGINE](aura.md#modelengine-attachment) | MEG, ME | 一个 ModelEngine 模型。 |

### ModelEngine 附着 {#modelengine-attachment}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| attachmentmodel | attachmodel, model | 附着物的模型。 |  |
| attachmentstate | attachstate, state | 模型将播放的状态。 |  |
| attachmentcolor | attachcolor | 应用于模型的颜色。 |  |
| attachmentscale | attachscale | 模型的缩放比例。 | 1 |
| attachmentViewRadius | attackviewradius | 模型的可视半径。保留为 -1 时，使用 ModelEngine 的默认设置。 | -1 |
| attachmentEnchanted | attachEnchanted, enchanted | 是否为模型应用附魔光效。 | false |
| attachmentGlowing | attachGlowing, glowing | 模型是否发光。 | false |
| attachmentglowcolor | attachglowcolor | `attachmentGlowing` 设为 `true` 时，模型的发光颜色。 |  |
| attachmentCulling | attachCulling, culling | 模型是否可以被 ModelEngine 剔除。 | true |
| attachmentoffset | attachoffset | 模型相对于所附着实体的偏移，格式为 `x,y,z,yaw,pitch`。也可写为 `x,y,z` 或 `x,y,z,yaw`。 | 0,0,0,0,0 |

## ShowBarTimer 属性 {#showbartimer-attribute}

如果设置为`true`，则附加属性可用

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bartimerdisplay | bartimertext | Boss 血条中的文字。 | auraname |
| bartimercolor |  | Boss 血条的[颜色](../../mobs/bossbar.md#color)。 | RED |
| bartimerstyle |  | Boss 血条的[样式](../../mobs/bossbar.md#style)。 | SOLID |

## 示例 {#examples}

```yaml
  Skills:
  - Aura{auraName=Retributing_Light;onTick=RetributingLightDamage;interval=10;duration=240} @self
```

为目标（本例为自身）施加持续 12 秒的 Retributing_Light 光环，每 10 游戏刻（半秒）触发 RetributingLightDamage 技能。

---

```yaml
 Skills:
  - onDamaged{auraName=fire_shield;onHit=FireShield;duration=200;charges=5;multiplier=0.5} @self
```

在此示例中，施法者在 10 秒内接下来受到的 5 次命中，会触发以攻击者为目标的 FireShield 技能，并使该次伤害变为 50%。不过，如果 FireShield 的条件不满足，就会受到正常伤害，因为伤害倍率也不会生效。

---

```yaml
  Skills:
  - onAttack{auraName=fiery_strikes;onHit=FireStrike;duration=200;charges=5;multiplier=2} @self
```

在此示例中，施法者在 10 秒内的接下来 5 次物理命中，会触发以被击中对象为目标的 FireStrike 技能，并造成 200% 伤害。不过，如果 FireStrike 的条件不满足，就会造成普通伤害，因为伤害倍率也不会生效。

## 别名 {#aliases}

- buff
- debuff
