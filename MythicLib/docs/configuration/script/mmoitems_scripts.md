---
title: script/mmoitems_scripts.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: script/mmoitems_scripts.yml
source_version: 1.7.1-SNAPSHOT
---

# script/mmoitems_scripts.yml

文件：`script/mmoitems_scripts.yml`。版本：`1.7.1-SNAPSHOT`。

随包脚本。

## `blunt_attack_effect` { #blunt_attack_effect }

```yaml title="script/mmoitems_scripts.yml · blunt_attack_effect"
##############################################################################################################################
#
# 钝击、穿刺、斩击武器
#
# 默认情况下，部分武器具有穿刺效果，会对初始目标后方锥形区域内的目标造成伤害。
# 伤害传递比例较高，但与钝击、斩击武器相比，范围伤害的区域较小。
# 穿刺武器通常包括匕首、短剑、矛和骑枪。
#
# 斩击武器也能造成范围伤害，伤害传递百分比较低，但范围更大。
# 斩击武器通常包括剑、巨剑和斧。
#
# 钝击武器会对初始敌人周围的目标造成范围伤害，类似原版的横扫之刃。
# 钝击武器通常包括锤和巨杖。
#
# 以上均为 MMOItems 的默认行为，可以按需重新定义。
# 可以创建新的物品类型、武器类型和武器效果等，制作独特的配置。
#
##############################################################################################################################

# BLUNT 武器的命中攻击效果
blunt_attack_effect:
  public: true
  conditions:
    - 'cooldown{path=mmoitems_blunt}'
  mechanics:
    - 'apply_cooldown{path=mmoitems_blunt;amount=3}'
    - 'set_integer{variable=initial_target_id;value="<target.id>"}'
    - 'particle{particle=EXPLOSION_LARGE}'
    - 'sound{sound=ENTITY_PLAYER_ATTACK_CRIT;pitch=.5}'
    - 'set_double{variable=damage_ratio;value="<stat.blunt_rating> / 100"}'
    - 'script{name=propagate_damage;target={type=nearby_entities;radius="<stat.blunt_power>"}}'
```

## `slashing_attack_effect` { #slashing_attack_effect }

```yaml title="script/mmoitems_scripts.yml · slashing_attack_effect"
# SLASHING 武器的命中攻击效果
slashing_attack_effect:
  public: true
  conditions:
    - 'cooldown{path=mmoitems_slashing}'
  mechanics:
    - 'apply_cooldown{path=mmoitems_slashing;amount=3}'
    - 'set_integer{variable=initial_target_id;value="<target.id>"}'
    - 'set_double{variable=damage_ratio;value=.4}'
    - 'set_double{variable=angle;value=60}'
    - 'cast{name=propagate_damage;target={type=cone;radius=6.5;angle=60}}'
    - 'script{name=slash_attack_effect}'
```

## `piercing_attack_effect` { #piercing_attack_effect }

```yaml title="script/mmoitems_scripts.yml · piercing_attack_effect"
# PIERCING 武器的命中攻击效果
piercing_attack_effect:
  public: true
  conditions:
    - 'cooldown{path=mmoitems_piercing}'
  mechanics:
    - 'apply_cooldown{path=mmoitems_piercing;amount=3}'
    - 'set_integer{variable=initial_target_id;value="<target.id>"}'
    - 'set_double{variable=damage_ratio;value=.6}'
    - 'set_double{variable=angle;value=30}'
    - 'cast{name=propagate_damage;target={type=cone;radius=6.5;angle=30}}'
    - 'script{name=slash_attack_effect}'
```

## `propagate_damage` { #propagate_damage }

```yaml title="script/mmoitems_scripts.yml · propagate_damage"
propagate_damage:
  conditions:
    - 'can_target{}'
    - 'boolean{formula="<target.id> != <initial_target_id>"}'
  mechanics:
    - 'damage{amount="<attack.damage> * <damage_ratio>";damage_type="PHYSICAL,WEAPON"}'
```

## `slash_attack_effect` { #slash_attack_effect }

