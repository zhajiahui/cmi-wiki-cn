---
title: Mount
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/mount
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mount {#mount}

## 说明 {#description}

使施法生物召唤指定 MythicMob 并骑乘它。施法者同时成为新生物的[所有者](../targeters/owner.md)和[父实体](../targeters/parent.md)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t, mob, m | 要召唤的 MythicMob 类型。 |  |
| stack | s | 召唤的生物是否堆叠到现有的被骑乘实体之上。 | false |

### Type 属性 {#type-attribute}

type 中定义的 MythicMob 必须是有效的 MythicMob 类型（并且区分大小写）。如果指定了无效类型，技能可能会抛出错误。

## 示例 {#examples}

此示例将召唤“UndeadMount”类型的Mythic 生物并让施法者骑乘它。

```yaml
CallSkeletalHorse:
  Skills:
  - mount{type=UndeadMount}
```

## 别名 {#aliases}

- vehicle
