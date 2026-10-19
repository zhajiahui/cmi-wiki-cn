---
title: weapons/defaultWeapons.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: weapons/defaultWeapons.yml
source_version: 0.98.13-x6
---

# weapons/defaultWeapons.yml

文件：`weapons/defaultWeapons.yml`。版本：`0.98.13-x6`。

随包配置。

## `Gauss` { #gauss }

```yaml title="weapons/defaultWeapons.yml · Gauss"
# CrackShot 自带的示例武器（中文版）：名字、说明、消息换成了中文，武器内部名和配置节点和原版一样。
# 这个文件只在 weapons 文件夹是空的时候生成一次，你改过以后插件不会再覆盖它。
Gauss:
    Item_Information:
        Item_Name: "&e高斯霰弹枪"
        Item_Type: 417
        Item_Lore: "&e先进的泵动式霰弹枪。|&e发射金属弹头，穿透|&e40 格内的所有目标。|&e对僵尸造成 200% 伤害。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    Shooting:
        Cancel_Left_Click_Block_Damage: true
        Cancel_Right_Click_Interactions: true
        Projectile_Amount: 1
        Projectile_Type: energy
        Projectile_Subtype: 40-1-NONE-0
        Projectile_Damage: 12
        Sounds_Shoot: WITHER_SHOOT-1-2-0,EXPLODE-1-2-0
    Reload:
        Enable: true
        Reload_Amount: 8
        Reload_Bullets_Individually: true
        Reload_Duration: 10
        Sounds_Reloading: IRONGOLEM_THROW-1-2-0
    Firearm_Action:
        Type: pump
        Open_Duration: 12
        Close_Duration: 3
        Sound_Open: PISTON_EXTEND-1-2-0
        Sound_Close: PISTON_EXTEND-1-2-0
    Abilities:
        Reset_Hit_Cooldown: true
        Super_Effective: ZOMBIE-2
    Particles:
        Enable: true
        Particle_Player_Shoot: BLOCK_BREAK-57
    Hit_Events:
        Enable: true
        Sounds_Shooter: SHOOT_ARROW-1-2-0
```

## `Carbine` { #carbine }

```yaml title="weapons/defaultWeapons.yml · Carbine"
Carbine:
    Item_Information:
        Item_Name: "&e卡宾枪"
        Item_Type: 417
        Item_Lore: "&e有 10% 几率暴击。|&e右键切换到榴弹发射器。|&e榴弹射出 0.25 秒后|&e引信才会生效。"
        Attachments:
            Type: main
            Info: "M320"
            Toggle_Delay: 5
            Sounds_Toggle: NOTE_STICKS-1-2-0
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    Shooting:
        Cancel_Left_Click_Block_Damage: true
        Cancel_Right_Click_Interactions: true
        Delay_Between_Shots: 3
        Recoil_Amount: 1
        Projectile_Amount: 1
        Projectile_Type: snowball
        Projectile_Speed: 40
        Projectile_Damage: 4
        Bullet_Spread: 0.5
        Sounds_Shoot: BLAZE_HIT-1-2-0,ZOMBIE_WOOD-1-2-0
    Sneak:
        Enable: true
        No_Recoil: true
        Bullet_Spread: 0.4
    Reload:
        Enable: true
        Reload_Amount: 8
        Reload_Duration: 30
        Sounds_Reloading: SKELETON_IDLE-1-0-0,FIRE_IGNITE-1-1-14,DOOR_OPEN-1-2-16,FIRE_IGNITE-1-1-26,HURT_FLESH-1-0-27,DOOR_CLOSE-1-2-28
    Firearm_Action:
        Type: slide
        Close_Duration: 8
        Sound_Close: CLICK-1-1-0
    Abilities:
        Reset_Hit_Cooldown: true
    Particles:
        Enable: true
        Particle_Impact_Anything: BLOCK_BREAK-80
        Particle_Critical: BLOCK_BREAK-55
    Hit_Events:
        Enable: true
        Sounds_Shooter: SHOOT_ARROW-1-2-0
    Critical_Hits:
        Enable: true
        Bonus_Damage: 2
        Chance: 10
        Sounds_Shooter: ORB_PICKUP-1-2-0
```

## `Deagle` { #deagle }

