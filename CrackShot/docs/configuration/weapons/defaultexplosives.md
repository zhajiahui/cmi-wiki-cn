---
title: weapons/defaultExplosives.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: weapons/defaultExplosives.yml
source_version: 0.98.13-x6
---

# weapons/defaultExplosives.yml

文件：`weapons/defaultExplosives.yml`。版本：`0.98.13-x6`。

随包配置。

## `CocoPops` { #cocopops }

```yaml title="weapons/defaultExplosives.yml · CocoPops"
# CrackShot 自带的示例手雷、炸药和地雷（中文版）：名字、说明、消息换成了中文，武器内部名和配置节点和原版一样。
# 这个文件只在 weapons 文件夹是空的时候生成一次，你改过以后插件不会再覆盖它。
CocoPops:
    Item_Information:
        Item_Name: "&e可可球"
        Item_Type: 351~3
        Item_Lore: "&e一种集束炸弹，|&e引爆时散出 10 枚子炸弹。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
        Remove_Unused_Tag: true
    Shooting:
        Right_Click_To_Shoot: true
        Cancel_Right_Click_Interactions: true
        Projectile_Amount: 1
        Projectile_Type: grenade
        Projectile_Subtype: 351~3
        Projectile_Speed: 12
        Sounds_Projectile: EAT-2-1-28,EAT-2-1-32,EAT-2-1-36
        Sounds_Shoot: FIRE_IGNITE-2-0-0
    Cluster_Bombs:
        Enable: true
        Bomblet_Type: 362
        Delay_Before_Split: 40
        Number_Of_Splits: 1
        Number_Of_Bomblets: 10
        Speed_Of_Bomblets: 8
        Delay_Before_Detonation: 40
        Detonation_Delay_Variation: 10
        Particle_Release: BLOCK_BREAK-127
        Sounds_Release: BURP-2-1-0
    Explosions:
        Enable: true
        Damage_Multiplier: 25
        Explosion_No_Grief: true
        Explosion_Radius: 4
        Sounds_Explode: ITEM_PICKUP-2-1-0
    Extras:
        One_Time_Use: true
```

## `Trinket` { #trinket }

```yaml title="weapons/defaultExplosives.yml · Trinket"
Trinket:
    Item_Information:
        Item_Name: "&e小饰品"
        Item_Type: 264
        Item_Lore: "&e左键设定主人。|&e下列情况会爆炸：|&e- 被捡起|&e- 被发射器射出|&e- 装着它的箱子被打开|&e- 放在物品展示框里，|&e  且附近的压力板被踩下|&e&o主人不会触发自己的陷阱。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    Explosive_Devices:
        Enable: true
        Device_Type: trap
        Device_Info: true-true-true-false-false
        Sounds_Deploy: ITEM_PICKUP-2-0-0
        Message_Trigger_Placer: "&e<victim> 触发了你的诡雷。"
        Message_Trigger_Victim: "&e你触发了 <shooter> 的诡雷。"
        Sounds_Trigger: SHEEP_IDLE-2-1-0
    Explosions:
        Enable: true
        Damage_Multiplier: 50
        Explosion_No_Grief: true
        Enable_Owner_Immunity: true
        Explosion_Radius: 5
        Explosion_Potion_Effect: POISON-100-2,HUNGER-100-2
        Explosion_Delay: 10
        Sounds_Explode: WITHER_SHOOT-2-2-0
```

## `Putty` { #putty }

```yaml title="weapons/defaultExplosives.yml · Putty"
Putty:
    Item_Information:
        Item_Name: "&e粘土炸药"
        Item_Type: 404
        Item_Lore: "&e遥控炸药。|&e右键投掷。|&e左键引爆。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    Shooting:
        Cancel_Left_Click_Block_Damage: true
        Cancel_Right_Click_Interactions: true
    Explosive_Devices:
        Enable: true
        Device_Type: itembomb
        Device_Info: 2,10,159,159~14
        Sounds_Deploy: SHOOT_ARROW-1-0-0
        Sounds_Alert_Placer: CLICK-1-1-0
        Sounds_Trigger: SHEEP_SHEAR-1-2-0
    Explosions:
        Enable: true
        Explosion_No_Grief: true
        Explosion_Radius: 5
        Explosion_Delay: 16
        Sounds_Explode: ZOMBIE_WOOD-2-0-0
```

## `C4` { #c4 }

```yaml title="weapons/defaultExplosives.yml · C4"
C4:
    Item_Information:
        Item_Name: "&eC4"
        Item_Type: 69
        Item_Lore: "&e遥控炸药。|&e右键放置。|&e左键引爆。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    Shooting:
        Cancel_Left_Click_Block_Damage: true
#    Ammo:
#        Enable: true
#        Ammo_Item_ID: 46
#        Take_Ammo_Per_Shot: true
    Explosive_Devices:
        Enable: true
        Device_Type: remote
        Device_Info: 2-1A-TheStabbyBunny
        Sounds_Deploy: CHICKEN_EGG_POP-1-1-0
        Message_Disarm: "&e你拆除了一个爆炸装置。"
        Message_Trigger_Placer: "&e<victim> 引爆了你的 C4。"
        Message_Trigger_Victim: "&e你引爆了 <shooter> 的 C4。"
        Sounds_Alert_Placer: CLICK-1-1-0
        Sounds_Trigger: SHEEP_SHEAR-1-1-0
    Explosions:
        Enable: true
        Explosion_No_Grief: true
        Explosion_Radius: 6
        Explosion_Delay: 16
        Sounds_Explode: ZOMBIE_WOOD-2-0-0
```

