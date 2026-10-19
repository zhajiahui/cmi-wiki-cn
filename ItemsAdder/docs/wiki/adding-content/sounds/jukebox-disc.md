---
title: "音乐唱片与唱片机"
source_url: "https://wiki.itemsadder.com/adding-content/sounds/jukebox-disc"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 音乐唱片与唱片机

#### 创建唱片物品

在配置中创建新物品

```yaml
info:
  namespace: my_sounds
items:
  song_1_disc:
    display_name: "Song 1 Disc"
    graphics:
      texture: item/song_1
    jukebox_disc:
      song: my_sounds:song_1
```

本例添加了名为 `jukebox_disc` 的特殊属性。\
此属性允许将物品放入唱片机。

**`name`**

要播放的声音，本例为 `my_sounds:song_1`。

**唱片机歌曲声音**

本例将声音文件放入 `contents/my_sounds/sounds/song_1.ogg`。

```yaml
info:
  namespace: my_sounds
sounds:
  song_1:
    path: song_1
    settings: # Optional
      subtitle: "Song 1 Disc" # Optional (No default value)
      volume: 1.0 # Optional (Default value: 1.0)
      pitch: 1.0 # Optional (Default value: 1.0)
      weight: 1 # Optional (Default value: 1)
      stream: true # Optional (Default value: false)
      attenuation_distance: 10 # Optional (Default value: 16)
      preload: true # Optional (Default value: false)
    jukebox:
      enabled: true
      description: "Song 1"
      comparator_output: 15 # Optional (Default value: 15)
```

本例设置了 `jukebox` 属性，使此声音可用于 Minecraft 1.21.1+ 新增的唱片机组件。

**`description`**

此属性用于在玩家快捷栏上方显示唱片名称。

在配置中创建新物品。

```yaml
  music_disc_cdk_sunday:
    display_name: display-name-music_disc_cdk_sunday
    permission: music_disc_cdk_sunday
    lore:
    - '&7Cdk - Sunday'
    resource:
      material: STICK
      generate: true
      textures:
      - item/music_disc_cdk_sunday.png
    behaviours:
      music_disc:
        song:
          name: my_sounds:music_disc.cdk_sunday
          description: Cdk - Sunday
```

本例添加了名为 `music_disc` 的特殊行为。

**`name`**

要播放的声音，本例为 `my_sounds:music_disc.cdk_sunday`。
