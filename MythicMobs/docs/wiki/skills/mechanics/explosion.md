---
title: Explosion
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/explosion
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Explosion {#explosion}

## 说明 {#description}

在目标实体或位置造成爆炸。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| yield | y | 爆炸强度，即威力。 | 0.013 |
| blockdamage | bd | (true/false) 爆炸是否破坏方块。 | false |
| fire | f,ft | (true/false) 爆炸后是否留下火。 | false |

> 警告
> Blockdamage 似乎不会遵守 WorldGuard 区域等保护限制，使用风险自行承担。

## 示例 {#examples}

```yaml
ExplosiveBlast:
  Skills:
  - explosion{yield=4} @target
```

## 别名 {#aliases}

- explode
