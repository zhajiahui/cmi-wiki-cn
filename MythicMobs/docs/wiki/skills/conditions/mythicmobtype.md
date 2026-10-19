---
title: Mythicmobtype
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mythicmobtype
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Mythicmobtype {#mythicmobtype}

## 说明 {#description}

检查目标生物的MythicMob类型

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | types, t | 要匹配的 MythicMob 类型列表。 |  |
| exactmatch | em | 指定类型是否必须与 MythicMob 的名称完全匹配。此属性设为 `false` 时，即使被检测实体的 MythicMob 名称仅*包含*任意一个指定类型，此条件也会成立。 | true |

## 示例 {#examples}

```yaml
  Conditions:
  - mythicmobtype{t=CoolZombie,IceZombie,SnowZombie} true
```

```yaml
  TargetConditions:
  - mythicmobtype{t=HotZombie,LavaZombie,FireZombie} true
```

## 别名 {#aliases}

- mmType
