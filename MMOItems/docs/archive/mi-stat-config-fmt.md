---
title: 剑与武器属性示例
source: https://docs.phoenixdevt.fr/archive/mi-stat-config-fmt
source_snapshot: '2026-10-19'
---

# 剑与武器属性示例 {#sword-weapon-stat-examples}

*如果有遗漏，请在支持不和谐中联系我。*

```
WIKISWORD:  
  base:  
    material: NETHERITE_SWORD
```

> 材料字段是你插入希望物品成为的Minecraft材料类型的位置，这意味着它支持当前 MC 版本中的所有有效材料枚举。

```
    revision-id: 2
```

>revision-id字段定义你的物品当前的“版本”。这取决于你的意愿，并且玩家具有的任何物品与编辑器中设置的修订版ID不匹配，将在交互时更新到最新版本。

```
    durability: 100.0
```

>耐久度字段尽管名称有点烦人，但它是在1.14自定义模型数据之前执行自定义纹理的旧方法。它设置物品的物理电流耐久度，并且不影响实际最大耐久度。

```
    custom-model-data: 5.0
```

> 对于自定义模型数据，此字段是不言自明的。

```
    max-durability: 1000.0
```

>Max-durability是你为此物品设置自定义耐久度的位置。

```
    will-break: true
```

> 自定义耐久度降到 0 时，物品是直接损坏，还是仅变为无法使用？

```
    name: '&cThis is a test sword.'
```

>物品的显示名称。

```
    lore:
    - reeee
    - fffffffff
```

>物品的描述，在列表中给出。当然支持颜色代码。

```
    custom-nbt:
    - NBT_TAG_KEY TAG_VALUE
```

> 你可以在此处设置任意和自定义的NBT标签以支持外部插件，或使用Minecraftcan-place系统等。

```
    lore-format: lore-format
```

> 你可以在此处输入lore-formats文件夹中的自定义lore-format文件，以便不同的物品类型可以具有不同的格式。极致定制。

```
    displayed-type: Fake Type Here
```

> 你可以在此处放置任意“Kings Sword”或其他内容，而不是像 SWORD 那样显示物品的实际物品类型。

```
    enchants:
      sharpness: 1.0
      mending: 2.0
```

>物品上的结界缩进列表。

```
    hide-enchants: true
```

> 是否应该隐藏附魔只是为了让物品发光。

```
    permission:
    - useme.sword
```

> 你需要什么权限才能使用此物品？

```
    item-particles:
      type: FIREFLIES
      particle: FLAME
      amount: 5.0
      radius: 1.4
      speed: 1.0
      rotation-speed: 2.0
      height: 2.0
```

> 可以在物品上运行的物品粒子列表，所有有效类型均通过游戏中的 list 命令给出，粒子是Minecraft的所有有效粒子类型。不同的粒子有不同的修饰符，除非你使用游戏编辑器中方便的花花公子，否则无法知道哪些粒子有效。

```
    disable-interaction: true
```

> 是否应该禁用与此物品的交互，例如放置方块。

```
    disable-crafting: true
```

> 这个物品可以用在合成配方上吗？

```
    disable-smelting: true
```

> 这个物品应该用来熔炼吗？

```
    disable-smithing: true
```

> 这个物品可以用于锻造吗？

```
    disable-enchanting: true
```

> 这个物品应该是附魔的吗？

```
    disable-repairing: true
```

> 这个物品应该可以修复/重命名吗？

```
    disable-attack-passive: true
```

> 是否应关闭此物品的MMOItems钝/砍/刺攻击被动效果。

```
    required-level: 5.0
```

> 兼容的RPG插件所需的等级，或原版经验等级。

```
    required-class:
    - ARCHER
```

> 兼容的 RPG 插件所要求的职业。

```
    attack-damage: 10.0
```

> 设置击中时武器底座攻击伤害，或射击时箭伤害。

```
    attack-speed: 10.0
```

>攻击速度的每秒攻击次数为物品。

```
    critical-strike-chance: 5.0
```

> 有机会出现暴击。

```
    critical-strike-power: 5.0
```

> 由暴击完成的额外倍增，与MythicLibconfig.yml的底座相结合

```
    block-power: 5.0
```

> 该物品可以阻挡的伤害百分比。

```
    block-rating: 5.0
```

> 再次，它实际阻止的机会与MythicLibconfig.yml的底座相结合

```
    block-cooldown-reduction: 5.0
```

> 从config.ymlmyticlib 的基础上额外减少块冷却时间。

```
    dodge-rating: 5.0
```

