---
title: "高级属性"
source_url: "https://wiki.itemsadder.com/adding-content/player-emotes/advanced-properties"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 高级属性

你还可以为表情指定一些特殊属性。\
为此，你需要创建一个新的 `.yml` 文件，如果你不需要覆盖这些属性，则表情不需要此文件。

`hide_equipment`: 是否需要隐藏玩家的某个装备部分。

`can_player_move`: 玩家是否可以在动画期间移动。

`cancel_conditions`: 会使动画停止的各种动作。

`stop_sounds`：取消表情动作时，停止所有已播放的声音。

`skip_emote_end`：取消时中断表情动作。

`background_music`：在表情动作期间播放歌曲，可选择循环播放。

## 示例

```yaml
info:
  namespace: test_emotes
emotes:
  example_1:
    id: example_1
    enabled: false
    hide_equipment:
      helmet: true
      mainhand: true
      offhand: true
    can_player_move: false
  example_2:
    id: example_2
    cancel_conditions:
      sneak: false
      take_damage: false
      deal_damage: false
      in_air: false
    hide_equipment:
      helmet: false
      mainhand: false
      offhand: false
    can_player_move: true
    on_stop:
      stop_sounds: true
      skip_emote_end: true
    background_music:
      sound:
        name: test_emotes:my_song
      repeat_interval_seconds: 5

```
