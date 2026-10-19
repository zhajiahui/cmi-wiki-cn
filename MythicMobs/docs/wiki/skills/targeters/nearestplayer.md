---
title: Nearest Player
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/NearestPlayer
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Nearest Player {#nearest-player}

## 说明 {#description}

瞄准半径内最近的玩家

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - settarget @NearestPlayer{r=10}
```
