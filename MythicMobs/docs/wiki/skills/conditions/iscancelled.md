---
title: Is Cancelled
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsCancelled
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Is Cancelled {#is-cancelled}

## 说明 {#description}

检查当前触发事件是否被取消。

当技能链中的先前机制取消了事件（例如通过 `cancelevent`），或者当基础 Bukkit 事件报告自身已取消时，这就是   true  。它对于触发流程中的中链检查最有用，例如在另一个机制可能取消事件后的`~onDamaged`。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| value | val, v, boolean, bool, b | 要匹配的取消状态。 | true |

## 示例 {#examples}

```yaml
  Conditions:
  - iscancelled{value=true} true
```

## 别名 {#aliases}

- isCanceled
- cancelled
- canceled
