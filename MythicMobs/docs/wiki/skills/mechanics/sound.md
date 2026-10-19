---
title: Sound
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Sound
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Sound {#sound}

## 说明 {#description}

在目标实体或位置播放原版游戏或资源包中的声音。可以在[此处](https://misode.github.io/sounds/)找到广泛的声音列表。将多种声音叠加在一起可以给人一种全新声音的印象。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| sound | s | 要播放的声音 | entity.zombie.attack_iron_door |
| pitch | p | 声音的音高，范围为 0.01 到 2.0。 | 1.0 |
| volume | v | 声音的音量。 | 1.0 |
| radius | r | 声音可被听见的半径 | `volume`*16 |
| soundcategory | category, sc | 播放声音所用的分类，可用于资源包 | MASTER |
| emitter | em | 让声音播放位置动态跟随实体，而不是固定位置 |  |
| audience |  | 效果的[可见对象](../audience.md)。 | world |

### SoundCategory 属性 {#soundcategory-attribute}

声音类别列表可以在[此处](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/SoundCategory.html)找到。

### Volume 属性 {#volume-attribute}

“音量”属性虽然高于“1”的值，但并不定义声音响度的百分比，而是确定在最大音量下可以听到声音的距离（以块为单位）。

公式为 v * 16 = 最大音量可听距离。例如 volume 为 1 时，声源周围 16 格内可听到最大音量；设为 20 时，这个半径就是 320 格（20 * 16）。

当该值在0和1之间时，声音仍以16块半径播放，但音量减小，0.1为正常音量的10％，0.4为正常音量的40％，依此类推。

### Emitter 属性 {#emitter-attribute}

如果设置了发射器，则声音播放将从发射器实体的位置而不是设置的位置动态发生。

| 发射源 | 说明 |
| --- | --- |
| CASTER | 调用此机制的实体 |
| TARGET | 此机制的目标实体 |
| BOTH | 分别在施法者和目标处播放，共播放两次 |
| AUDIENCE | 将机制的[接收对象](../audience.md)用作声音发出者 |

## 示例 {#examples}

```yaml
EndermanAttack:
  Skills:
  - sound{s=entity.enderman.scream} @self
```

##  {#section}

下面的示例播放资源包中的声音。可以在[此处](https://mcmodels.net/guides/4-sounds)找到有关添加自定义声音的良好指南。

```yaml
BossSoundEffect:
  Skills:
  - sound{s=yoursound:example.sound.name_1} @self
```

## 别名 {#aliases}

- effect:sound
- s
- e:sound
- e:s