## `Airstrike` { #airstrike }

```yaml title="weapons/defaultExplosives.yml · Airstrike"
#    Extras:
#        One_Time_Use: true

Airstrike:
    Item_Information:
        Item_Name: "&e鹞式空袭"
        Item_Type: 76
        Item_Lore: "&e在信号弹落下的位置|&e呼叫一次空袭。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
        Remove_Unused_Tag: true
    Shooting:
        Right_Click_To_Shoot: true
        Cancel_Right_Click_Interactions: true
        Projectile_Amount: 1
        Projectile_Type: flare
        Projectile_Subtype: 76
        Projectile_Speed: 10
        Sounds_Shoot: FIRE_IGNITE-2-0-0,FIZZ-2-0-0
    Airstrikes:
        Enable: true
        Flare_Activation_Delay: 60
        Particle_Call_Airstrike: lightning
        Message_Call_Airstrike: "&e友军空袭正在赶来。"
        Block_Type: 85
        Area: 4
        Distance_Between_Bombs: 4
        Height_Dropped: 90
        Vertical_Variation: 10
        Horizontal_Variation: 10
        Multiple_Strikes:
            Enable: true
            Number_Of_Strikes: 3
            Delay_Between_Strikes: 20
        Sounds_Airstrike: ENDERMAN_STARE-2-2-0
    Explosions:
        Enable: true
        Explosion_No_Grief: true
        Explosion_Radius: 4
        Sounds_Explode: ENDERDRAGON_HIT-2-2-0
    Extras:
        One_Time_Use: true
```

## `Grenade` { #grenade }

```yaml title="weapons/defaultExplosives.yml · Grenade"
Grenade:
    Item_Information:
        Item_Name: "&e破片手雷"
        Item_Type: 402
        Item_Lore: "&e投出三秒后爆炸。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
        Remove_Unused_Tag: true
    Shooting:
        Right_Click_To_Shoot: true
        Cancel_Right_Click_Interactions: true
        Delay_Between_Shots: 10
        Projectile_Amount: 1
        Projectile_Type: grenade
        Projectile_Subtype: 46
        Projectile_Speed: 10
        Sounds_Shoot: SHOOT_ARROW-2-0-0
    Explosions:
        Enable: true
        Explosion_No_Grief: true
        Explosion_Radius: 4
        Explosion_Delay: 60
    Extras:
        One_Time_Use: true
```

## `Flashbang` { #flashbang }

```yaml title="weapons/defaultExplosives.yml · Flashbang"
Flashbang:
    Item_Information:
        Item_Name: "&e闪光弹"
        Item_Type: 351~8
        Item_Lore: "&e爆炸时让目标晕头转向。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
        Remove_Unused_Tag: true
    Shooting:
        Right_Click_To_Shoot: true
        Cancel_Right_Click_Interactions: true
        Delay_Between_Shots: 10
        Projectile_Amount: 1
        Projectile_Type: grenade
        Projectile_Subtype: 351~8
        Projectile_Speed: 10
        Sounds_Shoot: SHOOT_ARROW-2-0-0
    Explosions:
        Enable: true
        Explosion_No_Grief: true
        Explosion_No_Damage: true
        Explosion_Radius: 6
        Explosion_Potion_Effect: BLINDNESS-120-1,SLOW-120-1
        Explosion_Delay: 20
        Sounds_Victim: LEVEL_UP-1-0-0
        Sounds_Explode: ANVIL_LAND-2-1-0
    Extras:
        One_Time_Use: true
```

## `Toaster` { #toaster }

```yaml title="weapons/defaultExplosives.yml · Toaster"
Toaster:
    Item_Information:
        Item_Name: "&e烤面包机"
        Item_Type: 343
        Item_Lore: "&e反步兵地雷。|&e下列情况会引发燃烧爆炸：|&e- 生物或玩家撞上|&e- 被拳头或物品击打|&e- 被弹丸击中"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
        Remove_Unused_Tag: true
    Shooting:
        Right_Click_To_Shoot: true
        Cancel_Right_Click_Interactions: true
    Explosive_Devices:
        Enable: true
        Device_Type: landmine
        Device_Info: 46,MINECART
        Sounds_Deploy: ORB_PICKUP-2-2-0
        Message_Trigger_Placer: "&e<victim> 触发了你的地雷。"
        Message_Trigger_Victim: "&e你触发了 <shooter> 的地雷。"
        Sounds_Trigger: ITEM_BREAK-2-1-0,ZOMBIE_UNFECT-2-2-0
    Explosions:
        Enable: true
        Ignite_Victims: 120
        Explosion_No_Grief: true
        Explosion_Radius: 4
        Explosion_Delay: 16
        Sounds_Explode: FIRE-2-0-0,ZOMBIE_METAL-2-0-0
    Extras:
        One_Time_Use: true
```
