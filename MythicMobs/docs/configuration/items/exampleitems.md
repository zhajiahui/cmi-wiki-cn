---
title: items/ExampleItems.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: items/ExampleItems.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# items/ExampleItems.yml

文件：`items/ExampleItems.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包物品或内容配置。

## `SkeletonKingSword` { #skeletonkingsword }

```yaml title="items/ExampleItems.yml · SkeletonKingSword"
# 更多信息请查看插件手册，或加入 Discord：
# http://www.mythicmobs.net
#  

SkeletonKingSword:
  Id: DIAMOND_SWORD
  Display: "&3骷髅王巨剑"
  Lore:
  - "&6一把强大的剑，"
  - "&6曾由骷髅王使用。"
  Enchantments:
  - DAMAGE_ALL:5
  - KNOCKBACK:2
  - FIRE_ASPECT:2
  Attributes:
    MainHand:
      Health: 10
      MovementSpeed: 0.1
```

## `KingsCrown` { #kingscrown }

```yaml title="items/ExampleItems.yml · KingsCrown"
KingsCrown:
  Id: GOLDEN_HELMET
  Display: "&d王者之冠"
  Lore:
  - "&6一顶王者的冠冕，赋予"
  - "&6佩戴者坚定不移的力量！"
  Enchantments:
  - PROTECTION_ENVIRONMENTAL:2
  - PROTECTION_PROJECTILE:2
  - PROTECTION_FIRE:2
  - PROTECTION_EXPLOSIONS:2
  Hide:
  - ATTRIBUTES
  - ENCHANTS
  Attributes:
    Head:
      Health: 10
      KnockbackResistance: 10
```

## `BanditTunic` { #bandittunic }

```yaml title="items/ExampleItems.yml · BanditTunic"
BanditTunic:
  Id: LEATHER_CHESTPLATE
  Display: "&a强盗皮衣"
  Lore:
  - "&6一件从强盗尸体上"
  - "&6取下的皮质上衣。"
  Options:
    Color: 255,40,40
```
