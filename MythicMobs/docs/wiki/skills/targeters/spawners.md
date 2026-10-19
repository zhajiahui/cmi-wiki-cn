---
title: 刷怪点
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Spawners
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 刷怪点

# Spawners {#spawners}

## 说明 {#description}

定位指定刷怪点的位置

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| spawners | spawner, s | 刷怪器名称。可以是简单名称、分组（`g:groupname`），或包含通配符（`Spawner*` 会选择 *Spawner1*、*Spawner2*、*Spawner3*……）。 |  |

## 示例 {#examples}

```yaml
ExampleSkill_SingleSpawner:
  Skills:
  - effect:particles @Spawner{s=TestSpawner}
```

```yaml
ExampleSkill_Group:
  Skills:
  - effect:particles @Spawner{s=g:ExampleSpawnerGroup}
```

```yaml
ExampleSkill_WildCard:
  Skills:
  - effect:particles @Spawner{s=ForestSpawner_*}
```
