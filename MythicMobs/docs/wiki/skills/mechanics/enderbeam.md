---
title: Ender Beam
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/EnderBeam
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Ender Beam {#ender-beam}

## 说明 {#description}

召唤一颗末影水晶，向目标发射光束。

**警告：此效果会创建末地水晶，水晶可被引爆并破坏方块。**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| duration | d | 效果生效的时间，单位为刻。 | 60 |
| yoffset | y, yo | 相对于施法生物的默认竖直偏移。 | 0 |

## 示例 {#examples}

```yaml
EnderBeamSkill:
  Skills:
  - effect:enderbeam{d=100;y=2} @target
```

## 别名 {#aliases}

- effect:enderbeam