```yaml title="script/mmoitems_scripts.yml · slash_attack_effect"
# 同时用于斩击和穿刺
slash_attack_effect:
  mechanics:
    - 'copy_vector{variable=src;value=caster.location}'
    - 'set_double{variable=p;value="<caster.eye_direction.pitch> * -PI / 180"}'
    - 'add_vector{variable=src;y=1}'
    - 'script{name=sae1;counter=c2;iterations="20"}'
```

## `sae1` { #sae1 }

```yaml title="script/mmoitems_scripts.yml · sae1"
sae1:
  mechanics:
    - 'set_int{variable=c1_max;value="<c2> * <angle> / 60.0"}'
    - 'script{name=sae2;counter=c1;iterations="<c1_max>"}'
```

## `sae2` { #sae2 }

```yaml title="script/mmoitems_scripts.yml · sae2"
sae2:
  mechanics:
    - 'set_double{variable=a;value="PI / 180.0 * (90 + <caster.eye_direction.yaw> + <angle> * (-0.5 + (<c1> - 0.5) / <c1_max>))"}'
    - 'set_double{variable=d;value=".4 + <c2> / 3"}'
    - 'copy_vector{variable=inter;value=src}'
    - 'add_vector{variable=inter;x="cos(<p>) * cos(<a>) * <d>";y="sin(<p>) * <d>";z="cos(<p>) *sin(<a>) * <d>"}'
    - 'particle{particle=CRIT;target={type=variable;name=inter}}'
```

## `staff_deal_damage` { #staff_deal_damage }

```yaml title="script/mmoitems_scripts.yml · staff_deal_damage"
##############################################################################################################################
#
# 法杖攻击
#
# 可以在此创建新脚本，并使用 'Left Click Effect' 物品选项
# 为 MMOItems 的法杖或魔杖物品绑定新的攻击效果。这些脚本使用
# MythicLib 脚本语言编写，但也支持 MythicMobs 和 Fabled。
#
# 还可扩展此系统，创建完全自定义的物品类型，并在
# 左键、右键、近战攻击和右键实体交互时触发自定义效果。
#
# 技能创建的更多信息见：https://gitlab.com/phoenix-dvpmt/mythiclib/-/wikis/Skills
# 物品类型的更多信息见：    https://gitlab.com/phoenix-dvpmt/mmoitems/-/wikis/Item%20Types
#
##############################################################################################################################

staff_deal_damage:
  mechanics:
    - 'damage{amount="<stat.attack_damage>";damage_type="WEAPON,MAGIC,PROJECTILE"}'
```

## `staff_default` { #staff_default }

```yaml title="script/mmoitems_scripts.yml · staff_default"
# 默认法杖攻击效果
staff_default:
  public: true
  mechanics:
    - 'set_double{variable=range;value="non_zero(<stat.range>, 12)"}'
    - 'sound{sound=ENTITY_FIREWORK_ROCKET_TWINKLE;volume=2;pitch=.5}'
    - 'projectile{life_span=10;speed="<var.range> * 2";hit_entity=staff_default_hit;hit_block=none;tick=staff_default_tick}'
```

## `staff_default_hit` { #staff_default_hit }

```yaml title="script/mmoitems_scripts.yml · staff_default_hit"
staff_default_hit:
  mechanics:
    - 'script{name=staff_deal_damage}'
```

## `staff_default_tick` { #staff_default_tick }

```yaml title="script/mmoitems_scripts.yml · staff_default_tick"
staff_default_tick:
  mechanics:
    - 'particle{particle=CRIT;x=.3;y=.3;z=.3;amount=2}'
```

## `staff_mana` { #staff_mana }

```yaml title="script/mmoitems_scripts.yml · staff_mana"
# 法杖 "mana" 攻击效果
staff_mana:
  public: true
  mechanics:
    - 'sound{sound=ENTITY_BLAZE_SHOOT;pitch=2}'
    - 'set_double{variable=range;value="non_zero(<stat.range>, 12)"}'
    - 'copy_vector{variable=dir;value=caster.eye_direction}'
    - 'set_double{variable=rad;value=.5}'
    - 'projectile{life_span=20;speed="<range> * 2";hit_entity=staff_mana_hit;hit_block=none;tick=staff_mana_tick}'
```

