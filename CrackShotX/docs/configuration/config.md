---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 1.1.0
---

# config.yml

文件：`config.yml`。版本：`1.1.0`。

主配置。

## `Language` { #language }

```yaml title="config.yml · Language"
# CrackShotX 配置文件
# 改完以后用 /csx reload 生效。

# 提示使用的语言：zh_CN（简体中文）或 en_US（英文）。
Language: zh_CN
```

## `Visual_Fix` { #visual_fix }

```yaml title="config.yml · Visual_Fix"
# 弹道视觉修复
# 弹丸速度很高时（武器配置里的 Projectile_Speed 大于 39），玩家看到的弹道会向一侧弯，
# 实际命中并不受影响。开启后弹道看起来是直的。
# 需要服务器装有 PacketEvents 或 ProtocolLib 其中一个。
# 1.21.9 及以后的版本本身没有这个问题，会自动跳过。
Visual_Fix:
    Enable: true
    # 用哪个发包库：auto（自动，两个都装了就用 PacketEvents）、PacketEvents、ProtocolLib
    Packet_Library: auto
```

## `Panel` { #panel }

```yaml title="config.yml · Panel"
Panel:
    Enable: true
    # 把每次发放和撤回记到 plugins/CrackShotX/logs/ 下
    Audit_Log: true
```

## `MythicMobs` { #mythicmobs }

```yaml title="config.yml · MythicMobs"
# MythicMobs 对接：怪物掉落里能写枪，技能条件能认枪，能按怪物调武器伤害。只支持 MythicMobs 5.x。
MythicMobs:
    Enable: true
```

## `AttributePlus` { #attributeplus }

```yaml title="config.yml · AttributePlus"
# AttributePlus 对接：枪的伤害吃 AttributePlus 的属性（物理伤害、暴击、吸血、防御、闪避这些）。只支持 AttributePlus 3.3.3.6。
# 想让两个插件互不干扰，把 Weapon_Damage 改成 false，不要关 Enable：
# 关掉 Enable 会回到两个插件各管各的样子，爆炸类武器会多打出一截伤害、莫名其妙地吸血。
AttributePlus:
    Enable: true
    # 武器伤害进不进 AttributePlus 的属性计算。关掉以后枪只按 CrackShot 自己的伤害打
    Weapon_Damage: true
    # 不进属性计算的武器，填内部名，比如 [Bazooka, Grenade]
    Excluded_Weapons: []
```

## `NeigeItems` { #neigeitems }

```yaml title="config.yml · NeigeItems"
# NeigeItems 对接：NeigeItems 的物品能当 CrackShot 的枪和弹药。按物品 ID 认，随机出来的名字和说明不影响开火。
# 验证过的是 NeigeItems 1.21.174。
NeigeItems:
    Enable: true
    # 哪些 NeigeItems 物品是枪：左边是 NeigeItems 的物品 ID，右边是 CrackShot 的武器名。去掉下面的 # 照着写
    Weapons:
        # Legend_Rifle: AK-47
    # 哪些 NeigeItems 物品是弹药：左边是 CrackShot 的武器名，下面列能给它当弹药的物品 ID，可以写多个。
    # 一发子弹扣弹药一点耐久；没有耐久就扣一次使用次数；两样都没有就扣一个。什么时候扣，照这把枪本来的配置
    Ammo:
```

## `PlaceholderAPI` { #placeholderapi }

```yaml title="config.yml · PlaceholderAPI"
        # AK-47:
        #     - Rifle_Magazine

# PlaceholderAPI 对接：计分板、聊天这些插件能用 %crackshot_ammo% 这类变量显示玩家手里的枪；
# 反过来，CrackShot 发给玩家的文字里也能写别的插件的变量。全部变量见使用说明。
PlaceholderAPI:
    Enable: true
    # 解析 CrackShot 发给玩家的提示、武器的消息、武器执行的命令里的变量。物品的名字和说明不解析
    Parse_Messages: true
```

## `WorldGuard` { #worldguard }

```yaml title="config.yml · WorldGuard"
# WorldGuard 对接：用区域标志规定哪里不能开枪、不受武器伤害、不能炸、不能放地雷，以及能用哪些枪。
# 标志用 WorldGuard 的命令设置，比如 /rg flag spawn crackshot-shoot deny。只支持 WorldGuard 7.x。
# 管理员也受这些标志限制，要让某人不受限制，给 crackshotx.bypass.region 权限。
WorldGuard:
    Enable: true
    # 同一名玩家多久提示一次“这里不能开枪”，单位是秒
    Message_Cooldown: 3
```
