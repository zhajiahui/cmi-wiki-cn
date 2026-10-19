---
title: Potion
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Potion
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Potion {#potion}

## 说明 {#description}

对目标实体施加药水效果，通常用于自定义生物创建，是一个非常强大的工具；因为它允许无数有趣的应用程序。有关可用药水效果的完整列表，请参阅 [spigot javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html)。

目前除盔甲架外，要让生物隐身只能使用药水效果。盔甲架有独立的永久隐身属性。极高的效果等级可能产生异常结果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t, effect | 要施加的[药水效果](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html)类型。 | SLOW |
| duration | d | 效果的持续时间，单位为刻 [1]。 | 100 |
| level | lvl, l | 药水效果的修饰等级。实际等级为 level 的值 +1。 | 0 |
| force | overwrite, ow, override, or | 是否覆盖当前的药水效果。 | false |
| hasParticles | particles, p | 是否显示状态效果粒子。 | true |
| hasIcon | icon, i | 是否显示状态效果图标。 | true |
| ambientparticles | ambient, a | 是否显示环境粒子。 | false |

## 示例 {#examples}

此示例技能配置将大幅减慢目标10秒（200游戏刻）并对其造成5心伤害。

```yaml
Cripple:
  Skills:
  - potion{type=SLOW;duration=200;level=4}
  - damage{amount=10}
```

> 20 游戏刻 = 1 秒
