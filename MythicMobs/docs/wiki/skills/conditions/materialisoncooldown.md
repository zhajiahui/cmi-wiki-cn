---
title: Material Is On Cooldown
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/MaterialIsOnCooldown
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Material Is On Cooldown {#material-is-on-cooldown}

## 说明 {#description}

检查目标玩家的指定材料是否处于冷却状态。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | mat, m | 要检查的材质。 | enderpearl |

## 示例 {#examples}

```yaml
  TargetConditions:
  - materialIsOnCooldown{mat=STONE} true
```

## 别名 {#aliases}

- materialCooldown
- matCooldown
