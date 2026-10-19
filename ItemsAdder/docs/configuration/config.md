---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 4.0.18
---

# config.yml

文件：`config.yml`。版本：`4.0.18`。

主配置。

连接信息或服务器标识已替换为示例值，使用时填写自己的信息。

## `metrics` { #metrics }

```yaml title="config.yml · metrics"
metrics: true
```

## `update-checker` { #update-checker }

```yaml title="config.yml · update-checker"
update-checker: true
```

## `server` { #server }

```yaml title="config.yml · server"
server:
  address: "HOST"
  port: 25565
```

## `resource-pack` { #resource-pack }

```yaml title="config.yml · resource-pack"
resource-pack:
  uuid: "00000000-0000-0000-0000-000000000000"
  auto_apply:
    enabled: true
    before_join: true
    delay_ticks: 1
  kick-player-on-decline: true
  kick-player-on-fail: true
  hosting:
    no-host:
      enabled: false
    simple_self_host:
      enabled: true
      server_address: "HOST"
      optimization:
        block_non_game_requests: true
        max_downloads_per_ip: 5
        max_speed_in_megabyte_ps: 30
    lobfile:
      enabled: false
    external-host:
      enabled: false
      url: ''
      skip_url_file_type_check: false
    self-host:
      enabled: false
      server-ip: "HOST"
      pack-port: 25565
      append-port: true
      protection:
        block_non_game_requests: false
        rate_limit:
          enabled: true
          max_requests: 3
          period_seconds: 2
          cooldown:
            enabled: true
            duration_minutes: 30
            trigger_on_failed_times: 5
  title:
    enabled: true
  fix_force_unicode_font_images: true
  allow_other_plugins_resourcepacks: true
  notify_other_plugins_resourcepacks: true
  protect-player:
    lock-player: true
    cancel_commands: true
    cancel_teleport: true
    force_cancel_movement: true
  command:
    usage-cooldown-seconds: 60
  custom-font:
    enabled: false
    name: ipaexg.ttf
    shift: '[0,0]'
    size: 11.0
    oversample: 2.0
  thin-font:
    enabled: false
  zip:
    extract_internal_utility_assets: true
    protect-file-from-unzip:
      protection_1: true
      protection_2: true
      protection_3: true
      short_texture_references: true
    compress-png-files: true
    compress-json-files: true
    compress-shader-files: true
    validate-shader-files: true
    compress_sounds:
      enabled: true
      bitrate_quality: 100
    custom_armors_shaders_legacy:
      vanilla:
        overwrite_leather_layers: true
        generate_shader:
          1_21_4_lower: true
          1_21_5_plus: true
      optifine:
        generate_cit:
          1_20_4_lower: false
    emotes:
      legacy_shaders: false
      1_21_5_to_1_21_9_shaders: false
      1_21_4_plus_modern_method: true
    models:
      fix_dark_in_inventory: true
      fix_missing_particle: true
      log_non_standard_rotations: true
      fix_1_21_11_plus_atlas_items_models:
        enabled: true
        models: []
    ignore-files-ext:
    - db
    - yml
    - xcf
    - psd
    - html
    - gz
    - rar
    - zip
    - 7z
    contents-folders-priority:
    - vanilla
    - _iainternal
    merge_other_plugins_resourcepacks_folders:
    - ModelEngine/resource pack
  items:
    CustomModelData-starting-value:
      ALL: 10000
      DIAMOND: 11000
  custom_blocks_sounds_patch:
    enabled: true
    step: true
    other: true
  pre_1_21_2_shaders_fix:
    enabled: true
```

## `config_files` { #config_files }

```yaml title="config.yml · config_files"
config_files:
  lang: en
  dictionaries-lang: en
  force-sync-loading: false
```

## `blocks` { #blocks }

