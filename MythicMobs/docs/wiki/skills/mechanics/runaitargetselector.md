---
title: Runaitargetselector
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/runaitargetselector
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Runaitargetselector {#runaitargetselector}

## 说明 {#description}

更改寻路 AI 的攻击目标。并非所有实体都支持所有目标。要重新设置 AI，先使用 clear，再通过 runaitargetselector 添加所需目标。与生物配置不同，这个机制每次只能指定一个目标；只要不使用 clear，新目标就会追加到已有目标末尾。

可用目标列表可以在[此处](../../mobs/custom-ai.md#ai-target-selectors)找到

> **这是一个无目标机制，受影响的实体将始终是施法者**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| target | aitargetselector, s, string, targetselector, goal, g | 要追加的目标选择器 |  |

## 示例 {#examples}

```yaml
TargetPossibleThreats:
  Skills:
  - runaitargetselector{target=clear}
  - runaitargetselector{target=players}
  - runaitargetselector{target=monsters}
```

## 别名 {#aliases}

- aitarget
