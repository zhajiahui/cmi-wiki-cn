---
title: 药水
source_url: https://wiki.mythiccraft.io/mythicmobs/Items/Potions
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 药水 {#potions}

此属性用于给药水类物品添加药水效果。请注意，药水效果可以添加到任何类型的物品上，但只有在药水上才会实际生效。示例如下：

### 格式 {#format}

```yml
internal_itemname:
  Id: potion
  Options:
    Color: 0,0,0 #rgb(red,green,blue) format
  PotionEffects:
    - <type> <duration> <level>
```

#### **<type>** {#type}

要应用的药水效果类型。所有类型的列表见下文。

#### **<duration>** {#duration}

药水效果的持续时间，单位为刻（*20 刻为 1 秒*）。

#### **<level>** {#level}

药水效果的等级修正。0 = 等级 I，1 = 等级 II，以此类推。

## 药水效果 {#potion-effects}

所有受支持的药水效果的完整列表见 [Spigot Javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html)。

## 示例 {#examples}

```yml
SupremeHealingPotion:
      Id: potion
      Display: '&6Supreme Healing Potion'
      Options:
        Color: 239,103,216
        HideFlags: true
      PotionEffects:
      - HEAL 60 1
      - CONFUSION 20 0
      Lore:
      - '&8An incredibly potent healing potion'
      - '&8able to cure even tremendous wounds.'
      - '&cNotice: May cause liver failure.'
```
