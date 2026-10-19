---
title: On Shoot
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/OnShoot
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Shoot {#on-shoot}

## 说明 {#description}

将光环组件应用于目标，当目标用弓射击时会触发技能。可以使用任意[光环](../aura.md)属性

| [已实现的占位符](../../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.bow-tension>` |

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onShootSkill | onshoot, osh, onbowshoot, onbowshootskill | 实体射击时执行的技能。 |  |
| cancelEvent | cE | 是否取消触发光环的事件。 | false |

## 示例 {#examples}

```yaml
  Skills:
    - aura{auraName=fireball_bow;duration=200;charges=5;components=[
      - onShoot{onShoot=[ shootfireball ];cancelEvent=true} @self
      ]} @self
```

在此示例中，施法者接下来的 5 次射箭会发射火球，而不是箭。

## 别名 {#aliases}

- onbowshoot
