---
title: Shoot
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Shoot
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Shoot {#shoot}

## 说明 {#description}

向目标实体或位置发射箭或物品弹射物，造成伤害。 2.4 版本中的射击机制发生了显着变化。请参阅下文了解添加之前和之后的工作原理。

MM 4.11 为 Shoot 和 Volley 加入了 Projectile 机制中的大部分选项。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t | 要发射的投射物类型。 | arrow |
| damage | d, amount | 投射物造成的伤害 | 5 |
| velocity | v | 投射物的速度 | 1 |
| maxDistance | md | 投射物飞行的最大距离 | 64 |
| poweraffectsvelocity | pav | 生物的强度等级是否影响投射物的速度 | true |
| interval | int, i | 投射物每秒触发 tick-event 的次数 | 4 |
| item |  | 发射的物品，仅适用于部分投射物类型 |  |
| ontickskill | ontick, ot, m, meta, s, skill | 投射物每次 tick/间隔执行的元技能 |  |
| onhitskill | onhit, oh | 投射物命中目标时执行的元技能 |  |
| onendskill | onend, oe | 投射物未命中目标并结束时执行的元技能 |  |
| bounce |  | 投射物命中物体时是否弹跳 | false |
| pickup |  | 是否可以拾取该物品。 | false |
| expiration | duration, expire, e | 投射物落地后保留多少刻才会被移除 | 100 |
| accuracy | ac, a | 投射物的精准度 | 1 |
| knockback | kb | 投射物的击退强度 | 0 |
| piercelevel | pl | 箭可以穿透实体的次数 | 0 |
| verticaloffset | vo | 发射投射物的垂直偏移量 | 0 |
| horizontaloffset | ho | 发射投射物的水平偏移量 | 0 |
| forwardoffset | startfoffset, sfo | 发射投射物的前向偏移量 | 1 |
| sideoffset | soffset, so | 发射投射物的侧向偏移量 | 0 |
| startsideoffset | ssoffset, sso | 发射投射物的侧向偏移量。与上一项相同，但*此参数*支持占位符。 | `sideOffset's value` |
| gravity | g | 投射物是否受重力影响 | true |
| startyoffset | syo | 投射物起点的 y 偏移量 | 0 |
| adjustvelocity | av | 施法者是玩家时，按玩家亲自射击的方式调整速度和方向 | true |
| calculatefiringangle | cfa | 设置此项且投射物启用了 `gravity` 时，投射物会在空中沿弧线飞行后落到目标位置 | false |
| verticalnoise | vn | 发射投射物的垂直扰动（随机性） | ((1-`accuracy`)*45)/10 |
| horizontalnoise | hn | 发射投射物的水平扰动（随机性） | (1-`accuracy`)*45 |
| fromorigin | fo | 是否从机制原点发射投射物 | false |

> 此机制继承 [Damage](damage.md) 机制的所有*可继承*属性。

### Type 属性 {#type-attribute}

弹射物的类型可以是

| 类型 | 别名 |
| --- | --- |
| `ARROW` |  |
| `SNOWBALL` |  |
| `EGG` |  |
| `ENDERPEARL` |  |
| `POTION` | `SPLASH_POTION` |
| `LINGERING_POTION` |  |
| `ITEM` |  |
| `BLOCK` | `FALLING_BLOCK` |
| `TRIDENT` |  |

#### 药水类型属性 {#potion-type-attributes}

如果弹射物为 `type` `POTION`，则这些属性适用

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| potiontype | ptype, effect, pt, pe | 类型为 POTION 时，投射物附带的药水效果类型 | SLOW |
| potionduration | pduration, pd | 药水效果的持续时间 | 100 |
| potionlevel | plevel, lvl, pl | 药水效果的等级 | 1 |
| force | overwrite, ow, override, or | 目标已具有该效果时，是否覆盖原效果 | false |
| potioncolor | pc | 药水的颜色 | #FFFFFF |
| hasParticles | particles | 是否显示状态效果粒子。 | true |
| hasIcon | icon | 是否显示状态效果图标。 | true |
| ambientparticles | ambient | 是否显示环境粒子。 | false |

#### 三叉戟类型属性 {#trident-type-attributes}

如果弹射物为 `type` `TRIDENT`，则这些属性适用

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| tridentitem | titem, ti | 三叉戟物品 |  |

## 示例 {#examples}

```yaml
ArrowBarrage:
  Skills:
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
  - delay 10
  - shoot{type=ARROW;velocity=5;damage=10}
```

## 别名 {#aliases}

- shootprojetile
