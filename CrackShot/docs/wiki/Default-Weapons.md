---
title: "默认武器"
source_url: "https://github.com/Shampaggon/CrackShot/wiki/Default-Weapons"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "Shampaggon/CrackShot Wiki @ d132397f9b52a5274dba87443ad0ebcde369a0a0；2026-10-19 快照；与 0.98.13-x6 的对应关系未确认"
---

<a id="all-default-weapons-of-crackshot-v098-and-above"></a>

## **░ CrackShot v0.98 及以上版本的全部默认武器**
<a id="gauss-shotgun-advanced-pump-action-shotgun"></a>

#### Gauss Shotgun（高级泵动霰弹枪）
    Gauss:
        Item_Information:
            Item_Name: "&eGauss Shotgun"
            Item_Type: 417
            Item_Lore: "&eAdvanced pump-action shotgun.|&eFires metal slugs that penetrate|&eall targets within 40 blocks.|&eDeals 200% damage to Zombies."
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

***

<a id="carbine-assault-rifle-w-grenade-launcher"></a>

#### Carbine（带榴弹发射器的突击步枪）
    Carbine:
        Item_Information:
            Item_Name: "&eCarbine"
            Item_Type: 417
            Item_Lore: "&eDeals crits with a 10% chance.|&eSwitch to the grenade launcher|&ewith right click. Fired grenades|&earm themselves in 0.25 seconds."
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

***

<a id="m320-attachment---grenade-launcher"></a>

#### M320（附件：榴弹发射器）
    M320:
        Item_Information:
            Attachments:
                Type: accessory
                Toggle_Delay: 5
                Sounds_Toggle: NOTE_STICKS-1-2-0
        Shooting:
            Cancel_Left_Click_Block_Damage: true
            Cancel_Right_Click_Interactions: true
            Recoil_Amount: 2
            Projectile_Amount: 1
            Projectile_Type: egg
            Projectile_Speed: 20
            Projectile_Damage: 1
            Sounds_Shoot: EXPLODE-1-2-0
        Sneak:
            Enable: true
            No_Recoil: true
        Reload:
            Enable: true
            Reload_Amount: 1
            Reload_Duration: 45
            Sounds_Reloading: PISTON_EXTEND-1-1-10,SKELETON_WALK-1-0-20,PISTON_RETRACT-1-1-35
        Particles:
            Enable: true
            Particle_Impact_Anything: BLOCK_BREAK-24
        Explosions:
            Enable: true
            Damage_Multiplier: 10
            Explosion_No_Grief: true
            Explosion_Radius: 5
            On_Impact_With_Anything: true
            Projectile_Activation_Time: 5
            Sounds_Shooter: SHOOT_ARROW-2-2-0

***

<a id="desert-eagle-dual-pistols"></a>

#### Desert Eagle（双持手枪）
    Deagle:
        Item_Information:
            Item_Name: "&eDesert Eagle"
            Item_Type: 417
            Item_Lore: "&eDual pistols.|&eLeft/right click to shoot.|&eShoot enemies in the back|&efor bonus backstab damage."
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

***

<a id="bazooka-rocket-launcher"></a>

#### Bazooka（火箭发射器）
    Bazooka:
        Item_Information:
            Item_Name: "&eBazooka"
            Item_Type: 417
            Item_Lore: "&eRocket launcher.|&eFire down at your|&efeet to rocket-jump.|&eNegates fall damage."
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

***

<a id="python-revolver-w-tactical-knife"></a>

#### Python（带战术匕首的左轮手枪）
    Python:
        Item_Information:
            Item_Name: "&ePython &l/&e Knife"
            Item_Type: 417
            Item_Lore: "&eRevolver with high power.|&eLeft click to melee enemies|&ewith the tactical knife."
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

***

<a id="tactical-knife-melee-attachment"></a>

#### Tactical Knife（近战附件）
    Tactical_Knife:
        Item_Information:
            Item_Name: "&eTactical Knife"
            Item_Type: 288
            Item_Lore: "&eA melee attachment.|&eNot intended for standalone use."
            Melee_Mode: true
            Sounds_Acquired: SHOOT_ARROW-1-0-0
            Hidden_From_List: true
        Shooting:
            Cancel_Left_Click_Block_Damage: true
            Cancel_Right_Click_Interactions: true
            Delay_Between_Shots: 20
            Projectile_Damage: 40
        Particles:
            Enable: true
            Particle_Hit: BLOCK_BREAK-55
        Hit_Events:
            Enable: true
            Sounds_Shooter: SHOOT_ARROW-1-0-0,SLIME_WALK-1-1-1

***

<a id="frag-grenade-explosive"></a>

#### Frag Grenade（爆炸物）
    Grenade:
        Item_Information:
            Item_Name: "&eFrag Grenade"
            Item_Type: 402
            Item_Lore: "&eExplodes three seconds after launch."
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

***

<a id="riot-shield-protection-device"></a>

#### Riot Shield（防护装置）
    Riotshield:
        Item_Information:
            Item_Name: "&eRiot Shield"
            Item_Type: 267
            Item_Lore: "&eBlocks all melee and ranged attacks.|&eIneffective against attacks from behind."
            Sounds_Acquired: BAT_TAKEOFF-1-1-0
            Remove_Unused_Tag: true
        Riot_Shield:
            Enable: true
            Durability_Loss_Per_Hit: 10
            Sounds_Blocked: GLASS-2-2-0
            Sounds_Break: ITEM_BREAK-2-1-0

