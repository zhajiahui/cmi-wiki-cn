---
title: Hologram
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/hologram
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Hologram {#hologram}

## 说明 {#description}

在目标位置生成全息图。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| text | t | 要显示的文字。 | Hologram Text Missing |
| stay | time, staytime | 全息显示的持续时间，单位为刻。 | 100 |

## 示例 {#examples}

当右键单击生物时，在生物上方创建一个全息图，显示 100 游戏刻。

```yaml
  Skills:
  - holo{text="Example Text";time=100} @selflocation{y=1.6} ~onInteract
```

## 别名 {#aliases}

- summonhologram
- holo