```yaml title="weapons/defaultWeapons.yml · Deagle"
Deagle:
    Item_Information:
        Item_Name: "&e沙漠之鹰"
        Item_Type: 417
        Item_Lore: "&e双持手枪。|&e左键和右键各开一把。|&e从背后击中敌人|&e有额外的背刺伤害。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    Shooting:
        Dual_Wield: true
        Cancel_Left_Click_Block_Damage: true
        Cancel_Right_Click_Interactions: true
        Delay_Between_Shots: 2
        Recoil_Amount: 2
        Projectile_Amount: 1
        Projectile_Type: egg
        Projectile_Speed: 40
        Projectile_Damage: 4
        Bullet_Spread: 1
        Sounds_Shoot: ZOMBIE_WOOD-1-2-0,ZOMBIE_WOOD-1-0-0
    Sneak:
        Enable: true
        No_Recoil: true
        Bullet_Spread: 0.75
    Reload:
        Enable: true
        Reload_Amount: 7
        Reload_Duration: 40
        Sounds_Out_Of_Ammo: CLICK-1-1-0
        Sounds_Reloading: DOOR_OPEN-1-2-4,DOOR_OPEN-1-2-8,DOOR_CLOSE-1-2-23,DOOR_CLOSE-1-2-38
        Dual_Wield:
            Single_Reload_Duration: 25
            Sounds_Single_Reload: DOOR_OPEN-1-2-4,DOOR_CLOSE-1-2-23
            Sounds_Shoot_With_No_Ammo: CLICK-1-2-0
    Abilities:
        Reset_Hit_Cooldown: true
    Backstab:
        Enable: true
        Bonus_Damage: 2
        Sounds_Shooter: ORB_PICKUP-1-2-0
    Particles:
        Enable: true
        Particle_Backstab: BLOCK_BREAK-55
    Hit_Events:
        Enable: true
        Sounds_Shooter: SHOOT_ARROW-1-2-0
```

## `Bazooka` { #bazooka }

```yaml title="weapons/defaultWeapons.yml · Bazooka"
Bazooka:
    Item_Information:
        Item_Name: "&e火箭筒"
        Item_Type: 417
        Item_Lore: "&e火箭发射器。|&e朝脚下开火|&e可以火箭跳。|&e免疫摔落伤害。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
        Inventory_Control: Group_Bazookas
    Shooting:
        Cancel_Left_Click_Block_Damage: true
        Cancel_Right_Click_Interactions: true
        Recoil_Amount: 2
        Projectile_Amount: 1
        Projectile_Type: fireball
        Projectile_Speed: 10
        Sounds_Shoot: ZOMBIE_WOOD-1-0-0,FIZZ-1-1-0
    Sneak:
        Enable: true
        No_Recoil: true
    Abilities:
        No_Fall_Damage: true
    Reload:
        Enable: true
        Reload_Amount: 1
        Reload_Duration: 55
        Sounds_Reloading: SKELETON_IDLE-1-0-10,PISTON_EXTEND-1-0-28,SKELETON_WALK-1-0-48
    Particles:
        Enable: true
        Particle_Player_Shoot: BLOCK_BREAK-35
    Shrapnel:
        Enable: true
        Block_Type: 77
        Amount: 14
        Speed: 7
    Explosions:
        Enable: true
        Knockback: 5
        Damage_Multiplier: 10
        Explosion_No_Grief: true
        Explosion_Radius: 6
        Sounds_Shooter: SHOOT_ARROW-1-2-0
```

## `Python` { #python }

```yaml title="weapons/defaultWeapons.yml · Python"
Python:
    Item_Information:
        Item_Name: "&e蟒蛇左轮 &l/&e 战术刀"
        Item_Type: 417
        Item_Lore: "&e威力很大的左轮手枪。|&e左键用战术刀|&e近战攻击敌人。"
        Melee_Attachment: Tactical_Knife
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    Shooting:
        Right_Click_To_Shoot: true
        Cancel_Left_Click_Block_Damage: true
        Cancel_Right_Click_Interactions: true
        Delay_Between_Shots: 2
        Projectile_Amount: 1
        Projectile_Type: snowball
        Projectile_Speed: 40
        Projectile_Damage: 6
        Bullet_Spread: 0.5
        Sounds_Shoot: IRONGOLEM_HIT-1-2-0,ZOMBIE_METAL-1-2-0
    Reload:
        Enable: true
        Reload_Amount: 6
        Reload_Duration: 35
        Sounds_Reloading: LEVEL_UP-1-1-10,FIRE_IGNITE-1-2-28
    Firearm_Action:
        Type: revolver
        Open_Duration: 5
        Close_Duration: 5
        Sound_Open: DOOR_OPEN-1-2-0
        Sound_Close: DOOR_CLOSE-1-2-0
    Abilities:
        Reset_Hit_Cooldown: true
    Hit_Events:
        Enable: true
        Sounds_Shooter: SHOOT_ARROW-1-2-0
```

