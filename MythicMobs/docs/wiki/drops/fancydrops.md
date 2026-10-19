---
title: 花式掉落
source_url: https://wiki.mythiccraft.io/mythicmobs/drops/FancyDrops
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 花式掉落 {#fancy-drops}

你是否觉得掉落物有些*过于*普通，想让它们更加闪亮？本页介绍了实现这些效果的方法！

不过请记住！花式掉落仅适用于 **Mythic、[MMOItems](drops.md#drop-types)、[掉落表](droptables.md)或原版物品**！

1. [掉落选项](fancydrops.md#drop-options)
   1. [DropMethod](fancydrops.md#dropmethod)
   2. [ShowDeathChatMessage](fancydrops.md#showdeathchatmessage)
   3. [ShowDeathHologram](fancydrops.md#showdeathhologram)
   4. [PerPlayerDrops](fancydrops.md#perplayerdrops)
   5. [ClientSideDrops](fancydrops.md#clientsidedrops)
   6. [Lootsplosion](fancydrops.md#lootsplosion)
   7. [HologramItemNames](fancydrops.md#hologramitemnames)
   8. [ItemGlowByDefault](fancydrops.md#itemglowbydefault)
   9. [ItemBeamByDefault](fancydrops.md#itembeambydefault)
   10. [ItemVFXByDefault](fancydrops.md#itemvfxbydefault)
   11. [ItemVFX](fancydrops.md#itemvfx)
   12. [RequiredDamagePercent](fancydrops.md#requireddamagepercent)
   13. [HologramTimeout](fancydrops.md#hologramtimeout)
   14. [HologramMessage](fancydrops.md#hologrammessage)
   15. [ChatMessage](fancydrops.md#chatmessage)
2. [掉落属性](fancydrops.md#drop-attributes)
   1. [时运（Fortune）](fancydrops.md#fortune)
   2. [示例](fancydrops.md#example)

## 掉落选项 {#drop-options}

生物配置中有一个额外的 `DropOptions` 字段，可以用来设置掉落相关的各种行为。

```yaml
  DropOptions:
    DropMethod: FANCY
    ShowDeathChatMessage: false
    ShowDeathHologram: false
    PerPlayerDrops: false
    ClientSideDrops: false
    Lootsplosion: false
    HologramItemNames: false
    ItemGlowByDefault: false
    ItemBeamByDefault: false
    ItemVFXByDefault: false
    ItemVFX:
      Material: STONE
      Model: 0
    RequiredDamagePercent: 0.1
    HologramTimeout: 6000
    HologramMessage:
    - ...
    - ...
    ChatMessage:
    - ...
    - ...
```

### DropMethod {#dropmethod}

可以设为以下两个值之一：

- `VANILLA`：保留所有“普通”的掉落行为。
- `FANCY`：启用伤害追踪、计分板以及更高级的掉落效果。如果相关配置允许，还可以为每位参与者分别抽取掉落，而不是只抽取一次。

因此，要让本页其余功能生效，必须将此项设为 `FANCY`。默认值为 `VANILLA`。

```yaml
  DropOptions:
    DropMethod: FANCY
```

### ShowDeathChatMessage {#showdeathchatmessage}

是否向玩家显示死亡聊天消息。默认值为 `false`。

```yaml
  DropOptions:
    ShowDeathChatMessage: true
```

### ShowDeathHologram {#showdeathhologram}

是否向玩家显示死亡全息文字。默认值为 `false`。

```yaml
  DropOptions:
    ShowDeathHologram: true
```

### PerPlayerDrops {#perplayerdrops}

是否为每位参与的玩家分别计算生物掉落。也就是说，每位玩家都会单独抽取一次掉落。

> **此功能[仅限 Paper](https://papermc.io/downloads/all)！**

```yaml
  DropOptions:
    PerPlayerDrops: true
```

### ClientSideDrops {#clientsidedrops}

是否以客户端方式为每位玩家分别显示掉落物。启用后，每位玩家只能看见自己获得的战利品。

```yaml
  DropOptions:
    ClientSideDrops: false
```

### 掉落物喷发（Lootsplosion） {#lootsplosion}

掉落物是否默认使用战利品喷发效果。

```yaml
  DropOptions:
    Lootsplosion: true
```

### HologramItemNames {#hologramitemnames}

物品是否默认显示全息名称。

```yaml
  DropOptions:
    HologramItemNames: true
```

### ItemGlowByDefault {#itemglowbydefault}

物品是否默认发光。使用此选项似乎会给掉落的物品添加 NBT，导致它们无法与通过其他方式获得的物品堆叠。

```yaml
  DropOptions:
    ItemGlowByDefault: true
```

### ItemBeamByDefault {#itembeambydefault}

物品是否默认显示光束。

```yaml
  DropOptions:
    ItemBeamByDefault: true
```

### ItemVFXByDefault {#itemvfxbydefault}

物品是否默认显示视觉特效。

```yaml
  DropOptions:
    ItemVFXByDefault: true
```

### ItemVFX {#itemvfx}

物品默认视觉特效的相关选项。

```yaml
  DropOptions:
    ItemVFX:
      Material: STONE # The default material of the vfx
      Model: 0 # The default model of the vfx
```

### RequiredDamagePercent {#requireddamagepercent}

为特定玩家生成掉落所需的最低伤害，以生物生命值的百分比表示。

```yaml
  DropOptions:
    RequiredDamagePercent: 0.1
```

### HologramTimeout {#hologramtimeout}

生物死亡时生成的全息文字在多长时间后消失。默认值为 `6000`。

```yaml
  DropOptions:
    HologramTimeout: 6000
```

### HologramMessage {#hologrammessage}

生物死亡时生成的全息文字的内容。支持使用特定占位符。

```yaml
  DropOptions:
    HologramMessage:
    - '<#FF9B00>========================'
    - '<mob.name> - <mob.hp>HP'
    - ''
    - '<#FFA300>1st Place | <1.name> | <1.damage>'
    - '<#D1FFFF>2nd Place | <2.name> | <2.damage>'
    - '<#D1FFFF>3rd Place | <3.name> | <3.damage>'
    - '<#E57A00>4th Place | <4.name> | <4.damage>'
    - '<#E57A00>5th Place | <5.name> | <5.damage>'
    - ''
    - 'Your rank: #<player.rank> | <player.damage>'
    - '<#FF9B00>========================'
```

> 如果指定排名没有玩家（例如，参与击杀生物的玩家少于 5 人），则不会显示使用该占位符的那一行。

### ChatMessage {#chatmessage}

生物死亡时向玩家发送的消息内容。支持使用特定占位符。

```yaml
  DropOptions:
    ChatMessage:
    - '<#F28800>===================================='
    - '<#FFA300>BOSS DEFEATED!'
    - '<#F2B600><mob.name>'
    - ''
    - '<#ffe259>1st Place »<#ffe259> <1.name> - <1.damage>'
    - '<#D1FFFF>2nd Place »<#D1FFFF> <2.name> - <2.damage>'
    - '<#D1FFFF>3rd Place »<#D1FFFF> <3.name> - <3.damage>'
    - '<#E57A00>4th Place »<#E57A00> <4.name> - <4.damage>'
    - '<#E57A00>5th Place »<#E57A00> <5.name> - <5.damage>'
    - ''
    - '<#F2B600>Your rank: #<player.rank> - <player.damage> (<pity> Pity)'
    - '<#F28800>===================================='
```

> 如果指定排名没有玩家（例如，参与击杀生物的玩家少于 5 人），则不会显示使用该占位符的那一行。

## 掉落参数 {#drop-attributes}

除了上述选项，还可以通过行内属性，为生物的每项掉落单独设置行为。

```yaml
  Drops:
  - amber_1{itemglow=true;itemglowcolor=GOLD;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
```

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| lootsplosion | lootsplosionenabled, ls | 掉落物生成后是否向外移动 |  |
| clientsidedrops | clientsidedropsenabled, csd | 掉落物是否仅在客户端显示 |  |
| hologramname | hologramnameenabled, hn | 掉落物是否显示名称全息图 |  |
| itemglow | itemglowenabled, ig | 掉落物是否发光 |  |
| itemglowcolor | glowcolor, gc | 发光的颜色（如果已设置） |  |
| itembeam | itembeamenabled, ib | 掉落物是否在自身上方生成粒子光束 |  |
| itembeamcolor | beamcolor, bc | 光束的颜色（如果已设置） |  |
| itemvfx | ivfx, vfx | 掉落物是否显示物品视觉效果 |  |
| vfxmaterial | vfxmat, vfxm | 视觉效果的材质 |  |
| vfxdata | vfxd | 视觉效果的数据 | 0 |
| vfxmodel | vfxitemmodel | 视觉效果的物品模型。Minecraft 1.21.3+ |  |
| vfxcolor | vfxc, color | 视觉效果的颜色 |  |
| pityModifier | pitymod, pmod | 保底值的修正量 | 0.0 |
| resetpity | resetp, rp | 是否重置保底值 | false |
| pcategory | pitycategory, category | 保底类别 | DEFAULT |
| damage | mindamage, min | 玩家至少需要对生物造成多少伤害，才有资格生成此掉落物 | 0.0 |
| top | placement, required | 玩家需要在伤害排行榜中达到的名次，才有资格生成此掉落物 | 2147483647 |
| billboarding | billboard, bill | 全息图的[面向模式（Billboarding）](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Display.Billboard.html) | VERTICAL |
| brightness | bright, b | 全息图的亮度 | 0 |
| fortune |  | 此掉落物是否受时运附魔影响 | false |
| fortuneMod |  | 每级时运附魔对掉落数量的影响 |  |

### 时运 {#fortune}

时运掉落数量的计算方式：

```math
  amount = min(1, floor(<random.float.0to1> * (2 + fortuneLevel) * fortuneMod ) ) * amount
```

### 示例 {#example}

```yaml
  Drops:
  - amber_1{itemglow=true;itemglowcolor=GOLD;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - adamantium_ore{itemglow=true;itemglowcolor=WHITE;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - amethyst_1{itemglow=true;itemglowcolor=YELLOW;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - andesite_bricks{itemglow=true;itemglowcolor=LIGHT_PURPLE;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - bananarang{itemglow=true;itemglowcolor=RED;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - augment_sword_midas_6{itemglow=true;itemglowcolor=AQUA;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - blue_stained_tiles{itemglow=true;itemglowcolor=GREEN;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - black_stained_tiles{itemglow=true;itemglowcolor=BLUE;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxdata=21;vfxc=#55ff55} 1 1
  - bismuth_2{itemglow=true;itemglowcolor=DARK_RED;hn=true;lootsplosion=true;vfxmaterial=POTION;vfxmodel="mythic:effects/item_beam_3"} 1 1
```
