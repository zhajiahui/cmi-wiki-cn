---
title: Haspermission
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/haspermission
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Haspermission {#haspermission}

## 说明 {#description}

此条件检查目标玩家是否有权限。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| permission | p | 要检查的权限。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - haspermission{p=permission.node.here} true
```

```yaml
  TargetConditions:
  - haspermission{p=permission.node.here} true
```

```yaml
  TriggerConditions:
  - haspermission{p=permission.node.here} true
```

## 别名 {#aliases}

- permission