```yaml title="config.yml · blocks"
blocks:
  custom:
    note: true
    mushroom: true
    chorus: true
    wire: false
    fire: false
    entity:
      enabled: true
      render-radius: 48
      max-displays-per-player: 512
      max-blocks-per-chunk: 256 # 设为 0 可关闭放置数量限制。
      fallback-vanilla-block: GRAY_CONCRETE
      update-interval: 2
      warm-slot-timeout: 40
  worlds:
  - '*'
  - example_world_*
  - '*_example_nether'
  - '!example_disabled_blocks_world'
  - '!example_disabled_blocks_world_*'
  cancel-break-wrong-tool:
    enabled: true
    send-actionbar: true
  fix-liquids-flow: true
  fix-floating-blocks: true
  fix-glitched-blocks:
    enabled: true
    only-new-chunks: false
  fix-reverted-custom-blockstates:
    enabled: true
  convert-vanilla-blocks:
    enabled: false
    only-new-chunks: true
  remove-unused-palettes-on-region-save: false
  convert_paper_to_block_in_inventory: false
```

## `items` { #items }

```yaml title="config.yml · items"
items:
  fix-show-attack-and-damage-as-lore: true
  hide-custom-durability-lore: true
  fix_trades_guis_match_custom_items:
    itemsadder_trade_machines: true
    vanilla_villagers: false
    other_plugins: true
  optimizations:
    kick_on_quickbar_spam:
      enabled: true
      ms: 200
      clicks: 6
  update-legacy-items:
    enabled: true
    update_durability: true
  auto_update:
    enabled: true
    fix_unstackable_items_on_click: true
```

## `liquids` { #liquids }

```yaml title="config.yml · liquids"
liquids:
  enabled: true
```

## `huds` { #huds }

```yaml title="config.yml · huds"
huds:
  enabled: true
  force_color:
    enabled: false
    color: '#FFFFFF'
```

## `cooldown_bars` { #cooldown_bars }

```yaml title="config.yml · cooldown_bars"
cooldown_bars:
  enabled: true
  refresh_ticks: 1
  bossbar:
    color: WHITE
    style: SOLID
```

## `loots` { #loots }

```yaml title="config.yml · loots"
loots:
  allow-loots-drop-from-spawners-using-silk-touch: true
```

## `compatibility` { #compatibility }

```yaml title="config.yml · compatibility"
compatibility:
  worldguard:
    show_legacy_furniture_flags: false
  advanced_enchantments:
    enable_custom_enchants_in_items_configs: false
```

## `cache_font_images_and_effects_replacements` { #cache_font_images_and_effects_replacements }

```yaml title="config.yml · cache_font_images_and_effects_replacements"
cache_font_images_and_effects_replacements: true
```

## `font_images` { #font_images }

```yaml title="config.yml · font_images"
font_images:
  chat:
    enabled: true
    add_hover_suggestion: true
    tab_autocompletion_1_19_1_plus: true
  iaimage-book:
    max-line-length: 18
    placeholder-font: minecraft:default
  command:
    enabled: true
    commandblocks: true
    excluded:
    - home
    - sethome
    - tpa
  customitem_name_and_lore:
    enabled: true
  sign:
    enabled: true
  book:
    enabled: true
  anvil:
    enabled: true
  inventory-title:
    enabled: true
  scoreboard-teams:
    enabled: false
    update-every-ticks: 3600
```

## `text_effects` { #text_effects }

```yaml title="config.yml · text_effects"
text_effects:
  enabled: true
  hide_scoreboard_numbers: false
  hide_scoreboard_numbers_old_clients: false
  legacy_colors_compatibility: true
  chat:
    enabled: true
  customitem_name_and_lore:
    enabled: true
  sign:
    enabled: true
  book:
    enabled: true
  anvil:
    enabled: true
```

## `entities` { #entities }

```yaml title="config.yml · entities"
entities:
  max-furniture-vehicles-per-chunk: 30
  max_furniture_per_chunk: 20
  custom_entities:
    enabled: true
    emotes:
      enabled: true
      third_person_view: false
    max_per_chunk: 5
    expert_users:
      delay_packets: false
      disguises_lag_compensation: true
  furniture:
    auto_convert_to_item_display: false
    auto_update_transformations: true
```

## `crops` { #crops }

