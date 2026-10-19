---
title: Percentdamage
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/percentdamage
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Percentdamage {#percentdamage}

## 说明 {#description}

造成相当于玩家最大生命值百分比的伤害，其中 1 为 100%。继承[伤害](damage.md)机制的所有属性。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| percent | p | 对目标造成伤害的百分比。 | 0.1 |
| currentHealth | current, c, ch | 使用原始生命值还是当前生命值计算百分比。 | false |

> 该机制继承了[伤害](damage.md)机制的所有属性
>

> > `amount` 属性被忽略

## 示例 {#examples}

伤害目标最大生命值的一半 (50%)。

```yaml
  Skills:
  - damagepercent{percent=0.5}
```

## 别名 {#aliases}

- damagepercent
- percentdamage