## `Riotshield` { #riotshield }

```yaml title="weapons/defaultWeapons.yml · Riotshield"
Riotshield:
    Item_Information:
        Item_Name: "&e防暴盾"
        Item_Type: 267
        Item_Lore: "&e挡下所有近战和远程攻击。|&e挡不住来自背后的攻击。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
        Remove_Unused_Tag: true
    Riot_Shield:
        Enable: true
        Durability_Loss_Per_Hit: 10
        Sounds_Blocked: GLASS-2-2-0
        Sounds_Break: ITEM_BREAK-2-1-0
```

## `Olympia` { #olympia }

```yaml title="weapons/defaultWeapons.yml · Olympia"
Olympia:
    Item_Information:
        Item_Name: "&e奥林匹亚"
        Item_Type: 417
        Item_Lore: "&e双管霰弹枪。|&e近距离威力致命。|&e距离一远就不疼了。|&e发射燃烧弹。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    Shooting:
        Cancel_Left_Click_Block_Damage: true
        Cancel_Right_Click_Interactions: true
        Delay_Between_Shots: 3
        Recoil_Amount: 5
        Projectile_Amount: 8
        Projectile_Type: egg
        Removal_Or_Drag_Delay: 4-false
        Projectile_Speed: 30
        Projectile_Damage: 5
        Projectile_Flames: true
        Projectile_Incendiary:
            Enable: true
            Duration: 80
        Bullet_Spread: 1
        Reset_Fall_Distance: true
        Sounds_Shoot: ZOMBIE_WOOD-1-1-0,EXPLODE-1-2-0,GHAST_FIREBALL-1-1-0
    Sneak:
        Enable: true
        No_Recoil: true
        Bullet_Spread: 1
    Reload:
        Enable: true
        Reload_Amount: 2
        Reload_Bullets_Individually: true
        Reload_Duration: 15
        Sounds_Reloading: NOTE_STICKS-1-1-0,NOTE_SNARE_DRUM-1-6-1
    Firearm_Action:
        Type: break
        Open_Duration: 10
        Close_Duration: 15
        Sound_Open: DOOR_OPEN-1-2-0
        Sound_Close: DOOR_CLOSE-1-2-0
    Abilities:
        Reset_Hit_Cooldown: true
        No_Fall_Damage: true
    Hit_Events:
        Enable: true
        Sounds_Shooter: SHOOT_ARROW-1-2-0
    Damage_Based_On_Flight_Time:
        Enable: true
        Bonus_Damage_Per_Tick: -1
        Maximum_Damage: -4
    Particles:
        Enable: true
        Particle_Player_Shoot: FLAMES-1
        Particle_Impact_Anything: BLOCK_BREAK-51
```

## `Hunting` { #hunting }

```yaml title="weapons/defaultWeapons.yml · Hunting"
Hunting:
    Item_Information:
        Item_Name: "&e猎枪"
        Item_Type: 417
        Item_Lore: "&e精度很高的栓动步枪。|&e装有夜视瞄准镜。|&e爆头造成双倍伤害。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    Shooting:
        Cancel_Left_Click_Block_Damage: true
        Cancel_Right_Click_Interactions: true
        Projectile_Amount: 1
        Projectile_Type: snowball
        Projectile_Speed: 1000
        Projectile_Damage: 12
        Sounds_Shoot: BLAZE_HIT-1-1-0,EXPLODE-1-2-0
    Custom_Death_Message:
        Normal: "&e<victim> 被 <shooter> 用猎枪狙杀了。"
    Reload:
        Enable: true
        Starting_Amount: 0
        Reload_Amount: 5
        Reload_Bullets_Individually: true
        Reload_Duration: 10
        Sounds_Reloading: NOTE_STICKS-1-1-0
    Firearm_Action:
        Type: bolt
        Open_Duration: 8
        Close_Duration: 7
        Close_Shoot_Delay: 6
        Sound_Open: NOTE_STICKS-1-0-0,PISTON_RETRACT-1-2-2
        Sound_Close: PISTON_EXTEND-1-2-0
    Headshot:
        Enable: true
        Bonus_Damage: 12
        Sounds_Shooter: NOTE_PLING-1-2-0
        Sounds_Victim: VILLAGER_DEATH-1-1-0
    Abilities:
        Reset_Hit_Cooldown: true
        Knockback: 3
    Particles:
        Enable: true
        Particle_Player_Shoot: BLOCK_BREAK-1
        Particle_Terrain: true
    Fireworks:
        Enable: true
        Firework_Headshot: STAR-TRUE-TRUE-250-0-0
    Scope:
        Enable: true
        Night_Vision: true
        Zoom_Amount: 5
        Sounds_Toggle_Zoom: NOTE_STICKS-1-2-0
    Hit_Events:
        Enable: true
        Sounds_Shooter: SHOOT_ARROW-1-2-0
```

