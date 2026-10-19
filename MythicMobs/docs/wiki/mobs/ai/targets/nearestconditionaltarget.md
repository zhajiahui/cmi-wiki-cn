---
title: Nearestconditionaltarget
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/nearestconditionaltarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Nearestconditionaltarget {#nearestconditionaltarget}

## 说明 {#description}

让生物根据条件选择目标。

需要 Mythic Mobs Premium。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| interval | int,i | 决定此 AI 行为的执行概率。 | 0 |
| mustsee | ms | 生物是否必须能够看见目标。 | true |
| mustreach | mr | 生物是否必须能够到达目标。 | false |
| conditions | c, cond, targetconditions | 使用的条件。 |  |

## 示例 {#examples}

会让生物以手持铁锭的实体为目标。

```yaml
ExampleMob:
  Type: ZOMBIE
  AITargetSelectors:
    - clear
    - nearestconditionaltarget{mr=true;ms=true;conditions=[ - holding{m=IRON_INGOT} true ]}
```

## 别名 {#aliases}

- nearestconditional
- nearestif
