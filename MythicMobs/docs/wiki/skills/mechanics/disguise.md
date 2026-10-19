---
title: Disguise
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/disguise
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Disguise {#disguise}

## 说明 {#description}

为施法生物应用伪装描述。需要安装 LibsDisguises 并开启伪装功能。

有关可用伪装的列表，请参阅[附加组件：伪装](../../mobs/disguises.md)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| disguise | d, type | 要应用到生物上的伪装。 | player Ashijin |
| audience |  | 伪装的[可见对象](../audience.md)。 |  |

## 示例 {#examples}

> 你可以使用 `/mm test cast TestingDisguiseMechanic` 来测试这两种伪装

##  {#section}

```yml
TestingDisguiseMechanic:
  Skills:
  - disguise{d="Sheep SetBurning SetSpinning"} @self
```

> 这会将你伪装成一只着火旋转的羊。

##  {#section-2}

```yml
TestingDisguiseMechanic:
  Skills:
  - disguise{d="Zombie setYModifier -1.5 setPitchLocked setInvisible setHelmet PLAYER_HEAD"} @self
```

> 这个例子将把你变成一个在地板上滑行的史蒂夫头。没有什么好的方式来描述它。这很有趣。我建议你尝试一下！
