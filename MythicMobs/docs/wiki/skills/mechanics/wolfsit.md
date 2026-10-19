---
title: Wolfsit
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/wolfsit
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Wolfsit {#wolfsit}

## 说明 {#description}

设置目标狼的坐姿。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| state | sit, value | 狼的状态。True = 坐下，False = 站立 | true |

## 示例 {#examples}

```yaml
# Standing
- wolfSit{state=false} @self ~onInteract
```

```yaml
# Sitting
- wolfSit{state=true} @self ~onInteract
```
