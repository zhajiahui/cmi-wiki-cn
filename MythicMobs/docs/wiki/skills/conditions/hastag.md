---
title: Hastag
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hastag
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Hastag {#hastag}

## 说明 {#description}

测试目标是否有记分板标签

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| tag | t | 要检查的标签。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - hastag{t=KilledBoss1} true
```

```yaml
  TargetConditions:
  - hastag{t=PuzzleRoom1Solved} true
```

## 别名 {#aliases}

- hasScoreboardTag
