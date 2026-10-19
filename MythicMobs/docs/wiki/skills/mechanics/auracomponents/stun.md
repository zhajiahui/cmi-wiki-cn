---
title: Stun
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/Stun
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Stun {#stun}

## 说明 {#description}

将目标暂时固定在适当的位置。

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><path d="M21.73 18 13.73 4a2 2 0 0 0-3.46 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"></path><path d="M12 9v4"></path><path d="M12 17h.01"></path></svg>Warning

此机制可能会导致 Spigot 踢玩家 (`PlayerName moved wrongly!`)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| stopai | ai | 眩晕期间移除实体的 AI。 | false |
| gravity | g | 眩晕期间移除目标的重力（1.9+）。 | false |
| facing | face, f | 为 false 时，实体在眩晕期间无法旋转或环顾四周。 | false |
| noknockback | nokb, kb | 为 true 时，实体在眩晕期间无法被击退。 | false |

## 示例 {#examples}

使目标昏迷3秒，在此期间目标无法旋转。

```yaml
ExampleSkill:
  Skills:
  - aura{d=60;components=[
    - stun{f=false}    
    ]} @target
```

## 别名 {#aliases}

- stunned
