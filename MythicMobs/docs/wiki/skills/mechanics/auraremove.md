---
title: Auraremove
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/auraremove
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Auraremove {#auraremove}

## 说明 {#description}

移除目标的光环。

你可以通过[光环](aura.md)机制的`DoEndSkillOnTerminate`属性来决定光环是否执行其`onEnd`元技能。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| auraName | aura, b, buff, buffname, debuff, debuffname, n, name | 光环名称。 | default |
| stacks | s | 层数。 | 最大层数 |

### Aura 属性 {#aura-attribute}

你可以指定 `ANY` 作为属性值，以移除目标上的所有光环

## 示例 {#examples}

```yaml
  Skills:
  - auraremove{aura=Ice;stacks=10} @self ~onTimer:200
```

## 别名 {#aliases}

- removeaura
- removebuff
- removedebuff
