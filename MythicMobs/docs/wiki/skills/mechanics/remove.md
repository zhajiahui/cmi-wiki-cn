---
title: Remove
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/remove
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Remove {#remove}

## 说明 {#description}

将目标实体从存在中移除。对玩家不起作用。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onRemoveSkill | onRemove, then | 实体被移除后执行的元技能 |  |

## 示例 {#examples}

该生物将在生成后 10 秒消失：

```yaml
  Skills:
  - remove{delay=200} @self ~onSpawn
```

当右键单击该技能时，该技能会立即使生物消失。

```yaml
  Skills:
  - remove @self ~onInteract
```

## 别名 {#aliases}

- delete
