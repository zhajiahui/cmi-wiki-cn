---
title: Consume
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/consume
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Consume {#consume}

## 说明 {#description}

对每个目标实体造成指定伤害，并按这种方式造成的伤害为施法生物治疗。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| damage | d,dmg | 要造成的伤害量。 | 1 |
| heal | h | 每个受到伤害的生物所对应的治疗量。 | 1 |

> 此机制继承 [Damage](damage.md) 机制的所有*可继承*属性。

## 示例 {#examples}

会消耗掉附近所有的僵尸，每杀死一个僵尸就能治疗 Boss 20 hp。

```yaml
  Skills:
  - consume{d=1000;h=20} @MobsInRadius{type=ZOMBIE;r=20}
```