> 完全躲避攻击的机会。

```
    dodge-cooldown-reduction: 5.0
```

> 从config.ymlMythiclib 中的基础上额外减少闪避冷却时间。

```
    parry-rating: 5.0
```

> 有机会招架攻击，这会抵消伤害并击退攻击者。

```
    parry-cooldown-reduction: 5.0
```

> 在你知道的训练中，从基础上额外减少招架冷却时间。

```
    cooldown-reduction: 5.0
```

> 减少物品和玩家技能的冷却时间(%)

```
    mana-cost: 5.0
```

>魔力使用所述物品的成本。

```
    stamina-cost: 5.0
```

>耐力使用所述物品的成本。

```
    pve-damage: 5.0
```

> 对非人类实体的额外伤害百分比

```
    pvp-damage: 5.0
```

> 对人类实体的额外伤害%

```
    weapon-damage: 5.0
```

> 额外基础武器伤害（%）

```
    skill-damage: 5.0
```

> 额外的 mmoitems 能力伤害（%）

```
    projectile-damage: 5.0
```

> 额外的技能/武器射弹伤害。

```
    magic-damage: 5.0
```

> 额外魔法能力和法杖伤害（%）

```
    physical-damage: 5.0
```

> 附加能力/武器物理（近战）伤害。

```
    defense: 100.0
```

> 防御给出，公式在mythiclibconfig.yml中设置

```
    damage-reduction: 5.0
```

> 总体伤害减少百分比

```
    fall-damage-reduction: 5.0
```

> 坠落伤害减少百分比

```
    projectile-damage-reduction: 5.0
```

> 射弹伤害减少%

```
    physical-damage-reduction: 5.0
```

> 物理（近战）伤害减少百分比

```
    fire-damage-reduction: 5.0
```

> 火焰伤害减少%

```
    magic-damage-reduction: 5.0
```

> 药水伤害减少%

```
    pve-damage-reduction: 5.0
```

> 仅来自小怪的伤害减少%。

```
    pvp-damage-reduction: 5.0
```

> PVP 受到的伤害减少%。

```
    undead-damage: 5.0
```

> 增加对不死生物的伤害%

```
    unbreakable: true
```

>物品牢不可破吗？

```
    tier: RARE
```

> 设置物品的等级。

```
    set: STARTER
```

> 设置物品的设置。

```
    armor: 5.0
```

> 设置物品的护甲值，视觉上上限为20，功能上上限为30。

```
    armor-toughness: 5.0
```

>护甲韧性原版基础属性，这有一些糟糕的公式 idk。

```
    max-health: 10.0
```

> 增加最大生命值，添加剂。

```
    unstackable: true
```

> 这个物品应该可以堆叠吗？

```
    max-mana: 20.0
```

> 增加魔力，如最大生命值。

```
    knockback-resistance: 0.7
```

> 否定击退,0.7的几率是70%

```
    movement-speed: 0.2
```

> 添加到玩家、原版的移动速度为0.1

```
    two-handed: true
```

> 如果这个物品是两只手，也就是说你不能用它来副手做某事。

```
    equip-priority: 5.0
```

> 新装备优先级属性，详细信息在单独的 wiki 页面上。

```
    perm-effects:
      POISON: 1.0
```

> 给持有者带来效果。为什么你想要毒药1？我不知道。

```
    granted-permissions:
    - tempperm.ree
```

> 持有/佩戴时给予临时权限。

```
    item-cooldown: 10.0
```

> 这以秒为单位，适用于消耗品和物品命令。

```
    crafting:
      shaped:
        '1':
        - diamond AIR AIR
        - AIR diamond AIR
        - AIR AIR netherite_block
      shapeless:
        '1':
        - AIR
        - AIR
        - AIR
        - AIR
        - nether_star
        - AIR
        - AIR
        - slime_ball
        - AIR
      furnace:
        '1':
          item: COAL
          time: 200
          experience: 10.0
      blast:
        '1':
          item: COAL
          time: 200
          experience: 10.0
      smoker:
        '1':
          item: COAL
          time: 200
          experience: 10.0
      campfire:
        '1':
          item: COD
          time: 100
          experience: 10.0
      smithing:
        '1':
          input1: DIAMOND_SWORD
          input2: DIAMOND
```

> 所有合成配方类型。

```
    craft-permission: youneedthis.tocraft
```

> 制作权限，呃。

```
    crafted-amount: 10.0
```

> 它应该制作多少这个 mmoiite。

