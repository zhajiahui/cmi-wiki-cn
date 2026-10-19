---
title: On Shoot
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onShoot
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Shoot {#on-shoot}

## 说明 {#description}

生物发弹射物射物时执行技能。例如，持弓的骷髅会射箭，恶魂、烈焰人或末影龙会发射某种火球。

> 关联的 [@trigger](../targeters/trigger.md) 是施法者

| [已实现的占位符](../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.bow-tension>` |

## 实现示例 {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onShoot)
- [MythicRPG](https://wiki.mythiccraft.io/mythicrpg/Skills/Triggers/onShoot)

## 示例 {#examples}

```yml
EXAMPLE_MOB:
  Type: SKELETON
  Skills:
    # sends a message to all the players in the world
    # when the skeleton shoots from a bow
    - message{m=I SHOT AN ARROW} @World ~onShoot
```

## 别名 {#aliases}

- onBowShoot
- onShootBow
