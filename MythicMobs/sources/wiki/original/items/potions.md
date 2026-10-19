# Potions

This attribute is used to apply potion effects to potion based items.
Note that potion effects can be added to any kind of item, but will only
have an actual function on potions. Here is an example:

### Format {#format}

```yml
internal_itemname:
  Id: potion
  Options:
    Color: 0,0,0 #rgb(red,green,blue) format
  PotionEffects:
    - <type> <duration> <level>
```

#### **<type>** {#type}

The type of potion effect that should be applied. See below for a list of all types.

#### **<duration>** {#duration}

The duration of the potion effect measured in ticks (*20 ticks is 1 second*).

#### **<level>** {#level}

The level modifier for the potion effect. 0 = Level I, 1 = Level II, Etc.

## Potion Effects {#potion-effects}

A complete list of all supported potion effects are listed on the [spigot javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html)

## Examples {#examples}

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
