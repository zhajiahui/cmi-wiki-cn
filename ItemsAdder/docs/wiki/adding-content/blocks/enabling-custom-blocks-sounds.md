---
title: "启用自定义方块声音"
source_url: "https://wiki.itemsadder.com/adding-content/blocks/enabling-custom-blocks-sounds"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 启用自定义方块声音

每次更改这些设置时，您都必须运行 `/iazip` 以重新生成资源包。

要启用自定义方块声音，您必须在 `config.yml` 中启用这些选项。

```yaml
  custom_blocks_sounds_patch:
    enabled: true
    step:
      enabled: true
      allow_non_player: true
    other: true
```

### `enabled`

启用整个模块。

### `step.enabled`

* `true`
  * 此选项将启用每次实体走在自定义方块上时播放自定义 `step` 声音。\
    \
    注意：它还会替换资源包中木材和石头的原版 `step` 声音。\
    (此信息仅对专业用户有用).
* `false`
  * 此选项不会让实体走过自定义方块时播放自定义脚步声。\
    \
    注意：它不会替换资源包中的原版木头和石头声音。\
    (此信息仅对专业用户有用).

### `other.enabled`

* `true`
  * 此选项将在各种情况下启用播放自定义声音：`break`, `fall`, `hit`, `place`.\
    \
    注意：它还会替换资源包中木材和石头的原版 `break`, `fall`, `hit`, `place` 声音。\
    (此信息仅对专业用户有用).
* `false`
  * 此选项不会启用在各种情况下播放自定义声音：`break`, `fall`, `hit`, `place`.\
    \
    注意：它不会替换资源包中的原版木头和石头声音。\
    (此信息仅对专业用户有用).

### `step.allow_non_player`

* `true`
  * 此选项将启用任何非玩家实体播放自定义 `step` 声音。\
    如果您担心由于调用此代码的频率高而导致服务器性能下降，您应该禁用此选项。\
    此功能的编写考虑了性能，并经过基准测试；不过，一些服务器管理员可能仍然特别谨慎，所以我加入了这个选项。
* `false`
  * 此选项不会启用任何非玩家实体播放自定义 `step` 声音。
