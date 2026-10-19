---
title: Totem Of Undying
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/TotemOfUndying
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Totem Of Undying {#totem-of-undying}

## 说明 {#description}

播放图腾复活玩家的效果，并可以选择指定要从资源包中使用的CustomModelData。

> 你无法禁用播放的声音

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| model | m | 显示图腾时使用的 CustomModelData |  |

## 示例 {#examples}

```yaml
PlayTotemEffect:
  Skills:
  - totemofundying{model=2} @PIR{r=5}
```

## 别名 {#aliases}

- totemresurrection
- effect:totemresurrection
- e:totemresurrection
- totemresurrectioneffect
- totemofundying
- e:totemofundying
- totemeffect