## `Type95` { #type95 }

```yaml title="weapons/defaultWeapons.yml · Type95"
Type95:
    Item_Information:
        Item_Name: "&e95 式"
        Item_Type: 417
        Item_Lore: "&e半自动，三发点射。|&e换弹需要恶魂之泪。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    SignShops:
        Enable: true
        Price: 266-10
        Sign_Gun_ID: 95
    Shooting:
        Cancel_Left_Click_Block_Damage: true
        Cancel_Right_Click_Interactions: true
        Delay_Between_Shots: 7
        Recoil_Amount: 1
        Projectile_Amount: 1
        Projectile_Type: snowball
        Projectile_Speed: 40
        Projectile_Damage: 4
        Bullet_Spread: 2
        Sounds_Shoot: ITEM_BREAK-1-2-2,NOTE_SNARE_DRUM-1-0-2
    Sneak:
        Enable: true
        No_Recoil: true
        Bullet_Spread: 1
    Burstfire:
        Enable: true
        Shots_Per_Burst: 3
        Delay_Between_Shots_In_Burst: 1
    Ammo:
        Enable: true
        Ammo_Item_ID: 370
        Sounds_Out_Of_Ammo: NOTE_PLING-1-2-0
        Sounds_Shoot_With_No_Ammo: NOTE_STICKS-1-2-0
    Reload:
        Enable: true
        Reload_Amount: 30
        Take_Ammo_On_Reload: true
        Reload_Duration: 40
        Sounds_Reloading: FIRE_IGNITE-1-1-4,DOOR_OPEN-1-2-6,FIRE_IGNITE-1-1-36,HURT_FLESH-1-0-37,DOOR_CLOSE-1-2-38
    Firearm_Action:
        Type: slide
        Close_Duration: 10
        Sound_Close: PISTON_RETRACT-1-2-0,PISTON_RETRACT-1-2-2
    Scope:
        Enable: true
        Zoom_Amount: 5
        Zoom_Bullet_Spread: 0
        Sounds_Toggle_Zoom: ENDERDRAGON_WINGS-1-2-0
    Abilities:
        Reset_Hit_Cooldown: true
    Hit_Events:
        Enable: true
        Sounds_Shooter: SHOOT_ARROW-1-2-0
```

## `AK-47` { #ak-47 }

```yaml title="weapons/defaultWeapons.yml · AK-47"
AK-47:
    Item_Information:
        Item_Name: "&eAK-47"
        Item_Type: 417
        Item_Lore: "&e全自动，威力大。|&e适合中距离作战。|&e左右键的用法和别的枪相反。"
        Sounds_Acquired: BAT_TAKEOFF-1-1-0
    Shooting:
        Right_Click_To_Shoot: true
        Cancel_Left_Click_Block_Damage: true
        Cancel_Right_Click_Interactions: true
        Recoil_Amount: 1
        Projectile_Amount: 1
        Projectile_Type: snowball
        Projectile_Speed: 40
        Projectile_Damage: 4
        Bullet_Spread: 2
        Sounds_Shoot: IRONGOLEM_HIT-1-2-0,SKELETON_HURT-1-2-0,ZOMBIE_WOOD-1-2-0
    Sneak:
        Enable: true
        No_Recoil: true
        Bullet_Spread: 1
    Fully_Automatic:
        Enable: true
        Fire_Rate: 6
    Reload:
        Enable: true
        Reload_Amount: 30
        Reload_Duration: 40
        Sounds_Out_Of_Ammo: ITEM_BREAK-1-1-0
        Sounds_Reloading: FIRE_IGNITE-1-1-4,DOOR_OPEN-1-2-6,FIRE_IGNITE-1-1-36,HURT_FLESH-1-0-37,DOOR_CLOSE-1-2-38
    Firearm_Action:
        Type: slide
        Close_Duration: 10
        Close_Shoot_Delay: 12
        Sound_Close: PISTON_RETRACT-1-2-0,PISTON_RETRACT-1-2-3
    Scope:
        Enable: true
        Zoom_Amount: 5
        Zoom_Bullet_Spread: 0
        Sounds_Toggle_Zoom: ENDERDRAGON_WINGS-1-2-0
    Abilities:
        Reset_Hit_Cooldown: true
    Hit_Events:
        Enable: true
        Sounds_Shooter: SHOOT_ARROW-1-2-0
```
