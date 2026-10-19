---
title: weapons/defaultAttachments.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: weapons/defaultAttachments.yml
source_version: 0.98.13-x6
---

# weapons/defaultAttachments.yml

文件：`weapons/defaultAttachments.yml`。版本：`0.98.13-x6`。

随包配置。

## `M320` { #m320 }

```yaml title="weapons/defaultAttachments.yml · M320"
# CrackShot 自带的示例配件（中文版）：名字、说明、消息换成了中文，武器内部名和配置节点和原版一样。
# 这个文件只在 weapons 文件夹是空的时候生成一次，你改过以后插件不会再覆盖它。
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
```

## `Tactical_Knife` { #tactical_knife }

```yaml title="weapons/defaultAttachments.yml · Tactical_Knife"
Tactical_Knife:
    Item_Information:
        Item_Name: "&e战术刀"
        Item_Type: 288
        Item_Lore: "&e近战配件。|&e不能单独使用。"
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
```
