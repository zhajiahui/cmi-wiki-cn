---
title: Particle Types
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle Types

以下是已实现粒子的列表，与其 DataType 组相关。根据它们所拥有的DataType，可以使用的属性也会相应变化。

**此列表的最新版本始终位于[此处](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html)的 spigot Javadoc 中**

- [DataTypes](particle-types.md#datatypes)
  - [ItemStack](particle-types.md#itemstack)
  - [BlockData](particle-types.md#blockdata)
  - [MaterialData](particle-types.md#materialdata)
  - [Color](particle-types.md#color)
  - [DustOptions](particle-types.md#dustoptions)
  - [DustTransition](particle-types.md#dusttransition)
  - [Spell](particle-types.md#spell)
- [Particles](particle-types.md#particles)

# DataTypes {#datatypes}

## ItemStack {#itemstack}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m | itemstack 粒子所使用的材质。 | STONE |

## BlockData {#blockdata}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m | blockdata 粒子所使用的材质。 | STONE |

## MaterialData {#materialdata}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m | materialdata 粒子所使用的材质。 | STONE |

## Color {#color}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c | 粒子的颜色。 | #FF0000 |

## DustOptions {#dustoptions}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c | 粒子的颜色。 | #FF0000 |
| size |  | 粒子的大小。 | 1 |

## DustTransition {#dusttransition}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c, color1, c1, fromcolor, fc | 粒子的起始颜色。 | #FF0000 |
| color2 | c2, tocolor, tc | 粒子渐变到的颜色。 | #0000FF |
| size |  | 粒子的大小。 | 1 |

## Spell 粒子 {#spell}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c | 粒子的颜色。 | #FF0000 |
| power | p | 法术粒子的威力。 | 1 |

# Particles {#particles}

| [Angry_Villager](particle-types/angry_villager.md) | [Ash](particle-types/ash.md) | [Barrier](particle-types/barrier.md) | [Block](particle-types/block.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Block_Crumble](particle-types/block_crumble.md) | [Block_Dust](particle-types/block_dust.md) | [Block_Marker](particle-types/block_marker.md) | [Bubble](particle-types/bubble.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Bubble_Column_Up](particle-types/bubble_column_up.md) | [Bubble_Pop](particle-types/bubble_pop.md) | [Campfire_Cosy_Smoke](particle-types/campfire_cosy_smoke.md) | [Campfire_Signal_Smoke](particle-types/campfire_signal_smoke.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Cherry_Leaves](particle-types/cherry_leaves.md) | [Cloud](particle-types/cloud.md) | [Composter](particle-types/composter.md) | [Copper_Fire_Flame](particle-types/copper_fire_flame.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Crimson_Spore](particle-types/crimson_spore.md) | [Crit](particle-types/crit.md) | [Current_Down](particle-types/current_down.md) | [Damage_Indicator](particle-types/damage_indicator.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Dolphin](particle-types/dolphin.md) | [Dragon_Breath](particle-types/dragon_breath.md) | [Dripping_Dripstone_Lava](particle-types/dripping_dripstone_lava.md) | [Dripping_Dripstone_Water](particle-types/dripping_dripstone_water.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Dripping_Honey](particle-types/dripping_honey.md) | [Dripping_Lava](particle-types/dripping_lava.md) | [Dripping_Obsidian_Tear](particle-types/dripping_obsidian_tear.md) | [Dripping_Water](particle-types/dripping_water.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Dust](particle-types/dust.md) | [Dust_Color_Transition](particle-types/dust_color_transition.md) | [Dust_Pillar](particle-types/dust_pillar.md) | [Dust_Plume](particle-types/dust_plume.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Effect](particle-types/effect.md) | [Egg_Crack](particle-types/egg_crack.md) | [Elder_Guardian](particle-types/elder_guardian.md) | [Electric_Spark](particle-types/electric_spark.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Enchant](particle-types/enchant.md) | [Enchanted_Hit](particle-types/enchanted_hit.md) | [End_Rod](particle-types/end_rod.md) | [Entity_Effect](particle-types/entity_effect.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Explosion](particle-types/explosion.md) | [Explosion_Emitter](particle-types/explosion_emitter.md) | [Falling_Dripstone_Lava](particle-types/falling_dripstone_lava.md) | [Falling_Dripstone_Water](particle-types/falling_dripstone_water.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Falling_Dust](particle-types/falling_dust.md) | [Falling_Honey](particle-types/falling_honey.md) | [Falling_Lava](particle-types/falling_lava.md) | [Falling_Nectar](particle-types/falling_nectar.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Falling_Obsidian_Tear](particle-types/falling_obsidian_tear.md) | [Falling_Spore_Blossom](particle-types/falling_spore_blossom.md) | [Falling_Water](particle-types/falling_water.md) | [Firefly](particle-types/firefly.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Firework](particle-types/firework.md) | [Fishing](particle-types/fishing.md) | [Flame](particle-types/flame.md) | [Flash](particle-types/flash.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Glow](particle-types/glow.md) | [Glow_Squid_Ink](particle-types/glow_squid_ink.md) | [Gust](particle-types/gust.md) | [Gust_Emitter_Large](particle-types/gust_emitter_large.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Gust_Emitter_Small](particle-types/gust_emitter_small.md) | [Happy_Villager](particle-types/happy_villager.md) | [Heart](particle-types/heart.md) | [Infested](particle-types/infested.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Instant_Effect](particle-types/instant_effect.md) | [Item](particle-types/item.md) | [Item_Slime](particle-types/item_slime.md) | [Item_Snowball](particle-types/item_snowball.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Landing_Honey](particle-types/landing_honey.md) | [Landing_Lava](particle-types/landing_lava.md) | [Landing_Obsidian_Tear](particle-types/landing_obsidian_tear.md) | [Large_Smoke](particle-types/large_smoke.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Lava](particle-types/lava.md) | [Light](particle-types/light.md) | [Mycelium](particle-types/mycelium.md) | [Nautilus](particle-types/nautilus.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Note](particle-types/note.md) | [Ominous_Spawning](particle-types/ominous_spawning.md) | [Pale_Oak_Leaves](particle-types/pale_oak_leaves.md) | [Poof](particle-types/poof.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Portal](particle-types/portal.md) | [Raid_Omen](particle-types/raid_omen.md) | [Rain](particle-types/rain.md) | [Reverse_Portal](particle-types/reverse_portal.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Scrape](particle-types/scrape.md) | [Sculk_Charge](particle-types/sculk_charge.md) | [Sculk_Charge_Pop](particle-types/sculk_charge_pop.md) | [Sculk_Soul](particle-types/sculk_soul.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Shriek](particle-types/shriek.md) | [Small_Flame](particle-types/small_flame.md) | [Small_Gust](particle-types/small_gust.md) | [Smoke](particle-types/smoke.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Sneeze](particle-types/sneeze.md) | [Snowflake](particle-types/snowflake.md) | [Sonic_Boom](particle-types/sonic_boom.md) | [Soul](particle-types/soul.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Soul_Fire_Flame](particle-types/soul_fire_flame.md) | [Spell_Mob_Ambient](particle-types/spell_mob_ambient.md) | [Spit](particle-types/spit.md) | [Splash](particle-types/splash.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Spore_Blossom_Air](particle-types/spore_blossom_air.md) | [Squid_Ink](particle-types/squid_ink.md) | [Suspended_Depth](particle-types/suspended_depth.md) | [Sweep_Attack](particle-types/sweep_attack.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Tinted_Leaves](particle-types/tinted_leaves.md) | [Totem_Of_Undying](particle-types/totem_of_undying.md) | [Trail](particle-types/trail.md) | [Trial_Omen](particle-types/trial_omen.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Trial_Spawner_Detection](particle-types/trial_spawner_detection.md) | [Trial_Spawner_Detection_Ominous](particle-types/trial_spawner_detection_ominous.md) | [Underwater](particle-types/underwater.md) | [Vault_Connection](particle-types/vault_connection.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [Vibration](particle-types/vibration.md) | [Warped_Spore](particle-types/warped_spore.md) | [Wax_Off](particle-types/wax_off.md) | [Wax_On](particle-types/wax_on.md) |
| --- | --- | --- | --- |
|  |  |  |  |

| [White_Ash](particle-types/white_ash.md) | [White_Smoke](particle-types/white_smoke.md) | [Witch](particle-types/witch.md) |
| --- | --- | --- |
|  |  |  |
