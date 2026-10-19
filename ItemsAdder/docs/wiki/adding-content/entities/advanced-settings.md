---
title: "高级设置"
source_url: "https://wiki.itemsadder.com/adding-content/entities/advanced-settings"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 高级设置

可在 `ItemsAdder/config.yml` 中找到自定义实体的高级设置。

```yaml
entities:
  max-furniture-vehicles-per-chunk: 30
  max_furniture_per_chunk: 20
  custom_entities:
    enabled: true
    emotes: true
    max_per_chunk: 5
    expert_users:
      delay_packets: false
      extract_emotes_shaders: true
  furniture:
    auto_convert_to_item_display: false
```

### `delay_packets`

此选项通过延迟发送数据包降低 CPU 处理负担，但在部分服务器上会使动画不流畅。

了解其副作用之前，不应启用此项。

`max_per_chunk`

每个区块允许的实体数量上限。

`emotes`

启用或禁用表情动作。需要执行 `/iazip`，才能从资源包中移除相关数据。

`extract_emotes_shaders`

设置是否包含表情动作着色器。如果要自行编写着色器，可以禁用此项；不建议新手这样做。

