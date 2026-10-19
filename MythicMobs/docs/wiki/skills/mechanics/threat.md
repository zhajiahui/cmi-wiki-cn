---
title: Threat
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/threat
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Threat {#threat}

## 说明 {#description}

修改生物对目标的仇恨值。需要施放生物启用[仇恨表](../../mobs/threattables.md)才能产生任何效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 给予目标的仇恨值，可以为负数。 | 1 |
| mode | m | 运算的[模式](threat.md#mode-attribute) | add |

### Mode 属性 {#mode-attribute}

| 模式 | 别名 | 说明 |
| --- | --- | --- |
| add |  | 为目标实体增加 `amount` 仇恨值 |
| remove |  | 从目标实体移除 `amount` 仇恨值 |
| multiply |  | 将对目标实体的仇恨值乘以 `amount` |
| divide |  | 将对目标实体的仇恨值除以 `amount` |
| set |  | 将对目标实体的仇恨值设为 `amount` |
| reset | delete | 移除对目标实体的所有仇恨值 |
| forcetop | force, top, topthreat, taunt | 给予目标足够的仇恨值，使其升至仇恨列表首位 |

## 示例 {#examples}

此示例会将最近玩家的仇恨值设置为非常高的值。

```yaml
Fixate:
  Skills:
  - threat{amount=10000} @NearestPlayer ~onSpawn
```

## 别名 {#aliases}

- threatchange
- threatmod
