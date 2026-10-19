---
title: Stop Sound
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/StopSound
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Stop Sound {#stop-sound}

## 说明 {#description}

停止目标实体播放原版或资源包声音。声音列表见[此处](https://minecraft.wiki/w/Sounds.json#sound_events)，使用 Sound Event 一列。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| sound | s | 要停止播放的声音 | entity.zombie.attack_iron_door |
| soundcategory | source, sc, category | 播放声音所用的分类，可用于资源包 | MASTER |

### SoundCategory 属性 {#soundcategory-attribute}

声音类别列表可以在[此处](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/SoundCategory.html)找到。

## 示例 {#examples}

```yaml
SilenceEndermanSkill:
  Skills:
  - stopsound{s=entity.enderman.scream} @PIR{r=10}
```

## 别名 {#aliases}

- effect:stopsound
- e:ss
- ss
