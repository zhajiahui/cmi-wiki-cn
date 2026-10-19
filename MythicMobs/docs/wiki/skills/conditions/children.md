---
title: Children
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/children
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Children {#children}

## 说明 {#description}

检查施法者有多少个子实体。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要检查的子实体数量。可接受范围值。 | 1 |

## 示例 {#examples}

```yaml
  Conditions:
  - children{a=1} true
```

```yaml
  Conditions:
  - children{a=>2} true
```

---

这个例子展示了一个父生物，它会召唤子生物，直到达到 3 总数，然后停止，直到 1 被杀死或消失

```yaml
children_overflow_mob:
  Type: ARMOR_STAND
  Skills:
  - skill{s=children_summon_more} @self ~onTimer:20
children_mob:
  Type: PIG
```

```yaml
children_summon_more:
  Conditions:
  - children{a=<3} orelsecast children_too_many
  Skills:
  - summon{m=children_mob;amount=1}
  - delay 0
  - message{m="<green>Child summoned, there are now <caster.children.size> children!"} @PIR{r=10}

children_too_many:
  Skills:
  - message{m="<red>No children summoned, already 3 or more!"} @PIR{r=10}
```

> *此示例由 slipperysmurf 友情提供*
