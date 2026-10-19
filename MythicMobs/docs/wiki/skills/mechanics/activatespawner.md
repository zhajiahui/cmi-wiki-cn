---
title: Activatespawner
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/activatespawner
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Activatespawner {#activatespawner}

## 说明 {#description}

激活 MythicMobs [刷怪点](../../spawners.md)，使其生成生物。不会覆盖刷怪点上设置的任何条件或选项。

> 最好配合将刷怪点的 `useTimer` 属性设置为
> `false` 一起使用。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| spawners | spawner, s | 要激活的刷怪器名称。使用相应语法时，也接受分组和通配符。 | NONE |

## 示例 {#examples}

这将激活名为“BossAdd”的刷怪点

```yaml
    Skills:
    - activatespawner{spawner=BossAdd}
```

##  {#section}

此示例将激活“城堡”组中的所有刷怪点

```yaml
    Skills:
    - activatespawner{spawner=g:Castle}
```

##  {#section-2}

此示例将激活以“DungeonBoss1Spawner”开头的所有刷怪点（即DungeonBoss1Spawner1、DungeonBoss1Spawner2等）

```yaml
    Skills:
    - activatespawner{spawner=DungeonBoss1Spawner*}
    - ...
```

## 别名 {#aliases}

- as
