---
title: Mobs In Radius
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/MobsInRadius
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mobs In Radius {#mobs-in-radius}

## 说明 {#description}

选中施法者周围指定半径内，所有属于指定类型的 MythicMobs 或原版生物覆盖实体

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |
| types | type, t | 目标 MythicMobs 的类型，可以是列表。 |  |
| checkiftemplate | cit | 是否改为检查生物的模板，而不是生物的内部名称。 | false |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - ignite @MobsInRadius{r=10;types=IncredibleZombie,SpookyScarySkeleton}
```

## 别名 {#aliases}

- MIR
- mobs