***

<a id="olympia-break-action-shotgun"></a>

#### Olympia（折管式霰弹枪）
    Olympia:
        Item_Information:
            Item_Name: "&eOlympia"
            Item_Type: 417
            Item_Lore: "&eDouble-barreled shotgun.|&eDeadly at close range.|&eIneffective at longer ranges.|&eFires incendiary ammo."
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

***

<a id="hunting-rifle-bolt-action-rifle"></a>

#### Hunting Rifle（栓动步枪）
    Hunting:
        Item_Information:
            Item_Name: "&eHunting Rifle"
            Item_Type: 417
            Item_Lore: "&eBolt-action rifle with high accuracy.|&eEquipped with a night vision scope.|&eDeals double damage on headshots."
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
            Normal: "&e<victim> was sniped by <shooter>'s Hunting Rifle!"
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

***

<a id="type-95-assault-rifle"></a>

#### Type 95（突击步枪）
    Type95:
        Item_Information:
            Item_Name: "&eType 95"
            Item_Type: 417
            Item_Lore: "&eSemi-automatic with three round burst fire.|&eGhast Tears are required for reloads."
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

***

<a id="ak-47-assault-rifle"></a>

#### AK-47（突击步枪）
    AK-47:
        Item_Information:
            Item_Name: "&eAK-47"
            Item_Type: 417
            Item_Lore: "&eFully automatic with high power.|&eEffective at medium range.|&eControls are inverted."
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

***

<a id="flashbang-tactical-grenade"></a>

#### Flashbang（战术手榴弹）
    Flashbang:
        Item_Information:
            Item_Name: "&eFlashbang"
            Item_Type: 351~8
            Item_Lore: "&eDisorientates the target upon detonation."
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

***

<a id="toaster-incendiary-landmine"></a>

#### Toaster（燃烧地雷）
    Toaster:
        Item_Information:
            Item_Name: "&eToaster"
            Item_Type: 343
            Item_Lore: "&eAnti-personnel mine.|&eTriggers a fiery explosion when:|&e- walked into by mobs or players|&e- struck with fists or items|&e- shot by projectiles"
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
            Message_Trigger_Placer: "&e<victim> has triggered your mine!"
            Message_Trigger_Victim: "&eYou have triggered <shooter>'s mine!"
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

***

<a id="harrier-strike-precision-airstrike"></a>

#### Harrier Strike（精确空袭）
    Airstrike:
        Item_Information:
            Item_Name: "&eHarrier Strike"
            Item_Type: 76
            Item_Lore: "&eCalls in an airstrike at the|&eposition of the thrown flare."
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
            Message_Call_Airstrike: "&eFriendly airstrike on the way."
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

***

<a id="putty-remote-detonated-explosive"></a>

#### Putty（遥控炸弹）
    Putty:
        Item_Information:
            Item_Name: "&ePutty"
            Item_Type: 404
            Item_Lore: "&eRemote explosives.|&eRight click to throw.|&eLeft click to detonate."
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

***

<a id="c4-remote-detonated-explosive"></a>

#### C4（遥控炸弹）
    C4:
        Item_Information:
            Item_Name: "&eC4"
            Item_Type: 69
            Item_Lore: "&eRemote explosives.|&eRight click to place.|&eLeft click to detonate."
            Sounds_Acquired: BAT_TAKEOFF-1-1-0
        Shooting:
            Cancel_Left_Click_Block_Damage: true
        Explosive_Devices:
            Enable: true
            Device_Type: remote
            Device_Info: 2-1A-TheStabbyBunny
            Sounds_Deploy: CHICKEN_EGG_POP-1-1-0
            Message_Disarm: "&eYou have disarmed an explosive device."
            Message_Trigger_Placer: "&e<victim> has set off your C4!"
            Message_Trigger_Victim: "&eYou have set off <shooter>'s C4!"
            Sounds_Alert_Placer: CLICK-1-1-0
            Sounds_Trigger: SHEEP_SHEAR-1-1-0
        Explosions:
            Enable: true
            Explosion_No_Grief: true
            Explosion_Radius: 6
            Explosion_Delay: 16
            Sounds_Explode: ZOMBIE_WOOD-2-0-0

***

<a id="trinket-booby-trap"></a>

#### Trinket（诡雷）
    Trinket:
        Item_Information:
            Item_Name: "&eTrinket"
            Item_Type: 264
            Item_Lore: "&eLeft-click to set the owner.|&eExplodes when:|&e- picked up|&e- shot out of a dispenser|&e- a chest containing this item is opened|&e- placed in an item frame, and nearby|&e ...pressure plates are stepped on.|&e&oOwners cannot trigger their own traps."
            Sounds_Acquired: BAT_TAKEOFF-1-1-0
        Explosive_Devices:
            Enable: true
            Device_Type: trap
            Device_Info: true-true-true-false-false
            Sounds_Deploy: ITEM_PICKUP-2-0-0
            Message_Trigger_Placer: "&e<victim> has triggered your booby trap!"
            Message_Trigger_Victim: "&eYou have triggered <shooter>'s booby trap!"
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

***

<a id="cocopops-cluster-bomb"></a>

#### CocoPops（集束炸弹）
    CocoPops:
        Item_Information:
            Item_Name: "&eCocoPops"
            Item_Type: 351~3
            Item_Lore: "&eA cluster bomb that releases|&e10 bomblets upon detonation."
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