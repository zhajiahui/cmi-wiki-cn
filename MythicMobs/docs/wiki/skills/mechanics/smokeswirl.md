---
title: Smoke Swirl
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SmokeSwirl
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Smoke Swirl {#smoke-swirl}

## 说明 {#description}

在目标实体或位置产生烟雾漩涡。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| duration | d | 旋涡持续的间隔次数 | 5 |
| interval | i | 每次喷出烟雾之间的间隔，以刻为单位 | 1 |

## 示例 {#examples}

```yaml
SmokeSwirlSkill:
  Skills:
  - smokeswirl{duration=10;interval=10} @TargetLocation
```

## 别名 {#aliases}

- effect:smokeswirl
- e:smokeswirl
