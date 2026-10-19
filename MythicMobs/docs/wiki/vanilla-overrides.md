---
title: 原版生物覆盖
source_url: https://wiki.mythiccraft.io/mythicmobs/Vanilla-Overrides
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 原版生物覆盖 {#vanilla-overrides}

除了制作新生物，还想自定义原版生物？使用原版生物覆盖即可实现！

## 什么是覆盖？ {#what-is-an-override}

原版生物覆盖是一种特殊的 MythicMob，使用与普通 MythicMob 相同的生物配置语法，但有以下两点例外：

- **[内部名称](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#internal_name)必须是原版生物的[类型名称](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html)**
- **该生物不需要 [Type](mobs/mobs.md#type) 字段**

完成这些设置后，配置会覆盖类型与其内部名称相同的所有原版实体。例如，覆盖配置的名称为 `Cow`，则所有牛都会变成该 MythicMob，无论它们以何种方式生成。

除此以外，普通 MythicMob 支持的功能也都可用于原版生物覆盖，例如伪装、自定义伤害修正和技能！

但请注意，并非所有生物都会变成原版生物覆盖：**通过其他生物繁殖生成的生物不会被覆盖！**

## 示例 {#examples}

```yml
ZOMBIE:
  Options:
    PreventSunburn: true
```

##  {#section}

```yml
CREEPER:
  Health: 100
  Display: '&bJohn'
  Disguise: Dolphin
  Options:
    MovementSpeed: 0.5
  Skills:
  - message{m="Oh no! I have died!"} @PlayersInRadius{r=30} ~onDeath
```

##  {#section-2}

下面的 PILLAGER 覆盖示例仍能正确给予不祥之兆效果，而普通覆盖会使该效果无法给予

```yaml
PILLAGER:
  Skills:
  - skill{s=[
    - potion{t=BAD_OMEN;l=4;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=3to4}
    - potion{t=BAD_OMEN;l=3;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=2}
    - potion{t=BAD_OMEN;l=2;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=1}
    - potion{t=BAD_OMEN;l=1;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=0}
    - potion{t=BAD_OMEN;l=0;d=120000}
    ]} @trigger ~onDeath ?~isPlayer ?wearing{m=WHITE_BANNER}
```