## `MANA_SPIRIT` { #mana_spirit }

```yaml title="script/mmoitems_scripts.yml · MANA_SPIRIT"
# 向后兼容 MI <6.9
# 更新旧物品后可移除。
MANA_SPIRIT:
  public: true
  mechanics:
    - 'script{name=staff_mana}'
```

## `staff_mana_tick` { #staff_mana_tick }

```yaml title="script/mmoitems_scripts.yml · staff_mana_tick"
staff_mana_tick:
  mechanics:
    - 'script{name=staff_mana_tick_2;counter=c;iterations=6}'
```

## `staff_mana_tick_2` { #staff_mana_tick_2 }

```yaml title="script/mmoitems_scripts.yml · staff_mana_tick_2"
staff_mana_tick_2:
  conditions:
    - 'boolean{formula="<random.double> < .6"}'
  mechanics:
    - 'set_double{variable=a;value="<random.double> * 2 * PI"}'
    - 'copy_vector{variable=curr;value=target_location}'
    - 'set_vector{variable=diff;x="<rad> * cos(<a>)",y="<rad> * sin(<a>)";z=0}'
    - 'orient_vector{variable=diff;axis=dir}'
    - 'add_vector{variable=curr;added=diff}'
    - 'particle{particle=REDSTONE;color={red=0;green=230;blue=255};target={type=variable;name=curr}}'
```

## `staff_mana_hit` { #staff_mana_hit }

```yaml title="script/mmoitems_scripts.yml · staff_mana_hit"
staff_mana_hit:
  mechanics:
    - 'sound{sound=ENTITY_BLAZE_HURT;pitch=2}'
    - 'sphere{radius=2;tick=staff_mana_hit_tick;points=500}'
    - 'script{name=staff_deal_damage}'
```

## `staff_mana_hit_tick` { #staff_mana_hit_tick }

```yaml title="script/mmoitems_scripts.yml · staff_mana_hit_tick"
staff_mana_hit_tick:
  mechanics:
    - 'particle{particle=REDSTONE;color={red=0;green=230;blue=255}}'
```

## `LIGHTNING_SPIRIT` { #lightning_spirit }

```yaml title="script/mmoitems_scripts.yml · LIGHTNING_SPIRIT"
# 向后兼容 MI <6.9
# 更新旧物品后可移除。
LIGHTNING_SPIRIT:
  public: true
  mechanics:
    - 'script{name=staff_lightning}'
```

## `staff_lightning` { #staff_lightning }

```yaml title="script/mmoitems_scripts.yml · staff_lightning"
# 法杖 "lightning" 攻击效果
staff_lightning:
  public: true
  mechanics:
    - 'set_double{variable=range;value="non_zero(<stat.range>, 12)"}'
    - 'sound{sound=ENTITY_FIREWORK_ROCKET_BLAST;volume=2;pitch=1.5}'
    - 'raytrace{tick=staff_lightning_tick;neutral=false;range="<range>";hit_entity=staff_lightning_hit;size=.2;step=.5}'
```

## `staff_lightning_hit` { #staff_lightning_hit }

```yaml title="script/mmoitems_scripts.yml · staff_lightning_hit"
staff_lightning_hit:
  mechanics:
    - 'script{name=staff_deal_damage}'
    - 'particle{particle=FIREWORKS_SPARK;speed=.1;amount=32}'
```

## `staff_lightning_tick` { #staff_lightning_tick }

```yaml title="script/mmoitems_scripts.yml · staff_lightning_tick"
staff_lightning_tick:
  mechanics:
    - 'particle{particle=FIREWORKS_SPARK;amount=1}'
```

## `staff_xray` { #staff_xray }

```yaml title="script/mmoitems_scripts.yml · staff_xray"
# 法杖 "X-ray" 攻击效果
staff_xray:
  public: true
  mechanics:
    - 'set_double{variable=range;value="non_zero(<stat.range>, 12)"}'
    - 'sound{sound=ENTITY_FIREWORK_ROCKET_BLAST;volume=2;pitch=1.5}'
    - 'raytrace{tick=staff_xray_tick;neutral=false;range="<range>";hit_entity=staff_xray_hit;size=.2;step=.5}'
```