```
    sounds:
      on-attack:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-pickup:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-consume:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-right-click:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-left-click:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-item-break:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-block-break:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-craft:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
      on-placed:
        sound: entity.generic.drink
        volume: 1.0
        pitch: 1.0
```

> 添加自定义声音。

```
    element:
      fire:
        damage: 10.0
      earth:
        defense: 10.0
```

> 元素伤害/防御。该系统正在重新设计。

```
    commands:
      cmd0:
        format: -d1 bc Hello, this is a test command.
        delay: 0.0
        op: true
      cmd1:
        format: -d1 bc Hello, this is a test command from console.
        delay: 0.0
        console: true
```

> 右键单击​​时将命令添加到物品。

```
    gem-sockets:
    - RED
    - GREEN
    - Poop
```

> 添加任意宝石插槽以匹配你的宝石。

```
    repair-type: EXAMPLE_REPAIR_STAT
```

> 此repair-type属性需要与你正在修复的消耗品匹配，或者留空以匹配所有。

```
    ability:
      ability1:
        type: BLOODBATH
        mana: 3.0
        mode: RIGHT_CLICK
```

> 这是能力格式，很像粒子，而不是用可能的修饰符输入所有90。使用GUI。

```
    upgrade:
      workbench: true
```

> 请参阅有关物品升级的 wiki 页面，并首先使用GUI来学习配置。这里要解释的太多了。

```
    health-regeneration: 10.0
```

>MMOCore生命恢复百分比

```
    mana-regeneration: 10.0
```

>MMOCore魔力再生百分比

```
    max-stamina: 10.0
```

>MMOCore最大耐力添加剂。

```
    stamina-regeneration: 10.0
```

>MMOCore耐力再生百分比。

```
    additional-experience: 50.0
```

> 额外的MMOCore经验（%）。

```
    faction-damage-enemy: 50.0
```

> 设置mythicmobs派别在这里增加。

```
    required-dexterity: 10.0
    required-strength: 10.0
```

> 需要MMOCore基础属性。

```
    profession-enchanting: 10.0
    profession-smithing: 10.0
    profession-mining: 10.0
```

> 需要MMOCore副职业。

**消耗品添加的额外属性**

```
WIKICONSUMABLE:
  base:
    material: APPLE
    disable-right-click-consume: true
```

> 这个消耗品应该可以右键食用吗？

```
    restore-health: 10.0
```

> 吃东西能恢复多少生命值？

```
    restore-food: 10.0
```

> 进食后可恢复多少食物。

```
    restore-saturation: 10.0
```

> 进食时要恢复多少饱和度？

```
    restore-mana: 10.0
```

> 吃东西能恢复多少魔力？

```
    restore-stamina: 10.0
```

> 吃东西能恢复多少耐力？

```
    can-identify: true
```

> 这个物品可以用来识别身份不明的物品吗？

```
    can-deconstruct: true
```

> 此物品可以用于分解其他物品吗？

```
    can-deskin: true
```

> 这个物品可以去除物品的皮肤吗？

```
    effects:
      REGENERATION:
        duration: 100.0
        amplifier: 1.0
```

> 消耗时给出的效果列表。

```
    soulbinding-chance: 100.0
```

> 有机会灵魂束缚物品。

```
    soulbound-break-chance: 100.0
```

> 如果失败的话可能会损坏。

```
    soulbound-level: 1.0
```

> 要应用的灵魂绑定等级。

```
    item-cooldown: 5.0
```

> 吃饭时冷却时间。

```
    vanilla-eating: true
```

>原版吃动画？仅适用于通常可以食用的材料。

```
    inedible: true
```

> 不可食用

```
    max-consume: 5.0
```

>物品有多少用途？

```
    repair: 100.0
```

> 这款物品能修复多少定制硬脑膜？

```
    repair-type: EXAMPLE_STAT
```

> 哪个物品可以修复，接收的物品需要有配套的repair-type。

**额外的属性由弓添加**

```
ELF_KINGS_LOST_BOW:
  base:
    material: BOW
    name: '&aElf King''s Lost Bow'
    arrow-particles:
      particle: FLAME
      amount: 5
      offset: 1.0
      speed: 1.0
```

> 在空气中飞行时的颗粒。

```
    arrow-velocity: 100.0
```

> 弓可以射多远。

```
    arrow-potion-effects:
      POISON:
        duration: 100.0
        amplifier: 1
```

> 药水会影响弓击中时的效果。

---

原文：[Sword / Weapon Stat Examples](https://docs.phoenixdevt.fr/archive/mi-stat-config-fmt) · 原文归档：2026-10-19
