---
title: Mobs Near Origin
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/MobsNearOrigin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mobs Near Origin {#mobs-near-origin}

## 说明 {#description}

选中原点周围指定半径内，所有属于指定类型的 MythicMobs 或原版生物覆盖实体

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |
| types | type, t | 目标 MythicMobs 的类型，可以是列表。 |  |

## 示例 {#examples}

该技能结束时将点燃其周围半径范围内给定类型的所有生物

```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onEnd=[
      - ignite @MobsNearOrigin{r=10;types=IncredibleZombie,SpookyScarySkeleton}
    ]}
```

## 别名 {#aliases}

- mobssnearsource