## `XRAY_SPIRIT` { #xray_spirit }

```yaml title="script/mmoitems_scripts.yml · XRAY_SPIRIT"
# 向后兼容 MI <6.9
# 更新旧物品后可移除。
XRAY_SPIRIT:
  public: true
  mechanics:
    - 'script{name=staff_xray}'
```

## `staff_xray_tick` { #staff_xray_tick }

```yaml title="script/mmoitems_scripts.yml · staff_xray_tick"
staff_xray_tick:
  mechanics:
    - 'particle{particle=REDSTONE;color={red=255;green=0;blue=0}}'
```

## `staff_xray_hit` { #staff_xray_hit }

```yaml title="script/mmoitems_scripts.yml · staff_xray_hit"
staff_xray_hit:
  mechanics:
    - 'script{name=staff_deal_damage}'
```

## `staff_void` { #staff_void }

```yaml title="script/mmoitems_scripts.yml · staff_void"
# 法杖 "Void" 攻击效果
staff_void:
  public: true
  mechanics:
    - 'set_double{variable=range;value="non_zero(<stat.range>, 12)"}'
    - 'sound{sound=ENTITY_BLAZE_SHOOT;volume=2;pitch=2}'
    - 'shulker_bullet{life_span=50;hit_entity=staff_void_hit}'
```

## `VOID_SPIRIT` { #void_spirit }

```yaml title="script/mmoitems_scripts.yml · VOID_SPIRIT"
# 向后兼容 MI <6.9
# 更新旧物品后可移除。
VOID_SPIRIT:
  public: true
  mechanics:
    - 'script{name=staff_void}'
```

## `staff_void_hit` { #staff_void_hit }

```yaml title="script/mmoitems_scripts.yml · staff_void_hit"
staff_void_hit:
  mechanics:
    - 'script{name=staff_deal_damage}'
    - 'helix{tick=staff_void_hit_tick}'
```

## `staff_void_hit_tick` { #staff_void_hit_tick }

```yaml title="script/mmoitems_scripts.yml · staff_void_hit_tick"
staff_void_hit_tick:
  mechanics:
    - 'particle{particle=REDSTONE;color={red=90;green=40;blue=40}}'
```

## `staff_nether` { #staff_nether }

```yaml title="script/mmoitems_scripts.yml · staff_nether"
# 法杖 "Nether" 攻击效果
staff_nether:
  public: true
  mechanics:
    - 'set_double{variable=range;value="non_zero(<stat.range>, 12)"}'
    - 'sound{sound=ENTITY_BLAZE_SHOOT;volume=2;pitch=2}'
    - 'projectile{life_span=20;speed="<var.range> * 2";hit_entity=staff_nether_hit;hit_block=none;tick=staff_nether_tick;size=.5}'
```

## `NETHER_SPIRIT` { #nether_spirit }

```yaml title="script/mmoitems_scripts.yml · NETHER_SPIRIT"
# 向后兼容 MI <6.9
# 更新旧物品后可移除。
NETHER_SPIRIT:
  public: true
  mechanics:
    - 'script{name=staff_nether}'
```

## `staff_nether_hit` { #staff_nether_hit }

```yaml title="script/mmoitems_scripts.yml · staff_nether_hit"
staff_nether_hit:
  mechanics:
    - 'script{name=staff_deal_damage}'
    - 'sound{sound=ENTITY_BLAZE_HURT;volume=2;pitch=2}'
    - 'particle{particle=FLAME;amount=12;speed=.1}'
    - 'particle{particle=LAVA;amount=6}'
```

## `staff_nether_tick` { #staff_nether_tick }

```yaml title="script/mmoitems_scripts.yml · staff_nether_tick"
staff_nether_tick:
  mechanics:
    - 'particle{particle=FLAME;x=.2;y=.2;z=.2}'
    - 'particle{particle=SMOKE_NORMAL;x=.2;y=.2;z=.2}'
```

## `staff_sunfire` { #staff_sunfire }

