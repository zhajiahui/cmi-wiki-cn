---
title: On Interact
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/OnInteract
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Interact {#on-interact}

## 说明 {#description}

为玩家施加光环组件。玩家手持物品交互（右键），或看向 5 格内显示轮廓的非空气方块时交互，会触发技能。

将光环组件应用于非玩家实体，当玩家与非玩家实体交互（右键单击）时，该实体会触发技能

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onrightclickskill | oninteractskill, onrightclick, oninteract, or, oi | 目标玩家与方块交互，或目标实体被玩家交互时执行的技能。 |  |

## 示例 {#examples}

简单1：（玩家有光环）

为自身施加 onInteract 光环。右键点击 5 格内显示轮廓的方块，或手持物品右键点击时，会获得药水效果。

```yaml
ApplyAura:
  Skills:
  - aura{auraname=GodMode;d=300;i=1;components=[
    - onInteract{or=PotionEffects}
    ]} @self
PotionEffects:
  Skills:
  - potion{t=DAMAGE_RESISTANCE;d=200;l=10;hasParticles=false} @self
  - potion{t=FIRE_RESISTANCE;d=200;l=10;hasParticles=false} @self
  - potion{t=REGENERATION;d=200;l=10;hasParticles=false} @self
  - potion{t=ABSORPTION;d=200;l=10;hasParticles=false} @self
```

---

简单2：（玩家将光环强加在附近的实体上）

使用 sudoskill 强制附近具有 30 方块的实体对自己施加 onInteract 光环。然后右键单击任何实体，即可为 30 块范围内的所有其他实体赋予药水效果。

```yaml
ForceApplyAura:
  Skills:
  - sudoskill{s=ApplyAura} @EntitiesInRadius{r=30}
ApplyAura:
  Skills:
  - aura{auraname=GodMode;d=300;i=1;components=[
    - onInteract{or=PotionEffects}
    ]} @self
PotionEffects:
  Skills:
  - potion{t=DAMAGE_RESISTANCE;d=200;l=10;hasParticles=false} @EIR{r=30}
  - potion{t=FIRE_RESISTANCE;d=200;l=10;hasParticles=false} @EIR{r=30}
  - potion{t=REGENERATION;d=200;l=10;hasParticles=false} @EIR{r=30}
  - potion{t=ABSORPTION;d=200;l=10;hasParticles=false} @EIR{r=30}
```

---

简单3：（玩家有光环并迫使附近的实体执行技能）

为自身施加 onInteract 光环。手持方块右键点击，或右键点击 5 格内显示轮廓的方块时，会将周围的所有生物送上月球，5 秒后再让它们砸回地面。

```yaml
ApplyAura:
  Skills:
  - aura{auraname=HerculesStrength;d=300;i=1;components=[
    - onInteract{or=ToTheMoonStart}
    ]} @self
ToTheMoonStart:
  Skills:
  - sudoskill{s=ToTheMoon} @EntitiesInRadius{r=10;targetPlayers=false}
ToTheMoon:
  Skills:
  - jump{v=10;repeat=4;repeatInterval=20} @self
  - delay 100
  - jump{v=-50} @self
```

## 别名 {#aliases}

- onrightclick
