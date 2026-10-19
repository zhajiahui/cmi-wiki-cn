---
title: Globalcooldown
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/globalcooldown
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Globalcooldown {#globalcooldown}

## 说明 {#description}

全局冷却技能可让你设置施法者的全局冷却时间，如果你希望生物的能力具有全局、整体共享的冷却时间，则与 [offgcd](../conditions/offgcd.md) 条件结合使用。这对于允许生物一次仅使用一项技能而不是通过为生物使用的每个技能提供冷却时间来使用多个技能非常有用。

> 这是一个无目标机制，受影响的实体将始终是施法者

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| ticks | t | 将 GCD 设置为多少刻。 | 20 |

## 示例 {#examples}

该技能会触发40的全局冷却时间，在此期间该技能和所有其他使用[offgcd](../conditions/offgcd.md)条件的技能将无法使用。

```yaml
IceBolt:
  Conditions:
  - offgcd
  Skills:
  - gcd{ticks=40}
```

## 别名 {#aliases}

- gcd
- setgcd
- setglobalcooldown