```yaml title="script/mmoitems_scripts.yml · staff_sunfire"
# 法杖 "Sunfire" 攻击效果
staff_sunfire:
  public: true
  mechanics:
    - 'set_double{variable=range;value="non_zero(<stat.range>, 12)"}'
    - 'ray_trace{size=.4;range="<range>";size=0;hit_block=staff_sunfire_success_block;hit_entity=staff_sunfire_success_entity}'
```

## `SUNFIRE_SPIRIT` { #sunfire_spirit }

```yaml title="script/mmoitems_scripts.yml · SUNFIRE_SPIRIT"
# 向后兼容 MI <6.9
# 更新旧物品后可移除。
SUNFIRE_SPIRIT:
  public: true
  mechanics:
    - 'script{name=staff_sunfire}'
```

## `staff_sunfire_success_block` { #staff_sunfire_success_block }

```yaml title="script/mmoitems_scripts.yml · staff_sunfire_success_block"
staff_sunfire_success_block:
  mechanics:
    - 'copy_vector{variable=meteor_tgt;value=target_location}'
    - 'script{name=staff_sunfire_success_2}'
```

## `staff_sunfire_success_entity` { #staff_sunfire_success_entity }

```yaml title="script/mmoitems_scripts.yml · staff_sunfire_success_entity"
staff_sunfire_success_entity:
  mechanics:
    - 'copy_vector{variable=meteor_tgt;value="target.bb_center"}'
    - 'script{name=staff_sunfire_success_2}'
```

## `staff_sunfire_success_2` { #staff_sunfire_success_2 }

```yaml title="script/mmoitems_scripts.yml · staff_sunfire_success_2"
staff_sunfire_success_2:
  mechanics:
    - 'sound{sound=ENTITY_WITHER_SHOOT;volume=2;pitch=2}'
    - 'set_double{variable=angle;value="<random.unif> * PI * 2"}'
    - 'set_vector{variable=meteor_src;x="<meteor_tgt.x> + 4 * cos(<angle>)";y="<meteor_tgt.y> + 10";z="<meteor_tgt.z> + 4 * sin(<angle>)"}'
    - 'copy_vector{variable=meteor_dir;value=meteor_tgt}'
    - 'sub_vec{variable=meteor_dir;subtracted=meteor_src}'
    - 'set_integer{variable=c;value=0}'
    - 'draw_line{source={type=variable;name=meteor_src};target={type=variable;name=meteor_tgt};tick=staff_sunfire_tick;end=staff_sunfire_explode;step=.7}'
```

## `staff_sunfire_explode` { #staff_sunfire_explode }

```yaml title="script/mmoitems_scripts.yml · staff_sunfire_explode"
staff_sunfire_explode:
  mechanics:
    - 'particle{particle=FLAME;speed=.12;amount=24}'
    - 'particle{particle=SMOKE_NORMAL;speed=.12;amount=24}'
    - 'particle{particle=EXPLOSION_LARGE}'
    - 'sound{sound=ENTITY_FIREWORK_ROCKET_BLAST;volume=2;pitch=2}'
    - 'script{name=staff_sunfire_hit;target={type=nearby_entities;radius=3}}'
```

## `staff_sunfire_hit` { #staff_sunfire_hit }

```yaml title="script/mmoitems_scripts.yml · staff_sunfire_hit"
staff_sunfire_hit:
  conditions:
    - 'can_target{}'
  mechanics:
    - 'script{name=staff_deal_damage}'
```

## `staff_sunfire_tick` { #staff_sunfire_tick }

```yaml title="script/mmoitems_scripts.yml · staff_sunfire_tick"
staff_sunfire_tick:
  mechanics:
    - 'particle{particle=FLAME;x=.3;y=.3;z=.3;amount=4}'
    - 'script{name=staff_sunfire_tick2}'
    - 'incr{variable=c}'
```

## `staff_sunfire_tick2` { #staff_sunfire_tick2 }

```yaml title="script/mmoitems_scripts.yml · staff_sunfire_tick2"
staff_sunfire_tick2:
  conditions:
    - 'boolean{formula="<c> % 4 == 0"}'
  mechanics:
    - 'sound{sound=BLOCK_FIRE_AMBIENT;volume=2;pitch=2}'
```