```yaml title="config.yml · crops"
crops:
  avg_seconds_per_stage: 240
  max_crops_in_area: 1000
  area_limit_blocks_radius: 32
  interaction:
    # 改善自定义作物碰撞箱的选择判定，避免被附近的原版方块干扰。
    precise_hitbox_targeting: true
    # 便于按住攻击键连续收获作物。
    continuous_harvesting_assistance: true
  rendering:
    tick_interval: 2
    max_shown_per_player: 1400
    radius_blocks: 32
    billboard:
      enabled: true
      distance: 10
    fov_render_limit: false
    checkerboard_pattern:
      enabled: true
      distance: 8
```

## `recipes` { #recipes }

```yaml title="config.yml · recipes"
recipes:
  hide-vanilla-unrecognized-recipe-errors: true
  fix-packet-too-large-kick: false
  show-no-permission-popup-in-recipebook: true
  show-no-permission-chat-message: false
  crafting:
    enabled: true
  cooking:
    enabled: true
  anvil:
    enabled: true
  smithing:
    enabled: true
  custom-recipes:
    unlock:
      automatically: true
      all-on-join: false
  remove-vanilla-recipes:
    enabled: true
    list:
      DIAMOND_SWORD: false
      IRON_INGOT: false
```

## `player_stats` { #player_stats }

```yaml title="config.yml · player_stats"
player_stats:
  save_type: CUSTOM_NBT # CUSTOM_NBT, PLAYER_DAT
```

## `show_plugin_logo_on_enable` { #show_plugin_logo_on_enable }

```yaml title="config.yml · show_plugin_logo_on_enable"
show_plugin_logo_on_enable: true
```

## `advanced` { #advanced }

```yaml title="config.yml · advanced"
advanced:
  legacy_shader_armor_conversion:
    append_new_equipment_tag:
      enabled: false
    completely_convert_to_new_equipment_tag:
      enabled: false
      new_armor_material: IRON
  update_resource_to_graphics: false
  ffmpeg:
    enabled: true
    download: true
  on_registries_changes:
    auto_re_join:
      enabled: true
    kick:
      enabled: false
```

## `debug` { #debug }

```yaml title="config.yml · debug"
debug:
  benchmark: false
  resourcepacks:
    log_player_install: false
    compression:
      files: false
      overlays: false
      duplicate_textures: false
  items:
    log-files-loading: false
    log-files-reloading: false
    log-items-loading: false
    log-items-loading-disabled: false
    log-font-images-loading: false
    log-huds-loading: false
    log-attribute-modifiers-loading: false
    log-warnings: false
    log-loots-loading: false
    log-loots-loading-disabled: false
    log-armors-loading: false
  recipes:
    log-recipes-loading: false
    log-recipes-loading-disabled: false
    log-recipes-removed-vanilla: false
    log-fix-packet-too-large: false
  blocks:
    log-save-load:
      enabled: false
      min-ms: 0
    log-convert-vanilla-blocks: false
    log-fix-bugged-blocks: false
    log-unusual-block-break: false
    log-unknown-block-break: false
  blocks-populators:
    log-loading: false
    log-loading-disabled: false
    log-loading-no-populators: false
    log-generation: false
  trees-populators:
    log-loading: false
    log-loading-disabled: false
    log-loading-no-populators: false
    log-generation: false
  surface-decorators:
    log-loading: false
    log-loading-disabled: false
    log-loading-no-decorators: false
    log-generation: false
  cave-decorators:
    log-loading: false
    log-loading-disabled: false
    log-loading-no-decorators: false
    log-generation: false
  player-stats:
    log-save: false
  performance:
    loading-ms: true
  huds:
    log-triggers: false
  other:
    log-dictionaries-loading: false
    log-liquids-loading: false
    log-minecraft_lang_overwrite-loading: false
  categories:
    log-total-loaded: true
    log-single-loaded: false
    log-single-loaded-overwrite: false
    log-single-skip: false
    log-icon-failed-load: false
  entities:
    log-files-loading: false
    log-entities-loading: false
    log-entities-loading-disabled: false
    log_bones_spawning: false
  issues:
    log_font_image_replace_json_syntax_exception: true
  scripts:
    log_compilation: true
    log_execution: true
```
