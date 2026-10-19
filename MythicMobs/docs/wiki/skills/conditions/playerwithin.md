---
title: Playerwithin
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/playerwithin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Playerwithin {#playerwithin}

## 说明 {#description}

检查目标半径内是否有玩家。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distance | d | 检查范围的半径。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - playerwithin{d=10} true
```

## 别名 {#aliases}

- playerswithin
