---
title: Enchanting Experience
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EnchantingExperience
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Enchanting Experience {#enchanting-experience}

## 说明 {#description}

检查目标玩家拥有的经验值。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| level | l, amount, a | 按 0 到 1 的范围检查距离下一级所缺少的经验点数。0 表示“没有进度”，1 表示“下一级”。接受范围值。 | 0 |

## 示例 {#examples}

```yaml
  TargetConditions:
  - enchantingExperience{l=>0.2} true
```

## 别名 {#aliases}

- enchantingExp
- enchantExperience
- enchantExp
