---
title: Projectile
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Projectile {#projectile}

## 说明 {#description}

Projectile 发射可用粒子与声音装饰的元弹射物，适合制作暗影箭、冰球、流星等复杂技能。它拥有比其他机制更多的选项，初次配置可能较难。命中阻挡它的实体或位置后会消失，可通过 `stopatblock`、`stopatentity`、`stopconditions` 等属性调整。

[Missile](missile.md)、[Totem](totem.md) 等机制是此机制的扩展，因此可以使用大量相同属性，具体见[可继承属性](projectile.md#inheritable-attributes)。

1. [属性](projectile.md#attributes)
   1. [可继承属性](projectile.md#inheritable-attributes)
   2. [弹丸特定属性](projectile.md#projectile-specific-attributes)
2. [特别提示](projectile.md#special-notes)
3. [弹射物子弹](projectile.md#projectile-bullets)
   1. [子弹通用属性](projectile.md#universal-bullet-attributes)
   2. [ARROW子弹](projectile.md#arrow-bullet)
   3. [BLOCK子弹](projectile.md#block-bullet)
   4. [SMALLBLOCK子弹](projectile.md#smallblock-bullet)
   5. [ITEM子弹](projectile.md#item-bullet)
   6. [MOB子弹](projectile.md#mob-bullet)
   7. [TRACKING子弹](projectile.md#tracking-bullet)
   8. [REALTRACKING子弹](projectile.md#realtracking-bullet)
   9. [DISPLAY子弹](projectile.md#display-bullet)
   10. [ME子弹](projectile.md#me-bullet)
   11. [TEXT子弹](projectile.md#text-bullet)
4. [示例](projectile.md#examples)
5. [别名](projectile.md#aliases)

## 属性 {#attributes}

### 可继承的属性 {#inheritable-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onStartSkill | onStart, oS | 弹射物开始时，在其原点位置执行的元技能。 |  |
| onTickSkill | onTick, oT, m, meta, s, skill | 每隔 [interval] 刻在弹射物原点位置执行的元技能。 |  |
| onHitSkill | onHit, oH | 弹射物命中允许命中的实体时执行的元技能。元技能会继承被命中的目标。 |  |
| onEndSkill | onEnd, oE | 弹射物结束时执行的元技能。 |  |
| onBounceSkill | onBounce | 弹射物弹跳时执行的元技能。**仅 Premium 版**支持。 |  |
| onHitBlockSkill | onHitBlock, ohb | 弹射物命中方块时执行的元技能。 |  |
| onInteractSkill | onInteract | 与弹射物交互时执行的元技能。 |  |
| BulletType | bullet, b | 弹体类型。设置后，会根据指定类型提供额外属性。弹体类型及其相关属性列表见[下文](projectile.md#projectile-bullets)。 |  |
| Interval | int, i | 弹射物更新位置的间隔，单位为刻。 | 1 |
| HorizontalRadius | hRadius, hR, r | 弹射物周围可命中实体的水平半径。 | 1.25 |
| VerticalRadius | vRadius, vR | 弹射物周围可命中实体的竖直半径。 | 1.25 |
| Duration | maxDuration, md, d | 弹射物存在的最长时间，单位为刻。 | 400 |
| MaxRange | mr | 弹射物的最大飞行距离，单位为格。 | 40 |
| Velocity | v | 弹射物的速度，以每秒移动的方块数表示。 | 5 |
| DeathDelay | death, dd | 弹射物终止时，延迟移除其弹体。 | 2 |
| StartYOffset | syo | 调整弹射物在施法生物身上的发射位置偏移。 | 1 |
| StartFOffset | forwardoffset, sfo | 弹射物在生物前方多远处开始。 | 1 |
| TargetYOffset | tyo, targety | 调整弹射物射向目标的具体位置偏移。 | 0 |
| SideOffset | soffset, so | 未为 StartSideOffset 和 EndSideOffset 指定值时，它们会继承此属性的值。 | 0 |
| StartSideOffset | ssoffset, sso | 弹射物在生物侧面多远处开始。 | sideoffset |
| EndSideOffset | endoffset, esoffset, eso | 弹射物最终到达目标位置侧面多远处。 | sideoffset |
| startingdirection | startingdir, startdir, sdir | 弹射物的初始方向。目前仅在被 missile 机制继承时生效。 | @Targeted |
| HorizontalOffset | hO | 水平偏移会绕 360 度轴旋转弹射物的水平初速度。 | 0 |
| VerticalOffset | vO | 竖直偏移会为弹射物的初始方向添加一个[斜率](https://en.wikipedia.org/wiki/Grade_(slope))。若要指定角度，可参考[此图](https://en.wikipedia.org/wiki/Grade_(slope)#/media/File:Slope_quadrant.svg)：所需值为图中红色数字除以 100，例如想要 40°，应输入 83.9/100 = `0.839`。 | 0 |
| Accuracy | ac, a | 决定弹射物的精度。 | 1 |
| HorizontalNoise | hn | 弹射物在水平方向上的随机程度。 | (1-ac)*45 |
| VerticalNoise | vn | 弹射物在竖直方向上的随机程度。 | (1-ac)*4.5 |
| StopAtEntity | sE | 弹射物命中可作为目标的实体时是否停止。 | true |
| StopAtBlock | sB | 弹射物命中不透明方块时是否停止。 | true |
| PowerAffectsRange | par | 生物的[威力等级](../../mobs/power.md)是否影响弹射物的射程。 | true |
| PowerAffectsVelocity | pav | 生物的[威力等级](../../mobs/power.md)是否影响弹射物的速度。 | true |
| Interactable |  | 弹射物是否可以交互。 | false |
| HitSelf |  | 弹射物是否可以命中施法者。 | false |
| HitPlayers | hp | 弹射物是否可以命中玩家。 | true |
| HitNonPlayers | hnp | 弹射物是否可以命中非玩家实体。 | false |
| HitTarget | ht | 弹射物是否可以命中机制的目标。 | true |
| HitTargetOnly | hto | 弹射物是否**只能**命中机制的目标。 | false |
| ImmuneDelay | immune, id | 设置命中免疫间隔，即目标可以再次被弹射物命中前需等待的时间。 | 2000 |
| hitConditions | conditions, cond, c | 目标必须满足这些条件，弹射物才能命中它。**仅 Premium 版**机制。 |  |
| stopconditions | stpcond | 目标必须满足这些条件，弹射物才会在命中它时结束。 | null |
| hitBlockConditions | hbcond | 针对弹射物将要停止处的方块位置检查的条件列表。仅在弹射物因方块而停止时（`stopAtBlock`）适用；任意条件未通过时，弹射物会穿过该位置，而不是在那里停止。**仅 Premium 版**支持。 |  |
| doEndSkillOnHit | esoh | 弹射物因命中实体而结束时，是否执行 onEnd 元技能。 | true |
| fromorigin | fo | 弹射物是否从机制的原点开始。 | false |
| requireLineOfSight | rlos, los, requirelos | 起点是否必须能直视原点。可设为 `true`、`false`、`PLAYERS_ONLY`。 | PLAYERS_ONLY |
| drawHitbox |  | 绘制弹射物的碰撞箱，便于调试。 | false |
| tickinterpolation | interpolation, ti | 在弹射物相邻两次刻更新之间插入指定数量的额外点，并在这些点上同样应用 onTick 和 onHit 技能。可用于填补高速弹射物的间隙，防止跳过实体。 | 0 |
| shareSubHitboxCooldown | shcd | 所有 meg 子碰撞箱是否与基础实体共用相同的命中免疫间隔。 | true |
| hitTargeter | htr | 实体目标选择器。弹射物命中后，所选实体会成为 onHit 元技能的目标，并像弹射物的主要目标一样获得命中免疫间隔。 |  |

### 投射物专用属性 {#projectile-specific-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| Type |  | 弹射物的“type”。默认弹射物从生物所在位置射向目标；METEOR 类型弹射物则从目标上方的天空落下。 | NORMAL |
| gravity | g | 决定弹射物的重力。可用小数（0.1-0.2）设置较低重力。 | 0 |
| Bounces | bounce | 弹射物是否弹跳。弹跳半径取决于弹射物的碰撞箱。**仅 Premium 版**支持。 | false |
| BounceVelocity | bv | 弹射物每次弹跳时，其速度都会乘以此值。**仅 Premium 版**支持。 | 0.9 |
| HugSurface | hs | 弹射物是否沿地面移动。 | false |
| HugLiquid | hugwater, huglava | 使用 hugSurface 时，也会在液体表面移动。 | false |
| HeightFromSurface | hfs | 对于 NORMAL 弹射物，此项表示 HugSurface 设为 TRUE 时，弹射物在表面上方滑行的高度；对于 METEOR 弹射物，此项表示弹射物在目标上方的初始高度。 | 0.5 |
| MaxClimbHeight | mch | 弹射物贴着方块或液体表面移动时，在自行终止前尝试**升高**其 y 坐标的次数。 | 3 |
| MaxDropHeight | mdh | 弹射物贴着方块或液体表面移动时，在自行终止前尝试**降低**其 y 坐标的次数。 | 10 |
| highAccuracyMode | ham | 是否使用高精度模式。此模式每刻执行射线检测，保证弹射物不会穿过任何物体。可设为 `true`、`false`、`PLAYERS_ONLY`。 | PLAYERS_ONLY |

## 特别说明 {#special-notes}

**onStart 技能：**onStart 的处理方式比较特殊。由它启动的、具有持续时间的增益或特殊效果机制，例如 ParticleTornado，会在持续期间附着于弹射物。

**对于onTick技能：**使用**@origin**目标选择器将导致任何技能或效果瞄准弹射物的位置。这是配置弹射物外观的预期方法。

**onHit 技能：**命中的目标会自动成为技能的继承目标。在 onHit 技能中另行指定目标，会覆盖这些目标，可能导致技能不符合预期。

**对于onEnd技能：**弹丸末端的特效也使用**@origin**。另外，如果你希望以某种方式击中弹射物末端附近的实体（例如最终的大型火球爆炸），你可以使用 **@PlayersNearOrigin{r=[radius]}** 瞄准器。

**类型：**
弹射物分为普通和 Meteor（流星）两种。Meteor 弹射物生成在目标上方，而不是发射它的生物所在位置。因此，Meteor 弹射物无法使用某些属性，具体哪些属性仍有待进一步测试。

## 投射物弹体 {#projectile-bullets}

代表弹射物的子弹类型。这些可以通过 BulletType 属性指定。这些与弹射物、导弹和轨道力学一起工作。

| BulletType | 别名 | 说明 |
| --- | --- | --- |
| [ARROW](projectile.md#arrow-bullet) |  | 弹体为 Minecraft 弹射物。 |
| [BLOCK](projectile.md#block-bullet) |  | 弹体为方块。 |
| [SMALLBLOCK](projectile.md#smallblock-bullet) |  | 弹体为小型方块。 |
| [ITEM](projectile.md#item-bullet) | MYTHICITEM | 弹体为物品或 MythicItem。 |
| [MOB](projectile.md#mob-bullet) |  | 弹体为生物。如果是 Mythicmobs 生物，会保留其技能。 |
| [TRACKING](projectile.md#tracking-bullet) | ARMOR_STAND, ARMORSTAND, PSTAND | 弹体为物品，但其旋转角度会根据弹射物的方向调整。 |
| [REALTRACKING](projectile.md#realtracking-bullet) | RTRACKING, REAL_ARMOR_STAND, REALARMORSTAND, STAND | 同上，但会生成真实的盔甲架，而不是使用数据包。 |
| [DISPLAY](projectile.md#display-bullet) |  | 弹射物为展示实体。 |
| [TEXT](projectile.md#text-bullet) |  | 弹射物会显示一行文字。 |
| [ME](projectile.md#me-bullet) | MEG, MODELENGINE | 弹射物为 [ModelEngine](https://wiki.mythiccraft.io/modelengine) 模型。 |

Examples:

```yaml
  - projectile{bulletType=ARROW;arrowType=TRIDENT;...}
  - projectile{bulletType=BLOCK;material=STONE;...}
  - projectile{bulletType=ITEM;material=MyMythicItem;...}
  - projectile{bulletType=MOB;mob=SkeletonKing;...}
```

### 通用弹体属性 {#universal-bullet-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bulletforwardoffset | bulletfo, bulletoffset, bfo | 弹体的偏移。 | 1.8 |
| bulletYOffset | byo | 弹体的 Y 轴偏移。 | 0 |

### ARROW 弹体 {#arrow-bullet}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| arrowtype | bulletarrowtype | 要使用的弹射物类型，可以为 `NORMAL`、`SPECTRAL`、`TRIDENT`。 | NORMAL |

### BLOCK 弹体 {#block-bullet}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bulletmaterial | material, mat | 弹体的材质。 | STONE |
| bulletspin | bspin | 弹体的自转。 | 0 |
| audience |  | 弹体的[可见对象](../audience.md)。 | world |

### SMALLBLOCK 弹体 {#smallblock-bullet}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bulletmaterial | material, mat | 弹体的材质。 | STONE |
| audience |  | 弹体的[可见对象](../audience.md)。 | world |

### ITEM 弹体 {#item-bullet}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bulletmaterial | material, mat | 弹体的材质，可以是原版物品类型或自定义 MythicItem。 | STONE |
| bulletModel | model | 材质的 CustomModelData 整数值；模型字符串应改在 MythicItem 上定义。 | 0 |
| bulletColor |  | 材质的颜色，须材质支持此项。 |  |
| bulletmatchdirection | bmd, bulletsmall | 弹体是否朝向弹射物的朝向。 | false |
| bulletEnchanted | enchanted | 材质是否带有附魔。 | false |
| audience |  | 弹体的[可见对象](../audience.md)。 | world |

### MOB 弹体 {#mob-bullet}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| mob | mobType, mm | 弹体所用的生物。 | SkeletalKnight |
| bulletspin | bspin | 弹体的自转。 | 0 |
| bulletmatchdirection | bmd | 弹体是否朝向弹射物的朝向。 | false |
| bulletKillable | bk | 允许其他实体对弹射物弹体造成伤害。 | false |
| bulletYOffset | byo | 弹体生物的 Y 轴偏移。 | 1.35 |
| bulletForwardOffset | bfo | 弹体生物的向前偏移。 | 1.35 |

### TRACKING 弹体 {#tracking-bullet}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bulletmaterial | material, mat | 弹体的材质，可以是原版物品类型或 MythicItem。 | STONE |
| bulletModel | model | 材质的 CustomModelData 整数值；模型字符串应改在 MythicItem 上定义。 | 0 |
| bulletColor |  | 材质的颜色，须材质支持此项。 |  |
| bulletEnchanted | enchanted | 材质是否带有附魔。 | false |
| pitch |  | 俯仰旋转角，单位为弧度。 | 0 |
| yaw |  | 偏航旋转角，单位为弧度。 | 0 |
| roll |  | 滚转角，单位为弧度。 | 0 |
| rotation | rot | 弹体的旋转角度，单位为弧度，格式为 x,y,z。 | 0,0,0 |
| pitchspeed | ps | 俯仰旋转速度。 | 0 |
| yawspeed | ys | 偏航旋转速度。 | 0 |
| rollspeed | rs | 滚转速度。 | 0 |
| rotationspeed | rotspeed, rots | 弹体的旋转速度，格式为 x,y,z。 | 0,0,0 |
| audience |  | 弹体的[可见对象](../audience.md)。 | world |

### REALTRACKING 弹体 {#realtracking-bullet}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bulletmaterial | material, mat | 弹体的材质，可以是原版物品类型或 MythicItem。 | STONE |
| bulletModel | model | 材质的 CustomModelData 整数值；模型字符串应改在 MythicItem 上定义。 | 0 |
| bulletColor |  | 材质的颜色，须材质支持此项。 |  |
| bulletEnchanted | enchanted | 材质是否带有附魔。 | false |

### DISPLAY 弹体 {#display-bullet}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bulletmaterial | material, mat, bulletitem | 弹体的材质，可以是原版物品类型或 MythicItem。 | STONE |
| bulletModel | model | 弹体的模型。 |  |
| bulletcustommodeldata | custommodeldata, cmd | 材质的 CustomModelData 整数值。 | 0 |
| bulletColor |  | 材质的颜色，须材质支持此项。 |  |
| bulletEnchanted | enchanted | 材质是否带有附魔。 | false |
| bulletscale | scale | 弹体的缩放比例。 | 0.5,0.5,0.5 |
| bulletyoffset | byoffset, byo | 弹体的 y 轴偏移。 | 0.2 |
| bulletBillboarding | bulletBillboard | 弹体的[公告板类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Display.Billboard.html)。 | FIXED |
| bulletbrightness | bulletbrightnessblock | 弹体的亮度。 | -1 |
| bulletbrightnesssky |  | 弹体的天空光照亮度。 | bulletbrightness |
| bulletCullingDistance | bulletViewDistance, bulletViewRange | 弹体的可见范围。 | 50 |
| pitch |  | 俯仰旋转角，单位为弧度。 | 0 |
| yaw |  | 偏航旋转角，单位为弧度。 | 0 |
| roll |  | 滚转角，单位为弧度。 | 0 |
| rotation | rot | 弹体的旋转角度，单位为弧度，格式为 x,y,z。 | 0,0,0 |
| pitchspeed | ps | 俯仰旋转速度。 | 0 |
| yawspeed | ys | 偏航旋转速度。 | 0 |
| rollspeed | rs | 滚转速度。 | 0 |
| rotationspeed | rotspeed, rots | 弹体的旋转速度，格式为 x,y,z。 | 0,0,0 |
| tx |  | x 轴平移量。 | 0 |
| ty |  | y 轴平移量。 | 0 |
| tz |  | z 轴平移量。 | 0 |
| translation | pos, offset | 各轴的平移量，格式为 x,y,z。 | 0,0,0 |
| hideFirstTick | hft | 在第一刻隐藏物品。 | false |
| bulletCullingHeight | cullHeight | 弹体展示实体的剔除高度。 | 0.0 |
| bulletCullingWidth | cullWidth | 子弹显示实体的剔除宽度 | 0.0 |
| audience |  | 弹体的[可见对象](../audience.md)。 | world |
| bulletgen | generation, bulletgeneration | 安装 MythicCrucible 时，用于生成子弹物品的选项 |  |

### ME 弹体 {#me-bullet}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bulletModel | model | 子弹使用的 MEG 模型 |  |
| bulletstate | state | MEG 模型要播放的状态 |  |
| bulletcolor |  | 子弹模型的染色 |  |
| bulletscale |  | 弹体的缩放比例。 | 1 |
| bulletEnchanted | enchanted | 子弹模型是否显示附魔效果 | false |
| bulletGlowing | glowing | 子弹模型是否发光 | false |
| bulletglowcolor |  | `bulletGlowing` 设为 true 时，子弹的发光颜色 |  |
| bulletCulling | culling | 是否对子弹模型应用剔除 | true |
| bulletViewRadius |  | 值大于 0 时，子弹可见的最远距离 | -1 |
| bulletBrightness |  | 子弹的亮度 |  |
| bulletalod | alod | 是否对子弹使用 LOD 剔除 | true |

### TEXT 弹体 {#text-bullet}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bulletText | text | 子弹的文本 | * |
| bulletBillboard | billboard | 弹体的[公告板类型](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Display.Billboard.html)。 | CENTER |
| bulletscale | scale | 弹体的缩放比例。 | 0.5,0.5,0.5 |
| forcedBulletRotation | forcedRotation | 以 x,y,z 格式指定 pitch、yaw 和 roll，强制设置子弹旋转。留空时，子弹会根据飞行方向动态旋转 |  |
| bulletRotatesBasedOnDirection |  | 文本子弹是否根据移动方向旋转。效果可能*并非*你所预期 | false |
| bulletyoffset | byoffset, byo | 弹体的 y 轴偏移。 | 0 |
| bulletforwardoffset | bulletfo, bulletoffset, bfo | 子弹的前向偏移量 | 1.8 |
| backgroundcolor | color | 背景颜色，使用 ARGB 格式 | 64,0,0,0 |
| bulletCullingDistance | bulletViewDistance, bulletViewRange | 弹体的可见范围。 | 50 |
| bulletCullingHeight | cullHeight | 弹体展示实体的剔除高度。 | 0.0 |
| bulletCullingWidth | cullWidth | 子弹显示实体的剔除宽度 | 0.0 |
| bulletBrightness | bulletBrightnessBlock | 值 > -1 时，子弹的亮度 | -1 |
| bulletBrightnessSky |  | 值 > -1 时，子弹的天空光亮度 | -1 |
| audience |  | 弹体的[可见对象](../audience.md)。 | world |

## 示例 {#examples}

此示例发射一个快速移动的冰球，它会损坏并减慢它击中的第一个实体：**Mob 文件**

```yaml
Mob:
  Type: SKELETON
  Skills:
  - skill{s=IceBolt} @target ~onTimer:100
```

**技能档案**

```yaml
IceBolt:
  Skills:
  - projectile{onTick=IceBolt-Tick;onHit=IceBolt-Hit;v=8;i=1;hR=1;vR=1;hnp=true}
IceBolt-Tick:
  Skills:
  - effect:particles{p=snowballpoof;amount=20;speed=0;hS=0.2;vS=0.2} @origin
IceBolt-Hit:
  Skills:
  - damage{a=10}
  - potion{type=SLOW;duration=100;lvl=2}
```

hitConditions使用示例：

```yaml
  - projectile{hitConditions=[  - isMonster true  - isFrozen false ]}
```

hitBlockConditions 使用示例。当弹射物击中的物块是黑曜石时，它才会停止（并发射其onHitBlock技能），否则它会继续行进：

```yaml
  - projectile{stopAtBlock=true;onHitBlock=Shatter;hitBlockConditions=[  - blockType{b=OBSIDIAN} true ]}
```

## 别名 {#aliases}

- p