## `staff_thunder` { #staff_thunder }

```yaml title="script/mmoitems_scripts.yml · staff_thunder"
# 法杖 "Thunder" 攻击效果
staff_thunder:
  public: true
  mechanics:
    - 'set_double{variable=range;value="non_zero(<stat.range>, 12)"}'
    - 'ray_trace{size=.4;range="<range>";size=0;hit_block=staff_thunder_success_block;hit_entity=staff_thunder_success_entity}'
```

## `THUNDER_SPIRIT` { #thunder_spirit }

```yaml title="script/mmoitems_scripts.yml · THUNDER_SPIRIT"
# 向后兼容 MI <6.9
# 更新旧物品后可移除。
THUNDER_SPIRIT:
  public: true
  mechanics:
    - 'script{name=staff_thunder}'
```

## `staff_thunder_success_block` { #staff_thunder_success_block }

```yaml title="script/mmoitems_scripts.yml · staff_thunder_success_block"
staff_thunder_success_block:
  mechanics:
    - 'copy_vector{variable=meteor_tgt;value=target_location}'
    - 'script{name=staff_thunder_success_2}'
```

## `staff_thunder_success_entity` { #staff_thunder_success_entity }

```yaml title="script/mmoitems_scripts.yml · staff_thunder_success_entity"
staff_thunder_success_entity:
  mechanics:
    - 'copy_vector{variable=meteor_tgt;value="target.bb_center"}'
    - 'script{name=staff_thunder_success_2}'
```

## `staff_thunder_success_2` { #staff_thunder_success_2 }

```yaml title="script/mmoitems_scripts.yml · staff_thunder_success_2"
staff_thunder_success_2:
  mechanics:
    - 'sound{sound=ENTITY_WITHER_SHOOT;volume=2;pitch=2}'
    - 'set_double{variable=angle;value="<random.unif> * PI * 2"}'
    - 'set_vector{variable=meteor_src;x="<meteor_tgt.x> + 4 * cos(<angle>)";y="<meteor_tgt.y> + 10";z="<meteor_tgt.z> + 4 * sin(<angle>)"}'
    - 'copy_vector{variable=meteor_dir;value=meteor_tgt}'
    - 'sub_vec{variable=meteor_dir;subtracted=meteor_src}'
    - 'set_integer{variable=c;value=0}'
    - 'draw_line{source={type=variable;name=meteor_src};target={type=variable;name=meteor_tgt};tick=staff_thunder_tick;end=staff_thunder_explode;step=.3;points_per_tick=4}'
```

## `staff_thunder_explode` { #staff_thunder_explode }

```yaml title="script/mmoitems_scripts.yml · staff_thunder_explode"
staff_thunder_explode:
  mechanics:
    - 'particle{particle=FIREWORKS_SPARK;speed=.12;amount=24}'
    - 'sound{sound=ENTITY_FIREWORK_ROCKET_BLAST;volume=2;pitch=2}'
    - 'script{name=staff_thunder_hit;target={type=nearby_entities;radius=3}}'
```

## `staff_thunder_hit` { #staff_thunder_hit }

```yaml title="script/mmoitems_scripts.yml · staff_thunder_hit"
staff_thunder_hit:
  conditions:
    - 'can_target{}'
  mechanics:
    - 'script{name=staff_deal_damage}'
```

## `staff_thunder_tick` { #staff_thunder_tick }

```yaml title="script/mmoitems_scripts.yml · staff_thunder_tick"
staff_thunder_tick:
  mechanics:
    - 'particle{particle=FIREWORKS_SPARK}'
    - 'script{name=staff_thunder_tick2}'
    - 'incr{variable=c}'
```

## `staff_thunder_tick2` { #staff_thunder_tick2 }

```yaml title="script/mmoitems_scripts.yml · staff_thunder_tick2"
staff_thunder_tick2:
  conditions:
    - 'boolean{formula="<c> % 2 == 0"}'
  mechanics:
    - 'sound{sound=BLOCK_NOTE_BLOCK_HAT;volume=2;pitch=2}'
```

