---
title: Smoke
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Smoke
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Smoke {#smoke}

## 说明 {#description}

在目标位置产生一股烟雾。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| direction | dir, d | 效果播放的方向，可以是 1 到 4 的整数 | 4 |

## 示例 {#examples}

```yaml
SmokeMonster:
  Type: ZOMBIE
  Skills:
  - smoke @target ~onTimer:10
  - smoke{direction=2} @self ~onAttack
```

## 别名 {#aliases}

- effect:smoke
- e:smoke