## `whip_attack` { #whip_attack }

```yaml title="script/mmoitems_scripts.yml · whip_attack"
##############################################################################################################################
#
# MMOItems 的其他脚本
#
##############################################################################################################################

# 鞭子攻击效果
whip_attack:
  public: true
  mechanics:
    - 'set_double{variable=range;value="non_zero(<stat.range>, 8)"}'
    - 'sound{sound=ENTITY_FIREWORK_ROCKET_BLAST;volume=2;pitch=1.5}'
    - 'raytrace{tick=whip_attack_tick;neutral=false;range="<range>";hit_entity=whip_attack_hit;size=.2;step=.5}'
```

## `whip_attack_tick` { #whip_attack_tick }

```yaml title="script/mmoitems_scripts.yml · whip_attack_tick"
whip_attack_tick:
  mechanics:
    - 'particle{particle=CRIT}'
```

## `whip_attack_hit` { #whip_attack_hit }

```yaml title="script/mmoitems_scripts.yml · whip_attack_hit"
whip_attack_hit:
  mechanics:
    - 'damage{amount="<stat.attack_damage>";damage_type="WEAPON,PHYSICAL"}'
```

## `staff_special_attack` { #staff_special_attack }

```yaml title="script/mmoitems_scripts.yml · staff_special_attack"
staff_special_attack:
  public: true
  conditions:
    - 'cooldown{path=mmoitems_staff_special}'
  mechanics:
    - 'apply_cooldown{path=mmoitems_staff_special;amount=10}'
    - 'particle{particle=EXPLOSION_LARGE}'
    - 'particle{particle=EXPLOSION_NORMAL;amount=16;speed=.1}'
    - 'sound{sound=BLOCK_ANVIL_LAND;pitch=2}'
    - 'copy_vector{variable=knockback;value=caster.eye_direction}'
    - 'set_y{variable=knockback;y=0}'
    - 'normalize_vector{variable=knockback}'
    - 'multiply_vector{variable=knockback;coef=1.1}'
    - 'set_y{variable=knockback;y=.4}'
    - 'set_velocity{vector=knockback}'
```

## `gauntlet_special_attack` { #gauntlet_special_attack }

```yaml title="script/mmoitems_scripts.yml · gauntlet_special_attack"
gauntlet_special_attack:
  public: true
  conditions:
    - 'cooldown{path=mmoitems_gauntlet}'
  mechanics:
    - 'apply_cooldown{path=mmoitems_gauntlet;amount=10}'
    - 'particle{particle=EXPLOSION_LARGE}'
    - 'sound{sound=BLOCK_ANVIL_LAND;pitch=2}'
    - 'remove_potion{effect=BLINDNESS}'
    - 'potion{effect=BLINDNESS;duration=40;level=1}'
    - 'copy_vector{variable=knockback;value=caster.eye_direction}'
    - 'set_y{variable=knockback;y=0}'
    - 'normalize_vector{variable=knockback}'
    - 'multiply_vector{variable=knockback;coef=1.3}'
    - 'set_y{variable=knockback;y=.5}'
    - 'set_velocity{vector=knockback}'
```

## `crossbow_attack` { #crossbow_attack }

```yaml title="script/mmoitems_scripts.yml · crossbow_attack"
crossbow_attack:
  public: true
  conditions:
    - 'ammo{item=ARROW;creative_infinite=true;item_ignore_tag=MMOITEMS_DISABLE_ARROW_CONSUMPTION;consume_if_met=true}'
  mechanics:
    - 'play_sound{sound=ENTITY_ARROW_SHOOT;pitch=.5}'
    - 'shoot_arrow{from_item=true;player_attack_damage=true;tick=crossbow_arrow_tick;velocity="non_zero(<stat.arrow_velocity>, 1) * 3"}'
```

## `crossbow_arrow_tick` { #crossbow_arrow_tick }

```yaml title="script/mmoitems_scripts.yml · crossbow_arrow_tick"
crossbow_arrow_tick:
  mechanics:
    - 'particle{particle=CRIT;speed=.05}'
```
